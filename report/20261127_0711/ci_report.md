# NPU CI 执行监控（2026-11-26）
**生成时间**: 2026-11-27 07:11
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-26 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 29

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 347 个 | 失败 30 个 | 成功 Job 平均耗时 14.5min
- **Run 执行情况**: 成功 14 个 | 失败 15 个 | 成功 Run 平均耗时 63.8min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 74.5min | #45748580481 | [job link](https://github.com/sgl-project/sglang/actions/runs/45748580481/job/139932345277) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 52.0min | #45766139949 | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221116) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 50.8min | #45736716222 | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139646247200) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 48.4min | #45769119831 | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787761091) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 46.5min | #45614212231 | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025343) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 43.8min | #45778059563 | [job link](https://github.com/sgl-project/sglang/actions/runs/45778059563/job/139885374997) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 43.0min | #45788258359 | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139889926968) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 42.9min | #45786701465 | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912375567) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 36.7min | #45765982525 | [job link](https://github.com/sgl-project/sglang/actions/runs/45765982525/job/139742609980) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 36.6min | #45735658305 | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667603287) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 38.5min | #45792730896 | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410579) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 35.2min | #45614212231 | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025380) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 34.0min | #45792730896 | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410514) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 33.6min | #45766139949 | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221115) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | #45767404137 | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541716) |
| multimodal-gen-test-4-npu-a3 (0) | 29.5min | #45786701465 | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912369659) |
| multimodal-gen-test-4-npu-a3 (0) | 29.1min | #45792730896 | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083743) |
| multimodal-gen-test-4-npu-a3 (0) | 27.3min | #45735658305 | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667599940) |
| multimodal-gen-test-4-npu-a3 (0) | 27.2min | #45736237743 | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648802) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | #45766139949 | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730187965) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| multimodal-gen-test-4-npu-a3 (0) | 15 | 8 | 7 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083743)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912369659)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787756408)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541716)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730187965) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 32 | 27 | 3 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410514)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221115)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025380) |
| extra-b-test-4-npu-a3 / run (1) | 26 | 23 | 1 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541944) |
| extra-b-test-1-npu-a3 / run (0) | 26 | 24 | 0 | 2 | 0 | - |
| extra-b-test-1-npu-a3 / run (1) | 26 | 24 | 0 | 2 | 0 | - |
| extra-b-test-16-npu-a3 / run (0) | 21 | 19 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931291)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707909) |
| extra-b-test-4-npu-a3 / run (0) | 26 | 24 | 0 | 2 | 0 | - |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 21 | 19 | 0 | 2 | 0 | - |
| extra-b-test-2-npu-a3 / run (0) | 27 | 26 | 0 | 1 | 0 | - |
| extra-b-test-2-npu-a3 / run (1) | 27 | 26 | 0 | 1 | 0 | - |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `qwen_image_t2i_2npu` | 8 | 1 | 7 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083743)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912369659)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787756408) |
| `wan2_2_t2v_14b_w8a8_2npu` | 8 | 1 | 7 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083743)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912369659)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787756408) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 9 | 6 | 3 | [extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410514)<br>[extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221115)<br>[extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025380) |
| `npu_speculative_moe_a2a_backend.py` | 13 | 11 | 2 | [extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931291)<br>[extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707909) |
| `npu_pd_disaggregation.py` | 11 | 10 | 1 | [extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541944) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #45736237743<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 93.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45736237743) |
| #45788258359<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 92.2min | 2 | extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3, extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45788258359) |
| #45736716222<br>[#50889 [Feat] [NPU] hicache: Use kv_exchange for MHA KV and Mamba state transfers](https://github.com/sgl-project/sglang/pull/50889) | `mha_op_pr` | 86.2min | 1 | extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45736716222) |
| #45766139949<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 81.7min | 2 | multimodal-gen-test-4-npu-a3 (0), extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45766139949) |
| #45614212231<br>[#49271 [Feat] [NPU] dcp: Switch MLA and DSA to token sharding](https://github.com/sgl-project/sglang/pull/49271) | `exp/npu-dsa-token-dcp-pd` | 74.6min | 1 | extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45614212231) |
| #45792730896<br>[#51069 [Fix] [NPU] multimodal_gen: Fix LLaDA-Image support for NPU backend](https://github.com/sgl-project/sglang/pull/51069) | `llada_image` | 72.6min | 2 | multimodal-gen-test-4-npu-a3 (0), extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45792730896) |
| #45735658305<br>[#50691 [Feat] [NPU] moe: Add MegaMoE fused_op support for prefill and decode](https://github.com/sgl-project/sglang/pull/50691) | `feat/dev_megamoe` | 61.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45735658305) |
| #45767404137<br>[#46208 [Feat] [NPU] multimodal: support mm_feature_transport=npu_ipc](https://github.com/sgl-project/sglang/pull/46208) | `feat/mm-feature-transport-npu-ipc` | 40.7min | 2 | multimodal-gen-test-4-npu-a3 (0), extra-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45767404137) |
| #45818403429<br>[#38860 [Feat] [NPU] DSpark: Load the GLM-5.2 Speculators draft for static decoding on NPU](https://github.com/sgl-project/sglang/pull/38860) | `main` | 37.4min | 1 | extra-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45818403429) |
| #45786701465<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 33.8min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45786701465) |
| #45745863467<br>[#50889 [Feat] [NPU] hicache: Use kv_exchange for MHA KV and Mamba state transfers](https://github.com/sgl-project/sglang/pull/50889) | `mha_op_pr` | 27.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45745863467) |
| #45769119831<br>[#38860 [Feat] [NPU] DSpark: Load the GLM-5.2 Speculators draft for static decoding on NPU](https://github.com/sgl-project/sglang/pull/38860) | `feat/glm52-dspark-npu-upstream` | 27.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45769119831) |
| #45822504381<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 27.0min | 1 | extra-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45822504381) |
| #45817009415<br>[#53323 [Feat] [NPU] kimi-k3.1: Support DSA cache layer splitting and prefetch](https://github.com/sgl-project/sglang/pull/53323) | `feat/kimi-k31-ascend-dsa-cache-layer-split` | 8.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45817009415) |
| #45737928716<br>[#53204 [Feat] [NPU] HiCache: support DeepSeek-V4.1 L2 host offload](https://github.com/sgl-project/sglang/pull/53204) | `dsv41-a5-hicache-l2` | 5.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45737928716) |

