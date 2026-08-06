"""
Self-contained performance dashboard - no Docker/Prometheus/Grafana required.
Reads benchmark files directly and serves an interactive web dashboard.
Each test case = model + quantization + parallelism + input_len + output_len + request_rate + dataset
Results are compared across dates for each exact test case.
"""
import os
import re
import json
import http.server
import socketserver
import subprocess
import sys
from prometheus_exporter import parse_filename, parse_benchmark_file, collect_eval_data, collect_accuracy_only_data, METRICS_DIR, GIT_PULL_ENABLED, get_metrics_dir, _iter_metrics_files

DASHBOARD_PORT = int(os.environ.get("DASHBOARD_PORT", "8080"))


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
            env_prefix = source_name.upper()

            # env var overrides
            repo_root = os.environ.get(f"{env_prefix}_REPO_ROOT", repo_root)
            yaml_rel = os.environ.get(f"{env_prefix}_YAML_CONFIG", yaml_rel)
            repo_url = os.environ.get(f"{env_prefix}_REPO_URL", repo_url)

            if repo_root and yaml_rel:
                yaml_abs = os.path.join(repo_root, yaml_rel)
                sources[source_name] = {
                    "repo_root": repo_root,
                    "yaml_config": yaml_abs,
                    "repo_url": repo_url,
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
            }

    # Validate and build derived structures
    valid_sources = {}
    for src_name, src_cfg in sources.items():
        repo_root = src_cfg["repo_root"]
        yaml_config = src_cfg["yaml_config"]
        if os.path.isfile(yaml_config):
            valid_sources[src_name] = src_cfg.copy()
        else:
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
        if repo_root and os.path.isdir(repo_root):
            for sub in ("ascend", "npu"):
                scripts_path = os.path.join(repo_root, "test", "registered", sub)
                if os.path.isdir(scripts_path) and scripts_path not in test_scripts_roots:
                    test_scripts_roots.append(scripts_path)
        yaml_configs.append(src_cfg["yaml_config"])

    return {
        "sources": valid_sources,
        "yaml_configs": yaml_configs,
        "test_scripts_roots": test_scripts_roots,
    }


_config = get_config_paths()
SOURCES = _config["sources"]
YAML_CONFIGS = _config["yaml_configs"]
TEST_SCRIPTS_ROOTS = _config["test_scripts_roots"]

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


# 基线缓存：启动时从两个仓刷新一次，请求期间复用
_baselines_cache = None


def collect_baselines(force=False):
    """Scan all test scripts and collect baseline values.
    Returns a dict: {test_case_name: {metric: value, ...}}
    每次启动 dashboard 时通过 force=True 从两个代码仓的测试脚本刷新，请求期间复用缓存。
    """
    global _baselines_cache
    if not force and _baselines_cache is not None:
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
    _baselines_cache = results
    return results

_nnodes_cache = {}

