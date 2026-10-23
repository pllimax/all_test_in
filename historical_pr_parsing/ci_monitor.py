#!/usr/bin/env python3
"""
NPU CI 流水线监控 Agent
拉取 sgl-project/sglang 的 pr-test-npu.yml workflow runs，
分析各 job 状态、下载失败日志做 AI 归因，生成 ci_report.md 并推送到报告仓库。
（仅 CI 流水线部分，不涉及 PR 分析）
"""

import json
import os
import re
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

import requests
import urllib3

# 禁用 SSL 警告（内网环境可能需要关闭证书验证）
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 强制 stdout/stderr 使用 UTF-8（Windows 终端默认 GBK 无法编码 emoji，会抛 UnicodeEncodeError）
for _s in (sys.stdout, sys.stderr):
    if hasattr(_s, "reconfigure"):
        _s.reconfigure(encoding="utf-8", errors="replace")


# 加载同目录 .env（若存在），密钥一律放 .env，不写入代码
def _load_dotenv():
    env_file = Path(__file__).resolve().parent / ".env"
    if not env_file.exists():
        return
    for _line in env_file.read_text(encoding="utf-8").splitlines():
        _line = _line.strip()
        if not _line or _line.startswith("#") or "=" not in _line:
            continue
        _k, _, _v = _line.partition("=")
        os.environ.setdefault(_k.strip(), _v.strip().strip('"').strip("'"))


_load_dotenv()

# ============================================================
# 配置区 — 按需修改
# ============================================================

# SSL 证书验证：内网环境如遇到 SSL 错误，设为 False
# SSL_VERIFY = os.environ.get("SSL_VERIFY", "true").lower() not in ("false", "0", "no")
SSL_VERIFY = (
    False  # 注意：必须是布尔值。传字符串 "false" 会被 requests 当作 CA 证书路径
)

# HTTP 代理（留空则不使用代理）
HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
HTTPS_PROXY = os.environ.get("HTTPS_PROXY", "")

# GitHub Personal Access Token（可选，提高 API 限额到 5000次/小时）
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# 目标仓库：sgl-project/sglang
TARGET_OWNER = "sgl-project"
TARGET_REPO = "sglang"

# 报告推送的目标仓库（如需认证，在 .env 的 REPORT_REMOTE 中内嵌 token）
REPORT_REMOTE = os.environ.get(
    "REPORT_REMOTE",
    "https://github.com/pllimax/all_test_in.git",
)
REPORT_BRANCH = "pr_report_save"

# AI API 配置（DeepSeek / OpenAI 兼容接口）
AI_API_KEY = os.environ.get("AI_API_KEY", "")
AI_API_BASE = os.environ.get("AI_API_BASE", "https://api.deepseek.com")
AI_MODEL = os.environ.get("AI_MODEL", "deepseek-chat")

# 本脚本所在目录（部署后自动指向 ci_monitor 目录）
SCRIPT_DIR = Path(__file__).resolve().parent
REPORTS_DIR = SCRIPT_DIR / "npu_reports"

# ============================================================
# CI 专用状态与阈值
# ============================================================

CI_STATE_FILE = SCRIPT_DIR / "analyzed_ci_runs.json"
CI_RUNS_TO_SCAN = 500  # 拉取最近完成的 run 数量上限（安全上限，防止极端海量）
CI_RUNS_WINDOW_DAYS = 1  # 分析“前一天”（北京时间）完成的 run；设为 0 则关闭窗口过滤，退化为最近 CI_RUNS_TO_SCAN 条
CI_TZ = timezone(timedelta(hours=8))  # 北京时间（窗口/统计按此区）
CI_MIN_RUN_DURATION_MIN = 5  # run 总耗时 < 此值视为未跑到测试阶段，跳过
CI_MIN_JOB_DURATION_MIN = 0.5  # job < 此值视为 skip（check-changes/pr-gate 等）
CI_CATCHUP_MAX_DAYS = 7  # 漏采自动回补的最大天数（防止停机过久导致单次运行超长）

# ============================================================
# GitHub API 辅助
# ============================================================


def _request_kwargs():
    """构建 requests 公共参数"""
    kwargs = {"verify": SSL_VERIFY, "timeout": 30}
    proxies = {}
    if HTTP_PROXY:
        proxies["http"] = HTTP_PROXY
    if HTTPS_PROXY:
        proxies["https"] = HTTPS_PROXY
    if proxies:
        kwargs["proxies"] = proxies
    return kwargs


def _http_get_with_retry(url, *, max_retries=3, backoff=1.5, **kwargs):
    """GET with retry on 429/5xx/connection errors. Returns the response."""
    last_exc = None
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, **kwargs)
            if resp.status_code in (429, 500, 502, 503, 504):
                last_exc = RuntimeError(f"HTTP {resp.status_code}")
                time.sleep(backoff * (attempt + 1))
                continue
            return resp
        except (requests.ConnectionError, requests.Timeout) as e:
            last_exc = e
            time.sleep(backoff * (attempt + 1))
    if last_exc:
        raise last_exc
    raise RuntimeError("retry exhausted")


