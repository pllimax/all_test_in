"""nightly 用例配置漂移检测（方案 B：只检测报告，不落盘配置）。

每日 cron 运行：拉取社区 sgl-project/sglang main，扫描 test/registered/npu 下全部
register_npu_ci(suite="nightly-...") 注册声明与 nightly-test-npu.yml 多节点 matrix
引用，与 testcases_config.json 对比，差异写入报告文件。

设计约束：
  - 只读对比，绝不修改 testcases_config.json（该文件由 git 管理，服务器自动改动
    会破坏 10 分钟 cron 的 fetch + merge --ff-only 同步链路）
  - 社区仓 fetch 失败（服务器到 github 网络不稳）不视为致命错误，报告中注明并
    基于本地克隆继续对比
  - 报告输出到 logs/testcases_drift/（未跟踪目录，不影响 git 状态）

用法：python3 check_testcases_drift.py [--no-fetch] [--repo-dir <路径>]
"""
import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_REPO = os.path.dirname(BASE_DIR)
CONFIG_PATH = os.path.join(BASE_DIR, "testcases_config.json")
REPORT_DIR = os.path.join(DEFAULT_REPO, "logs", "testcases_drift")
NIGHTLY_REPO = os.path.join(BASE_DIR, ".testcases_repo", "nightly")
NIGHTLY_YML = ".github/workflows/nightly-test-npu.yml"

FETCH_TIMEOUT = 600  # 秒，服务器到 github 网络不稳，留足超时

SUITE_RE = re.compile(r"suite\s*=\s*['\"]([^'\"]+)['\"]")
TEST_CASE_RE = re.compile(r"test_case:\s*(test/registered/npu/\S+\.py)")


def run_git(repo, args, timeout=120):
    try:
        out = subprocess.run(
            ["git", "-C", repo] + args,
            capture_output=True, text=True, encoding="utf-8",
            errors="replace", timeout=timeout,
        )
        return out.returncode, out.stdout, out.stderr
    except subprocess.TimeoutExpired:
        return 124, "", f"git {' '.join(args)} timed out after {timeout}s"


def load_nightly_suites(repo):
    """从 test/run_suite.py 提取全部 nightly-*npu* suite 名（动态跟随上游变更）。"""
    path = os.path.join(repo, "test", "run_suite.py")
    if not os.path.isfile(path):
        return set()
    body = open(path, encoding="utf-8", errors="replace").read()
    return set(re.findall(r"['\"](nightly-[a-z0-9-]*npu[a-z0-9-]*)['\"]", body))


