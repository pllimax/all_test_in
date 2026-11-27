# NPU CI 执行监控（2026-11-27）
**生成时间**: 2026-11-28 07:07
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-27 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 19

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 237 个 | 失败 20 个 | 成功 Job 平均耗时 14.6min
- **Run 执行情况**: 成功 10 个 | 失败 9 个 | 成功 Run 平均耗时 65.7min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 53.1min | #45997546494 | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140516427829) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 49.3min | #45921869748 | [job link](https://github.com/sgl-project/sglang/actions/runs/45921869748/job/140275549859) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 49.2min | #45875069478 | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140256054004) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 49.0min | #45941688782 | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140383792406) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 47.5min | #45973557600 | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601396) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 45.3min | #45952889737 | [job link](https://github.com/sgl-project/sglang/actions/runs/45952889737/job/140376571486) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 44.9min | #45976615375 | [job link](https://github.com/sgl-project/sglang/actions/runs/45976615375/job/140442979484) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 44.7min | #45935537360 | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140306442038) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 38.7min | #45926215606 | [job link](https://github.com/sgl-project/sglang/actions/runs/45926215606/job/140278880400) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 35.9min | #45927478484 | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403147890) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 34.7min | #45921703844 | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012394) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | #45875069478 | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122036) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 33.8min | #45973557600 | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601411) |
| multimodal-gen-test-4-npu-a3 (0) | 29.0min | #45970853256 | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910398) |
| multimodal-gen-test-4-npu-a3 (0) | 26.9min | #45997546494 | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169371) |
| multimodal-gen-test-4-npu-a3 (0) | 25.4min | #45934625827 | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693124) |
| multimodal-gen-test-1-npu-a3 (0) | 22.4min | #45875069478 | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247121957) |
| multimodal-gen-test-4-npu-a3 (0) | 20.1min | #45927478484 | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403142363) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | #45970853256 | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910532) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | #45934625827 | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693041) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| multimodal-gen-test-4-npu-a3 (0) | 13 | 7 | 5 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169371)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910398)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587574)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693124)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122036) |
| multimodal-gen-test-1-npu-a3 (0) | 5 | 0 | 5 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169387)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910532)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693041)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403142243)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247121957) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 24 | 20 | 2 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601411)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012394) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 15 | 13 | 0 | 2 | 0 | - |
| extra-b-test-4-npu-a3 / run (1) | 16 | 15 | 0 | 1 | 0 | - |
| extra-b-test-4-npu-a3 / run (0) | 16 | 15 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910763) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 11 | 10 | 0 | 1 | 0 | - |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `wan2_2_t2v_14b_w8a8_2npu` | 6 | 0 | 6 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169371)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910398)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587574) |
| `wan2_1_t2v_1.3b_1_npu` | 5 | 0 | 5 | [multimodal-gen-test-1-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169387)<br>[multimodal-gen-test-1-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910532)<br>[multimodal-gen-test-1-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693041) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 7 | 5 | 2 | [extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601411)<br>[extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012394) |
| `npu_dp_attention.py` | 9 | 8 | 1 | [extra-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910763) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #45997546494<br>[#53546 [Fix] ci: Skip short first-attempt runs of every event in the runner utilization scan](https://github.com/sgl-project/sglang/pull/53546) | `main` | 110.8min | 2 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45997546494) |
| #45875069478<br>[#51016 [Feat] [NPU] glm5: Support INT8 and mxFP8 index cache for the KPool pooled-key indexer](https://github.com/sgl-project/sglang/pull/51016) | `npu-dsa-int8-index-kpool` | 108.5min | 2 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45875069478) |
| #45941688782<br>[#49547 [Feat] [NPU] DSpark: GLM-5.2 support DSpark compact mode](https://github.com/sgl-project/sglang/pull/49547) | `feat/glm52-dspark-compact-main` | 95.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45941688782) |
| #45935537360<br>[#52518 [Feat] [NPU] kimi-k3.1: Enable DFLASH speculative decoding on Ascend](https://github.com/sgl-project/sglang/pull/52518) | `k3.1-dflash2-npu-v2` | 88.0min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45935537360) |
| #45973557600<br>[#49547 [Feat] [NPU] DSpark: GLM-5.2 support DSpark compact mode](https://github.com/sgl-project/sglang/pull/49547) | `feat/glm52-dspark-compact-main` | 76.6min | 1 | extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45973557600) |
| #45921703844<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 62.0min | 1 | extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45921703844) |
| #45970853256<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 35.6min | 3 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), extra-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45970853256) |
| #45934625827<br>[#32602 [Feat] [NPU] quantization: :sparkles: Support online W4A4 MoE](https://github.com/sgl-project/sglang/pull/32602) | `junlin_qwen3.5_moe_w4a4` | 33.7min | 2 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45934625827) |
| #45927478484<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 23.6min | 2 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45927478484) |

