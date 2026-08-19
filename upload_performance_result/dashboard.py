"""
Self-contained performance dashboard - no Docker/Prometheus/Grafana required.
Reads benchmark files directly and serves an interactive web dashboard.
Each test case = model + quantization + parallelism + input_len + output_len + request_rate + dataset
Results are compared across dates for each exact test case.
"""
import os
import re
import json
import sys
import time
import threading
import urllib.request
import urllib.parse
import http.server
import socketserver
import subprocess
import shutil
from prometheus_exporter import parse_filename, parse_benchmark_file, collect_eval_data, collect_accuracy_only_data, GIT_PULL_ENABLED, GIT_METRICS_DIR, get_metrics_dir, _iter_metrics_files, PERF_ONLY_FIELDS


def _run(cmd, **kw):
    """subprocess.run 包装：默认捕获输出并以 UTF-8 解码（兼容 Windows 下 git 的
    UTF-8 输出与本地 GBK 编码不一致导致 text=True 解码抛异常的问题）。"""
    kw.setdefault("capture_output", True)
    kw.setdefault("text", True)
    kw.setdefault("encoding", "utf-8")
    kw.setdefault("errors", "replace")
    return subprocess.run(cmd, **kw)

DASHBOARD_PORT = int(os.environ.get("DASHBOARD_PORT", "8080"))
# 默认仅监听本机回环地址，避免在共享网络中意外暴露性能数据与备注接口；
# 需要对外提供时显式设置 DASHBOARD_HOST=0.0.0.0（并建议配置 NOTE_API_TOKEN）。
DASHBOARD_HOST = os.environ.get("DASHBOARD_HOST", "127.0.0.1")
# API 响应 CORS 来源：默认空（不发送 CORS 头，同源访问不受影响）；
# 需允许其它前端跨域访问时显式配置，例如 DASHBOARD_CORS_ORIGIN=https://example.com
DASHBOARD_CORS_ORIGIN = os.environ.get("DASHBOARD_CORS_ORIGIN", "")

# ============================================================
# 受管源码仓缓存目录（方案A）
# 配置了 repo_url 的 source，其用例列表 YAML 与测试脚本（基线）由
# dashboard 自己稀疏克隆/更新到该缓存目录，不再依赖本地手动克隆路径。
# 稀疏检出仅保留 workflows YAML 与测试脚本目录，避免全量克隆过大。
# ============================================================
TESTCASES_CACHE_DIR = os.environ.get(
    "TESTCASES_CACHE_DIR",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), ".testcases_repo"),
)
SPARSE_CHECKOUT_PATHS = [
    ".github/workflows",
    "test/registered/ascend",
    "test/registered/npu",
]
# 源码仓周期性同步间隔（秒），与基线/链接缓存 TTL 一致（默认每 2 小时）
SOURCE_SYNC_INTERVAL = int(os.environ.get("SOURCE_SYNC_INTERVAL", "7200"))

# ============================================================
# suite → 用例 映射（新框架聚合 job 适配）
# 新测试框架将 a3 芯片用例聚合到 suite job（如 nightly-perf-2-npu-a3）运行，
# job 名 = suite 名，不含具体用例名。为把用例链接到其聚合 job，需从用例文件
# 的 register_npu_ci(suite="X", nightly=True) 注册信息构建 suite→用例 映射。
# pllimax 分支已合并到社区 main，直接使用 sgl-project/sglang 的 main 分支。
# ============================================================
SUITE_REGISTRY_CACHE_DIR = os.environ.get(
    "SUITE_REGISTRY_CACHE_DIR",
    os.path.join(TESTCASES_CACHE_DIR, "suite_registry"),
)
SUITE_REGISTRY_REPO_URL = os.environ.get(
    "SUITE_REGISTRY_REPO_URL", "https://github.com/sgl-project/sglang.git"
)
SUITE_REGISTRY_BRANCH = os.environ.get(
    "SUITE_REGISTRY_BRANCH", "main"
)
SUITE_REGISTRY_SUBDIR = "test/registered/npu"

# ============================================================
# 平台展示用例的本地配置文件（权威来源）
# 为避免 GitHub 社区仓中用例被他人删除/修改导致平台用例列表漂移，
# 将识别到的用例清单固化为本地 testcases_config.json，
# collect_expected_test_cases 优先从该文件加载。
# 如需更新用例列表，执行 python dashboard.py --update-testcases-config
# （会先同步代码仓，再基于最新 YAML + 注册器扫描结果重新生成配置文件）。
# ============================================================
TESTCASES_CONFIG_FILE = os.environ.get(
    "TESTCASES_CONFIG_FILE",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "testcases_config.json"),
)

# 用例 → suite 全局映射（构建成功后缓存）
_suite_case_map = None       # {suite: [case_name, ...]}
_case_suite_map = None       # {case_name: suite}
_suite_map_ts = 0.0
_suite_map_lock = threading.RLock()  # 保护 suite 映射缓存的并发读写


def get_config_paths():
    """
    Get configuration paths with priority: environment variable > config file > relative path default.
    Supports cross-platform usage without modifying source code.

    Config structure (dashboard_config.json):
    {
        "sources": {
            "fulltest": {
                "repo_url": "https://...",
                "repo_root": "/path/to/repo",
                "yaml_config": "relative/path/to/workflow.yml"
            },
            "nightly": { ... }
        }
    }
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(current_dir, "dashboard_config.json")

    config_data = {}
    if os.path.isfile(config_file):
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config_data = json.load(f)
            print(f"[config] Loaded config from: {config_file}")
        except Exception as e:
            print(f"[config] Warning: Failed to load config file {config_file}: {e}")

    # Parse new "sources" structure
    sources = {}
    if "sources" in config_data:
        for source_name, source_cfg in config_data["sources"].items():
            repo_root = source_cfg.get("repo_root", "")
            yaml_rel = source_cfg.get("yaml_config", "")
            repo_url = source_cfg.get("repo_url", "")
            branch = source_cfg.get("branch", "")
            env_prefix = source_name.upper()

            # env var overrides
            repo_root = os.environ.get(f"{env_prefix}_REPO_ROOT", repo_root)
            yaml_rel = os.environ.get(f"{env_prefix}_YAML_CONFIG", yaml_rel)
            repo_url = os.environ.get(f"{env_prefix}_REPO_URL", repo_url)
            branch = os.environ.get(f"{env_prefix}_BRANCH", branch)

            # 方案A：配置了 repo_url 时，优先使用 dashboard 自管理的
            # 稀疏克隆缓存目录（.testcases_repo/{source_name}）。
            # 用例 YAML 与测试脚本（基线）均从该 git 仓动态读取，
            # 不依赖本地手动克隆的社区仓/测试仓路径。
            # 受管目录由 sync_repos 在启动时克隆/更新（clone 失败时
            # _sync_managed_repo 会打印错误，collect_* 内部跳过不存在的目录，
            # 不会因受管目录不可用导致 YAML 与测试脚本全部缺失）。
            if repo_url:
                managed_root = os.path.join(TESTCASES_CACHE_DIR, source_name)
                print(f"[config] {source_name}: 使用受管克隆目录 {managed_root} (branch={branch or 'main'}, 本地回退 {repo_root})")
                repo_root = managed_root

            if repo_root and yaml_rel:
                yaml_abs = os.path.join(repo_root, yaml_rel)
                sources[source_name] = {
                    "repo_root": repo_root,
                    "yaml_config": yaml_abs,
                    "repo_url": repo_url,
                    "branch": branch,
                }
                print(f"[config] {source_name}: repo={repo_root}, yaml={yaml_abs}")
            else:
                print(f"[config] Warning: source '{source_name}' missing repo_root or yaml_config")

    # Legacy fallback: flat structure with yaml_configs + test_scripts_roots
    if not sources:
        print("[config] Using legacy flat config structure")
        yaml_configs = []
        yaml_env = os.environ.get("YAML_CONFIG_PATHS")
        if yaml_env:
            yaml_configs = [p.strip() for p in yaml_env.split(";") if p.strip()]
        elif "yaml_configs" in config_data:
            yaml_configs = config_data["yaml_configs"]
        else:
            default_sglang_root = os.path.join(os.path.dirname(current_dir), "sglang")
            yaml_configs = [
                os.path.join(default_sglang_root, ".github", "workflows", "full-test-npu.yml"),
                os.path.join(default_sglang_root, ".github", "workflows", "nightly-test-npu.yml"),
            ]

        test_scripts_roots = []
        fulltest_root = os.environ.get("FULLTEST_TEST_SCRIPTS_ROOT", "")
        nightly_root = os.environ.get("NIGHTLY_TEST_SCRIPTS_ROOT", "")
        if not fulltest_root and "fulltest_test_scripts_root" in config_data:
            fulltest_root = config_data["fulltest_test_scripts_root"]
        if not nightly_root and "nightly_test_scripts_root" in config_data:
            nightly_root = config_data["nightly_test_scripts_root"]
        if fulltest_root:
            test_scripts_roots.append(fulltest_root)
        if nightly_root:
            test_scripts_roots.append(nightly_root)

        # Map legacy: index 0=fulltest, index 1=nightly
        for i, yp in enumerate(yaml_configs):
            src_name = "fulltest" if i == 0 else "nightly"
            root = test_scripts_roots[i] if i < len(test_scripts_roots) else ""
            sources[src_name] = {
                "repo_root": root,
                "yaml_config": yp,
                "repo_url": "",
                "branch": "",
            }

    # Validate and build derived structures
    valid_sources = {}
    for src_name, src_cfg in sources.items():
        repo_root = src_cfg["repo_root"]
        yaml_config = src_cfg["yaml_config"]
        if os.path.isfile(yaml_config):
            valid_sources[src_name] = src_cfg.copy()
        else:
            # 方案A：受管克隆目录在 sync_repos 前尚未创建，属正常现象，不告警
            if not src_cfg.get("repo_url"):
                print(f"[config] Warning: yaml not found for '{src_name}': {yaml_config}")
            # still keep it for repo sync, but mark yaml as missing
            valid_sources[src_name] = src_cfg.copy()
            valid_sources[src_name]["yaml_valid"] = False
            if src_name == "nightly":
                valid_sources[src_name]["yaml_valid"] = True  # still try

    test_scripts_roots = []
    yaml_configs = []
    for src_name, src_cfg in valid_sources.items():
        repo_root = src_cfg["repo_root"]
        # 测试脚本可能位于 test/registered/ascend 或 test/registered/npu
        # 注：不在此处用 os.path.isdir 过滤 —— 方案A 的受管目录由 sync_repos
        # 在启动后克隆创建；collect_baselines / _get_nnodes_from_script /
        # collect_script_urls 内部均会跳过不存在的目录，这里仅登记候选路径。
        if repo_root:
            for sub in ("ascend", "npu"):
                scripts_path = os.path.join(repo_root, "test", "registered", sub)
                if scripts_path not in test_scripts_roots:
                    test_scripts_roots.append(scripts_path)
        yaml_configs.append(src_cfg["yaml_config"])

    # Parse branch_repo_map: {branch前缀: repo_url}
    # 用于解析 CI 运行（GitHub Actions run）所属的仓库，
    # 分支模式数据目录名为 {分支}-{create_date}-{run_id}，run 通常运行在分支的 fork 仓。
    branch_repo_map = {}
    if "branch_repo_map" in config_data:
        branch_repo_map = {
            str(k).strip(): str(v).strip()
            for k, v in config_data["branch_repo_map"].items()
            if str(k).strip() and str(v).strip()
        }
    branch_repo_map_env = os.environ.get("BRANCH_REPO_MAP", "")
    if branch_repo_map_env:
        try:
            parsed = json.loads(branch_repo_map_env)
            if isinstance(parsed, dict):
                branch_repo_map = {str(k).strip(): str(v).strip() for k, v in parsed.items()}
        except Exception as e:
            print(f"[config] Warning: Failed to parse BRANCH_REPO_MAP env: {e}")
    if branch_repo_map:
        print(f"[config] branch_repo_map: {branch_repo_map}")

    return {
        "sources": valid_sources,
        "yaml_configs": yaml_configs,
        "test_scripts_roots": test_scripts_roots,
        "branch_repo_map": branch_repo_map,
    }


_config = get_config_paths()
SOURCES = _config["sources"]
YAML_CONFIGS = _config["yaml_configs"]
TEST_SCRIPTS_ROOTS = _config["test_scripts_roots"]
BRANCH_REPO_MAP = _config["branch_repo_map"]

# ============================================================
# 用例备注（notes）
# 每条备注针对「某一条执行结果」保存，而不是整个用例（yaml_name）共享一条。
# 执行结果由复合键标识：{yaml_name}|{date}|{branch}|{run_id}，
# 保证同一用例在不同日期/分支/run 下的执行结果可分别备注。
# 备注本地持久化到 notes.json，并可选定期 commit/push 到 git 仓（与 collect_metrics.sh 的 git 上传模式一致）。
# ============================================================
NOTES_FILE = os.environ.get(
    "NOTES_FILE",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes.json"),
)
# 定期将备注持久化到 git 仓的间隔（秒），默认 14400s（4 小时）
NOTES_GIT_INTERVAL = int(os.environ.get("NOTES_GIT_INTERVAL", "14400"))
# 是否启用 git 持久化（配置 repo 与 git 可用时才有意义）
NOTES_GIT_PUSH_ENABLED = os.environ.get("NOTES_GIT_PUSH", "1") != "0"

NOTES_KEY_SEP = "|"

_notes = {}          # {复合键: note_text}
_notes_loaded = False
_notes_dirty = False  # 本地已有变更但尚未提交到 git
_notes_lock = threading.RLock()  # RLock：save_note 内调用 load_notes 需可重入


def _notes_path():
    return NOTES_FILE


def note_key_for(yaml_name, date="", branch="", run_id=""):
    """构造某条执行结果的备注复合键。"""
    return NOTES_KEY_SEP.join(
        [str(yaml_name or ""), str(date or ""), str(branch or ""), str(run_id or "")]
    )


def note_key_for_item(item):
    """从数据条目构造备注复合键。"""
    return note_key_for(
        item.get("yaml_name", ""),
        item.get("date", ""),
        item.get("branch", ""),
        item.get("run_id", ""),
    )


def load_notes():
    """加载备注（进程内缓存，首次从 notes.json 读取）。"""
    global _notes, _notes_loaded
    if _notes_loaded:
        return _notes
    with _notes_lock:
        if _notes_loaded:
            return _notes
        _notes = {}
        if os.path.isfile(_notes_path()):
            try:
                with open(_notes_path(), "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, dict):
                    _notes = {str(k): str(v) for k, v in data.items()}
            except Exception as e:
                print(f"[notes] load notes failed: {e}")
        _notes_loaded = True
        return _notes


def _write_notes_atomic(notes):
    """原子写 notes.json：先写临时文件再 os.replace，避免进程中断留下半写文件。"""
    tmp_path = _notes_path() + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, _notes_path())


def save_note(key, note_text):
    """保存一条执行结果的备注（复合键），立即写盘。返回 True 表示成功。"""
    global _notes, _notes_dirty
    with _notes_lock:
        load_notes()
        note_text = (note_text or "").strip()
        if note_text:
            _notes[key] = note_text
        else:
            _notes.pop(key, None)
        try:
            _write_notes_atomic(_notes)
            _notes_dirty = True
            return True
        except Exception as e:
            print(f"[notes] save notes failed: {e}")
            return False


def clear_notes_for_case(yaml_name):
    """删除某用例（yaml_name）的所有历史备注条目（纯键 + 复合键）。返回删除条数。"""
    global _notes, _notes_dirty
    with _notes_lock:
        load_notes()
        prefix = str(yaml_name or "").strip()
        if not prefix:
            return 0
        removed = [k for k in _notes
                   if k == prefix or k.startswith(prefix + NOTES_KEY_SEP)]
        for k in removed:
            _notes.pop(k, None)
        try:
            _write_notes_atomic(_notes)
            _notes_dirty = True
            return len(removed)
        except Exception as e:
            print(f"[notes] clear notes failed: {e}")
            return 0


def attach_notes(items):
    """为每条数据附加 note / note_date 字段（按执行结果复合键匹配）。

    优先级：
      1) 精确复合键命中 → 该执行结果自己的备注，note_date 为空（即当日备注）。
      2) 未命中 → 回退到该用例（同 yaml_name）最新的历史备注：从所有复合键中
         取日期（date）最大的一条作为默认备注，并附加其日期 note_date；
         若该用例只有纯 yaml_name 历史键（无日期）则回退到该键且 note_date 为空。
    """
    notes = load_notes()
    # 预构建 yaml_name → (date, note) 的最新历史备注映射（复合键，date 最大者）
    latest_hist = {}
    # 加锁保护对共享 _notes 字典的迭代，避免与 save_note / clear_notes_for_case
    # 的并发修改产生 RuntimeError: dictionary changed size during iteration
    with _notes_lock:
        for k, v in notes.items():
            parts = k.split(NOTES_KEY_SEP)
            if len(parts) >= 2:
                yaml_name = parts[0]
                date = parts[1]
                cur = latest_hist.get(yaml_name)
                if cur is None or date > cur[0]:
                    latest_hist[yaml_name] = (date, v)
    for item in items:
        key = note_key_for_item(item)
        note = notes.get(key)
        note_date = None
        if note is None:
            yaml_name = str(item.get("yaml_name", "") or "")
            hist = latest_hist.get(yaml_name)
            if hist is not None:
                note, note_date = hist[1], hist[0]
            else:
                note = notes.get(yaml_name, "")
        item["note"] = note or ""
        if note_date:
            item["note_date"] = note_date
        else:
            # 清理陈旧残留：未命中历史备注时显式移除，避免复用旧数据里的 note_date
            item.pop("note_date", None)
    return items

# Test cases to exclude from the dashboard
EXCLUDED_TEST_CASES = {
    "glm4_6v_flash_1p_mmmu",
    "test_npu_cp_vs_nocp_ttft",
}

# Mapping from test script attribute names to metric names
ATTR_TO_METRIC = {
    "ttft": "mean_ttft",
    "tpot": "mean_tpot",
    "e2e_latency": "mean_e2e_latency",
    "output_token_throughput": "output_token_throughput",
    "accuracy": "eval_score",
}

# Regex patterns to extract baseline values from Python test scripts
BASELINE_PATTERNS = {
    "ttft": re.compile(r'^\s*ttft\s*=\s*([\d.]+)', re.MULTILINE),
    "tpot": re.compile(r'^\s*tpot\s*=\s*([\d.]+)', re.MULTILINE),
    "e2e_latency": re.compile(r'^\s*e2e_latency\s*=\s*([\d.]+)', re.MULTILINE),
    "output_token_throughput": re.compile(r'^\s*output_token_throughput\s*=\s*([\d.]+)', re.MULTILINE),
    "accuracy": re.compile(r'^\s*accuracy\s*=\s*([\d.]+)', re.MULTILINE),
}


def parse_test_script_baselines(filepath):
    """Parse a single test script file and extract baseline values."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return {}
    baselines = {}
    for attr, pattern in BASELINE_PATTERNS.items():
        match = pattern.search(content)
        if match:
            metric = ATTR_TO_METRIC[attr]
            try:
                baselines[metric] = float(match.group(1))
            except ValueError:
                pass
    return baselines


# 基线缓存：启动时从两个仓刷新一次，此后周期性自动刷新（TTL），
# 避免平台长时间运行期间脚本仓新增/更新用例而基线不更新。
BASELINES_CACHE_TTL = 600  # 秒
_baselines_cache = None
_baselines_cache_ts = 0.0
_baselines_lock = threading.RLock()  # 保护基线缓存的并发读写


def collect_baselines(force=False):
    """Scan all test scripts and collect baseline values.
    Returns a dict: {test_case_name: {metric: value, ...}}
    每次启动 dashboard 时通过 force=True 刷新；此后每 BASELINES_CACHE_TTL 秒自动重扫。
    """
    global _baselines_cache, _baselines_cache_ts
    now = time.time()
    with _baselines_lock:
        if not force and _baselines_cache is not None and (now - _baselines_cache_ts) < BASELINES_CACHE_TTL:
            return _baselines_cache

    results = {}
    for category in ["performance", "accuracy"]:
        for test_scripts_root in TEST_SCRIPTS_ROOTS:
            cat_dir = os.path.join(test_scripts_root, category)
            if not os.path.isdir(cat_dir):
                continue
            for dirpath, _, filenames in os.walk(cat_dir):
                for filename in filenames:
                    if not filename.endswith(".py") or filename.startswith("__"):
                        continue
                    test_case_name = filename[:-3]
                    filepath = os.path.join(dirpath, filename)
                    baselines = parse_test_script_baselines(filepath)
                    if baselines:
                        if test_case_name not in results:
                            results[test_case_name] = {}
                        results[test_case_name].update(baselines)
    with _baselines_lock:
        _baselines_cache = results
        _baselines_cache_ts = time.time()
    return results