---


## [Run #45822504381](https://github.com/sgl-project/sglang/actions/runs/45822504381)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 27.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45822504381

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 18.2min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931291) |

- **extra-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931291

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139918684820) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139918684849) |
| extra-b-test-1-npu-a3 / run (0) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931148) |
| extra-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931162) |
| extra-b-test-1-npu-a3 / run (1) | 6.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931194) |
| extra-b-test-2-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931293) |
| extra-b-test-2-npu-a3 / run (1) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931312) |
| extra-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931332) |
| extra-b-test-4-npu-a3 / run (1) | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45822504381/job/139919931417) |


## [Run #45818403429](https://github.com/sgl-project/sglang/actions/runs/45818403429)
- **分支**: `main`
- **总耗时**: 37.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45818403429

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 22.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707909) |

- **extra-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707909

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139904202326) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707419) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707508) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707534) |
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707765) |
| extra-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707937) |
| extra-b-test-1-npu-a3 / run (1) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707944) |
| extra-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707988) |
| extra-b-test-1-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905707994) |
| extra-b-test-2-npu-a3 / run (1) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905708002) |
| extra-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905708076) |
| extra-b-test-2-npu-a3 / run (0) | 24.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45818403429/job/139905708159) |


## [Run #45817009415](https://github.com/sgl-project/sglang/actions/runs/45817009415)
- **分支**: `feat/kimi-k31-ascend-dsa-cache-layer-split`
- **总耗时**: 8.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45817009415

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139907534848) |
| extra-b-test-2-npu-a3 / run (0) | 3.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139907534883) |
| extra-b-test-2-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139907534926) |
| extra-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139907535025) |
| extra-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139907535103) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139907535161) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139906283032) |
| extra-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45817009415/job/139906283109) |


