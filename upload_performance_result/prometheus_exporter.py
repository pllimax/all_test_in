"""
Prometheus exporter for sglang benchmark results.
Scans date-foldered benchmark files and exposes key metrics via HTTP.
Supports dynamic Git pull for data updates.
"""
import os
import re
import time
import shutil
import subprocess
import threading
import urllib.parse
from prometheus_client import start_http_server, Gauge


def _run(cmd, **kw):
    """subprocess.run 包装：默认捕获输出并以 UTF-8 解码（兼容 Windows 下 git 的
    UTF-8 输出与本地 GBK 编码不一致导致 text=True 解码抛异常的问题）。"""
    kw.setdefault("capture_output", True)
    kw.setdefault("text", True)
    kw.setdefault("encoding", "utf-8")
    kw.setdefault("errors", "replace")
    return subprocess.run(cmd, **kw)


def _mask_repo_url(url):
    """脱敏仓库地址：去掉 URL 中内嵌的凭据（userinfo），避免日志泄漏 token。"""
    try:
        parts = urllib.parse.urlsplit(url or "")
        if parts.username or parts.password:
            netloc = parts.hostname or ""
            if parts.port:
                netloc += f":{parts.port}"
            parts = parts._replace(netloc=netloc)
        return parts.geturl()
    except Exception:
        return url or ""


def _reliable_rmtree(path):
    """可靠删除目录：Windows 上 git 对象/索引文件常带只读属性，shutil.rmtree 会
    半删除留下损坏目录，先递归解除只读再删除。删除后目录仍存在则返回 False。"""
    if not os.path.isdir(path):
        return True
    try:
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

# Git repo config for syncing metrics data
GIT_REPO_URL = os.environ.get("GIT_REPO_URL", "https://github.com/pllimax/all_test_in.git")
GIT_BRANCH = os.environ.get("GIT_BRANCH", "main")
GIT_TARGET_PATH = os.environ.get("GIT_TARGET_PATH", "upload_performance_result/metrics/sglang")
GIT_SPARSE_PATH = os.environ.get("GIT_SPARSE_PATH", "upload_performance_result/metrics/")
GIT_LOCAL_CLONE = os.environ.get("GIT_LOCAL_CLONE",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), ".data_repo"))

# If GIT_PULL_ENABLED=true, metrics data is synced from Git before reading
GIT_PULL_ENABLED = os.environ.get("GIT_PULL_ENABLED", "true").lower() in ("1", "true", "yes")
LOCAL_METRICS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metrics", "sglang")
GIT_METRICS_DIR = os.path.join(GIT_LOCAL_CLONE, GIT_TARGET_PATH)

def get_metrics_dir():
    """Return the active metrics directory, preferring Git clone if available."""
    if GIT_PULL_ENABLED and os.path.isdir(GIT_METRICS_DIR):
        return GIT_METRICS_DIR
    return LOCAL_METRICS_DIR

METRICS_DIR = get_metrics_dir()

# ============================================================
# 新目录结构 workflow 目录名 → 标准 workflow 类型
# 新结构: metrics/sglang/{branch}-{run_id}/{workflow_name}/结果文件
#   Full_Test_NPU    → fulltest
#   Nightly_Test_NPU → nightly
# ============================================================
WORKFLOW_NAME_MAP = {
    "Full_Test_NPU": "fulltest",
    "Full_Test_(NPU)": "fulltest",
    "Nightly_Test_NPU": "nightly",
    "Nightly_Test_(NPU)": "nightly",
    "Single_Test_NPU": "single",
    "Single_Test_(NPU)": "single",
}


def _is_date_dir(name):
    """判断目录名是否为日期格式（旧结构按日期存放）。"""
    return bool(re.match(r"^\d{8}$", name))


