# NPU CI 执行监控（2026-11-17）
**生成时间**: 2026-11-18 07:15
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-17 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 129

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1250 个 | 失败 129 个 | 成功 Job 平均耗时 13.2min
- **Run 执行情况**: 成功 65 个 | 失败 64 个 | 成功 Run 平均耗时 42.8min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-4-npu-a3 / run (0) | 61.7min | #44081864554 | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828300) |
| base-b-test-2-npu-a3 / run (0) | 54.8min | #44081864554 | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828393) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.4min | #44028916033 | [job link](https://github.com/sgl-project/sglang/actions/runs/44028916033/job/133917488996) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.3min | #44043441586 | [job link](https://github.com/sgl-project/sglang/actions/runs/44043441586/job/133915358224) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 42.9min | #44029416167 | [job link](https://github.com/sgl-project/sglang/actions/runs/44029416167/job/133904598729) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 38.9min | #44042283129 | [job link](https://github.com/sgl-project/sglang/actions/runs/44042283129/job/133913933127) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.5min | #43984101253 | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133720281913) |
| multimodal-gen-test-4-npu-a3 (0) | 37.1min | #44050275639 | [job link](https://github.com/sgl-project/sglang/actions/runs/44050275639/job/134015683465) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 36.5min | #43830929475 | [job link](https://github.com/sgl-project/sglang/actions/runs/43830929475/job/133807299967) |
| multimodal-gen-test-4-npu-a3 (1) | 35.6min | #43914629484 | [job link](https://github.com/sgl-project/sglang/actions/runs/43914629484/job/133876855500) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 63.9min | #44085201225 | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939625) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.4min | #43826899517 | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133949520792) |
| multimodal-gen-test-4-npu-a3 (0) | 40.9min | #43922134264 | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846666) |
| multimodal-gen-test-4-npu-a3 (0) | 38.8min | #43948457441 | [job link](https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133585373740) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | #43981642271 | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864689) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | #44003014857 | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505735) |
| multimodal-gen-test-4-npu-a3 (0) | 32.8min | #43999080357 | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328443) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | #43988491778 | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724301981) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | #43984099422 | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026872) |
| multimodal-gen-test-4-npu-a3 (0) | 31.3min | #44005297833 | [job link](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873940) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| multimodal-gen-test-4-npu-a3 (0) | 100 | 64 | 29 | 0 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939625)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291623)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599873)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133781160543)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873940) |
| base-b-test-16-npu-a3 / run (0) | 81 | 66 | 8 | 2 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115138197)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939829)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921692)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156762)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394315) |
| base-b-test-8-npu-a3 / run (0) | 82 | 73 | 4 | 2 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586568)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864260)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830358)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989430) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 56 | 47 | 5 | 0 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44089466660/job/134066843582)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133856312520)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133771644330)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133623090457)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133949520792) |
| base-b-test-1-npu-a3 / run (0) | 91 | 80 | 3 | 1 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828374)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718083)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054380) |
| base-b-test-4-npu-a3 / run (1) | 91 | 83 | 3 | 1 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162120)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998408)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054752) |
| base-b-test-4-npu-a3 / run (0) | 91 | 81 | 3 | 1 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133909219408)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591531)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850304) |
| base-b-test-2-npu-a3 / run (0) | 94 | 83 | 2 | 1 | 8 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748482)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054546) |
| multimodal-gen-test-1-npu-a3 (1) | 67 | 62 | 1 | 0 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628306972) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 108 | 103 | 1 | 0 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133525648729) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `qwen_image_t2i_2npu` | 42 | 10 | 32 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825717851)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291623)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599873) |
| `npu_pd_disaggregation.py` | 52 | 47 | 5 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133909219408)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162120)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850304) |
| `npu_speculative_moe_a2a_backend.py` | 43 | 40 | 3 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115138197)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921692)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021436) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 49 | 46 | 3 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864260)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830358)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989430) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 24 | 21 | 3 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133856312520)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133771644330)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133623090457) |
| `minimax_h3_t2va_2npu` | 38 | 37 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939625) |
| `npu_return_indexer_topk_deepseek_v4.py` | 45 | 44 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054546) |
| `ernie_image_t2i_1npu` | 41 | 40 | 1 | [multimodal-gen-test-1-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470400) |
| `npu_sampling_backend.py` | 46 | 45 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828374) |
| `ltx_2_ti2va_2npu` | 37 | 36 | 1 | [multimodal-gen-test-4-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328460) |
| `npu_dsv4_hicache_l2_pool.py` | 29 | 28 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054380) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 26 | 25 | 1 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133525648729) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43891721088<br>[#50803 [Refactor] srt: Fix silent failures and prune dead code in the runtime core (1/4)](https://github.com/sgl-project/sglang/pull/50803) | `bbuf/cleanup4-srt-core` | 85.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43891721088) |
| #43984101253 | `dark/eagle-fused-draft-sample` | 83.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43984101253) |
| #44003014857<br>[#47588 [Feat] sail: support DeepGEMM GEMM/MoE backends [4/N]](https://github.com/sgl-project/sglang/pull/47588) | `ywj/upstream_deepgemm_split` | 83.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44003014857) |
| #43826899517<br>[#49068 [Perf] dsv41-flash: Reuse paged Indexer key tiles during verification](https://github.com/sgl-project/sglang/pull/49068) | `v4.1/h20-verify-k-reuse` | 83.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43826899517) |
| #43936732666<br>[#50707 [Feat] [AMD] muse-spark: Add gfx1250 support](https://github.com/sgl-project/sglang/pull/50707) | `pr/muse-gfx1250` | 82.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43936732666) |
| #43984099422 | `dark/dflash2-fused-select` | 81.9min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43984099422) |
| #43978624685<br>[#42103 [Feat] weights: Add native ModelExpress weight transfer backend support](https://github.com/sgl-project/sglang/pull/42103) | `hwoo/delta-recipes-sglang` | 80.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43978624685) |
| #43988491778<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 80.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43988491778) |
| #44005749755<br>[#50803 [Refactor] srt: Fix silent failures and prune dead code in the runtime core (1/4)](https://github.com/sgl-project/sglang/pull/50803) | `bbuf/cleanup4-srt-core` | 79.8min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44005749755) |
| #43941300510<br>[#46210 [Feat] [NVIDIA] megakernels: DSA / MLA binding view, EAGLE draft capture checks, early draft embedding sharing](https://github.com/sgl-project/sglang/pull/46210) | `megakernel-dsa-view-draft-capture` | 78.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43941300510) |
| #43999080357<br>[#50032 [Perf] scheduler: Cut per-step host work in the batch-1 speculative decode loop](https://github.com/sgl-project/sglang/pull/50032) | `spec-batch1-host-loop` | 76.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43999080357) |
| #43922134264<br>[#49571 [Feat] flashinfer: Add opt-in scoped caching for single-rank decode graphs](https://github.com/sgl-project/sglang/pull/49571) | `feat/flashinfer-scoped-graph-cache` | 75.9min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43922134264) |
| #43909957963<br>[#50707 [Feat] [AMD] muse-spark: Add gfx1250 support](https://github.com/sgl-project/sglang/pull/50707) | `pr/muse-gfx1250` | 75.9min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43909957963) |
| #44006553438<br>[#50906 [Feat] glm5_next: Support LayerNorm sequence parallelism](https://github.com/sgl-project/sglang/pull/50906) | `perf/glm5-next-layernorm-sp` | 75.7min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44006553438) |
| #43908980485<br>[#49571 [Feat] flashinfer: Add opt-in scoped caching for single-rank decode graphs](https://github.com/sgl-project/sglang/pull/49571) | `feat/flashinfer-scoped-graph-cache` | 73.9min | 2 | multimodal-gen-test-4-npu-a3 (0), base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43908980485) |
| #43991150360<br>[#50707 [Feat] [AMD] muse-spark: Add gfx1250 support](https://github.com/sgl-project/sglang/pull/50707) | `pr/muse-gfx1250` | 73.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43991150360) |
| #43948364364<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 72.1min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43948364364) |
| #44085201225<br>[#49995 [Refactor] [NPU] operators: Migrate sgl-kernel-npu calls to public operators entry points](https://github.com/sgl-project/sglang/pull/49995) | `sgl-kernel-npu-refactor` | 70.7min | 2 | multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44085201225) |
| #44081864554<br>[#47052 [Perf] [AMD] qwen3: Fuse prefill QK-norm + RoPE on ROCm with the JIT qknorm_rope kernel](https://github.com/sgl-project/sglang/pull/47052) | `main` | 68.8min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44081864554) |
| #43927224247<br>[#46935 [Fix] hicache: Look up L3 below a device-only anchor under write-back](https://github.com/sgl-project/sglang/pull/46935) | `hicache-write-back-storage-lookup` | 59.4min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43927224247) |
| #43889940777<br>[#50804 [Refactor] models: Fix silent failures and prune dead code in srt models and layers (2/4)](https://github.com/sgl-project/sglang/pull/50804) | `bbuf/cleanup4-srt-models-layers` | 58.9min | 3 | multimodal-gen-test-4-npu-a3 (0), base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43889940777) |
| #43954451169<br>[#50853 [Feat] disaggregation: Report a full decode host pool and landed host-staged transfers in /v1/loads](https://github.com/sgl-project/sglang/pull/50853) | `oss-sync-637b260a19` | 52.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43954451169) |
| #43981642271<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 50.4min | 2 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43981642271) |
| #43992226690<br>[#46063 [Fix] scheduler: Reserve encoder-replay rows in the shortest-prefill-first chunk reservation](https://github.com/sgl-project/sglang/pull/46063) | `agentx/spf-replay-reserve` | 48.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43992226690) |
| #43999069533<br>[#50471 [Perf] dsv41: Share Engram tables across servers with replication group_shards](https://github.com/sgl-project/sglang/pull/50471) | `engram-group-shards` | 44.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43999069533) |
| #44026123919<br>[#48899 [Feat] hisparse: support DFLASH speculative decoding](https://github.com/sgl-project/sglang/pull/48899) | `pr/hisparse-dflash2` | 42.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44026123919) |
| #43948457441<br>[#40856 [Perf] [NPU] sensenova: Fuse rotary position embeddings](https://github.com/sgl-project/sglang/pull/40856) | `sensenova-bf16-rope-npu-main` | 42.0min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43948457441) |
| #44019331522<br>[#47588 [Feat] sail: support DeepGEMM GEMM/MoE backends [4/N]](https://github.com/sgl-project/sglang/pull/47588) | `ywj/upstream_deepgemm_split` | 37.3min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44019331522) |
| #43889954943<br>[#50805 [Refactor] kernels: Fix silent failures and prune dead code in the kernels package (3/4)](https://github.com/sgl-project/sglang/pull/50805) | `bbuf/cleanup4-kernels` | 36.2min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43889954943) |
| #44037240836<br>[#50150 [Feat] platforms: Let OOT platforms provide breakable graph backends (3/3)](https://github.com/sgl-project/sglang/pull/50150) | `refactor/graph-break-recorder` | 36.1min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44037240836) |
| #44005297833<br>[#47756 [Fix] [AMD] diffusion: install amd-smi so FLUX.3 serves on ROCm on gfx1151](https://github.com/sgl-project/sglang/pull/47756) | `vvvdwbvvv/enabling-aiter-on-sgl-diffusion-gfx1151` | 34.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44005297833) |
| #44003647941<br>[#44349 [Feat] beam-search: Add trie head and shared-context attention](https://github.com/sgl-project/sglang/pull/44349) | `feat/trie-head-shared-attention` | 34.5min | 2 | base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44003647941) |
| #43941077287<br>[#48579 [Perf] io_struct: Validate an input_embeds body against one union member](https://github.com/sgl-project/sglang/pull/48579) | `perf/input-embeds-one-union-member` | 34.4min | 2 | multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43941077287) |
| #44019941085<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 34.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44019941085) |
| #43895367887<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 33.9min | 4 | multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43895367887) |
| #44017873452 | `rainj-me/rust-apis-09-logging-dumper-l3-elastic` | 33.6min | 3 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44017873452) |
| #44017869551 | `rainj-me/rust-apis-02-pause-and-frontend-state` | 33.5min | 3 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44017869551) |
| #43960748144<br>[#48767 [Perf] [AMD] diffusion: Mount the Wan FFN linear+GELU site on gfx1250 with a bit-exact GELU](https://github.com/sgl-project/sglang/pull/48767) | `amd/wan22-gfx1250-gelu` | 32.8min | 2 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43960748144) |
| #44005719585<br>[#46029 [Feat] [NPU] diffusion: Integrate MindIE-SD quantized attention into Ascend FA](https://github.com/sgl-project/sglang/pull/46029) | `feat/ascend-quant-fa` | 31.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44005719585) |
| #44049442789<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 31.4min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44049442789) |
| #43990429766<br>[#50804 [Refactor] models: Fix silent failures and prune dead code in srt models and layers (2/4)](https://github.com/sgl-project/sglang/pull/50804) | `bbuf/cleanup4-srt-models-layers` | 30.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43990429766) |
| #43933670349<br>[#45560 [elastic ep] live serving during scale](https://github.com/sgl-project/sglang/pull/45560) | `qkang/elastic-ep-mooncake-scale-down` | 29.3min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43933670349) |
| #43985882217<br>[#50806 [Refactor] diffusion: Fix silent failures and prune dead code in multimodal_gen (4/4)](https://github.com/sgl-project/sglang/pull/50806) | `bbuf/cleanup4-diffusion` | 29.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43985882217) |
| #44021828389<br>[#49735 [Feat] rust-server: Pause and continue generation, freeze_gc, ping and ready, and the frontend state](https://github.com/sgl-project/sglang/pull/49735) | `rainj-me/rust-apis-02-pause-and-frontend-state` | 27.1min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44021828389) |
| #43955528880<br>[#48700 [Fix] [AMD] aiter: Reserve the decode workspace in the automatic mem_fraction_static](https://github.com/sgl-project/sglang/pull/48700) | `ci-fix/amd-aiter-workspace-reserve` | 26.8min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43955528880) |
| #44000700148 | `amd/gfx942-aiter-mhc` | 26.7min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44000700148) |
| #43883325871<br>[#50228 [Perf] [NVIDIA] gemma4: run the fused all-reduce sites for decode batches inside the decode CUDA graphs](https://github.com/sgl-project/sglang/pull/50228) | `gemma4-ar-fusion-decode` | 26.6min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43883325871) |
| #44031517530<br>[#50228 [Perf] [NVIDIA] gemma4: run the fused all-reduce sites for decode batches inside the decode CUDA graphs](https://github.com/sgl-project/sglang/pull/50228) | `gemma4-ar-fusion-decode` | 26.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44031517530) |
| #44022875351<br>[#50196 [Perf] [AMD] mhc: Enable AITER mHC kernels on gfx942](https://github.com/sgl-project/sglang/pull/50196) | `amd/gfx942-aiter-mhc` | 25.9min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44022875351) |
| #43889969273<br>[#50806 [Refactor] diffusion: Fix silent failures and prune dead code in multimodal_gen (4/4)](https://github.com/sgl-project/sglang/pull/50806) | `bbuf/cleanup4-diffusion` | 25.4min | 1 | multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43889969273) |
| #44091370604<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 24.8min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44091370604) |
| #43973051402<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 24.8min | 2 | multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43973051402) |
| #44033200138<br>[#46190 [Feat] spec: confidence-scheduled compact verify for DFLASH](https://github.com/sgl-project/sglang/pull/46190) | `codex/av-7` | 24.4min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44033200138) |
| #43978177116<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 24.4min | 3 | multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43978177116) |
| #44007696764<br>[#36591 [Fix] hisparse: state-preserving retraction and recovery for DSV4](https://github.com/sgl-project/sglang/pull/36591) | `fix/hisparse-cpu-copy-retraction` | 18.7min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44007696764) |
| #44042962705<br>[#50968 [Feat] [NPU] glm5: Support PD disaggregation for DSA kpool tail buffer](https://github.com/sgl-project/sglang/pull/50968) | `glm53flash-pd` | 17.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44042962705) |
| #44035712083 | `feat/qsa-cache-sharding` | 17.2min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44035712083) |
| #44041975737<br>[#50883 [Feat] gc: Add idle freeze and checks for heap growth and frozen garbage](https://github.com/sgl-project/sglang/pull/50883) | `lsyin/gc-freeze-on-idle` | 16.5min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44041975737) |
| #43999991933<br>[#50518 [Fix] tokenizer_manager: Stop the schedulers only after every tokenizer worker drains](https://github.com/sgl-project/sglang/pull/50518) | `multi-tokenizer-graceful-drain` | 10.7min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43999991933) |
| #43976802741<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 9.7min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43976802741) |
| #43991076949<br>[#46063 [Fix] scheduler: Reserve encoder-replay rows in the shortest-prefill-first chunk reservation](https://github.com/sgl-project/sglang/pull/46063) | `agentx/spf-replay-reserve` | 9.2min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43991076949) |
| #44038600385<br>[#48414 [Feat] kimi_k3: Merge the rest of the Kimi-K3.1 Day-0 branch](https://github.com/sgl-project/sglang/pull/48414) | `kimi-k3.1-day-0` | 8.2min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44038600385) |
| #44089466660<br>[#51017 [Fix] [NPU] dsa: Preserve global DSA top-k for MTP seed export](https://github.com/sgl-project/sglang/pull/51017) | `fix-q-shard-mtp` | 6.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44089466660) |
| #43935911666 | `pr/muse-gfx1250` | 5.0min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43935911666) |

---


## [Run #44091370604](https://github.com/sgl-project/sglang/actions/runs/44091370604)
- **分支**: `clearing_console_output`
- **总耗时**: 24.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44091370604

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 23.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115138197) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115138197

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115138679) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115138730) |
| multimodal-gen-test-4-npu-a3 (0) | 28.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115140061) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115140507) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115140538) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115140591) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115140943) |
| multimodal-gen-test-4-npu-a3 (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115141013) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115142146) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115142914) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44091370604/job/134115143441) |