def github_headers():
    headers = {"Accept": "application/vnd.github+json"}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    return headers


def api_get(url, params=None):
    resp = _http_get_with_retry(
        url, headers=github_headers(), params=params, **_request_kwargs()
    )
    resp.raise_for_status()
    return resp.json()


def fetch_pr_by_sha(sha):
    """通过 commit SHA 搜索对应的 PR"""
    url = "https://api.github.com/search/issues"
    params = {
        "q": f"repo:{TARGET_OWNER}/{TARGET_REPO} type:pr sha:{sha}",
        "per_page": 1,
    }
    try:
        data = api_get(url, params=params)
        items = data.get("items", [])
        if items:
            pr = items[0]
            return {
                "number": pr["number"],
                "title": pr["title"],
                "html_url": pr["html_url"],
            }
    except Exception:
        pass
    return None


# ============================================================
# CI 状态持久化
# ============================================================


def load_ci_state():
    if CI_STATE_FILE.exists():
        return json.loads(CI_STATE_FILE.read_text(encoding="utf-8"))
    return {}


def save_ci_state(state):
    CI_STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8"
    )


# ============================================================
# CI runs 拉取与过滤
# ============================================================


def ci_window_days():
    """本次应分析的天数：默认 CI_RUNS_WINDOW_DAYS；若上次成功运行距今超过
    1 天（漏采），自动扩大窗口回补缺失日期，上限 CI_CATCHUP_MAX_DAYS。
    返回 0 表示关闭窗口过滤。"""
    if CI_RUNS_WINDOW_DAYS <= 0:
        return 0
    today0 = datetime.now(CI_TZ).replace(hour=0, minute=0, second=0, microsecond=0)
    last = load_ci_state().get("_last_success_date")
    if last:
        try:
            gap = (today0.date() - date.fromisoformat(last)).days
        except ValueError:
            gap = 0
        return min(max(CI_RUNS_WINDOW_DAYS, gap), CI_CATCHUP_MAX_DAYS)
    return CI_RUNS_WINDOW_DAYS


def fetch_ci_runs():
    """获取 pr-test-npu.yml 在“前一天”（北京时间）内完成的 workflow runs。

    默认窗口为北京时间 [昨天00:00, 今天00:00)；CI_RUNS_TO_SCAN 保留为极端海量时的安全上限。
    窗口关闭（CI_RUNS_WINDOW_DAYS=0）时退化为拉取最近 CI_RUNS_TO_SCAN 条 completed run。
    """
    url = f"https://api.github.com/repos/{TARGET_OWNER}/{TARGET_REPO}/actions/workflows/pr-test-npu.yml/runs"

    # 时间窗口（北京时间）；漏采时 ci_window_days() 自动扩大以回补
    start_utc = end_utc = None
    window_days = ci_window_days()
    if window_days > 0:
        bj_now = datetime.now(CI_TZ)
        today0 = bj_now.replace(hour=0, minute=0, second=0, microsecond=0)
        start_utc = (today0 - timedelta(days=window_days)).astimezone(
            timezone.utc
        )
        end_utc = today0.astimezone(timezone.utc)

    all_runs = []
    page = 1
    stop = False
    while not stop and len(all_runs) < CI_RUNS_TO_SCAN:
        # 注意：GitHub API 带 status=completed 过滤时返回顺序不稳定（实测可能从最旧开始），
        # 因此不传该参数（默认按 created_at 倒序返回最新 run），改为在本地过滤 completed
        data = api_get(url, params={"per_page": 100, "page": page})
        runs = data.get("workflow_runs", [])
        if not runs:
            break
        for r in runs:
            if r.get("status") != "completed":
                continue
            if start_utc is not None:
                created = datetime.fromisoformat(r["created_at"].replace("Z", "+00:00"))
                if created < start_utc:
                    # 已翻到窗口之前（列表按 created_at 倒序），提前终止
                    stop = True
                    break
                if created >= end_utc:
                    continue  # 今天 0 点之后新触发的 run，不在“昨天”窗口内
            all_runs.append(r)
            if len(all_runs) >= CI_RUNS_TO_SCAN:
                break
        page += 1
    return all_runs[:CI_RUNS_TO_SCAN]


# ============================================================
# 日志分析与 AI 归因
# ============================================================