def scan_registered_cases(repo, suites):
    """扫描 test/registered/npu 下注册到 nightly suite 的用例，及 workflow matrix 引用。"""
    registered = {}
    test_root = os.path.join(repo, "test", "registered", "npu")
    if os.path.isdir(test_root):
        for root, _dirs, files in os.walk(test_root):
            for fn in files:
                if not (fn.startswith("test_npu_") and fn.endswith(".py")):
                    continue
                path = os.path.join(root, fn)
                rel = os.path.relpath(path, repo).replace("\\", "/")
                body = open(path, encoding="utf-8", errors="replace").read()
                hit = {s for s in SUITE_RE.findall(body) if s in suites}
                if not hit:
                    continue
                low = rel.lower()
                if "/performance/" in low:
                    t = "performance"
                elif "/accuracy/" in low:
                    t = "accuracy"
                else:
                    t = "function"
                registered[fn[:-3]] = {"suites": sorted(hit), "type": t}

    # workflow 多节点 matrix 的 test_case 引用（suite 集合之外的执行入口）
    yml = os.path.join(repo, NIGHTLY_YML)
    if os.path.isfile(yml):
        body = open(yml, encoding="utf-8", errors="replace").read()
        for rel in TEST_CASE_RE.findall(body):
            case = os.path.basename(rel)[:-3]
            if case not in registered:
                low = rel.lower()
                t = "performance" if "/performance/" in low else "accuracy"
                registered[case] = {"suites": ["multi-node-matrix"], "type": t}
    return registered


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--no-fetch", action="store_true", help="跳过社区仓 fetch")
    ap.add_argument("--repo-dir", default=NIGHTLY_REPO,
                    help="社区 sglang 克隆路径（默认 .testcases_repo/nightly）")
    args = ap.parse_args()

    lines = []
    now = datetime.now()
    lines.append(f"nightly 用例配置漂移检测报告  {now:%Y-%m-%d %H:%M:%S}")
    lines.append(f"社区仓: {args.repo_dir}")

    fetch_ok = None
    if not args.no_fetch:
        rc, _out, err = run_git(args.repo_dir, ["fetch", "origin", "main"],
                                timeout=FETCH_TIMEOUT)
        fetch_ok = rc == 0
        if fetch_ok:
            rc2, _o, e2 = run_git(args.repo_dir,
                                  ["merge", "--ff-only", "FETCH_HEAD"])
            fetch_ok = rc2 == 0
            if not fetch_ok:
                lines.append(f"[警告] 社区仓 fast-forward 失败: {e2.strip()[:200]}")
        else:
            lines.append(f"[警告] 社区仓 fetch 失败（网络或超时），基于本地克隆对比: "
                         f"{err.strip()[:200]}")
    lines.append(f"fetch 状态: {'成功' if fetch_ok else '失败/跳过'}")

    head_rc, head, _ = run_git(args.repo_dir, ["rev-parse", "--short", "HEAD"])
    lines.append(f"社区仓 HEAD: {head.strip() if head_rc == 0 else '未知'}")

    suites = load_nightly_suites(args.repo_dir)
    lines.append(f"nightly suite 数: {len(suites)}")
    if not suites:
        lines.append("[错误] 未能从 run_suite.py 提取 nightly suite，可能克隆不完整")

    registered = scan_registered_cases(args.repo_dir, suites)
    lines.append(f"社区 nightly 注册用例数: {len(registered)}")

    try:
        cfg = json.load(open(CONFIG_PATH, encoding="utf-8"))
        lines.append(f"平台配置用例数: {len(cfg)}")
    except Exception as e:
        lines.append(f"[错误] 读取配置失败: {e}")
        cfg = {}

    missing = sorted(set(registered) - set(cfg))
    extra = [c for c in sorted(set(cfg) - set(registered))
             if "fulltest" not in cfg[c].get("source", "")]
    type_diff = [(c, cfg[c].get("type"), registered[c]["type"])
                 for c in sorted(set(registered) & set(cfg))
                 if cfg[c].get("type") != registered[c]["type"]]

    lines.append("")
    if not (missing or extra or type_diff):
        lines.append("结论: 配置与社区 nightly 一致，无漂移。")
    else:
        lines.append(f"结论: 发现漂移！缺失 {len(missing)} / 多余 {len(extra)} / "
                     f"类型差异 {len(type_diff)}")
    if missing:
        lines.append("\n== 缺失（社区已注册，配置没有）==")
        for c in missing:
            lines.append(f"  + {c}  type={registered[c]['type']} "
                         f"suites={registered[c]['suites']}")
    if extra:
        lines.append("\n== 多余（配置有 nightly 来源，社区已无注册/引用）==")
        for c in extra:
            lines.append(f"  - {c}  source={cfg[c].get('source')} "
                         f"type={cfg[c].get('type')}")
    if type_diff:
        lines.append("\n== 类型差异 ==")
        for c, have, want in type_diff:
            lines.append(f"  ! {c}: config={have} community={want}")
    lines.append("\n处理方式: 人工核对后在本机更新 testcases_config.json 并提交，"
                 "随 10 分钟 cron 自动下发，切勿在服务器直接改配置。")

    report = "\n".join(lines)
    print(report)

    os.makedirs(REPORT_DIR, exist_ok=True)
    dated = os.path.join(REPORT_DIR, f"report-{now:%Y%m%d}.txt")
    latest = os.path.join(REPORT_DIR, "latest.txt")
    for p in (dated, latest):
        tmp = p + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            f.write(report + "\n")
        os.replace(tmp, p)
    # 只保留最近 30 天的日期报告
    from datetime import timedelta
    cutoff = f"report-{(now - timedelta(days=30)):%Y%m%d}"
    for name in os.listdir(REPORT_DIR):
        if name.startswith("report-") and name < cutoff:
            try:
                os.remove(os.path.join(REPORT_DIR, name))
            except OSError:
                pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