## [Run #45792730896](https://github.com/sgl-project/sglang/actions/runs/45792730896)
- **分支**: `llada_image`
- **总耗时**: 72.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45792730896

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.1min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083743) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 34.0min | 环境问题 | 精度测试作业失败，日志中段被省略，无法看到真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410514) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 38.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410579) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-2.zip 失败产物，作业以非零退出码结束。结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段中的 Traceback/RuntimeError 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083743

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志仅显示artifact上传成功与清理阶段，中间测试执行部分被省略，未见Traceback。结合退出码5，推测为server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410514


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139816755050) |
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139816755106) |
| multimodal-gen-test-4-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083614) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083697) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083721) |
| extra-b-test-16-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083845) |
| extra-b-test-2-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083872) |
| extra-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083930) |
| extra-b-test-2-npu-a3 / run (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818083944) |
| extra-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818084046) |
| extra-b-test-1-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818084072) |
| extra-b-test-1-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818084076) |
| extra-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139818084080) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45792730896/job/139828410709) |


## [Run #45788258359](https://github.com/sgl-project/sglang/actions/runs/45788258359)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 92.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45788258359

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 8.6min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139912989357) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 6.9min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，多为setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139912989521) |

- **extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5对应unittest errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139912989357

- **extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（host OOM或进程被SIGKILL），需查看被省略的测试日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139912989521

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139870427216) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139870427442) |
| extra-b-test-4-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664552) |
| extra-b-test-4-npu-a3 / run (1) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664617) |
| extra-b-test-2-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664681) |
| extra-b-test-2-npu-a3 / run (1) | 25.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664723) |
| extra-b-test-16-npu-a3 / run (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664782) |
| extra-b-test-1-npu-a3 / run (1) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664789) |
| extra-b-test-1-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664848) |
| extra-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139871664893) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 43.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139889926968) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139889927133) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45788258359/job/139889927214) |


## [Run #45786701465](https://github.com/sgl-project/sglang/actions/runs/45786701465)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 33.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45786701465

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.5min | 环境问题 | 日志中未见真实错误，仅显示测试失败产物上传，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912369659) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，仅见 artifact diffusion-failures-npu-2-part0-3.zip 上传成功，无 Traceback/RuntimeError 等真实错误信息。按退出码 5 推断为 unittest errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看完整日志确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912369659

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-4-npu-a3 (1) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912371447) |
| extra-b-test-1-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912371448) |
| multimodal-gen-test-1-npu-a3 (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912371638) |
| extra-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912371650) |
| extra-b-test-2-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912371860) |
| extra-b-test-1-npu-a3 / run (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912372362) |
| extra-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912372566) |
| multimodal-gen-test-1-npu-a3 (1) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912372989) |
| extra-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912373013) |
| extra-b-test-2-npu-a3 / run (1) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912373034) |
| extra-b-test-4-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912373682) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912375133) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 42.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912375567) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912376060) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912376577) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912378064) |
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912428097) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45786701465/job/139912451529) |


## [Run #45769119831](https://github.com/sgl-project/sglang/actions/runs/45769119831)
- **分支**: `feat/glm52-dspark-npu-upstream`
- **总耗时**: 27.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45769119831

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 26.4min | 其他 | 多模态生成测试失败，失败产物已上传，但日志省略了真实错误信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787756408) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业退出码5表示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。日志中间部分被省略，未显示Traceback，需查看上传的diffusion-failures-npu-2-part0-3.zip或完整日志确认具体异常。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787756408

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787757979) |
| extra-b-test-2-npu-a3 / run (1) | 27.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758033) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758171) |
| multimodal-gen-test-4-npu-a3 (1) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758267) |
| multimodal-gen-test-1-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758347) |
| extra-b-test-2-npu-a3 / run (0) | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758386) |
| multimodal-gen-test-1-npu-a3 (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758418) |
| extra-b-test-1-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758505) |
| extra-b-test-16-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758534) |
| extra-b-test-1-npu-a3 / run (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758535) |
| extra-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787758679) |
| extra-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787760285) |
| extra-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787760289) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 48.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787761091) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787761482) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787762515) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787763563) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45769119831/job/139787763615) |