def date_from_label(date_label):
    """从目录标记中提取展示日期（以数据目录中的 create_date 为准）。

    旧结构（日期目录 YYYYMMDD）→ 目录名本身；
    新结构（分支模式 {branch}-{date}-{time}-{run_id}-{attempt}/{workflow}）
    → 目录名中的日期段（CI 任务创建日期，同一任务的所有用例显示在同一天）。
    无法解析时原样返回。
    """
    top = str(date_label).split("/", 1)[0]
    if _is_date_dir(top):
        return top
    # 新格式：{branch}-{date}-{time}-{run_id}-{attempt}（time 段 2-4 位，run_id 至少 5 位）
    m = re.search(r"-(\d{8})-(\d{2,4})-(\d{5,})", top)
    if m:
        return m.group(1)
    # 旧格式（分支模式）：{branch}-{date}-{run_id}[-{attempt}]
    m = re.search(r"-(\d{8})-(\d{5,})", top)
    if m:
        return m.group(1)
    return top


def _iter_metrics_files(metrics_dir, suffix, subdir=""):
    """遍历 metrics 目录下所有结果文件，兼容新旧两种目录结构。

    旧结构: {date}/file.suffix                    (date = 20260727)
    新结构: {branch}-{run_id}/{workflow_name}/file.suffix
            其中 workflow_name 映射为 fulltest/nightly

    Args:
        metrics_dir: metrics 根目录
        suffix: 文件名后缀（如 ".txt" / ".log"）
        subdir: 可选子目录名（如 "eval" / "accuracy"），仅在该子目录内查找

    Yields:
        (date_label, filepath)
        date_label: 旧结构为日期，新结构为 "{branch}-{run_id}/{workflow}"
    """
    if not os.path.isdir(metrics_dir):
        return

    for top in sorted(os.listdir(metrics_dir)):
        top_path = os.path.join(metrics_dir, top)
        if not os.path.isdir(top_path):
            continue

        if _is_date_dir(top):
            # 旧结构：日期目录
            scan_dir = os.path.join(top_path, subdir) if subdir else top_path
            if not os.path.isdir(scan_dir):
                continue
            for name in sorted(os.listdir(scan_dir)):
                if name.endswith(suffix):
                    yield top, os.path.join(scan_dir, name)
        else:
            # 新结构：{branch}-{run_id}/{workflow_name}/
            for wf_dir in sorted(os.listdir(top_path)):
                wf_path = os.path.join(top_path, wf_dir)
                if not os.path.isdir(wf_path):
                    continue
                workflow = WORKFLOW_NAME_MAP.get(wf_dir, wf_dir.lower())
                date_label = f"{top}/{workflow}"
                scan_dir = os.path.join(wf_path, subdir) if subdir else wf_path
                if not os.path.isdir(scan_dir):
                    continue
                for name in sorted(os.listdir(scan_dir)):
                    if name.endswith(suffix):
                        yield date_label, os.path.join(scan_dir, name)


# Define the 4 key metrics as Gauges with labels
LABELS = ["date", "model", "quantization", "parallelism", "input_len", "output_len", "request_rate", "dataset"]

mean_ttft = Gauge(
    "sglang_mean_ttft_ms",
    "Mean Time to First Token (ms)",
    LABELS,
)

mean_tpot = Gauge(
    "sglang_mean_tpot_ms",
    "Mean Time per Output Token excluding first token (ms)",
    LABELS,
)

mean_e2e_latency = Gauge(
    "sglang_mean_e2e_latency_ms",
    "Mean End-to-End Latency (ms)",
    LABELS,
)

output_token_throughput = Gauge(
    "sglang_output_token_throughput_tok_per_s",
    "Output token throughput (tok/s)",
    LABELS,
)

p90_ttft = Gauge(
    "sglang_p90_ttft_ms",
    "P90 Time to First Token (ms)",
    LABELS,
)

p90_tpot = Gauge(
    "sglang_p90_tpot_ms",
    "P90 Time per Output Token excluding first token (ms)",
    LABELS,
)

total_token_throughput = Gauge(
    "sglang_total_token_throughput_tok_per_s",
    "Total token throughput (tok/s)",
    LABELS,
)

