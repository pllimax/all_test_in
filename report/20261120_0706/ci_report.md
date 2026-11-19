# NPU CI 执行监控（2026-11-19）
**生成时间**: 2026-11-20 07:06
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-19 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 24

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 278 个 | 失败 37 个 | 成功 Job 平均耗时 16.6min
- **Run 执行情况**: 成功 8 个 | 失败 16 个 | 成功 Run 平均耗时 95.2min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 69.0min | #44522582853 | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373986) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 49.0min | #44313087804 | [job link](https://github.com/sgl-project/sglang/actions/runs/44313087804/job/134893075497) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 47.5min | #44304724892 | [job link](https://github.com/sgl-project/sglang/actions/runs/44304724892/job/135291872809) |
| extra-b-test-2-npu-a3 / run (0) | 42.8min | #44543140706 | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612469) |
| extra-b-test-2-npu-a3 / run (0) | 42.7min | #44435027440 | [job link](https://github.com/sgl-project/sglang/actions/runs/44435027440/job/135262798720) |
| extra-b-test-2-npu-a3 / run (0) | 41.5min | #44454235705 | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416789) |
| extra-b-test-2-npu-a3 / run (0) | 41.5min | #44251536550 | [job link](https://github.com/sgl-project/sglang/actions/runs/44251536550/job/134888822008) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 40.9min | #44296753017 | [job link](https://github.com/sgl-project/sglang/actions/runs/44296753017/job/135313743017) |
| extra-b-test-2-npu-a3 / run (0) | 40.5min | #44528667603 | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552471) |
| extra-b-test-2-npu-a3 / run (0) | 40.0min | #44313087804 | [job link](https://github.com/sgl-project/sglang/actions/runs/44313087804/job/134866485428) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 64.2min | #44430889179 | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134600) |
| extra-b-test-2-npu-a3 / run (0) | 63.3min | #44522582853 | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374031) |
| extra-b-test-1-npu-a3 / run (0) | 62.9min | #44522582853 | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374225) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 38.1min | #44430889179 | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595380) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 36.0min | #44543140706 | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517787) |
| extra-b-test-2-npu-a3 / run (0) | 34.4min | #44516526118 | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215533) |
| extra-b-test-1-npu-a3 / run (0) | 34.0min | #44449369647 | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 33.7min | #44523876192 | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940317) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 32.4min | #44479323501 | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077760) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 30.3min | #44528667603 | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602555885) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 15 | 8 | 5 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517787)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602555885)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940317)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077760)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135418922547) |
| extra-b-test-1-npu-a3 / run (0) | 22 | 15 | 3 | 1 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374225)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016537) |
| multimodal-gen-test-1-npu-a3 (1) | 13 | 11 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535405) |
| multimodal-gen-test-1-npu-a3 (0) | 13 | 11 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535397) |
| multimodal-gen-test-4-npu-a3 (0) | 22 | 20 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134600) |
| extra-b-test-2-npu-a3 / run (0) | 22 | 17 | 1 | 0 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374031) |
| extra-b-test-16-npu-a3 / run (0) | 22 | 18 | 1 | 0 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535610) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 30 | 29 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595380) |
| extra-b-test-1-npu-a3 / run (1) | 1 | 0 | 0 | 1 | 0 | - |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 7 | 6 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356669749) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 7 | 6 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356670058) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_deepseek_v4_flash_w8a8_8p_gpqa.py` | 7 | 3 | 4 | [extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517787)<br>[extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602555885)<br>[extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940317) |
| `minimax_h3_t2va_2npu` | 9 | 7 | 2 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535479)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134600) |
| `npu_topk_routing_inputs.py` | 7 | 6 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016537) |
| `npu_speculative_moe_a2a_backend.py` | 13 | 12 | 1 | [extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535610) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 9 | 8 | 1 | [extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595380) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 7 | 6 | 1 | [extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135418922547) |
| `npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` | 1 | 0 | 1 | [extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356669749) |
| `npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py` | 1 | 0 | 1 | [extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356670058) |
| `shape0` | 1 | 0 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |
| `shape1` | 1 | 0 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |
| `shape0-0.0001-1e-06` | 1 | 0 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |
| `shape1-100.0-1e-05` | 1 | 0 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |
| `test_rmsnorm_refuses_tiles_under_16_rows` | 1 | 0 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |
| `npu_fusions.py` | 1 | 0 | 1 | [extra-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #44454235705<br>[#49995 [Refactor] [NPU] operators: Migrate sgl-kernel-npu calls to public operators entry points](https://github.com/sgl-project/sglang/pull/49995) | `sgl-kernel-npu-refactor` | 92.3min | 2 | extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3, extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44454235705) |
| #44523876192<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 89.8min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44523876192) |
| #44430889179<br>[#49995 [Refactor] [NPU] operators: Migrate sgl-kernel-npu calls to public operators entry points](https://github.com/sgl-project/sglang/pull/49995) | `sgl-kernel-npu-refactor` | 84.8min | 2 | multimodal-gen-test-4-npu-a3 (0), extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44430889179) |
| #44543140706<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 83.2min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44543140706) |
| #44528667603<br>[#44320 [Perf] [NPU] dcp: DSA extend gathers the prefix KV when that moves fewer bytes](https://github.com/sgl-project/sglang/pull/44320) | `npu-dcp-extend-kv-gather-main` | 82.9min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44528667603) |
| #44522582853<br>[#51504 [Doc] cookbook: Refresh SemiAnalysis AgentX launches to InferenceX main df623226](https://github.com/sgl-project/sglang/pull/51504) | `main` | 79.5min | 2 | extra-b-test-2-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44522582853) |
| #44477449994 | `feat/npu-none-shared-experts-fusion` | 69.9min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44477449994) |
| #44449369647<br>[#44056 [Feat] [NPU] diffusion: Adapt Qwen-Image 2.1 and Turbo on Ascend](https://github.com/sgl-project/sglang/pull/44056) | `qwenimage21` | 45.9min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), extra-b-test-16-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44449369647) |
| #44516526118<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 44.2min | 3 | extra-b-test-1-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0), extra-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44516526118) |
| #44441101443 | `feat/npu-none-shared-experts-fusion` | 40.7min | 1 | extra-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44441101443) |
| #44479323501<br>[#48420 [Feat] [NPU] kimi-k3.1: Add model support and route DSA attention path on Ascend](https://github.com/sgl-project/sglang/pull/48420) | `feat/dsa-routed` | 40.1min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44479323501) |
| #44506875531<br>[#44320 [Perf] [NPU] dcp: DSA extend gathers the prefix KV when that moves fewer bytes](https://github.com/sgl-project/sglang/pull/44320) | `npu-dcp-extend-kv-gather-main` | 21.3min | 4 | extra-b-test-1-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (0), extra-b-test-16-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44506875531) |
| #44388749861<br>[#44320 [Perf] [NPU] dcp: DSA extend gathers the prefix KV when that moves fewer bytes](https://github.com/sgl-project/sglang/pull/44320) | `npu-dcp-extend-kv-gather-main` | 20.9min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44388749861) |
| #44542996259<br>[#51551 [CI] [NPU] ci: Split extra-b-test-1/2 into two partitions to avoid timeouts](https://github.com/sgl-project/sglang/pull/51551) | `ci/npu-extra-b-partitions` | 16.5min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), extra-b-test-16-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (1), extra-b-test-4-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (1), extra-b-test-1-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44542996259) |
| #44524201427<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 8.5min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44524201427) |
| #44503043747<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 6.0min | 0 |  | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44503043747) |

---


## [Run #44543140706](https://github.com/sgl-project/sglang/actions/runs/44543140706)
- **分支**: `dsv41-a5`
- **总耗时**: 83.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44543140706

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 36.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517787) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517787

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135627011554) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135627011685) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612104) |
| multimodal-gen-test-4-npu-a3 (1) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612124) |
| multimodal-gen-test-1-npu-a3 (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612313) |
| multimodal-gen-test-4-npu-a3 (0) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612463) |
| extra-b-test-2-npu-a3 / run (0) | 42.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612469) |
| extra-b-test-1-npu-a3 / run (0) | 33.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612490) |
| extra-b-test-8-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612566) |
| extra-b-test-16-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612644) |
| extra-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628612940) |
| extra-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135628613017) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517536) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44543140706/job/135656517633) |


## [Run #44542996259](https://github.com/sgl-project/sglang/actions/runs/44542996259)
- **分支**: `ci/npu-extra-b-partitions`
- **总耗时**: 16.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44542996259

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 11.9min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824538) |
| multimodal-gen-test-1-npu-a3 (1) | 12.2min | 环境问题 | 多模态测试用例执行失败，上传了diffusion-failures产物，疑似server启动失败导致unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824555) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 NPU 环境或 server 启动异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824619) |
| multimodal-gen-test-4-npu-a3 (0) | 11.6min | 环境问题 | 多模态生成测试作业失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824680) |
| extra-b-test-16-npu-a3 / run (0) | 12.8min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824859) |
| extra-b-test-4-npu-a3 / run (1) | 10.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825037) |
| extra-b-test-4-npu-a3 / run (0) | 10.9min | 其他 | 日志被截断，缺少真实错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825040) |
| extra-b-test-1-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825049) |
| extra-b-test-2-npu-a3 / run (1) | 12.8min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825133) |
| extra-b-test-1-npu-a3 / run (0) | 12.8min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825141) |
| extra-b-test-2-npu-a3 / run (0) | 12.9min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825142) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part0-2.zip 失败产物，作业以非零退出。结合退出码 5 提示，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824538

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示作业上传了diffusion-failures-npu-1-part1-2.zip失败产物，说明测试用例执行出错；结合退出码5对应unittest errors，常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看产物中Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824555

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，未见具体 Traceback；作业退出码 5 通常表示 unittest 存在 errors，最常见为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。已上传 diffusion-failures-npu-2-part1-2.zip 工件，需查看该工件中的真实错误定位。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824619

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-2.zip 工件，说明测试用例执行失败并收集了失败产物；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824680

- **extra-b-test-16-npu-a3 / run (0)**: 可见日志仅包含 runner 初始化、action 下载、artifact 上传和清理阶段，中间省略部分未显示 Traceback/RuntimeError 等真实错误，无法判断是 setUpClass 启动失败还是其他原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824859

- **extra-b-test-4-npu-a3 / run (1)**: 日志中段被省略，未见具体Traceback；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略部分确认真实异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825037

- **extra-b-test-4-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、action 下载、artifact 上传和清理阶段，均正常；中间省略部分才包含测试执行与报错，但未提供。无法确认是否为 setUpClass 中 server 启动失败或退出码 5 的具体 Traceback，需查看省略段日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825040


- **extra-b-test-2-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，未见Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825133

- **extra-b-test-1-npu-a3 / run (0)**: 日志省略了中间部分，仅显示artifact上传和清理成功，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825141

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，通常为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628825142

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135627048061) |
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135627048074) |
| extra-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44542996259/job/135628824891) |


## [Run #44528667603](https://github.com/sgl-project/sglang/actions/runs/44528667603)
- **分支**: `npu-dcp-extend-kv-gather-main`
- **总耗时**: 82.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44528667603

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 30.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602555885) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602555885

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135576115460) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135576115560) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577551629) |
| multimodal-gen-test-4-npu-a3 (1) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577551742) |
| extra-b-test-8-npu-a3 / run (0) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552028) |
| extra-b-test-1-npu-a3 / run (0) | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552247) |
| extra-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552248) |
| extra-b-test-4-npu-a3 / run (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552329) |
| extra-b-test-2-npu-a3 / run (0) | 40.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552471) |
| extra-b-test-16-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135577552791) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602555906) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44528667603/job/135602556007) |


## [Run #44524201427](https://github.com/sgl-project/sglang/actions/runs/44524201427)
- **分支**: `dsv41-a5`
- **总耗时**: 8.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44524201427

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 5.0min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，多为setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621491026) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 日志中间省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（host OOM或进程被SIGKILL），需查看被省略的测试日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621491026

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621488165) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621488178) |
| multimodal-gen-test-4-npu-a3 (0) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621488837) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621488963) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621489152) |
| extra-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621489322) |
| extra-b-test-1-npu-a3 / run (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621489625) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621489820) |
| extra-b-test-2-npu-a3 / run (0) | 39.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621490092) |
| extra-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621490566) |
| extra-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621490950) |
| extra-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621491777) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621493824) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44524201427/job/135621493825) |


## [Run #44523876192](https://github.com/sgl-project/sglang/actions/runs/44523876192)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 89.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44523876192

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 33.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940317) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940317

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135559478445) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135559478687) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548274) |
| extra-b-test-4-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548426) |
| extra-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548485) |
| extra-b-test-1-npu-a3 / run (0) | 30.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548504) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548524) |
| extra-b-test-2-npu-a3 / run (0) | 38.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548531) |
| extra-b-test-4-npu-a3 / run (1) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548595) |
| extra-b-test-16-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135560548624) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940202) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44523876192/job/135584940452) |


## [Run #44522582853](https://github.com/sgl-project/sglang/actions/runs/44522582853)
- **分支**: `main`
- **总耗时**: 79.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44522582853

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 63.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374031) |
| extra-b-test-1-npu-a3 / run (0) | 62.9min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374225) |

- **extra-b-test-2-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374031

- **extra-b-test-1-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看上传的测试日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374225

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135554927249) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373467) |
| multimodal-gen-test-1-npu-a3 (1) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373488) |
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373545) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373549) |
| extra-b-test-8-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373850) |
| extra-b-test-4-npu-a3 / run (0) | 69.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556373986) |
| extra-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374030) |
| extra-b-test-16-npu-a3 / run (0) | 36.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44522582853/job/135556374156) |


## [Run #44516526118](https://github.com/sgl-project/sglang/actions/runs/44516526118)
- **分支**: `dsv41-a5`
- **总耗时**: 44.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44516526118

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (0) | 29.5min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215511) |
| extra-b-test-2-npu-a3 / run (0) | 34.4min | 环境问题 | 上传测试日志产物时作业已结束，CreateArtifact 返回 403 permission_denied（job is completed），导致步骤失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215533) |
| extra-b-test-16-npu-a3 / run (0) | 21.9min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215560) |

- **extra-b-test-1-npu-a3 / run (0)**: 日志中段被省略，仅见 artifact 上传与清理，无 Traceback。退出码5表示 unittest 存在 errors，最常见为 setUpClass 时 server 启动失败（host OOM 或进程被 SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215511

- **extra-b-test-2-npu-a3 / run (0)**: 日志显示 upload-artifact 调用 CreateArtifact 收到 403 Forbidden，响应体为 code=permission_denied, msg=job is completed，说明作业在产物上传前已被判定完成/取消，属 runner 与 GitHub 结果服务交互的环境/基础设施问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215533

- **extra-b-test-16-npu-a3 / run (0)**: 日志中段被省略，未见Traceback/RuntimeError等真实错误；仅见artifact上传成功和清理步骤。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215560

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135539822364) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135539822395) |
| multimodal-gen-test-4-npu-a3 (0) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541214821) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541214980) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215047) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215118) |
| extra-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215422) |
| extra-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215514) |
| extra-b-test-4-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44516526118/job/135541215761) |


## [Run #44506875531](https://github.com/sgl-project/sglang/actions/runs/44506875531)
- **分支**: `npu-dcp-extend-kv-gather-main`
- **总耗时**: 21.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44506875531

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (0) | 17.4min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408280) |
| extra-b-test-4-npu-a3 / run (0) | 17.4min | 其他 | 日志被截断，缺少真实错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408331) |
| extra-b-test-16-npu-a3 / run (0) | 17.4min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408346) |
| extra-b-test-2-npu-a3 / run (0) | 17.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408421) |

- **extra-b-test-1-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408280

- **extra-b-test-4-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、下载 action、上传 artifact 和清理阶段，中间省略部分包含实际测试输出。退出码 5 提示 unittest 存在 errors，通常为 setUpClass 阶段 sglang server 启动失败，但需查看省略段中的 Traceback/RuntimeError 才能确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408331

- **extra-b-test-16-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，通常为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408346

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见退出码5（unittest errors）。按背景知识，最常见为 setUpClass 时 sglang server 启动失败（host OOM 或进程被 SIGKILL），需查看省略部分的 Traceback/RuntimeError 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408421

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135501096716) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135501096730) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408044) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408183) |
| extra-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408253) |
| extra-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44506875531/job/135502408277) |


## [Run #44503043747](https://github.com/sgl-project/sglang/actions/runs/44503043747)
- **分支**: `dsv41-a5`
- **总耗时**: 6.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44503043747

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 5.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530840692) |
| extra-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530840715) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-1-npu-a3 (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530842179) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843076) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843185) |
| extra-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843236) |
| extra-b-test-16-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843420) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843508) |
| extra-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843752) |
| extra-b-test-4-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843900) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530843972) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44503043747/job/135530907615) |


## [Run #44479323501](https://github.com/sgl-project/sglang/actions/runs/44479323501)
- **分支**: `feat/dsa-routed`
- **总耗时**: 40.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44479323501

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 32.4min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077760) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077760

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543075802) |
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543076031) |
| extra-b-test-2-npu-a3 / run (0) | 39.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543076107) |
| extra-b-test-1-npu-a3 / run (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077214) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077229) |
| extra-b-test-16-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077364) |
| extra-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543077755) |
| extra-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543078010) |
| extra-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543078424) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543080558) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543080650) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44479323501/job/135543122958) |


## [Run #44477449994](https://github.com/sgl-project/sglang/actions/runs/44477449994)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 69.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44477449994

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 27.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135418922547) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135418922547

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135401527863) |
| extra-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135401527867) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402380715) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402380730) |
| extra-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402380935) |
| extra-b-test-1-npu-a3 / run (0) | 31.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402380984) |
| extra-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402381010) |
| extra-b-test-16-npu-a3 / run (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402381029) |
| extra-b-test-4-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402381031) |
| extra-b-test-2-npu-a3 / run (0) | 38.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135402381099) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135418922592) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44477449994/job/135418922605) |


## [Run #44454235705](https://github.com/sgl-project/sglang/actions/runs/44454235705)
- **分支**: `sgl-kernel-npu-refactor`
- **总耗时**: 92.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44454235705

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 7.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356669749) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 5.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356670058) |

- **extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py, npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356669749

- **extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135356670058

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135325405786) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135325405830) |
| multimodal-gen-test-1-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416643) |
| multimodal-gen-test-4-npu-a3 (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416648) |
| extra-b-test-16-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416675) |
| multimodal-gen-test-1-npu-a3 (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416677) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416680) |
| extra-b-test-2-npu-a3 / run (0) | 41.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416789) |
| extra-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416806) |
| extra-b-test-1-npu-a3 / run (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416808) |
| extra-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416849) |
| extra-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135326416881) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 38.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135342292217) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135342292324) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44454235705/job/135342292409) |


## [Run #44449369647](https://github.com/sgl-project/sglang/actions/runs/44449369647)
- **分支**: `qwenimage21`
- **总耗时**: 45.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44449369647

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 20.0min | 环境问题 | multimodal 测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535397) |
| multimodal-gen-test-1-npu-a3 (1) | 21.2min | 环境问题 | multimodal-gen 测试用例执行失败，上传了 diffusion-failures 失败产物，疑似 setUpClass 阶段 server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535405) |
| extra-b-test-16-npu-a3 / run (0) | 27.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535610) |
| extra-b-test-1-npu-a3 / run (0) | 34.0min | 其他 | 日志被截断，缺少真实错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业运行约20分钟后上传 diffusion-failures-npu-1-part0-1.zip 产物，说明测试用例执行失败并收集了失败信息；结合退出码5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看产物中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535397

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见退出后上传 diffusion-failures-npu-1-part1-1.zip 失败产物，说明用例运行出错（退出码5，unittest errors），常见于 setUpClass 时 sglang server 启动失败（host OOM/进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535405

- **extra-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535610

- **extra-b-test-1-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、下载 action、上传 artifact 和清理阶段，中间省略部分包含实际测试输出。退出码 5 提示 unittest 存在 errors，可能为 setUpClass 中 sglang server 启动失败，但日志未显示 Traceback，需查看完整日志确认。
  - 失败用例: shape0, shape1, shape0-0.0001-1e-06, shape1-100.0-1e-05, test_rmsnorm_refuses_tiles_under_16_rows
  链接: https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535751

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135309429455) |
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135309429462) |
| multimodal-gen-test-4-npu-a3 (0) | 39.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535479) |
| multimodal-gen-test-4-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535522) |
| extra-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535587) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535595) |
| extra-b-test-4-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535596) |
| extra-b-test-2-npu-a3 / run (0) | 39.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44449369647/job/135310535642) |


## [Run #44441101443](https://github.com/sgl-project/sglang/actions/runs/44441101443)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 40.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44441101443

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (0) | 30.1min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016537) |

- **extra-b-test-1-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、action 下载、artifact 上传和清理阶段，均正常完成；中间省略部分才包含测试执行与退出码 5 的真实 Traceback，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败。
  - 失败用例: npu_topk_routing_inputs.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016537

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135282091195) |
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135282091309) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016328) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016430) |
| extra-b-test-16-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016462) |
| extra-b-test-2-npu-a3 / run (0) | 37.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016491) |
| extra-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016516) |
| extra-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016535) |
| extra-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44441101443/job/135283016538) |


## [Run #44430889179](https://github.com/sgl-project/sglang/actions/runs/44430889179)
- **分支**: `sgl-kernel-npu-refactor`
- **总耗时**: 84.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44430889179

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 64.2min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134600) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 38.1min | 环境问题 | 日志中未见测试失败的具体错误信息，作业在 artifact 上传后正常清理退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595380) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；作业退出后上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行中报错（可能 setUpClass 阶段 server 启动失败或 OOM）。需查看产物与完整日志确认根因。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134600

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志仅显示 runner 初始化、下载 action、上传测试日志 artifact 及 post job cleanup，未包含测试执行阶段的 Traceback/RuntimeError 等真实错误，无法定位失败原因，需查看被省略的中间日志或 artifact 内容。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595380

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135247860483) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135247860527) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134465) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134542) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134546) |
| extra-b-test-1-npu-a3 / run (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134595) |
| extra-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134646) |
| extra-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134672) |
| extra-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134722) |
| extra-b-test-2-npu-a3 / run (0) | 39.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134732) |
| extra-b-test-16-npu-a3 / run (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135249134735) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 38.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595305) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44430889179/job/135267595377) |


## [Run #44388749861](https://github.com/sgl-project/sglang/actions/runs/44388749861)
- **分支**: `npu-dcp-extend-kv-gather-main`
- **总耗时**: 20.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44388749861

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 19.8min | 环境问题 | 日志被截断，未包含实际测试失败信息，仅见作业收尾阶段正常上传产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489621560) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 可见日志仅为 runner 初始化与 artifact 上传/清理，缺少 unittest 报错或 Traceback；退出码 5 提示 setUpClass 中 sglang server 启动失败（如 host OOM/SIGKILL），需查看被省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489621560

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489619581) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489619906) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489620714) |
| extra-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489620733) |
| extra-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489620867) |
| extra-b-test-1-npu-a3 / run (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489621004) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489621084) |
| extra-b-test-2-npu-a3 / run (0) | 39.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489621210) |
| extra-b-test-4-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489622461) |
| extra-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489622491) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489625056) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44388749861/job/135489625607) |


---
*Auto-generated by ci_monitor.py*