def _get_nnodes_from_script(yaml_name):
    """Read the test script for a given yaml_name and return the nnodes value.
    Returns 1 if not found or not configured."""
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
                    # Find all --nnodes occurrences and get the value on the next line
                    # For PD separation, use the first nnodes (prefill) or max of all
                    nnodes_vals = []
                    for m in re.finditer(r"--nnodes\s*\n\s*(\d+)", content):
                        nnodes_vals.append(int(m.group(1)))
                    if nnodes_vals:
                        # Use the minimum nnodes value (single node if any node is 1)
                        val = min(nnodes_vals)
                    else:
                        val = 1  # Not configured, default to 1
                    _nnodes_cache[yaml_name] = val
                    return val
                except Exception:
                    pass
                break
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
    seq_length = ""
    in_match = re.search(r'_in(\d+k?\d*|1024x1024|1080p)', yaml_name)
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
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/xlsx@0.18.5/dist/xlsx.full.min.js"></script>
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
.table-container { padding: 0 24px 20px; }
.table-container h3 { font-size: 14px; color: #8b949e; margin-bottom: 12px; }
table { width: 100%; border-collapse: collapse; background: #161b22; border: 1px solid #30363d; border-radius: 8px; overflow: hidden; }
th { background: #21262d; padding: 10px 12px; text-align: left; font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #30363d; cursor: pointer; white-space: normal; overflow: hidden; text-overflow: ellipsis; display: table-cell; -webkit-line-clamp: 2; line-clamp: 2; }
th:hover { color: #c9d1d9; }
td { padding: 8px 12px; font-size: 13px; border-bottom: 1px solid #21262d; white-space: nowrap; }
tr:hover { background: #1c2128; }
tr.selected { background: #1f3a5f !important; }
tr.selected:hover { background: #254070 !important; }
.no-data { text-align: center; padding: 40px; color: #8b949e; }
.testcase-id { font-family: 'Consolas', 'Courier New', monospace; font-size: 12px; color: #58a6ff; max-width: 400px; overflow: hidden; text-overflow: ellipsis; }
.status-pass { color: #7ee787; font-weight: 700; }
.status-fail { color: #ff7b72; font-weight: 700; }
.status-none { color: #ff7b72; font-weight: 700; }
.baseline-val { font-size: 11px; color: #8b949e; }
.metric-fail { color: #ff7b72; font-weight: 700; }
.baseline-col { font-size: 11px; color: #8b949e; max-width: 200px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
.chart-row td { padding: 0; }
.tc-charts { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; padding: 12px; background: #0d1117; }
.tc-chart-box { background: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 8px; }
.tc-chart-box h4 { font-size: 12px; color: #8b949e; margin: 0 0 4px 0; }
.tc-chart-box canvas { max-height: 200px; }
.expand-icon { display: inline-block; width: 14px; font-size: 10px; transition: transform 0.2s; }
.col-uniform { width: 90px; }
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
  <button class="btn btn-reset" onclick="resetFilters()">重置筛选</button>
  <button class="btn" onclick="exportToExcel()">导出Excel</button>
</div>
<div class="table-container">
  <h3>详细数据 <span style="font-weight:normal;font-size:12px;color:#8b949e" id="tableCount"></span></h3>
  <table id="dataTable">
    <thead>
      <tr>
        <th>模型</th>
        <th>测试用例ID</th>
        <th>日期</th>
        <th>来源</th>
        <th>状态</th>
        <th>基线</th>
        <th class="col-uniform">组网</th>
        <th class="col-uniform">卡数</th>
        <th class="col-uniform">序列长度</th>
        <th class="col-uniform">prefix</th>
        <th class="col-uniform">数据集</th>
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

<script>
let allData = [];
let charts = {};

function buildTestCaseId(d) {
  return d.yaml_name || '';
}

function buildShortLabel(d) {
  const parts = [];
  if (d.model) parts.push(d.model);
  if (d.quantization) parts.push(d.quantization);
  if (d.parallelism) parts.push(d.parallelism);
  if (d.input_len) parts.push('in'+d.input_len);
  if (d.output_len) parts.push('out'+d.output_len);
  if (d.request_rate) parts.push(d.request_rate);
  if (d.dataset) parts.push(d.dataset);
  if (d.prefix) parts.push(d.prefix);
  return parts.join('_');
}

function initCharts() {
  // Charts are created dynamically when a test case row is expanded
}

function showTestCaseChart(tcId, label) {
  const items = allData.filter(d => d._id === tcId);
  items.sort((a, b) => a.date.localeCompare(b.date));
  const dates = items.map(d => d.date);

  const chartRow = document.getElementById('chart_' + tcId.replace(/[^a-zA-Z0-9]/g, '_'));
  if (!chartRow) return;

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

async function loadData() {
  const resp = await fetch('/api/data');
  allData = await resp.json();
  allData.forEach(d => { d._id = buildTestCaseId(d); d._label = buildShortLabel(d); });
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

function computeStatus(d) {
  const b = d.baselines || {};
  const hasPerf = d.mean_ttft != null;
  const hasEval = d.eval_score != null;
  const hasBaseline = Object.keys(b).length > 0;
  if (!hasBaseline) return hasPerf || hasEval ? '' : 'FAILED(无结果)';
  if (!hasPerf && !hasEval) return 'FAILED(无结果)';
  // TPOT: baseline < 50 → +1ms absolute; baseline >= 50 → +2% relative
  if (b.mean_tpot != null) {
    if (d.mean_tpot == null) return 'FAILED';
    const tpotLimit = b.mean_tpot < TPOT_THRESHOLD
      ? b.mean_tpot + TPOT_TOLERANCE_LOW
      : b.mean_tpot * TPOT_TOLERANCE_HIGH;
    if (d.mean_tpot > tpotLimit) return 'FAILED';
  }
  // TTFT: +2% tolerance
  if (b.mean_ttft != null) {
    if (d.mean_ttft == null) return 'FAILED';
    if (d.mean_ttft > b.mean_ttft * TTFT_TOLERANCE) return 'FAILED';
  }
  // E2E Latency: +2% tolerance
  if (b.mean_e2e_latency != null) {
    if (d.mean_e2e_latency == null) return 'FAILED';
    if (d.mean_e2e_latency > b.mean_e2e_latency * E2E_TOLERANCE) return 'FAILED';
  }
  // Output Token Throughput: -2% tolerance
  if (b.output_token_throughput != null) {
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

function getTestCaseStatus(items) {
  if (items.length === 0) return 'FAILED(无结果)';
  // 取时间段内最新一次有结果的执行；全部无结果时取最后一项
  const withData = items.filter(d => hasData(d));
  const latest = withData.length > 0 ? withData[withData.length - 1] : items[items.length - 1];
  return computeStatus(latest);
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
      if (statusFilter.includes('PASS') && status === 'PASS') keepIds.add(id);
      if (statusFilter.includes('FAILED') && (status === 'FAILED' || status === 'FAILED(无结果)')) keepIds.add(id);
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
  onFilterChange();
}

function updateTable(data) {
  const tbody = document.getElementById('tableBody');
  if (data.length === 0) {
    document.getElementById('tableCount').textContent = '(0 条)';
    tbody.innerHTML = '<tr><td colspan="27" class="no-data">无匹配数据</td></tr>';
    return;
  }

  // Group by test case, sort by date within each group
  const groups = {};
  data.forEach(d => {
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

  function fmtBaseline(b) {
    const parts = [];
    if (b.mean_ttft != null) parts.push(`TTFT≤${b.mean_ttft}`);
    if (b.mean_tpot != null) parts.push(`TPOT≤${b.mean_tpot}`);
    if (b.mean_e2e_latency != null) parts.push(`E2E时间≤${b.mean_e2e_latency}`);
    if (b.output_token_throughput != null) parts.push(`输出吞吐≥${b.output_token_throughput}`);
    if (b.eval_score != null) parts.push(`精度≥${b.eval_score}`);
    return parts.length > 0 ? parts.join(', ') : '--';
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
      const statusCls = status === 'PASS' ? 'status-pass' : status === 'FAILED' ? 'status-fail' : 'status-none';
      const b = d.baselines || {};
      const bl = (key, sym) => b[key] != null ? `<br><span class="baseline-val">${sym}${b[key]}</span>` : '';
      const expandIcon = isLatest && items.length > 1
        ? `<span class="expand-icon" style="cursor:pointer;color:#58a6ff;margin-right:4px;" title="点击展开历史">▶</span>`
        : '';
      const rowStyle = isLatest ? '' : 'style="display:none"';
      if (isLatest) visibleCount++;
      const modelDisplay = isLatest && groupShowModel[gIdx] ? d.model : '';
      rows += `<tr class="data-row" data-tc="${safeId}" ${rowStyle}>
        <td>${modelDisplay}</td>
        <td><span class="testcase-id" title="${tcId}">${expandIcon}${tcId}</span></td>
        <td>${d.date}</td>
        <td>${d.source || '--'}</td>
        <td><span class="${statusCls}">${status}</span></td>
        <td><span class="baseline-col" title="${fmtBaseline(b)}">${fmtBaseline(b)}</span></td>
        <td class="col-uniform">${d.topology || '--'}</td>
        <td class="col-uniform">${d.card_count || '--'}</td>
        <td class="col-uniform">${d.seq_length || '--'}</td>
        <td class="col-uniform">${(d.prefix || '').replace('prefix', '') || '0'}</td>
        <td>${d.dataset || '--'}</td>
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
    rows += `<tr class="chart-row" id="chart_${safeId}" data-tc="${safeId}" style="display:none"><td colspan="27"></td></tr>`;
  });
  document.getElementById('tableCount').textContent = `(${visibleCount} 条)`;
  tbody.innerHTML = rows;
}

// Click row to expand/collapse history and charts
document.getElementById('tableBody').addEventListener('click', function(e) {
  const tr = e.target.closest('tr');
  if (!tr || tr.querySelector('.no-data') || tr.classList.contains('chart-row')) return;
  const tcId = tr.getAttribute('data-tc');
  if (!tcId) return;

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

    // Expand: show all rows for this test case, highlight, show chart
    allRows.forEach(r => { r.style.display = ''; r.classList.add('selected'); });
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
        const keep = (statusVals.includes('PASS') && status === 'PASS') ||
                     (statusVals.includes('FAILED') && (status === 'FAILED' || status === 'FAILED(无结果)'));
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
      '模型', '测试用例ID', '日期', '来源', '状态', '基线',
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
      const blParts = [];
      if (b.mean_ttft != null) blParts.push('TTFT≤' + b.mean_ttft);
      if (b.mean_tpot != null) blParts.push('TPOT≤' + b.mean_tpot);
      if (b.mean_e2e_latency != null) blParts.push('E2E≤' + b.mean_e2e_latency);
      if (b.output_token_throughput != null) blParts.push('吞吐≥' + b.output_token_throughput);
      if (b.eval_score != null) blParts.push('精度≥' + b.eval_score);
      return [
        d.model || '', d._id || '', d.date || '', d.source || '', computeStatus(d),
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
  setInterval(loadData, 300000);
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


def collect_expected_test_cases():
    """Parse YAML workflow configs and collect all expected test case IDs.
    Only extracts names from matrix.test_config entries (structure-aware parsing).
    Returns a dict: {test_case_id: {"labels": labels, "source": "fulltest"|"nightly"|...}}
    """
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
                    continue

                # Only match - name: entries that are indented deeper than test_config
                if current_indent > test_config_indent:
                    name_match = re.match(r'- name:\s*(\S+)', stripped)
                    if name_match:
                        name = name_match.group(1)
                        labels = parse_yaml_test_name(name)
                        model = labels.get("model", "")
                        if " " in model or not model:
                            continue
                        # Skip excluded test cases
                        if name in EXCLUDED_TEST_CASES:
                            continue
                        # Use YAML name directly as test case ID
                        if name not in expected:
                            expected[name] = {"labels": labels, "source": source, "yaml_name": name}
                        else:
                            # 同一用例可能同时存在于多个 workflow（如 fulltest + nightly），合并 source
                            existing = expected[name]
                            if source not in existing["source"].split(","):
                                existing["source"] = existing["source"] + "," + source

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
    """拆分 date_label 为 (date, branch)。
    新格式: {branch_label}-{create_date}-{run_id}/{workflow}
            → (create_date, branch_label)   # branch 仅取日期之前的字段
    旧格式: YYYYMMDD → (YYYYMMDD, "")
    """
    if not date_label:
        return date_label, ""
    m = re.match(r"^(.+)-(\d{8})-(\d+)/(.+)$", date_label)
    if m:
        return m.group(2), m.group(1)
    return date_label, ""


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
        date_part, branch_part = split_date_label(date_folder)
        labels["date"] = date_part
        labels["branch"] = branch_part
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
        date_part, branch_part = split_date_label(item.get("date", ""))
        item["date"] = date_part
        item["branch"] = branch_part
    results.extend(accuracy_data)

    # Append accuracy-only entries for eval/ scores not matched to benchmark results
    # (e.g., accuracy-only tests like qwen3_vl_8b_thinking_1p_mmmu whose results
    #  are in eval/ but have no matching .txt benchmark file)
    for (test_case_name, date), score in eval_data.items():
        if (test_case_name, date) not in consumed_eval_keys:
            labels = parse_filename(test_case_name + ".txt")
            date_part, branch_part = split_date_label(date)
            labels["date"] = date_part
            labels["branch"] = branch_part
            labels["yaml_name"] = filename_to_yaml_name(test_case_name)
            if labels["yaml_name"] not in expected_tc_ids:
                alt = "test_npu_" + labels["yaml_name"]
                if alt in expected_tc_ids:
                    labels["yaml_name"] = alt
            labels["eval_score"] = score
            labels["mean_ttft"] = None
            labels["mean_tpot"] = None
            labels["mean_e2e_latency"] = None
            labels["output_token_throughput"] = None
            labels["p90_ttft"] = None
            labels["p90_tpot"] = None
            labels["total_token_throughput"] = None
            labels["total_requests"] = None
            labels["max_concurrency"] = None
            labels["system_concurrency"] = None
            labels["request_throughput"] = None
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
            filtered.append(r)

    # Add placeholder entries for expected test cases that have no data
    # 为每个出现的日期补充占位符条目：该日期无结果的用例也显示（FAILED(无结果)）

    # Collect all dates that appear in results
    all_dates = sorted(set(r.get("date", "") for r in filtered if r.get("date")))
    if not all_dates:
        # No data at all: use a placeholder date so expected cases still render
        all_dates = [""]

    # Existing (yaml_name, date) pairs to avoid duplicating real results
    existing_pairs = set((r.get("yaml_name", ""), r.get("date", "")) for r in filtered)

    for date in all_dates:
        for yaml_name, info in expected.items():
            if (yaml_name, date) in existing_pairs:
                continue
            labels = info["labels"]
            # Derive baseline key from yaml_name: prefix with "test_npu_" if not already
            if yaml_name.startswith("test_npu_"):
                baseline_key = yaml_name
            else:
                baseline_key = "test_npu_" + yaml_name
            placeholder_baselines = baselines.get(baseline_key, {})
            date_part, branch_part = split_date_label(date)
            placeholder = {
                "model": labels.get("model", ""),
                "quantization": labels.get("quantization", ""),
                "parallelism": labels.get("parallelism", ""),
                "input_len": labels.get("input_len", ""),
                "output_len": labels.get("output_len", ""),
                "request_rate": labels.get("request_rate", ""),
                "dataset": labels.get("dataset", ""),
                "prefix": labels.get("prefix", ""),
                "date": date_part,
                "branch": branch_part,
                "yaml_name": yaml_name,
                "mean_ttft": None,
                "mean_tpot": None,
                "mean_e2e_latency": None,
                "output_token_throughput": None,
                "p90_ttft": None,
                "p90_tpot": None,
                "total_token_throughput": None,
                "total_requests": None,
                "max_concurrency": None,
                "system_concurrency": None,
                "request_throughput": None,
                "eval_score": None,
                "baselines": placeholder_baselines,
                "source": info["source"],
            }
            filtered.append(placeholder)

    # Attach topology info to all items
    for item in filtered:
        yaml_name = item.get("yaml_name", "")
        topology, card_count, seq_length = compute_topology_info(yaml_name)
        item["topology"] = topology
        item["card_count"] = card_count
        item["seq_length"] = seq_length

    return filtered


class DashboardHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/" or self.path == "/index.html":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode("utf-8"))
        elif self.path == "/api/data":
            data = collect_all_data()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(json.dumps(data, ensure_ascii=False).encode("utf-8"))
        elif self.path == "/api/status":
            source = "本地文件"
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(json.dumps({"source": source, "git_enabled": GIT_PULL_ENABLED}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def sync_repos():
    """Force-sync (git pull) all configured source repos on startup."""
    for src_name, src_cfg in SOURCES.items():
        repo_root = src_cfg.get("repo_root", "")
        repo_url = src_cfg.get("repo_url", "")
        if not repo_root:
            print(f"[sync] {src_name}: no repo_root configured, skipping")
            continue

        if not os.path.isdir(repo_root):
            # Repo doesn't exist locally - try to clone
            if repo_url:
                parent_dir = os.path.dirname(repo_root)
                os.makedirs(parent_dir, exist_ok=True)
                print(f"[sync] {src_name}: cloning {repo_url} -> {repo_root}")
                try:
                    subprocess.run(
                        ["git", "clone", repo_url, repo_root],
                        capture_output=True, text=True, timeout=120,
                        cwd=parent_dir,
                    )
                    print(f"[sync] {src_name}: clone OK")
                except Exception as e:
                    print(f"[sync] {src_name}: clone failed: {e}")
            else:
                print(f"[sync] {src_name}: repo not found at {repo_root} and no repo_url to clone")
            continue

        # Repo exists - force pull latest
        print(f"[sync] {src_name}: pulling latest from {repo_root}")
        try:
            # Reset any local changes and pull
            subprocess.run(
                ["git", "reset", "--hard", "HEAD"],
                capture_output=True, text=True, timeout=30,
                cwd=repo_root,
            )
            result = subprocess.run(
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
        except subprocess.TimeoutExpired:
            print(f"[sync] {src_name}: pull timed out")
        except Exception as e:
            print(f"[sync] {src_name}: pull error: {e}")


def start_dashboard():
    print("=" * 60)
    print("[startup] Syncing test case repos...")
    sync_repos()
    # 启动时从两个代码仓的测试脚本刷新基线缓存
    print("[startup] Refreshing baselines from test scripts...")
    collect_baselines(force=True)
    print("=" * 60)
    server = socketserver.ThreadingTCPServer(("0.0.0.0", DASHBOARD_PORT), DashboardHandler)
    print(f"Dashboard running at http://localhost:{DASHBOARD_PORT}")
    server.serve_forever()


if __name__ == "__main__":
    start_dashboard()
