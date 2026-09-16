# NPU CI 执行监控（2026-09-15）
**生成时间**: 2026-09-16 11:01
**分析 Run 数**: 1

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 8 个 | 失败 3 个 | 成功 Job 平均耗时 23.7min
- **Run 执行情况**: 成功 0 个 | 失败 1 个 | 成功 Run 平均耗时 0.0min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-1-npu-a3 (0) | 38.0min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627354713) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353944) |
| multimodal-gen-test-4-npu-a3 (1) | 28.2min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627354911) |
| base-b-test-1-npu-a3 / run (0) | 25.3min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353984) |
| base-a-test-1-npu-a2 / run (0) | 22.9min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353941) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353968) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627355180) |
| base-b-test-4-npu-a3 / run (0) | 13.9min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353953) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-8-npu-a3 / run (0) | 4.1min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353844) |
| base-b-test-2-npu-a3 / run (0) | 4.0min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353965) |
| base-b-test-4-npu-a3 / run (1) | 3.5min | #34988003938 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353895) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-8-npu-a3 / run (0) | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353844) |
| base-b-test-4-npu-a3 / run (1) | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353895) |
| base-b-test-2-npu-a3 / run (0) | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353965) |

---

## 📋 各用例失败统计

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 1 | 0 | 1 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353844) |
| `npu_llada2_mini.py` | 1 | 0 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353895) |
| `npu_expert_distribution_recorder_mode.py` | 1 | 0 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353965) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #34988003938<br>[#37615 [kv-shard 2/4] Sharded pools](https://github.com/sgl-project/sglang/pull/37615) | `kvshard/2-sharded-pools` | 31.2min | 3 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/34988003938) |

---


## [Run #34988003938](https://github.com/sgl-project/sglang/actions/runs/34988003938)
- **分支**: `kvshard/2-sharded-pools`
- **总耗时**: 31.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/34988003938

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 4.1min | 环境问题 | modelscope_hub 包版本不兼容，缺少 DEFAULT_CREDENTIALS_PATH 导致导入失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353844) |
| base-b-test-4-npu-a3 / run (1) | 3.5min | 环境问题 | modelscope_hub 包版本不兼容，导入 DEFAULT_CREDENTIALS_PATH 失败导致测试报错。 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353895) |
| base-b-test-2-npu-a3 / run (0) | 4.0min | 环境问题 | modelscope_hub 包版本不兼容，缺少 DEFAULT_CREDENTIALS_PATH 导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353965) |

- **base-b-test-8-npu-a3 / run (0)**: 测试脚本导入 modelscope_hub.compat.constants 的 DEFAULT_CREDENTIALS_PATH 时报 ImportError，说明容器内 modelscope_hub 版本与代码不匹配，属依赖/环境问题，非代码逻辑错误。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353844

- **base-b-test-4-npu-a3 / run (1)**: test_npu_llada2_mini.py 运行时从 modelscope_hub.compat.constants 导入 DEFAULT_CREDENTIALS_PATH 失败（ImportError），属依赖包版本不匹配的环境问题，非代码逻辑错误，2 个用例全部失败。
  - 失败用例: npu_llada2_mini.py, npu_llada2_mini.py
  链接: https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353895

- **base-b-test-2-npu-a3 / run (0)**: 测试脚本导入 modelscope_hub.compat.constants 的 DEFAULT_CREDENTIALS_PATH 失败，报 ImportError，属依赖包版本不匹配的环境问题，导致 6 个测试全部失败（0/6 通过）。
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353965

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-1-npu-a2 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353941) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353944) |
| base-b-test-4-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353953) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353968) |
| base-b-test-1-npu-a3 / run (0) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627353984) |
| multimodal-gen-test-1-npu-a3 (0) | 38.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627354713) |
| multimodal-gen-test-4-npu-a3 (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627354911) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/34988003938/job/104627355180) |


---
*Auto-generated by ci_monitor.py*