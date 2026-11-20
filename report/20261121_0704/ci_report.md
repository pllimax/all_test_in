# NPU CI 执行监控（2026-11-20）
**生成时间**: 2026-11-21 07:04
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-20 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 10

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 107 个 | 失败 28 个 | 成功 Job 平均耗时 16.2min
- **Run 执行情况**: 成功 1 个 | 失败 9 个 | 成功 Run 平均耗时 14.6min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 66.6min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948814) |
| extra-b-test-2-npu-a3 / run (0) | 52.6min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948847) |
| extra-b-test-2-npu-a3 / run (0) | 40.9min | #44531840328 | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072228) |
| extra-b-test-1-npu-a3 / run (0) | 38.0min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948942) |
| extra-b-test-1-npu-a3 / run (1) | 37.9min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283949372) |
| extra-b-test-2-npu-a3 / run (1) | 37.0min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948913) |
| multimodal-gen-test-4-npu-a3 (0) | 35.1min | #44531840328 | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072008) |
| extra-b-test-1-npu-a3 / run (0) | 34.5min | #44531840328 | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072345) |
| extra-b-test-16-npu-a3 / run (0) | 33.2min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948911) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948707) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (1) | 49.5min | #44690316896 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827382) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 28.9min | #44734606931 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105847) |
| extra-b-test-4-npu-a3 / run (1) | 14.7min | #44690316896 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827584) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 12.8min | #44696120442 | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761668) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 11.6min | #44685891914 | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136130446609) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 10.5min | #44740314444 | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871709) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 10.1min | #44672235001 | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136089001412) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 10.1min | #44655155915 | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530793) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 9.6min | #44531840328 | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135742437427) |
| extra-b-test-2-npu-a3 / run (1) | 5.8min | #44690316896 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827579) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 7 | 0 | 7 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871709)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105847)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761668)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136130446609)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136089001412) |
| extra-b-test-16-npu-a3 / run (0) | 9 | 7 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905904)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827520) |
| extra-b-test-2-npu-a3 / run (0) | 9 | 7 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281906212)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827501) |
| extra-b-test-1-npu-a3 / run (0) | 9 | 7 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905828)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827545) |
| extra-b-test-4-npu-a3 / run (0) | 9 | 7 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905833)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827648) |
| extra-b-test-2-npu-a3 / run (1) | 8 | 6 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281906146)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827579) |
| extra-b-test-1-npu-a3 / run (1) | 8 | 6 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905974)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827672) |
| extra-b-test-4-npu-a3 / run (1) | 9 | 7 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905788)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827584) |
| extra-b-test-8-npu-a3 / run (0) | 9 | 7 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905962)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827440) |
| multimodal-gen-test-4-npu-a3 (0) | 8 | 7 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905667) |
| multimodal-gen-test-4-npu-a3 (1) | 8 | 6 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905704) |
| multimodal-gen-test-1-npu-a3 (1) | 5 | 4 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905626) |
| multimodal-gen-test-1-npu-a3 (0) | 5 | 4 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905719) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_deepseek_v4_flash_w8a8_8p_gpqa.py` | 7 | 0 | 7 | [extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871709)<br>[extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105847)<br>[extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761668) |
| `npu_speculative_moe_a2a_backend.py` | 8 | 7 | 1 | [extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827520) |
| `npu_mla_fia_hicache_bf16.py` | 8 | 7 | 1 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827501) |
| `npu_pause_continue.py` | 6 | 5 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827545) |
| `npu_dp_attention.py` | 8 | 7 | 1 | [extra-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827648) |
| `npu_hicache_mha.py` | 6 | 5 | 1 | [extra-b-test-1-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827672) |
| `npu_pd_disaggregation.py` | 6 | 5 | 1 | [extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827584) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 8 | 7 | 1 | [extra-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827440) |
| `npu_update_weights_from_tensor.py` | 7 | 6 | 1 | [extra-b-test-2-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827579) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #44734606931<br>[#43095 [Test] scheduler: Test that the admission re-match records num_matched_prefix_tokens](https://github.com/sgl-project/sglang/pull/43095) | `main` | 99.2min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44734606931) |
| #44740314444<br>[#44320 [Perf] [NPU] dcp: DSA extend gathers the prefix KV when that moves fewer bytes](https://github.com/sgl-project/sglang/pull/44320) | `npu-dcp-extend-kv-gather-main` | 80.2min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44740314444) |
| #44531840328<br>[#51536 [CI] [NPU] chore: Bump SGLang kernel NPU tag to 2026.11.0.post10](https://github.com/sgl-project/sglang/pull/51536) | `main` | 72.8min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44531840328) |
| #44672235001 | `feat/npu-none-shared-experts-fusion` | 59.3min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44672235001) |
| #44690316896<br>[#50889 [Feat] [NPU] hicache: Use kv_exchange for MHA KV and Mamba state transfers](https://github.com/sgl-project/sglang/pull/50889) | `mha_op_pr` | 53.6min | 9 | multimodal-gen-test-4-npu-a3 (1), extra-b-test-8-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0), extra-b-test-16-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (1), extra-b-test-4-npu-a3 / run (1), extra-b-test-4-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44690316896) |
| #44696120442<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 47.6min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44696120442) |
| #44685891914<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 47.0min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44685891914) |
| #44655155915<br>[#51689 [Feat] [NPU] dcp: Support Kimi K3.1 with DSpark decode graphs](https://github.com/sgl-project/sglang/pull/51689) | `feat/dsa-routed` | 11.0min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44655155915) |
| #44720421273<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post12](https://github.com/sgl-project/sglang/pull/51818) | `main` | 7.6min | 12 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), extra-b-test-4-npu-a3 / run (1), extra-b-test-1-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (0), extra-b-test-16-npu-a3 / run (0), extra-b-test-8-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1), extra-b-test-2-npu-a3 / run (1), extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44720421273) |

---


## [Run #44740314444](https://github.com/sgl-project/sglang/actions/runs/44740314444)
- **分支**: `npu-dcp-extend-kv-gather-main`
- **总耗时**: 80.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44740314444

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 10.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871709) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871709

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136302238415) |
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136302238438) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333276) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333326) |
| extra-b-test-16-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333418) |
| extra-b-test-2-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333420) |
| extra-b-test-1-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333470) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333501) |
| extra-b-test-2-npu-a3 / run (1) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333524) |
| extra-b-test-1-npu-a3 / run (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333525) |
| extra-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333527) |
| extra-b-test-8-npu-a3 / run (0) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136303333597) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871711) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44740314444/job/136327871833) |


## [Run #44734606931](https://github.com/sgl-project/sglang/actions/runs/44734606931)
- **分支**: `main`
- **总耗时**: 99.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44734606931

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 28.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105847) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105847

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136282866762) |
| multimodal-gen-test-1-npu-a3 (1) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948567) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948621) |
| multimodal-gen-test-4-npu-a3 (1) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948649) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948707) |
| extra-b-test-8-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948758) |
| extra-b-test-4-npu-a3 / run (0) | 66.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948814) |
| extra-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948822) |
| extra-b-test-2-npu-a3 / run (0) | 52.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948847) |
| extra-b-test-16-npu-a3 / run (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948911) |
| extra-b-test-2-npu-a3 / run (1) | 37.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948913) |
| extra-b-test-1-npu-a3 / run (0) | 38.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283948942) |
| extra-b-test-1-npu-a3 / run (1) | 37.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136283949372) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105810) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44734606931/job/136316105882) |


## [Run #44720421273](https://github.com/sgl-project/sglang/actions/runs/44720421273)
- **分支**: `main`
- **总耗时**: 7.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44720421273

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 3.0min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905626) |
| multimodal-gen-test-4-npu-a3 (0) | 2.7min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905667) |
| multimodal-gen-test-4-npu-a3 (1) | 3.0min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业失败原因不明确。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905704) |
| multimodal-gen-test-1-npu-a3 (0) | 3.0min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905719) |
| extra-b-test-4-npu-a3 / run (1) | 2.8min | 环境问题 | 测试日志文件未生成，用例脚本退出码5，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905788) |
| extra-b-test-1-npu-a3 / run (0) | 2.7min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905828) |
| extra-b-test-4-npu-a3 / run (0) | 2.8min | 环境问题 | 测试日志文件未生成，用例脚本退出码5，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905833) |
| extra-b-test-16-npu-a3 / run (0) | 2.5min | 环境问题 | 测试日志文件未生成，疑似测试用例未执行或提前失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905904) |
| extra-b-test-8-npu-a3 / run (0) | 2.6min | 环境问题 | 测试日志文件未生成，用例脚本无输出，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905962) |
| extra-b-test-1-npu-a3 / run (1) | 2.8min | 环境问题 | 测试日志文件未生成，用例脚本未产出日志，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905974) |
| extra-b-test-2-npu-a3 / run (1) | 2.5min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281906146) |
| extra-b-test-2-npu-a3 / run (0) | 2.5min | 环境问题 | 测试日志文件未生成，测试用例未实际执行或提前退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281906212) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志被截断，缺少真实错误信息；仅见 upload-artifact 提示未找到 diffusion-failures/ 路径，无 Traceback 或退出码 5 的上下文，无法确认是 server 启动失败还是其他环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905626

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件可上传，说明测试未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905667

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，缺少实际测试输出与错误堆栈；仅见 artifact 路径 diffusion-failures/ 不存在，无法确认是 server 启动失败还是其他原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905704

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见用例收集失败，而是 unittest 报 errors（退出码5），常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 upload-artifact 未找到 diffusion-failures/ 目录，无产物上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905719

- **extra-b-test-4-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 unittest 出现 errors。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905788

- **extra-b-test-1-npu-a3 / run (0)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未正常产出日志，结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905828

- **extra-b-test-4-npu-a3 / run (0)**: 日志显示未找到/tmp/test-logs/*.log，无artifacts上传；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致unittest出现errors。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905833

- **extra-b-test-16-npu-a3 / run (0)**: 日志显示未找到 /tmp/test-logs/*.log，无测试输出；结合退出码5，可能是 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），但日志中无具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905904

- **extra-b-test-8-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无任何 Traceback 或测试输出，作业在 k8s 步骤后直接清理。结合退出码 5，最可能是 setUpClass 中 server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例 error 且未产生日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905962

- **extra-b-test-1-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志中未见具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281905974

- **extra-b-test-2-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 未找到，无测试产物上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），但日志中未见具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281906146

- **extra-b-test-2-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无任何测试输出或 Traceback，说明测试脚本未产生日志即结束，疑似 setUpClass 阶段 server 启动失败或进程被 SIGKILL，属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136281906212

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136280429212) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44720421273/job/136280429220) |


## [Run #44696120442](https://github.com/sgl-project/sglang/actions/runs/44696120442)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 47.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44696120442

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 12.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761668) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761668

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136153343115) |
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136153343133) |
| multimodal-gen-test-1-npu-a3 (1) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426729) |
| multimodal-gen-test-4-npu-a3 (0) | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426742) |
| multimodal-gen-test-4-npu-a3 (1) | 27.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426796) |
| extra-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426831) |
| extra-b-test-1-npu-a3 / run (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426835) |
| extra-b-test-16-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426846) |
| multimodal-gen-test-1-npu-a3 (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426850) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426862) |
| extra-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426865) |
| extra-b-test-2-npu-a3 / run (1) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426925) |
| extra-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154426980) |
| extra-b-test-1-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136154427091) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761514) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44696120442/job/136164761588) |


## [Run #44690316896](https://github.com/sgl-project/sglang/actions/runs/44690316896)
- **分支**: `mha_op_pr`
- **总耗时**: 53.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44690316896

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 49.5min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 NPU 上 server 启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827382) |
| extra-b-test-8-npu-a3 / run (0) | 4.7min | 环境问题 | 日志中未见明确错误，作业在测试后正常上传产物并清理，失败原因需查看被省略的中间日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827440) |
| extra-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827501) |
| extra-b-test-16-npu-a3 / run (0) | 4.9min | 环境问题 | 日志被截断，无法看到真实错误，但作业在测试阶段失败并上传了测试日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827520) |
| extra-b-test-1-npu-a3 / run (0) | 5.2min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827545) |
| extra-b-test-2-npu-a3 / run (1) | 5.8min | 环境问题 | 日志中未见明确错误，但用例退出码5提示setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827579) |
| extra-b-test-4-npu-a3 / run (1) | 14.7min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827584) |
| extra-b-test-4-npu-a3 / run (0) | 5.2min | 环境问题 | 日志中未见测试执行失败的具体错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827648) |
| extra-b-test-1-npu-a3 / run (1) | 4.6min | 环境问题 | 日志中未见明确错误，但作业失败，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827672) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，未见具体 Traceback；作业以失败结束并上传 diffusion-failures-npu 工件，结合退出码 5 的说明，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），属环境/资源问题，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827382

- **extra-b-test-8-npu-a3 / run (0)**: 可见日志仅显示 runner 启动、下载 action、上传 artifact 和清理，均正常。真实失败点在被省略的中间部分，需查看测试日志 artifact 中的 Traceback/RuntimeError 才能定位。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827440

- **extra-b-test-2-npu-a3 / run (0)**: 日志省略了中间部分，仅显示artifact上传和清理成功，无Traceback。退出码5表示unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827501

- **extra-b-test-16-npu-a3 / run (0)**: 日志中间省略，仅见 artifact 上传与清理，未见 Traceback。按背景，退出码5多为 setUpClass 中 sglang server 启动失败（host OOM/SIGKILL），需查看上传的 selected-test-logs 确认。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827520

- **extra-b-test-1-npu-a3 / run (0)**: 日志中段省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pause_continue.py, npu_pause_continue.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827545

- **extra-b-test-2-npu-a3 / run (1)**: 日志被截断，仅见artifact上传与清理，无Traceback。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_update_weights_from_tensor.py, npu_update_weights_from_tensor.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827579

- **extra-b-test-4-npu-a3 / run (1)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827584

- **extra-b-test-4-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 selected-test-logs artifact 及 post job cleanup，均成功；关键测试阶段被省略，无法定位 Traceback。若退出码为 5，多为 setUpClass 中 sglang server 启动失败（如 host OOM/SIGKILL），需查看完整日志确认。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827648

- **extra-b-test-1-npu-a3 / run (1)**: 日志仅显示 artifact 上传成功和清理过程，无 Traceback。按背景知识，退出码 5 通常因 setUpClass 中 server 启动失败（如 host OOM、进程被 SIGKILL），需查看被省略的中间日志确认。
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827672

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136134866231) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136134866525) |
| multimodal-gen-test-1-npu-a3 (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827287) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827291) |
| multimodal-gen-test-1-npu-a3 (1) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44690316896/job/136135827323) |


## [Run #44685891914](https://github.com/sgl-project/sglang/actions/runs/44685891914)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 47.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44685891914

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 11.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136130446609) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136130446609

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136120194134) |
| extra-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136120194185) |
| extra-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090570) |
| extra-b-test-1-npu-a3 / run (1) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090594) |
| extra-b-test-2-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090613) |
| extra-b-test-16-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090630) |
| extra-b-test-1-npu-a3 / run (0) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090639) |
| extra-b-test-4-npu-a3 / run (1) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090647) |
| extra-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090669) |
| extra-b-test-2-npu-a3 / run (1) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136121090676) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136130446663) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44685891914/job/136130446695) |


## [Run #44672235001](https://github.com/sgl-project/sglang/actions/runs/44672235001)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 59.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44672235001

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 10.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136089001412) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136089001412

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136075833082) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136075833088) |
| extra-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939396) |
| extra-b-test-2-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939398) |
| extra-b-test-2-npu-a3 / run (1) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939399) |
| extra-b-test-16-npu-a3 / run (0) | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939401) |
| extra-b-test-1-npu-a3 / run (1) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939417) |
| extra-b-test-4-npu-a3 / run (1) | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939461) |
| extra-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939551) |
| extra-b-test-1-npu-a3 / run (0) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136076939620) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136089001557) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44672235001/job/136089001558) |


## [Run #44655155915](https://github.com/sgl-project/sglang/actions/runs/44655155915)
- **分支**: `feat/dsa-routed`
- **总耗时**: 11.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44655155915

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 10.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530793) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530793

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530130) |
| extra-b-test-16-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530219) |
| extra-b-test-2-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530337) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530383) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530393) |
| extra-b-test-1-npu-a3 / run (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530573) |
| extra-b-test-1-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530620) |
| extra-b-test-2-npu-a3 / run (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530779) |
| extra-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129530868) |
| extra-b-test-4-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129531539) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129531752) |
| extra-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129532197) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129533271) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44655155915/job/136129533416) |


## [Run #44531840328](https://github.com/sgl-project/sglang/actions/runs/44531840328)
- **分支**: `main`
- **总耗时**: 72.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44531840328

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 9.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135742437427) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135742437427

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135713030236) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135713030245) |
| multimodal-gen-test-4-npu-a3 (0) | 35.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072008) |
| multimodal-gen-test-1-npu-a3 (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072043) |
| multimodal-gen-test-1-npu-a3 (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072088) |
| extra-b-test-4-npu-a3 / run (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072149) |
| extra-b-test-16-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072162) |
| multimodal-gen-test-4-npu-a3 (1) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072170) |
| extra-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072223) |
| extra-b-test-2-npu-a3 / run (0) | 40.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072228) |
| extra-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072299) |
| extra-b-test-1-npu-a3 / run (0) | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135715072345) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135742437398) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44531840328/job/135742437490) |


---
*Auto-generated by ci_monitor.py*