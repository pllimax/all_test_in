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
from prometheus_exporter import parse_filename, parse_benchmark_file, collect_eval_data, collect_accuracy_only_data, METRICS_DIR

DASHBOARD_PORT = int(os.environ.get("DASHBOARD_PORT", "8080"))

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>SGLang Benchmark 性能分析平台</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
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
.summary { display: grid; grid-template-columns: repeat(5, 1fr); gap: 16px; padding: 20px 24px; }
.summary-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 16px; text-align: center; }
.summary-card .label { font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 8px; }
.summary-card .value { font-size: 28px; font-weight: 700; }
.ttft .value { color: #f78166; }
.tpot .value { color: #d2a8ff; }
.e2e .value { color: #ff7b72; }
.throughput .value { color: #7ee787; }
.eval-score .value { color: #e3b341; }
.charts { padding: 0 24px 20px; }
.chart-section { background: #161b22; border: 1px solid #30363d; border-radius: 8px; margin-bottom: 12px; overflow: hidden; }
.chart-header { display: flex; align-items: center; gap: 8px; padding: 12px 16px; cursor: pointer; user-select: none; }
.chart-header:hover { background: #1c2128; }
.chart-header .arrow { font-size: 12px; color: #8b949e; transition: transform 0.2s; display: inline-block; width: 16px; }
.chart-header .arrow.open { transform: rotate(90deg); }
.chart-header h3 { font-size: 14px; color: #8b949e; margin: 0; }
.chart-body { display: none; padding: 0 16px 16px; }
.chart-body.open { display: block; }
.chart-body canvas { max-height: 350px; }
.table-container { padding: 0 24px 20px; }
.table-container h3 { font-size: 14px; color: #8b949e; margin-bottom: 12px; }
table { width: 100%; border-collapse: collapse; background: #161b22; border: 1px solid #30363d; border-radius: 8px; overflow: hidden; }
th { background: #21262d; padding: 10px 12px; text-align: left; font-size: 12px; color: #8b949e; text-transform: uppercase; letter-spacing: 0.5px; border-bottom: 1px solid #30363d; cursor: pointer; white-space: nowrap; }
th:hover { color: #c9d1d9; }
td { padding: 8px 12px; font-size: 13px; border-bottom: 1px solid #21262d; white-space: nowrap; }
tr:hover { background: #1c2128; }
tr.selected { background: #1f3a5f !important; }
tr.selected:hover { background: #254070 !important; }
.no-data { text-align: center; padding: 40px; color: #8b949e; }
.testcase-id { font-family: 'Consolas', 'Courier New', monospace; font-size: 12px; color: #58a6ff; max-width: 400px; overflow: hidden; text-overflow: ellipsis; }
.diff-up { color: #ff7b72; }
.diff-down { color: #7ee787; }
.diff-same { color: #8b949e; }
</style>
</head>
<body>
<div class="header">
  <h1>SGLang Benchmark 性能分析平台</h1>
  <div class="info" id="updateTime"></div>
</div>
<div class="filters">
  <div class="filter-group">
    <label>模型</label>
    <select id="modelFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>量化</label>
    <select id="quantFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>并行策略</label>
    <select id="paraFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>输入长度</label>
    <select id="inFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>输出长度</label>
    <select id="outFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>请求速率</label>
    <select id="rrFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>数据集</label>
    <select id="dsFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>Prefix</label>
    <select id="prefixFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <div class="filter-group">
    <label>日期</label>
    <select id="dateFilter" multiple onchange="onFilterChange()"></select>
  </div>
  <button class="btn btn-reset" onclick="resetFilters()">重置筛选</button>
</div>
<div class="summary">
  <div class="summary-card ttft">
    <div class="label">Mean TTFT (ms)</div>
    <div class="value" id="avgTTFT">--</div>
  </div>
  <div class="summary-card tpot">
    <div class="label">Mean TPOT (ms)</div>
    <div class="value" id="avgTPOT">--</div>
  </div>
  <div class="summary-card e2e">
    <div class="label">Mean E2E Latency (ms)</div>
    <div class="value" id="avgE2E">--</div>
  </div>
  <div class="summary-card throughput">
    <div class="label">Output Token Throughput (tok/s)</div>
    <div class="value" id="avgThroughput">--</div>
  </div>
  <div class="summary-card eval-score">
    <div class="label">Accuracy Score</div>
    <div class="value" id="avgEvalScore">--</div>
  </div>
</div>
<div class="charts">
  <div class="chart-section">
    <div class="chart-header" onclick="toggleChart('chartTTFT')">
      <span class="arrow" id="arrowTTFT">▶</span>
      <h3>Mean TTFT (ms) - 按日期对比</h3>
    </div>
    <div class="chart-body" id="bodyTTFT">
      <canvas id="chartTTFT"></canvas>
    </div>
  </div>
  <div class="chart-section">
    <div class="chart-header" onclick="toggleChart('chartTPOT')">
      <span class="arrow" id="arrowTPOT">▶</span>
      <h3>Mean TPOT (ms) - 按日期对比</h3>
    </div>
    <div class="chart-body" id="bodyTPOT">
      <canvas id="chartTPOT"></canvas>
    </div>
  </div>
  <div class="chart-section">
    <div class="chart-header" onclick="toggleChart('chartE2E')">
      <span class="arrow" id="arrowE2E">▶</span>
      <h3>Mean E2E Latency (ms) - 按日期对比</h3>
    </div>
    <div class="chart-body" id="bodyE2E">
      <canvas id="chartE2E"></canvas>
    </div>
  </div>
  <div class="chart-section">
    <div class="chart-header" onclick="toggleChart('chartThroughput')">
      <span class="arrow" id="arrowThroughput">▶</span>
      <h3>Output Token Throughput (tok/s) - 按日期对比</h3>
    </div>
    <div class="chart-body" id="bodyThroughput">
      <canvas id="chartThroughput"></canvas>
    </div>
  </div>
  <div class="chart-section">
    <div class="chart-header" onclick="toggleChart('chartEvalScore')">
      <span class="arrow" id="arrowEvalScore">▶</span>
      <h3>Accuracy Score - 按日期对比</h3>
    </div>
    <div class="chart-body" id="bodyEvalScore">
      <canvas id="chartEvalScore"></canvas>
    </div>
  </div>
</div>
<div class="table-container">
  <h3>详细数据 <span style="font-weight:normal;font-size:12px;color:#8b949e" id="tableCount"></span></h3>
  <table id="dataTable">
    <thead>
      <tr>
        <th>测试用例ID</th>
        <th>日期</th>
        <th>模型</th>
        <th>量化</th>
        <th>并行</th>
        <th>输入长度</th>
        <th>输出长度</th>
        <th>请求速率</th>
        <th>数据集</th>
        <th>Prefix</th>
        <th>TTFT (ms)</th>
        <th>TPOT (ms)</th>
        <th>E2E (ms)</th>
        <th>Throughput (tok/s)</th>
        <th>Accuracy Score</th>
      </tr>
    </thead>
    <tbody id="tableBody"></tbody>
  </table>
</div>

<script>
let allData = [];
let charts = {};
const COLORS = ['#f78166','#58a6ff','#d2a8ff','#7ee787','#f0883e','#db6d8c','#56d4dd','#e3b341','#b392f0','#79c0ff','#ffa198','#a5d6ff'];

function buildTestCaseId(d) {
  return [d.model, d.quantization, d.parallelism, d.input_len, d.output_len, d.request_rate, d.dataset, d.prefix]
    .filter(v => v).join('|') || d.model;
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

function toggleChart(chartId) {
  const body = document.getElementById('body' + chartId.replace('chart', ''));
  const arrow = document.getElementById('arrow' + chartId.replace('chart', ''));
  body.classList.toggle('open');
  arrow.classList.toggle('open');
  if (body.classList.contains('open')) {
    arrow.textContent = '▼';
  } else {
    arrow.textContent = '▶';
  }
}

function initCharts() {
  const commonOpts = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'bottom', labels: { color: '#8b949e', font: { size: 10 }, boxWidth: 12, padding: 8 } }
    },
    scales: {
      x: { ticks: { color: '#8b949e', font: { size: 11 } }, grid: { color: '#21262d' } },
      y: { ticks: { color: '#8b949e' }, grid: { color: '#21262d' } }
    },
    interaction: { mode: 'index', intersect: false }
  };
  const chartIds = { ttft: 'chartTTFT', tpot: 'chartTPOT', e2e: 'chartE2E', throughput: 'chartThroughput', evalscore: 'chartEvalScore' };
  Object.entries(chartIds).forEach(([k, id]) => {
    charts[k] = new Chart(document.getElementById(id), {
      type: 'line', data: { labels: [], datasets: [] }, options: commonOpts
    });
  });
}

async function loadData() {
  const resp = await fetch('/api/data');
  allData = await resp.json();
  allData.forEach(d => { d._id = buildTestCaseId(d); d._label = buildShortLabel(d); });
  populateFilters();
  onFilterChange();
  document.getElementById('updateTime').textContent = '更新: ' + new Date().toLocaleTimeString();
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
  const keys = ['model','quantization','parallelism','input_len','output_len','request_rate','dataset','prefix','date'];
  const ids = ['modelFilter','quantFilter','paraFilter','inFilter','outFilter','rrFilter','dsFilter','prefixFilter','dateFilter'];
  keys.forEach((k, i) => {
    let vals;
    if (k === 'prefix') {
      // Include empty string as "无" option for non-prefix cases
      vals = [...new Set(allData.map(d => d[k] || '无'))].sort();
    } else {
      vals = [...new Set(allData.map(d => d[k]).filter(Boolean))].sort();
    }
    populateMultiSelect(ids[i], vals, '全部');
  });
}

function getSelectedValues(id) {
  const sel = document.getElementById(id);
  const vals = [...sel.selectedOptions].map(o => o.value);
  if (vals.includes('__all__') || vals.length === 0) return null;
  return vals;
}

function onFilterChange() {
  const filters = {
    model: getSelectedValues('modelFilter'),
    quantization: getSelectedValues('quantFilter'),
    parallelism: getSelectedValues('paraFilter'),
    input_len: getSelectedValues('inFilter'),
    output_len: getSelectedValues('outFilter'),
    request_rate: getSelectedValues('rrFilter'),
    dataset: getSelectedValues('dsFilter'),
    prefix: getSelectedValues('prefixFilter'),
    date: getSelectedValues('dateFilter'),
  };

  let filtered = allData;
  Object.entries(filters).forEach(([key, vals]) => {
    if (vals !== null) {
      if (key === 'prefix') {
        filtered = filtered.filter(d => vals.includes(d[key] || '无'));
      } else {
        filtered = filtered.filter(d => vals.includes(d[key]));
      }
    }
  });

  updateSummary(filtered);
  updateCharts(filtered);
  updateTable(filtered);
}

function resetFilters() {
  ['modelFilter','quantFilter','paraFilter','inFilter','outFilter','rrFilter','dsFilter','prefixFilter','dateFilter'].forEach(id => {
    const sel = document.getElementById(id);
    [...sel.options].forEach(o => o.selected = o.value === '__all__');
  });
  onFilterChange();
}

function updateSummary(data) {
  const avg = (arr, key) => {
    const vals = arr.map(d => d[key]).filter(v => v != null);
    return vals.length ? (vals.reduce((s, v) => s + v, 0) / vals.length).toFixed(4) : '--';
  };
  document.getElementById('avgTTFT').textContent = avg(data, 'mean_ttft');
  document.getElementById('avgTPOT').textContent = avg(data, 'mean_tpot');
  document.getElementById('avgE2E').textContent = avg(data, 'mean_e2e_latency');
  document.getElementById('avgThroughput').textContent = avg(data, 'output_token_throughput');
  document.getElementById('avgEvalScore').textContent = avg(data, 'eval_score');
}

function updateCharts(data) {
  // Group by test case ID, then sort each group by date
  const groups = {};
  data.forEach(d => {
    if (!groups[d._id]) groups[d._id] = [];
    groups[d._id].push(d);
  });

  // Sort each group by date
  Object.values(groups).forEach(g => g.sort((a, b) => a.date.localeCompare(b.date)));

  // Collect all unique dates across all groups for x-axis
  const allDates = [...new Set(data.map(d => d.date))].sort();

  const metrics = [
    { key: 'mean_ttft', chart: 'ttft' },
    { key: 'mean_tpot', chart: 'tpot' },
    { key: 'mean_e2e_latency', chart: 'e2e' },
    { key: 'output_token_throughput', chart: 'throughput' },
    { key: 'eval_score', chart: 'evalscore' },
  ];

  metrics.forEach(({ key, chart }) => {
    const datasets = [];
    let colorIdx = 0;
    Object.entries(groups).forEach(([tcId, items]) => {
      const label = items[0]._label;
      const dateMap = {};
      items.forEach(d => { dateMap[d.date] = d[key]; });
      const dataPoints = allDates.map(date => dateMap[date] ?? null);
      datasets.push({
        label: label,
        data: dataPoints,
        borderColor: COLORS[colorIdx % COLORS.length],
        backgroundColor: COLORS[colorIdx % COLORS.length] + '30',
        borderWidth: 2,
        pointRadius: 4,
        pointHoverRadius: 6,
        tension: 0.1,
        spanGaps: false,
      });
      colorIdx++;
    });
    charts[chart].data.labels = allDates;
    charts[chart].data.datasets = datasets;
    charts[chart].update();
  });
}

function updateTable(data) {
  const tbody = document.getElementById('tableBody');
  document.getElementById('tableCount').textContent = '(' + data.length + ' 条)';
  if (data.length === 0) {
    tbody.innerHTML = '<tr><td colspan="15" class="no-data">无匹配数据</td></tr>';
    return;
  }

  // Group by test case, sort by date within each group
  const groups = {};
  data.forEach(d => {
    if (!groups[d._id]) groups[d._id] = [];
    groups[d._id].push(d);
  });
  Object.values(groups).forEach(g => g.sort((a, b) => a.date.localeCompare(b.date)));

  // Sort groups by test case ID
  const sortedGroups = Object.entries(groups).sort((a, b) => a[0].localeCompare(b[0]));

  // Calculate diffs for consecutive dates within same test case
  const diffCache = {};
  Object.values(groups).forEach(items => {
    for (let i = 1; i < items.length; i++) {
      const prev = items[i-1], curr = items[i];
      const key = curr._id + '|' + curr.date;
      diffCache[key] = {};
      ['mean_ttft','mean_tpot','mean_e2e_latency','output_token_throughput'].forEach(k => {
        if (prev[k] && curr[k]) {
          diffCache[key][k] = ((curr[k] - prev[k]) / prev[k] * 100).toFixed(1);
        }
      });
    }
  });

  function diffSpan(curr, prev, key) {
    if (!prev || curr[key] == null || prev[key] == null) return '';
    const pct = ((curr[key] - prev[key]) / prev[key] * 100).toFixed(1);
    const cls = pct > 0 ? (key === 'output_token_throughput' ? 'diff-up' : 'diff-down')
              : pct < 0 ? (key === 'output_token_throughput' ? 'diff-down' : 'diff-up')
              : 'diff-same';
    const arrow = pct > 0 ? '↑' : pct < 0 ? '↓' : '→';
    return ` <span class="${cls}">${arrow}${Math.abs(pct)}%</span>`;
  }

  function fmtVal(v, digits) {
    return v != null ? v.toFixed(digits) : '--';
  }

  let rows = '';
  sortedGroups.forEach(([tcId, items]) => {
    items.forEach((d, i) => {
      const prev = i > 0 ? items[i-1] : null;
      rows += `<tr>
        <td><span class="testcase-id" title="${tcId}">${tcId}</span></td>
        <td>${d.date}</td><td>${d.model}</td><td>${d.quantization}</td><td>${d.parallelism}</td>
        <td>${d.input_len || '--'}</td><td>${d.output_len || '--'}</td><td>${d.request_rate || '--'}</td><td>${d.dataset || '--'}</td><td>${d.prefix || '--'}</td>
        <td>${fmtVal(d.mean_ttft, 2)}${diffSpan(d, prev, 'mean_ttft')}</td>
        <td>${fmtVal(d.mean_tpot, 2)}${diffSpan(d, prev, 'mean_tpot')}</td>
        <td>${fmtVal(d.mean_e2e_latency, 2)}${diffSpan(d, prev, 'mean_e2e_latency')}</td>
        <td>${fmtVal(d.output_token_throughput, 2)}${diffSpan(d, prev, 'output_token_throughput')}</td>
        <td>${d.eval_score != null ? d.eval_score.toFixed(4) : '--'}</td>
      </tr>`;
    });
  });
  tbody.innerHTML = rows;
}

// Click-to-select rows for comparison
document.getElementById('tableBody').addEventListener('click', function(e) {
  const tr = e.target.closest('tr');
  if (!tr || tr.querySelector('.no-data')) return;
  tr.classList.toggle('selected');
});

document.addEventListener('DOMContentLoaded', () => {
  initCharts();
  loadData();
  setInterval(loadData, 300000);
});
</script>
</body>
</html>"""


def collect_all_data():
    """Collect all benchmark data into a list of dicts."""
    results = []
    if not os.path.isdir(METRICS_DIR):
        return results

    # Collect eval scores: {(test_case_name, date): max_score}
    eval_data = collect_eval_data()

    for date_folder in sorted(os.listdir(METRICS_DIR)):
        date_path = os.path.join(METRICS_DIR, date_folder)
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
            labels.update(parsed)

            # Attach eval score: key is (test_case_name without .txt, date)
            test_case_name = filename[:-4]  # strip .txt
            eval_key = (test_case_name, date_folder)
            labels["eval_score"] = eval_data.get(eval_key)

            results.append(labels)

    # Append accuracy-only test results (no performance metrics)
    accuracy_data = collect_accuracy_only_data()
    results.extend(accuracy_data)

    return results


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
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


def start_dashboard():
    server = socketserver.ThreadingTCPServer(("0.0.0.0", DASHBOARD_PORT), DashboardHandler)
    print(f"Dashboard running at http://localhost:{DASHBOARD_PORT}")
    server.serve_forever()


if __name__ == "__main__":
    start_dashboard()