# ============================================================
# 用例脚本 Git 平台链接
# 启动时（sync_repos 拉取最新脚本后）强制重建一次，此后每
# SCRIPT_URLS_CACHE_TTL 秒自动重扫，保证新增/更新用例的链接始终最新。
# 结果形如: {script_name: {source_name: web_url}}
#   script_name = test_npu_xxx.py 去掉后缀；source_name = fulltest/nightly
# ============================================================
SCRIPT_URLS_CACHE_TTL = 600  # 秒
_script_urls_cache = {}
_script_urls_cache_ts = 0.0
_script_urls_lock = threading.RLock()  # 保护脚本链接缓存的并发读写


def _normalize_web_url(url):
    """将 git 仓库地址归一化为网页基地址（去掉 .git 后缀，ssh 形式转 https）。"""
    url = re.sub(r"\.git$", "", (url or "").strip())
    m = re.match(r"^git@([^:]+):(.+)$", url)
    if m:
        url = "https://" + m.group(1) + "/" + m.group(2)
    return url.rstrip("/")


def _get_git_web_url(repo_root, repo_url):
    """获取仓库在 Git 平台上的网页访问基地址（不含 .git 后缀）。
    优先使用配置的 repo_url，为空时回退到本地 git remote origin。
    支持 https://host/org/repo.git 与 git@host:org/repo.git 两种形式。
    无法解析时返回空字符串。
    """
    url = (repo_url or "").strip()
    if not url:
        try:
            result = _run(
                ["git", "remote", "get-url", "origin"],
                capture_output=True, text=True, timeout=15,
                cwd=repo_root,
            )
            if result.returncode == 0:
                url = result.stdout.strip()
        except Exception:
            pass
    if not url:
        return ""
    return _normalize_web_url(url)


def _get_git_branch(repo_root):
    """获取仓库当前分支名，失败时返回空字符串。"""
    try:
        result = _run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=15,
            cwd=repo_root,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except Exception:
        pass
    return ""


def collect_script_urls(force=False):
    """扫描各测试脚本仓（test/registered/{ascend|npu}），构建脚本 → Git 平台链接映射。
    每次启动 dashboard 时通过 force=True 重建；此后每 SCRIPT_URLS_CACHE_TTL 秒自动重扫。
    """
    global _script_urls_cache, _script_urls_cache_ts
    now = time.time()
    with _script_urls_lock:
        if not force and _script_urls_cache and (now - _script_urls_cache_ts) < SCRIPT_URLS_CACHE_TTL:
            return _script_urls_cache

    results = {}
    for src_name, src_cfg in SOURCES.items():
        repo_root = src_cfg.get("repo_root", "")
        repo_url = src_cfg.get("repo_url", "")
        if not repo_root or not os.path.isdir(repo_root):
            continue
        web_base = _get_git_web_url(repo_root, repo_url)
        branch = _get_git_branch(repo_root)
        if not web_base or not branch:
            continue
        for sub in ("ascend", "npu"):
            scripts_root = os.path.join(repo_root, "test", "registered", sub)
            if not os.path.isdir(scripts_root):
                continue
            for dirpath, _, filenames in os.walk(scripts_root):
                for filename in filenames:
                    if not filename.endswith(".py") or filename.startswith("__"):
                        continue
                    script_name = filename[:-3]
                    rel_path = os.path.relpath(
                        os.path.join(dirpath, filename), repo_root
                    ).replace("\\", "/")
                    url = f"{web_base}/blob/{branch}/{rel_path}"
                    results.setdefault(script_name, {})[src_name] = url

    with _script_urls_lock:
        _script_urls_cache = results
        _script_urls_cache_ts = time.time()
    return results


def _match_script_urls(yaml_name, sources, script_urls):
    """根据用例 yaml_name 与其来源（fulltest/nightly）匹配脚本链接列表。
    yaml_name 可能带/不带 test_npu_ 前缀，两种形式都尝试。
    返回: [{"source": "fulltest", "url": "https://..."}, ...]
    """
    candidates = []
    if yaml_name:
        candidates.append(yaml_name)
        if not yaml_name.startswith("test_npu_"):
            candidates.append("test_npu_" + yaml_name)
    links = []
    for key in candidates:
        mapping = script_urls.get(key, {})
        if not mapping:
            continue
        for s in sources:
            url = mapping.get(s, "")
            if url and all(link["url"] != url for link in links):
                links.append({"source": s, "url": url})
        if links:
            break
    return links


def _resolve_repo_web_url(url):
    """将 repo_url 归一化为网页基地址（去掉 .git 后缀，ssh 形式转 https）。"""
    return _normalize_web_url(url)


def _get_repo_web_base_for_run(branch, source, run_workflow=""):
    """确定 CI 运行（GitHub Actions run）链接所属的仓库网页基地址。
    匹配优先级：
      0. 按数据实际来源的 workflow 目录（如 Nightly_Test_NPU → nightly）查 branch_repo_map；
      1. 按来源名（fulltest/nightly）查 branch_repo_map；
      2. 按分支前缀（最长优先）查 branch_repo_map；
      3. 回退到该来源配置的 base 仓（git remote）。
    无法解析时返回空字符串。
    """
    sources = [s.strip() for s in str(source or "").split(",") if s.strip()]
    # 0) 实际 workflow 目录优先（最精确：run 具体跑在哪个 workflow）。
    #    _iter_metrics_files 产出的 workflow 已是映射后的来源名（fulltest/nightly）。
    if run_workflow and run_workflow in BRANCH_REPO_MAP:
        web = _resolve_repo_web_url(BRANCH_REPO_MAP[run_workflow])
        if web:
            return web
    # 1) 来源名直查（如 "fulltest" / "nightly"）
    for s in sources:
        if s in BRANCH_REPO_MAP:
            web = _resolve_repo_web_url(BRANCH_REPO_MAP[s])
            if web:
                return web
    # 2) 分支前缀最长匹配（兼容分支模式数据目录 {branch}-{date}-{run_id}）
    if branch:
        for prefix in sorted(BRANCH_REPO_MAP, key=len, reverse=True):
            if branch.startswith(prefix):
                web = _resolve_repo_web_url(BRANCH_REPO_MAP[prefix])
                if web:
                    return web
    # 3) 回退来源配置的 base 仓
    for s in sources:
        src_cfg = SOURCES.get(s, {})
        repo_root = src_cfg.get("repo_root", "")
        if repo_root:
            web = _get_git_web_url(repo_root, src_cfg.get("repo_url", ""))
            if web:
                return web
    return ""


def _attach_script_urls(items):
    """为每个数据条目附加 script_urls（用例脚本在 Git 平台的链接）与 run_url（GitHub Actions 运行链接）。"""
    script_urls = collect_script_urls()
    for item in items:
        sources = [s.strip() for s in str(item.get("source", "")).split(",") if s.strip()]
        item["script_urls"] = _match_script_urls(item.get("yaml_name", ""), sources, script_urls)
        run_id = str(item.get("run_id", "") or "")
        if run_id:
            web_base = _get_repo_web_base_for_run(
                item.get("branch", ""), item.get("source", ""), item.get("run_workflow", "")
            )
            if web_base:
                item["run_url"] = f"{web_base}/actions/runs/{run_id}"

    # 解析到具体 job（GitHub Actions job_id），失败时保留 run_url 兜底
    # 新框架：matrix job 名含用例名；聚合 suite job 名 = suite 名（如 nightly-perf-2-npu-a3），
    # 用例通过 suite→用例 映射匹配到聚合 job。
    jobs_cache = fetch_run_jobs_for_items(items)
    case_suite_map = get_case_suite_map()
    for item in items:
        run_id = str(item.get("run_id", "") or "")
        run_url = item.get("run_url", "")
        if run_id and run_url:
            repo = _web_base_to_repo(run_url)
            jobs_for_run = jobs_cache.get((repo, run_id))
            job = _match_job_for_case_with_suite(item.get("yaml_name", ""), jobs_for_run, case_suite_map)
            if job:
                item["job_url"] = f"{run_url}/job/{job['job_id']}"
                # job 状态/结论用于前端区分「已执行但失败」与「尚未执行」
                item["job_status"] = job.get("status", "")
                item["job_conclusion"] = job.get("conclusion", "")
            elif jobs_for_run is not None:
                # 该 run 的 job 列表已抓取到但未匹配到本用例 → 该 run 未执行此用例
                item["job_status"] = "no_job"

    # 功能用例 per-case 状态：聚合 suite job 的结论是 suite 级，不能代表单个用例，
    # 需解析 suite job 日志得到每个功能用例的真实通过/失败（func_status: pass/fail/running）。
    # 解析结果由后台线程异步填充缓存，未解析到时前端回退到 job 结论归因。
    func_log_cache = fetch_func_logs_for_items(items)
    for item in items:
        if item.get("case_type") != "function":
            continue
        run_id = str(item.get("run_id", "") or "")
        run_url = item.get("run_url", "")
        if not run_id or not run_url:
            continue
        repo = _web_base_to_repo(run_url)
        if not repo:
            continue
        yaml_name = str(item.get("yaml_name", "") or "")
        base = re.sub(r"^test_npu_", "", yaml_name)
        suite = None
        for c in (yaml_name, base, "test_npu_" + base):
            if c in case_suite_map:
                suite = case_suite_map[c]
                break
        if not suite:
            continue
        entry = func_log_cache.get((repo, run_id, suite))
        if entry is None:
            continue
        if entry.get("running"):
            item["func_status"] = "running"
        else:
            pmap = entry.get("map", {})
            if base in pmap:
                item["func_status"] = "pass" if pmap[base] else "fail"


# ============================================================
# GitHub Actions job 级链接解析
# 通过 GitHub REST API 拉取每个 run 下的 jobs 列表并按用例名匹配，
# 生成直达具体 job 的链接（actions/runs/{run_id}/job/{job_id}）。
# 需要环境变量 GH_TOKEN / GITHUB_TOKEN（认证限流 5000 次/小时）；
# 未配置或调用失败时回退到 run 级链接。
# ============================================================
JOBS_CACHE_TTL = 600  # 秒：已完成（终态）job 的缓存时长，过期后不再重复请求
JOBS_REFRESH_INTERVAL = 60  # 秒：非终态（queued/in_progress）job 的刷新间隔，用于更新执行状态
JOBS_RETRY_INTERVAL = 300  # 秒：抓取失败后的退避重试间隔，避免频繁请求耗尽 API 配额
JOBS_API_TIMEOUT = 20  # 秒
_jobs_cache = {}       # {(repo, run_id): {case_name: {"job_id": ..., "name": ...}}}
_jobs_cache_ts = {}    # {(repo, run_id): 最近一次成功抓取时间}
_jobs_failed_ts = {}   # {(repo, run_id): 最近一次失败时间（退避用）}
_jobs_pending = set()  # 待后台抓取的 (repo, run_id)
_jobs_refresh_started = False
_jobs_fetch_logged = {}
_jobs_lock = threading.RLock()  # 保护 jobs 缓存系列变量的并发读写
_run_jobs_raw = {}     # {(repo, run_id): [job, ...]}  原始 job 列表（含重试 attempt），由 _fetch_run_jobs 填充，供功能用例日志解析使用


def _github_token():
    """读取 GitHub API token（环境变量 GH_TOKEN 或 GITHUB_TOKEN）。"""
    return os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or ""


def _web_base_to_repo(run_url):
    """从 run/job 链接中提取 owner/repo（如 https://github.com/sgl-project/sglang/actions/runs/... → sgl-project/sglang）。"""
    m = re.search(r"https://([^/]+)/([^/]+)/([^/]+)(?:/|$)", run_url)
    if m:
        return f"{m.group(2)}/{m.group(3)}"
    return ""


def _fetch_run_jobs(repo, run_id):
    """调用 GitHub API 获取指定 run 的 jobs 列表，返回 {case_name: {job_id, name}}。
    调用失败（网络/限流/token 无效）时返回 None。
    """
    if not repo or not run_id:
        return None
    token = _github_token()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "sglang-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    result = {}
    raw_jobs = []
    # GitHub API 单页上限 100 且默认返回第一页；run 的 job 数可能超过 100
    # （大规模 nightly 全套测试），需按 page 循环抓取避免数据丢失。
    per_page = 100
    max_pages = 20  # 上限 2000 个 job，足够覆盖所有真实场景，防止异常死循环
    try:
        for page in range(1, max_pages + 1):
            url = (
                f"https://api.github.com/repos/{repo}/actions/runs/{run_id}/jobs"
                f"?per_page={per_page}&page={page}"
            )
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=JOBS_API_TIMEOUT) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            jobs = data.get("jobs", [])
            raw_jobs.extend(jobs)
            for job in jobs:
                name = job.get("name", "")
                job_id = job.get("id")
                if not name or job_id is None:
                    continue
                # 保存 status/conclusion，用于区分「已执行但失败」与「尚未执行」
                job_info = {
                    "job_id": str(job_id),
                    "name": name,
                    "status": str(job.get("status", "") or ""),
                    "conclusion": str(job.get("conclusion", "") or ""),
                }
                for case in _extract_case_names(name):
                    result[case] = job_info
            # 本页未满 100 个说明没有下一页，提前退出
            if len(jobs) < per_page:
                break
    except Exception as e:
        key = (repo, run_id)
        if _jobs_fetch_logged.get(key) != str(e):
            _jobs_fetch_logged[key] = str(e)
            print(f"[jobs] fetch failed for {repo}/{run_id}: {e}")
        return None
    with _jobs_lock:
        _run_jobs_raw[(repo, run_id)] = raw_jobs
    return result


def _extract_case_names(job_name):
    """从 job name 中提取候选用例名（去重保序）。
    实际格式：single-node-poc (qwen3_6_35b_a3b_1p_aime26, runner, test/... / qwen3_6_35b_a3b_1p_aime26
    提取括号内第一个字段与末尾 / 后的字段，并去掉 test_npu_ 前缀。
    聚合 suite job 名形如 "nightly-1-npu-a3 / run (0)" 或
    "nightly-perf-2-npu-a3 / nightly-perf-2-npu-a3"：额外提取 " / " 前的
    suite 名作为候选 key，供 _match_job_for_case_with_suite 按 suite 匹配。
    """
    cases = []
    m = re.search(r"\(\s*([^,()]+?)\s*,", job_name)
    if m:
        c = m.group(1).strip()
        if c:
            cases.append(c)
    m = re.search(r"/\s*([^\s/()]+)\s*$", job_name)
    if m:
        c = m.group(1).strip()
        if c:
            cases.append(c)
    # 聚合 suite job：" / " 分隔的两段中，干净标识符（无括号/逗号）均提取为候选 key。
    # 实际命名变体：前后一致（nightly-perf-16-npu-a3 / nightly-perf-16-npu-a3）、
    # 尾段为 suite（nightly-acc-2-npu-a3 (part 0/3) / nightly-acc-2-npu-a3）、
    # 首段为展示名/尾段为 suite（single-node-mix-a2 / nightly-mix-1-npu-a2）。
    if " / " in job_name:
        for part in job_name.split(" / "):
            part = part.strip()
            if part and not any(ch in part for ch in "(),"):
                cases.append(part)
    result = []
    for c in cases:
        c = re.sub(r"^test_npu_", "", c)
        if c and c not in result:
            result.append(c)
    return result


def _match_job_for_case(case_key, jobs):
    """按用例名匹配 job。jobs 形如 {case_name: {job_id, name}}。
    兼容 yaml_name 带/不带 test_npu_ 前缀、带/不带 _a2 后缀。
    """
    if not jobs:
        return None
    candidates = []
    if case_key:
        candidates.append(case_key)
        if case_key.startswith("test_npu_"):
            candidates.append(case_key[len("test_npu_"):])
        else:
            candidates.append("test_npu_" + case_key)
    # 末尾 _a2 芯片标记差异容错
    for c in list(candidates):
        if c.endswith("_a2"):
            candidates.append(c[:-3])
        else:
            candidates.append(c + "_a2")
    for c in candidates:
        if c in jobs:
            return jobs[c]
    return None


def fetch_run_jobs_for_items(items):
    """读取 jobs 缓存；将数据中未缓存或需刷新/重试的 (repo, run_id) 提交到后台线程，不阻塞当前请求。
    返回缓存字典 {(repo, run_id): {case_name: {job_id, name}}}。
    调度规则：
      - 未缓存且距上次失败超过退避间隔 → 加入抓取队列
      - 已缓存但存在非终态 job（queued/in_progress）且超过刷新间隔 → 重新抓取以更新状态
      - 已缓存且全部为终态 → 不再重复请求（避免浪费 API 配额）
    """
    global _jobs_cache
    now = time.time()
    pairs = {}
    for item in items:
        run_id = str(item.get("run_id", "") or "")
        run_url = item.get("run_url", "")
        if not run_id or not run_url:
            continue
        repo = _web_base_to_repo(run_url)
        if repo and run_id:
            pairs[(repo, run_id)] = True
    # 加锁保护缓存的读取与任务入队，避免与后台抓取线程产生竞态
    with _jobs_lock:
        for p in pairs:
            cached = _jobs_cache.get(p)
            if cached is None:
                # 未缓存：失败退避后重试
                last_fail = _jobs_failed_ts.get(p, 0)
                if now - last_fail >= JOBS_RETRY_INTERVAL:
                    _jobs_pending.add(p)
            elif _has_incomplete_jobs(cached):
                # 存在执行中的 job：超过刷新间隔后重新抓取，保证状态更新
                # 同时尊重失败退避，避免持续失败导致高频重试
                last_ts = _jobs_cache_ts.get(p, 0)
                last_fail = _jobs_failed_ts.get(p, 0)
                if now - last_ts >= JOBS_REFRESH_INTERVAL and now - last_fail >= JOBS_RETRY_INTERVAL:
                    _jobs_pending.add(p)
            # 全部终态：保持缓存，不重复请求
    _ensure_jobs_thread()
    # 返回快照，避免外部调用方在后台线程更新缓存时遍历被修改的字典
    with _jobs_lock:
        return {k: dict(v) for k, v in _jobs_cache.items()}


def _has_incomplete_jobs(jobs):
    """判断缓存中的 jobs 是否存在非终态（queued/in_progress/waiting 等）条目。"""
    for info in jobs.values():
        status = str(info.get("status", "") or "")
        if status and status != "completed":
            return True
    return False


def _ensure_jobs_thread():
    """确保后台 jobs 刷新线程已启动（单次）。"""
    global _jobs_refresh_started
    with _jobs_lock:
        if _jobs_refresh_started:
            return
        _jobs_refresh_started = True
    t = threading.Thread(target=_jobs_refresh_worker, daemon=True)
    t.start()


def _jobs_refresh_worker():
    """后台线程：逐个抓取待处理 (repo, run_id) 的 jobs 并写入缓存。
    记录成功/失败时间戳，供调度逻辑（刷新间隔 / 退避重试）使用。
    周期性淘汰超过 TTL 且已终态的缓存条目，防止长期运行内存无限增长。
    """
    global _jobs_cache
    while True:
        try:
            p = None
            # 锁内取任务，锁外执行网络请求，避免长时间持锁
            with _jobs_lock:
                if _jobs_pending:
                    p = _jobs_pending.pop()
            if p is not None:
                fetched = _fetch_run_jobs(p[0], p[1])
                with _jobs_lock:
                    if fetched is not None:
                        _jobs_cache[p] = fetched
                        _jobs_cache_ts[p] = time.time()
                        _jobs_failed_ts.pop(p, None)
                    else:
                        _jobs_failed_ts[p] = time.time()
            # 淘汰过期缓存：仅淘汰超过 TTL 且全部为终态（completed）的条目，
            # 避免淘汰仍在执行中、需要持续刷新的 job
            with _jobs_lock:
                now = time.time()
                stale = [
                    k for k, ts in _jobs_cache_ts.items()
                    if now - ts > JOBS_CACHE_TTL and not _has_incomplete_jobs(_jobs_cache.get(k))
                ]
                for k in stale:
                    _jobs_cache.pop(k, None)
                    _jobs_cache_ts.pop(k, None)
                    _jobs_failed_ts.pop(k, None)
                    _jobs_pending.discard(k)
        except Exception as e:
            print(f"[jobs] worker error: {e}")
        time.sleep(2)


def force_refresh_jobs():
    """启动时清空 jobs 缓存，让后台线程对当前数据重新抓取。"""
    global _jobs_cache
    with _jobs_lock:
        _jobs_cache = {}
        _jobs_cache_ts.clear()
        _jobs_failed_ts.clear()
    return _jobs_cache