## [Run #45767404137](https://github.com/sgl-project/sglang/actions/runs/45767404137)
- **分支**: `feat/mm-feature-transport-npu-ipc`
- **总耗时**: 40.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45767404137

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | 其他 | 日志中未见明确错误，仅显示测试失败产物上传及清理，无法定位具体原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541716) |
| extra-b-test-4-npu-a3 / run (1) | 9.6min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541944) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，仅见 artifact diffusion-failures-npu-2-part0-2.zip 上传成功及 post job cleanup，无 Traceback/RuntimeError 等真实错误信息，无法判断失败根因，需查看完整日志确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541716

- **extra-b-test-4-npu-a3 / run (1)**: 日志中段省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（OOM/SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541944

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139732565420) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139732565448) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541690) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541713) |
| multimodal-gen-test-4-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541750) |
| extra-b-test-1-npu-a3 / run (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541814) |
| extra-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541834) |
| extra-b-test-1-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541863) |
| extra-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541880) |
| extra-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541896) |
| extra-b-test-8-npu-a3 / run (0) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541919) |
| extra-b-test-2-npu-a3 / run (1) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45767404137/job/139733541938) |


## [Run #45766139949](https://github.com/sgl-project/sglang/actions/runs/45766139949)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 81.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45766139949

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | 环境问题 | 日志中未见明确错误，但作业以退出码5失败，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730187965) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 33.6min | 环境问题 | 精度测试作业失败，日志末尾仅显示清理与上传产物，未包含真实错误信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221115) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示artifact上传成功和清理过程，省略部分可能包含真实错误。退出码5表示unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志中的Traceback确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730187965

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志被截断，仅见 artifact 上传成功与 post job cleanup，无 Traceback/RuntimeError。按背景，退出码5多为 setUpClass 阶段 sglang server 启动失败（host OOM 或进程被 SIGKILL），需查看被省略的中间日志确认。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221115

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139729416656) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139729416688) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730187940) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730187944) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188045) |
| extra-b-test-1-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188083) |
| extra-b-test-16-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188106) |
| extra-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188115) |
| extra-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188116) |
| extra-b-test-1-npu-a3 / run (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188122) |
| extra-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188144) |
| extra-b-test-2-npu-a3 / run (1) | 25.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188195) |
| extra-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139730188220) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221096) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 52.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45766139949/job/139740221116) |


## [Run #45745863467](https://github.com/sgl-project/sglang/actions/runs/45745863467)
- **分支**: `mha_op_pr`
- **总耗时**: 27.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45745863467

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139684948066) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139684948123) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139684948156) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-b-test-2-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139676999207) |
| extra-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139676999726) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000140) |
| extra-b-test-16-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000183) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000311) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000347) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000375) |
| extra-b-test-2-npu-a3 / run (1) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000419) |
| extra-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000454) |
| extra-b-test-1-npu-a3 / run (1) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000633) |
| extra-b-test-1-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677000691) |
| extra-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45745863467/job/139677002082) |


## [Run #45737928716](https://github.com/sgl-project/sglang/actions/runs/45737928716)
- **分支**: `dsv41-a5-hicache-l2`
- **总耗时**: 5.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45737928716

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45737928716/job/139642429141) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45737928716/job/139642429145) |
| extra-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45737928716/job/139642429162) |
| extra-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45737928716/job/139642429221) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45737928716/job/139641394289) |
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45737928716/job/139641394310) |