---


## [Run #45997546494](https://github.com/sgl-project/sglang/actions/runs/45997546494)
- **分支**: `main`
- **总耗时**: 110.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45997546494

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 26.9min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败导致 unittest errors。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169371) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169387) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例运行出错；结合退出码 5 与背景知识，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169371

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业退出并上传 diffusion-failures-npu-1-part0-1.zip 失败产物，说明测试用例运行出错（退出码5，unittest errors），常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看产物中 Traceback 确认。
  - 失败用例: wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169387

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140500798205) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169274) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169404) |
| extra-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169422) |
| extra-b-test-4-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169477) |
| extra-b-test-16-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169512) |
| extra-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169523) |
| extra-b-test-2-npu-a3 / run (1) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169595) |
| extra-b-test-1-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169618) |
| extra-b-test-1-npu-a3 / run (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169646) |
| extra-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140502169735) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140516427752) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140516427809) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 53.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140516427829) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140542255354) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45997546494/job/140542255540) |


## [Run #45973557600](https://github.com/sgl-project/sglang/actions/runs/45973557600)
- **分支**: `feat/glm52-dspark-compact-main`
- **总耗时**: 76.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45973557600

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 33.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601411) |

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志中段被省略，未见具体Traceback。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。需查看省略部分及上传的selected-test-logs确认真实异常。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601411

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140429528517) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140429528529) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430796805) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430796852) |
| extra-b-test-1-npu-a3 / run (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430796874) |
| extra-b-test-2-npu-a3 / run (1) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430796953) |
| extra-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430796955) |
| extra-b-test-1-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430796968) |
| extra-b-test-2-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430797010) |
| extra-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430797034) |
| extra-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430797039) |
| extra-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140430797122) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601378) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 47.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45973557600/job/140442601396) |


## [Run #45970853256](https://github.com/sgl-project/sglang/actions/runs/45970853256)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 35.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45970853256

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.0min | 环境问题 | 多模态生成测试用例执行失败，退出码5表示unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910398) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | 环境问题 | multimodal 测试用例执行失败，退出码 5 表示 unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910532) |
| extra-b-test-4-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910659) |
| extra-b-test-4-npu-a3 / run (0) | 7.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910763) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中间省略部分未显示具体Traceback，但作业上传了diffusion-failures-npu-2-part0-3.zip失败产物，退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看省略日志确认。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910398

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见失败产物 diffusion-failures-npu-1-part0-3.zip 上传成功，未见具体 Traceback。按退出码 5 推断为 setUpClass 中 server 启动失败（如 host OOM 或进程被 SIGKILL），属环境/资源问题，需查看省略段确认。
  - 失败用例: wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910532


- **extra-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910763

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140417588838) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140417588922) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910466) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910519) |
| extra-b-test-2-npu-a3 / run (1) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910724) |
| extra-b-test-1-npu-a3 / run (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910733) |
| extra-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910776) |
| extra-b-test-16-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910785) |
| extra-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910790) |
| extra-b-test-1-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45970853256/job/140418910917) |


## [Run #45941688782](https://github.com/sgl-project/sglang/actions/runs/45941688782)
- **分支**: `feat/glm52-dspark-compact-main`
- **总耗时**: 95.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45941688782

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140404465832) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140373343686) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140373343710) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294368) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294424) |
| extra-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294447) |
| extra-b-test-1-npu-a3 / run (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294468) |
| extra-b-test-2-npu-a3 / run (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294484) |
| extra-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294527) |
| extra-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294551) |
| extra-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294552) |
| extra-b-test-1-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294573) |
| extra-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140374294864) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140383792327) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140383792359) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 49.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140383792406) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45941688782/job/140404465823) |


## [Run #45935537360](https://github.com/sgl-project/sglang/actions/runs/45935537360)
- **分支**: `k3.1-dflash2-npu-v2`
- **总耗时**: 88.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45935537360

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 11.8min | 环境问题 | 日志被截断，未见真实错误，但上传了 diffusion-failures 工件，推测测试用例失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587574) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中间省略，仅见上传 diffusion-failures-npu-2-part0-2.zip 工件，说明多模态生成测试存在失败用例；未见 Traceback，无法确认具体原因，需查看工件或完整日志。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587574

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140299551899) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140299551916) |
| extra-b-test-1-npu-a3 / run (0) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587595) |
| extra-b-test-2-npu-a3 / run (1) | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587607) |
| extra-b-test-2-npu-a3 / run (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587612) |
| extra-b-test-4-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587613) |
| extra-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587628) |
| extra-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587631) |
| extra-b-test-16-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587645) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587657) |
| extra-b-test-1-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140300587670) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 44.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140306442038) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140306442067) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140306442122) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140320264699) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45935537360/job/140320264707) |