# ============================================================
# 功能用例 per-case 状态：解析聚合 suite job 日志
# 聚合 suite job（如 nightly-1-npu-a3）一次运行多个功能用例，其 conclusion 是
# suite 级（一个用例失败整套失败），不能代表单个功能用例的实际结果。
# 需下载该 suite job 日志，解析 JSON 行 {"file": "...", "passed": ...}
# 得到每个功能用例的真实通过/失败。重试 job（run (N)）取最高 attempt 日志。
# ============================================================
FUNC_LOG_CACHE_TTL = 12 * 3600      # 秒：已完成 suite job 日志缓存时长（终态日志不变）
FUNC_LOG_REFRESH_INTERVAL = 120     # 秒：suite job 仍在执行中时的刷新间隔
FUNC_LOG_RETRY_INTERVAL = 600       # 秒：日志下载失败后的退避重试间隔
FUNC_LOG_API_TIMEOUT = 90           # 秒：日志下载超时（日志较大）
_func_log_cache = {}       # {(repo, run_id, suite): {case: passed_bool}}，缺失=日志中未找到该用例
_func_log_running = {}     # {(repo, run_id, suite): bool}  该 suite 是否有 job 仍在执行中
_func_log_ts = {}          # {(repo, run_id, suite): 最近成功抓取时间}
_func_log_failed_ts = {}   # {(repo, run_id, suite): 最近失败时间（退避用）}
_func_log_pending = set()  # 待后台抓取的 (repo, run_id, suite)
_func_log_started = False
_func_log_lock = threading.RLock()  # 保护 func-log 缓存系列变量的并发读写


class _NoAuthRedirect(urllib.request.HTTPRedirectHandler):
    """GitHub 日志下载会 302 重定向到带签名的对象存储 URL，
    重定向时需剥离 Authorization 头，否则签名 URL 校验失败返回 401。"""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        newreq = super().redirect_request(req, fp, code, msg, headers, newurl)
        if newreq is not None:
            newreq.headers.pop("Authorization", None)
        return newreq


def _download_job_log(repo, job_id):
    """下载 GitHub Actions job 日志文本；失败返回 None。"""
    if not repo or not job_id:
        return None
    token = _github_token()
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "sglang-dashboard",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    url = f"https://api.github.com/repos/{repo}/actions/jobs/{job_id}/logs"
    try:
        req = urllib.request.Request(url, headers=headers)
        opener = urllib.request.build_opener(_NoAuthRedirect())
        with opener.open(req, timeout=FUNC_LOG_API_TIMEOUT) as resp:
            return resp.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"[func-log] download failed {repo}/{job_id}: {e}")
        return None


def _parse_func_log(log_text):
    """从 job 日志解析 per-case 结果：{"file": "...", "passed": ...} 行 → {case_name: passed}。"""
    result = {}
    if not log_text:
        return result
    for line in log_text.splitlines():
        ln = re.sub(r"^.*?Z ", "", line).strip()
        if ln.startswith('{"file"') and '"passed"' in ln and '"elapsed"' in ln:
            try:
                obj = json.loads(ln)
                fname = obj.get("file", "")
                base = os.path.basename(fname).replace(".py", "")
                c = re.sub(r"^test_npu_", "", base)
                if c:
                    result[c] = bool(obj.get("passed"))
            except Exception:
                pass
    return result


def _attempt_of(job_name):
    """从聚合 job 名提取重试序号："nightly-1-npu-a3 / run (2)" → 2；无重试 → 0。"""
    m = re.search(r"/ run\s*\(\s*(\d+)\s*\)", job_name or "")
    return int(m.group(1)) if m else 0


def _ensure_func_log_thread():
    global _func_log_started
    with _func_log_lock:
        if _func_log_started:
            return
        _func_log_started = True
    t = threading.Thread(target=_func_log_worker, daemon=True)
    t.start()


def _func_log_worker():
    """后台线程：逐个抓取待处理 (repo, run_id, suite) 的 per-case 日志结果并写入缓存。
    周期性淘汰超过 TTL 且已终态（无运行中 job）的缓存条目。
    """
    while True:
        try:
            key = None
            with _func_log_lock:
                if _func_log_pending:
                    key = _func_log_pending.pop()
            if key is not None:
                _fetch_func_log(key)
            with _func_log_lock:
                now = time.time()
                stale = [
                    k for k, ts in _func_log_ts.items()
                    if now - ts > FUNC_LOG_CACHE_TTL and not _func_log_running.get(k)
                ]
                for k in stale:
                    _func_log_cache.pop(k, None)
                    _func_log_running.pop(k, None)
                    _func_log_ts.pop(k, None)
                    _func_log_failed_ts.pop(k, None)
                    _func_log_pending.discard(k)
        except Exception as e:
            print(f"[func-log] worker error: {e}")
        time.sleep(2)


def _fetch_func_log(key):
    """抓取一个 (repo, run_id, suite) 的 per-case 日志结果写入缓存。
    取该 run 原始 job 列表中匹配该 suite 的全部 job（含重试），
    任一 job 仍在执行中则标记 running（稍后刷新）；否则按 attempt 从高到低
    下载最高 attempt 已完成 job 的日志解析 per-case 状态。
    """
    repo, run_id, suite = key
    with _jobs_lock:
        raw = list(_run_jobs_raw.get((repo, run_id), []))
    if not raw:
        # 原始 job 列表未缓存：先抓取一次 jobs（同时填充 _run_jobs_raw）
        _fetch_run_jobs(repo, run_id)
        with _jobs_lock:
            raw = list(_run_jobs_raw.get((repo, run_id), []))
        if not raw:
            _func_log_failed_ts[key] = time.time()
            return
    matches = []
    for j in raw:
        name = str(j.get("name", "") or "")
        if name == suite or name.startswith(suite + " /") or name.startswith(suite + "/"):
            matches.append((_attempt_of(name), j))
    if not matches:
        # 该 run 未执行此 suite → 该 suite 全部用例无结果
        _func_log_cache[key] = {}
        _func_log_running[key] = False
        _func_log_ts[key] = time.time()
        return
    if any(str(j.get("status", "") or "") != "completed" for _, j in matches):
        # 存在执行中的 job：标记 running，由调度按刷新间隔重新抓取
        _func_log_running[key] = True
        _func_log_ts[key] = time.time()
        return
    _func_log_running[key] = False
    # 合并所有已完成 attempt 的 per-case 结果：重试 job（run (N)）与首次运行
    # 可能运行不同的用例子集（如重试只补跑部分用例），需解析全部日志补齐缺口。
    # 同一用例多个 attempt 都有结果时，高 attempt（最终状态）优先。
    merged = {}
    for _, j in sorted(matches, key=lambda x: x[0], reverse=True):
        if str(j.get("status", "") or "") != "completed":
            continue
        log_text = _download_job_log(repo, j.get("id"))
        if log_text is None:
            continue
        for c, passed in _parse_func_log(log_text).items():
            if c not in merged:
                merged[c] = passed
    if merged:
        _func_log_cache[key] = merged
        _func_log_ts[key] = time.time()
        _func_log_failed_ts.pop(key, None)
        return
    _func_log_failed_ts[key] = time.time()


def fetch_func_logs_for_items(items):
    """为功能用例调度聚合 suite job 日志抓取（后台线程，不阻塞请求），返回缓存快照。
    返回 {(repo, run_id, suite): {"map": {case: passed}, "running": bool}}。
    调度规则：
      - 未缓存且距上次失败超过退避间隔 → 加入抓取队列
      - 已缓存但 suite job 仍在执行中且超过刷新间隔 → 重新抓取
      - 已缓存且已终态 → 不再重复请求
    """
    now = time.time()
    pairs = {}
    case_suite_map = get_case_suite_map()
    for item in items:
        if item.get("case_type") != "function":
            continue
        run_id = str(item.get("run_id", "") or "")
        run_url = item.get("run_url", "")
        if not run_id or not run_url:
            continue
        repo = _web_base_to_repo(run_url)
        if not repo:
            continue
        yaml_name = str(item.get("yaml_name", "") or "")
        base = re.sub(r"^test_npu_", "", yaml_name)
        suite = None
        for c in (yaml_name, base, "test_npu_" + base):
            if c in case_suite_map:
                suite = case_suite_map[c]
                break
        if not suite:
            continue
        pairs[(repo, run_id, suite)] = True
    with _func_log_lock:
        for k in pairs:
            cached = _func_log_cache.get(k)
            if cached is not None:
                if _func_log_running.get(k) and now - _func_log_ts.get(k, 0) >= FUNC_LOG_REFRESH_INTERVAL:
                    _func_log_pending.add(k)
                continue
            last_fail = _func_log_failed_ts.get(k, 0)
            if now - last_fail >= FUNC_LOG_RETRY_INTERVAL:
                _func_log_pending.add(k)
    _ensure_func_log_thread()
    with _func_log_lock:
        return {
            k: {"map": dict(v), "running": bool(_func_log_running.get(k, False))}
            for k, v in _func_log_cache.items()
        }


_nnodes_cache = {}
_nnodes_lock = threading.RLock()  # 保护 nnodes 缓存


def _get_nnodes_from_script(yaml_name):
    """Read the test script for a given yaml_name and return the nnodes value.
    Returns 1 if not found or not configured."""
    with _nnodes_lock:
        if yaml_name in _nnodes_cache:
            return _nnodes_cache[yaml_name]
    test_file = "test_npu_" + yaml_name + ".py"
    for test_scripts_root in TEST_SCRIPTS_ROOTS:
        for root, _, files in os.walk(test_scripts_root):
            if test_file in files:
                filepath = os.path.join(root, test_file)
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()
                    # 兼容实际脚本的多种写法："--nnodes",\n"1" / --nnodes 1 / --nnodes=1 /
                    # --nnodes\n1（旧正则 `--nnodes\s*\n\s*(\d+)` 无法匹配带引号/逗号的格式）
                    nnodes_vals = []
                    for m in re.finditer(r"--nnodes[^\d]*?(\d+)", content):
                        nnodes_vals.append(int(m.group(1)))
                    if nnodes_vals:
                        # 取最小 nnodes：任一阶段为单节点即按单机处理（PD 分离常见 prefill 单节点）
                        val = min(nnodes_vals)
                    else:
                        val = 1  # Not configured, default to 1
                    with _nnodes_lock:
                        _nnodes_cache[yaml_name] = val
                    return val
                except Exception:
                    pass
                break
    with _nnodes_lock:
        _nnodes_cache[yaml_name] = 1
    return 1