## [Run #45736716222](https://github.com/sgl-project/sglang/actions/runs/45736716222)
- **分支**: `mha_op_pr`
- **总耗时**: 86.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45736716222

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 2.3min | 环境问题 | 测试日志未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139664590554) |

- **extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3**: 日志显示 /tmp/test-logs/*.log 未找到，无产物上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），但日志中未见具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139664590554

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139635224309) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139635224319) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326189) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326271) |
| extra-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326316) |
| extra-b-test-4-npu-a3 / run (1) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326334) |
| extra-b-test-2-npu-a3 / run (1) | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326363) |
| extra-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326377) |
| extra-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326382) |
| extra-b-test-1-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326422) |
| extra-b-test-1-npu-a3 / run (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326430) |
| extra-b-test-16-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139636326506) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 50.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139646247200) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 34.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139646247257) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736716222/job/139646247294) |


## [Run #45736237743](https://github.com/sgl-project/sglang/actions/runs/45736237743)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 93.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45736237743

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.2min | 环境问题 | 日志中未见明确错误，但作业以退出码5失败，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648802) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志省略了中间关键部分，仅显示artifact上传成功和清理过程，无Traceback。退出码5表明unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648802

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139633586724) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139633586726) |
| multimodal-gen-test-4-npu-a3 (1) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648517) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648554) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648616) |
| extra-b-test-16-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648785) |
| extra-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648801) |
| extra-b-test-1-npu-a3 / run (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648870) |
| extra-b-test-2-npu-a3 / run (1) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648932) |
| extra-b-test-1-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648955) |
| extra-b-test-2-npu-a3 / run (0) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648978) |
| extra-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634648990) |
| extra-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139634649033) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139645534521) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139645534540) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139645534549) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45736237743/job/139657222769) |


## [Run #45735658305](https://github.com/sgl-project/sglang/actions/runs/45735658305)
- **分支**: `feat/dev_megamoe`
- **总耗时**: 61.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45735658305

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.3min | 其他 | 日志被截断，缺少真实错误信息，无法确定失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667599940) |

- **multimodal-gen-test-4-npu-a3 (0)**: 可见日志仅含 runner 初始化、artifact 上传（diffusion-failures-npu-2-part0-3.zip）和清理阶段，中间省略部分包含实际测试输出。退出码 5 提示 unittest 存在 errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），但需查看完整日志中的 Traceback/RuntimeError 才能确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667599940

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667600709) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667601041) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 36.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667601753) |
| extra-b-test-2-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667601794) |
| extra-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667601846) |
| extra-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667601880) |
| extra-b-test-4-npu-a3 / run (1) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667601956) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602091) |
| extra-b-test-2-npu-a3 / run (1) | 28.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602132) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602135) |
| extra-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602198) |
| extra-b-test-1-npu-a3 / run (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602253) |
| extra-b-test-16-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602299) |
| multimodal-gen-test-1-npu-a3 (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667602527) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 36.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667603287) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139667603833) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45735658305/job/139680441926) |


## [Run #45614212231](https://github.com/sgl-project/sglang/actions/runs/45614212231)
- **分支**: `exp/npu-dsa-token-dcp-pd`
- **总耗时**: 74.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45614212231

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 35.2min | 环境问题 | 精度测试作业失败，日志末尾仅显示清理与上传产物，未包含真实错误信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025380) |

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志被截断，中间省略部分未显示 Traceback/RuntimeError。作业在 03:04 完成产物上传与清理，退出码 5 提示 unittest 存在 errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段真实错误确认。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025380

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139641293949) |
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139641293961) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235222) |
| multimodal-gen-test-4-npu-a3 (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235236) |
| extra-b-test-8-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235264) |
| extra-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235308) |
| extra-b-test-4-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235315) |
| extra-b-test-16-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235322) |
| extra-b-test-2-npu-a3 / run (1) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235333) |
| extra-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235350) |
| extra-b-test-1-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235362) |
| extra-b-test-1-npu-a3 / run (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139642235490) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 46.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025343) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45614212231/job/139651025491) |


---
*Auto-generated by ci_monitor.py*