total_requests = Gauge(
    "sglang_total_requests",
    "Total successful requests",
    LABELS,
)

max_concurrency = Gauge(
    "sglang_max_concurrency",
    "Max request concurrency",
    LABELS,
)

system_concurrency = Gauge(
    "sglang_system_concurrency",
    "System concurrency",
    LABELS,
)

request_throughput = Gauge(
    "sglang_request_throughput_req_per_s",
    "Request throughput (req/s)",
    LABELS,
)


def parse_filename(filename):
    """Extract labels from benchmark filename.
    Examples:
      test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.txt
      test_npu_qwen3_6_35b_a3b_1p_in1080p_30_out256_50ms.txt
      test_npu_mimo_v2_flash_1p1d_12p_in32k_out1_ttft_5s.txt
      test_npu_qwen3_6_27b_w8a8_2p_in16k_out1k_50ms_1.txt
      test_npu_qwen3_32b_w8a8_2p_in3k5_out1k_50ms__20260726.txt  (含源日期后缀)
    """
    name = os.path.splitext(filename)[0]
    # Strip __YYYYmmdd source date suffix (added by collect_metrics.sh)
    name = re.sub(r"__\d{8}$", "", name)
    # Strip -HHMMSS CI timestamp suffix (from CI directory naming)
    name = re.sub(r"-\d{6}(?=_.*|$)", "", name)
    name = name.replace("test_npu_", "", 1)

    # Strip numeric run suffix (e.g., _1, _2, ..., _19)
    name = re.sub(r"_\d+$", "", name)

    # Strip _a2 chip marker suffix (must be before field extraction below)
    name = re.sub(r"_a2$", "", name)

    # Extract extra parameters that distinguish test cases:
    #   _prefix\d+  (prefix cache ratio) -> appended to input_len
    #   _bs\d+      (batch size)         -> appended to output_len
    extra_prefix = ""
    extra_bs = ""
    pm = re.search(r"_(prefix\d+)", name)
    if pm:
        extra_prefix = pm.group(1)
        name = name[:pm.start()] + name[pm.end():]
    bm = re.search(r"_(bs\d+)", name)
    if bm:
        extra_bs = bm.group(1)
        name = name[:bm.start()] + name[bm.end():]

    # Extract dataset suffix (e.g., _aime26, _gpqa)
    dataset = ""
    dataset_match = re.search(r"_(aime\d+|gpqa|mmmu|random)$", name)
    if dataset_match:
        dataset = dataset_match.group(1)
        name = name[: dataset_match.start()]

    # Extract request_rate (e.g., _50ms, _5s, _inf)
    request_rate = ""
    rr_match = re.search(r"_(\d+ms|\d+s|inf)$", name)
    if rr_match:
        request_rate = rr_match.group(1)
        name = name[: rr_match.start()]

    # Handle special benchmark type suffixes (_ttft, _tpot)
    bench_type = ""
    bt_match = re.search(r"_(ttft|tpot)$", name)
    if bt_match:
        bench_type = bt_match.group(1)
        name = name[: bt_match.start()]
        if not dataset:
            dataset = bench_type

    # Extract input_len for multimodal cases first (e.g., _in1024x1024_30, _in1080p_30)
    # Resolution -> input_len, frame count -> output_len
    input_len = ""
    output_len = ""
    mm_match = re.search(r"_in(1024x1024|1080p)_(\d+)", name)
    if mm_match:
        input_len = mm_match.group(1)
        output_len = mm_match.group(2)
        name = name[: mm_match.start()]
        # Strip the _out part for multimodal cases (output_len already set from frame count)
        out_strip = re.search(r"_out\d+k?\d*$", name)
        if out_strip:
            name = name[: out_strip.start()]
    else:
        # Extract output_len (e.g., _out1k, _out1k5, _out100, _out256)
        out_match = re.search(r"_out(\d+k?\d*)$", name)
        if out_match:
            output_len = out_match.group(1)
            name = name[: out_match.start()]

        # Extract input_len (e.g., _in64k, _in3k5)
        in_match = re.search(r"_in(\d+k?\d*)$", name)
        if in_match:
            input_len = in_match.group(1)
            name = name[: in_match.start()]

    # Append extra parameters to distinguish cases
    prefix = extra_prefix  # e.g., "prefix90"
    if extra_bs:
        output_len = (output_len + "_" + extra_bs) if output_len else extra_bs

    # Extract parallelism (e.g., _1p1d_32p, _8p, _2p1d_32p, _1p)
    parallelism = ""
    p_match = re.search(r"_(\d+p\d*d?(?:_\d+p)?)$", name)
    if p_match:
        parallelism = p_match.group(1)
        name = name[: p_match.start()]

    # Extract quantization (e.g., _w4a8, _w8a8, _bf16)
    quantization = ""
    q_match = re.search(r"_(w\d+a\d+|bf16|fp8|fp16)$", name)
    if q_match:
        quantization = q_match.group(1)
        name = name[: q_match.start()]

    model = name

    return {
        "model": model,
        "quantization": quantization,
        "parallelism": parallelism,
        "input_len": input_len,
        "output_len": output_len,
        "request_rate": request_rate,
        "dataset": dataset,
        "prefix": prefix,
    }