def ai_analyze_ci_log(job_name, log_text):
    """将日志尾部 + 关键错误片段发给 AI 分析失败原因"""
    if not AI_API_KEY:
        return {
            "category": "未配置",
            "summary": "AI_API_KEY 未配置，跳过分析",
            "detail": "",
        }

    # 截取：日志开头2000字 + 最后5000字（错误通常在末尾）
    if len(log_text) > 8000:
        log_snippet = log_text[:2000] + "\n...(中间省略)...\n" + log_text[-5000:]
    else:
        log_snippet = log_text

    prompt = f"""你是 sglang NPU CI 调试助手。以下是一个失败的 GitHub Actions 作业的日志。
请用**中文**简要分析失败原因（不超过100字），并给出分类：

作业名称: {job_name}

日志:
{log_snippet}

请用JSON格式回答：
{{"category": "性能回归|精度回归|环境问题|代码错误|超时|其他", "summary": "一句话原因（中文）", "detail": "具体说明（中文，100字以内）"}}"""

    try:
        resp = requests.post(
            f"{AI_API_BASE}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {AI_API_KEY}",
                "Content-Type": "application/json",
            },
            json={
                "model": AI_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 300,
            },
            **_request_kwargs(),
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"].strip()
        json_match = re.search(r"\{[^{}]*\}", content, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        return {"category": "未知", "summary": content[:100], "detail": content[:100]}
    except Exception as e:
        return {
            "category": "AI调用失败",
            "summary": str(e)[:100],
            "detail": str(e)[:100],
        }


def extract_log_errors(log_text):
    """从日志中提取关键错误片段和测试用例结果（不用AI，做预截取）"""
    lines = log_text.split("\n")
    result = {
        "assertions": [],
        "tracebacks": [],
        "final_result": "",
        "failed_tests": [],
        "all_tests": [],
    }

    def strip_line(line):
        # 去掉 GitHub Actions 时间戳前缀（如 2026-08-23T15:48:32.6520241Z）
        s = re.sub(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(\.\d+)?Z\s*", "", line)
        # 去掉日志乱码图标前缀
        s = re.sub(r"^[\u00e2\u0080-\u00a0\s]+", "", s)
        return s.strip()

    # 同一 job 内对 (name, status) 去重
    seen_tests = set()
    # "PASSED:" 单独成行时，路径在下一行（NPU 文件级用例输出格式）
    pass_pending = False

    def add_test(name, status):
        if not name or len(name) > 120:
            return
        key = (name, status)
        if key not in seen_tests:
            seen_tests.add(key)
            result["all_tests"].append({"name": name, "status": status})

    for line in lines:
        if "AssertionError" in line:
            result["assertions"].append(line.strip()[:300])
        if "FAILED (failures=" in line or "FAILED (errors=" in line:
            result["final_result"] = line.strip()
        if "Accuracy:" in line:
            result["final_result"] += " | " + line.strip()

        s = strip_line(line)
        if not s:
            continue

        # 0) 上一行是 "PASSED:"：当前行为用例文件路径（可能连续多行）
        if pass_pending:
            m = re.match(r"^\s*(\S+\.py)", s)
            if m:
                path = m.group(1).replace("\\", "/").rstrip("/")
                name = path.rsplit("/", 1)[-1]
                name = name.removeprefix("test_")
                add_test(name, "PASSED")
                continue
            pass_pending = False

        # 1) [server-test] PASSED/FAILED diffusion testcase: <name>
        m = re.match(
            r"\[server-test\]\s+(PASSED|FAILED)\s+diffusion\s+testcase:\s*(\S+)", s
        )
        if m:
            add_test(m.group(2), m.group(1))
            if m.group(1) == "FAILED":
                result["failed_tests"].append(m.group(2))
            continue

        # 2) [Consistency Check] <name>: PASSED/FAILED
        m = re.match(r"\[Consistency Check\]\s+(\S+?):\s*(PASSED|FAILED)", s)
        if m:
            add_test(m.group(1), m.group(2))
            if m.group(2) == "FAILED":
                result["failed_tests"].append(m.group(1))
            continue

        # 3) pytest 形式：PASSED/FAILED <path>.py::<Class>::<method>[<param>] ...
        m = re.match(r"^(PASSED|FAILED):?\s+(.+?\.py)::(\S+)", s)
        if m:
            full = m.group(3).rstrip(" -")
            pm = re.search(r"\[([^\]]+)\]$", full)
            if pm and pm.group(1):
                name = pm.group(1)
            else:
                name = full
            add_test(name, m.group(1))
            if m.group(1) == "FAILED":
                result["failed_tests"].append(name)
            continue

        # 4) perf/acc 形式：FAILED: <.../test_npu_<case>
        m = re.match(r"^FAILED:\s+(\S+)", s)
        if m:
            path = m.group(1).replace("\\", "/").rstrip("/")
            name = path.rsplit("/", 1)[-1]
            name = name.removeprefix("test_")
            add_test(name, "FAILED")
            result["failed_tests"].append(name)
            continue

        # 4b) PASSED: <path>（与 FAILED: 同行形式对应）
        m = re.match(r"^PASSED:?\s+(\S+\.py)", s)
        if m:
            path = m.group(1).replace("\\", "/").rstrip("/")
            name = path.rsplit("/", 1)[-1]
            name = name.removeprefix("test_")
            add_test(name, "PASSED")
            continue

        # 4c) 单独 "PASSED:" 行 → 标记，路径在下一行处理
        if re.match(r"^PASSED:?\s*$", s):
            pass_pending = True

    # 找最后一个 Traceback
    in_tb = False
    tb_lines = []
    for i, line in enumerate(lines):
        if "Traceback (most recent call last)" in line:
            tb_lines = [line.strip()]
            in_tb = True
        elif in_tb:
            tb_lines.append(line.strip())
            if len(tb_lines) > 15:
                break
    if tb_lines:
        result["tracebacks"] = tb_lines

    return result


# ============================================================
# CI runs 分析主逻辑
# ============================================================


def _fetch_and_analyze_job(payload):
    """下载 job 日志 + 提取错误（+ AI 归因），供线程池并发调用。

    payload: (job_id, job_name, need_ai)
    返回 dict，含 ai_analysis 与 errors_extracted。
    """
    job_id, job_name, need_ai = payload
    try:
        dl_kwargs = _request_kwargs()
        dl_kwargs["timeout"] = (10, 120)  # 日志可能较大，读取超时放宽到 120s
        log_resp = _http_get_with_retry(
            f"https://api.github.com/repos/{TARGET_OWNER}/{TARGET_REPO}/actions/jobs/{job_id}/logs",
            headers=github_headers(),
            allow_redirects=True,
            stream=True,
            **dl_kwargs,
        )
        if log_resp.status_code != 200:
            raise RuntimeError(f"日志下载 HTTP {log_resp.status_code}")
        log_text = log_resp.text
        errors = extract_log_errors(log_text)
        result = {"errors_extracted": {k: v for k, v in errors.items() if v}}
        if need_ai:
            ai_result = ai_analyze_ci_log(job_name, log_text)
            result["ai_analysis"] = ai_result
        return result
    except Exception as e:
        return {"ai_analysis": {"category": "日志下载失败", "summary": str(e)[:100]}}


def analyze_ci_jobs():
    """主入口：拉取 NPU CI runs，分析各 job 状态，返回结构化结果"""
    print("\n[CI] 获取 NPU CI 执行结果...")
    ci_state = load_ci_state()

    try:
        runs = fetch_ci_runs()
    except Exception as e:
        print(f"  [CI WARN] 获取 CI runs 失败: {e}")
        return None

    print(f"  [CI] 拉取到 {len(runs)} 个 completed runs")

    report_runs = []  # 报告用的 run 列表
    pending = []  # (run_idx, job_idx, job_id, job_name, need_ai) 需要下载日志的 job

    for run in runs:
        run_id = str(run["id"])
        # 跳过已分析过的 run
        if run_id in ci_state:
            continue

        # 计算 run 总耗时
        run_dur = 0
        if run.get("run_started_at") and run.get("updated_at"):
            s = datetime.fromisoformat(run["run_started_at"].replace("Z", "+00:00"))
            e = datetime.fromisoformat(run["updated_at"].replace("Z", "+00:00"))
            run_dur = (e - s).total_seconds() / 60

        if run_dur < CI_MIN_RUN_DURATION_MIN:
            # 快速失败（pr-gate 没过），跳过，不记录以减少 CI 报告噪音
            continue

        print(
            f"  [CI] 分析 Run #{run_id} ({run_dur:.1f}min) branch={run['head_branch']}..."
        )

        # 获取 jobs
        try:
            url = f"https://api.github.com/repos/{TARGET_OWNER}/{TARGET_REPO}/actions/runs/{run_id}/jobs"
            jobs = api_get(url, {"per_page": 30}).get("jobs", [])
        except Exception as e:
            print(f"    [CI WARN] 获取 jobs 失败: {e}")
            continue

        run_entry = {
            "run_id": run_id,
            "html_url": run["html_url"],
            "branch": run["head_branch"],
            "conclusion": run["conclusion"],
            "duration_min": round(run_dur, 1),
            "created_at": run["created_at"],
            "head_sha": run.get("head_sha", ""),
            "jobs": [],
            "failed_jobs_analyzed": [],
        }

        # 获取 PR 信息
        pr_info = fetch_pr_by_sha(run.get("head_sha", ""))
        if pr_info:
            run_entry["pr_number"] = pr_info["number"]
            run_entry["pr_title"] = pr_info["title"]
            run_entry["pr_html_url"] = pr_info["html_url"]
            print(f"    → 关联 PR: #{pr_info['number']} - {pr_info['title']}")

        # 当前 run 在 report_runs 中的索引（append 前的长度）
        run_idx = len(report_runs)

        for j in jobs:
            name = j["name"]
            con = j.get("conclusion", "unknown")
            j_dur = 0
            if j.get("started_at") and j.get("completed_at"):
                s = datetime.fromisoformat(j["started_at"].replace("Z", "+00:00"))
                e = datetime.fromisoformat(j["completed_at"].replace("Z", "+00:00"))
                j_dur = (e - s).total_seconds() / 60

            if j_dur < CI_MIN_JOB_DURATION_MIN:
                continue

            job_entry = {
                "name": name,
                "conclusion": con,
                "duration_min": round(j_dur, 1),
                "completed_at": j.get("completed_at", ""),
                "html_url": j.get("html_url", ""),
                "run_id": run["id"],
            }
            job_idx = len(run_entry["jobs"])

            # 非 success 且非 skipped 的 job → 标记 alert
            if con in ("failure", "timed_out", "cancelled"):
                job_entry["alert"] = True
                steps = j.get("steps", [])
                failed_step = next(
                    (st for st in steps if st.get("conclusion") == "failure"), None
                )
                is_fast_fail = bool(failed_step) and (
                    "check-pr-test-health" in (failed_step.get("name") or "")
                    or "Check PR test health" in (failed_step.get("name") or "")
                )
                job_entry["fast_fail"] = is_fast_fail

                if is_fast_fail:
                    job_entry["ai_analysis"] = {
                        "category": "健康检查失败",
                        "summary": "check-pr-test-health 步骤失败（fast-fail 级联）",
                    }
                    print(f"    ⏭️ 健康检查失败（fast-fail）: {name}")
                elif con == "cancelled" and not steps:
                    # 排队/等待后被取消：job 从未执行任何步骤（无日志），跳过下载与 AI
                    job_entry["ai_analysis"] = {
                        "category": "排队取消",
                        "summary": "job 未执行任何步骤（steps=0），排队/等待后随 run 取消",
                    }
                    job_entry["no_log"] = True
                    print(f"    ⏭️ 排队取消（无日志）: {name}")
                else:
                    print(
                        f"    ⚠️ 失败 job: {name} ({j_dur:.1f}min)，下载日志 AI 分析..."
                    )
                    pending.append((run_idx, job_idx, j["id"], name, True))
            elif con == "success":
                job_entry["alert"] = False
                print(f"    ✅ 成功 job: {name} ({j_dur:.1f}min)，下载日志提取用例...")
                pending.append((run_idx, job_idx, j["id"], name, False))
            else:
                job_entry["alert"] = False

            run_entry["jobs"].append(job_entry)

        if run_entry["jobs"]:
            report_runs.append(run_entry)

        ci_state[run_id] = {
            "verdict": run["conclusion"],
            "branch": run["head_branch"],
            "duration_min": round(run_dur, 1),
            "analyzed_at": datetime.now(timezone.utc).isoformat(),
        }

    # 并发下载日志 + AI 归因（ex.map 保持顺序，结果按 pending 回填）
    if pending:
        total = len(pending)
        print(f"  [CI] 并发下载 {total} 个 job 日志并分析...", flush=True)
        results = []
        with ThreadPoolExecutor(max_workers=10) as ex:
            for done, res in enumerate(
                ex.map(
                    _fetch_and_analyze_job,
                    [(jid, jname, need) for _, _, jid, jname, need in pending],
                ),
                1,
            ):
                results.append(res)
                if done % 50 == 0 or done == total:
                    print(f"      ...已处理 {done}/{total} 个 job", flush=True)
        for (run_idx, job_idx, _, _, _), res in zip(pending, results):
            report_runs[run_idx]["jobs"][job_idx].update(res)
            ai = res.get("ai_analysis", {})
            print(
                f"      AI 判定: [{ai.get('category', '?')}] {ai.get('summary', '?')[:60]}"
            )

    save_ci_state(ci_state)
    print(f"  [CI] 本次新增分析: {len(report_runs)} 个 run")
    return report_runs


def generate_ci_report(ci_results) -> str:
    """生成 CI 监控报告"""
    now = datetime.now(CI_TZ).strftime("%Y-%m-%d %H:%M")

    # 监控窗口对应的具体日期（北京时间），与 fetch_ci_runs 使用同一回补逻辑
    window_days = ci_window_days()
    if window_days > 0:
        today0 = datetime.now(CI_TZ).replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        win_start = (today0 - timedelta(days=window_days)).date()
        win_end = (today0 - timedelta(days=1)).date()
        window_label = (
            f"{win_start.isoformat()}"
            if win_start == win_end
            else f"{win_start.isoformat()} ~ {win_end.isoformat()}"
        )
    else:
        window_label = "最近运行（未按日期过滤）"

    all_success_jobs = []
    for run_entry in ci_results:
        for j in run_entry.get("jobs", []):
            if j.get("conclusion") == "success" and not j.get("alert"):
                all_success_jobs.append(j)

    all_failed_jobs = []
    for run_entry in ci_results:
        for j in run_entry.get("jobs", []):
            if j.get("alert") and not j.get("no_log"):
                all_failed_jobs.append(j)

    failed_runs = []
    for run_entry in ci_results:
        alert_jobs = [
            j
            for j in run_entry.get("jobs", [])
            if j.get("alert") and not j.get("no_log")
        ]
        if alert_jobs:
            failed_runs.append(run_entry)

    success_runs = [r for r in ci_results if r not in failed_runs]
    avg_success_run_dur = 0.0
    if success_runs:
        avg_success_run_dur = sum(r["duration_min"] for r in success_runs) / len(
            success_runs
        )

    top10_success = sorted(
        all_success_jobs, key=lambda x: x["duration_min"], reverse=True
    )[:10]
    top10_failed = sorted(
        all_failed_jobs, key=lambda x: x["duration_min"], reverse=True
    )[:10]
    avg_success_dur = 0.0
    if all_success_jobs:
        avg_success_dur = sum(j["duration_min"] for j in all_success_jobs) / len(
            all_success_jobs
        )

    lines = []
    lines.append(f"# NPU CI 执行监控（{window_label}）")
    lines.append(f"**生成时间**: {now}")
    lines.append(f"**分析 Run 数**: {len(ci_results)}")
    lines.append("")
    lines.append("---")
    lines.append("")

    # 1. 总结区
    lines.append("## 📊 本次执行总结")
    lines.append("")
    lines.append(
        f"- **Job 执行情况**: 成功 {len(all_success_jobs)} 个 | "
        f"失败 {len(all_failed_jobs)} 个 | 成功 Job 平均耗时 {avg_success_dur:.1f}min"
    )
    lines.append(
        f"- **Run 执行情况**: 成功 {len(success_runs)} 个 | "
        f"失败 {len(failed_runs)} 个 | 成功 Run 平均耗时 {avg_success_run_dur:.1f}min"
    )
    lines.append("")

    if top10_success:
        lines.append("### ✅ 耗时最长的成功 Job（Top 10）")
        lines.append("")
        lines.append("| Job 名称 | 耗时 | 所属 Run | 链接 |")
        lines.append("|----------|------|----------|------|")
        for j in top10_success:
            lines.append(
                f"| {j['name']} | {j['duration_min']}min | #{j.get('run_id', '?')} | [job link]({j['html_url']}) |"
            )
        lines.append("")

    if top10_failed:
        lines.append("### ❌ 耗时最长的失败 Job（Top 10）")
        lines.append("")
        lines.append("| Job 名称 | 耗时 | 所属 Run | 链接 |")
        lines.append("|----------|------|----------|------|")
        for j in top10_failed:
            lines.append(
                f"| {j['name']} | {j['duration_min']}min | #{j.get('run_id', '?')} | [job link]({j['html_url']}) |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")

    # 2. Job 统计
    lines.append("## 📋 各任务执行统计")
    lines.append("")
    job_stats = {}
    for run_entry in ci_results:
        for j in run_entry.get("jobs", []):
            name = j["name"]
            if name not in job_stats:
                job_stats[name] = {
                    "total": 0,
                    "success": 0,
                    "failure": 0,
                    "check_health_failure": 0,
                    "cancelled": 0,
                    "failed_links": [],
                }
            job_stats[name]["total"] += 1
            if j.get("conclusion") == "success":
                job_stats[name]["success"] += 1
            elif j.get("fast_fail"):
                job_stats[name]["check_health_failure"] += 1
            elif j.get("conclusion") == "cancelled":
                job_stats[name]["cancelled"] += 1
            else:
                job_stats[name]["failure"] += 1
                if len(job_stats[name]["failed_links"]) < 5:
                    job_stats[name]["failed_links"].append(j["html_url"])

    job_stats_sorted = sorted(
        [
            (name, s)
            for name, s in job_stats.items()
            if s["failure"] + s["check_health_failure"] > 0
        ],
        key=lambda x: x[1]["failure"] + x[1]["check_health_failure"],
        reverse=True,
    )

    if job_stats_sorted:
        lines.append(
            "| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |"
        )
        lines.append(
            "|----------|----------|------|---------|-------------|------|-------------|"
        )
        for name, s in job_stats_sorted:
            if s["failure"] > 0 and s["failed_links"]:
                links_str = "<br>".join(
                    f"[job link {i + 1}]({url})"
                    for i, url in enumerate(s["failed_links"])
                )
            else:
                links_str = "-"
            lines.append(
                f"| {name} | {s['total']} | {s['success']} | {s['failure']} | {s['check_health_failure']} | {s['cancelled']} | {links_str} |"
            )
        lines.append("")
    else:
        lines.append("*无执行失败的任务。*")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 3. 用例统计
    lines.append("## 📋 各用例失败统计")
    lines.append("")
    test_case_stats = {}
    for run_entry in ci_results:
        for j in run_entry.get("jobs", []):
            for tc in j.get("errors_extracted", {}).get("all_tests", []):
                name = tc["name"]
                if name not in test_case_stats:
                    test_case_stats[name] = {
                        "total": 0,
                        "passed": 0,
                        "failed": 0,
                        "failed_job_links": [],
                    }
                test_case_stats[name]["total"] += 1
                if tc["status"] == "PASSED":
                    test_case_stats[name]["passed"] += 1
                elif tc["status"] == "FAILED":
                    test_case_stats[name]["failed"] += 1
                    job_link = f"[{j['name']}]({j['html_url']})"
                    if job_link not in test_case_stats[name]["failed_job_links"]:
                        if len(test_case_stats[name]["failed_job_links"]) < 3:
                            test_case_stats[name]["failed_job_links"].append(job_link)

    sorted_tcs = sorted(
        [(n, s) for n, s in test_case_stats.items() if s["failed"] > 0],
        key=lambda x: x[1]["failed"],
        reverse=True,
    )

    if sorted_tcs:
        lines.append("| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |")
        lines.append("|----------|----------|------|------|-------------|")
        for tc_name, s in sorted_tcs:
            links_str = (
                "<br>".join(s["failed_job_links"]) if s["failed_job_links"] else "-"
            )
            lines.append(
                f"| `{tc_name}` | {s['total']} | {s['passed']} | {s['failed']} | {links_str} |"
            )
        lines.append("")
    else:
        lines.append("*本次分析未发现失败用例。*")
        lines.append("")

    lines.append("---")
    lines.append("")

    # 4. 失败 CI Run 表格
    if failed_runs:
        lines.append("### ⚠️ 失败的 CI Run")
        lines.append("")
        lines.append("| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |")
        lines.append("|--------|------|------|-----------|-----------|------|------|")
        for r in sorted(failed_runs, key=lambda x: x["duration_min"], reverse=True):
            real_fail_jobs = [
                j
                for j in r.get("jobs", [])
                if j.get("alert") and not j.get("fast_fail") and not j.get("no_log")
            ]
            alert_count = len(real_fail_jobs)
            alert_names = ", ".join(j["name"] for j in real_fail_jobs)
            run_id_str = f"#{r['run_id']}"
            if r.get("pr_number"):
                run_id_str += (
                    f"<br>[#{r['pr_number']} {r['pr_title']}]({r['pr_html_url']})"
                )
            lines.append(
                f"| {run_id_str} | `{r['branch']}` | {r['duration_min']}min | {alert_count} | {alert_names} | {r['conclusion']} | [run link]({r['html_url']}) |"
            )
        lines.append("")

    lines.append("---")
    lines.append("")

    for run_entry in ci_results:
        alert_jobs = [j for j in run_entry.get("jobs", []) if j.get("alert")]
        normal_jobs = [j for j in run_entry.get("jobs", []) if not j.get("alert")]

        lines.append("")
        lines.append(f"## [Run #{run_entry['run_id']}]({run_entry['html_url']})")
        lines.append(f"- **分支**: `{run_entry['branch']}`")
        lines.append(
            f"- **总耗时**: {run_entry['duration_min']}min | **结论**: {run_entry['conclusion']}"
        )
        lines.append(f"- **workflow 链接**: {run_entry['html_url']}")
        lines.append("")

        if alert_jobs:
            lines.append("### ⚠️ 失败/超时任务")
            lines.append("")
            lines.append("| 任务 | 耗时 | 分类 | AI 分析 | 链接 |")
            lines.append("|------|------|------|---------|------|")
            for j in alert_jobs:
                ai = j.get("ai_analysis", {})
                lines.append(
                    f"| {j['name']} | {j['duration_min']}min | "
                    f"{ai.get('category', '?')} | {ai.get('summary', '?')} | "
                    f"[job link]({j['html_url']}) |"
                )
            lines.append("")

            for j in alert_jobs:
                ai = j.get("ai_analysis", {})
                if ai.get("detail") or j.get("errors_extracted", {}).get(
                    "failed_tests"
                ):
                    lines.append(f"- **{j['name']}**: {ai.get('detail', '')}")
                    failed_tests = j.get("errors_extracted", {}).get("failed_tests", [])
                    if failed_tests:
                        lines.append(f"  - 失败用例: {', '.join(failed_tests[:5])}")
                    lines.append(f"  链接: {j['html_url']}")
                lines.append("")

        if normal_jobs:
            lines.append("### 正常任务")
            lines.append("")
            lines.append("| 任务 | 耗时 | 结果 | 链接 |")
            lines.append("|------|------|------|------|")
            for j in normal_jobs:
                lines.append(
                    f"| {j['name']} | {j['duration_min']}min | {j['conclusion']} | "
                    f"[job link]({j['html_url']}) |"
                )
            lines.append("")

    lines.append("")
    lines.append("---")
    lines.append("*Auto-generated by ci_monitor.py*")
    return "\n".join(lines)


# ============================================================
# Git 操作
# ============================================================


def run_git_with_retry(cmd, cwd, retries=3, delay=15):
    """执行 git 命令，网络瞬断导致失败时自动重试（fetch/push 用）"""
    result = None
    for attempt in range(1, retries + 1):
        result = subprocess.run(cmd, cwd=str(cwd))
        if result.returncode == 0:
            return
        print(f"[git] 命令失败 (exit {result.returncode})，第 {attempt}/{retries} 次重试")
        if attempt < retries:
            time.sleep(delay)
    result.check_returncode()


def ensure_report_repo():
    """确保报告仓库存在并是最新的"""
    if not REPORTS_DIR.exists():
        print(f"[git] 克隆报告仓库 {REPORT_REMOTE}...")
        subprocess.run(
            ["git", "clone", "-b", REPORT_BRANCH, REPORT_REMOTE, str(REPORTS_DIR)],
            check=True,
            cwd=str(SCRIPT_DIR),
        )
    else:
        print("[git] 拉取最新...")
        try:
            run_git_with_retry(
                ["git", "fetch", "origin", REPORT_BRANCH], cwd=REPORTS_DIR
            )
        except subprocess.CalledProcessError:
            # 远端分支可能被误删：用本地分支自动重建后再拉取
            print(f"[git] fetch 失败，尝试用本地分支重建远端 {REPORT_BRANCH}...")
            run_git_with_retry(
                ["git", "push", "origin", REPORT_BRANCH], cwd=REPORTS_DIR
            )
            run_git_with_retry(
                ["git", "fetch", "origin", REPORT_BRANCH], cwd=REPORTS_DIR
            )
        subprocess.run(
            ["git", "checkout", REPORT_BRANCH], check=True, cwd=str(REPORTS_DIR)
        )
        subprocess.run(
            ["git", "reset", "--hard", f"origin/{REPORT_BRANCH}"],
            check=True,
            cwd=str(REPORTS_DIR),
        )


def commit_and_push_ci(ci_report: str):
    """提交并推送 ci_report.md（CI-only）"""
    ensure_report_repo()

    now = datetime.now(CI_TZ)
    dirname = now.strftime("%Y%m%d_%H%M")
    report_dir = REPORTS_DIR / "report" / dirname
    report_dir.mkdir(parents=True, exist_ok=True)

    ci_path = report_dir / "ci_report.md"
    ci_path.write_text(ci_report, encoding="utf-8")

    msg = f"[CI] NPU CI 监控 {now.strftime('%Y-%m-%d %H:%M')} - 更新 CI 执行报告"
    print(f"[git] 提交: {msg}")
    subprocess.run(
        ["git", "add", f"report/{dirname}/ci_report.md"],
        check=True,
        cwd=str(REPORTS_DIR),
    )
    subprocess.run(["git", "commit", "-m", msg], check=True, cwd=str(REPORTS_DIR))
    run_git_with_retry(["git", "push", "origin", REPORT_BRANCH], cwd=REPORTS_DIR)
    print("[git] 推送成功")


# ============================================================
# 主流程
# ============================================================


def main():
    print(
        f"[{datetime.now(CI_TZ).strftime('%Y-%m-%d %H:%M:%S')}] NPU CI 监控开始（仅流水线）"
    )
    print(f"  目标仓库: {TARGET_OWNER}/{TARGET_REPO}")

    ci_results = analyze_ci_jobs()
    if not ci_results:
        print("  无新的 CI 结果")
        return

    print("  生成报告...")
    ci_report = generate_ci_report(ci_results)

    dirname = datetime.now(CI_TZ).strftime("%Y%m%d_%H%M")
    local_dir = SCRIPT_DIR / "reports" / dirname
    local_dir.mkdir(parents=True, exist_ok=True)
    (local_dir / "ci_report.md").write_text(ci_report, encoding="utf-8")
    print(f"  本地报告: {local_dir}")

    try:
        print("  推送报告到 GitHub...")
        commit_and_push_ci(ci_report)
    except Exception as e:
        print(f"  [ERROR] Git 推送失败: {e}")
        print(f"  报告已保存在本地: {local_dir}")

    alert_count = sum(
        sum(1 for j in run.get("jobs", []) if j.get("alert") and not j.get("no_log"))
        for run in ci_results
    )
    print(f"  CI: {len(ci_results)} 个 run, {alert_count} 个失败任务")

    # 记录本次成功运行日期，供下次漏采自动回补
    state = load_ci_state()
    state["_last_success_date"] = datetime.now(CI_TZ).date().isoformat()
    save_ci_state(state)


if __name__ == "__main__":
    main()
