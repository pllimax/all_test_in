"""
Prometheus exporter for sglang benchmark results.
Scans date-foldered benchmark files and exposes key metrics via HTTP.
Supports dynamic Git pull for data updates.
"""
import os
import re
import time
import glob
import subprocess
from prometheus_client import start_http_server, Gauge, Info
from prometheus_client.core import REGISTRY

# Git repo config (same as collect_metrics.sh)
GIT_REPO_URL = os.environ.get("GIT_REPO_URL", "git@github.com-pllimax:pllimax/all_test_in.git")
GIT_BRANCH = os.environ.get("GIT_BRANCH", "main")
GIT_TARGET_PATH = os.environ.get("GIT_TARGET_PATH", "upload_performance_result/metrics/sglang")
GIT_LOCAL_CLONE = os.environ.get("GIT_LOCAL_CLONE",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), ".data_repo"))

# If GIT_PULL_ENABLED=true, data is pulled from Git; otherwise read local metrics/
GIT_PULL_ENABLED = os.environ.get("GIT_PULL_ENABLED", "true").lower() in ("1", "true", "yes")
LOCAL_METRICS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "metrics", "sglang")
GIT_METRICS_DIR = os.path.join(GIT_LOCAL_CLONE, GIT_TARGET_PATH)

def get_metrics_dir():
    """Return the active metrics directory, preferring Git clone if available."""
    if GIT_PULL_ENABLED and os.path.isdir(GIT_METRICS_DIR):
        return GIT_METRICS_DIR
    return LOCAL_METRICS_DIR

METRICS_DIR = get_metrics_dir()

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


def parse_filename(filename):
    """Extract labels from benchmark filename.
    Examples:
      test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.txt
      test_npu_qwen3_6_35b_a3b_1p_in1080p_30_out256_50ms.txt
      test_npu_mimo_v2_flash_1p1d_12p_in32k_out1_ttft_5s.txt
      test_npu_qwen3_6_27b_w8a8_2p_in16k_out1k_50ms_1.txt
    """
    name = os.path.splitext(filename)[0]
    name = name.replace("test_npu_", "", 1)

    # Strip numeric run suffix (e.g., _1, _2, ..., _19)
    name = re.sub(r"_\d+$", "", name)

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
    dataset_match = re.search(r"_(aime\d+|gpqa|random)$", name)
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
    """Parse a benchmark result file and extract the 4 key metrics."""
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

    return metrics