def parse_benchmark_file(filepath):
    """Parse a benchmark result file and extract all key metrics."""
    metrics = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None

    patterns = {
        "mean_ttft": r"Mean TTFT \(ms\):\s+([\d.]+)",
        "mean_tpot": r"Mean TPOT \(ms\):\s+([\d.]+)",
        "mean_e2e_latency": r"Mean E2E Latency \(ms\):\s+([\d.]+)",
        "output_token_throughput": r"Output token throughput \(tok/s\):\s+([\d.]+)",
    }

    for key, pattern in patterns.items():
        match = re.search(pattern, content)
        if match:
            metrics[key] = float(match.group(1))
        else:
            return None  # File missing required metrics

    # Optional P90 and total throughput metrics
    optional_patterns = {
        "p90_ttft": r"P90 TTFT \(ms\):\s+([\d.]+)",
        "p90_tpot": r"P90 TPOT \(ms\):\s+([\d.]+)",
        "total_token_throughput": r"Total token throughput \(tok/s\):\s+([\d.]+)",
        "total_requests": r"Successful requests:\s+([\d]+)",
        "max_concurrency": r"Max request concurrency:\s+([\d]+)",
        "system_concurrency": r"Concurrency:\s+([\d.]+)",
        "request_throughput": r"Request throughput \(req/s\):\s+([\d.]+)",
    }
    for key, pattern in optional_patterns.items():
        match = re.search(pattern, content)
        if match:
            metrics[key] = float(match.group(1))
        else:
            metrics[key] = None

    return metrics


# 性能指标字段：纯精度用例（accuracy）在输出时清空这些字段，只保留精度结果
PERF_ONLY_FIELDS = [
    "mean_ttft", "mean_tpot", "mean_e2e_latency", "output_token_throughput",
    "p90_ttft", "p90_tpot", "total_token_throughput", "total_requests",
    "max_concurrency", "system_concurrency", "request_throughput",
]