## [Run #44089466660](https://github.com/sgl-project/sglang/actions/runs/44089466660)
- **分支**: `fix-q-shard-mtp`
- **总耗时**: 6.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44089466660

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.2min | 其他 | 日志被截断，缺少实际测试执行与错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44089466660/job/134066843582) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 可见日志仅包含 runner 初始化、action 下载、artifact 上传（425字节）和清理阶段，中间省略部分未提供。无 Traceback/RuntimeError/退出码等关键信息，无法判断是否为 setUpClass 启动失败或其他问题，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44089466660/job/134066843582

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089466660/job/134065198725) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089466660/job/134065198737) |


## [Run #44085201225](https://github.com/sgl-project/sglang/actions/runs/44085201225)
- **分支**: `sgl-kernel-npu-refactor`
- **总耗时**: 70.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44085201225

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 63.9min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939625) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939829) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；作业退出码 5 对应 unittest errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。已上传 diffusion-failures-npu-2-part0-2.zip 产物，需查看该产物中的真实错误定位。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939625

- **base-b-test-16-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，多为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939829

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134047668998) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134047669246) |
| multimodal-gen-test-1-npu-a3 (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939540) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939575) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939791) |
| base-b-test-4-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939884) |
| base-b-test-4-npu-a3 / run (1) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939896) |
| base-b-test-1-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939905) |
| base-b-test-2-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048939974) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44085201225/job/134048940194) |


