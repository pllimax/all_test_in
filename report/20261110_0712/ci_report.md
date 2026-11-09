# NPU CI 执行监控（2026-11-09）
**生成时间**: 2026-11-10 07:12
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-09 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 110

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1100 个 | 失败 148 个 | 成功 Job 平均耗时 15.5min
- **Run 执行情况**: 成功 63 个 | 失败 47 个 | 成功 Run 平均耗时 75.3min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 89.6min | #42615961538 | [job link](https://github.com/sgl-project/sglang/actions/runs/42615961538/job/129185806048) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 59.3min | #42595004172 | [job link](https://github.com/sgl-project/sglang/actions/runs/42595004172/job/129097396830) |
| base-b-test-4-npu-a3 / run (0) | 58.2min | #42615961538 | [job link](https://github.com/sgl-project/sglang/actions/runs/42615961538/job/129157081163) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 57.2min | #42552016518 | [job link](https://github.com/sgl-project/sglang/actions/runs/42552016518/job/129019314578) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.4min | #42547776794 | [job link](https://github.com/sgl-project/sglang/actions/runs/42547776794/job/129059192663) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 48.9min | #42566033808 | [job link](https://github.com/sgl-project/sglang/actions/runs/42566033808/job/129003670996) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.7min | #42559785443 | [job link](https://github.com/sgl-project/sglang/actions/runs/42559785443/job/128985518840) |
| multimodal-gen-test-4-npu-a3 (0) | 46.7min | #42516898155 | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500024) |
| base-b-test-1-npu-a3 / run (0) | 46.6min | #42615961538 | [job link](https://github.com/sgl-project/sglang/actions/runs/42615961538/job/129157081044) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 44.5min | #42557083365 | [job link](https://github.com/sgl-project/sglang/actions/runs/42557083365/job/128973442634) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 61.4min | #42612352671 | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993005) |
| multimodal-gen-test-4-npu-a3 (0) | 51.9min | #42627577165 | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959191) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.8min | #42617229266 | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129173861158) |
| multimodal-gen-test-4-npu-a3 (0) | 36.6min | #42548079234 | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014813) |
| multimodal-gen-test-4-npu-a3 (0) | 31.8min | #42584629925 | [job link](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272422) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.9min | #42593403200 | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129093205208) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | #42616249704 | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884916) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | #42634129413 | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296002) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | #42582476449 | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437382) |
| base-b-test-1-npu-a3 / run (0) | 19.4min | #42527569705 | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109998) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-16-npu-a3 / run (0) | 76 | 56 | 5 | 9 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961975039)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656432)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013643)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581430)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288849) |
| base-b-test-2-npu-a3 / run (0) | 89 | 72 | 5 | 8 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296002)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224525)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437430)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743724)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702416) |
| base-b-test-1-npu-a3 / run (0) | 84 | 68 | 4 | 7 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231678)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884916)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444965)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581455) |
| multimodal-gen-test-4-npu-a3 (0) | 87 | 73 | 10 | 0 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959191)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993005)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272422)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974892)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656293) |
| base-b-test-4-npu-a3 / run (0) | 91 | 75 | 3 | 7 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960589164)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013579)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977705) |
| base-b-test-8-npu-a3 / run (0) | 75 | 60 | 4 | 6 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181980)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656464)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581395)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702315) |
| base-b-test-4-npu-a3 / run (1) | 91 | 77 | 2 | 7 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014968)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977795) |
| multimodal-gen-test-4-npu-a3 (1) | 87 | 77 | 5 | 0 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974715)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656402)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862454)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581340)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959462) |
| multimodal-gen-test-1-npu-a3 (0) | 55 | 48 | 5 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862432)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013520)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581396)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702189)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128947463117) |
| multimodal-gen-test-1-npu-a3 (1) | 55 | 50 | 3 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862533)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013488)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128947462937) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 56 | 50 | 3 | 0 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42553077747/job/128955636045)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128957015776)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128952276405) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 47 | 44 | 1 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128950201060) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_pd_disaggregation.py` | 28 | 25 | 3 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960589164)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014968)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977795) |
| `mova_360p_ti2va_2npu` | 18 | 16 | 2 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959191)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993005) |
| `npu_mla_fia_hicache_bf16.py` | 27 | 25 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224525)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702416) |
| `npu_autoround_moe.py` | 21 | 19 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231678)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444965) |
| `wan2_2_t2v_14b_w8a8_2npu` | 19 | 18 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272422) |
| `minimax_h3_t2va_2npu` | 19 | 18 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272422) |
| `npu_return_indexer_topk_deepseek_v4.py` | 20 | 19 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296002) |
| `npu_expert_distribution_recorder_mode.py` | 21 | 20 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437430) |
| `npu_moe_dense_tp_size.py` | 22 | 21 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743724) |
| `npu_dp_attention.py` | 22 | 21 | 1 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977705) |
| `npu_sampling_backend.py` | 22 | 21 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581455) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 23 | 22 | 1 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181980) |
| `dspark_npu_dispatch.py` | 13 | 12 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884916) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #42627577165<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 109.9min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42627577165) |
| #42554844033<br>[#45718 [Feat] [NPU] memory-saver: Release device communication domains on sleep mode](https://github.com/sgl-project/sglang/pull/45718) | `hccl_clean` | 100.7min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42554844033) |
| #42612352671<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 78.8min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42612352671) |
| #42507953531<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 78.0min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42507953531) |
| #42634129413<br>[#47438 [Refactor] [NPU] dsv4: Migrate to the released CANN transformer operators](https://github.com/sgl-project/sglang/pull/47438) | `cann92_ops_port` | 76.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42634129413) |
| #42548972797<br>[#45205 [Feat] [AMD] hicache: Enable HiCache for DSA DCP with a packed MTP draft](https://github.com/sgl-project/sglang/pull/45205) | `amd/hicache-dsa-dcp-packed-mtp` | 69.0min | 1 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42548972797) |
| #42617229266<br>[#44736 [Fix] [NPU] CI: Update NPU failure analyzer coverage](https://github.com/sgl-project/sglang/pull/44736) | `fix_npu_diffusion_failure_analyzer` | 67.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42617229266) |
| #42593403200<br>[#48353 [Fix] [XPU] compressed-tensors: Support W8A8 int8 on XPU and quantize Whisper MLP linears.](https://github.com/sgl-project/sglang/pull/48353) | `fix/xpu-whisper-w8a8-int8` | 62.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42593403200) |
| #42549836753<br>[#48118 [Perf] [AMD] gdn: Add an aiter backend for linear-chain target verify](https://github.com/sgl-project/sglang/pull/48118) | `feature/yunkai/gdn-verify-aiter` | 52.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42549836753) |
| #42516898155<br>[#44152 [Feat] score/embedding: Add raw embeddings, score rids, encode input_ids, and schedule-decision logging](https://github.com/sgl-project/sglang/pull/44152) | `jsheng/score-embedding-features` | 50.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42516898155) |
| #42551913853<br>[#49332 [Perf] [AMD] mori: Read MORI EPv2 AsyncLL segmented receive in place, skipping the receive copy](https://github.com/sgl-project/sglang/pull/49332) | `mori_epv2_asyncll_tbo` | 47.5min | 3 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42551913853) |
| #42616249704<br>[#45862 [Perf] [NVIDIA] gemm: Add W8A16 small-M GEMM for GLM-5.2 block-FP8 decode projections](https://github.com/sgl-project/sglang/pull/45862) | `feat/glm52-fp8-fused-a-gemm` | 42.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42616249704) |
| #42544435658<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 41.7min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42544435658) |
| #42548079234<br>[#36153 [Feat] [Intel] diffusion: Add packed QKV kernel and enable Ulysses SP on CPU](https://github.com/sgl-project/sglang/pull/36153) | `cpu-ulysses-pack-qkv` | 40.5min | 2 | multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42548079234) |
| #42571201277<br>[#41329 [Feat] [CPU] quantization: Add CPU FP8/INT8 quant ops and compressed-tensors support](https://github.com/sgl-project/sglang/pull/41329) | `yanbing/cpu-fp8-quant-support` | 39.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42571201277) |
| #42584629925<br>[#44753 [Refactor] RoPE: Support RotaryEmbedding class usage for DiT models](https://github.com/sgl-project/sglang/pull/44753) | `rope_support_dits` | 39.7min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42584629925) |
| #42584038966<br>[#48787 [Perf] [XPU] fp8: Run FP8 dense layers weight-only (W8A16) through sgl_kernel.fp8_linear](https://github.com/sgl-project/sglang/pull/48787) | `upr/xpu-fp8-w8a16-linear-v3` | 38.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42584038966) |
| #42559424112<br>[#49228 [Feat] [MLU] ops: Add fused operator support](https://github.com/sgl-project/sglang/pull/49228) | `feat/mlu-fused-operators` | 38.3min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42559424112) |
| #42548054985<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 37.5min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42548054985) |
| #42564233794<br>[#47210 [Perf] [SM120] fp8: Use native block32 DeepGEMM for DSV4.1](https://github.com/sgl-project/sglang/pull/47210) | `sm120-block32-native-deepgemm` | 37.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42564233794) |
| #42570312200<br>[#33815 [Feat] [Intel] diffusion: Add rotary embedding kernel for CPU](https://github.com/sgl-project/sglang/pull/33815) | `sgl-diffusion-rope` | 36.4min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42570312200) |
| #42626808944<br>[#44736 [Fix] [NPU] CI: Update NPU failure analyzer coverage](https://github.com/sgl-project/sglang/pull/44736) | `fix_npu_diffusion_failure_analyzer` | 35.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42626808944) |
| #42554786181<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 30.6min | 5 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42554786181) |
| #42593089849<br>[#38371 [Perf][mem_cache] Persistent lazy eviction heap for the UnifiedRadixCache Full component (bit-identical order)](https://github.com/sgl-project/sglang/pull/38371) | `perf/unified-radix-lazy-eviction-heap` | 29.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42593089849) |
| #42555064606<br>[#39694 [Perf] mem_cache: Cap SWA windows per radix path with --swa-max-states-per-path](https://github.com/sgl-project/sglang/pull/39694) | `perf/dsv4-mooncake-integrated` | 29.5min | 4 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42555064606) |
| #42551785897<br>[#36153 [Feat] [Intel] diffusion: Add packed QKV kernel and enable Ulysses SP on CPU](https://github.com/sgl-project/sglang/pull/36153) | `cpu-ulysses-pack-qkv` | 29.4min | 4 | multimodal-gen-test-1-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42551785897) |
| #42575847178<br>[#47859 [Feat] moe: Add Mooncake Elastic EP scale-up support](https://github.com/sgl-project/sglang/pull/47859) | `elastic-base` | 28.4min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42575847178) |
| #42552669397<br>[#44152 [Feat] score/embedding: Add raw embeddings, score rids, encode input_ids, and schedule-decision logging](https://github.com/sgl-project/sglang/pull/44152) | `jsheng/score-embedding-features` | 27.6min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42552669397) |
| #42553457583<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 27.2min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42553457583) |
| #42582476449<br>[#49253 [Fix] scheduler: Retract every KV holder on pause and order a few releases behind in-flight steps](https://github.com/sgl-project/sglang/pull/49253) | `lsyin/sched-pr36` | 25.0min | 3 | base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42582476449) |
| #42555831078<br>[#48065 [Fix] [AMD] dsv4: Fix the mHC weight orientation across layer boundaries](https://github.com/sgl-project/sglang/pull/48065) | `dsv4-mhc-orientation-gfx1250_di_2/N` | 24.9min | 3 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42555831078) |
| #42527569705<br>[#49151 [Fix] scheduler: Finish rejected requests and offloaded releases through the request retirer](https://github.com/sgl-project/sglang/pull/49151) | `lsyin/retirer-bypass` | 23.0min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42527569705) |
| #42584055626<br>[#46213 [Perf] flashinfer-megamoe: Add an optional decode workspace](https://github.com/sgl-project/sglang/pull/46213) | `flashinfer-megamoe-autotune-decode-workspace` | 22.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42584055626) |
| #42571018715<br>[#44684 [Feat] HiSparse: Support DeepSeek-V4 with MTP and DSpark](https://github.com/sgl-project/sglang/pull/44684) | `dsv4_hisparse_dspark` | 22.4min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42571018715) |
| #42555385347<br>[#46499 [Feat] UnifiedL3: support mooncake storage backend](https://github.com/sgl-project/sglang/pull/46499) | `page-unified/mooncake-storage` | 18.1min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42555385347) |
| #42553077747<br>[#47658 [Perf] SM120: honour SGLANG_OPT_DEEPGEMM_HC_PRENORM for the DeepSeek-V4.1 compensated mhc projection](https://github.com/sgl-project/sglang/pull/47658) | `sm120-mhc-bf16x3-prenorm` | 17.6min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42553077747) |
| #42548867335<br>[#47287 [Perf] [AMD] Qwen3.5: enable fused GDN decode unpack + Conv1D for ROCm platform](https://github.com/sgl-project/sglang/pull/47287) | `opt/qwen35_gdn_decode_fused_proj_conv` | 15.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42548867335) |
| #42586723669<br>[#46213 [Perf] flashinfer-megamoe: Add an optional decode workspace](https://github.com/sgl-project/sglang/pull/46213) | `flashinfer-megamoe-autotune-decode-workspace` | 14.8min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42586723669) |
| #42585964598<br>[#47584 [Fix] [AMD] hicache: Book explicitly sized host pools against one host memory snapshot](https://github.com/sgl-project/sglang/pull/47584) | `fix/host-memory-budget-race` | 14.4min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42585964598) |
| #42586727150<br>[#49253 [Fix] scheduler: Retract every KV holder on pause and order a few releases behind in-flight steps](https://github.com/sgl-project/sglang/pull/49253) | `lsyin/sched-pr36` | 12.8min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42586727150) |
| #42625981239<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 11.3min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42625981239) |
| #42538007744<br>[#49207 [Fix] session: Defer a session close while an unfinished turn still reads its media](https://github.com/sgl-project/sglang/pull/49207) | `lsyin/sched-pr33` | 11.0min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42538007744) |
| #42585311128<br>[#49253 [Fix] scheduler: Retract every KV holder on pause and order a few releases behind in-flight steps](https://github.com/sgl-project/sglang/pull/49253) | `lsyin/sched-pr36` | 9.1min | 8 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42585311128) |
| #42611265528<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 9.0min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42611265528) |
| #42551170546<br>[#48646 [Fix] [XPU] diffusion/z-image: Fix missing QK norm + RoPE fusion path for B=1 (already used for B>1)](https://github.com/sgl-project/sglang/pull/48646) | `xpu/zimage-xpu-qknorm-rope-b1fix` | 8.4min | 2 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42551170546) |
| #42581004302<br>[#48093 [Perf] [AMD] dsv4: Cut HIP prefill and verify host overhead](https://github.com/sgl-project/sglang/pull/48093) | `dsv4-host-overhead-gfx1250_di_5/N` | 7.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42581004302) |
| #42564462239 | `mani1106/gdn-mis-delimiter-isolation` | 5.4min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42564462239) |

---


## [Run #42634129413](https://github.com/sgl-project/sglang/actions/runs/42634129413)
- **分支**: `cann92_ops_port`
- **总耗时**: 76.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42634129413

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 21.9min | 代码错误 | test_npu_return_indexer_topk_deepseek_v4.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296002) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296083) |

- **base-b-test-2-npu-a3 / run (0)**: TIMINGS 显示 test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py 的 passed 为 false（耗时 181s），其余用例均通过，最终进程以 exit code 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出以定位是 setUpClass 阶段 server 启动失败还是断言失败。
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296002


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129217956578) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129217956579) |
| multimodal-gen-test-4-npu-a3 (0) | 38.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219295810) |
| multimodal-gen-test-4-npu-a3 (1) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219295817) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296033) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296066) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296084) |
| base-b-test-4-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296181) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296218) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42634129413/job/129219296462) |


## [Run #42627577165](https://github.com/sgl-project/sglang/actions/runs/42627577165)
- **分支**: `F4_support`
- **总耗时**: 109.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42627577165

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 51.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959191) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约51分钟后结束，diffusion-failures目录无文件可上传，说明测试用例执行阶段出错。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  - 失败用例: mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959191

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129195592723) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129195593026) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959035) |
| multimodal-gen-test-4-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959137) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959148) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959377) |
| base-b-test-4-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959484) |
| base-b-test-16-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959523) |
| base-b-test-4-npu-a3 / run (1) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129196959589) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129207858110) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129221267693) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42627577165/job/129221267906) |


## [Run #42626808944](https://github.com/sgl-project/sglang/actions/runs/42626808944)
- **分支**: `fix_npu_diffusion_failure_analyzer`
- **总耗时**: 35.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42626808944

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 10.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231678) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231678

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129192962770) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129192962821) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231480) |
| multimodal-gen-test-1-npu-a3 (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231530) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231546) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231570) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231698) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231701) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231755) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231915) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42626808944/job/129194231941) |


## [Run #42625981239](https://github.com/sgl-project/sglang/actions/runs/42625981239)
- **分支**: `F4_support`
- **总耗时**: 11.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42625981239

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 7.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191207840) |
| multimodal-gen-test-4-npu-a3 (0) | 7.9min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208017) |
| multimodal-gen-test-4-npu-a3 (1) | 7.8min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208080) |
| multimodal-gen-test-1-npu-a3 (1) | 7.6min | 环境问题 | 作业失败但日志中未见具体错误，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208087) |
| base-b-test-4-npu-a3 / run (0) | 6.7min | 其他 | 日志显示测试全部通过，作业本身无失败迹象，失败可能发生在省略的中间日志段。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208363) |
| base-b-test-16-npu-a3 / run (0) | 2.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在依赖安装阶段中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208407) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208483) |
| base-b-test-4-npu-a3 / run (1) | 6.7min | 环境问题 | 自定义容器执行失败，服务健康检查返回503，作业被终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208734) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，符合unittest errors特征，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191207840

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产出结果。退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208017

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208080

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾仅提示未找到 diffusion-failures/ 路径，无 Traceback 或退出码信息；结合背景，可能是 setUpClass 阶段 server 启动失败导致用例 error，但日志被截断无法确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208087

- **base-b-test-4-npu-a3 / run (0)**: 可见日志中 test_npu_w4a4_quantization.py 通过（1/1 passed），退出码正常，仅 Node.js 20 弃用警告。失败原因应在被省略的中间日志中，需查看完整日志定位。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208363

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 pip 安装 triton-ascend 等依赖过程中报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208407

- **base-b-test-8-npu-a3 / run (0)**: 日志显示各 TP/EP 进程正在加载权重时，出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208483

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 /health_generate 返回 503 Service Unavailable，随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129191208734

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129190008380) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42625981239/job/129190008406) |


## [Run #42617229266](https://github.com/sgl-project/sglang/actions/runs/42617229266)
- **分支**: `fix_npu_diffusion_failure_analyzer`
- **总耗时**: 67.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42617229266

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129173861158) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试请求正常返回 200，随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129173861158

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129160202292) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129160202367) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161402969) |
| base-b-test-8-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403108) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403159) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403166) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403175) |
| multimodal-gen-test-4-npu-a3 (0) | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403210) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403223) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403343) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403366) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129161403417) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129173861074) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42617229266/job/129173861090) |


## [Run #42616249704](https://github.com/sgl-project/sglang/actions/runs/42616249704)
- **分支**: `feat/glm52-fp8-fused-a-gemm`
- **总耗时**: 42.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42616249704

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.9min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884916) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 14 秒），其余用例均通过，因此该用例失败使进程以退出码 1 结束；日志未给出具体 Traceback，需查看该用例详细输出。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884916

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129156926633) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129156926649) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884426) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884554) |
| multimodal-gen-test-4-npu-a3 (0) | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884563) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884613) |
| base-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884786) |
| base-b-test-16-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884787) |
| base-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884794) |
| base-b-test-4-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157884802) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42616249704/job/129157885021) |


## [Run #42612352671](https://github.com/sgl-project/sglang/actions/runs/42612352671)
- **分支**: `F4_support`
- **总耗时**: 78.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42612352671

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 61.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993005) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约1小时后结束。退出码5表明unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  - 失败用例: mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993005

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144048837) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144048903) |
| multimodal-gen-test-1-npu-a3 (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144992970) |
| multimodal-gen-test-4-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993027) |
| multimodal-gen-test-1-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993172) |
| base-b-test-4-npu-a3 / run (0) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993300) |
| base-b-test-4-npu-a3 / run (1) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993301) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993303) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129144993339) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129153093998) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129166556193) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42612352671/job/129166556234) |


## [Run #42611265528](https://github.com/sgl-project/sglang/actions/runs/42611265528)
- **分支**: `F4_support`
- **总耗时**: 9.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42611265528

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 5.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233700) |
| multimodal-gen-test-1-npu-a3 (1) | 5.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233742) |
| base-b-test-16-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233774) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233814) |
| multimodal-gen-test-4-npu-a3 (1) | 5.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233926) |
| base-b-test-4-npu-a3 / run (1) | 5.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233961) |
| base-b-test-4-npu-a3 / run (0) | 5.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233970) |
| base-b-test-8-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141234040) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业在约5分钟内结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233700

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示用例失败（退出码5，unittest errors），且未生成 diffusion-failures/ 目录产物。常见原因为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233742

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在模型加载/Tokenizer 初始化后，属 runner 容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233774

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233814

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233926

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码问题；后续仅为清理步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233961

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器执行环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141233970

- **base-b-test-8-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；此前 scheduler 初始化正常，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129141234040

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129140154872) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42611265528/job/129140155090) |


## [Run #42593403200](https://github.com/sgl-project/sglang/actions/runs/42593403200)
- **分支**: `fix/xpu-whisper-w8a8-int8`
- **总耗时**: 62.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42593403200

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.9min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129093205208) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明自托管 runner 的容器实现异常，导致作业在 decode 阶段被中断，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129093205208

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129080432062) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129080432147) |
| multimodal-gen-test-1-npu-a3 (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451440) |
| multimodal-gen-test-1-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451492) |
| multimodal-gen-test-4-npu-a3 (0) | 40.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451497) |
| multimodal-gen-test-4-npu-a3 (1) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451531) |
| base-b-test-16-npu-a3 / run (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451699) |
| base-b-test-4-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451853) |
| base-b-test-2-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451885) |
| base-b-test-1-npu-a3 / run (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451916) |
| base-b-test-4-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451972) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129081451978) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129093205192) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593403200/job/129093205230) |


## [Run #42593089849](https://github.com/sgl-project/sglang/actions/runs/42593089849)
- **分支**: `perf/unified-radix-lazy-eviction-heap`
- **总耗时**: 29.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42593089849

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224525) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224525

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129079337065) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129079337174) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224341) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224470) |
| base-b-test-1-npu-a3 / run (0) | 26.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224610) |
| base-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224641) |
| base-b-test-8-npu-a3 / run (0) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224676) |
| base-b-test-16-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224686) |
| base-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42593089849/job/129080224703) |


## [Run #42586727150](https://github.com/sgl-project/sglang/actions/runs/42586727150)
- **分支**: `lsyin/sched-pr36`
- **总耗时**: 12.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42586727150

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 9.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587878) |
| base-b-test-16-npu-a3 / run (0) | 9.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587934) |
| base-b-test-4-npu-a3 / run (0) | 8.7min | 环境问题 | 自定义容器执行失败，作业被 runner 中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587935) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587969) |
| base-b-test-1-npu-a3 / run (0) | 8.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059588004) |
| base-b-test-4-npu-a3 / run (1) | 8.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059588032) |
| base-b-test-2-npu-a3 / run (0) | 8.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059588132) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587878

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题；后续仅为清理步骤，未见用例 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587934

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例执行中（TestDPAttentionDP2TP2.test_regex_generate_phone）出现 ##[error]Executing the custom container implementation failed，提示联系 self-hosted runner 管理员，属于 runner/容器环境异常，非用例断言失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587935

- **base-b-test-8-npu-a3 / run (0)**: 日志中 test_npu_eplb_min_rebalancing_utilization_threshold.py 运行成功，Test Summary 为 1/1 passed，随后正常执行 Post job cleanup，未见任何 Traceback、RuntimeError 或非零退出码，无法从该日志定位失败原因，建议核对作业最终状态或获取完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587969

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已正常启动（Uvicorn 监听 11000），随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059588004

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 runner 无法启动指定 CANN 镜像容器，属基础设施/环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059588032

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059588132

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129058435457) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129058435540) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586727150/job/129059587983) |


## [Run #42586723669](https://github.com/sgl-project/sglang/actions/runs/42586723669)
- **分支**: `flashinfer-megamoe-autotune-decode-workspace`
- **总耗时**: 14.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42586723669

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129063397001) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 apt 安装 libsndio7.0 等包后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129063397001

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129058461896) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129058461897) |
| base-b-test-4-npu-a3 / run (1) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129059181402) |
| base-b-test-2-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129059181429) |
| base-b-test-1-npu-a3 / run (0) | 6.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129059181430) |
| base-b-test-4-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42586723669/job/129059181481) |


## [Run #42585964598](https://github.com/sgl-project/sglang/actions/runs/42585964598)
- **分支**: `fix/host-memory-budget-race`
- **总耗时**: 14.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42585964598

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656031) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656127) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656151) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656195) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656226) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656251) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129055929172) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129055929381) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056655989) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42585964598/job/129056656027) |


## [Run #42585311128](https://github.com/sgl-project/sglang/actions/runs/42585311128)
- **分支**: `lsyin/sched-pr36`
- **总耗时**: 9.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42585311128

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787742) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787746) |
| base-b-test-4-npu-a3 / run (0) | 5.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787759) |
| base-b-test-1-npu-a3 / run (0) | 5.2min | 环境问题 | 自定义容器执行失败，sglang server 健康检查返回 503，服务未就绪 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787764) |
| multimodal-gen-test-4-npu-a3 (1) | 5.0min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787771) |
| base-b-test-8-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787847) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787851) |
| base-b-test-4-npu-a3 / run (1) | 5.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787899) |

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码问题；此前仅有 tokenizer 慢速等警告，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787742

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787746

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787759

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 /health_generate 返回 503 Service Unavailable，随后报错“Executing the custom container implementation failed”，属于 runner 容器/环境异常，非用例代码问题，需联系 self-hosted runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787764

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787771

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在容器启动阶段，非用例代码问题，属 runner/容器环境故障。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787847

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，按背景知识为unittest errors，最常见原因是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787851

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 Load weight 后立即报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129054787899

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129053915999) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42585311128/job/129053916035) |


## [Run #42584629925](https://github.com/sgl-project/sglang/actions/runs/42584629925)
- **分支**: `rope_support_dits`
- **总耗时**: 39.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42584629925

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 31.8min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272422) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾显示上传 diffusion-failures-npu-2-part0-1.zip 工件，说明测试用例执行失败并产生失败产物；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272422

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129051578625) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272309) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272317) |
| multimodal-gen-test-4-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584629925/job/129052272375) |


## [Run #42584055626](https://github.com/sgl-project/sglang/actions/runs/42584055626)
- **分支**: `flashinfer-megamoe-autotune-decode-workspace`
- **总耗时**: 22.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42584055626

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 8.7min | 环境问题 | 自定义容器执行失败，服务健康检查持续返回503，server未就绪 | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129054696636) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 /health_generate 多次返回 503，随后报错 'Executing the custom container implementation failed'，属自托管 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129054696636

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129049638064) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129049638173) |
| base-b-test-4-npu-a3 / run (1) | 6.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129050638520) |
| base-b-test-2-npu-a3 / run (0) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129050638568) |
| base-b-test-4-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129050638593) |
| base-b-test-1-npu-a3 / run (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584055626/job/129050638636) |


## [Run #42584038966](https://github.com/sgl-project/sglang/actions/runs/42584038966)
- **分支**: `upr/xpu-fp8-w8a16-linear-v3`
- **总耗时**: 38.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42584038966

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728434) |
| base-b-test-4-npu-a3 / run (1) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728477) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728504) |
| base-b-test-16-npu-a3 / run (0) | 3.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728537) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728539) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728567) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129049602729) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129049602773) |
| multimodal-gen-test-4-npu-a3 (0) | 33.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728264) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728292) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728485) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42584038966/job/129050728497) |


## [Run #42582476449](https://github.com/sgl-project/sglang/actions/runs/42582476449)
- **分支**: `lsyin/sched-pr36`
- **总耗时**: 25.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42582476449

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 18.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437309) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在容器启动阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437382) |
| base-b-test-2-npu-a3 / run (0) | 13.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437430) |

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码或精度问题；此前仅有 Ascend 算子脚本的 SyntaxWarning，不影响执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437309

- **base-b-test-1-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明是 runner 侧容器实现异常，而非用例代码或精度问题；此前仅有 torch_npu 的 ImportWarning/RuntimeWarning，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437382

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437430

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129044423208) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129044423236) |
| multimodal-gen-test-4-npu-a3 (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437264) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437269) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437405) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437457) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42582476449/job/129045437480) |


## [Run #42581004302](https://github.com/sgl-project/sglang/actions/runs/42581004302)
- **分支**: `dsv4-host-overhead-gfx1250_di_5/N`
- **总耗时**: 7.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42581004302

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42581004302/job/129040465935) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42581004302/job/129039593208) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42581004302/job/129039593254) |


## [Run #42575847178](https://github.com/sgl-project/sglang/actions/runs/42575847178)
- **分支**: `elastic-base`
- **总耗时**: 28.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42575847178

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 9.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181980) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024182047) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181980


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129023419090) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129023419182) |
| multimodal-gen-test-4-npu-a3 (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181788) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181800) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181937) |
| base-b-test-4-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024181938) |
| base-b-test-1-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024182039) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575847178/job/129024182063) |


## [Run #42571201277](https://github.com/sgl-project/sglang/actions/runs/42571201277)
- **分支**: `yanbing/cpu-fp8-quant-support`
- **总耗时**: 39.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42571201277

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009654922) |
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009655003) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009655032) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009655037) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009655046) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009655119) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129008842045) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129008842060) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009654820) |
| multimodal-gen-test-4-npu-a3 (0) | 35.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009654834) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009654843) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571201277/job/129009654885) |


## [Run #42571018715](https://github.com/sgl-project/sglang/actions/runs/42571018715)
- **分支**: `dsv4_hisparse_dspark`
- **总耗时**: 22.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42571018715

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009083988) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009084009) |
| base-b-test-16-npu-a3 / run (0) | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009084091) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009084107) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009084144) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009084199) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129008269465) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129008269513) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009083881) |
| multimodal-gen-test-4-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42571018715/job/129009083892) |


## [Run #42570312200](https://github.com/sgl-project/sglang/actions/runs/42570312200)
- **分支**: `sgl-diffusion-rope`
- **总耗时**: 36.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42570312200

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761526) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761563) |
| base-b-test-2-npu-a3 / run (0) | 1.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761600) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761640) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006046001) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006046034) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761482) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761500) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761508) |
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42570312200/job/129006761511) |


## [Run #42564462239](https://github.com/sgl-project/sglang/actions/runs/42564462239)
- **分支**: `mani1106/gdn-mis-delimiter-isolation`
- **总耗时**: 5.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42564462239

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 1.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42564462239/job/128988490546) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 1.9min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，作业在安装 Rust 组件时中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42564462239/job/128988490563) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 apt 安装依赖后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42564462239/job/128988490546

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 rustup 下载 1.92 组件过程中报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42564462239/job/128988490563

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564462239/job/128987949229) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564462239/job/128987949262) |


## [Run #42564233794](https://github.com/sgl-project/sglang/actions/runs/42564233794)
- **分支**: `sm120-block32-native-deepgemm`
- **总耗时**: 37.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42564233794

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743724) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moe_dense_tp_size.py, npu_moe_dense_tp_size.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743724

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987221387) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987221399) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743651) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743684) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743697) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743708) |
| multimodal-gen-test-4-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743731) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743740) |
| base-b-test-1-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743742) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743751) |
| base-b-test-4-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42564233794/job/128987743778) |


## [Run #42559424112](https://github.com/sgl-project/sglang/actions/runs/42559424112)
- **分支**: `feat/mlu-fused-operators`
- **总耗时**: 38.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42559424112

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 15.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444965) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019445059) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444965


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129018641039) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129018641171) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444823) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444835) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444873) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444885) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444905) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444959) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019444961) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42559424112/job/129019445029) |


## [Run #42555831078](https://github.com/sgl-project/sglang/actions/runs/42555831078)
- **分支**: `dsv4-mhc-orientation-gfx1250_di_2/N`
- **总耗时**: 24.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42555831078

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974715) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974892) |
| base-b-test-16-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961975039) |

- **multimodal-gen-test-4-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业未真正执行测试。需检查镜像名/标签是否存在、私有仓库 imagePullSecret 凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974715

- **multimodal-gen-test-4-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业未执行即失败。需检查镜像名/标签、私有仓库凭据及节点到仓库的网络。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974892

- **base-b-test-16-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败超过300秒，Pod 一直 Pending，需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961975039

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961308876) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961308970) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974863) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961974947) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961975019) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961975024) |
| base-b-test-2-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555831078/job/128961975154) |


## [Run #42555385347](https://github.com/sgl-project/sglang/actions/runs/42555385347)
- **分支**: `page-unified/mooncake-storage`
- **总耗时**: 18.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42555385347

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 14.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960589164) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960589164

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128959926750) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128959926754) |
| base-b-test-4-npu-a3 / run (1) | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960588993) |
| base-b-test-2-npu-a3 / run (0) | 6.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960588995) |
| base-b-test-1-npu-a3 / run (0) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555385347/job/128960589021) |


## [Run #42555064606](https://github.com/sgl-project/sglang/actions/runs/42555064606)
- **分支**: `perf/dsv4-mooncake-integrated`
- **总耗时**: 29.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42555064606

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656293) |
| multimodal-gen-test-4-npu-a3 (1) | 5.9min | 环境问题 | Pod 镜像拉取失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656402) |
| base-b-test-16-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656432) |
| base-b-test-8-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器进入 ImagePullBackOff 状态 | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656464) |

- **multimodal-gen-test-4-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过 300s 宽限期，Pod 一直处于 Pending，作业未真正执行测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656293

- **multimodal-gen-test-4-npu-a3 (1)**: 容器镜像 cann:9.1.0-a3-ubuntu22.04-py3.12 持续 ImagePullBackOff 超过300秒，Pod 一直 Pending，作业在准备阶段即失败，与用例代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656402

- **base-b-test-16-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败超过300秒，Pod 一直 Pending，需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656432

- **base-b-test-8-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 317 秒超过 300 秒宽限期，Pod 一直处于 Pending，作业未开始执行测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656464

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128958941799) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128958941836) |
| multimodal-gen-test-1-npu-a3 (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656317) |
| multimodal-gen-test-1-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656352) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656462) |
| base-b-test-1-npu-a3 / run (0) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656472) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656591) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42555064606/job/128959656598) |


## [Run #42554844033](https://github.com/sgl-project/sglang/actions/runs/42554844033)
- **分支**: `hccl_clean`
- **总耗时**: 100.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42554844033

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 5.6min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862432) |
| multimodal-gen-test-4-npu-a3 (1) | 5.9min | 环境问题 | Pod 拉取镜像失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862454) |
| multimodal-gen-test-1-npu-a3 (1) | 6.0min | 环境问题 | Pod 拉取镜像失败导致作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862533) |
| multimodal-gen-test-4-npu-a3 (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862680) |

- **multimodal-gen-test-1-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败（ImagePullBackOff），重试305秒超过300秒宽限，Pod 一直 Pending，作业无法执行。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862432

- **multimodal-gen-test-4-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过300秒，Pod 一直处于 Pending，作业未真正执行测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862454

- **multimodal-gen-test-1-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过300秒宽限期，Pod 一直 Pending，后续步骤因 jobPod 未就绪报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862533

- **multimodal-gen-test-4-npu-a3 (0)**: 容器 job 拉取镜像 cann:9.1.0-a3-ubuntu22.04-py3.12 持续 ImagePullBackOff 超过 300 秒，Pod 一直 Pending，作业未真正执行测试。需检查镜像名/标签是否存在、私有仓库 imagePullSecret 凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862680

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958274433) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958274444) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862520) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862550) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862629) |
| base-b-test-2-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862646) |
| base-b-test-16-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862649) |
| base-b-test-1-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128958862654) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 41.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128965860380) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128965860456) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128965860520) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128977294273) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554844033/job/128977294430) |


## [Run #42554786181](https://github.com/sgl-project/sglang/actions/runs/42554786181)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 30.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42554786181

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013479) |
| multimodal-gen-test-1-npu-a3 (1) | 5.6min | 环境问题 | Pod 镜像拉取失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013488) |
| multimodal-gen-test-1-npu-a3 (0) | 5.6min | 环境问题 | Pod 镜像拉取失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013520) |
| base-b-test-4-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器进入 ImagePullBackOff 状态，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013579) |
| base-b-test-16-npu-a3 / run (0) | 5.8min | 环境问题 | 容器镜像拉取失败导致 Pod 无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013643) |

- **multimodal-gen-test-4-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 301s），Pod 一直处于 Pending，作业未真正执行测试。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013479

- **multimodal-gen-test-1-npu-a3 (1)**: 容器镜像 cann:9.1.0-a3-ubuntu22.04-py3.12 持续 ImagePullBackOff 超过 300 秒，Pod 一直 Pending，作业无法执行。需检查镜像名/标签是否存在、私有仓库 imagePullSecret 凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013488

- **multimodal-gen-test-1-npu-a3 (0)**: 容器镜像 cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败（ImagePullBackOff），超过300秒宽限期，Pod 一直 Pending，作业无法执行。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013520

- **base-b-test-4-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 317 秒超过 300 秒宽限期，Pod 一直处于 Pending。需检查镜像名与 tag 是否存在、私有仓库的 imagePullSecret 凭据，以及节点到仓库的网络（DNS、防火墙、代理、TLS）。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013579

- **base-b-test-16-npu-a3 / run (0)**: Pod 拉取镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 时持续 ImagePullBackOff，超过 300 秒宽限期，容器未就绪，作业在启动阶段即失败，未执行任何测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013643

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128958267649) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128958267710) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013550) |
| base-b-test-1-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013561) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013592) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013652) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42554786181/job/128959013665) |


## [Run #42553457583](https://github.com/sgl-project/sglang/actions/runs/42553457583)
- **分支**: `new-model-support`
- **总耗时**: 27.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42553457583

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 5.6min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581340) |
| base-b-test-8-npu-a3 / run (0) | 5.8min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581395) |
| multimodal-gen-test-1-npu-a3 (0) | 5.7min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581396) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581407) |
| base-b-test-16-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581430) |
| base-b-test-1-npu-a3 / run (0) | 8.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581455) |

- **multimodal-gen-test-4-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业无法执行。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581340

- **base-b-test-8-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 301 秒超过 300 秒宽限期，Pod 一直 Pending。需检查镜像名/tag 是否存在、私有仓库 imagePullSecret 凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581395

- **multimodal-gen-test-1-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业无法执行。需检查镜像名/tag、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581396

- **multimodal-gen-test-4-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业无法执行。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581407

- **base-b-test-16-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败（ImagePullBackOff），超过300秒宽限期，Pod 一直 Pending，作业未执行测试即退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581430

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581455

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128953992966) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128953993027) |
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581350) |
| base-b-test-2-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581414) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581488) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553457583/job/128954581541) |


## [Run #42553077747](https://github.com/sgl-project/sglang/actions/runs/42553077747)
- **分支**: `sm120-mhc-bf16x3-prenorm`
- **总耗时**: 17.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42553077747

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.9min | 环境问题 | Pod 镜像拉取失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42553077747/job/128955636045) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业未进入测试阶段。需检查镜像名/tag 是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42553077747/job/128955636045

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553077747/job/128952854623) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553077747/job/128952854699) |
| base-b-test-2-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42553077747/job/128953494996) |


## [Run #42552669397](https://github.com/sgl-project/sglang/actions/runs/42552669397)
- **分支**: `jsheng/score-embedding-features`
- **总耗时**: 27.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42552669397

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288849) |

- **base-b-test-16-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败超过 300 秒，Pod 一直 Pending，需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288849

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128951584795) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128951584814) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288697) |
| multimodal-gen-test-4-npu-a3 (0) | 6.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288714) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288813) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288819) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288843) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288851) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42552669397/job/128952288860) |


## [Run #42551913853](https://github.com/sgl-project/sglang/actions/runs/42551913853)
- **分支**: `mori_epv2_asyncll_tbo`
- **总耗时**: 47.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42551913853

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959462) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959478) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.8min | 环境问题 | 镜像拉取失败导致 Pod 无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128957015776) |

- **multimodal-gen-test-4-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过 300 秒宽限期，Pod 一直处于 Pending，作业无法执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959462

- **multimodal-gen-test-4-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败（ImagePullBackOff），超过300秒宽限期，Pod 一直处于 Pending，作业未能开始执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959478

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业未进入测试阶段。需检查镜像名/tag 是否存在、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128957015776

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949270531) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949270540) |
| base-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959559) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959577) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959584) |
| base-b-test-16-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959586) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959588) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128949959600) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128957015701) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551913853/job/128957015765) |


## [Run #42551785897](https://github.com/sgl-project/sglang/actions/runs/42551785897)
- **分支**: `cpu-ulysses-pack-qkv`
- **总耗时**: 29.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42551785897

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 5.9min | 环境问题 | Pod 拉取镜像失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702189) |
| base-b-test-8-npu-a3 / run (0) | 5.9min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702315) |
| base-b-test-2-npu-a3 / run (0) | 7.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702416) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | Pod 拉取镜像失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702486) |

- **multimodal-gen-test-1-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过300秒宽限期，Pod 一直 Pending，作业无法运行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702189

- **base-b-test-8-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 317 秒超过 300 秒宽限期，Pod 一直 Pending。需检查镜像名/tag 是否存在、私有仓库 imagePullSecret 凭据、节点到仓库的网络（DNS/防火墙/代理/TLS）。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702315

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702416

- **multimodal-gen-test-4-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过300秒宽限期，Pod 一直 Pending，作业未执行即失败。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库网络。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702486

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128948944661) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128948944711) |
| multimodal-gen-test-4-npu-a3 (1) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702279) |
| base-b-test-1-npu-a3 / run (0) | 24.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702286) |
| multimodal-gen-test-1-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702322) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702382) |
| base-b-test-4-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702431) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551785897/job/128949702453) |


## [Run #42551170546](https://github.com/sgl-project/sglang/actions/runs/42551170546)
- **分支**: `xpu/zimage-xpu-qknorm-rope-b1fix`
- **总耗时**: 8.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42551170546

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 5.6min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128947462937) |
| multimodal-gen-test-1-npu-a3 (0) | 5.6min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128947463117) |

- **multimodal-gen-test-1-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过 300 秒宽限期，Pod 一直处于 Pending，作业未真正执行测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128947462937

- **multimodal-gen-test-1-npu-a3 (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取持续失败（ImagePullBackOff 超 300s），Pod 一直 Pending，作业未真正执行测试。需检查镜像名/标签是否存在、私有仓库凭据及节点到仓库的网络。
  链接: https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128947463117

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42551170546/job/128946998976) |


## [Run #42549836753](https://github.com/sgl-project/sglang/actions/runs/42549836753)
- **分支**: `feature/yunkai/gdn-verify-aiter`
- **总耗时**: 52.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42549836753

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.8min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128952276405) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败（ImagePullBackOff），超过300秒宽限期，Pod 一直 Pending，作业未执行任何测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128952276405

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128942828339) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128942828424) |
| multimodal-gen-test-1-npu-a3 (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550792) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550880) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550882) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550926) |
| base-b-test-2-npu-a3 / run (0) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550966) |
| multimodal-gen-test-1-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550975) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550980) |
| multimodal-gen-test-4-npu-a3 (0) | 36.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943550999) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943551007) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128943551097) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128952276425) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42549836753/job/128952276571) |


## [Run #42548972797](https://github.com/sgl-project/sglang/actions/runs/42548972797)
- **分支**: `amd/hicache-dsa-dcp-packed-mtp`
- **总耗时**: 69.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42548972797

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 5.8min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128950201060) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过 300 秒宽限期，Pod 一直 Pending，作业未执行测试即退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128950201060

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128940164947) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128940165105) |
| base-b-test-1-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128940768143) |
| base-b-test-2-npu-a3 / run (0) | 6.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128940768181) |
| base-b-test-4-npu-a3 / run (1) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128940768187) |
| base-b-test-4-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128940768277) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128944173580) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548972797/job/128950201049) |


## [Run #42548867335](https://github.com/sgl-project/sglang/actions/runs/42548867335)
- **分支**: `opt/qwen35_gdn_decode_fused_proj_conv`
- **总耗时**: 15.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42548867335

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358403) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358424) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358428) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358432) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358495) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358550) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128939861382) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128939861415) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358401) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548867335/job/128940358417) |


## [Run #42548079234](https://github.com/sgl-project/sglang/actions/runs/42548079234)
- **分支**: `cpu-ulysses-pack-qkv`
- **总耗时**: 40.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42548079234

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 36.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014813) |
| base-b-test-4-npu-a3 / run (1) | 15.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014968) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产生输出。退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014813

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014968

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128937433571) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128937433588) |
| multimodal-gen-test-4-npu-a3 (1) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014760) |
| base-b-test-2-npu-a3 / run (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014830) |
| multimodal-gen-test-1-npu-a3 (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014860) |
| multimodal-gen-test-1-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014863) |
| base-b-test-4-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014864) |
| base-b-test-16-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014909) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938014920) |
| base-b-test-1-npu-a3 / run (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548079234/job/128938015070) |


## [Run #42548054985](https://github.com/sgl-project/sglang/actions/runs/42548054985)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 37.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42548054985

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977705) |
| base-b-test-4-npu-a3 / run (1) | 17.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977795) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977705

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977795

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937431475) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937431523) |
| multimodal-gen-test-1-npu-a3 (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977475) |
| multimodal-gen-test-4-npu-a3 (1) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977478) |
| multimodal-gen-test-1-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977520) |
| multimodal-gen-test-4-npu-a3 (0) | 33.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977529) |
| base-b-test-2-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977592) |
| base-b-test-1-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977604) |
| base-b-test-16-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977688) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42548054985/job/128937977760) |


## [Run #42544435658](https://github.com/sgl-project/sglang/actions/runs/42544435658)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 41.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42544435658

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 8.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128934965388) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 8.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在模型分片加载过程中被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128934965480) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 pip 构建 wheel 过程中报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境异常，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128934965388

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载到约89%时出现“Executing the custom container implementation failed”，属于 runner/容器环境异常，并非用例收集或代码断言失败，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128934965480

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128926356336) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128926356361) |
| multimodal-gen-test-4-npu-a3 (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022728) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022752) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022757) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022762) |
| base-b-test-16-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022819) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022895) |
| base-b-test-2-npu-a3 / run (0) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022921) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022964) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022965) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128927022991) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42544435658/job/128934965470) |


## [Run #42538007744](https://github.com/sgl-project/sglang/actions/runs/42538007744)
- **分支**: `lsyin/sched-pr33`
- **总耗时**: 11.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42538007744

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 8.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911799949) |
| base-b-test-1-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800055) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800074) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800094) |
| base-b-test-16-npu-a3 / run (0) | 8.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800097) |
| base-b-test-2-npu-a3 / run (0) | 7.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800113) |
| base-b-test-4-npu-a3 / run (1) | 8.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800149) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试未正常产出结果；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911799949

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到25%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器运行时故障，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800055

- **base-b-test-8-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例代码或精度问题；此前测试仍在正常输出 Expert Balancedness 日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800074

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员；此前测试用例已正常执行并返回 200 OK，失败发生在容器执行层而非用例断言，属 runner/容器环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800094

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载至58%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码错误，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800097

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载到 12% 时出现 'Executing the custom container implementation failed'，属于 runner/容器基础设施故障，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800113

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner 容器环境故障，并非用例断言失败；请求虽返回 200，但容器执行异常使作业失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911800149

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911230014) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911230067) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42538007744/job/128911799936) |


## [Run #42527569705](https://github.com/sgl-project/sglang/actions/runs/42527569705)
- **分支**: `lsyin/retirer-bypass`
- **总耗时**: 23.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42527569705

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 18.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109996) |
| base-b-test-1-npu-a3 / run (0) | 19.4min | 环境问题 | 自定义容器执行失败，作业在运行第6个用例时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109998) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在 NPU graph 捕获阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875110014) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，并非用例本身失败；此前测试均正常通过，失败发生在第4个用例启动时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109996

- **base-b-test-1-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed”，发生在运行 test_npu_eagle3.py 期间，属于自托管 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109998

- **base-b-test-4-npu-a3 / run (0)**: 日志显示在 Capture decode NPU graph 时出现 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码错误；随后进入清理流程，未出现 unittest 报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875110014

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128874575643) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128874575656) |
| multimodal-gen-test-4-npu-a3 (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109850) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109909) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109917) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109927) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42527569705/job/128875109978) |


## [Run #42516898155](https://github.com/sgl-project/sglang/actions/runs/42516898155)
- **分支**: `jsheng/score-embedding-features`
- **总耗时**: 50.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42516898155

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500104) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500115) |
| base-b-test-2-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500143) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500170) |
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500191) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500239) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128841886517) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128841886587) |
| multimodal-gen-test-4-npu-a3 (0) | 46.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500024) |
| multimodal-gen-test-1-npu-a3 (0) | 31.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500043) |
| multimodal-gen-test-1-npu-a3 (1) | 33.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500048) |
| multimodal-gen-test-4-npu-a3 (1) | 35.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42516898155/job/128842500102) |


## [Run #42507953531](https://github.com/sgl-project/sglang/actions/runs/42507953531)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 78.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42507953531

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 12.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128906233902) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 12.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128906233918) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，并非用例本身失败；前一个 perf 用例已正常完成并输出 throughput 指标。
  链接: https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128906233902

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例或代码本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128906233918

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890259613) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890259708) |
| multimodal-gen-test-4-npu-a3 (0) | 40.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860192) |
| multimodal-gen-test-4-npu-a3 (1) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860247) |
| multimodal-gen-test-1-npu-a3 (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860255) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860259) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860282) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860296) |
| multimodal-gen-test-1-npu-a3 (1) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860301) |
| base-b-test-2-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860317) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860374) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128890860408) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128897693902) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128897693908) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42507953531/job/128897693941) |


---
*Auto-generated by ci_monitor.py*