def parse_eval_log(filepath):
    """Parse an eval log file and extract the accuracy score.
    Handles both MMMU (multi-subset with OVERALL row) and non-MMMU (single row) formats.
    Returns the score as a float, or None if not found.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None

    # Pattern for a data row with OVERALL in the Subset column:
    # │ ... │ ... │ ... │ ...OVERALL... │ digits │ float │ ... │
    overall_data_pattern = r"│[^│]*OVERALL[^│]*│\s*\d+\s*│\s*([\d.]+)\s*│"
    # Generic data row pattern: │ ... │ ... │ ... │ ... │ digits │ float │ ... │
    generic_data_pattern = r"│[^│]*│[^│]*│[^│]*│[^│]*│\s*\d+\s*│\s*([\d.]+)\s*│"

    # Strategy 1: look for "Overall report table" section
    overall_idx = content.rfind("Overall report table")
    if overall_idx != -1:
        tail = content[overall_idx:]

        # Try to find an OVERALL row first (MMMU-style multi-subset)
        match = re.search(overall_data_pattern, tail)
        if match:
            return float(match.group(1))

        # Fallback: first data row (single-subset, e.g., gsm8k/aime25)
        match = re.search(generic_data_pattern, tail)
        if match:
            return float(match.group(1))

        return None

    # Strategy 2: no "Overall report table" → search entire content for OVERALL row
    # (older evalscope versions with MMMU breakdown table)
    match = re.search(overall_data_pattern, content)
    if match:
        return float(match.group(1))

    # Strategy 3: last resort — single score row anywhere in content
    match = re.search(generic_data_pattern, content)
    if match:
        return float(match.group(1))

    return None


def _parse_eval_log_filename(base):
    """统一解析 eval 日志文件名（不含 .log 后缀），返回干净的用例名；无法解析时返回 None。

    支持的命名格式：
      简化格式: {tc_name}__{date}.log
      新格式:   {test_type}__{tc_name}__{date}.log  (test_type = perf/accuracy)
      历史格式: {tc_name}__{eval_ts}.log            (eval_ts = 20260717_204110)
      历史格式: {tc_name}-{ci_ts}__{eval_ts}__{date}.log
      历史格式: {date}__{tc_name}__{source_date}.log
      变体后缀: __{eval_ts}-perf.log / __{eval_ts}-output.log
    最后一段可能为: 20260726 | 20260717_204110 | 20260718_103021-perf |
                    20260725_210147-output | 20260806-1
    """
    if "__" not in base:
        return None
    parts = base.split("__")
    if len(parts) < 2 or not re.match(r"^\d{8}(?:_\d{6})?(?:-(?:\d+|perf|output))?$", parts[-1]):
        return None
    test_case_name = parts[0]
    # 兼容带前缀格式: {test_type}__{tc}__{date} / {date}__{tc}__{source_date}
    if len(parts) >= 3 and (
        test_case_name in ("perf", "accuracy")
        or re.match(r"^\d{8}$", test_case_name)
    ):
        test_case_name = parts[1]
    # 剥离 CI 时间戳后缀（-HHMMSS），如 test_npu_x-205203 → test_npu_x
    test_case_name = re.sub(r"-\d{6}$", "", test_case_name)
    return test_case_name or None


def collect_eval_data():
    """Scan all date folders' eval/ subdirectories and collect accuracy scores.
    For the same test case on the same date, keep only the highest score.
    Returns a dict: {(test_case_name, date): max_score}
    """
    eval_data = {}
    metrics_dir = get_metrics_dir()

    if not os.path.isdir(metrics_dir):
        return eval_data

    for date_folder, filepath in _iter_metrics_files(metrics_dir, ".log", "eval"):
        filename = os.path.basename(filepath)
        # Filename format (new): test_type__test_case_name__YYYYmmdd.log
        # Filename format (old): test_case_name__YYYYMMDD_HHMMSS.log
        #                                or test_case_name__YYYYMMDD_HHMMSS__YYYYmmdd.log
        test_case_name = _parse_eval_log_filename(filename[:-4])  # strip .log
        if not test_case_name:
            continue
        score = parse_eval_log(filepath)

        if score is not None:
            key = (test_case_name, date_folder)
            if key not in eval_data or score > eval_data[key]:
                eval_data[key] = score

    return eval_data


def collect_accuracy_only_data():
    """Scan accuracy/ subdirectories in each date folder for standalone accuracy tests.
    These tests have no performance metrics, only eval scores.
    Returns a list of dicts with model labels and eval_score.
    """
    results = []
    metrics_dir = get_metrics_dir()

    if not os.path.isdir(metrics_dir):
        return results

    # Track best score per test case per date (date_label)
    best_scores = {}

    for date_folder, filepath in _iter_metrics_files(metrics_dir, ".log", "accuracy"):
        filename = os.path.basename(filepath)
        test_case_name = _parse_eval_log_filename(filename[:-4])
        if not test_case_name:
            continue
        score = parse_eval_log(filepath)

        if score is not None:
            key = (test_case_name, date_folder)
            if key not in best_scores or score > best_scores[key]:
                best_scores[key] = score

    # Build result entries
    for (test_case_name, date), score in best_scores.items():
        labels = parse_filename(test_case_name + ".txt")
        labels["date"] = date
        labels["eval_score"] = score
        # Derive yaml name from test_case_name
        yaml_name = test_case_name
        if yaml_name.startswith("test_npu_"):
            yaml_name = yaml_name[len("test_npu_"):]
        labels["yaml_name"] = yaml_name
        # No performance metrics（纯精度用例，清空性能字段）
        labels.update({k: None for k in PERF_ONLY_FIELDS})
        results.append(labels)

    return results


def _clone_repo():
    """Clone the Git repository with shallow + sparse checkout (metrics directory only).
    Returns True on success, False on failure.
    """
    print(f"[git] Cloning metrics data from: {_mask_repo_url(GIT_REPO_URL)}")
    os.makedirs(os.path.dirname(GIT_LOCAL_CLONE), exist_ok=True)
    # Step 1: shallow clone without checkout
    result = _run(
        ["git", "clone", "--depth=1", "--no-checkout",
         "--branch", GIT_BRANCH, GIT_REPO_URL, GIT_LOCAL_CLONE],
        timeout=120
    )
    if result.returncode != 0:
        print(f"[git] clone failed: {result.stderr.strip()}")
        return False
    # Step 2: enable sparse checkout (cone mode)
    result = _run(
        ["git", "sparse-checkout", "init", "--cone"],
        cwd=GIT_LOCAL_CLONE, timeout=30
    )
    if result.returncode != 0:
        print(f"[git] sparse-checkout init failed: {result.stderr.strip()}")
        return False
    # Step 3: set sparse path to metrics directory only
    result = _run(
        ["git", "sparse-checkout", "set", GIT_SPARSE_PATH],
        cwd=GIT_LOCAL_CLONE, timeout=30
    )
    if result.returncode != 0:
        print(f"[git] sparse-checkout set failed: {result.stderr.strip()}")
        return False
    # Step 4: checkout only the sparse paths
    result = _run(
        ["git", "checkout", GIT_BRANCH],
        cwd=GIT_LOCAL_CLONE, timeout=60
    )
    if result.returncode != 0:
        print(f"[git] checkout failed: {result.stderr.strip()}")
        return False
    print("[git] Metrics data cloned successfully")
    return True


_git_pull_lock = threading.Lock()

def git_pull():
    """Sync metrics data from Git repository using sparse checkout.
    - Clone: shallow clone with sparse checkout, only pull metrics/ directory
    - Update: fetch and checkout only metrics/ files, never reset code
    Throttled: only actually pulls if at least 60s since last pull.
    Falls back to re-cloning if fetch fails (e.g. remote force-push).
    """
    if not GIT_PULL_ENABLED:
        return

    # Throttle: don't pull more than once per 60 seconds
    with _git_pull_lock:
        now = time.time()
        if now - git_pull._last_pull < 60:
            return
        git_pull._last_pull = now

    try:
        if os.path.isdir(os.path.join(GIT_LOCAL_CLONE, ".git")):
            # Update: fetch latest and checkout only the metrics directory
            result = _run(
                ["git", "fetch", "origin", GIT_BRANCH, "--depth=1"],
                cwd=GIT_LOCAL_CLONE, timeout=60
            )
            if result.returncode != 0:
                # Fetch failed (e.g. remote force-push causing unrelated histories),
                # fall back to re-cloning
                print(f"[git] fetch failed ({result.stderr.strip()}), re-cloning...")
                _reliable_rmtree(GIT_LOCAL_CLONE)
                _clone_repo()
                return
            # Only checkout metrics files, never reset code
            result = _run(
                ["git", "checkout", f"origin/{GIT_BRANCH}", "--", GIT_SPARSE_PATH.rstrip("/")],
                cwd=GIT_LOCAL_CLONE, timeout=60
            )
            if result.returncode != 0:
                print(f"[git] checkout failed: {result.stderr.strip()}")
                return
            print("[git] Metrics data updated successfully")
        else:
            _clone_repo()
    except subprocess.TimeoutExpired:
        print("[git] Operation timed out")
    except FileNotFoundError:
        print("[git] Git not found in PATH, falling back to local data")
    except Exception as e:
        print(f"[git] Error: {e}")

git_pull._last_pull = 0


def collect_metrics():
    """Scan all date folders and update Prometheus metrics."""
    metrics_dir = get_metrics_dir()
    # Clear existing metrics
    mean_ttft.clear()
    mean_tpot.clear()
    mean_e2e_latency.clear()
    output_token_throughput.clear()
    p90_ttft.clear()
    p90_tpot.clear()
    total_token_throughput.clear()
    total_requests.clear()
    max_concurrency.clear()
    system_concurrency.clear()
    request_throughput.clear()

    if not os.path.isdir(metrics_dir):
        print(f"Metrics directory not found: {metrics_dir}")
        return

    for date_folder, filepath in _iter_metrics_files(metrics_dir, ".txt"):
        filename = os.path.basename(filepath)
        parsed = parse_benchmark_file(filepath)
        if parsed is None:
            continue

        labels = parse_filename(filename)
        labels["date"] = date_from_label(date_folder)

        label_values = [labels[k] for k in LABELS]

        mean_ttft.labels(*label_values).set(parsed["mean_ttft"])
        mean_tpot.labels(*label_values).set(parsed["mean_tpot"])
        mean_e2e_latency.labels(*label_values).set(parsed["mean_e2e_latency"])
        output_token_throughput.labels(*label_values).set(parsed["output_token_throughput"])
        if parsed.get("p90_ttft") is not None:
            p90_ttft.labels(*label_values).set(parsed["p90_ttft"])
        if parsed.get("p90_tpot") is not None:
            p90_tpot.labels(*label_values).set(parsed["p90_tpot"])
        if parsed.get("total_token_throughput") is not None:
            total_token_throughput.labels(*label_values).set(parsed["total_token_throughput"])
        if parsed.get("total_requests") is not None:
            total_requests.labels(*label_values).set(parsed["total_requests"])
        if parsed.get("max_concurrency") is not None:
            max_concurrency.labels(*label_values).set(parsed["max_concurrency"])
        if parsed.get("system_concurrency") is not None:
            system_concurrency.labels(*label_values).set(parsed["system_concurrency"])
        if parsed.get("request_throughput") is not None:
            request_throughput.labels(*label_values).set(parsed["request_throughput"])

    print(f"Metrics updated at {time.strftime('%Y-%m-%d %H:%M:%S')}")


def update_loop(interval=300):
    """Periodically pull from Git and update metrics."""
    while True:
        git_pull()
        collect_metrics()
        time.sleep(interval)


if __name__ == "__main__":
    # Initial Git pull + collection
    git_pull()
    collect_metrics()

    # Start background updater
    updater = threading.Thread(target=update_loop, args=(300,), daemon=True)
    updater.start()

    # Start HTTP server
    port = int(os.environ.get("EXPORTER_PORT", "9099"))
    start_http_server(port)
    print(f"Prometheus exporter listening on port {port}")
    print(f"Metrics directory: {METRICS_DIR}")

    # Keep main thread alive
    try:
        while True:
            time.sleep(60)
    except KeyboardInterrupt:
        print("Shutting down...")
