# NPU CI 执行监控（2026-11-07）
**生成时间**: 2026-11-08 07:11
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-07 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 107

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1039 个 | 失败 135 个 | 成功 Job 平均耗时 15.0min
- **Run 执行情况**: 成功 68 个 | 失败 39 个 | 成功 Run 平均耗时 65.3min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 73.5min | #42371724401 | [job link](https://github.com/sgl-project/sglang/actions/runs/42371724401/job/128415231172) |
| base-b-test-4-npu-a3 / run (0) | 60.9min | #42371724401 | [job link](https://github.com/sgl-project/sglang/actions/runs/42371724401/job/128401656679) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 58.7min | #42089083993 | [job link](https://github.com/sgl-project/sglang/actions/runs/42089083993/job/128061629318) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 55.3min | #42242749889 | [job link](https://github.com/sgl-project/sglang/actions/runs/42242749889/job/127991231567) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 51.9min | #42359803361 | [job link](https://github.com/sgl-project/sglang/actions/runs/42359803361/job/128371201896) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.9min | #42294575575 | [job link](https://github.com/sgl-project/sglang/actions/runs/42294575575/job/128168204336) |
| base-b-test-1-npu-a3 / run (0) | 47.0min | #42371724401 | [job link](https://github.com/sgl-project/sglang/actions/runs/42371724401/job/128401656699) |
| base-b-test-2-npu-a3 / run (0) | 42.9min | #42371724401 | [job link](https://github.com/sgl-project/sglang/actions/runs/42371724401/job/128401656706) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 42.8min | #42281722556 | [job link](https://github.com/sgl-project/sglang/actions/runs/42281722556/job/128125820550) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 42.7min | #42286510725 | [job link](https://github.com/sgl-project/sglang/actions/runs/42286510725/job/128142065291) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 57.0min | #42244763737 | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464861) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.8min | #42345180632 | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128327541590) |
| multimodal-gen-test-4-npu-a3 (0) | 27.9min | #42293832287 | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105373) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.8min | #42380715488 | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680424) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.9min | #42354841044 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194441) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | #42314852493 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587831) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | #42303562890 | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857298) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | #42320759667 | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337054) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | #42319040124 | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239522063) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | #42303562890 | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857556) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-2-npu-a3 / run (0) | 84 | 61 | 10 | 1 | 12 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120247)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239522063)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914911)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587955)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632720) |
| base-b-test-1-npu-a3 / run (0) | 80 | 62 | 5 | 1 | 12 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823187)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337054)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587831)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857298)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076814920) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 54 | 45 | 5 | 1 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680424)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128353869153)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194441)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128327541590)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128236035472) |
| base-b-test-4-npu-a3 / run (1) | 82 | 68 | 4 | 1 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587829)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632735)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242709)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332413) |
| base-b-test-4-npu-a3 / run (0) | 82 | 66 | 2 | 1 | 13 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105670)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242804) |
| base-b-test-8-npu-a3 / run (0) | 71 | 64 | 1 | 1 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332339) |
| base-b-test-16-npu-a3 / run (0) | 70 | 59 | 0 | 2 | 9 | - |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 90 | 85 | 0 | 2 | 3 | - |
| multimodal-gen-test-4-npu-a3 (0) | 86 | 76 | 1 | 0 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464861) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_mla_fia_hicache_bf16.py` | 25 | 19 | 6 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914911)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587955)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632720) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 9 | 4 | 5 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680424)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128353869153)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194441) |
| `npu_pd_disaggregation.py` | 29 | 25 | 4 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587829)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632735)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242709) |
| `npu_return_indexer_topk_deepseek_v4.py` | 17 | 14 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120247)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239522063)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857556) |
| `npu_hicache_mha.py` | 26 | 24 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823187)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076814920) |
| `mova_360p_ti2va_2npu` | 13 | 12 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464861) |
| `npu_expert_distribution_recorder_mode.py` | 19 | 18 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795571) |
| `flux_2_image_t2i_2npu` | 18 | 17 | 1 | [multimodal-gen-test-4-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144329) |
| `npu_tp1_bf16.py` | 24 | 23 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337054) |
| `npu_eagle3.py` | 23 | 22 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587831) |
| `dspark_npu_dispatch.py` | 13 | 12 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857298) |
| `npu_dp_attention.py` | 25 | 24 | 1 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242804) |
| `npu_w4a4_quantization.py` | 25 | 24 | 1 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105670) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 33 | 32 | 1 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332339) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #42244763737<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 124.9min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42244763737) |
| #42354453484<br>[#48375 [Feat] PD: Publish spec_kv_layout so DSpark/DFlash prefill and decode must match](https://github.com/sgl-project/sglang/pull/48375) | `pd-spec-kv-layout` | 78.5min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42354453484) |
| #42298183607<br>[#48762 [Refactor] scheduler: Run every state check through SchedulerInvariantChecker.run](https://github.com/sgl-project/sglang/pull/48762) | `lsyin/sched-pr25` | 74.3min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42298183607) |
| #42380715488<br>[#47210 [Perf] [SM120] fp8: Use native block32 DeepGEMM for DSV4.1](https://github.com/sgl-project/sglang/pull/47210) | `sm120-block32-native-deepgemm` | 58.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42380715488) |
| #42345180632<br>[#46693 [Feat] [AMD] minimax: Support MiniMax-M3.1-Flash on MI350X / MI355X (gfx950)](https://github.com/sgl-project/sglang/pull/46693) | `m31-amd/integration` | 57.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42345180632) |
| #42276169748<br>[#44152 [Feat] score/embedding: Add raw embeddings, score rids, encode input_ids, and schedule-decision logging](https://github.com/sgl-project/sglang/pull/44152) | `jsheng/score-embedding-features` | 55.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42276169748) |
| #42354841044<br>[#48895 [Perf] [NVIDIA] dsa/dcp: Fused DCP8 indexer top-k for decode](https://github.com/sgl-project/sglang/pull/48895) | `dcp-fused-topk-main` | 53.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42354841044) |
| #42314853155<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 51.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42314853155) |
| #42348866170<br>[#48375 [Feat] PD: Publish spec_kv_layout so DSpark/DFlash prefill and decode must match](https://github.com/sgl-project/sglang/pull/48375) | `pd-spec-kv-layout` | 43.8min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42348866170) |
| #42350633219<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 41.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42350633219) |
| #42275307696<br>[#48946 [Refactor] moe: Remove the bailing_moe_topk and JIT moe_topk_sigmoid routers](https://github.com/sgl-project/sglang/pull/48946) | `moe-router-dedup` | 39.0min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42275307696) |
| #42354163215<br>[#48992 [Fix] scheduler: Honor pause_generation under PP and release aborted PD rooms and rejected sessions](https://github.com/sgl-project/sglang/pull/48992) | `lsyin/sched-pr27` | 37.6min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42354163215) |
| #42327577134<br>[#49001 [Feat] [AMD] custom-all-reduce: Run carv2 on MI450 with FABRIC handles and a gfx1250 table](https://github.com/sgl-project/sglang/pull/49001) | `users/wenkaidu/carv2-rocm-fabric` | 37.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42327577134) |
| #42351933812<br>[#48375 [Feat] PD: Publish spec_kv_layout so DSpark/DFlash prefill and decode must match](https://github.com/sgl-project/sglang/pull/48375) | `pd-spec-kv-layout` | 36.8min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42351933812) |
| #42293832287<br>[#48739 [Feat] kimi-k3.1: DSPARK and DFLASH under decode context parallelism](https://github.com/sgl-project/sglang/pull/48739) | `kpham/k31-dcp-spec-verify` | 36.3min | 2 | multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42293832287) |
| #42263377662<br>[#48468 [Chore] [NVIDIA] deps: Bump FlashInfer to 0.7.3 and migrate the NVLink one-sided all-to-all to flashinfer.moe_ep](https://github.com/sgl-project/sglang/pull/48468) | `flashinfer-0.7.3-moe-ep` | 33.9min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42263377662) |
| #42303562890<br>[#45862 [Perf] [NVIDIA] gemm: Add W8A16 small-M GEMM for GLM-5.2 block-FP8 decode projections](https://github.com/sgl-project/sglang/pull/45862) | `feat/glm52-fp8-fused-a-gemm` | 33.0min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42303562890) |
| #42320759667<br>[#48980 [Fix] deepseek-v4.1: Run attention on the real rows of an MLP-sync-padded extend](https://github.com/sgl-project/sglang/pull/48980) | `lsyin/dsv41-megamoe-tp-padding` | 30.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42320759667) |
| #42195273006<br>[#48739 [Feat] kimi-k3.1: DSPARK and DFLASH under decode context parallelism](https://github.com/sgl-project/sglang/pull/48739) | `kpham/k31-dcp-spec-verify` | 29.9min | 1 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42195273006) |
| #42267410089<br>[#48938 [Fix] watchdog: Let py-spy attach to watched processes in CI](https://github.com/sgl-project/sglang/pull/48938) | `fix-pyspy-ptrace-ci` | 28.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42267410089) |
| #42254280802<br>[#46645 [Fix] grammar: mask the startup stop tokens until the grammar can end](https://github.com/sgl-project/sglang/pull/46645) | `devin/pr-gramstop` | 27.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42254280802) |
| #42317006731<br>[#48980 [Fix] deepseek-v4.1: Run attention on the real rows of an MLP-sync-padded extend](https://github.com/sgl-project/sglang/pull/48980) | `lsyin/dsv41-megamoe-tp-padding` | 26.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42317006731) |
| #42314851933<br>[#46693 [Feat] [AMD] minimax: Support MiniMax-M3.1-Flash on MI350X / MI355X (gfx950)](https://github.com/sgl-project/sglang/pull/46693) | `m31-amd/integration` | 26.9min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42314851933) |
| #42314852493<br>[#47862 [Feat] [AMD] aiter: One folder of in-tree aiter tuned rows for every model](https://github.com/sgl-project/sglang/pull/47862) | `m31-amd/aiter-tuned-tables` | 26.2min | 3 | base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42314852493) |
| #42319040124<br>[#48763 [Feat] dflash: Serve MoE FFN drafts for DFlash and DSpark](https://github.com/sgl-project/sglang/pull/48763) | `dflash-family-moe-ffn` | 25.6min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42319040124) |
| #42295261408<br>[#48762 [Refactor] scheduler: Run every state check through SchedulerInvariantChecker.run](https://github.com/sgl-project/sglang/pull/48762) | `lsyin/sched-pr25` | 23.0min | 4 | multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42295261408) |
| #42355272049<br>[#47469 [Perf] [NVIDIA] attention: Add opt-in LiteTopK prefill indexer top-k for DSA (FP8) and DeepSeek-V4.1 (FP4) on SM100](https://github.com/sgl-project/sglang/pull/47469) | `litetopk-prefill` | 22.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42355272049) |
| #42270968319<br>[#47977 [Feat] mm: Add --disable-multimodal to serve a multimodal model text-only](https://github.com/sgl-project/sglang/pull/47977) | `jain-ria/disable-multimodal` | 22.0min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42270968319) |
| #42292662363<br>[#48762 [Refactor] scheduler: Run every state check through SchedulerInvariantChecker.run](https://github.com/sgl-project/sglang/pull/48762) | `lsyin/sched-pr25` | 18.9min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42292662363) |
| #42324315819<br>[#48993 [Refactor] attention: Let the DSV4 backend count the query rows of its prefill shared-read snapshot](https://github.com/sgl-project/sglang/pull/48993) | `lsyin/dsv4-prefill-row-count` | 18.8min | 7 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42324315819) |
| #42353049292<br>[#48992 [Fix] scheduler: Honor pause_generation under PP and release aborted PD rooms and rejected sessions](https://github.com/sgl-project/sglang/pull/48992) | `lsyin/sched-pr27` | 16.6min | 5 | base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42353049292) |
| #42326615190<br>[#48993 [Refactor] attention: Let the DSV4 backend count the query rows of its prefill shared-read snapshot](https://github.com/sgl-project/sglang/pull/48993) | `lsyin/dsv4-prefill-row-count` | 16.6min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42326615190) |
| #42335345749<br>[#48997 [Feat] scheduler: Run the state checks in the PD and PP loops and after a flush](https://github.com/sgl-project/sglang/pull/48997) | `lsyin/sched-pr26` | 15.1min | 6 | base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42335345749) |
| #42360493949<br>[#48217 [Refactor] custom-ar-v2: Single-word push epoch and consume-style pull semaphores](https://github.com/sgl-project/sglang/pull/48217) | `comm-push-epoch-protocol` | 12.2min | 9 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42360493949) |
| #42361293484<br>[#48217 [Refactor] custom-ar-v2: Single-word push epoch and consume-style pull semaphores](https://github.com/sgl-project/sglang/pull/48217) | `comm-push-epoch-protocol` | 11.4min | 10 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42361293484) |
| #42285108678<br>[#44152 [Feat] score/embedding: Add raw embeddings, score rids, encode input_ids, and schedule-decision logging](https://github.com/sgl-project/sglang/pull/44152) | `jsheng/score-embedding-features` | 10.0min | 10 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42285108678) |
| #42307727478<br>[#48762 [Refactor] scheduler: Run every state check through SchedulerInvariantChecker.run](https://github.com/sgl-project/sglang/pull/48762) | `lsyin/sched-pr25` | 8.3min | 8 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42307727478) |
| #42343676956 | `main-opt3-only-k` | 6.9min | 4 | base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42343676956) |
| #42354486070 | `dcp-fused-topk-main` | 5.2min | 9 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42354486070) |

---


## [Run #42380715488](https://github.com/sgl-project/sglang/actions/runs/42380715488)
- **分支**: `sm120-block32-native-deepgemm`
- **总耗时**: 58.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42380715488

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680424) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680424

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128427656372) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128427656498) |
| multimodal-gen-test-1-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213508) |
| multimodal-gen-test-1-npu-a3 (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213518) |
| multimodal-gen-test-4-npu-a3 (0) | 35.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213552) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213628) |
| multimodal-gen-test-4-npu-a3 (1) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213638) |
| base-b-test-1-npu-a3 / run (0) | 27.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213687) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213688) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213693) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213701) |
| base-b-test-16-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128428213769) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680379) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42380715488/job/128434680466) |


## [Run #42361293484](https://github.com/sgl-project/sglang/actions/runs/42361293484)
- **分支**: `comm-push-epoch-protocol`
- **总耗时**: 11.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42361293484

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707940) |
| multimodal-gen-test-4-npu-a3 (0) | 6.8min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707941) |
| multimodal-gen-test-1-npu-a3 (0) | 7.0min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707969) |
| multimodal-gen-test-1-npu-a3 (1) | 7.0min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707978) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载权重阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708038) |
| base-b-test-16-npu-a3 / run (0) | 7.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片时中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708047) |
| base-b-test-4-npu-a3 / run (1) | 6.8min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708072) |
| base-b-test-1-npu-a3 / run (0) | 6.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708101) |
| base-b-test-2-npu-a3 / run (0) | 7.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在加载权重过程中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708102) |
| base-b-test-4-npu-a3 / run (0) | 6.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708103) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707940

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例执行阶段出错；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707941

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact，说明测试用例执行阶段出错。退出码5对应 unittest errors，常见于 setUpClass 中 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707969

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明用例未正常产出结果；退出码5对应 unittest errors，最常见为 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370707978

- **base-b-test-8-npu-a3 / run (0)**: 日志显示各 TP/EP 进程正在加载权重时，runner 报错“Executing the custom container implementation failed”，属于自托管 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708038

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载至36%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码错误，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708047

- **base-b-test-4-npu-a3 / run (1)**: 日志显示容器实现执行失败（Executing the custom container implementation failed），提示联系自托管 runner 管理员；此前 NPU 推理正常，无代码异常，属 runner/容器环境故障。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708072

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非用例或代码本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708101

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载至 88% 时出现 'Executing the custom container implementation failed'，属于 runner/容器基础设施异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708102

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 NPU 推理正常进行后出现 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370708103

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370204100) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42361293484/job/128370204120) |


## [Run #42360493949](https://github.com/sgl-project/sglang/actions/runs/42360493949)
- **分支**: `comm-push-epoch-protocol`
- **总耗时**: 12.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42360493949

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 8.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158474) |
| multimodal-gen-test-4-npu-a3 (1) | 8.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158507) |
| base-b-test-2-npu-a3 / run (0) | 9.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158530) |
| base-b-test-4-npu-a3 / run (0) | 8.9min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158546) |
| multimodal-gen-test-4-npu-a3 (0) | 8.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158552) |
| base-b-test-16-npu-a3 / run (0) | 8.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片时中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158562) |
| base-b-test-4-npu-a3 / run (1) | 8.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在测试启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158614) |
| base-b-test-1-npu-a3 / run (0) | 8.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在测试启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158635) |
| multimodal-gen-test-1-npu-a3 (0) | 8.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368159005) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致unittest报errors而非用例未收集。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158474

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158507

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158530

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 tokenizer 初始化后立即报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158546

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158552

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在模型分片加载约78%时，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158562

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题；此前仅有 CANN/HDK 版本与 32 字节 padding 内存分配的警告，未见 Traceback 或退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158614

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；server 初始化后即中断，未出现 Traceback 或退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158635

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行异常。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368159005

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128367735386) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128367735417) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42360493949/job/128368158610) |


## [Run #42355272049](https://github.com/sgl-project/sglang/actions/runs/42355272049)
- **分支**: `litetopk-prefill`
- **总耗时**: 22.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42355272049

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 12.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128353869153) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128353869153

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128351965665) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128351965742) |
| base-b-test-2-npu-a3 / run (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42355272049/job/128352510813) |


## [Run #42354841044](https://github.com/sgl-project/sglang/actions/runs/42354841044)
- **分支**: `dcp-fused-topk-main`
- **总耗时**: 53.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42354841044

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194441) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194441

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128350682676) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128350682689) |
| multimodal-gen-test-1-npu-a3 (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144245) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144252) |
| multimodal-gen-test-4-npu-a3 (0) | 29.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144326) |
| multimodal-gen-test-4-npu-a3 (1) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144329) |
| base-b-test-16-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144349) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144464) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144474) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144475) |
| base-b-test-2-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144510) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128351144534) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194474) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354841044/job/128356194530) |


## [Run #42354486070](https://github.com/sgl-project/sglang/actions/runs/42354486070)
- **分支**: `dcp-fused-topk-main`
- **总耗时**: 5.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42354486070

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 1.2min | 环境问题 | 日志中未见实际测试错误，仅显示未找到 diffusion-failures/ 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024593) |
| multimodal-gen-test-4-npu-a3 (0) | 1.3min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略的中间日志确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024623) |
| multimodal-gen-test-1-npu-a3 (0) | 1.1min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024628) |
| base-b-test-16-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024637) |
| multimodal-gen-test-1-npu-a3 (1) | 1.0min | 环境问题 | 作业在测试执行前即失败，未产生测试产物，疑似环境/runner异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024681) |
| base-b-test-1-npu-a3 / run (0) | 1.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装 python3 后报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024734) |
| base-b-test-8-npu-a3 / run (0) | 1.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024739) |
| base-b-test-4-npu-a3 / run (0) | 0.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024750) |
| base-b-test-4-npu-a3 / run (1) | 2.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024793) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，作业在启动阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024872) |

- **multimodal-gen-test-4-npu-a3 (1)**: 作业日志被截断，缺少 unittest 退出码及 Traceback。可见信息仅为 upload-artifact 未找到 diffusion-failures/ 路径，属产物缺失；真实失败原因需查看被省略的测试执行段（可能为 setUpClass 中 server 启动失败）。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024593

- **multimodal-gen-test-4-npu-a3 (0)**: 日志可见部分仅有 Node.js 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback 或 RuntimeError。中间省略段可能含真实错误，建议查看完整日志中 setUpClass/server 启动相关报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024623

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 artifact 上传步骤，提示 No files were found with the provided path: diffusion-failures/，未出现测试脚本的 Traceback 或退出码 5 信息，无法确认具体失败原因，疑似测试未实际运行或产物目录缺失。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024628

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 apt 下载依赖过程中出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024637

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示上传产物时提示 diffusion-failures/ 目录不存在，说明测试脚本未生成失败产物；结合退出码5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024681

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在容器内 apt 安装 python3 过程中，属 runner/容器环境异常，非用例代码问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024734

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 apt 解包 mesa/net-tools 等依赖时，容器启动/执行异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024739

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，runner 无法启动指定 CANN 镜像容器，测试尚未开始执行，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024750


- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，作业在运行 k8s 容器步骤时失败，未进入测试阶段，属 runner/容器环境问题，非代码或用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128350024872

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128349559488) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354486070/job/128349559499) |


## [Run #42354453484](https://github.com/sgl-project/sglang/actions/runs/42354453484)
- **分支**: `pd-spec-kv-layout`
- **总耗时**: 78.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42354453484

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 6.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128364707053) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 6.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128364707114) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示模型分片加载刚开始（0/55）即报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非用例代码或性能问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128364707053

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，发生在 NPU graph 捕获阶段，属于 runner/容器环境异常，非用例代码或性能回归问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128364707114

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349497162) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349497204) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989760) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989811) |
| multimodal-gen-test-4-npu-a3 (1) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989825) |
| base-b-test-16-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989831) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989872) |
| base-b-test-4-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989911) |
| base-b-test-2-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989930) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128349989958) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128355907401) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128355907407) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354453484/job/128355907434) |


## [Run #42354163215](https://github.com/sgl-project/sglang/actions/runs/42354163215)
- **分支**: `lsyin/sched-pr27`
- **总耗时**: 37.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42354163215

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.8min | 环境问题 | 自托管 runner 的容器执行失败，作业在加载权重过程中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128355320592) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 6.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在服务就绪后被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128355320681) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 Multi-thread loading shards 加载到 2/282 时出现 'Executing the custom container implementation failed'，属于自托管 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128355320592

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 server 已启动并返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128355320681

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128348679576) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128348679602) |
| multimodal-gen-test-4-npu-a3 (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203595) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203612) |
| base-b-test-1-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203636) |
| base-b-test-2-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203664) |
| base-b-test-16-npu-a3 / run (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203673) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203710) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349203719) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128349204097) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42354163215/job/128355320633) |


## [Run #42353049292](https://github.com/sgl-project/sglang/actions/runs/42353049292)
- **分支**: `lsyin/sched-pr27`
- **总耗时**: 16.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42353049292

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 12.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598621) |
| multimodal-gen-test-4-npu-a3 (1) | 13.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598622) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598698) |
| base-b-test-4-npu-a3 / run (0) | 12.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598762) |
| base-b-test-1-npu-a3 / run (0) | 13.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598767) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 TokenizerManager 初始化后立即报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598621

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598622

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598698

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 NPU 推理仍在正常输出 prefill/decode 吞吐，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境/基础设施故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598762

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例或代码本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598767

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345179144) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345179251) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598636) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598679) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42353049292/job/128345598791) |


## [Run #42351933812](https://github.com/sgl-project/sglang/actions/runs/42351933812)
- **分支**: `pd-spec-kv-layout`
- **总耗时**: 36.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42351933812

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 10.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128347060076) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128347060152) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试请求正常返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner 容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128347060076

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128347060152

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128341868588) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128341868608) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214257) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214335) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214363) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214373) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214392) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214432) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214475) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128342214568) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42351933812/job/128347060085) |


## [Run #42350633219](https://github.com/sgl-project/sglang/actions/runs/42350633219)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 41.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42350633219

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128343050798) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128343050834) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128343050885) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128337890537) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128337890547) |
| multimodal-gen-test-4-npu-a3 (0) | 39.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271598) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271615) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271617) |
| multimodal-gen-test-4-npu-a3 (1) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271651) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271667) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271670) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271674) |
| base-b-test-16-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271694) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271711) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42350633219/job/128338271726) |


## [Run #42348866170](https://github.com/sgl-project/sglang/actions/runs/42348866170)
- **分支**: `pd-spec-kv-layout`
- **总耗时**: 43.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42348866170

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128338243574) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 16.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128338243660) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试请求正常返回 200 OK 后，突然报错 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128338243574

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例断言失败；此前 decode 日志正常，随后作业直接报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128338243660

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332561768) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332561813) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332906933) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332906946) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332906978) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332907042) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332907057) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332907082) |
| base-b-test-16-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332907130) |
| base-b-test-1-npu-a3 / run (0) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128332907153) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42348866170/job/128338243637) |


## [Run #42345180632](https://github.com/sgl-project/sglang/actions/runs/42345180632)
- **分支**: `m31-amd/integration`
- **总耗时**: 57.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42345180632

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128327541590) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128327541590

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321357137) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321357194) |
| multimodal-gen-test-1-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781616) |
| base-b-test-16-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781653) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781660) |
| multimodal-gen-test-1-npu-a3 (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781664) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781690) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781697) |
| multimodal-gen-test-4-npu-a3 (1) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781700) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781707) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781726) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128321781739) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128327541588) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42345180632/job/128327541701) |


## [Run #42343676956](https://github.com/sgl-project/sglang/actions/runs/42343676956)
- **分支**: `main-opt3-only-k`
- **总耗时**: 6.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42343676956

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 6.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823084) |
| base-b-test-4-npu-a3 / run (0) | 6.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823171) |
| base-b-test-1-npu-a3 / run (0) | 5.4min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823187) |
| multimodal-gen-test-4-npu-a3 (1) | 6.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823230) |

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 server 已启动并健康检查通过，随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时/基础设施故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823084

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试执行中报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823171

- **base-b-test-1-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823187

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示未找到 diffusion-failures/ 目录，无产物上传；退出码5表明 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823230

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823797) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361823939) |
| multimodal-gen-test-4-npu-a3 (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42343676956/job/128361824022) |


## [Run #42335345749](https://github.com/sgl-project/sglang/actions/runs/42335345749)
- **分支**: `lsyin/sched-pr26`
- **总耗时**: 15.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42335345749

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.3min | 环境问题 | 自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572607) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572610) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572619) |
| base-b-test-2-npu-a3 / run (0) | 11.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572648) |
| base-b-test-1-npu-a3 / run (0) | 11.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572649) |
| base-b-test-16-npu-a3 / run (0) | 11.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572691) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 返回200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572607

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 Multi-thread loading shards 加载到 18% 时出现 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572610

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约11分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572619

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572648

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572649

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 DeepseekV3 权重加载完成后报错 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572691

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128290994321) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128290994357) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572576) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42335345749/job/128291572727) |


## [Run #42327577134](https://github.com/sgl-project/sglang/actions/runs/42327577134)
- **分支**: `users/wenkaidu/carv2-rocm-fabric`
- **总耗时**: 37.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42327577134

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120247) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120247

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128266447366) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128266447375) |
| multimodal-gen-test-1-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120067) |
| multimodal-gen-test-1-npu-a3 (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120081) |
| multimodal-gen-test-4-npu-a3 (0) | 34.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120136) |
| multimodal-gen-test-4-npu-a3 (1) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120293) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120330) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120340) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120356) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120442) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42327577134/job/128267120567) |


## [Run #42326615190](https://github.com/sgl-project/sglang/actions/runs/42326615190)
- **分支**: `lsyin/dsv4-prefill-row-count`
- **总耗时**: 16.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42326615190

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 12.4min | 环境问题 | 日志中未见明确错误，但上传产物路径 diffusion-failures/ 不存在，疑似测试脚本未产出失败用例目录，作业以非零退出码结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100241) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100262) |
| multimodal-gen-test-1-npu-a3 (1) | 12.6min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100335) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败，疑似host OOM或进程被SIGKILL | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100351) |
| base-b-test-4-npu-a3 / run (0) | 12.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100372) |
| base-b-test-16-npu-a3 / run (0) | 12.4min | 超时 | Scheduler watchdog 超时导致容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100382) |
| base-b-test-2-npu-a3 / run (0) | 12.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100405) |
| base-b-test-1-npu-a3 / run (0) | 11.8min | 环境问题 | 自定义容器执行失败，作业在模型权重加载完成后被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100536) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，仅见 'No files were found with the provided path: diffusion-failures/'，说明测试失败用例目录未生成；结合退出码 5 推测 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），需查看完整日志中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100241

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约12分钟结束，退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100262

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100335

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，作业失败。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100351

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 NPU 推理正常进行中，随后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100372

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP13 EP13 的 Scheduler watchdog timeout（watchdog_timeout=300，soft=True），随后报错“Executing the custom container implementation failed”，作业因调度器看门狗超时而失败，属超时类问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100382

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题；此前 server 已启动并正常响应 expert distribution 请求。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100405

- **base-b-test-1-npu-a3 / run (0)**: 日志显示权重分片加载完成后报错“Executing the custom container implementation failed”，属自托管 runner 容器环境异常，非用例代码错误，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100536

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128263476137) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128263476167) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100389) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42326615190/job/128264100514) |


## [Run #42324315819](https://github.com/sgl-project/sglang/actions/runs/42324315819)
- **分支**: `lsyin/dsv4-prefill-row-count`
- **总耗时**: 18.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42324315819

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 15.5min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966093) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | 环境问题 | 日志中未见具体 Traceback，但用例退出码 5 表明 unittest 存在 errors，最可能是 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966107) |
| multimodal-gen-test-1-npu-a3 (1) | 15.2min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966153) |
| multimodal-gen-test-4-npu-a3 (1) | 15.4min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966218) |
| base-b-test-2-npu-a3 / run (0) | 15.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966273) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966282) |
| base-b-test-1-npu-a3 / run (0) | 14.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966322) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约15分钟结束，退出码5表明unittest有errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966093

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，仅见 Node 弃用警告与 'No files were found with the provided path: diffusion-failures/'，无真实错误堆栈。退出码 5 对应 unittest errors，常见于 setUpClass 时 server 启动失败（如 host OOM、进程被 SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966107

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成该目录（可能用例未产出失败样本或路径配置错误），导致 upload-artifact 步骤失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966153

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示退出码 5（unittest errors），上传产物时提示未找到 diffusion-failures/ 路径，说明测试在 setUpClass 阶段即失败，最可能是 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966218

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner/容器环境故障，非用例代码问题；此前 Gloo 仅连接 0 个 peer 也提示单卡环境异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966273

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 NPU 推理正常进行中，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966282

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966322

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258319038) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258319167) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966249) |
| base-b-test-4-npu-a3 / run (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966324) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42324315819/job/128258966347) |


## [Run #42320759667](https://github.com/sgl-project/sglang/actions/runs/42320759667)
- **分支**: `lsyin/dsv41-megamoe-tp-padding`
- **总耗时**: 30.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42320759667

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337054) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_tp1_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337054

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128244593872) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128244593915) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245336891) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245336947) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245336984) |
| base-b-test-16-npu-a3 / run (0) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337006) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337063) |
| base-b-test-2-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337170) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42320759667/job/128245337188) |


## [Run #42319040124](https://github.com/sgl-project/sglang/actions/runs/42319040124)
- **分支**: `dflash-family-moe-ffn`
- **总耗时**: 25.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42319040124

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 20.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239522063) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239522063

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128238938399) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128238938491) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239521842) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239521894) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239521944) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239521949) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239521956) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239521963) |
| base-b-test-16-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42319040124/job/128239522086) |


## [Run #42317006731](https://github.com/sgl-project/sglang/actions/runs/42317006731)
- **分支**: `lsyin/dsv41-megamoe-tp-padding`
- **总耗时**: 26.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42317006731

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914911) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914911

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235262812) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235262852) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914818) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914861) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914901) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914908) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914930) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235914981) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42317006731/job/128235915020) |


## [Run #42314853155](https://github.com/sgl-project/sglang/actions/runs/42314853155)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 51.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42314853155

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 11.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128236035472) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128236035472

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128224989219) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128224989291) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638468) |
| multimodal-gen-test-4-npu-a3 (0) | 32.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638501) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638529) |
| multimodal-gen-test-1-npu-a3 (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638566) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638611) |
| base-b-test-1-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638636) |
| base-b-test-2-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638671) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638690) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638698) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128225638801) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128236035470) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314853155/job/128236035560) |


## [Run #42314852493](https://github.com/sgl-project/sglang/actions/runs/42314852493)
- **分支**: `m31-amd/aiter-tuned-tables`
- **总耗时**: 26.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42314852493

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 18.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587829) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587831) |
| base-b-test-2-npu-a3 / run (0) | 6.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587955) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587829

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587831

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587955

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128224999996) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225000022) |
| multimodal-gen-test-4-npu-a3 (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587725) |
| multimodal-gen-test-4-npu-a3 (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587744) |
| base-b-test-8-npu-a3 / run (0) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587801) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587806) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314852493/job/128225587830) |


## [Run #42314851933](https://github.com/sgl-project/sglang/actions/runs/42314851933)
- **分支**: `m31-amd/integration`
- **总耗时**: 26.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42314851933

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632720) |
| base-b-test-4-npu-a3 / run (1) | 14.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632735) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632720

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632735

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225006946) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225006953) |
| multimodal-gen-test-4-npu-a3 (0) | 5.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632416) |
| base-b-test-1-npu-a3 / run (0) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632570) |
| multimodal-gen-test-4-npu-a3 (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632580) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632605) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632657) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42314851933/job/128225632742) |


## [Run #42307727478](https://github.com/sgl-project/sglang/actions/runs/42307727478)
- **分支**: `lsyin/sched-pr25`
- **总耗时**: 8.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42307727478

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 4.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408037) |
| base-b-test-16-npu-a3 / run (0) | 4.7min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408103) |
| base-b-test-4-npu-a3 / run (1) | 4.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408126) |
| multimodal-gen-test-4-npu-a3 (0) | 3.6min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408154) |
| base-b-test-1-npu-a3 / run (0) | 4.4min | 环境问题 | 自定义容器执行失败，作业在测试启动阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408253) |
| base-b-test-2-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408329) |
| base-b-test-8-npu-a3 / run (0) | 4.2min | 环境问题 | 自定义容器执行失败，作业在运行测试脚本时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408359) |
| base-b-test-4-npu-a3 / run (0) | 4.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408419) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408037

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器环境异常，非用例代码本身报错；测试刚开始执行 TestAscendDistTimeout.test_a_gsm8k 即中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408103

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器运行时环境故障，非用例代码问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408126

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中无 diffusion-failures 目录产物，说明用例未正常执行；退出码5对应 unittest errors，最常见为 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408154

- **base-b-test-1-npu-a3 / run (0)**: 日志显示执行自定义容器实现失败（Executing the custom container implementation failed），发生在 HiCache MHA 测试开始后不久，属于自托管 runner 容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408253

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在容器启动阶段，尚未进入用例执行，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408329

- **base-b-test-8-npu-a3 / run (0)**: 日志显示测试脚本开始执行后约44秒出现“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例断言失败，需联系 runner 管理员排查容器/节点。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408359

- **base-b-test-4-npu-a3 / run (0)**: 日志报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，容器未能正常启动，测试未真正执行，属 runner/容器环境问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128202408419

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128201459698) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42307727478/job/128201459814) |


## [Run #42303562890](https://github.com/sgl-project/sglang/actions/runs/42303562890)
- **分支**: `feat/glm52-fp8-fused-a-gemm`
- **总耗时**: 33.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42303562890

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857298) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857556) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 16s），其余用例均通过，因此该用例失败导致进程退出码为 1；日志未给出具体 Traceback，需查看该用例详细输出以定位原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857298

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857556

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128187976196) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128187976231) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857098) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857101) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857236) |
| multimodal-gen-test-4-npu-a3 (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857325) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857370) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857375) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857385) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42303562890/job/128188857390) |


## [Run #42298183607](https://github.com/sgl-project/sglang/actions/runs/42298183607)
- **分支**: `lsyin/sched-pr25`
- **总耗时**: 74.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42298183607

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128197348100) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 9.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128197348193) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示模型分片加载到51%时出现 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码或性能回归问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128197348100

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 prefill 正常进行后出现 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128197348193

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128169807386) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128169807493) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946155) |
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946180) |
| base-b-test-4-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946372) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946389) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946419) |
| base-b-test-2-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946477) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946535) |
| base-b-test-16-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128170946556) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128182504188) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128182504246) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42298183607/job/128182504276) |


## [Run #42295261408](https://github.com/sgl-project/sglang/actions/runs/42295261408)
- **分支**: `lsyin/sched-pr25`
- **总耗时**: 23.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42295261408

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 8.8min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277656) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | 环境问题 | 自托管 runner 的容器执行失败，作业在运行第7个测试文件时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277691) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | 环境问题 | 自定义容器执行失败，作业在启动容器阶段报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277755) |
| base-b-test-1-npu-a3 / run (0) | 17.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277767) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact，说明测试用例执行异常。退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277656

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，而非用例断言失败；前6个测试均通过，第7个测试启动后约12秒作业中断，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277691

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于自托管 runner 的容器启动/运行环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277755

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 DetokenizerManager 初始化后报错 'Executing the custom container implementation failed'，属于 runner 容器环境问题，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277767

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128159074517) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128159074596) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277670) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277736) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277877) |
| base-b-test-16-npu-a3 / run (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42295261408/job/128160277898) |


## [Run #42293832287](https://github.com/sgl-project/sglang/actions/runs/42293832287)
- **分支**: `kpham/k31-dcp-spec-verify`
- **总耗时**: 36.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42293832287

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105373) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105670) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约27分钟后结束，diffusion-failures目录无文件可上传，说明测试用例在setUpClass阶段即失败（可能server启动失败/OOM/SIGKILL），未产生失败产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105373

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_w4a4_quantization.py, npu_w4a4_quantization.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105670

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128154123505) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128154123507) |
| multimodal-gen-test-4-npu-a3 (1) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105370) |
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105431) |
| multimodal-gen-test-1-npu-a3 (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105502) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105590) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105600) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105686) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105756) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42293832287/job/128155105840) |


## [Run #42292662363](https://github.com/sgl-project/sglang/actions/runs/42292662363)
- **分支**: `lsyin/sched-pr25`
- **总耗时**: 18.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42292662363

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694507) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694619) |
| base-b-test-2-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在测试启动阶段被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694641) |
| base-b-test-16-npu-a3 / run (0) | 10.0min | 超时 | Scheduler watchdog 超时导致容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694661) |
| base-b-test-4-npu-a3 / run (0) | 10.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694707) |
| base-b-test-1-npu-a3 / run (0) | 10.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694751) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例未正常产出失败产物；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694507

- **base-b-test-4-npu-a3 / run (1)**: 日志显示模型分片加载到 18% 时出现 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题；随后进入清理流程。
  链接: https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694619

- **base-b-test-2-npu-a3 / run (0)**: 日志报错 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例代码问题；此时仅打印了 HCCL 环境变量，测试尚未真正运行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694641

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP6 EP6 Scheduler watchdog timeout（watchdog_timeout=300，soft=True），随后报错 custom container implementation failed，作业因调度器看门狗超时失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694661

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型分片加载完成后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694707

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694751

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128152518898) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128152518980) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694584) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42292662363/job/128153694906) |


## [Run #42292266983](https://github.com/sgl-project/sglang/actions/runs/42292266983)
- **分支**: `lsyin/sched-pr25`
- **总耗时**: 8.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42292266983

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 0.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581512) |
| multimodal-gen-test-4-npu-a3 (0) | 0.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581587) |
| base-b-test-2-npu-a3 / run (0) | 5.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581634) |
| base-b-test-1-npu-a3 / run (0) | 0.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581700) |
| base-b-test-8-npu-a3 / run (0) | 0.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581794) |
| base-b-test-4-npu-a3 / run (0) | 0.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581828) |
| base-b-test-4-npu-a3 / run (1) | 0.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128149581834) |








### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128148627647) |
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42292266983/job/128148627651) |


## [Run #42285108678](https://github.com/sgl-project/sglang/actions/runs/42285108678)
- **分支**: `jsheng/score-embedding-features`
- **总耗时**: 10.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42285108678

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102619) |
| multimodal-gen-test-1-npu-a3 (1) | 6.5min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102664) |
| multimodal-gen-test-4-npu-a3 (1) | 6.7min | 环境问题 | 日志中未见测试用例执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略的中间日志确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102686) |
| base-b-test-4-npu-a3 / run (0) | 6.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102698) |
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102707) |
| base-b-test-4-npu-a3 / run (1) | 6.4min | 环境问题 | 自定义容器执行失败，作业被 runner 中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102728) |
| multimodal-gen-test-1-npu-a3 (0) | 6.4min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102786) |
| base-b-test-1-npu-a3 / run (0) | 6.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102821) |
| base-b-test-8-npu-a3 / run (0) | 6.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102844) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片时中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102951) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产出结果。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102619

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行异常。退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102664

- **multimodal-gen-test-4-npu-a3 (1)**: 可见日志仅有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback 或退出码信息；中间省略部分可能含真实错误，无法据此断定具体失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102686

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型分片加载至88%时出现“Executing the custom container implementation failed”，属 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102698

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，容器实现执行失败，随后进入清理流程，未进入实际测试阶段，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102707

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境问题，并非用例断言失败；此前 server 仍在正常 decode 输出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102728

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中 upload-artifact 提示未找到 diffusion-failures/ 目录，说明用例未正常产出失败产物；结合退出码5，最可能是 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102786

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在第2个用例启动后约11秒，非用例断言失败，属 runner/容器环境异常，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102821

- **base-b-test-8-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例断言失败；此前仅有 Expert Balancedness 正常输出，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102844

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载到约12%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128125102951

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128123987272) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42285108678/job/128123987368) |


## [Run #42276169748](https://github.com/sgl-project/sglang/actions/runs/42276169748)
- **分支**: `jsheng/score-embedding-features`
- **总耗时**: 55.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42276169748

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367058) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367140) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367219) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367246) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367333) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367355) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128093191402) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128093191517) |
| multimodal-gen-test-1-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094366898) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094366930) |
| multimodal-gen-test-4-npu-a3 (0) | 33.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367000) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42276169748/job/128094367008) |


## [Run #42275307696](https://github.com/sgl-project/sglang/actions/runs/42275307696)
- **分支**: `moe-router-dedup`
- **总耗时**: 39.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42275307696

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242696) |
| base-b-test-4-npu-a3 / run (1) | 14.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242709) |
| base-b-test-4-npu-a3 / run (0) | 13.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242804) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242696

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242709

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242804

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128090226351) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128090226421) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242508) |
| multimodal-gen-test-1-npu-a3 (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242602) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242611) |
| multimodal-gen-test-4-npu-a3 (0) | 35.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242637) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242740) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242747) |
| base-b-test-16-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42275307696/job/128091242760) |


## [Run #42270968319](https://github.com/sgl-project/sglang/actions/runs/42270968319)
- **分支**: `jain-ria/disable-multimodal`
- **总耗时**: 22.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42270968319

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076814920) |
| base-b-test-2-npu-a3 / run (0) | 6.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076815180) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076815597) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076814920

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076815180


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128075401914) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128075401994) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076803757) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076803897) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076815088) |
| base-b-test-4-npu-a3 / run (1) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076815299) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42270968319/job/128076815382) |


## [Run #42267410089](https://github.com/sgl-project/sglang/actions/runs/42267410089)
- **分支**: `fix-pyspy-ptrace-ci`
- **总耗时**: 28.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42267410089

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 10.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795571) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795571

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128084526577) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128084526760) |
| multimodal-gen-test-4-npu-a3 (0) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795302) |
| multimodal-gen-test-4-npu-a3 (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795305) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795471) |
| base-b-test-8-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795594) |
| base-b-test-1-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795683) |
| base-b-test-16-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795718) |
| base-b-test-4-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42267410089/job/128085795740) |


## [Run #42263377662](https://github.com/sgl-project/sglang/actions/runs/42263377662)
- **分支**: `flashinfer-0.7.3-moe-ep`
- **总耗时**: 33.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42263377662

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 9.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332339) |
| base-b-test-4-npu-a3 / run (1) | 14.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332413) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332339

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332413

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128049087002) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128049087295) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332149) |
| multimodal-gen-test-4-npu-a3 (0) | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332252) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332302) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332336) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332406) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332419) |
| multimodal-gen-test-1-npu-a3 (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332517) |
| base-b-test-16-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42263377662/job/128050332668) |


## [Run #42254280802](https://github.com/sgl-project/sglang/actions/runs/42254280802)
- **分支**: `devin/pr-gramstop`
- **总耗时**: 27.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42254280802

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828460) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828460

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128017494314) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128017494415) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828368) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828427) |
| base-b-test-16-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828571) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828598) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828680) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018828748) |
| base-b-test-4-npu-a3 / run (1) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42254280802/job/128018829092) |


## [Run #42244763737](https://github.com/sgl-project/sglang/actions/runs/42244763737)
- **分支**: `F4_support`
- **总耗时**: 124.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42244763737

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 57.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464861) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约1小时后结束，退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  - 失败用例: mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464861

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127984177152) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127984177349) |
| multimodal-gen-test-4-npu-a3 (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464913) |
| base-b-test-16-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464966) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985464969) |
| base-b-test-4-npu-a3 / run (0) | 6.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985465027) |
| base-b-test-4-npu-a3 / run (1) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985465285) |
| multimodal-gen-test-1-npu-a3 (1) | 28.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985465554) |
| multimodal-gen-test-1-npu-a3 (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/127985466557) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/128010330305) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/128020849906) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42244763737/job/128020849936) |


## [Run #42195273006](https://github.com/sgl-project/sglang/actions/runs/42195273006)
- **分支**: `kpham/k31-dcp-spec-verify`
- **总耗时**: 29.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42195273006

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 7.6min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128148174369) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128148174403) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示模型分片加载到25%时出现“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128148174369


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139657597) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139657602) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139657913) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658024) |
| multimodal-gen-test-4-npu-a3 (0) | 36.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658074) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658356) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658357) |
| base-b-test-16-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658406) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658468) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658496) |
| multimodal-gen-test-1-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658528) |
| multimodal-gen-test-4-npu-a3 (1) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658568) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139658865) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139659283) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42195273006/job/128139661044) |


---
*Auto-generated by ci_monitor.py*