def parse_eval_log(filepath):
    """Parse an eval log file and extract the Score value.
    Looks for the "Overall report table" section with the Score column.
    Returns the score as a float, or None if not found.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception:
        return None

    # Find the "Overall report table" section
    overall_idx = content.rfind("Overall report table")
    if overall_idx == -1:
        return None

    # Find the data row after the header (contains │ Score │)
    tail = content[overall_idx:]
    # Match the data row: │ model │ dataset │ metric │ subset │ num │ score │ cat │
    # Pattern: │ ... │ ... │ ... │ ... │ digits │ float │ ... │
    match = re.search(r"│[^│]*│[^│]*│[^│]*│[^│]*│\s*\d+\s*│\s*([\d.]+)\s*│", tail)
    if match:
        return float(match.group(1))

    return None


def collect_eval_data():
    """Scan all date folders' eval/ subdirectories and collect accuracy scores.
    For the same test case on the same date, keep only the highest score.
    Returns a dict: {(test_case_name, date): max_score}
    """
    eval_data = {}
    metrics_dir = get_metrics_dir()

    if not os.path.isdir(metrics_dir):
        return eval_data

    for date_folder in sorted(os.listdir(metrics_dir)):
        date_path = os.path.join(metrics_dir, date_folder)
        if not os.path.isdir(date_path):
            continue

        eval_dir = os.path.join(date_path, "eval")
        if not os.path.isdir(eval_dir):
            continue

        for filename in os.listdir(eval_dir):
            if not filename.endswith(".log"):
                continue

            # Filename format: test_case_name__timestamp.log
            base = filename[:-4]  # strip .log
            if "__" not in base:
                continue

            # Split on first __ (test case name may contain underscores)
            # The timestamp is always YYYYMMDD_HHMMSS format
            match = re.match(r"(.+?)__(\d{8}_\d{6})$", base)
            if not match:
                continue

            test_case_name = match.group(1)
            filepath = os.path.join(eval_dir, filename)
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

    for date_folder in sorted(os.listdir(metrics_dir)):
        date_path = os.path.join(metrics_dir, date_folder)
        if not os.path.isdir(date_path):
            continue

        acc_dir = os.path.join(date_path, "accuracy")
        if not os.path.isdir(acc_dir):
            continue

        # Track best score per test case per date
        best_scores = {}

        for filename in os.listdir(acc_dir):
            if not filename.endswith(".log"):
                continue

            base = filename[:-4]
            if "__" not in base:
                continue

            match = re.match(r"(.+?)__(\d{8}_\d{6})$", base)
            if not match:
                continue

            test_case_name = match.group(1)
            filepath = os.path.join(acc_dir, filename)
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
            # No performance metrics
            labels["mean_ttft"] = None
            labels["mean_tpot"] = None
            labels["mean_e2e_latency"] = None
            labels["output_token_throughput"] = None
            results.append(labels)

    return results


def git_pull():
    """Clone or pull the latest data from Git repository.
    Throttled: only actually pulls if at least 60s since last pull.
    """
    if not GIT_PULL_ENABLED:
        return

    # Throttle: don't pull more than once per 60 seconds
    now = time.time()
    if now - git_pull._last_pull < 60:
        return
    git_pull._last_pull = now

    try:
        if os.path.isdir(os.path.join(GIT_LOCAL_CLONE, ".git")):
            # Update existing repo
            result = subprocess.run(
                ["git", "fetch", "origin", GIT_BRANCH, "--depth=1"],
                cwd=GIT_LOCAL_CLONE, capture_output=True, text=True, timeout=60
            )
            if result.returncode != 0:
                print(f"[git] fetch failed: {result.stderr.strip()}")
                return
            result = subprocess.run(
                ["git", "reset", "--hard", f"origin/{GIT_BRANCH}"],
                cwd=GIT_LOCAL_CLONE, capture_output=True, text=True, timeout=30
            )
            if result.returncode != 0:
                print(f"[git] reset failed: {result.stderr.strip()}")
                return
            print("[git] Data repo updated successfully")
        else:
            # Clone fresh
            print(f"[git] Cloning data repo: {GIT_REPO_URL}")
            os.makedirs(os.path.dirname(GIT_LOCAL_CLONE), exist_ok=True)
            result = subprocess.run(
                ["git", "clone", "--depth=1", "--branch", GIT_BRANCH,
                 GIT_REPO_URL, GIT_LOCAL_CLONE],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode != 0:
                print(f"[git] clone failed: {result.stderr.strip()}")
                return
            print("[git] Data repo cloned successfully")
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

    if not os.path.isdir(metrics_dir):
        print(f"Metrics directory not found: {metrics_dir}")
        return

    for date_folder in sorted(os.listdir(metrics_dir)):
        date_path = os.path.join(metrics_dir, date_folder)
        if not os.path.isdir(date_path):
            continue

        for filename in os.listdir(date_path):
            if not filename.endswith(".txt"):
                continue

            filepath = os.path.join(date_path, filename)
            parsed = parse_benchmark_file(filepath)
            if parsed is None:
                continue

            labels = parse_filename(filename)
            labels["date"] = date_folder

            label_values = [labels[k] for k in LABELS]

            mean_ttft.labels(*label_values).set(parsed["mean_ttft"])
            mean_tpot.labels(*label_values).set(parsed["mean_tpot"])
            mean_e2e_latency.labels(*label_values).set(parsed["mean_e2e_latency"])
            output_token_throughput.labels(*label_values).set(parsed["output_token_throughput"])

    print(f"Metrics updated at {time.strftime('%Y-%m-%d %H:%M:%S')}")


def update_loop(interval=300):
    """Periodically pull from Git and update metrics."""
    while True:
        git_pull()
        collect_metrics()
        time.sleep(interval)


if __name__ == "__main__":
    import threading

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