## [Run #45934625827](https://github.com/sgl-project/sglang/actions/runs/45934625827)
- **分支**: `junlin_qwen3.5_moe_w4a4`
- **总耗时**: 33.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45934625827

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693041) |
| multimodal-gen-test-4-npu-a3 (0) | 25.4min | 其他 | 多模态生成测试失败，上传了 diffusion-failures 产物，但日志省略段未显示具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693124) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140408394042) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140408394185) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140408394422) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见测试结束后上传 diffusion-failures-npu-1-part0-3.zip 失败产物，作业以非零退出码结束。结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段中的 Traceback/RuntimeError 确认。
  - 失败用例: wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693041

- **multimodal-gen-test-4-npu-a3 (0)**: 作业退出码5表示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。日志中间省略，未见Traceback，需查看diffusion-failures-npu-2-part0-3.zip产物确认具体异常。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693124




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140396399392) |
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140396399463) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693042) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693097) |
| extra-b-test-16-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693262) |
| extra-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693291) |
| extra-b-test-1-npu-a3 / run (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693300) |
| extra-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693350) |
| extra-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693370) |
| extra-b-test-1-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693377) |
| extra-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693445) |
| extra-b-test-2-npu-a3 / run (1) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45934625827/job/140397693447) |


## [Run #45927478484](https://github.com/sgl-project/sglang/actions/runs/45927478484)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 23.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45927478484

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 12.4min | 环境问题 | 多模态测试用例执行失败，退出码5表示unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403142243) |
| multimodal-gen-test-4-npu-a3 (0) | 20.1min | 环境问题 | 多模态生成测试用例执行失败，退出码5表示unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403142363) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 4.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145276) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被省略，仅见失败产物diffusion-failures-npu-1-part0-3.zip上传。退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看省略部分Traceback确认。
  - 失败用例: wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403142243

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，仅见失败产物diffusion-failures-npu-2-part0-3.zip上传。退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略部分Traceback确认。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403142363


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403143965) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403144429) |
| multimodal-gen-test-4-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403144568) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403144572) |
| extra-b-test-1-npu-a3 / run (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145169) |
| extra-b-test-16-npu-a3 / run (0) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145340) |
| extra-b-test-8-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145353) |
| extra-b-test-1-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145592) |
| extra-b-test-2-npu-a3 / run (1) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145753) |
| extra-b-test-2-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403145875) |
| extra-b-test-4-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403146020) |
| extra-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403146752) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 35.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403147890) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 6.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45927478484/job/140403148306) |


## [Run #45921703844](https://github.com/sgl-project/sglang/actions/runs/45921703844)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 62.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45921703844

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 34.7min | 环境问题 | 精度测试作业失败，日志中段被省略，无法看到真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012394) |

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志仅显示作业准备、artifact上传和清理阶段，中间测试执行部分被省略，未包含Traceback/RuntimeError等真实错误信息。根据退出码5推断为unittest errors，最可能是setUpClass时server启动失败（host OOM/SIGKILL），需查看完整日志确认。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012394

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265017716) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265017720) |
| extra-b-test-1-npu-a3 / run (1) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783284) |
| extra-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783288) |
| extra-b-test-4-npu-a3 / run (1) | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783293) |
| extra-b-test-2-npu-a3 / run (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783298) |
| extra-b-test-2-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783330) |
| extra-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783333) |
| extra-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783337) |
| extra-b-test-1-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140265783400) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 33.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012365) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45921703844/job/140273012415) |


## [Run #45875069478](https://github.com/sgl-project/sglang/actions/runs/45875069478)
- **分支**: `npu-dsa-int8-index-kpool`
- **总耗时**: 108.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45875069478

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 22.4min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 工件，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247121957) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122036) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见退出后上传 diffusion-failures-npu-1-part0-2.zip 工件，说明用例执行出错（退出码5，unittest errors）。最可能为 setUpClass 时 sglang server 启动失败（host OOM 或进程被 SIGKILL），需查看省略段 Traceback 确认。
  - 失败用例: wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247121957

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；作业退出码 5 表示 unittest 存在 errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。已上传 diffusion-failures-npu-2-part0-2.zip 失败产物，需查看该产物中的真实错误定位。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122036

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140246275484) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140246275594) |
| multimodal-gen-test-1-npu-a3 (1) | 25.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247121907) |
| multimodal-gen-test-4-npu-a3 (1) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247121983) |
| extra-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122055) |
| extra-b-test-1-npu-a3 / run (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122131) |
| extra-b-test-16-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122153) |
| extra-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122166) |
| extra-b-test-2-npu-a3 / run (1) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122168) |
| extra-b-test-1-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122170) |
| extra-b-test-2-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122227) |
| extra-b-test-4-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140247122304) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 49.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140256054004) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 34.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140256054031) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140256054050) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140271143238) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45875069478/job/140271143259) |


---
*Auto-generated by ci_monitor.py*