## [Run #44081864554](https://github.com/sgl-project/sglang/actions/runs/44081864554)
- **分支**: `main`
- **总耗时**: 68.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44081864554

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 13.6min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828374) |

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，未见Traceback/RuntimeError等真实错误；仅见artifact上传成功和Node.js弃用警告。退出码5表明unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828374

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134034421912) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828151) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828281) |
| base-b-test-16-npu-a3 / run (0) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828293) |
| base-b-test-4-npu-a3 / run (0) | 61.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828300) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828311) |
| base-b-test-8-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828370) |
| base-b-test-2-npu-a3 / run (0) | 54.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828393) |
| multimodal-gen-test-4-npu-a3 (0) | 28.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828410) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081864554/job/134035828413) |


## [Run #44049442789](https://github.com/sgl-project/sglang/actions/runs/44049442789)
- **分支**: `clearing_console_output`
- **总耗时**: 31.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44049442789

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 23.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921692) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921692

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134016567643) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134016567853) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921332) |
| multimodal-gen-test-4-npu-a3 (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921365) |
| multimodal-gen-test-4-npu-a3 (0) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921395) |
| base-b-test-2-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921490) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921526) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921615) |
| multimodal-gen-test-1-npu-a3 (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921653) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921715) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44049442789/job/134017921753) |


## [Run #44042962705](https://github.com/sgl-project/sglang/actions/runs/44042962705)
- **分支**: `glm53flash-pd`
- **总耗时**: 17.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44042962705

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 14.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133909219408) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133909219408

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133908216945) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133908217011) |
| base-b-test-4-npu-a3 / run (1) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44042962705/job/133909219367) |


## [Run #44041975737](https://github.com/sgl-project/sglang/actions/runs/44041975737)
- **分支**: `lsyin/gc-freeze-on-idle`
- **总耗时**: 16.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44041975737

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 13.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637089) |
| base-b-test-1-npu-a3 / run (0) | 13.3min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示产物上传成功和清理过程，无法定位具体错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637106) |
| base-b-test-4-npu-a3 / run (0) | 13.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637130) |
| base-b-test-2-npu-a3 / run (0) | 13.1min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637473) |

- **base-b-test-16-npu-a3 / run (0)**: 日志中段省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637089

- **base-b-test-1-npu-a3 / run (0)**: 日志中省略了中间测试执行部分，可见内容只有 runner 初始化、下载 action、上传 artifact 和 post job cleanup，没有 Traceback/RuntimeError 或退出码 5 的相关记录，需查看完整日志确认 setUpClass 阶段 server 启动失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637106

- **base-b-test-4-npu-a3 / run (0)**: 日志仅显示artifact上传和清理，无Traceback。退出码5表示unittest有errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637130

- **base-b-test-2-npu-a3 / run (0)**: 作业以退出码5结束，表明unittest存在errors，常见于setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。日志中段被省略，未显示Traceback/RuntimeError，需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637473

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133898623708) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133898623735) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899636977) |
| multimodal-gen-test-4-npu-a3 (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637023) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637068) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44041975737/job/133899637082) |


## [Run #44038600385](https://github.com/sgl-project/sglang/actions/runs/44038600385)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 8.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44038600385

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 2.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586369) |
| multimodal-gen-test-1-npu-a3 (0) | 4.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586386) |
| multimodal-gen-test-1-npu-a3 (1) | 2.0min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586408) |
| multimodal-gen-test-4-npu-a3 (1) | 4.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586465) |
| base-b-test-8-npu-a3 / run (0) | 2.8min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586568) |
| base-b-test-4-npu-a3 / run (0) | 4.9min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586580) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586584) |
| base-b-test-16-npu-a3 / run (0) | 4.8min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586593) |
| base-b-test-1-npu-a3 / run (0) | 4.9min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586596) |
| base-b-test-4-npu-a3 / run (1) | 4.8min | 环境问题 | 日志中未见明确错误，但用例退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586601) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业在约2分钟内结束，未找到 diffusion-failures/ 目录产物，说明测试用例在 setUpClass 阶段即报错（退出码5对应 FAILED (errors=N)），最常见原因是 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志中未见具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586369


- **multimodal-gen-test-1-npu-a3 (1)**: 日志仅包含 runner 初始化、action 下载和清理过程，未出现测试脚本输出或 Traceback；upload-artifact 提示 diffusion-failures/ 路径无文件，说明测试阶段未产生预期产物，作业在无实际用例执行的情况下结束，疑似环境或前置步骤异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586408


- **base-b-test-8-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586568

- **base-b-test-4-npu-a3 / run (0)**: 日志中段被省略，未见Traceback/RuntimeError。退出码5表示unittest有errors，常见于setUpClass时server启动失败（如host OOM、进程被SIGKILL）。需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586580

- **base-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，最可能是setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586584

- **base-b-test-16-npu-a3 / run (0)**: 日志仅显示artifact上传和清理阶段，缺少测试执行与Traceback内容，无法定位具体异常；按背景知识，退出码5多为setUpClass中server启动失败，需查看完整日志确认OOM/SIGKILL等真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586593

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，常见于setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586596

- **base-b-test-4-npu-a3 / run (1)**: 日志被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（host OOM/被SIGKILL），需查看省略段真实异常确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133888586601

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133887603682) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44038600385/job/133887603809) |


## [Run #44037240836](https://github.com/sgl-project/sglang/actions/runs/44037240836)
- **分支**: `refactor/graph-break-recorder`
- **总耗时**: 36.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44037240836

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.4min | 环境问题 | 日志中未见测试执行错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156762) |

- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 323 字节 artifact 及 post job cleanup，无 Traceback/RuntimeError。退出码 5 对应 unittest errors，通常为 setUpClass 中 sglang server 启动失败（host OOM 或进程被 SIGKILL），但具体错误在被省略的中间日志中，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156762

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133883160531) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133883160615) |
| multimodal-gen-test-4-npu-a3 (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156166) |
| multimodal-gen-test-1-npu-a3 (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156320) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156337) |
| multimodal-gen-test-4-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156382) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156592) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156664) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156814) |
| base-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156860) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44037240836/job/133884156890) |


## [Run #44035712083](https://github.com/sgl-project/sglang/actions/runs/44035712083)
- **分支**: `feat/qsa-cache-sharding`
- **总耗时**: 17.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44035712083

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 11.4min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303163) |
| multimodal-gen-test-1-npu-a3 (1) | 9.6min | 其他 | 日志被截断，缺少真实错误信息，无法确定失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303189) |
| multimodal-gen-test-4-npu-a3 (0) | 9.5min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303194) |
| base-b-test-8-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303244) |
| multimodal-gen-test-4-npu-a3 (1) | 3.9min | 环境问题 | diffusion 测试失败且未生成失败产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303248) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303367) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303370) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303431) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303434) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303448) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，未见具体 Traceback；但作业上传了 diffusion-failures-npu-1-part0-1.zip 失败产物，且用例退出码 5 通常对应 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。需查看省略段确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303163

- **multimodal-gen-test-1-npu-a3 (1)**: 可见日志仅为 runner 初始化、artifact 上传（diffusion-failures-npu-1-part1-1.zip）和清理阶段，中间省略部分未包含 Traceback/RuntimeError 等真实错误，也无退出码 5 的上下文，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303189

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业退出并上传 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例运行出错（退出码5，unittest errors），常见原因为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志省略部分未显示具体 Traceback，需查看上传的失败产物确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303194


- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试用例执行失败但未产出失败文件；结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133879303248






### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133878165280) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44035712083/job/133878165288) |


## [Run #44033200138](https://github.com/sgl-project/sglang/actions/runs/44033200138)
- **分支**: `codex/av-7`
- **总耗时**: 24.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44033200138

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 4.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864260) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864260

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133869932440) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133869932499) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864125) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864208) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864222) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864226) |
| base-b-test-1-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864251) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864331) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44033200138/job/133870864339) |