def compute_topology_info(yaml_name):
    """Compute topology, card count, and sequence length from yaml_name.
    Returns (topology, card_count, seq_length) tuple."""
    # 组网: check PD分离 first
    pd_match = re.search(r'_(\d+p\d+d)', yaml_name)
    if pd_match:
        topology = f"PD分离/{pd_match.group(1)}"
    else:
        nnodes = _get_nnodes_from_script(yaml_name)
        topology = "单机混部" if nnodes <= 1 else "多机混部"

    # 卡数: extract xxp from parallelism section (skip xpxd PD patterns)
    card_count = ""
    p_match = re.search(r'_(\d+p\d*d?(?:_\d+p)?)(?=_|$)', yaml_name)
    if p_match:
        parallelism = p_match.group(1)
        total = 0
        for part in parallelism.split('_'):
            # Skip PD separation patterns like 1p1d, 2p1d
            if re.search(r'\d+p\d+d', part):
                continue
            n = re.search(r'(\d+)p', part)
            if n:
                total += int(n.group(1))
        if total > 0:
            card_count = f"{total}卡"

    # 序列长度: extract in/out
    # 多模态用例（如 in1024x1024、in1080p）不显示序列长度，返回空 → 前端显示 "--"
    seq_length = ""
    multimodal = bool(re.search(r'1024x1024|1080p', yaml_name))
    if not multimodal:
        in_match = re.search(r'_in(\d+k?\d*)', yaml_name)
        out_match = re.search(r'_out(\d+k?\d*)', yaml_name)
        if in_match and out_match:
            seq_length = f"in{in_match.group(1)}_out{out_match.group(1)}"
        elif in_match:
            seq_length = f"in{in_match.group(1)}"
        elif out_match:
            seq_length = f"out{out_match.group(1)}"

    return topology, card_count, seq_length

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SGLang Benchmark 性能分析平台</title>
<script src="__CHART_JS_SRC__"></script>
<script src="__XLSX_SRC__"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0d1117; color: #c9d1d9; }
.header { background: #161b22; border-bottom: 1px solid #30363d; padding: 16px 24px; display: flex; align-items: center; justify-content: space-between; }
.header h1 { font-size: 20px; color: #58a6ff; }
.header .info { font-size: 13px; color: #8b949e; }
.filters { background: #161b22; border-bottom: 1px solid #30363d; padding: 12px 24px; display: flex; gap: 12px; flex-wrap: wrap; align-items: flex-end; }
.filter-group { display: flex; flex-direction: column; gap: 4px; }
.filter-group label { font-size: 11px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; }
.filter-group select { background: #21262d; color: #c9d1d9; border: 1px solid #30363d; border-radius: 6px; padding: 6px 10px; font-size: 13px; min-width: 120px; max-width: 200px; }
.filter-group select:focus { outline: none; border-color: #58a6ff; }
.filter-group select[multiple] { height: 120px; }
.btn { background: #238636; color: #fff; border: none; border-radius: 6px; padding: 7px 16px; font-size: 13px; cursor: pointer; }
.btn:hover { background: #2ea043; }
.btn-reset { background: #21262d; color: #c9d1d9; border: 1px solid #30363d; }
.btn-reset:hover { background: #30363d; }
.btn-danger { background: #21262d; color: #f85149; border: 1px solid #f85149; }
.btn-danger:hover { background: #da3633; color: #fff; border-color: #da3633; }
.table-container { padding: 0 24px 20px; }
.table-container h3 { font-size: 14px; color: #8b949e; margin-bottom: 12px; }
.table-wrap { overflow: auto; max-height: calc(100vh - 320px); min-height: 300px; border: 1px solid #30363d; border-radius: 8px; }
/* 滚动条深色风格（贴合页面背景） */
.table-wrap::-webkit-scrollbar { width: 10px; height: 10px; }
.table-wrap::-webkit-scrollbar-track { background: #161b22; }
.table-wrap::-webkit-scrollbar-thumb { background: #30363d; border-radius: 5px; border: 2px solid #161b22; }
.table-wrap::-webkit-scrollbar-thumb:hover { background: #484f58; }
.table-wrap::-webkit-scrollbar-corner { background: #161b22; }
.table-wrap { scrollbar-width: thin; scrollbar-color: #30363d #161b22; }
table { width: 2785px; table-layout: fixed; border-collapse: separate; border-spacing: 0; background: #161b22; }
th { background: #21262d; padding: 10px 4px; text-align: left; font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #30363d; cursor: pointer; white-space: normal; overflow: hidden; text-overflow: ellipsis; display: table-cell; -webkit-line-clamp: 2; line-clamp: 2; }
th:hover { color: #c9d1d9; }
td { padding: 8px 4px; font-size: 13px; border-bottom: 1px solid #21262d; white-space: normal; overflow-wrap: anywhere; word-break: break-all; }
tr:hover { background: #1c2128; }
tr.selected { background: #1f3a5f !important; }
tr.selected:hover { background: #254070 !important; }
.no-data { text-align: center; padding: 40px; color: #8b949e; }
.testcase-id { font-family: 'Consolas', 'Courier New', monospace; font-size: 12px; color: #58a6ff; white-space: normal; overflow-wrap: anywhere; word-break: break-all; }
.script-link { color: #58a6ff; text-decoration: none; font-size: 12px; margin-right: 6px; white-space: normal; overflow-wrap: anywhere; word-break: break-all; display: inline-block; }
.script-link:hover { text-decoration: underline; color: #79c0ff; }
.status-pass { color: #7ee787; font-weight: 700; }
.status-fail { color: #ff7b72; font-weight: 700; }
.status-none { color: #ff7b72; font-weight: 700; }
/* 已执行成功但无结果数据（CI job conclusion=success 但无指标）→ 绿色，区别于失败/未执行 */
.status-success-nr { color: #7ee787; font-weight: 700; }
/* CI job 执行中 */
.status-running { color: #d29922; font-weight: 700; }
/* 功能用例聚合明细行：浅色底纹 + 左侧缩进，区别于普通数据行 */
.func-detail-row { background: rgba(88, 166, 255, 0.04); }
.func-detail-row td { border-top: 1px dashed rgba(88, 166, 255, 0.12); }
.baseline-val { font-size: 11px; color: #8b949e; }
.metric-fail { color: #ff7b72; font-weight: 700; }
.baseline-col { font-size: 11px; color: #8b949e; display: block; width: 100%; white-space: normal; overflow-wrap: anywhere; word-break: break-all; }
.col-note { white-space: normal; overflow-wrap: anywhere; word-break: break-all; }
.note-cell { display: flex; align-items: flex-start; }
.note-text { color: #e6edf3; font-size: 12px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; line-height: 1.4; max-height: 2.8em; flex: 1; min-width: 0; }
.note-date { color: #8b949e; font-size: 11px; flex-shrink: 0; margin-left: 4px; line-height: 1.4; white-space: nowrap; }
.note-edit { cursor: pointer; color: #58a6ff; font-size: 12px; flex-shrink: 0; margin-right: 4px; line-height: 1.4; }
.note-edit:hover { color: #79c0ff; }
.chart-row td { padding: 0; background: #0d1117; }
.tc-charts { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; padding: 12px; background: #0d1117; }
.tc-chart-box { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 8px; }
.tc-chart-box h4 { font-size: 12px; color: #8b949e; margin: 0 0 4px 0; }
.tc-chart-box canvas { max-height: 200px; }
.expand-icon { display: inline-block; width: 14px; font-size: 10px; transition: transform 0.2s; }
/* 测试结果列（精度列起）：等宽 + 居中，数字等宽；宽度容纳最长结果数字，数字不换行 */
.col-uniform { width: 76px; min-width: 76px; text-align: center; white-space: normal; overflow-wrap: anywhere; word-break: break-all; font-variant-numeric: tabular-nums; }
/* 配置列（组网/卡数/序列长度/prefix/数据集）：等宽 + 居中 */
.col-config { width: 44px; text-align: center; white-space: normal; overflow-wrap: anywhere; word-break: break-all; }
/* 组网列单独：比其它配置列稍宽（PD分离两行显示） */
.col-topology { width: 64px; text-align: center; white-space: normal; overflow-wrap: anywhere; word-break: break-all; }
/* 左侧元数据列宽度：尽量一致 */
th.col-meta { width: 64px; }
td.col-meta { width: 64px; }
th.col-model { width: 104px; }
td.col-model { width: 104px; }
th.col-tc-id { width: 224px; }
td.col-tc-id { width: 224px; }
th.col-script { width: 74px; }
td.col-script { width: 74px; }
th.col-note, td.col-note { width: 220px; }
th.col-baseline { width: 100px; }
td.col-baseline { width: 100px; }
/* 左侧元数据列锁定：横向滚动时固定不滚动（锁定到基线列，含基线） */
.sticky-col, thead th.sticky-col { position: sticky; z-index: 3; background: #21262d; }
tbody td.sticky-col { background: #161b22; }
tbody tr:hover td.sticky-col { background: #1c2128; }
tbody tr.selected td.sticky-col { background: #1f3a5f !important; }
tbody tr.selected:hover td.sticky-col { background: #254070 !important; }
.col-l0 { left: 0; }
.col-l1 { left: 104px; }
.col-l2 { left: 328px; }
.col-l3 { left: 392px; }
.col-l4 { left: 456px; }
.col-l5 { left: 530px; }
.col-l6 { left: 594px; }
.col-l7 { left: 773px; }
/* 表头 sticky（垂直滚动时表头固定） */
thead th { position: sticky; top: 0; z-index: 4; }
thead th.sticky-col { z-index: 5; }
</style>
</head>
<body>
<div class="header">
  <h1>SGLang Benchmark 性能分析平台</h1>
  <div class="info"><span id="dataSource"></span> | <span id="updateTime"></span></div>
</div>
<div class="filters">
  <div class="filter-group">
    <label>模型</label>
    <select id="modelFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>日期</label>
    <select id="dateFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>来源</label>
    <select id="sourceFilter" multiple onchange="onFilterChange()">
      <option value="__all__" selected>全部</option>
      <option value="fulltest">fulltest</option>
      <option value="nightly">nightly</option>
    </select>
  </div>
  <div class="filter-group">
    <label>分支</label>
    <select id="branchFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>状态</label>
    <select id="statusFilter" multiple onchange="onFilterChange()">
      <option value="__all__" selected>全部</option>
      <option value="PASS">PASS</option>
      <option value="FAILED">FAILED</option>
    </select>
  </div>
  <div class="filter-group">
    <label>历史天数</label>
    <input type="number" id="historyDays" value="7" min="1" max="365" onchange="applyHistoryFilter()" style="width:70px;padding:5px;background:#161b22;color:#e6edf3;border:1px solid #30363d;border-radius:6px;">
  </div>
  <button class="btn btn-reset" onclick="resetFilters()">重置筛选</button>
  <button class="btn" onclick="exportToExcel()">导出Excel</button>
</div>
<div class="table-container">
  <h3>详细数据 <span style="font-weight:normal;font-size:12px;color:#8b949e" id="tableCount"></span></h3>
  <div class="table-wrap">
  <table id="dataTable">
    <thead>
      <tr>
        <th class="col-model sticky-col col-l0">模型</th>
        <th class="col-tc-id sticky-col col-l1">测试用例ID</th>
        <th class="col-meta sticky-col col-l2">日期</th>
        <th class="col-meta sticky-col col-l3">状态</th>
        <th class="col-script sticky-col col-l4">用例脚本</th>
        <th class="col-meta sticky-col col-l5">任务</th>
        <th class="col-note sticky-col col-l6">备注</th>
        <th class="col-baseline sticky-col col-l7">基线</th>
        <th class="col-topology">组网</th>
        <th class="col-config">卡数</th>
        <th class="col-config">序列</th>
        <th class="col-config">prefix</th>
        <th class="col-config">数据集</th>
        <th class="col-uniform">精度</th>
        <th class="col-uniform">总请求数</th>
        <th class="col-uniform">最大并发数</th>
        <th class="col-uniform">系统并发数</th>
        <th class="col-uniform">请求频率<br>(req/s)</th>
        <th class="col-uniform">TTFT<br>(ms)</th>
        <th class="col-uniform">TTFT P90<br>(ms)</th>
        <th class="col-uniform">TPOT<br>(ms)</th>
        <th class="col-uniform">TPOT P90<br>(ms)</th>
        <th class="col-uniform">E2E时间<br>(ms)</th>
        <th class="col-uniform">输出吞吐<br>(tps)</th>
        <th class="col-uniform">单卡<br>输出吞吐<br>(tps)</th>
        <th class="col-uniform">E2E 吞吐<br>(tps)</th>
        <th class="col-uniform">单卡<br>E2E 吞吐<br>(tps)</th>
        <th class="col-uniform">QPS</th>
        <th class="col-uniform">QPM</th>
      </tr>
    </thead>
    <tbody id="tableBody"></tbody>
  </table>
  </div>
</div>

<!-- 备注编辑弹窗 -->
<div id="noteModal" style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(0,0,0,.55);z-index:1000;align-items:center;justify-content:center;">
  <div style="background:#161b22;border:1px solid #30363d;border-radius:8px;padding:16px;width:480px;max-width:92vw;">
    <h4 style="margin:0 0 6px;color:#e6edf3;">填写执行结果备注</h4>
    <div style="font-size:12px;color:#8b949e;margin-bottom:4px;word-break:break-all;" id="noteModalTc"></div>
    <div style="font-size:12px;color:#8b949e;margin-bottom:10px;" id="noteModalExec"></div>
    <textarea id="noteInput" rows="4" placeholder="输入该执行结果的备注..." style="width:100%;box-sizing:border-box;background:#0d1117;color:#e6edf3;border:1px solid #30363d;border-radius:6px;padding:8px;font-size:13px;"></textarea>
    <div style="margin-top:12px;display:flex;justify-content:space-between;align-items:center;">
      <button class="btn btn-danger" onclick="clearCaseNotes()">清理该用例所有历史备注</button>
      <span>
        <button class="btn btn-reset" onclick="closeNoteEditor()">取消</button>
        <button class="btn" onclick="saveNote()">保存</button>
      </span>
    </div>
  </div>
</div>

<script>
let allData = [];
let charts = {};

function buildTestCaseId(d) {
  return d.yaml_name || '';
}

function initCharts() {
  // Charts are created dynamically when a test case row is expanded
}

function showTestCaseChart(tcId, label) {
  // 仅保留有执行结果的条目：无结果日期不显示在折线图中，保证折线连续
  const items = allData.filter(d => d._id === tcId && hasData(d));
  items.sort((a, b) => a.date.localeCompare(b.date));
  const dates = items.map(d => d.date);

  const chartRow = document.getElementById('chart_' + tcId.replace(/[^a-zA-Z0-9]/g, '_'));
  if (!chartRow) return;

  // Chart.js 未加载（如内网无法访问 CDN）时给出提示而非静默失败
  if (typeof Chart === 'undefined') {
    chartRow.querySelector('td').innerHTML =
      '<div style="padding:12px;color:#8b949e;font-size:13px;">图表库加载失败（无法访问 CDN），历史数据仍可在表格中查看。</div>';
    return;
  }

  // Build chart definitions from baseline keys
  const baselineMetricDefs = {
    mean_ttft:     { key: 'mean_ttft', label: 'TTFT (ms)', color: '#f78166' },
    mean_tpot:     { key: 'mean_tpot', label: 'TPOT (ms)', color: '#d2a8ff' },
    mean_e2e_latency: { key: 'mean_e2e_latency', label: 'E2E时间 (ms)', color: '#ff7b72' },
    output_token_throughput: { key: 'output_token_throughput', label: '输出吞吐 (tps)', color: '#7ee787' },
    eval_score:    { key: 'eval_score', label: 'Accuracy', color: '#e3b341' },
  };
  // Get baselines from the first item that has them
  const baseline = items.find(d => d.baselines && Object.keys(d.baselines).length > 0);
  const metricDefs = [];
  if (baseline) {
    for (const [key, def] of Object.entries(baselineMetricDefs)) {
      if (baseline.baselines[key] != null) {
        metricDefs.push(def);
      }
    }
  }

  const commonOpts = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { display: false }
    },
    scales: {
      x: { ticks: { color: '#8b949e', font: { size: 10 } }, grid: { color: '#21262d' } },
      y: { ticks: { color: '#8b949e', font: { size: 10 } }, grid: { color: '#21262d' } }
    },
    interaction: { mode: 'index', intersect: false }
  };

  let html = '<div class="tc-charts">';
  metricDefs.forEach((def, i) => {
    const vals = items.map(d => d[def.key]);
    if (vals.some(v => v != null)) {
      const canvasId = 'chart_' + tcId.replace(/[^a-zA-Z0-9]/g, '_') + '_' + def.key;
      html += `<div class="tc-chart-box"><h4>${def.label}</h4><canvas id="${canvasId}"></canvas></div>`;
    }
  });
  html += '</div>';
  chartRow.querySelector('td').innerHTML = html;

  // Create charts after DOM is updated
  setTimeout(() => {
    metricDefs.forEach(def => {
      const vals = items.map(d => d[def.key]);
      if (vals.some(v => v != null)) {
        const canvasId = 'chart_' + tcId.replace(/[^a-zA-Z0-9]/g, '_') + '_' + def.key;
        const canvas = document.getElementById(canvasId);
        if (canvas) {
          new Chart(canvas, {
            type: 'line',
            data: {
              labels: dates,
              datasets: [{
                label: def.label,
                data: vals,
                borderColor: def.color,
                backgroundColor: def.color + '30',
                borderWidth: 2,
                pointRadius: 3,
                pointHoverRadius: 5,
                tension: 0.1,
                spanGaps: false,
              }]
            },
            options: commonOpts
          });
        }
      }
    });
  }, 10);
}

function destroyCharts(tcId) {
  const chartRow = document.getElementById('chart_' + tcId.replace(/[^a-zA-Z0-9]/g, '_'));
  if (chartRow) {
    chartRow.querySelector('td').innerHTML = '';
  }
}

// ===== 执行结果备注编辑 =====
let _noteEditingKey = null;   // 当前编辑的执行结果复合键
let _noteEditingTc = null;    // 当前编辑的用例 yaml_name

// HTML 转义（备注文本/历史记录渲染通用）
function escHtml(s) {
  return String(s == null ? '' : s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#39;');
}

// JS 字符串转义（用于 HTML onclick 属性内的单引号字符串参数，如 openNoteEditorFromRow）。
// 先转义反斜杠（防止后续转义符被二次转义），再转义单引号（JS 字符串边界），
// 最后转义 HTML 属性特殊字符（双引号等），保证属性与 JS 两层解析都不越界。
function escJsAttr(s) {
  return String(s == null ? '' : s)
    .replace(/\\/g, '\\\\')
    .replace(/'/g, "\\'")
    .replace(/&/g, '&amp;')
    .replace(/"/g, '&quot;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\r/g, '\\r')
    .replace(/\n/g, '\\n');
}

// 构造执行结果复合键（与后端 note_key_for 一致）
function buildNoteKey(d) {
  return [d.yaml_name || '', d.date || '', d.branch || '', d.run_id || ''].join('|');
}

// 从表格行打开备注编辑（按 yaml_name+date+branch+run_id 定位执行结果）
function openNoteEditorFromRow(tcId, date, branch, runId) {
  const item = allData.find(d =>
    d._id === tcId && d.date === date && (d.branch || '') === branch && (d.run_id || '') === runId);
  if (!item) return;
  openNoteEditor(item);
}

function openNoteEditor(d) {
  _noteEditingTc = d.yaml_name || '';
  _noteEditingKey = buildNoteKey(d);
  document.getElementById('noteModalTc').textContent = '用例: ' + _noteEditingTc;
  document.getElementById('noteModalExec').textContent =
    '执行结果: 日期=' + (d.date || '--') + '  分支=' + (d.branch || '--') + '  run_id=' + (d.run_id || '--');
  document.getElementById('noteInput').value = d.note || '';
  const modal = document.getElementById('noteModal');
  modal.style.display = 'flex';
  document.getElementById('noteInput').focus();
}

function closeNoteEditor() {
  document.getElementById('noteModal').style.display = 'none';
  _noteEditingKey = null;
  _noteEditingTc = null;
}

async function saveNote() {
  if (!_noteEditingTc || !_noteEditingKey) return;
  const note = document.getElementById('noteInput').value || '';
  const parts = _noteEditingKey.split('|');
  try {
    const resp = await fetch('/api/note', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({
        yaml_name: parts[0], date: parts[1], branch: parts[2], run_id: parts[3], note: note
      })
    });
    const res = await resp.json();
    if (res.ok) {
      // 更新本地对应执行结果的数据，重新渲染表格
      allData.forEach(d => { if (buildNoteKey(d) === _noteEditingKey) d.note = note; });
      closeNoteEditor();
      onFilterChange();
    } else {
      alert('保存失败: ' + (res.error || '未知错误'));
    }
  } catch (e) {
    alert('保存失败: ' + e);
  }
}

// 一键清理该用例的所有历史备注（含纯键 + 所有复合键）
async function clearCaseNotes() {
  if (!_noteEditingTc) return;
  if (!confirm(`确定清理用例「${_noteEditingTc}」的所有历史备注吗？此操作不可恢复。`)) return;
  try {
    const resp = await fetch('/api/notes/clear', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ yaml_name: _noteEditingTc })
    });
    const res = await resp.json();
    if (res.ok) {
      closeNoteEditor();
      loadData(); // 重新拉取数据并刷新表格
    } else {
      alert('清理失败: ' + (res.error || '未知错误'));
    }
  } catch (e) {
    alert('清理失败: ' + e);
  }
}

// 点击弹窗背景关闭
document.addEventListener('click', (e) => {
  if (e.target && e.target.id === 'noteModal') closeNoteEditor();
});
// 按 Esc 关闭弹窗
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') closeNoteEditor();
});

async function loadData() {
  const resp = await fetch('/api/data');
  allData = await resp.json();
  allData.forEach(d => { d._id = buildTestCaseId(d); });
  populateFilters();
  onFilterChange();
  document.getElementById('updateTime').textContent = '更新: ' + new Date().toLocaleTimeString();
  // Fetch data source status
  try {
    const sr = await fetch('/api/status');
    const st = await sr.json();
    document.getElementById('dataSource').textContent = st.source;
  } catch(e) {}
}

function populateMultiSelect(id, values, allLabel) {
  const sel = document.getElementById(id);
  const current = [...sel.selectedOptions].map(o => o.value);
  sel.innerHTML = '';
  if (allLabel) {
    const o = document.createElement('option'); o.value = '__all__'; o.textContent = allLabel;
    if (current.length === 0 || current.includes('__all__')) o.selected = true;
    sel.appendChild(o);
  }
  values.forEach(v => {
    const o = document.createElement('option'); o.value = v; o.textContent = v;
    if (current.includes(v)) o.selected = true;
    sel.appendChild(o);
  });
}

function populateFilters() {
  const keys = ['model','date','branch'];
  const ids = ['modelFilter','dateFilter','branchFilter'];
  keys.forEach((k, i) => {
    const vals = [...new Set(allData.map(d => d[k]).filter(Boolean))].sort();
    populateMultiSelect(ids[i], vals, '全部');
  });
}

function getSelectedValues(id) {
  const sel = document.getElementById(id);
  const vals = [...sel.selectedOptions].map(o => o.value);
  if (vals.includes('__all__') || vals.length === 0) return null;
  return vals;
}

// Tolerance constants (matching test framework in sglang-plli-shequ)
const TPOT_THRESHOLD = 50;
const TPOT_TOLERANCE_LOW = 1.0;   // +1ms for small TPOT
const TPOT_TOLERANCE_HIGH = 1.02; // +2% for large TPOT
const TTFT_TOLERANCE = 1.02;      // +2%
const E2E_TOLERANCE = 1.02;       // +2%
const THROUGHPUT_TOLERANCE = 0.98; // -2%
const ACCURACY_TOLERANCE = 0.99;  // -1% for general datasets

function getAccuracyThreshold(baseline, dataset) {
  // Dataset-specific absolute tolerance (question count based)
  if (dataset === 'aime25' || dataset === 'aime26') {
    return baseline - 2 / 30; // 2 questions out of 30
  }
  if (dataset === 'gpqa') {
    return baseline - 5 / 198; // 5 questions out of 198
  }
  return baseline * ACCURACY_TOLERANCE;
}

// 结合 run_id 关联的 GitHub Actions job 状态，推断「无结果」的成因。
// 仅当存在 run_id（分支模式数据）且已抓到 job 信息时才能区分：
//   completed + conclusion ∈ {failure, timed_out, action_required, cancelled} → 已执行但失败
//   completed + conclusion == success                                        → 执行成功但指标未上传（状态显示「成功(无结果)」，按 PASS 筛选）
//   completed + conclusion ∈ {skipped, stale, neutral}（未实际运行）          → 未执行
//   queued / in_progress / waiting / requested / pending                     → 执行中
//   匹配到 job 列表但未命中本用例（no_job）                                  → 未执行
// 无 run_id（旧格式）或 job 尚未抓取到时返回空串，保持原「FAILED(无结果)」显示。
const FAIL_JOB_CONCLUSIONS = ['failure', 'timed_out', 'action_required', 'cancelled'];
const SKIP_JOB_CONCLUSIONS = ['skipped', 'stale', 'neutral'];
function jobRunLabel(d) {
  if (!d.run_id) return '';
  const s = String(d.job_status || '').toLowerCase();
  const c = String(d.job_conclusion || '').toLowerCase();
  if (s === 'no_job') return '未执行';
  if (!s && !c) return ''; // job 信息尚未抓取到
  if (s === 'completed') {
    if (FAIL_JOB_CONCLUSIONS.includes(c)) return '已执行失败';
    if (c === 'success') return '成功';
    if (SKIP_JOB_CONCLUSIONS.includes(c)) return '未执行';
    return ''; // completed 但结论未知（异常），保持原「无结果」显示
  }
  return '执行中'; // queued / in_progress / waiting / requested / pending
}

function computeStatus(d) {
  // 功能用例（case_type=function）：不参与基线/指标比对（功能用例无性能/精度指标）。
  // 状态优先取后端解析的 per-case 结果（func_status: pass/fail/running，来自聚合
  // suite job 日志），未解析到时回退到 GitHub job 结论归因（suite 级，仅供参考）。
  if (d.case_type === 'function') {
    if (d.func_status === 'pass') return 'PASS';
    if (d.func_status === 'fail') return 'FAILED';
    if (d.func_status === 'running') return '执行中';
    const runLabel = jobRunLabel(d);
    if (runLabel === '成功') return 'PASS';
    if (runLabel === '已执行失败') return 'FAILED';
    if (runLabel === '执行中') return '执行中';
    if (runLabel === '未执行') return 'FAILED(无结果)';
    return 'FAILED(无结果)'; // 无 run_id 或 job 信息尚未抓取到
  }
  const b = d.baselines || {};
  const hasPerf = d.mean_ttft != null;
  const hasEval = d.eval_score != null;
  const hasBaseline = Object.keys(b).length > 0;
  if (!hasPerf && !hasEval) {
    // 无执行结果：结合 run_id 关联的 CI job 状态归因（已执行失败/执行中/未执行）
    const runLabel = jobRunLabel(d);
    return runLabel ? runLabel + '(无结果)' : 'FAILED(无结果)';
  }
  if (!hasBaseline) return '';
  // 性能类基线仅在该用例有性能数据时校验
  // （避免 accuracy-only 用例因合并了同名 perf 脚本基线而被误判）
  // TPOT: baseline < 50 → +1ms absolute; baseline >= 50 → +2% relative
  if (hasPerf && b.mean_tpot != null) {
    if (d.mean_tpot == null) return 'FAILED';
    const tpotLimit = b.mean_tpot < TPOT_THRESHOLD
      ? b.mean_tpot + TPOT_TOLERANCE_LOW
      : b.mean_tpot * TPOT_TOLERANCE_HIGH;
    if (d.mean_tpot > tpotLimit) return 'FAILED';
  }
  // TTFT: +2% tolerance
  if (hasPerf && b.mean_ttft != null) {
    if (d.mean_ttft == null) return 'FAILED';
    if (d.mean_ttft > b.mean_ttft * TTFT_TOLERANCE) return 'FAILED';
  }
  // E2E Latency: +2% tolerance
  if (hasPerf && b.mean_e2e_latency != null) {
    if (d.mean_e2e_latency == null) return 'FAILED';
    if (d.mean_e2e_latency > b.mean_e2e_latency * E2E_TOLERANCE) return 'FAILED';
  }
  // Output Token Throughput: -2% tolerance
  if (hasPerf && b.output_token_throughput != null) {
    if (d.output_token_throughput == null) return 'FAILED';
    if (d.output_token_throughput < b.output_token_throughput * THROUGHPUT_TOLERANCE) return 'FAILED';
  }
  // Accuracy: dataset-specific tolerance
  if (b.eval_score != null) {
    if (d.eval_score == null) return 'FAILED';
    const threshold = getAccuracyThreshold(b.eval_score, d.dataset);
    if (d.eval_score < threshold) return 'FAILED';
  }
  return 'PASS';
}

// 功能用例聚合状态：统计一组（同日期）功能用例的通过/失败/执行中/未执行数量。
// 状态取自 computeStatus（功能用例仅依据 GitHub job 结论判定）。
function aggregateFuncStatus(items) {
  const counts = { pass: 0, fail: 0, run: 0, nores: 0 };
  items.forEach(d => {
    const s = computeStatus(d);
    if (s === 'PASS') counts.pass++;
    else if (s === '执行中') counts.run++;
    else if (s === 'FAILED') counts.fail++;
    else counts.nores++; // FAILED(无结果) 等 → 未执行
  });
  const parts = [];
  if (counts.pass) parts.push('通过 ' + counts.pass);
  if (counts.fail) parts.push('失败 ' + counts.fail);
  if (counts.run) parts.push('执行中 ' + counts.run);
  if (counts.nores) parts.push('未执行 ' + counts.nores);
  return parts.join(' / ') || '--';
}

// 收起所有已展开的功能用例聚合明细行
function collapseFuncAggregates(root) {
  root.querySelectorAll('tr.func-agg-row.func-open').forEach(r => {
    const od = r.getAttribute('data-fdate');
    root.querySelectorAll('tr[data-fdet="1"][data-fdate="' + od + '"]').forEach(dr => { dr.style.display = 'none'; });
    r.classList.remove('func-open');
    const ic = r.querySelector('.expand-icon');
    if (ic) ic.textContent = '▶';
  });
}

function getTestCaseStatus(items) {
  if (items.length === 0) return 'FAILED(无结果)';
  // 取时间段内最新一次有结果的执行；全部无结果时取最后一项
  const withData = items.filter(d => hasData(d));
  const latest = withData.length > 0 ? withData[withData.length - 1] : items[items.length - 1];
  return computeStatus(latest);
}

// 判断是否为「成功(无结果)」状态：CI job 执行成功但无指标数据。
// 该状态视为通过（按 PASS 筛选/统计），只是缺少结果数据。
function isSuccessNoResult(d) {
  const b = d.baselines || {};
  const hasPerf = d.mean_ttft != null;
  const hasEval = d.eval_score != null;
  if (hasPerf || hasEval) return false;
  const runLabel = jobRunLabel(d);
  return runLabel === '成功';
}

function hasData(d) {
  return d.mean_ttft != null || d.eval_score != null;
}

function onFilterChange() {
  const filters = {
    source: getSelectedValues('sourceFilter'),
    model: getSelectedValues('modelFilter'),
    date: getSelectedValues('dateFilter'),
    branch: getSelectedValues('branchFilter'),
  };
  const statusFilter = getSelectedValues('statusFilter');

  let filtered = allData;
  Object.entries(filters).forEach(([key, vals]) => {
    if (vals !== null) {
      if (key === 'source') {
        // source 可能为逗号分隔的多来源（如 "fulltest,nightly"），任一匹配即通过
        filtered = filtered.filter(d => String(d.source || '').split(',').some(s => vals.includes(s)));
      } else {
        filtered = filtered.filter(d => vals.includes(d[key]));
      }
    }
  });

  if (statusFilter !== null) {
    const groups = {};
    filtered.forEach(d => {
      if (!groups[d._id]) groups[d._id] = [];
      groups[d._id].push(d);
    });
    const keepIds = new Set();
      Object.entries(groups).forEach(([id, items]) => {
        items.sort((a, b) => a.date.localeCompare(b.date));
        const status = getTestCaseStatus(items);
        const hasSuccessNoResult = items.some(d => isSuccessNoResult(d));
        // 成功(无结果) 视为通过：勾选 PASS 时保留
        if (statusFilter.includes('PASS') && (status === 'PASS' || hasSuccessNoResult)) keepIds.add(id);
        // FAILED 过滤：排除「成功(无结果)」（其以"(无结果)"结尾，但仍属通过），仅保留真正失败/执行失败/执行中/未执行/缺省
        if (statusFilter.includes('FAILED') && (status === 'FAILED' || (status.endsWith('(无结果)') && !status.startsWith('成功')))) keepIds.add(id);
      });
    filtered = filtered.filter(d => keepIds.has(d._id));
  }

  updateTable(filtered);
}

function resetFilters() {
  ['sourceFilter','modelFilter','dateFilter','branchFilter','statusFilter'].forEach(id => {
    const sel = document.getElementById(id);
    [...sel.options].forEach(o => o.selected = o.value === '__all__');
  });
  // 历史天数一并重置为默认 7 天
  document.getElementById('historyDays').value = 7;
  onFilterChange();
  applyHistoryFilter();
}

function updateTable(data) {
  const tbody = document.getElementById('tableBody');
  if (data.length === 0) {
    document.getElementById('tableCount').textContent = '(0 条)';
    tbody.innerHTML = '<tr><td colspan="29" class="no-data">无匹配数据</td></tr>';
    return;
  }

  // 分离功能用例：不解析模型名、整体按日期聚合成一组（见下方聚合渲染），
  // 不参与普通用例分组；其余用例维持原分组逻辑。
  const funcRows = data.filter(d => d.case_type === 'function');
  const normalData = data.filter(d => d.case_type !== 'function');

  // Group by test case, sort by date within each group（普通用例）
  const groups = {};
  normalData.forEach(d => {
    if (!groups[d._id]) groups[d._id] = [];
    groups[d._id].push(d);
  });
  Object.values(groups).forEach(g => {
    g.sort((a, b) => a.date.localeCompare(b.date));
    // 勾选多日期时显示时间段内最新一次有结果的执行：
    // 无结果的占位符排前，有结果的按日期升序排后，isLatest 即最新有结果条目
    g.sort((a, b) => (hasData(a) ? 1 : 0) - (hasData(b) ? 1 : 0));
  });

  // Sort groups by test case ID
  const sortedGroups = Object.entries(groups).sort((a, b) => a[0].localeCompare(b[0]));

  function fmtVal(v, digits) {
    return v != null ? v.toFixed(digits) : '--';
  }

  function fmtInt(v) {
    return v != null ? Math.round(v) : '--';
  }
  function getCardCount(d) {
    const m = (d.card_count || '').match(/(\d+)/);
    return m ? parseInt(m[1]) : 0;
  }
  function fmtSingleCard(val, d) {
    if (val == null) return '--';
    const n = getCardCount(d);
    return n > 0 ? (val / n).toFixed(2) : '--';
  }

  function fmtBaseline(b, d) {
    // 基线来自用例脚本，与是否有执行结果无关：
    // accuracy-only 用例显示精度基线；performance 用例显示性能基线；unknown/混合显示全部。
    // （避免无结果占位符条目因缺少数据而误显示为空）
    const parts = [];
    const t = d != null ? d.case_type : 'unknown';
    if (t === 'accuracy') {
      if (b.eval_score != null) parts.push(`精度≥${b.eval_score}`);
    } else if (t === 'performance') {
      if (b.mean_ttft != null) parts.push(`TTFT≤${b.mean_ttft}`);
      if (b.mean_tpot != null) parts.push(`TPOT≤${b.mean_tpot}`);
      if (b.mean_e2e_latency != null) parts.push(`E2E时间≤${b.mean_e2e_latency}`);
      if (b.output_token_throughput != null) parts.push(`输出吞吐≥${b.output_token_throughput}`);
    } else {
      if (b.mean_ttft != null) parts.push(`TTFT≤${b.mean_ttft}`);
      if (b.mean_tpot != null) parts.push(`TPOT≤${b.mean_tpot}`);
      if (b.mean_e2e_latency != null) parts.push(`E2E时间≤${b.mean_e2e_latency}`);
      if (b.output_token_throughput != null) parts.push(`输出吞吐≥${b.output_token_throughput}`);
      if (b.eval_score != null) parts.push(`精度≥${b.eval_score}`);
    }
    return parts.length > 0 ? parts.join('<br>') : '--';
  }

  // Render metric value with red font if it fails baseline (with tolerance):
  //   type: 'tpot'|'ttft'|'e2e'|'throughput'|'accuracy'
  //   Tolerances match test framework: TPOT (+1ms or +2%), TTFT/E2E (+2%), Throughput (-2%), Accuracy (dataset-specific)
  function fmtMetric(val, digits, baseline, type, dataset) {
    if (val == null) return '--';
    const v = val.toFixed(digits);
    if (baseline != null) {
      let fail = false;
      switch (type) {
        case 'tpot':
          if (baseline < TPOT_THRESHOLD) {
            fail = val > baseline + TPOT_TOLERANCE_LOW;
          } else {
            fail = val > baseline * TPOT_TOLERANCE_HIGH;
          }
          break;
        case 'ttft':
          fail = val > baseline * TTFT_TOLERANCE;
          break;
        case 'e2e':
          fail = val > baseline * E2E_TOLERANCE;
          break;
        case 'throughput':
          fail = val < baseline * THROUGHPUT_TOLERANCE;
          break;
        case 'accuracy':
          fail = val < getAccuracyThreshold(baseline, dataset);
          break;
      }
      if (fail) {
        return `<span class="metric-fail">${v}</span>`;
      }
    }
    return v;
  }

  // 渲染用例脚本在 Git 平台的链接（可能来自多个来源仓）
  // 渲染来源 + 用例脚本链接（合并展示）：
  // 有脚本链接 → 链接标签即来源名（如 fulltest↗ / nightly↗）；
  // 无链接但有来源 → 显示来源文本；都无 → '--'
  function fmtScriptLinks(d) {
    const urls = d.script_urls || [];
    const src = d.source || '';
    if (urls.length > 0) {
      // 多个来源链接（如 fulltest/nightly 同用例）换行显示，每个链接一行
      return urls.map(u =>
        `<a class="script-link" href="${escHtml(u.url)}" target="_blank" rel="noopener" title="${escHtml(u.url)}">${escHtml(u.source)}↗</a>`
      ).join('<br>');
    }
    return escHtml(src) || '--';
  }

  // 渲染 CI 运行/任务链接：有具体 job 链接时优先显示，否则回退到 run 链接
  function fmtRunLink(d) {
    if (d.job_url) {
      return `<a class="script-link" href="${escHtml(d.job_url)}" target="_blank" rel="noopener" title="${escHtml(d.job_url)}">job↗</a>`;
    }
    if (d.run_url) {
      return `<a class="script-link" href="${escHtml(d.run_url)}" target="_blank" rel="noopener" title="${escHtml(d.run_url)}">运行↗</a>`;
    }
    return '--';
  }

  // 渲染执行结果备注：显示文本 + 编辑按钮（点击弹窗编辑，备注按执行结果复合键对应该条记录）
  // note_date 存在时表示该备注为回填的历史备注，额外显示其对应日期
  function fmtNote(d) {
    const note = d.note || '';
    const noteDate = d.note_date || '';
    // 编辑按钮参数处于 HTML onclick 属性的 JS 单引号字符串中，需用 escJsAttr 双层转义
    const editBtn = `<span class="note-edit" onclick="openNoteEditorFromRow('${escJsAttr(d._id)}','${escJsAttr(d.date)}','${escJsAttr(d.branch || '')}','${escJsAttr(d.run_id || '')}')" title="填写备注">✏️</span>`;
    let text = '';
    if (note) {
      const tip = noteDate ? `${note}（${noteDate}）` : note;
      const dateTag = noteDate ? `<span class="note-date">（${escHtml(noteDate)}）</span>` : '';
      text = `<span class="note-text" title="${escHtml(tip)}">${escHtml(note)}</span>${dateTag}`;
    }
    return `<span class="note-cell">${editBtn}${text}</span>`;
  }

  // 组网列显示：PD分离/1p1d → 拆成两行（PD分离 + 1p1d）；其他保持不变
  function fmtTopology(t) {
    if (!t) return '--';
    if (t.indexOf('PD分离/') === 0) {
      return `PD分离<br>${escHtml(t.substring('PD分离/'.length))}`;
    }
    return escHtml(t);
  }

  // 序列长度列显示：in3k5_out1k5 → 拆成两行（in3k5 + out1k5）；只有 in/out 单段时保持原样
  function fmtSeqLength(s) {
    if (!s) return '--';
    const m = s.match(/^(.+)_out(.+)$/);
    if (m) {
      return `${escHtml(m[1])}<br>out${escHtml(m[2])}`;
    }
    return escHtml(s);
  }

  let rows = '';
  let visibleCount = 0;
  // 预计算每个分组在 collapsed 视图中是否应显示模型名
  // 规则：分组间按 latest 行比较，模型变了才显示
  const groupShowModel = [];
  let prevLatestModel = null;
  sortedGroups.forEach(([tcId, items]) => {
    const latestModel = items[items.length - 1].model;
    groupShowModel.push(latestModel !== prevLatestModel);
    prevLatestModel = latestModel;
  });
  sortedGroups.forEach(([tcId, items], gIdx) => {
    const safeId = tcId.replace(/[^a-zA-Z0-9]/g, '_');
    items.forEach((d, i) => {
      const isLatest = i === items.length - 1;
      const status = computeStatus(d);
      // 状态样式：PASS/成功(无结果) → 绿；无基线(空) → 红；其余(FAILED等) → 红
      const statusCls = status === 'PASS' || status.indexOf('成功') === 0
        ? (status === 'PASS' ? 'status-pass' : 'status-success-nr')
        : (status === '' ? 'status-none' : 'status-fail');
      const b = d.baselines || {};
      const bl = (key, sym) => b[key] != null ? `<br><span class="baseline-val">${sym}${b[key]}</span>` : '';
      const expandIcon = isLatest && items.length > 1
        ? `<span class="expand-icon" style="cursor:pointer;color:#58a6ff;margin-right:4px;" title="点击展开历史">▶</span>`
        : '';
      const rowStyle = isLatest ? '' : 'style="display:none"';
      if (isLatest) visibleCount++;
      const modelDisplay = isLatest && groupShowModel[gIdx] ? d.model : '';
      rows += `<tr class="data-row" data-tc="${safeId}" data-date="${escHtml(d.date)}" data-hasdata="${hasData(d) ? '1' : '0'}" ${rowStyle}>
        <td class="col-model sticky-col col-l0">${escHtml(modelDisplay)}</td>
        <td class="col-tc-id sticky-col col-l1"><span class="testcase-id" title="${escHtml(tcId)}">${expandIcon}${escHtml(tcId)}</span></td>
        <td class="col-meta sticky-col col-l2">${escHtml(d.date)}</td>
        <td class="col-meta sticky-col col-l3"><span class="${statusCls}">${escHtml(status)}</span></td>
        <td class="col-script sticky-col col-l4">${fmtScriptLinks(d)}</td>
        <td class="col-meta sticky-col col-l5">${fmtRunLink(d)}</td>
        <td class="col-note sticky-col col-l6">${fmtNote(d)}</td>
        <td class="col-baseline sticky-col col-l7"><span class="baseline-col" title="${fmtBaseline(b, d)}">${fmtBaseline(b, d)}</span></td>
        <td class="col-topology">${fmtTopology(d.topology)}</td>
        <td class="col-config">${escHtml(d.card_count || '--')}</td>
        <td class="col-config">${fmtSeqLength(d.seq_length)}</td>
        <td class="col-config">${escHtml((d.prefix || '').replace('prefix', '') || '0')}</td>
        <td class="col-config">${escHtml(d.dataset || '--')}</td>
        <td class="col-uniform">${fmtMetric(d.eval_score, 4, b.eval_score, 'accuracy', d.dataset)}</td>
        <td class="col-uniform">${fmtInt(d.total_requests)}</td>
        <td class="col-uniform">${fmtInt(d.max_concurrency)}</td>
        <td class="col-uniform">${fmtVal(d.system_concurrency, 2)}</td>
        <td class="col-uniform">${fmtVal(d.request_throughput, 2)}</td>
        <td class="col-uniform">${fmtMetric(d.mean_ttft, 2, b.mean_ttft, 'ttft')}</td>
        <td class="col-uniform">${fmtVal(d.p90_ttft, 2)}</td>
        <td class="col-uniform">${fmtMetric(d.mean_tpot, 2, b.mean_tpot, 'tpot')}</td>
        <td class="col-uniform">${fmtVal(d.p90_tpot, 2)}</td>
        <td class="col-uniform">${fmtMetric(d.mean_e2e_latency, 2, b.mean_e2e_latency, 'e2e')}</td>
        <td class="col-uniform">${fmtMetric(d.output_token_throughput, 2, b.output_token_throughput, 'throughput')}</td>
        <td class="col-uniform">${fmtSingleCard(d.output_token_throughput, d)}</td>
        <td class="col-uniform">${fmtVal(d.total_token_throughput, 2)}</td>
        <td class="col-uniform">${fmtSingleCard(d.total_token_throughput, d)}</td>
        <td class="col-uniform">${fmtVal(d.request_throughput, 2)}</td>
        <td class="col-uniform">${d.request_throughput != null ? (d.request_throughput * 60).toFixed(2) : '--'}</td>
      </tr>`;
    });
    // Add hidden chart row after each test case group
    rows += `<tr class="chart-row" id="chart_${safeId}" data-tc="${safeId}" style="display:none"><td colspan="29"></td></tr>`;
  });

  // ---- 功能用例聚合渲染：不解析模型名、整体汇总到一起，按日期每组一行聚合行（可展开查看明细） ----
  // 模型列统一显示"功能用例"，用例ID列显示"功能用例（可展开）"
  const funcDateGroups = {};
  funcRows.forEach(d => {
    const fdate = d.date || '';
    if (!funcDateGroups[fdate]) funcDateGroups[fdate] = [];
    funcDateGroups[fdate].push(d);
  });
  // 日期倒序展示，最新日期在前
  const sortedFuncDates = Object.keys(funcDateGroups).sort((a, b) => b.localeCompare(a));

  sortedFuncDates.forEach(fdate => {
    const items = funcDateGroups[fdate];
    // 明细行内按用例名排序，便于查看
    items.sort((a, b) => (a._id || '').localeCompare(b._id || ''));
    const aggStatus = aggregateFuncStatus(items);
    // 全部通过 → 绿；无任何状态 → 红；其余（含失败/执行中/未执行）→ 红
    const statusCls = /^通过 \d+$/.test(aggStatus) ? 'status-pass'
      : (aggStatus === '--' ? 'status-none' : 'status-fail');
    visibleCount++;
    rows += `<tr class="data-row func-agg-row" data-fdate="${escHtml(fdate)}">
      <td class="col-model sticky-col col-l0">功能用例</td>
      <td class="col-tc-id sticky-col col-l1"><span class="testcase-id" style="cursor:pointer;" title="点击展开/收起功能用例明细"><span class="expand-icon" style="cursor:pointer;color:#58a6ff;margin-right:4px;">▶</span>功能用例</span></td>
      <td class="col-meta sticky-col col-l2">${escHtml(fdate)}</td>
      <td class="col-meta sticky-col col-l3"><span class="${statusCls}">${escHtml(aggStatus)}</span></td>
      <td class="col-script sticky-col col-l4">--</td>
      <td class="col-meta sticky-col col-l5">--</td>
      <td class="col-note sticky-col col-l6">--</td>
      <td class="col-baseline sticky-col col-l7">--</td>
      <td colspan="21">--</td>
    </tr>`;
    // 明细行：每个功能用例一条，默认隐藏
    items.forEach(d => {
      const status = computeStatus(d);
      // PASS → 绿；执行中 → 黄；FAILED → 红；FAILED(无结果)/未执行 → 默认色
      const statusCls2 = status === 'PASS' ? 'status-pass'
        : (status === '执行中' ? 'status-running'
          : (status === 'FAILED' ? 'status-fail' : ''));
      rows += `<tr class="data-row func-detail-row" data-fdet="1" data-fdate="${escHtml(fdate)}" style="display:none">
        <td class="col-model sticky-col col-l0"></td>
        <td class="col-tc-id sticky-col col-l1" style="padding-left:26px;"><span class="testcase-id" title="${escHtml(d._id || '')}">${escHtml(d._id || '')}</span></td>
        <td class="col-meta sticky-col col-l2">${escHtml(d.date)}</td>
        <td class="col-meta sticky-col col-l3"><span class="${statusCls2}">${escHtml(status)}</span></td>
        <td class="col-script sticky-col col-l4">${fmtScriptLinks(d)}</td>
        <td class="col-meta sticky-col col-l5">${fmtRunLink(d)}</td>
        <td class="col-note sticky-col col-l6">${fmtNote(d)}</td>
        <td class="col-baseline sticky-col col-l7">--</td>
        <td colspan="21">--</td>
      </tr>`;
    });
  });

  document.getElementById('tableCount').textContent = `(${visibleCount} 条)`;
  tbody.innerHTML = rows;
}

// 日期辅助：YYYYMMDD 纯日期字符串（date 标签已拆分，格式固定）
function pad2(n) { return String(n).padStart(2, '0'); }
function getDateCutoff(days) {
  // 最近 N 天 → 今天往前推 (N-1) 天；如 7 天 = 今天+前6天
  const t = new Date();
  t.setDate(t.getDate() - (days - 1));
  return `${t.getFullYear()}${pad2(t.getMonth() + 1)}${pad2(t.getDate())}`;
}

// 修改历史天数配置后，对当前展开的用例重新应用过滤
function applyHistoryFilter() {
  const histDays = parseInt(document.getElementById('historyDays').value) || 7;
  const cutoff = getDateCutoff(histDays);
  document.querySelectorAll('.chart-row').forEach(chartRow => {
    if (chartRow.style.display !== 'none') {
      const tcId = chartRow.getAttribute('data-tc');
      const allRows = document.querySelectorAll(`tr[data-tc="${tcId}"].data-row`);
      allRows.forEach((r, i) => {
        const isLast = i === allRows.length - 1;
        const rd = r.getAttribute('data-date');
        const show = isLast || (rd != null && rd >= cutoff && r.getAttribute('data-hasdata') === '1');
        r.style.display = show ? '' : 'none';
        if (show) r.classList.add('selected');
      });
    }
  });
}

// 点击测试用例ID列 → 展开/收起历史直接结果与图表；
// 点击行其它位置 → 仅高亮该条结果（选中），不展开；
// 点击链接/按钮（脚本/任务/备注等交互元素）不触发以上行为。
document.getElementById('tableBody').addEventListener('click', function(e) {
  const tr = e.target.closest('tr');
  if (!tr || tr.querySelector('.no-data') || tr.classList.contains('chart-row')) return;
  // 功能用例聚合行：点击任意位置 → 展开/收起该日功能用例明细
  const fAgg = tr.closest('tr.func-agg-row');
  if (fAgg) {
    const fdate = fAgg.getAttribute('data-fdate');
    if (fAgg.classList.contains('func-open')) {
      collapseFuncAggregates(this);
    } else {
      collapseFuncAggregates(this); // 先收起其它已展开的聚合行
      this.querySelectorAll(`tr[data-fdet="1"][data-fdate="${fdate}"]`).forEach(dr => { dr.style.display = ''; });
      fAgg.classList.add('func-open');
      const ic = fAgg.querySelector('.expand-icon');
      if (ic) ic.textContent = '▼';
    }
    return;
  }
  // 交互元素（链接、备注按钮、展开图标）点击不触发行选中/展开
  if (e.target.closest('a') || e.target.closest('.note-edit') || e.target.closest('.expand-icon')) return;
  const tcId = tr.getAttribute('data-tc');
  if (!tcId) return;

  const isTcIdClick = !!e.target.closest('.col-tc-id');

  if (!isTcIdClick) {
    // 非用例ID列：仅切换该行选中高亮
    tr.classList.toggle('selected');
    return;
  }

  const chartRow = document.getElementById('chart_' + tcId);
  const allRows = this.querySelectorAll(`tr[data-tc="${tcId}"].data-row`);
  const isExpanded = chartRow && chartRow.style.display !== 'none';

  if (isExpanded) {
    // Collapse: hide all rows except the latest, hide chart, destroy chart
    allRows.forEach((r, i) => {
      if (i < allRows.length - 1) r.style.display = 'none';
    });
    allRows.forEach(r => r.classList.remove('selected'));
    if (chartRow) { chartRow.style.display = 'none'; destroyCharts(tcId); }
    // Reset expand icon
    const latestRow = allRows[allRows.length - 1];
    if (latestRow) {
      const icon = latestRow.querySelector('.expand-icon');
      if (icon) icon.textContent = '▶';
    }
  } else {
    // Collapse all other expanded groups first
    this.querySelectorAll('.chart-row').forEach(r => { r.style.display = 'none'; });
    this.querySelectorAll('tr.selected').forEach(r => r.classList.remove('selected'));
    this.querySelectorAll('.expand-icon').forEach(icon => { icon.textContent = '▶'; });
    // Hide all non-latest rows globally
    this.querySelectorAll('tr.data-row').forEach(r => {
      const tc = r.getAttribute('data-tc');
      const siblings = this.querySelectorAll(`tr[data-tc="${tc}"].data-row`);
      if (siblings.length > 1 && r !== siblings[siblings.length - 1]) {
        r.style.display = 'none';
      }
    });

    // Expand: show history rows within the configured day range, highlight, show chart
    const histDays = parseInt(document.getElementById('historyDays').value) || 7;
    const cutoff = getDateCutoff(histDays);
    allRows.forEach((r, i) => {
      // 最新行始终显示；历史行仅显示配置天数内且有执行结果的行（无结果日期不显示）
      const isLast = i === allRows.length - 1;
      const rd = r.getAttribute('data-date');
      const show = isLast || (rd != null && rd >= cutoff && r.getAttribute('data-hasdata') === '1');
      r.style.display = show ? '' : 'none';
      if (show) r.classList.add('selected');
    });
    const latestRow = allRows[allRows.length - 1];
    if (latestRow) {
      const icon = latestRow.querySelector('.expand-icon');
      if (icon) icon.textContent = '▼';
    }
    const label = latestRow ? latestRow.querySelector('.testcase-id')?.getAttribute('title') : '';
    if (chartRow && label) {
      chartRow.style.display = '';
      showTestCaseChart(label, label);
    }
  }
});

function exportToExcel() {
  try {
    if (typeof XLSX === 'undefined') {
      alert('Excel导出库加载失败，请检查网络连接后刷新页面重试。');
      return;
    }
    if (!allData || allData.length === 0) {
      alert('暂无数据可导出。');
      return;
    }

    // Recompute filtered data matching current table display
    const sourceVals = getSelectedValues('sourceFilter');
    const modelVals = getSelectedValues('modelFilter');
    const dateVals = getSelectedValues('dateFilter');
    const branchVals = getSelectedValues('branchFilter');
    const statusVals = getSelectedValues('statusFilter');

    let filtered = allData;
    // source 可能为逗号分隔的多来源（如 "fulltest,nightly"），任一匹配即通过
    if (sourceVals !== null) filtered = filtered.filter(d => String(d.source || '').split(',').some(s => sourceVals.includes(s)));
    if (modelVals !== null) filtered = filtered.filter(d => modelVals.includes(d.model));
    if (dateVals !== null) filtered = filtered.filter(d => dateVals.includes(d.date));
    if (branchVals !== null) filtered = filtered.filter(d => branchVals.includes(d.branch));

    // Group by test case ID, keep latest only
    const groups = {};
    filtered.forEach(d => {
      if (!groups[d._id]) groups[d._id] = [];
      groups[d._id].push(d);
    });

    let rows = [];
    Object.entries(groups).forEach(([id, items]) => {
      items.sort((a, b) => a.date.localeCompare(b.date));
      // 最新有结果优先：无结果占位符排前，有结果的按日期升序排后
      items.sort((a, b) => (hasData(a) ? 1 : 0) - (hasData(b) ? 1 : 0));
      if (statusVals !== null) {
        const status = getTestCaseStatus(items);
        const hasSuccessNoResult = items.some(d => isSuccessNoResult(d));
        const keep = (statusVals.includes('PASS') && (status === 'PASS' || hasSuccessNoResult)) ||
                     (statusVals.includes('FAILED') && (status === 'FAILED' || (status.endsWith('(无结果)') && !status.startsWith('成功'))));
        if (!keep) return;
      }
      rows.push(items[items.length - 1]);
    });

    if (rows.length === 0) {
      alert('当前筛选条件下无数据可导出。');
      return;
    }

    // Build Excel data
    const headers = [
      '模型', '测试用例ID', '日期', '状态', '用例脚本', '任务', '备注', '基线',
      '组网', '卡数', '序列长度', 'PREFIX', '数据集',
      '精度', '总请求数', '最大并发数', '系统并发数', '请求频率',
      'TTFT(ms)', 'TTFT P90(ms)', 'TPOT(ms)', 'TPOT P90(ms)',
      'E2E时间(ms)', '输出吞吐(TPS)', '单卡输出吞吐(TPS)',
      'E2E吞吐(TPS)', '单卡E2E吞吐(TPS)', 'QPS', 'QPM'
    ];

    const getCardCount = (d) => {
      const m = (d.card_count || '').match(/(\d+)/);
      return m ? parseInt(m[1]) : 0;
    };

    const dataRows = rows.map(d => {
      const b = d.baselines || {};
      const n = getCardCount(d);
      // 基线来自用例脚本，与是否有执行结果无关；按用例类型过滤
      // （accuracy-only 只显示精度基线，performance 只显示性能基线）
      const t = d.case_type;
      const blParts = [];
      if (t === 'accuracy') {
        if (b.eval_score != null) blParts.push('精度≥' + b.eval_score);
      } else if (t === 'performance') {
        if (b.mean_ttft != null) blParts.push('TTFT≤' + b.mean_ttft);
        if (b.mean_tpot != null) blParts.push('TPOT≤' + b.mean_tpot);
        if (b.mean_e2e_latency != null) blParts.push('E2E≤' + b.mean_e2e_latency);
        if (b.output_token_throughput != null) blParts.push('吞吐≥' + b.output_token_throughput);
      } else {
        if (b.mean_ttft != null) blParts.push('TTFT≤' + b.mean_ttft);
        if (b.mean_tpot != null) blParts.push('TPOT≤' + b.mean_tpot);
        if (b.mean_e2e_latency != null) blParts.push('E2E≤' + b.mean_e2e_latency);
        if (b.output_token_throughput != null) blParts.push('吞吐≥' + b.output_token_throughput);
        if (b.eval_score != null) blParts.push('精度≥' + b.eval_score);
      }
      return [
        d.model || '', d._id || '', d.date || '', computeStatus(d),
        // 用例脚本列（合并来源）：有脚本链接时显示 来源(URL)，否则显示来源
        (d.script_urls || []).map(u => u.source + '(' + u.url + ')').join('; ') || d.source || '',
        d.job_url || d.run_url || '',
        d.note || '',
        blParts.join(', '),
        d.topology || '', d.card_count || '', d.seq_length || '',
        (d.prefix || '').replace('prefix', '') || '0', d.dataset || '',
        d.eval_score != null ? d.eval_score : '',
        d.total_requests != null ? d.total_requests : '',
        d.max_concurrency != null ? d.max_concurrency : '',
        d.system_concurrency != null ? d.system_concurrency.toFixed(2) : '',
        d.request_throughput != null ? d.request_throughput.toFixed(2) : '',
        d.mean_ttft != null ? d.mean_ttft.toFixed(2) : '',
        d.p90_ttft != null ? d.p90_ttft.toFixed(2) : '',
        d.mean_tpot != null ? d.mean_tpot.toFixed(2) : '',
        d.p90_tpot != null ? d.p90_tpot.toFixed(2) : '',
        d.mean_e2e_latency != null ? d.mean_e2e_latency.toFixed(2) : '',
        d.output_token_throughput != null ? d.output_token_throughput.toFixed(2) : '',
        n > 0 && d.output_token_throughput != null ? (d.output_token_throughput / n).toFixed(2) : '',
        d.total_token_throughput != null ? d.total_token_throughput.toFixed(2) : '',
        n > 0 && d.total_token_throughput != null ? (d.total_token_throughput / n).toFixed(2) : '',
        d.request_throughput != null ? d.request_throughput.toFixed(2) : '',
        d.request_throughput != null ? (d.request_throughput * 60).toFixed(2) : ''
      ];
    });

    const wsData = [headers, ...dataRows];
    const ws = XLSX.utils.aoa_to_sheet(wsData);
    ws['!cols'] = headers.map(() => ({ wch: 18 }));
    const wb = XLSX.utils.book_new();
    XLSX.utils.book_append_sheet(wb, ws, '性能数据');
    XLSX.writeFile(wb, 'sglang_benchmark_' + new Date().toISOString().slice(0, 10) + '.xlsx');
  } catch (e) {
    console.error('导出失败:', e);
    alert('导出失败: ' + e.message);
  }
}

document.addEventListener('DOMContentLoaded', () => {
  initCharts();
  loadData();
  // 轮询间隔 60s：与后端 DATA_CACHE_TTL(30s) + jobs 后台刷新配合，
  // 保证「执行中/已执行失败/成功(无结果)」等 job 状态与任务链接及时更新
  setInterval(loadData, 60000);
});
</script>
</body>
</html>"""


def parse_yaml_test_name(name):
    """Convert a YAML test config name to dashboard labels using parse_filename.
    Example: qwen3_6_35b_a3b_2p_in984k_out1k -> {model, parallelism, input_len, output_len, ...}
    """
    # Strip test_npu_ prefix if present
    if name.startswith("test_npu_"):
        name = name[len("test_npu_"):]
    # Strip _a2 suffix (A2 chip marker)
    name = re.sub(r"_a2$", "", name)
    # Use parse_filename by feeding it as if it were a filename
    labels = parse_filename("test_npu_" + name + ".txt")
    return labels


def build_test_case_id(labels):
    """Build a dashboard test case ID from labels dict."""
    parts = [
        labels.get("model", ""),
        labels.get("quantization", ""),
        labels.get("parallelism", ""),
        labels.get("input_len", ""),
        labels.get("output_len", ""),
        labels.get("request_rate", ""),
        labels.get("dataset", ""),
        labels.get("prefix", ""),
    ]
    return "|".join(p for p in parts if p)


def filename_to_yaml_name(filename):
    """Convert a benchmark/test filename to YAML test case name.
    e.g., 'test_npu_qwen3_6_35b_a3b_2p_in984k_out1k.txt' -> 'qwen3_6_35b_a3b_2p_in984k_out1k'
          'test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_a2.txt' -> 'qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_a2'
          'test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms__20260726.txt' -> 'qwen3_32b_w8a8_2p_in3k5_out1k5_50ms'
    """
    name = filename
    # Strip __YYYYmmdd source date suffix (added by collect_metrics.sh)
    name = re.sub(r"__\d{8}", "", name)
    # Strip -HHMMSS CI timestamp suffix (from CI directory naming)
    name = re.sub(r"-\d{6}(?=_.*|\.)", "", name)
    if name.endswith(".txt"):
        name = name[:-4]
    if name.startswith("test_npu_"):
        name = name[len("test_npu_"):]
    return name


def _is_nightly_registered(content):
    """判断测试脚本是否通过 register_npu_ci(nightly=True) 注册到 nightly 流水线。
    通过括号配对提取每个 register_npu_ci(...) 调用的参数块后匹配 nightly=True。
    """
    for m in re.finditer(r"register_npu_ci\s*\(", content):
        depth = 0
        start = m.end() - 1
        end = start
        for i in range(start, len(content)):
            if content[i] == "(":
                depth += 1
            elif content[i] == ")":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        args_block = content[m.end() - 1:end]
        if re.search(r"nightly\s*=\s*True", args_block):
            return True
    return False


def _nightly_suite_of(content):
    """返回 content 中 register_npu_ci(nightly=True) 注册对应的 suite 值。

    仅统计 nightly=True 的注册调用；同一脚本可能注册到多个 suite，
    优先返回以 nightly- 开头的 suite（与 _build_suite_maps_from_registry 的
    聚合 job 命名规则一致）；无 nightly 注册或无 suite 时返回空字符串。
    """
    suite = ""
    for m in re.finditer(r"register_npu_ci\s*\(", content):
        depth = 0
        start = m.end() - 1
        end = start
        for i in range(start, len(content)):
            if content[i] == "(":
                depth += 1
            elif content[i] == ")":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        args_block = content[m.end() - 1:end]
        if not re.search(r"nightly\s*=\s*True", args_block):
            continue
        suite_match = re.search(
            r"suite\s*=\s*([\"']?)(.*?)\1\s*(,|$)", args_block
        )
        if suite_match and suite_match.group(2).strip():
            s = suite_match.group(2).strip()
            if s.startswith("nightly-"):
                return s
            if not suite:
                suite = s
    return suite


def _collect_registry_expected_test_cases():
    """扫描各 source 仓库的 test/registered/npu 目录，
    收集 register_npu_ci(nightly=True) 注册的 nightly 单机用例。

    新测试框架下，单机用例通过注册器注册到 nightly 流水线（不再全部写在
    nightly-test-npu.yml 的 test_config 中）；多机用例仍在 YAML 中单独配置
    （由 collect_expected_test_cases 的 YAML 解析负责）。

    用例类型按所在子目录区分：accuracy/performance 目录 → accuracy/performance；
    其余目录（basic_function/llm_models/interface/embedding_models/rerank_models/
    reward_models/vlm_models 等功能用例）及根级散文件 → function。

    功能用例仅从 nightly 来源收集：功能用例是 nightly 流水线由注册器创建运行的，
    fulltest 来源仓虽也含同名功能用例文件，但不在 nightly 流水线执行，纳入平台
    列表会形成永远无执行结果的噪音用例；accuracy/performance 仍收集全部来源
    （与既有行为一致）。

    返回 {yaml_name: {"labels": ..., "source": ..., "yaml_name": ..., "type": ...}}，
    其中 type 根据所在子目录取 accuracy/performance/function。
    """
    # 子目录 → 用例类型；不在映射中的目录及根级文件一律视为功能用例（function）
    type_map = {
        "accuracy": "accuracy",
        "performance": "performance",
    }
    # 功能用例仅收集 nightly 来源（见函数 docstring 说明）
    function_only_sources = {"nightly"}
    found = {}
    for src_name, src_cfg in SOURCES.items():
        repo_root = src_cfg.get("repo_root", "")
        if not repo_root:
            continue
        npu_root = os.path.join(repo_root, "test", "registered", "npu")
        if not os.path.isdir(npu_root):
            continue
        for root, _, files in os.walk(npu_root):
            rel = os.path.relpath(root, npu_root)
            top_dir = rel.split(os.sep)[0] if rel != "." else ""
            case_type = type_map.get(top_dir, "function")
            if case_type == "function" and src_name not in function_only_sources:
                continue
            for fname in sorted(files):
                if not fname.endswith(".py"):
                    continue
                case_name = fname[:-3]  # 去掉 .py，如 test_npu_xxx
                yaml_name = filename_to_yaml_name(case_name + ".txt")
                if yaml_name in EXCLUDED_TEST_CASES or case_name in EXCLUDED_TEST_CASES:
                    continue
                filepath = os.path.join(root, fname)
                try:
                    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                        content = f.read()
                except OSError:
                    continue
                if not _is_nightly_registered(content):
                    continue
                # 功能用例需额外筛选 suite 以 nightly- 开头（仅收集 nightly 流水线执行的功能用例）
                if case_type == "function":
                    suite = _nightly_suite_of(content)
                    if not suite.startswith("nightly-"):
                        continue
                labels = parse_yaml_test_name(yaml_name)
                if yaml_name not in found:
                    found[yaml_name] = {
                        "labels": labels,
                        "source": src_name,
                        "yaml_name": yaml_name,
                        "type": case_type,
                    }
                else:
                    existing = found[yaml_name]
                    if src_name not in existing["source"].split(","):
                        existing["source"] = existing["source"] + "," + src_name
                    if existing.get("type") == "unknown":
                        existing["type"] = case_type
    if found:
        print(f"[registry] 识别到 {len(found)} 个 register_npu_ci(nightly=True) 注册用例")
    return found


def _load_testcases_config():
    """从本地配置文件加载需展示的用例列表（权威来源）。

    配置文件中每条仅保留 {source, type}：key 即 yaml_name，
    labels 由 parse_yaml_test_name(yaml_name) 动态推导，避免冗余存储。
    返回 dict 或 None（文件不存在/解析失败时返回 None，由调用方回退到动态扫描）。
    """
    if not os.path.isfile(TESTCASES_CONFIG_FILE):
        return None
    try:
        with open(TESTCASES_CONFIG_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, dict):
            print(f"[testcases-config] Warning: {TESTCASES_CONFIG_FILE} 格式异常（应为对象），忽略")
            return None
        # 补全动态推导字段，供 collect_all_data / 占位符逻辑使用
        for name, info in data.items():
            if not isinstance(info, dict):
                continue
            info["labels"] = parse_yaml_test_name(name)
            info["yaml_name"] = name
        print(f"[testcases-config] 从本地配置文件加载 {len(data)} 个需展示用例: {TESTCASES_CONFIG_FILE}")
        return data
    except Exception as e:
        print(f"[testcases-config] Warning: 加载配置文件失败 {e}，回退到动态扫描")
        return None


def regenerate_testcases_config():
    """基于最新代码仓内容（YAML test_config + 注册器用例）重新生成本地配置文件。

    调用前需先执行 sync_repos() 拉取最新代码；采用临时文件 + os.replace 原子写入。
    简化存储：key 即 yaml_name，labels 由 parse_yaml_test_name(yaml_name) 动态推导，
    故每条仅保存 {source, type}，减小文件体积并避免冗余。
    """
    expected = collect_expected_test_cases(use_local_config=False)
    simplified = {
        name: {
            "source": info.get("source", ""),
            "type": info.get("type", "unknown"),
        }
        for name, info in expected.items()
    }
    tmp = TESTCASES_CONFIG_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(simplified, f, ensure_ascii=False, indent=2)
    os.replace(tmp, TESTCASES_CONFIG_FILE)
    n_type = {}
    for v in simplified.values():
        t = v.get("type", "unknown")
        n_type[t] = n_type.get(t, 0) + 1
    print(f"[testcases-config] 已生成 {len(simplified)} 个用例配置文件: {TESTCASES_CONFIG_FILE}")
    print(f"[testcases-config] 类型分布: {n_type}")


def collect_expected_test_cases(use_local_config=True):
    """获取平台需展示的期望用例列表。

    优先从本地配置文件 testcases_config.json 加载（权威来源），避免 GitHub
    社区仓中用例被他人删除/修改导致平台展示列表漂移；仅当配置文件不存在时，
    才回退到动态扫描（YAML test_config + 注册器用例，见 _collect_registry_expected_test_cases），
    并提示使用 python dashboard.py --update-testcases-config 生成配置文件。

    use_local_config=False 时跳过本地配置，强制动态扫描（用于重新生成配置文件）。
    Returns a dict: {test_case_id: {"labels": labels, "source": "fulltest"|"nightly"|..., "type": ...}}
    """
    if use_local_config:
        cfg = _load_testcases_config()
        if cfg is not None:
            return cfg
        print("[testcases-config] 配置文件不存在，回退到动态扫描"
              "（可用 python dashboard.py --update-testcases-config 生成本地配置）")
    if not YAML_CONFIGS:
        print("[yaml] No YAML configs available (skip collecting expected test cases)")
        return {}

    expected = {}
    yaml_source_map = {}
    for src_name, src_cfg in SOURCES.items():
        yaml_source_map[src_cfg["yaml_config"]] = src_name

    for yaml_path in YAML_CONFIGS:
        if not os.path.isfile(yaml_path):
            print(f"[yaml] Config not found: {yaml_path}")
            continue
        try:
            with open(yaml_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"[yaml] Error reading {yaml_path}: {e}")
            continue

        source = yaml_source_map.get(yaml_path, "unknown")
        in_test_config = False
        test_config_indent = 0
        current_name = None

        for line in lines:
            stripped = line.strip()
            current_indent = len(line) - len(line.lstrip())

            # Detect test_config: line (e.g., "        test_config:")
            if re.match(r'^\s*test_config:\s*$', line):
                in_test_config = True
                test_config_indent = current_indent
                continue

            if in_test_config:
                # Skip comment lines (avoid false block exit when # starts at column 0)
                if stripped.startswith('#'):
                    continue

                # Exit block when we hit a non-empty line at or before test_config indent
                if stripped and current_indent <= test_config_indent:
                    in_test_config = False
                    current_name = None
                    continue

                # Only match - name: entries that are indented deeper than test_config
                if current_indent > test_config_indent:
                    name_match = re.match(r'- name:\s*(\S+)', stripped)
                    if name_match:
                        current_name = name_match.group(1)
                        name = current_name
                        labels = parse_yaml_test_name(name)
                        model = labels.get("model", "")
                        if " " in model or not model:
                            current_name = None
                            continue
                        # Skip excluded test cases
                        if name in EXCLUDED_TEST_CASES:
                            current_name = None
                            continue
                        # Use YAML name directly as test case ID
                        if name not in expected:
                            expected[name] = {"labels": labels, "source": source, "yaml_name": name, "type": "unknown"}
                        else:
                            # 同一用例可能同时存在于多个 workflow（如 fulltest + nightly），合并 source
                            existing = expected[name]
                            if source not in existing["source"].split(","):
                                existing["source"] = existing["source"] + "," + source
                    else:
                        # 解析 test_case 路径，判断用例类型（accuracy/performance）
                        tc_match = re.match(r'test_case:\s*(\S+)', stripped)
                        if tc_match and current_name and current_name in expected:
                            tc_path = tc_match.group(1)
                            if "/accuracy/" in tc_path or tc_path.startswith("accuracy"):
                                case_type = "accuracy"
                            elif "/performance/" in tc_path or tc_path.startswith("performance"):
                                case_type = "performance"
                            else:
                                case_type = "unknown"
                            if expected[current_name].get("type") == "unknown":
                                expected[current_name]["type"] = case_type

    # 合并注册器用例（新测试框架）：单机用例通过 register_npu_ci(nightly=True)
    # 注册到 nightly 流水线，仅筛选 test/registered/npu/{accuracy,performance}
    # 目录（排除 basic_function 等功能用例）；多机用例仍在 YAML test_config 中配置。
    registry = _collect_registry_expected_test_cases()
    for name, info in registry.items():
        srcs = [s for s in info["source"].split(",") if s]
        case_type = info.get("type", "unknown")
        target_key = name
        if name not in expected:
            # YAML 中可能以 test_npu_ 前缀命名（如 mimo 系列），做前缀归一化
            alt = "test_npu_" + name
            if alt in expected:
                target_key = alt
        if target_key in expected:
            existing = expected[target_key]
            for s in srcs:
                if s and s not in existing["source"].split(","):
                    existing["source"] = existing["source"] + "," + s if existing["source"] else s
            if existing.get("type") == "unknown":
                existing["type"] = case_type
        else:
            expected[target_key] = {
                "labels": info["labels"],
                "source": ",".join(srcs),
                "yaml_name": target_key,
                "type": case_type,
            }

    return expected


def _match_baselines_for_item(item, baselines):
    """Match and attach baselines to an accuracy-only item.
    First tries direct key lookup via yaml_name, then falls back to label matching.
    """
    item["baselines"] = {}
    yaml_name = item.get("yaml_name", "")
    # Try direct key lookup: test_npu_ + yaml_name
    if yaml_name:
        if yaml_name.startswith("test_npu_"):
            direct_key = yaml_name
        else:
            direct_key = "test_npu_" + yaml_name
        if direct_key in baselines:
            item["baselines"] = baselines[direct_key]
            return
    # Fall back to label matching (all key fields must match)
    for tc_key, tc_baseline in baselines.items():
        tc_parsed = parse_filename(tc_key + ".txt")
        if (tc_parsed.get("model") == item.get("model") and
            tc_parsed.get("dataset") == item.get("dataset") and
            tc_parsed.get("quantization") == item.get("quantization") and
            tc_parsed.get("parallelism") == item.get("parallelism") and
            tc_parsed.get("input_len") == item.get("input_len") and
            tc_parsed.get("output_len") == item.get("output_len") and
            tc_parsed.get("request_rate") == item.get("request_rate") and
            tc_parsed.get("prefix") == item.get("prefix")):
            item["baselines"] = tc_baseline
            break


def split_date_label(date_label):
    """拆分 date_label 为 (date, branch, run_id, run_workflow)。

    新格式（CI 目录新增时间/序号段）:
            {branch}-{date}-{time}-{run_id}-{attempt}/{workflow}
            例如 pllimax-pllimax-outputlogdirstructure-20260813-2002-31698149241-1/Nightly_Test_NPU
            → (20260813, pllimax-pllimax-outputlogdirstructure, 31698149241, Nightly_Test_NPU)
            # 中间 -2002- 为 CI 时间/序号段（2-4 位），跳过；run_id 剥离本地去重后缀 -N。
    旧格式（分支模式）:
            {branch}-{date}-{run_id}-{attempt}/{workflow}
            例如 pllimax-...-20260809-31317079962-1/Nightly_Test_NPU
    旧格式: YYYYMMDD → (YYYYMMDD, "", "", "")
    """
    if not date_label:
        return date_label, "", "", ""
    # 新格式：{branch}-{date}-{time}-{run_id}-{attempt}/{workflow}
    # run_id 至少 5 位（GitHub Actions run_id 实际 9-11 位），time 段 2-4 位
    m = re.match(r"^(.+)-(\d{8})-(\d{2,4})-(\d{5,})(?:-(\d+))?/(.+)$", date_label)
    if m:
        run_id = re.sub(r"-\d+$", "", m.group(4))
        return m.group(2), m.group(1), run_id, m.group(6)
    # 旧格式（分支模式）：{branch}-{date}-{run_id}-{attempt}/{workflow}
    m = re.match(r"^(.+)-(\d{8})-(\d{5,})(?:-(\d+))?/(.+)$", date_label)
    if m:
        run_id = re.sub(r"-\d+$", "", m.group(3))
        return m.group(2), m.group(1), run_id, m.group(5)
    return date_label, "", "", ""


def collect_all_data():
    """Collect all benchmark data into a list of dicts.
    Only includes test cases defined in YAML workflow configs.
    """
    results = []
    metrics_dir = get_metrics_dir()
    if not os.path.isdir(metrics_dir):
        return results

    # Get expected test cases from YAML configs (with source info)
    expected = collect_expected_test_cases()
    expected_tc_ids = set(expected.keys())

    # Collect eval scores: {(test_case_name, date): max_score}
    eval_data = collect_eval_data()

    # Collect baselines from test scripts
    baselines = collect_baselines()

    # Track which eval keys were consumed by benchmark results
    consumed_eval_keys = set()

    for date_folder, filepath in _iter_metrics_files(metrics_dir, ".txt"):
        filename = os.path.basename(filepath)
        parsed = parse_benchmark_file(filepath)
        if parsed is None:
            continue

        labels = parse_filename(filename)
        date_part, branch_part, run_id, run_workflow = split_date_label(date_folder)
        labels["date"] = date_part
        labels["branch"] = branch_part
        labels["run_id"] = run_id
        labels["run_workflow"] = run_workflow
        labels["yaml_name"] = filename_to_yaml_name(filename)
        # Fallback: if stripped name not in expected, try with test_npu_ prefix
        if labels["yaml_name"] not in expected_tc_ids:
            alt = "test_npu_" + labels["yaml_name"]
            if alt in expected_tc_ids:
                labels["yaml_name"] = alt
        labels.update(parsed)

        # Strip __YYYYmmdd source date suffix for eval/baseline lookups
        base_name = filename[:-4]  # strip .txt
        base_name = re.sub(r"__\d{8}$", "", base_name)
        test_case_name = base_name

        # Attach eval score: key is (test_case_name, date)
        eval_key = (test_case_name, date_folder)
        labels["eval_score"] = eval_data.get(eval_key)
        consumed_eval_keys.add(eval_key)

        # Attach baselines
        labels["baselines"] = baselines.get(test_case_name, {})

        results.append(labels)

    # Append accuracy-only test results from accuracy/ directory (no performance metrics)
    accuracy_data = collect_accuracy_only_data()
    for item in accuracy_data:
        _match_baselines_for_item(item, baselines)
        date_part, branch_part, run_id, run_workflow = split_date_label(item.get("date", ""))
        item["date"] = date_part
        item["branch"] = branch_part
        item["run_id"] = run_id
        item["run_workflow"] = run_workflow
    results.extend(accuracy_data)

    # Append accuracy-only entries for eval/ scores not matched to benchmark results
    # (e.g., accuracy-only tests like qwen3_vl_8b_thinking_1p_mmmu whose results
    #  are in eval/ but have no matching .txt benchmark file)
    for (test_case_name, date), score in eval_data.items():
        if (test_case_name, date) not in consumed_eval_keys:
            labels = parse_filename(test_case_name + ".txt")
            date_part, branch_part, run_id, run_workflow = split_date_label(date)
            labels["date"] = date_part
            labels["branch"] = branch_part
            labels["run_id"] = run_id
            labels["run_workflow"] = run_workflow
            labels["yaml_name"] = filename_to_yaml_name(test_case_name)
            if labels["yaml_name"] not in expected_tc_ids:
                alt = "test_npu_" + labels["yaml_name"]
                if alt in expected_tc_ids:
                    labels["yaml_name"] = alt
            labels["eval_score"] = score
            labels.update({k: None for k in PERF_ONLY_FIELDS})
            _match_baselines_for_item(labels, baselines)
            results.append(labels)

    # Apply yaml_name fallback for all items (handle test_npu_ prefix in YAML names)
    for r in results:
        yaml_name = r.get("yaml_name", "")
        if yaml_name not in expected_tc_ids and yaml_name:
            alt = "test_npu_" + yaml_name
            if alt in expected_tc_ids:
                r["yaml_name"] = alt

    # Filter: only keep results whose yaml_name is in expected YAML scope
    filtered = []
    for r in results:
        yaml_name = r.get("yaml_name", "")
        if yaml_name in expected_tc_ids:
            r["source"] = expected[yaml_name]["source"]
            # 用例类型（accuracy/performance/unknown）用于前端基线显示与状态判定
            r["case_type"] = expected[yaml_name].get("type", "unknown")
            # 功能用例不解析模型名：模型列统一显示为"功能用例"
            if r["case_type"] == "function":
                r["model"] = "功能用例"
            # 纯精度用例（YAML 定义为 accuracy 测试）只显示精度结果：
            # 丢弃因同名 perf 脚本或历史数据混入的性能字段
            if r["case_type"] == "accuracy":
                for k in PERF_ONLY_FIELDS:
                    r[k] = None
            filtered.append(r)

    # Add placeholder entries for expected test cases that have no data
    # 为每个 (分支, 日期) 组合补充占位符条目：
    # 选中具体分支或日期时，无结果的用例也显示（FAILED(无结果)）

    # Collect all (branch, date) pairs that appear in results
    # 同时记录每个 (branch, date) 对应的 run 上下文（run_id / run_workflow），
    # 使占位符条目也能解析 GitHub Actions 任务链接与 job 状态
    branch_dates = {}
    run_context = {}  # (branch, date) -> (run_id, run_workflow)
    for r in filtered:
        b = r.get("branch", "")
        d = r.get("date", "")
        if d:
            branch_dates.setdefault(b, set()).add(d)
            rid = r.get("run_id", "") or ""
            rwf = r.get("run_workflow", "") or ""
            if rid:
                run_context[(b, d)] = (rid, rwf)
    if not branch_dates:
        # No data at all: use a placeholder pair so expected cases still render
        branch_dates = {"": {""}}

    # 同一 (用例, 分支, 日期) 可能来自多个数据源（.txt / accuracy 子目录 / eval 兜底），
    # 合并去重：保留所有非 None 字段（字段级合并）。
    # key 必须包含 run_id / run_workflow：同一分支同一天可能有多个 CI run（不同 run_id），
    # 若只用 (yaml_name, branch, date) 合并，后遍历的 run 会被先遍历的 run 覆盖而完全丢失。
    merged = {}
    for r in filtered:
        key = (r.get("yaml_name", ""), r.get("branch", ""), r.get("date", ""),
               r.get("run_id", ""), r.get("run_workflow", ""))
        if key in merged:
            for k, v in r.items():
                if v is not None and merged[key].get(k) is None:
                    merged[key][k] = v
        else:
            merged[key] = r
    filtered = list(merged.values())

    # Existing (yaml_name, branch, date) triples to avoid duplicating real results
    existing_pairs = set(
        (r.get("yaml_name", ""), r.get("branch", ""), r.get("date", ""))
        for r in filtered
    )

    for branch, dates in branch_dates.items():
        for date in sorted(dates):
            rid, rwf = run_context.get((branch, date), ("", ""))
            for yaml_name, info in expected.items():
                if (yaml_name, branch, date) in existing_pairs:
                    continue
                labels = info["labels"]
                # Derive baseline key from yaml_name: prefix with "test_npu_" if not already
                if yaml_name.startswith("test_npu_"):
                    baseline_key = yaml_name
                else:
                    baseline_key = "test_npu_" + yaml_name
                placeholder_baselines = baselines.get(baseline_key, {})
                placeholder = {
                    "model": labels.get("model", ""),
                    "quantization": labels.get("quantization", ""),
                    "parallelism": labels.get("parallelism", ""),
                    "input_len": labels.get("input_len", ""),
                    "output_len": labels.get("output_len", ""),
                    "request_rate": labels.get("request_rate", ""),
                    "dataset": labels.get("dataset", ""),
                    "prefix": labels.get("prefix", ""),
                    "date": date,
                    "branch": branch,
                    "run_id": rid,
                    "run_workflow": rwf,
                    "yaml_name": yaml_name,
                    "case_type": info.get("type", "unknown"),
                    "eval_score": None,
                    "baselines": placeholder_baselines,
                    "source": info["source"],
                }
                # 占位符无性能数据，清空全部性能字段
                placeholder.update({k: None for k in PERF_ONLY_FIELDS})
                # 功能用例占位符同样统一模型列显示
                if info.get("type", "unknown") == "function":
                    placeholder["model"] = "功能用例"
                filtered.append(placeholder)

    # Attach topology info to all items
    for item in filtered:
        yaml_name = item.get("yaml_name", "")
        topology, card_count, seq_length = compute_topology_info(yaml_name)
        item["topology"] = topology
        item["card_count"] = card_count
        item["seq_length"] = seq_length

    # Attach git platform script links for each test case
    _attach_script_urls(filtered)

    return filtered


# /api/data 结果缓存：metrics 数据更新不频繁（每 300s 轮询 + 手动刷新），
# 加 TTL 缓存避免每次请求全量重扫 metrics 目录与解析 YAML。
DATA_CACHE_TTL = 30  # 秒
_data_cache = {"ts": 0, "payload": None}
_data_lock = threading.RLock()  # 保护 /api/data 结果缓存的并发读写


def _get_data():
    # 加锁保证并发请求下缓存只被构建一次，且 attach_notes 对共享
    # payload 的修改串行化，避免多个线程同时写 item["note"] 的竞态
    with _data_lock:
        now = time.time()
        if _data_cache["payload"] is None or now - _data_cache["ts"] >= DATA_CACHE_TTL:
            _data_cache["payload"] = collect_all_data()
            _data_cache["ts"] = now
        payload = _data_cache["payload"]
        # 附加用例备注（每次请求都刷新，保证保存后立即可见）
        attach_notes(payload)
        return payload


# ============================================================
# 前端静态资源：优先本地 vendored 文件（内网可用），缺失时回退 CDN。
# vendor 文件位于本文件同目录的 static/ 下（chart.js / xlsx）。
# ============================================================
STATIC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
CDN_CHART_JS = "https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"
CDN_XLSX = "https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"
# 允许通过静态服务提供的白名单文件（防路径穿越）
STATIC_ALLOWLIST = {
    "chart.umd.min.js",
    "xlsx.full.min.js",
}


def _asset_url(filename, cdn_url):
    """返回资源 URL：本地 static/ 存在则用相对路径，否则回退到 CDN。"""
    if filename in STATIC_ALLOWLIST and os.path.isfile(os.path.join(STATIC_DIR, filename)):
        return f"/static/{filename}"
    return cdn_url


class DashboardHandler(http.server.BaseHTTPRequestHandler):
    def _send_json(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        if DASHBOARD_CORS_ORIGIN:
            self.send_header("Access-Control-Allow-Origin", DASHBOARD_CORS_ORIGIN)
        self.end_headers()
        self.wfile.write(body)

    def _serve_static(self, filename):
        """安全地提供 static/ 下的白名单静态资源（防目录穿越）。"""
        filename = os.path.basename(filename or "")
        if filename not in STATIC_ALLOWLIST:
            self.send_response(404)
            self.end_headers()
            return
        path = os.path.join(STATIC_DIR, filename)
        if not os.path.isfile(path):
            self.send_response(404)
            self.end_headers()
            return
        content_type = "application/javascript; charset=utf-8"
        with open(path, "rb") as f:
            body = f.read()
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "public, max-age=3600")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        # 剥离 query 串（如 /api/data?x=1），避免带参数请求被 404
        path = urllib.parse.urlsplit(self.path).path
        if path == "/" or path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            html = HTML_TEMPLATE.replace(
                "__CHART_JS_SRC__", _asset_url("chart.umd.min.js", CDN_CHART_JS)
            ).replace(
                "__XLSX_SRC__", _asset_url("xlsx.full.min.js", CDN_XLSX)
            )
            self.wfile.write(html.encode("utf-8"))
        elif path.startswith("/static/"):
            self._serve_static(path[len("/static/"):])
        elif path == "/api/data":
            data = _get_data()
            self._send_json(data)
        elif path == "/api/status":
            # 根据实际生效的指标目录判断数据来源（git 克隆 / 本地文件）
            source = "git克隆" if GIT_PULL_ENABLED and get_metrics_dir() == GIT_METRICS_DIR else "本地文件"
            self._send_json({"source": source, "git_enabled": GIT_PULL_ENABLED})
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        """保存/清理执行结果备注。
        支持:
          POST /api/note            保存一条备注 {"yaml_name","date","branch","run_id","note"}
          POST /api/notes/clear     清理某用例的所有历史备注 {"yaml_name"}
        """
        path = urllib.parse.urlsplit(self.path).path
        # 可选鉴权：配置 NOTE_API_TOKEN 环境变量后，请求需在头 X-API-Token
        # 携带匹配 token；未配置时保持向后兼容（不校验）
        if path in ("/api/note", "/api/notes/clear"):
            expected_token = os.environ.get("NOTE_API_TOKEN", "")
            if expected_token and self.headers.get("X-API-Token") != expected_token:
                self._send_json({"ok": False, "error": "unauthorized"}, status=401)
                return
        if path == "/api/note":
            try:
                length = int(self.headers.get("Content-Length", 0) or 0)
                body = self.rfile.read(length).decode("utf-8") if length else "{}"
                data = json.loads(body)
                yaml_name = str(data.get("yaml_name", "") or "").strip()
                note = str(data.get("note", "") or "")
                date = str(data.get("date", "") or "").strip()
                branch = str(data.get("branch", "") or "").strip()
                run_id = str(data.get("run_id", "") or "").strip()
                if not yaml_name:
                    self._send_json({"ok": False, "error": "yaml_name is required"}, status=400)
                    return
                key = note_key_for(yaml_name, date, branch, run_id)
                ok = save_note(key, note)
                self._send_json({"ok": ok, "key": key})
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, status=400)
        elif path == "/api/notes/clear":
            try:
                length = int(self.headers.get("Content-Length", 0) or 0)
                body = self.rfile.read(length).decode("utf-8") if length else "{}"
                data = json.loads(body)
                yaml_name = str(data.get("yaml_name", "") or "").strip()
                if not yaml_name:
                    self._send_json({"ok": False, "error": "yaml_name is required"}, status=400)
                    return
                removed = clear_notes_for_case(yaml_name)
                self._send_json({"ok": True, "removed": removed})
            except Exception as e:
                self._send_json({"ok": False, "error": str(e)}, status=400)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def _sync_managed_repo(src_name, repo_root, repo_url, branch):
    """受管模式（方案A）：在 TESTCASES_CACHE_DIR 下稀疏克隆/更新源码仓缓存。
    只检出 workflows YAML 与测试脚本目录，避免全量克隆。
    检测半初始化残留（有 .git 但非 sparse 检出）时重新完整克隆。
    """
    branch = branch or "main"
    if os.path.isdir(os.path.join(repo_root, ".git")):
        # 历史残留：.git 存在但未启用 sparse-checkout（或未检出任何文件），
        # 增量更新无法修复，直接删除后重新稀疏克隆。
        if not _is_sparse_worktree(repo_root):
            print(f"[sync] {src_name}: 检测到未完成/损坏的受管目录，重新克隆 {repo_root}")
            _remove_dir_force(repo_root)
            _clone_managed_repo(src_name, repo_root, repo_url, branch)
        else:
            _update_managed_repo(src_name, repo_root, repo_url, branch)
    else:
        _clone_managed_repo(src_name, repo_root, repo_url, branch)


def _is_sparse_worktree(repo_root):
    """判断仓库是否已启用 sparse-checkout（受管目录正常状态）。"""
    try:
        result = _run(
            ["git", "sparse-checkout", "list"],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        return result.returncode == 0 and bool(result.stdout.strip())
    except Exception:
        return False


def _remove_dir_force(path):
    """可靠删除目录：Windows 上 .git 文件常带只读属性，shutil.rmtree 会失败，
    先解除只读再删除。返回是否成功。"""
    if not os.path.exists(path):
        return True
    try:
        # 递归解除只读属性（git 对象/索引文件常见只读）
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                p = os.path.join(root, name)
                try:
                    os.chmod(p, 0o777)
                except OSError:
                    pass
            for name in dirs:
                p = os.path.join(root, name)
                try:
                    os.chmod(p, 0o777)
                except OSError:
                    pass
        shutil.rmtree(path, ignore_errors=True)
    except Exception:
        pass
    return not os.path.exists(path)


def _clone_managed_repo(src_name, repo_root, repo_url, branch):
    """稀疏克隆源码仓到缓存目录（首次）。"""
    parent_dir = os.path.dirname(repo_root)
    os.makedirs(parent_dir, exist_ok=True)
    if os.path.exists(repo_root):
        _remove_dir_force(repo_root)
    print(f"[sync] {src_name}: 稀疏克隆 {repo_url} ({branch}) -> {repo_root}")
    try:
        result = _run(
            ["git", "clone", "--depth=1", "--no-checkout", "--branch", branch, repo_url, repo_root],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode != 0:
            print(f"[sync] {src_name}: clone failed: {result.stderr.strip()}")
            return
        result = _run(
            ["git", "sparse-checkout", "init", "--cone"],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            print(f"[sync] {src_name}: sparse-checkout init failed: {result.stderr.strip()}")
            return
        result = _run(
            ["git", "sparse-checkout", "set"] + SPARSE_CHECKOUT_PATHS,
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        if result.returncode != 0:
            print(f"[sync] {src_name}: sparse-checkout set failed: {result.stderr.strip()}")
            return
        result = _run(
            ["git", "checkout", branch],
            cwd=repo_root, capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            print(f"[sync] {src_name}: checkout failed: {result.stderr.strip()}")
            return
        print(f"[sync] {src_name}: 稀疏克隆完成")
    except Exception as e:
        print(f"[sync] {src_name}: clone error: {e}")


def _update_managed_repo(src_name, repo_root, repo_url, branch):
    """受管模式增量更新：fetch + reset 到远端分支；失败则重新克隆。"""
    branch = branch or "main"
    print(f"[sync] {src_name}: 增量更新 {repo_root} ({branch})")
    try:
        result = _run(
            ["git", "fetch", "origin", branch, "--depth=1"],
            cwd=repo_root, capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            # 增量更新失败（如远程 force push 导致历史不相关），重新克隆
            print(f"[sync] {src_name}: fetch 失败 ({result.stderr.strip()})，重新克隆")
            _remove_dir_force(repo_root)
            _clone_managed_repo(src_name, repo_root, repo_url, branch)
            return
        # reset --hard 在 cone 稀疏检出下仅物化稀疏路径内的文件
        result = _run(
            ["git", "reset", "--hard", f"origin/{branch}"],
            cwd=repo_root, capture_output=True, text=True, timeout=60,
        )
        if result.returncode != 0:
            print(f"[sync] {src_name}: reset failed: {result.stderr.strip()}")
            return
        print(f"[sync] {src_name}: 更新完成")
    except Exception as e:
        print(f"[sync] {src_name}: update error: {e}")


def _sync_local_repo(src_name, repo_root):
    """回退模式：repo_url 为空时，对本地路径执行原 git pull 逻辑。"""
    if not os.path.isdir(repo_root):
        print(f"[sync] {src_name}: repo not found at {repo_root} and no repo_url to clone")
        return

    print(f"[sync] {src_name}: pulling latest from {repo_root}")
    stashed = False
    try:
        # 检查是否有本地未提交改动，避免 reset --hard 清空用户改动
        status = _run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, timeout=30,
            cwd=repo_root,
        )
        has_local_changes = bool(status.stdout.strip())
        if has_local_changes:
            print(f"[sync] {src_name}: 检测到本地未提交改动，使用 stash 暂存后再更新（保留用户改动）")
            stash = _run(
                ["git", "stash", "push", "-u", "-m", "dashboard-sync"],
                capture_output=True, text=True, timeout=30,
                cwd=repo_root,
            )
            stashed = stash.returncode == 0
            if not stashed:
                print(f"[sync] {src_name}: stash 失败，跳过更新: {stash.stderr.strip()}")

        result = _run(
            ["git", "pull", "--ff-only"],
            capture_output=True, text=True, timeout=60,
            cwd=repo_root,
        )
        if result.returncode == 0:
            print(f"[sync] {src_name}: pull OK")
            if "Already up to date" not in (result.stdout + result.stderr):
                print(f"[sync] {src_name}: updated to latest")
        else:
            print(f"[sync] {src_name}: pull failed: {result.stderr.strip()}")

        # 恢复被暂存的本地改动
        if stashed:
            pop = _run(
                ["git", "stash", "pop"],
                capture_output=True, text=True, timeout=30,
                cwd=repo_root,
            )
            if pop.returncode != 0:
                # pop 失败（冲突）时改动仍在 stash 中，不丢失，仅提示
                print(f"[sync] {src_name}: stash pop 冲突，改动保留在 stash 中，请手动处理: {pop.stderr.strip()}")
            else:
                print(f"[sync] {src_name}: 本地改动已恢复")
    except subprocess.TimeoutExpired:
        print(f"[sync] {src_name}: pull timed out")
    except Exception as e:
        print(f"[sync] {src_name}: pull error: {e}")


def sync_repos():
    """同步所有配置的源码仓（用例列表 YAML + 测试脚本基线）。

    方案A（受管模式）：配置了 repo_url 的 source 在 TESTCASES_CACHE_DIR 下
    稀疏克隆/更新，只检出 workflows 与测试脚本目录，不依赖本地手动克隆。
    回退模式：repo_url 为空时沿用原逻辑，对本地路径执行 git pull。
    """
    for src_name, src_cfg in SOURCES.items():
        repo_root = src_cfg.get("repo_root", "")
        repo_url = src_cfg.get("repo_url", "")
        branch = src_cfg.get("branch", "")
        if not repo_root:
            print(f"[sync] {src_name}: no repo_root configured, skipping")
            continue

        if repo_url:
            _sync_managed_repo(src_name, repo_root, repo_url, branch)
        else:
            _sync_local_repo(src_name, repo_root)

    # 同步 suite→用例 注册信息（聚合 job 匹配用）
    sync_suite_registry()


def sync_suite_registry():
    """同步/构建 suite→用例 映射。

    新测试框架的聚合 suite job（如 nightly-perf-2-npu-a3）运行多个用例，
    job 名不含用例名。通过稀疏克隆 SUITE_REGISTRY_REPO_URL 分支的
    test/registered/npu 用例文件，解析 register_npu_ci(suite="X", nightly=True)
    注册信息，构建 {suite: [用例名]} / {用例名: suite} 映射。

    克隆/解析失败时仅打印错误，不影响平台其它功能（任务链接回退 run 级）。
    """
    global _suite_case_map, _case_suite_map, _suite_map_ts
    try:
        repo_root = SUITE_REGISTRY_CACHE_DIR
        if os.path.isdir(os.path.join(repo_root, ".git")):
            if not _is_sparse_worktree(repo_root):
                _remove_dir_force(repo_root)
            else:
                result = _run(
                    ["git", "fetch", "origin", SUITE_REGISTRY_BRANCH, "--depth=1"],
                    cwd=repo_root, capture_output=True, text=True, timeout=120,
                )
                if result.returncode != 0:
                    print(f"[suite] fetch failed: {result.stderr.strip()}")
                else:
                    _run(
                        ["git", "reset", "--hard", f"origin/{SUITE_REGISTRY_BRANCH}"],
                        cwd=repo_root, capture_output=True, text=True, timeout=60,
                    )
        if not os.path.isdir(os.path.join(repo_root, ".git")):
            # 首次：稀疏克隆仅 test/registered/npu
            parent = os.path.dirname(repo_root)
            os.makedirs(parent, exist_ok=True)
            _remove_dir_force(repo_root)
            result = _run(
                ["git", "clone", "--depth=1", "--no-checkout", "--branch",
                 SUITE_REGISTRY_BRANCH, SUITE_REGISTRY_REPO_URL, repo_root],
                capture_output=True, text=True, timeout=180,
            )
            if result.returncode != 0:
                print(f"[suite] clone failed: {result.stderr.strip()}")
                return
            # 与 _clone_managed_repo 保持一致：逐命令检查，任一失败则删除半初始化目录，
            # 下次同步重新克隆（避免留下只有 .git 而无检出文件的损坏目录）
            for cmd, step in [
                (["git", "sparse-checkout", "init", "--cone"], "sparse-checkout init"),
                (["git", "sparse-checkout", "set", SUITE_REGISTRY_SUBDIR], "sparse-checkout set"),
                (["git", "checkout", SUITE_REGISTRY_BRANCH], "checkout"),
            ]:
                result = _run(
                    cmd, cwd=repo_root, capture_output=True, text=True, timeout=60,
                )
                if result.returncode != 0:
                    print(f"[suite] {step} failed: {result.stderr.strip()}")
                    _remove_dir_force(repo_root)
                    return

        with _suite_map_lock:
            _suite_case_map, _case_suite_map = _build_suite_maps_from_registry(repo_root)
            _suite_map_ts = time.time()
        n_suites = len(_suite_case_map) if _suite_case_map else 0
        print(f"[suite] 构建 suite→用例 映射完成: {n_suites} 个 suite")
    except Exception as e:
        print(f"[suite] sync error: {e}")


def _build_suite_maps_from_registry(repo_root):
    """扫描用例注册目录，解析 register_npu_ci 调用，返回 (suite_cases, case_suite)。

    对每个 .py 文件解析所有 register_npu_ci(...) 调用参数，优先记录
    nightly=True 且 suite 非空的 suite（聚合 suite job 命名规则）。
    """
    suite_cases = {}
    case_suite = {}
    scan_root = os.path.join(repo_root, SUITE_REGISTRY_SUBDIR)
    if not os.path.isdir(scan_root):
        return suite_cases, case_suite
    for root, _, files in os.walk(scan_root):
        for fname in sorted(files):
            if not fname.endswith(".py"):
                continue
            filepath = os.path.join(root, fname)
            try:
                with open(filepath, "r", encoding="utf-8", errors="replace") as f:
                    content = f.read()
            except OSError:
                continue
            case_name = fname[:-3]  # 去掉 .py，如 test_npu_xxx
            # 解析 register_npu_ci(...) 的 suite= 与 nightly= 参数
            # 简化处理：提取所有 suite="X" 与 nightly=True 出现位置，
            # 通过括号配对找到同一调用内的参数。
            for m in re.finditer(r"register_npu_ci\s*\(", content):
                depth = 0
                start = m.end() - 1
                end = start
                for i in range(start, len(content)):
                    if content[i] == "(":
                        depth += 1
                    elif content[i] == ")":
                        depth -= 1
                        if depth == 0:
                            end = i + 1
                            break
                args_block = content[m.end() - 1:end]
                suite_m = re.search(r"suite\s*=\s*['\"]([^'\"]+)['\"]", args_block)
                nightly_m = re.search(r"nightly\s*=\s*True", args_block)
                if suite_m and nightly_m:
                    suite = suite_m.group(1).strip()
                    if suite:
                        suite_cases.setdefault(suite, [])
                        if case_name not in suite_cases[suite]:
                            suite_cases[suite].append(case_name)
                        # 用例可能注册到多个 nightly suite（如 nightly-perf-2-npu-a3 与
                        # full-16-npu-a3）。聚合 job 名与 nightly- 前缀 suite 对应，
                        # 优先记录 nightly- 开头的 suite，保证匹配到正确的聚合 job。
                        if case_name not in case_suite or \
                           (suite.startswith("nightly-") and not case_suite[case_name].startswith("nightly-")):
                            case_suite[case_name] = suite
    return suite_cases, case_suite


def get_case_suite_map():
    """返回用例 → suite 映射（懒构建，未同步时尝试本地已缓存映射）。"""
    global _suite_case_map, _case_suite_map, _suite_map_ts
    with _suite_map_lock:
        if _case_suite_map is None:
            # 尝试从本地缓存目录直接解析（无需网络）
            try:
                repo_root = SUITE_REGISTRY_CACHE_DIR
                if os.path.isdir(os.path.join(repo_root, ".git")):
                    _suite_case_map, _case_suite_map = _build_suite_maps_from_registry(repo_root)
                    _suite_map_ts = time.time()
            except Exception:
                _case_suite_map = {}
        return _case_suite_map or {}


def _match_job_for_case_with_suite(case_key, jobs, case_suite_map):
    """增强匹配：先按用例名匹配（matrix job），失败后按用例所属 suite
    匹配聚合 job（新框架聚合 suite job 名 = suite 名）。
    """
    job = _match_job_for_case(case_key, jobs)
    if job:
        return job
    # 用例名直接匹配失败 → 尝试 suite 聚合 job
    if case_suite_map and jobs:
        # case_suite_map 的 key 可能带/不带 test_npu_ 前缀，双向兼容
        candidates = []
        base = case_key
        candidates.append(base)
        if base.startswith("test_npu_"):
            candidates.append(base[len("test_npu_"):])
        else:
            candidates.append("test_npu_" + base)
        suite = None
        for c in candidates:
            if c in case_suite_map:
                suite = case_suite_map[c]
                break
        if suite and suite in jobs:
            return jobs[suite]
    return None


_sync_thread_started = False
_sync_thread_lock = threading.RLock()  # 保护 sync 线程启动标志


def _ensure_sync_thread():
    """确保后台周期同步线程已启动（单次）。"""
    global _sync_thread_started
    with _sync_thread_lock:
        if _sync_thread_started:
            return
        _sync_thread_started = True
    t = threading.Thread(target=_sync_worker, daemon=True)
    t.start()


def _sync_worker():
    """后台线程：周期性同步源码仓并刷新基线/脚本链接缓存，
    保证平台长时间运行期间脚本仓新增/更新用例持续生效。
    """
    while True:
        time.sleep(SOURCE_SYNC_INTERVAL)
        try:
            sync_repos()
            collect_baselines(force=True)
            collect_script_urls(force=True)
        except Exception as e:
            print(f"[sync] periodic sync error: {e}")


# ============================================================
# 备注 git 持久化：定期将 notes.json commit + push 到当前 git 仓。
# 与 collect_metrics.sh 的上传模式一致，仅在存在变更时提交。
# 未配置 git / push 失败时静默跳过（本地 notes.json 始终已持久化）。
# ============================================================
_notes_git_thread_started = False
_notes_git_thread_lock = threading.RLock()  # 保护 notes git 线程启动标志


def _git_repo_root():
    """查找当前项目所在 git 仓根目录（向上遍历直到找到 .git）。"""
    d = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.isdir(os.path.join(d, ".git")):
            return d
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def _push_notes_to_git():
    """将 notes.json 提交并推送到当前 git 仓。成功返回 True。"""
    global _notes_dirty
    repo_root = _git_repo_root()
    if not repo_root:
        return False
    rel_path = os.path.relpath(_notes_path(), repo_root).replace("\\", "/")
    try:
        # 只提交 notes.json，避免把其他未跟踪/改动文件带入
        r = _run(
            ["git", "add", "--", rel_path], cwd=repo_root,
            capture_output=True, text=True, timeout=60,
        )
        if r.returncode != 0:
            print(f"[notes-git] add failed: {r.stderr.strip()[:200]}")
            return False
        r = _run(
            ["git", "commit", "-m", "dashboard: update test case notes", "--", rel_path],
            cwd=repo_root, capture_output=True, text=True, timeout=60,
        )
        if r.returncode != 0 and "nothing to commit" not in r.stdout + r.stderr:
            print(f"[notes-git] commit failed: {r.stderr.strip()[:200]}")
            return False
        # 推送前先追平远端（同事的备注提交），避免 push 因远端已推进被拒绝
        r = _run(
            ["git", "pull", "--rebase", "--autostash", "origin", "main"],
            cwd=repo_root, capture_output=True, text=True, timeout=120,
        )
        if r.returncode != 0:
            print(f"[notes-git] pull --rebase failed: {r.stderr.strip()[:200]}")
            return False
        r = _run(
            ["git", "push", "origin", "HEAD"], cwd=repo_root,
            capture_output=True, text=True, timeout=120,
        )
        if r.returncode != 0:
            print(f"[notes-git] push failed: {r.stderr.strip()[:200]}")
            return False
        _notes_dirty = False
        return True
    except Exception as e:
        print(f"[notes-git] error: {e}")
        return False


def _notes_git_worker():
    """后台线程：定期将变更的备注提交到 git 仓。"""
    while True:
        time.sleep(NOTES_GIT_INTERVAL)
        if not NOTES_GIT_PUSH_ENABLED:
            continue
        if _notes_dirty:
            _push_notes_to_git()


def _ensure_notes_git_thread():
    """确保备注 git 持久化线程已启动（单次）。"""
    global _notes_git_thread_started
    with _notes_git_thread_lock:
        if _notes_git_thread_started:
            return
        _notes_git_thread_started = True
    t = threading.Thread(target=_notes_git_worker, daemon=True)
    t.start()


def start_dashboard():
    print("=" * 60)
    print("[startup] Syncing test case repos...")
    sync_repos()
    # 启动时从两个代码仓的测试脚本刷新基线缓存
    print("[startup] Refreshing baselines from test scripts...")
    collect_baselines(force=True)
    # 启动时重建用例脚本在 Git 平台的链接映射（sync_repos 已拉取最新脚本）
    print("[startup] Refreshing test script git links...")
    collect_script_urls(force=True)
    # 清空 GitHub jobs 缓存，让首次数据加载时重新拉取每个 run 的 job 列表
    print("[startup] Resetting GitHub Actions jobs cache...")
    force_refresh_jobs()
    # 后台周期同步：持续拉取最新用例/基线
    _ensure_sync_thread()
    # 后台定期将用例备注持久化到 git 仓
    if NOTES_GIT_PUSH_ENABLED:
        print(f"[startup] Notes git persistence enabled (every {NOTES_GIT_INTERVAL}s)")
        _ensure_notes_git_thread()
    print("=" * 60)
    server = socketserver.ThreadingTCPServer((DASHBOARD_HOST, DASHBOARD_PORT), DashboardHandler)
    print(f"Dashboard running at http://{DASHBOARD_HOST}:{DASHBOARD_PORT}")
    server.serve_forever()


if __name__ == "__main__":
    if "--update-testcases-config" in sys.argv:
        # 先同步代码仓，再基于最新 YAML + 注册器扫描结果生成本地配置文件
        sync_repos()
        regenerate_testcases_config()
    else:
        start_dashboard()
