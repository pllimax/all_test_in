# all_test_in_main

SGLang Ascend NPU 性能测试结果收集与可视化浏览项目。

## 1. 项目概览

| 文件 | 作用 |
|---|---|
| `upload_performance_result/metrics/sglang/collect_metrics.sh` | 在 CI 机器上收集测试结果（性能 `.txt` + 精度 `eval/*.log`），并自动 push 到 Git 数据仓 `pllimax/all_test_in.git` |
| `upload_performance_result/dashboard.py` | **自包含 Web Dashboard**，无需 Docker/Prometheus/Grafana，读取基准文件直接提供交互式网页浏览（默认 `http://localhost:8080`） |
| `upload_performance_result/prometheus_exporter.py` | 解析基准文件、抽取指标（TTFT/TPOT/吞吐等），供 dashboard 复用 |
| `upload_performance_result/dashboard_config.json.example` | 配置示例（数据源 repo、用例 YAML 位置等） |

**数据目录两种结构**（dashboard.py 自动兼容）：
- 旧结构：`metrics/sglang/{日期}/`，如 `20260718/`
- 新结构：`metrics/sglang/{分支}-{日期}-{run_id}-{attempt}/{workflow}/`，如 `pllimax-...-31297708320-1/Nightly_Test_NPU/`
- 性能文件命名：`{用例名}__{日期}.txt`；精度日志在 `{日期}/eval/` 下，命名 `{用例名}__{日期}.log`

## 2. 环境准备

```bash
# Python 3.8+（自带 http.server）
# 唯一第三方依赖：
pip install prometheus_client

# git（dashboard 启动时需要同步源码仓/数据仓）
git --version
```

> 本项目已自带 `metrics/sglang/` 历史数据，**不需要安装 SGLang、CANN、NPU 驱动**。收集测试结果才需要在 Ascend CI 机器上运行。

## 3. 启动 Dashboard

```bash
cd upload_performance_result

# 方式 A：纯本地浏览（不拉取远程数据，用仓库自带的 metrics 目录）
GIT_PULL_ENABLED=false python dashboard.py

# 方式 B：从 Git 数据仓拉取最新数据（默认行为）
# 首次启动会稀疏克隆 https://github.com/pllimax/all_test_in.git 的 metrics 目录到 .data_repo/
python dashboard.py
```

启动成功后输出类似：
```
Dashboard running at http://localhost:8080
```

浏览器打开 **http://localhost:8080** 即可浏览。

**Windows PowerShell 下设置环境变量**：
```powershell
cd upload_performance_result
$env:GIT_PULL_ENABLED="false"
python dashboard.py
```

## 4. 可选配置

### 4.1 数据源配置 `dashboard_config.json`

复制示例并修改：

```bash
copy dashboard_config.json.example dashboard_config.json
```

```json
{
  "sources": {
    "fulltest": {
      "repo_url": "https://github.com/Ascend/sglang.git",
      "yaml_config": ".github/workflows/full-test-npu.yml"
    },
    "nightly": {
      "repo_url": "https://github.com/sgl-project/sglang.git",
      "yaml_config": ".github/workflows/nightly-test-npu.yml"
    }
  },
  "branch_repo_map": {
    "fulltest": "https://github.com/Ascend/sglang.git",
    "nightly": "https://github.com/sgl-project/sglang.git"
  }
}
```

> 配置了 `repo_url` 后，dashboard 启动时会自动稀疏克隆到 `.testcases_repo/` 缓存（只需 `.github/workflows` 和 `test/registered/ascend|npu` 目录），用于把用例链接到 CI job 和解析基线。`branch_repo_map` 用于把分支模式数据目录解析到对应仓库。

### 4.2 常用环境变量

| 变量 | 默认值 | 说明 |
|---|---|---|
| `DASHBOARD_PORT` | `8080` | Web 端口 |
| `GIT_PULL_ENABLED` | `true` | 是否从 Git 同步指标数据（本地浏览建议 `false`） |
| `GIT_REPO_URL` | `pllimax/all_test_in.git` | 指标数据仓 |
| `GH_TOKEN` / `GITHUB_TOKEN` | 空 | GitHub API token，用于拉取 CI job 运行状态（限流 5000 次/时，不配置也能浏览数据） |
| `NOTES_GIT_PUSH` | `1` | 是否把用例备注定期 push 回 git 仓 |
| `SOURCE_SYNC_INTERVAL` | `7200` | 源码仓同步间隔（秒） |

## 5. 浏览使用

打开 http://localhost:8080 后可：
- **按用例对比**：Dashboard 把每个测试用例识别为 `模型 + 量化 + 并行度 + 输入长度 + 输出长度 + 请求速率 + 数据集`，并对同一用例跨日期展示指标（TTFT / TPOT / E2E 延迟 / 吞吐等）。
- **查看精度**：`eval/` 下的 `.log` 会展示对应用例的精度评测结果（AIME/GQA/MMMU 等）。
- **查看 CI 状态**：配置 `GH_TOKEN` 后可看到每次 run 的 job 列表与结论。
- **用例备注**：可给每个用例填写备注，本地存 `notes.json`。

页面 API 会标注当前数据来源是 `git克隆` 还是 `本地文件`。

## 6. 数据收集（可选，Ascend CI 机器上）

只在有 Ascend CI 测试产物的机器上执行，会收集并 push 到数据仓：

```bash
# 自动收集今天及前 3 天
./collect_metrics.sh

# 指定日期
./collect_metrics.sh 20260718 20260719

# 分支模式（按 CI 目录名 {分支}-{日期}-{run_id}-{attempt} 归类）
./collect_metrics.sh --branch pllimax
```

常用参数：`--src-base`（CI 产物根目录）、`--git-repo`（目标仓库，私有仓用带凭据地址）、`--branch`（按前缀过滤）。收集完成后本地浏览只需刷新 dashboard 或重新拉取数据。

## 7. 常见问题

| 现象 | 处理 |
|---|---|
| 8080 端口被占用 | `DASHBOARD_PORT=9090 python dashboard.py` |
| 首次启动慢 / 克隆失败 | 网络问题可设 `GIT_PULL_ENABLED=false` 纯本地浏览 |
| 不配置 `GH_TOKEN` | 不影响浏览数据，仅 CI job 状态/链接不可用 |
| 页面看不到最新数据 | 检查数据目录是否已通过 `collect_metrics.sh` push；本地浏览时确认数据在 `metrics/sglang/` 下且文件名格式正确 |
| 私有仓克隆需要认证 | 按仓库要求把 token 嵌入 URL 或配置 credential helper |