## [Run #44031517530](https://github.com/sgl-project/sglang/actions/runs/44031517530)
- **分支**: `gemma4-ar-fusion-decode`
- **总耗时**: 26.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44031517530

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 7.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591442) |
| base-b-test-4-npu-a3 / run (0) | 4.3min | 环境问题 | 日志中未见明确错误，但用例退出码5提示setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591531) |


- **base-b-test-4-npu-a3 / run (0)**: 日志被截断，仅见artifact上传与清理，无Traceback。按退出码5推断为setUpClass阶段server启动失败（如host OOM或进程被SIGKILL），属环境问题，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591531

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133864534332) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133864534430) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591312) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591388) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591481) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591532) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591536) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44031517530/job/133865591588) |


## [Run #44026123919](https://github.com/sgl-project/sglang/actions/runs/44026123919)
- **分支**: `pr/hisparse-dflash2`
- **总耗时**: 42.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44026123919

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133856312520) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133856312520

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133846974660) |
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133846974679) |
| multimodal-gen-test-4-npu-a3 (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848066979) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848066990) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848067086) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848067114) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848067130) |
| base-b-test-4-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848067191) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848067197) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133848067259) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133856312396) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44026123919/job/133856312427) |


## [Run #44022875351](https://github.com/sgl-project/sglang/actions/runs/44022875351)
- **分支**: `amd/gfx942-aiter-mhc`
- **总耗时**: 25.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44022875351

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.8min | 环境问题 | 日志中未见测试执行错误，作业在 artifact 上传后正常清理，失败原因需结合省略部分确认 | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394315) |

- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅显示 checkout、artifact 上传（323字节）和 post job cleanup，无 Traceback 或退出码5的报错信息；省略部分可能含 setUpClass 阶段 server 启动失败（如 host OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394315

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133836341985) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133836342365) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394144) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394150) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394236) |
| base-b-test-1-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394288) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394291) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394422) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44022875351/job/133837394444) |


## [Run #44021828389](https://github.com/sgl-project/sglang/actions/runs/44021828389)
- **分支**: `rainj-me/rust-apis-02-pause-and-frontend-state`
- **总耗时**: 27.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44021828389

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162120) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162120

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133833251993) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133833252025) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834161884) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834161942) |
| base-b-test-16-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162036) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162060) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162064) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162086) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44021828389/job/133834162130) |


## [Run #44019941085](https://github.com/sgl-project/sglang/actions/runs/44019941085)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 34.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44019941085

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 3.8min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748482) |

- **base-b-test-2-npu-a3 / run (0)**: 日志中段被省略，未包含Traceback/RuntimeError等真实错误；仅见artifact上传成功与清理。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748482

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133826904989) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133826905062) |
| multimodal-gen-test-1-npu-a3 (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748193) |
| multimodal-gen-test-4-npu-a3 (0) | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748236) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748271) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748406) |
| base-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748434) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748445) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748503) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748512) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019941085/job/133827748574) |


## [Run #44019331522](https://github.com/sgl-project/sglang/actions/runs/44019331522)
- **分支**: `ywj/upstream_deepgemm_split`
- **总耗时**: 37.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44019331522

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 4.1min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718083) |

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718083

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133824950939) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133824951116) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825717849) |
| multimodal-gen-test-4-npu-a3 (0) | 34.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825717851) |
| multimodal-gen-test-1-npu-a3 (1) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825717866) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825717915) |
| base-b-test-16-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718065) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718074) |
| base-b-test-2-npu-a3 / run (0) | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718100) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718119) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44019331522/job/133825718193) |


## [Run #44017873452](https://github.com/sgl-project/sglang/actions/runs/44017873452)
- **分支**: `rainj-me/rust-apis-09-logging-dumper-l3-elastic`
- **总耗时**: 33.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44017873452

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 1.7min | 环境问题 | 测试日志文件未生成，用例未实际执行，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133831196842) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 1.3min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133831196871) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.5min | 环境问题 | 测试日志未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133831196942) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示未找到 /tmp/test-logs/*.log，无 Traceback 等真实错误信息；结合退出码 5 推断 unittest 存在 errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例未执行、日志缺失。
  链接: https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133831196842

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未生成日志，结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例未执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133831196871

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 与 setUpClass 启动失败常见原因，推测 server 启动阶段异常（如 OOM/SIGKILL），但日志中未见具体 Traceback，需查看被省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133831196942

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133820289931) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133820289984) |
| sgl-router-build-aarch64 / Build sgl-router | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133820353041) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133821257124) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133821257175) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133821257222) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133821257227) |
| base-b-test-2-npu-a3 / run (0) | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133821257237) |
| base-b-test-16-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133821257238) |
| base-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133822099735) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017873452/job/133822099755) |


## [Run #44017869551](https://github.com/sgl-project/sglang/actions/runs/44017869551)
- **分支**: `rainj-me/rust-apis-02-pause-and-frontend-state`
- **总耗时**: 33.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44017869551

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.2min | 环境问题 | 自托管 runner 的容器实现失败，jobPod 未创建，测试未执行 | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133831188814) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.3min | 环境问题 | 测试日志未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133831188858) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.2min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133831188914) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed' 和 'jobPod must be set'，说明 k8s runner 在准备容器/Pod 阶段就失败，测试脚本未运行，属 runner 基础设施问题，需联系自托管 runner 管理员。
  链接: https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133831188814

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 与 setUpClass 启动失败背景，推测 server 启动异常（如 OOM/SIGKILL），但日志被截断未见具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133831188858

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），但日志中未见具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133831188914

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133820276838) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133820276911) |
| sgl-router-build-aarch64 / Build sgl-router | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133820349311) |
| multimodal-gen-test-4-npu-a3 (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133821199404) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133821199418) |
| base-b-test-2-npu-a3 / run (0) | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133821199576) |
| base-b-test-16-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133821199580) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133821199585) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133821199586) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133822129119) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44017869551/job/133822129194) |


## [Run #44007696764](https://github.com/sgl-project/sglang/actions/runs/44007696764)
- **分支**: `fix/hisparse-cpu-copy-retraction`
- **总耗时**: 18.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44007696764

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 15.1min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示产物上传成功与清理过程，无法定位具体错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131057) |
| base-b-test-1-npu-a3 / run (0) | 15.0min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示产物上传成功和清理过程，无法定位具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131099) |
| base-b-test-4-npu-a3 / run (0) | 15.0min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131103) |

- **base-b-test-2-npu-a3 / run (0)**: 日志中段被省略，可见部分只有 artifact 上传成功和 post job cleanup，没有 Traceback/RuntimeError 或退出码 5 的上下文，无法确认是 setUpClass 中 server 启动失败还是其他原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131057

- **base-b-test-1-npu-a3 / run (0)**: 提供的日志被省略，缺少 Traceback/RuntimeError 等真实错误。作业名 base-b-test-1-npu-a3 退出码 5 通常指向 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131099

- **base-b-test-4-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看省略段真实异常确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131103

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133787058855) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133787058935) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788130852) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788130884) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131037) |
| base-b-test-16-npu-a3 / run (0) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131068) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44007696764/job/133788131128) |


## [Run #44006553438](https://github.com/sgl-project/sglang/actions/runs/44006553438)
- **分支**: `perf/glm5-next-layernorm-sp`
- **总耗时**: 75.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44006553438

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.8min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291623) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志省略了中间部分，仅显示artifact上传成功和清理步骤，无Traceback。退出码5表示unittest有errors，常见于setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看省略段确认具体异常。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291623

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133789306796) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133789306841) |
| multimodal-gen-test-1-npu-a3 (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291594) |
| multimodal-gen-test-4-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291602) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291656) |
| base-b-test-16-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291797) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291873) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291899) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291906) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291924) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133790291950) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133799542149) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133799542185) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133799542232) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133809937891) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44006553438/job/133809937997) |


## [Run #44005749755](https://github.com/sgl-project/sglang/actions/runs/44005749755)
- **分支**: `bbuf/cleanup4-srt-core`
- **总耗时**: 79.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44005749755

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.9min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599873) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败工件，说明测试用例执行失败；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志省略了具体 Traceback，需查看失败工件确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599873

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133780731373) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133780731510) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599912) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599936) |
| multimodal-gen-test-1-npu-a3 (1) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599967) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599971) |
| base-b-test-2-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781599996) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781600014) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781600045) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781600082) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133781600089) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133792254534) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133792254562) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133792254668) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133802535921) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005749755/job/133802535946) |


## [Run #44005719585](https://github.com/sgl-project/sglang/actions/runs/44005719585)
- **分支**: `feat/ascend-quant-fa`
- **总耗时**: 31.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44005719585

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.1min | 其他 | 多模态生成测试失败，上传了 diffusion-failures 产物，但日志省略部分未显示具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133781160543) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业运行约29分钟后上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行失败；但日志中间被省略，未见 Traceback/RuntimeError 等真实错误，无法确定是 server 启动失败还是用例断言失败，需查看完整日志或产物确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133781160543

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133780637660) |
| multimodal-gen-test-1-npu-a3 (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133781160445) |
| multimodal-gen-test-4-npu-a3 (1) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133781160475) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005719585/job/133781160490) |


## [Run #44005297833](https://github.com/sgl-project/sglang/actions/runs/44005297833)
- **分支**: `vvvdwbvvv/enabling-aiter-on-sgl-diffusion-gfx1151`
- **总耗时**: 34.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44005297833

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 31.3min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873940) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，未见具体 Traceback。结合退出码 5 与产物命名，推测 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL）导致用例 error，需查看省略段确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873940

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779224478) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873884) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873916) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44005297833/job/133779873951) |


## [Run #44003647941](https://github.com/sgl-project/sglang/actions/runs/44003647941)
- **分支**: `feat/trie-head-shared-attention`
- **总耗时**: 34.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44003647941

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 5.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830358) |
| multimodal-gen-test-4-npu-a3 (0) | 29.9min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830379) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830358

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，作业以非零退出。结合退出码 5 的说明，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830379

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133773729558) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133773729584) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830189) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830201) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830283) |
| multimodal-gen-test-1-npu-a3 (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830291) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830339) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830345) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830401) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003647941/job/133774830425) |


## [Run #44003014857](https://github.com/sgl-project/sglang/actions/runs/44003014857)
- **分支**: `ywj/upstream_deepgemm_split`
- **总耗时**: 83.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44003014857

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505735) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中上传了 diffusion-failures-npu-2-part0-1.zip，说明测试用例执行失败并产生失败工件；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看工件中的 Traceback 确认具体错误。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505735

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133771652006) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133771652237) |
| multimodal-gen-test-1-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505751) |
| multimodal-gen-test-4-npu-a3 (1) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505754) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505809) |
| base-b-test-1-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505815) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505832) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505833) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505853) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505864) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133772505865) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133781956205) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133781956225) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133781956240) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133795642192) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44003014857/job/133795642385) |


## [Run #44000700148](https://github.com/sgl-project/sglang/actions/runs/44000700148)
- **分支**: `amd/gfx942-aiter-mhc`
- **总耗时**: 26.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44000700148

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 0.8min | 环境问题 | 自托管 runner 的容器实现执行失败，jobPod 未创建，测试未真正运行 | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878347) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878398) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed' 及 'jobPod must be set - ensure prepareJob completed successfully'，说明 k8s runner 在准备容器/Pod 阶段失败，属于 CI 基础设施环境问题，而非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878347


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133763910049) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133763910191) |
| multimodal-gen-test-4-npu-a3 (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878153) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878165) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878257) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878290) |
| base-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878309) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44000700148/job/133764878344) |


## [Run #43999991933](https://github.com/sgl-project/sglang/actions/runs/43999991933)
- **分支**: `multi-tokenizer-graceful-drain`
- **总耗时**: 10.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43999991933

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 6.3min | 环境问题 | 日志中未见明确 Traceback，但作业以退出码 5 结束，提示 unittest 存在 errors，最可能是 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850304) |

- **base-b-test-4-npu-a3 / run (0)**: 日志被截断，仅见 artifact 上传与清理，无真实错误堆栈；退出码 5 表示 unittest errors，常见于 setUpClass 中 server 启动失败（如 host OOM、进程被 SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850304

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133765743883) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133765743898) |
| base-b-test-1-npu-a3 / run (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850185) |
| base-b-test-4-npu-a3 / run (1) | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850247) |
| base-b-test-2-npu-a3 / run (0) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999991933/job/133766850324) |


## [Run #43999080357](https://github.com/sgl-project/sglang/actions/runs/43999080357)
- **分支**: `spec-batch1-host-loop`
- **总耗时**: 76.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43999080357

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 32.8min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328443) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约32分钟后上传 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例报错。结合退出码5对应 unittest errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328443

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133758485966) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133758486030) |
| multimodal-gen-test-1-npu-a3 (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328425) |
| multimodal-gen-test-4-npu-a3 (1) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328460) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328469) |
| base-b-test-1-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328496) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328636) |
| base-b-test-16-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328649) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328657) |
| base-b-test-2-npu-a3 / run (0) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328723) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133759328795) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133769258636) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133769258645) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 25.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133769258704) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133779875559) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999080357/job/133779875610) |


## [Run #43999069533](https://github.com/sgl-project/sglang/actions/runs/43999069533)
- **分支**: `engram-group-shards`
- **总耗时**: 44.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43999069533

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133771644330) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133771644330

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133761047068) |
| base-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133761047285) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347189) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347197) |
| base-b-test-4-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347310) |
| base-b-test-8-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347366) |
| base-b-test-16-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347393) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347416) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762347725) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133762348465) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133771644400) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43999069533/job/133771644463) |


## [Run #43992226690](https://github.com/sgl-project/sglang/actions/runs/43992226690)
- **分支**: `agentx/spf-replay-reserve`
- **总耗时**: 48.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43992226690

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 21.9min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133746816021) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 可见日志仅为 runner 初始化、下载 action、上传 artifact 和清理阶段，中间省略部分包含真正的测试执行与报错。需查看完整日志中 Traceback/RuntimeError 或退出码 5 对应的 setUpClass 失败信息。
  链接: https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133746816021

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133735763203) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133735763277) |
| multimodal-gen-test-4-npu-a3 (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030581) |
| multimodal-gen-test-4-npu-a3 (1) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030617) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030656) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030710) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030808) |
| base-b-test-16-npu-a3 / run (0) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030816) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030847) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133737030929) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133746815749) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43992226690/job/133746815770) |


## [Run #43991150360](https://github.com/sgl-project/sglang/actions/runs/43991150360)
- **分支**: `pr/muse-gfx1250`
- **总耗时**: 73.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43991150360

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.5min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798729) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798729

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133731916929) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133731917068) |
| base-b-test-1-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798701) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798703) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798728) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798741) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798838) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798856) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798929) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732798949) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133732799101) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133742812324) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133742812336) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133742812471) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133754160058) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991150360/job/133754160143) |


## [Run #43991076949](https://github.com/sgl-project/sglang/actions/runs/43991076949)
- **分支**: `agentx/spf-replay-reserve`
- **总耗时**: 9.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43991076949

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 5.7min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792036) |
| base-b-test-4-npu-a3 / run (0) | 5.8min | 环境问题 | 日志中未见明确错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792312) |
| base-b-test-8-npu-a3 / run (0) | 5.7min | 环境问题 | 日志中未见测试执行错误，作业在 artifact 上传后正常清理，失败原因需结合省略的中间日志确认 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792313) |
| base-b-test-1-npu-a3 / run (0) | 5.7min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792382) |
| base-b-test-2-npu-a3 / run (0) | 5.8min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792409) |
| base-b-test-4-npu-a3 / run (1) | 5.8min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792481) |
| base-b-test-16-npu-a3 / run (0) | 5.7min | 环境问题 | 日志中未见明确错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792548) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中上传了 diffusion-failures-npu-2-part1-1.zip 失败产物，说明多模态生成用例执行失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792036

- **base-b-test-4-npu-a3 / run (0)**: 日志被截断，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792312

- **base-b-test-8-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 selected-test-logs artifact 及 post job cleanup，均成功；真正的失败发生在被省略的中间测试阶段，当前片段无法定位具体 Traceback，建议查看完整日志中退出码 5 对应的 setUpClass/server 启动错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792313

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，未见Traceback/RuntimeError等真实错误；仅见artifact上传成功与Node.js弃用警告。退出码5表明unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792382

- **base-b-test-2-npu-a3 / run (0)**: 日志仅显示artifact上传成功和清理，无Traceback。按背景知识，退出码5多为setUpClass时server启动失败（如host OOM、进程被SIGKILL），属环境问题，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792409

- **base-b-test-4-npu-a3 / run (1)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792481

- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅显示 checkout、artifact 上传成功及 Node.js 弃用警告，无 Traceback/RuntimeError。若退出码为 5，多为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略部分确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792548

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133731688909) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133731689034) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43991076949/job/133732792098) |


## [Run #43990429766](https://github.com/sgl-project/sglang/actions/runs/43990429766)
- **分支**: `bbuf/cleanup4-srt-models-layers`
- **总耗时**: 30.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43990429766

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | 其他 | 日志被截断，未显示实际失败原因，仅见产物上传成功 | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769932482) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中省略了中间部分，可见内容只有 runner 初始化、下载 action、上传 diffusion-failures 产物和清理步骤，没有 Traceback 或退出码信息，无法定位具体失败原因，需查看完整日志确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769932482

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769933695) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769933801) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769933937) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769934081) |
| base-b-test-16-npu-a3 / run (0) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769934244) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769934562) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769934689) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769935287) |
| base-b-test-8-npu-a3 / run (0) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769935577) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769937427) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769937772) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769938432) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769939453) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769939887) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769940543) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43990429766/job/133769940713) |


## [Run #43988491778](https://github.com/sgl-project/sglang/actions/runs/43988491778)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 80.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43988491778

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | 其他 | 多模态生成测试失败，上传了 diffusion-failures 工件，但日志省略段未显示具体错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724301981) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业退出码非0，上传了 diffusion-failures-npu-2-part0-1.zip 失败工件；可见日志仅为 runner 初始化与清理，缺少 Traceback，无法定位具体原因，需查看省略段或工件。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724301981

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133723066995) |
| Recommend tests from coverage | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133723067086) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724301900) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724301955) |
| multimodal-gen-test-1-npu-a3 (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724302029) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724302317) |
| base-b-test-2-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724302335) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724302506) |
| base-b-test-16-npu-a3 / run (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724302657) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724303286) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133724303362) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133735038412) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133735038449) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133735038490) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133748465129) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43988491778/job/133748465226) |


## [Run #43985882217](https://github.com/sgl-project/sglang/actions/runs/43985882217)
- **分支**: `bbuf/cleanup4-diffusion`
- **总耗时**: 29.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43985882217

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | 环境问题 | 多模态生成测试用例执行失败，退出码5表示unittest存在errors，疑似setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43985882217/job/133769843512) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中上传了diffusion-failures-npu-2-part0-2.zip失败产物，说明测试用例运行出错。退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看上传产物中的Traceback确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43985882217/job/133769843512

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43985882217/job/133769844608) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43985882217/job/133769844978) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43985882217/job/133769845856) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43985882217/job/133769845869) |


## [Run #43984101253](https://github.com/sgl-project/sglang/actions/runs/43984101253)
- **分支**: `dark/eagle-fused-draft-sample`
- **总耗时**: 83.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43984101253

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.2min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224090) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明多模态生成用例执行失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224090

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133707919201) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133707919323) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709223974) |
| multimodal-gen-test-1-npu-a3 (0) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224096) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224170) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224187) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224210) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224239) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224292) |
| base-b-test-16-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224304) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133709224375) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133720281913) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133720281956) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133720282019) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133737491635) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984101253/job/133737491722) |


## [Run #43984099422](https://github.com/sgl-project/sglang/actions/runs/43984099422)
- **分支**: `dark/dflash2-fused-select`
- **总耗时**: 81.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43984099422

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | 环境问题 | 日志中未见明确错误，但上传了 diffusion-failures 产物，推测测试用例失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026872) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，仅见 artifact 上传成功，无 Traceback。作业名 multimodal-gen-test-4-npu-a3，上传 diffusion-failures-npu-2-part0-1.zip，说明测试存在失败用例，具体原因需查看产物或完整日志。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026872

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133707875316) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133707875388) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026781) |
| multimodal-gen-test-1-npu-a3 (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026792) |
| base-b-test-2-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026884) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709026902) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709027019) |
| base-b-test-16-npu-a3 / run (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709027127) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709027153) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709027352) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133709027605) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133719808575) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133719808639) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133719808929) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133735043209) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43984099422/job/133735043241) |


## [Run #43981642271](https://github.com/sgl-project/sglang/actions/runs/43981642271)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 50.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43981642271

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864689) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 25.5min | 其他 | 日志片段未包含实际测试失败信息，仅显示产物上传和清理成功。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133710824542) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，作业以非零退出。结合退出码 5 提示，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看省略段 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864689

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 提供的日志被截断，缺少测试执行阶段的 Traceback/RuntimeError 等真实错误；无法确认退出码 5 的具体原因，需查看完整日志中 setUpClass 或 server 启动部分。
  链接: https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133710824542

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133699776779) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133699776917) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864619) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864742) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864804) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864929) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864970) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700864992) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700865002) |
| base-b-test-4-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700865020) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133700865103) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133710824519) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43981642271/job/133710824529) |


## [Run #43978624685](https://github.com/sgl-project/sglang/actions/runs/43978624685)
- **分支**: `hwoo/delta-recipes-sglang`
- **总耗时**: 80.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43978624685

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.9min | 环境问题 | 多模态生成测试中 server 启动失败，导致 unittest 出现 errors（退出码 5） | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532118) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示上传了 diffusion-failures-npu-2 失败产物，作业以用例 errors 结束；结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看上传的失败日志确认具体 Traceback。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532118

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133689212240) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133689212298) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532058) |
| multimodal-gen-test-1-npu-a3 (1) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532077) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532102) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532298) |
| base-b-test-2-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532304) |
| base-b-test-16-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532342) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532436) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532520) |
| base-b-test-1-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133690532525) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133702423597) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133702423605) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133702423640) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133717297179) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978624685/job/133717297206) |


## [Run #43978177116](https://github.com/sgl-project/sglang/actions/runs/43978177116)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 24.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43978177116

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 19.6min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 NPU 上 server 启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689391785) |
| base-b-test-1-npu-a3 / run (0) | 20.0min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392011) |
| base-b-test-2-npu-a3 / run (0) | 18.9min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示产物上传成功和清理过程，无法定位具体错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392067) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，作业以失败结束；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），需查看省略段中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689391785

- **base-b-test-1-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、action 下载、artifact 上传和 post-job 清理，均正常完成；中间省略部分才包含测试执行与退出码 5 的真实 Traceback，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392011

- **base-b-test-2-npu-a3 / run (0)**: 提供的日志被截断，缺少测试执行阶段的 Traceback/RuntimeError 等真实错误。退出码 5 提示 unittest 存在 errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），但需以完整日志中的实际异常为准。
  链接: https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392067

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133687935929) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133687936505) |
| multimodal-gen-test-4-npu-a3 (1) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689391679) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689391842) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689391995) |
| base-b-test-16-npu-a3 / run (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392009) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392143) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392182) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43978177116/job/133689392223) |


## [Run #43976802741](https://github.com/sgl-project/sglang/actions/runs/43976802741)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 9.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43976802741

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 4.7min | 环境问题 | multimodal-gen 测试用例执行失败，退出码 5 表明 unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684541903) |
| multimodal-gen-test-1-npu-a3 (1) | 4.8min | 环境问题 | multimodal 测试失败，上传了 diffusion-failures 工件，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684541939) |
| multimodal-gen-test-4-npu-a3 (1) | 5.5min | 环境问题 | 多模态生成测试失败，失败产物已上传，但日志中未显示具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542061) |
| base-b-test-8-npu-a3 / run (0) | 5.6min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542131) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 NPU 环境或 server 启动问题 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542194) |
| base-b-test-4-npu-a3 / run (0) | 5.7min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542215) |
| base-b-test-4-npu-a3 / run (1) | 5.7min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542310) |
| base-b-test-1-npu-a3 / run (0) | 5.7min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示 artifact 上传与清理成功，无法定位具体错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542428) |
| base-b-test-16-npu-a3 / run (0) | 5.7min | 环境问题 | 日志中未见测试执行错误，作业在 artifact 上传后正常清理，失败原因需查看省略的中间日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542449) |
| base-b-test-2-npu-a3 / run (0) | 5.9min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542488) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见失败产物 diffusion-failures-npu-1-part0-1.zip 上传。退出码 5 对应 unittest errors，最常见为 setUpClass 时 server 启动失败（host OOM 或进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684541903

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part1-1.zip（943字节）及退出码5，表明 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL）。需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684541939

- **multimodal-gen-test-4-npu-a3 (1)**: 作业退出码5表明unittest存在errors，通常为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。日志省略了中间部分，仅见diffusion-failures产物上传，未见Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542061

- **base-b-test-8-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542131

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；作业上传了 diffusion-failures-npu-2-part0-1.zip（533字节），说明测试用例失败并生成失败产物。结合退出码 5 的常见原因，推测 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），属环境问题，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542194

- **base-b-test-4-npu-a3 / run (0)**: 日志省略了中间部分，仅显示artifact上传和清理成功，未包含实际测试失败信息。根据退出码5推断，unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志中的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542215

- **base-b-test-4-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5对应unittest errors，常见于setUpClass时server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542310

- **base-b-test-1-npu-a3 / run (0)**: 可见日志均为 runner 初始化、下载 action、上传 selected-test-logs artifact 及 post job cleanup，未见 Traceback/RuntimeError 或退出码 5 的用例错误。需查看被省略的中间日志确认 setUpClass 阶段 server 启动失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542428

- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 artifact 和 post job cleanup，均成功；关键测试执行段被省略，无法定位具体 Traceback。若退出码为 5，多为 setUpClass 阶段 sglang server 启动失败（如 host OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542449

- **base-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133684542488

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133683123878) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43976802741/job/133683124122) |


## [Run #43973051402](https://github.com/sgl-project/sglang/actions/runs/43973051402)
- **分支**: `kimi-k3.1-day-0`
- **总耗时**: 24.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43973051402

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 19.6min | 其他 | 日志中未见明确错误，仅显示上传了 diffusion-failures 工件，失败原因需查看工件内容。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551387) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551868) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，仅见工件上传成功及 Node.js 弃用警告，无 Traceback/RuntimeError。作业失败但未暴露具体错误，推测为测试用例失败（退出码5），需查看 diffusion-failures-npu-2-part0-1.zip 中的真实报错。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551387

- **base-b-test-2-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传和清理，无Traceback。退出码5表示unittest有errors，常见于setUpClass中server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551868

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133670113606) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133670113733) |
| multimodal-gen-test-4-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551386) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551400) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551411) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551732) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551811) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551813) |
| base-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671551939) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43973051402/job/133671552203) |


## [Run #43960748144](https://github.com/sgl-project/sglang/actions/runs/43960748144)
- **分支**: `amd/wan22-gfx1250-gelu`
- **总耗时**: 32.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43960748144

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 2.9min | 环境问题 | 未找到 diffusion-failures 目录，测试产物缺失，疑似用例执行失败或未生成输出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628306972) |
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 工件，疑似 NPU 上 server 启动或推理异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628307132) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 步骤报 'No files were found with the provided path: diffusion-failures/'，说明测试未产出预期失败样本目录；结合退出码 5 提示 unittest 存在 errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628306972

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾仅显示上传 diffusion-failures-npu-2-part0-1.zip 工件，说明测试用例失败并收集了失败产物；中间省略部分应含真实 Traceback。结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），属环境问题，需查看省略日志中的具体异常确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628307132

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133627406838) |
| multimodal-gen-test-4-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628306802) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43960748144/job/133628306963) |


## [Run #43955528880](https://github.com/sgl-project/sglang/actions/runs/43955528880)
- **分支**: `ci-fix/amd-aiter-workspace-reserve`
- **总耗时**: 26.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43955528880

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 4.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989430) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989430

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133609219999) |
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133609220287) |
| multimodal-gen-test-4-npu-a3 (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610988974) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989006) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989073) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989079) |
| base-b-test-2-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989233) |
| base-b-test-1-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989320) |
| base-b-test-16-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43955528880/job/133610989349) |


## [Run #43954451169](https://github.com/sgl-project/sglang/actions/runs/43954451169)
- **分支**: `oss-sync-637b260a19`
- **总耗时**: 52.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43954451169

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 21.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133623090457) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133623090457

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133605522412) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133605522470) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095053) |
| multimodal-gen-test-4-npu-a3 (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095145) |
| base-b-test-1-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095310) |
| base-b-test-16-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095400) |
| base-b-test-2-npu-a3 / run (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095420) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095450) |
| base-b-test-4-npu-a3 / run (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095515) |
| base-b-test-4-npu-a3 / run (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133607095522) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133623090603) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43954451169/job/133623090717) |


## [Run #43948457441](https://github.com/sgl-project/sglang/actions/runs/43948457441)
- **分支**: `sensenova-bf16-rope-npu-main`
- **总耗时**: 42.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43948457441

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 38.8min | 其他 | 多模态生成测试失败，上传了 diffusion-failures 产物，具体错误被省略 | [job link](https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133585373740) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，推测为用例执行失败（退出码5，unittest errors），最可能为 setUpClass 阶段 server 启动失败，需查看省略部分 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133585373740

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133584503719) |
| multimodal-gen-test-4-npu-a3 (1) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133585373929) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133585373970) |
| multimodal-gen-test-1-npu-a3 (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948457441/job/133585374056) |


## [Run #43948364364](https://github.com/sgl-project/sglang/actions/runs/43948364364)
- **分支**: `clearing_console_output`
- **总耗时**: 72.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43948364364

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.0min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470553) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败工件，说明测试用例执行失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看工件中的 Traceback 确认具体错误。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470553

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133584162099) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133584162209) |
| multimodal-gen-test-1-npu-a3 (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470400) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470522) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470731) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470771) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470772) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470779) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470818) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470882) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133585470885) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133599465841) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133599465925) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133599465974) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133614826106) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43948364364/job/133614826166) |


## [Run #43941300510](https://github.com/sgl-project/sglang/actions/runs/43941300510)
- **分支**: `megakernel-dsa-view-draft-capture`
- **总耗时**: 78.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43941300510

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.9min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560784732) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认具体错误。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560784732

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133559444515) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133559444753) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560784659) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560784684) |
| multimodal-gen-test-1-npu-a3 (1) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560784687) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560784962) |
| base-b-test-2-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560785003) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560785008) |
| base-b-test-16-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560785086) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560785092) |
| base-b-test-1-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133560785369) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133575145658) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133575145792) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133575145834) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133593833541) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941300510/job/133593833634) |


## [Run #43941077287](https://github.com/sgl-project/sglang/actions/runs/43941077287)
- **分支**: `perf/input-embeds-one-union-member`
- **总耗时**: 34.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43941077287

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.7min | 环境问题 | 多模态生成测试作业失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559997992) |
| base-b-test-4-npu-a3 / run (1) | 7.8min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998408) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，未见具体 Traceback；结合退出码 5 推断为 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL）导致用例 error。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559997992

- **base-b-test-4-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998408

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133558690318) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133558690325) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559997802) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559997883) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559997938) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998068) |
| base-b-test-16-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998137) |
| base-b-test-2-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998203) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998303) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43941077287/job/133559998431) |


## [Run #43936732666](https://github.com/sgl-project/sglang/actions/runs/43936732666)
- **分支**: `pr/muse-gfx1250`
- **总耗时**: 82.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43936732666

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.4min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545275854) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，未见具体 Traceback；但作业上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，且退出码 5 对应 unittest errors，最常见为 setUpClass 时 sglang server 启动失败（host OOM 或进程被 SIGKILL）。需查看省略段与产物确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545275854

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133543676421) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133543676497) |
| multimodal-gen-test-4-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545275698) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545275764) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545275886) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545275895) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545276025) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545276079) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545276088) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545276246) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133545276251) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133559351858) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133559351876) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133559351956) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133579734080) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43936732666/job/133579734159) |


## [Run #43935911666](https://github.com/sgl-project/sglang/actions/runs/43935911666)
- **分支**: `pr/muse-gfx1250`
- **总耗时**: 5.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43935911666

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 1.4min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542089932) |
| multimodal-gen-test-4-npu-a3 (1) | 0.9min | 环境问题 | 日志在 checkout 后即被清理，未进入测试阶段，疑似 runner 环境或 k8s 执行异常导致作业提前终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090013) |
| multimodal-gen-test-4-npu-a3 (0) | 1.3min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090112) |
| multimodal-gen-test-1-npu-a3 (1) | 1.1min | 环境问题 | 日志中未见测试执行错误，仅显示未找到 diffusion-failures 目录，作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090146) |
| base-b-test-4-npu-a3 / run (0) | 1.6min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090262) |
| base-b-test-4-npu-a3 / run (1) | 1.6min | 环境问题 | 测试日志文件未生成，用例脚本退出码5，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090287) |
| base-b-test-8-npu-a3 / run (0) | 1.6min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090346) |
| base-b-test-2-npu-a3 / run (0) | 1.6min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090356) |
| base-b-test-1-npu-a3 / run (0) | 1.6min | 环境问题 | 测试日志文件未生成，测试用例未实际执行或提前失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090606) |
| base-b-test-16-npu-a3 / run (0) | 1.6min | 环境问题 | 测试日志文件未生成，测试用例未实际执行，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090611) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志仅包含 runner 初始化、action 下载和清理过程，未出现测试脚本输出或 Traceback；upload-artifact 提示未找到 diffusion-failures/ 路径，说明测试阶段未产生预期产物，疑似环境或前置步骤异常导致用例未实际运行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542089932

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅显示 checkout 完成及 Node.js 20 弃用警告，随后出现 Cleaning up orphan processes，无测试执行与 Traceback，无法确认退出码 5 的具体来源，判断为 runner/k8s 环境异常导致作业中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090013

- **multimodal-gen-test-4-npu-a3 (0)**: 作业在准备/清理阶段结束，未出现 Traceback 或 RuntimeError；仅提示 No files were found with the provided path: diffusion-failures/，说明测试产物目录未生成，疑似用例未实际运行或前置步骤失败，属环境/流程问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090112

- **multimodal-gen-test-1-npu-a3 (1)**: 日志被截断，可见部分只有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，未出现 Traceback 或退出码 5 的具体错误。推测测试脚本未产生失败产物目录，可能 setUpClass 阶段 server 启动失败或测试未实际运行，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090146

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未生成日志，结合退出码 5（unittest errors）推断 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090262

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 unittest errors，而非用例未收集。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090287

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未正常运行或未生成日志，随后直接进入清理阶段，无 Traceback 可查，疑似环境/容器启动或脚本执行异常导致。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090346

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无测试产物上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），但日志中未见具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090356

- **base-b-test-1-npu-a3 / run (0)**: 日志显示未找到 /tmp/test-logs/*.log，说明测试脚本未产出日志，可能 setUpClass 阶段 server 启动失败或进程被终止，导致用例未运行即退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090606

- **base-b-test-16-npu-a3 / run (0)**: 日志显示未找到 /tmp/test-logs/*.log，无 artifact 上传，说明测试脚本未产出日志；结合退出码 5 常见于 setUpClass 中 sglang server 启动失败（如 host OOM、进程被 SIGKILL），属环境/资源问题，非用例收集问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133542090611

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133540573378) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43935911666/job/133540573385) |


## [Run #43933670349](https://github.com/sgl-project/sglang/actions/runs/43933670349)
- **分支**: `qkang/elastic-ep-mooncake-scale-down`
- **总耗时**: 29.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43933670349

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | 环境问题 | 日志中未见明确错误，但作业以退出码5失败，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744589776) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志省略了中间部分，仅显示artifact上传成功和清理步骤，无Traceback。退出码5表示unittest存在errors，最常见为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看省略段确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744589776

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744591227) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744591538) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744591826) |
| multimodal-gen-test-1-npu-a3 (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744591934) |
| base-b-test-16-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744592185) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744592586) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744592685) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744593123) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744593151) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744593157) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744593373) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744594537) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 25.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744594720) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744594738) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744595964) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43933670349/job/133744597000) |


## [Run #43927224247](https://github.com/sgl-project/sglang/actions/runs/43927224247)
- **分支**: `hicache-write-back-storage-lookup`
- **总耗时**: 59.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43927224247

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133525648729) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133525648729

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133510010584) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133510010665) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511642972) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643089) |
| base-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643321) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643388) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643558) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643582) |
| base-b-test-4-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643588) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133511643615) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133525648612) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43927224247/job/133525648662) |


## [Run #43922134264](https://github.com/sgl-project/sglang/actions/runs/43922134264)
- **分支**: `feat/flashinfer-scoped-graph-cache`
- **总耗时**: 75.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43922134264

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 40.9min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846666) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例运行出错；结合退出码 5 与 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL）的常见原因，判断为环境/资源问题而非用例未收集。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846666

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133492283813) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133492283970) |
| multimodal-gen-test-1-npu-a3 (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846371) |
| multimodal-gen-test-1-npu-a3 (1) | 28.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846389) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846608) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846871) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846891) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846937) |
| base-b-test-1-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493846972) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493847060) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133493847115) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133506807952) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133506807956) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133506808029) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133525538562) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43922134264/job/133525538692) |


## [Run #43909957963](https://github.com/sgl-project/sglang/actions/runs/43909957963)
- **分支**: `pr/muse-gfx1250`
- **总耗时**: 75.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43909957963

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.3min | 环境问题 | 多模态生成测试作业失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450312816) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-1.zip 失败产物，未见具体 Traceback。按退出码 5 推断为 unittest errors，常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段真实错误确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450312816

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133449127516) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133449127591) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450312542) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450312551) |
| base-b-test-16-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450312968) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450312999) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450313139) |
| multimodal-gen-test-4-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450313173) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450313207) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450313264) |
| base-b-test-1-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133450313566) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133464040773) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133464041054) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133464041063) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133485867404) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43909957963/job/133485867444) |


## [Run #43908980485](https://github.com/sgl-project/sglang/actions/runs/43908980485)
- **分支**: `feat/flashinfer-scoped-graph-cache`
- **总耗时**: 73.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43908980485

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | 环境问题 | 日志中未见测试用例执行，作业在 artifact 上传后正常清理，失败原因需查看省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447478955) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.3min | 环境问题 | 日志被截断，无法看到真实错误，但作业在测试阶段失败且退出码为5，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133483556617) |

- **multimodal-gen-test-4-npu-a3 (0)**: 可见日志仅显示 runner 初始化、下载 action、上传 diffusion-failures-npu-2-part0-1.zip 及 post job cleanup，未包含测试执行与错误 Traceback；无法从现有片段确认退出码 5 的具体原因，需查看省略的中间日志中 setUpClass/server 启动错误。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447478955

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 可见日志仅含runner初始化、action下载、artifact上传和清理，缺少测试执行与Traceback部分。退出码5表示unittest有errors，最可能是setUpClass中server启动失败（OOM/SIGKILL），需查看被省略的中间日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133483556617

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133445644166) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133445644216) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447478939) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479000) |
| multimodal-gen-test-4-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479068) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479093) |
| base-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479189) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479195) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479396) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479551) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133447479633) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133462851327) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133462851455) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133462851468) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43908980485/job/133483556481) |


## [Run #43895367887](https://github.com/sgl-project/sglang/actions/runs/43895367887)
- **分支**: `dsv41-a5`
- **总耗时**: 33.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43895367887

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410051590) |
| base-b-test-1-npu-a3 / run (0) | 23.0min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054380) |
| base-b-test-2-npu-a3 / run (0) | 18.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054546) |
| base-b-test-4-npu-a3 / run (1) | 14.2min | 环境问题 | 日志被截断，未显示真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054752) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-2.zip 失败产物，说明多模态生成测试用例失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410051590

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，未见Traceback/RuntimeError。退出码5表示unittest有errors，通常为setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL）。需查看完整日志确认具体异常。
  - 失败用例: npu_dsv4_hicache_l2_pool.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054380

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054546

- **base-b-test-4-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5对应unittest errors，常见于setUpClass时server启动失败（OOM/SIGKILL），需查看完整日志确认具体异常。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054752

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133408302439) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133408302598) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410051641) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410051645) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410051758) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054301) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054318) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43895367887/job/133410054535) |


## [Run #43891721088](https://github.com/sgl-project/sglang/actions/runs/43891721088)
- **分支**: `bbuf/cleanup4-srt-core`
- **总耗时**: 85.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43891721088

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.3min | 环境问题 | 多模态生成测试作业失败，上传了 diffusion-failures 产物，疑似 NPU 上 server 启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160377) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，仅见上传 diffusion-failures-npu-2-part0-2.zip 失败产物，未见具体 Traceback。结合退出码 5 提示，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看产物中真实错误确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160377

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133702091184) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133702091203) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160259) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160327) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160334) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160389) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160412) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160417) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160440) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160464) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133703160608) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133714201645) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133714201659) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133714201671) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133730232851) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43891721088/job/133730232893) |


## [Run #43889969273](https://github.com/sgl-project/sglang/actions/runs/43889969273)
- **分支**: `bbuf/cleanup4-diffusion`
- **总耗时**: 25.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43889969273

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 24.7min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43889969273/job/133702049573) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-3.zip 失败产物，作业以非零退出。结合退出码 5 提示，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43889969273/job/133702049573

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889969273/job/133702051540) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889969273/job/133702051705) |
| Recommend tests from coverage | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889969273/job/133702051962) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889969273/job/133702052090) |


## [Run #43889954943](https://github.com/sgl-project/sglang/actions/runs/43889954943)
- **分支**: `bbuf/cleanup4-kernels`
- **总耗时**: 36.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43889954943

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 25.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021436) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021436

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133846070567) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133846070642) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021315) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021369) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021377) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021471) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021474) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021505) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021521) |
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021534) |
| base-b-test-4-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889954943/job/133847021658) |


## [Run #43889940777](https://github.com/sgl-project/sglang/actions/runs/43889940777)
- **分支**: `bbuf/cleanup4-srt-models-layers`
- **总耗时**: 58.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43889940777

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.9min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388538) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 6.2min | 其他 | 日志片段未包含实际测试失败的错误信息，仅显示产物上传成功和清理过程。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133726327931) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 6.2min | 环境问题 | 日志被截断，未包含实际失败错误信息，无法定位具体原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133726328059) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行了约30分钟后上传了 diffusion-failures-npu-2-part0-2.zip 失败产物，说明测试用例执行失败；结合退出码5的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认具体错误。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388538

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志中省略了中间部分，可见部分只有 runner 初始化、下载 action、上传 artifact 和 post job cleanup，没有 Traceback/RuntimeError 或退出码 5 的具体错误，无法定位失败原因，需查看被省略的测试执行段日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133726327931

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 可见日志仅为 runner 初始化、artifact 上传和清理阶段，均正常完成；中间省略部分才含测试执行与错误，但未提供。无法确认是否为 setUpClass 启动失败或退出码 5，需查看完整日志中的 Traceback/RuntimeError。
  链接: https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133726328059

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133702220342) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133702220736) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388546) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388597) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388664) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388686) |
| base-b-test-16-npu-a3 / run (0) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388709) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388773) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388784) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388786) |
| base-b-test-4-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133703388822) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133713899833) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133713899907) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43889940777/job/133713899928) |


## [Run #43883325871](https://github.com/sgl-project/sglang/actions/runs/43883325871)
- **分支**: `gemma4-ar-fusion-decode`
- **总耗时**: 26.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43883325871

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819571) |

- **base-b-test-16-npu-a3 / run (0)**: 日志中段省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819571

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772010267) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772010278) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819394) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819396) |
| base-b-test-1-npu-a3 / run (0) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819478) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819525) |
| base-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819564) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819569) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43883325871/job/133772819570) |


## [Run #43826899517](https://github.com/sgl-project/sglang/actions/runs/43826899517)
- **分支**: `v4.1/h20-verify-k-reuse`
- **总耗时**: 83.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43826899517

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.4min | 环境问题 | 上传测试产物时进度停滞，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133949520792) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示上传 artifact 到 blob storage 时出现 'Upload progress stalled'，仅上传 84586 字节后卡住，最终进程退出码 1，属于 CI 存储/网络环境问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133949520792

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133932471842) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133932471904) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757557) |
| base-b-test-2-npu-a3 / run (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757597) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757611) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757612) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757620) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757677) |
| base-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757713) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757733) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933757886) |
| base-b-test-4-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133933758290) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133949520769) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43826899517/job/133949520908) |


---
*Auto-generated by ci_monitor.py*