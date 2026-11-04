# NPU CI 执行监控（2026-11-03）
**生成时间**: 2026-11-04 09:50
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-03 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 200

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1862 个 | 失败 382 个 | 成功 Job 平均耗时 14.3min
- **Run 执行情况**: 成功 104 个 | 失败 96 个 | 成功 Run 平均耗时 78.2min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 67.2min | #41634481961 | [job link](https://github.com/sgl-project/sglang/actions/runs/41634481961/job/125943077293) |
| base-b-test-4-npu-a3 / run (0) | 60.4min | #41634481961 | [job link](https://github.com/sgl-project/sglang/actions/runs/41634481961/job/125913427837) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 58.9min | #41601700181 | [job link](https://github.com/sgl-project/sglang/actions/runs/41601700181/job/125812478547) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 56.3min | #41567796775 | [job link](https://github.com/sgl-project/sglang/actions/runs/41567796775/job/125709884165) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 53.2min | #41564653072 | [job link](https://github.com/sgl-project/sglang/actions/runs/41564653072/job/125699535009) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.6min | #41512027288 | [job link](https://github.com/sgl-project/sglang/actions/runs/41512027288/job/125536817834) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 45.8min | #41564655436 | [job link](https://github.com/sgl-project/sglang/actions/runs/41564655436/job/125698905407) |
| multimodal-gen-test-4-npu-a3 (0) | 44.0min | #41537036955 | [job link](https://github.com/sgl-project/sglang/actions/runs/41537036955/job/125593125702) |
| base-b-test-1-npu-a3 / run (0) | 43.7min | #41596492773 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596492773/job/125787592446) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 42.8min | #41564366853 | [job link](https://github.com/sgl-project/sglang/actions/runs/41564366853/job/125697079909) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.2min | #41608777768 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906270) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.4min | #41553611334 | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125656859483) |
| multimodal-gen-test-4-npu-a3 (0) | 26.3min | #41527221106 | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353504) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.4min | #41596278362 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125794973674) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.4min | #41575190385 | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125752969106) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.1min | #41623078729 | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306619) |
| multimodal-gen-test-1-npu-a3 (1) | 23.6min | #41606300368 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957147) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | #41541182001 | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860431) |
| multimodal-gen-test-4-npu-a3 (1) | 23.0min | #41606300368 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957225) |
| multimodal-gen-test-1-npu-a3 (0) | 22.8min | #41606300368 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957142) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-2-npu-a3 / run (0) | 166 | 104 | 12 | 22 | 28 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488938)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946780)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493929)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721908)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864234) |
| base-b-test-4-npu-a3 / run (1) | 177 | 123 | 7 | 24 | 23 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061570)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572710)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400635)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867893)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503803) |
| base-b-test-4-npu-a3 / run (0) | 177 | 122 | 7 | 22 | 26 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946578)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014600)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125162)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525237)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331479) |
| base-b-test-1-npu-a3 / run (0) | 165 | 112 | 4 | 22 | 27 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946764)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503851)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860431)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41521451036/job/125540085615) |
| base-b-test-8-npu-a3 / run (0) | 150 | 104 | 5 | 21 | 20 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946379)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833257)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400496)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087660)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539531586) |
| base-b-test-16-npu-a3 / run (0) | 154 | 107 | 0 | 23 | 24 | - |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 90 | 74 | 9 | 0 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306619)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906270)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125781965145)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125728754099)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125716594742) |
| multimodal-gen-test-4-npu-a3 (1) | 157 | 127 | 1 | 0 | 29 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946050) |
| multimodal-gen-test-1-npu-a3 (1) | 99 | 81 | 1 | 0 | 17 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947945951) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 166 | 158 | 0 | 1 | 7 | - |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 73 | 72 | 0 | 1 | 0 | - |
| pr-test-npu-finish | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125556522347) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 13 | 4 | 9 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306619)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906270)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125781965145) |
| `npu_pd_disaggregation.py` | 48 | 40 | 8 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061570)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572710)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125040) |
| `npu_dp_attention.py` | 45 | 39 | 6 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014600)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125162)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525237) |
| `npu_mla_fia_hicache_bf16.py` | 41 | 37 | 4 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721908)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864234)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867814) |
| `npu_return_indexer_topk_deepseek_v4.py` | 32 | 29 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488938)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493929)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600563) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 47 | 44 | 3 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833257)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400496)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087660) |
| `npu_moe_dense_tp_size.py` | 37 | 35 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170984)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525171) |
| `npu_moe_runner_backend.py` | 35 | 34 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468952) |
| `npu_tp2_fia_bf16.py` | 32 | 31 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503815) |
| `npu_sampling_backend.py` | 40 | 39 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503851) |
| `npu_basic_sanity_eagle3.py` | 39 | 38 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860431) |
| `dspark_npu_dispatch.py` | 26 | 25 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41521451036/job/125540085615) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #41567481151<br>[#44492 [Feat] [AMD] mori: Run MORI EPv2 dispatch/combine on AsyncLL kernels for TBO](https://github.com/sgl-project/sglang/pull/44492) | `mori_epv2_asyncll_tbo` | 124.7min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41567481151) |
| #41608777768<br>[#48041 [Fix] moe: Skip hash layers before topk_config in prefill routing paths](https://github.com/sgl-project/sglang/pull/48041) | `fix/hash-topk-dual-stream` | 97.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41608777768) |
| #41567832278<br>[#41846 [Feat] embedding: Support BERT and XLM-R masked-LM checkpoints](https://github.com/sgl-project/sglang/pull/41846) | `xlm-roberta-masked-lm-embedding` | 84.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41567832278) |
| #41410159938<br>[#41916 [Fix] sampling: Make top-k/top-p filtering consistent across sampling paths](https://github.com/sgl-project/sglang/pull/41916) | `fix/top-k-top-p-filtering` | 84.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41410159938) |
| #41484593681<br>[#47948 [Perf] diffusion: Fuse LTX-2.3 vocoder resampling and SnakeBeta](https://github.com/sgl-project/sglang/pull/47948) | `perf/ltx23-alias-free-gap` | 82.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41484593681) |
| #41592906386 | `new-model-support` | 81.8min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41592906386) |
| #41582774906<br>[#43907 [Refactor] scheduler: Share one interface across request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43907) | `lsyin/sched-pr13` | 77.3min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41582774906) |
| #41575190385 | `halops_sglang` | 75.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41575190385) |
| #41605997897<br>[#47853 [Feat] halops: Add HALOps as an opt-in MXFP8 GEMM backend for Blackwell and support mxfp8 megamoe](https://github.com/sgl-project/sglang/pull/47853) | `halops_sglang` | 64.1min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41605997897) |
| #41575235496<br>[#43417 [Fix] cutedsl-mla: Use CuTeDSL MLA for draft prefill and extend](https://github.com/sgl-project/sglang/pull/43417) | `c/cutedsl-mla-draft-extend` | 57.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41575235496) |
| #41623078729<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 57.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41623078729) |
| #41598701821<br>[#43908 [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43908) | `lsyin/sched-pr14` | 57.1min | 3 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41598701821) |
| #41596278362<br>[#41329 [Feat] [CPU] Quantization: Add FP8 quantization support for compressed-tensors paths](https://github.com/sgl-project/sglang/pull/41329) | `yanbing/cpu-fp8-quant-support` | 55.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41596278362) |
| #41582087367<br>[#45798 [Fix] llava: Load LLaVA-1.5 CLIP tower](https://github.com/sgl-project/sglang/pull/45798) | `fix/llava_and_blip` | 54.7min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41582087367) |
| #41571699769<br>[#47308 [Feat] scheduler: add mixed-prefill resource controls](https://github.com/sgl-project/sglang/pull/47308) | `wuyaole/fix-prefill-reservation-budget` | 53.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41571699769) |
| #41534708310<br>[#34212 [Fix] [AMD] DSP: skip unused QuickAllReduce allocation for DCP groups](https://github.com/sgl-project/sglang/pull/34212) | `fix/dcp-disable-unused-quickallreduce` | 53.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41534708310) |
| #41494594784<br>[#44152 [Feat] score/embedding: Add raw embeddings, score rids, encode input_ids, and schedule-decision logging](https://github.com/sgl-project/sglang/pull/44152) | `jsheng/score-embedding-features` | 53.0min | 3 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41494594784) |
| #41553611334<br>[#47960 [Perf] [NVIDIA] dsv4/topk_v2: Exactness modes (fast / exact / deterministic) and an exact cluster path](https://github.com/sgl-project/sglang/pull/47960) | `topk-v2-exact-modes` | 52.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41553611334) |
| #41563491502<br>[#44017 [Feat] [XPU] GDN: support speculative decoding](https://github.com/sgl-project/sglang/pull/44017) | `gdn-spec-decode-xpu` | 48.5min | 3 | base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41563491502) |
| #41581444357 | `followup/qwen35-megakernel-runtime-v3-runtime` | 47.9min | 3 | base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41581444357) |
| #41592686275<br>[#47955 [Perf] srt: Record per request whether an extend row completes its prompt](https://github.com/sgl-project/sglang/pull/47955) | `oss-sync-e54877d341` | 47.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41592686275) |
| #41537658781<br>[#47948 [Perf] diffusion: Fuse LTX-2.3 vocoder resampling and SnakeBeta](https://github.com/sgl-project/sglang/pull/47948) | `perf/ltx23-alias-free-gap` | 47.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41537658781) |
| #41525795413<br>[#46496 [Fix] scheduler: Keep the new-token ratio at its floor after a KV-full retraction](https://github.com/sgl-project/sglang/pull/46496) | `fix/retract-keeps-new-token-ratio` | 46.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41525795413) |
| #41608332411<br>[#41968 [Feat] [NVIDIA] mamba2: Add compact speculative-state replay](https://github.com/sgl-project/sglang/pull/41968) | `shreyasm/mamba2-spec-replay-pr` | 46.5min | 6 | base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41608332411) |
| #41641870450<br>[#46858 [Feat] lfm3: Add text, vision, audio and Omni support](https://github.com/sgl-project/sglang/pull/46858) | `lfm3` | 45.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41641870450) |
| #41581999028<br>[#40333 [Feat] [NVIDIA] deepseek-v4.1: Support prefill CP with BCG in PD serving (2/N)](https://github.com/sgl-project/sglang/pull/40333) | `main-v4.1-cp-bcg` | 44.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41581999028) |
| #41551508199<br>[#47990 [Refactor] imports: Import names from where they are defined; remove re-export shims](https://github.com/sgl-project/sglang/pull/47990) | `lsyin/indirect-imports` | 43.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41551508199) |
| #41592931472<br>[#46327 [Perf] [AMD] unquant: Pad gfx115x linear and lm_head weight rows to avoid cache aliasing](https://github.com/sgl-project/sglang/pull/46327) | `amd/gfx11-pad-linear-weights` | 42.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41592931472) |
| #41554553662<br>[#43579 [Feat] [NPU] sparse-kv: Extend offload with PD disaggregation and LRU caching](https://github.com/sgl-project/sglang/pull/43579) | `cryang/pr/sparsity-pd-disagg-LRU` | 41.1min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41554553662) |
| #41521441760<br>[#42790 [Feat] mamba: Allow skipping per-draft intermediate SSM state](https://github.com/sgl-project/sglang/pull/42790) | `kurt/allocate-intermediate-ssm` | 41.0min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41521441760) |
| #41571425060<br>[#47891 [Feat] [XPU] graph: add context-aware support for XPU graph](https://github.com/sgl-project/sglang/pull/47891) | `ecao/xpu_graph_context_aware_opt` | 40.5min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41571425060) |
| #41648750312<br>[#27267 [Feat] mem_cache: Add hugepage preflight and allocation modes for host pools](https://github.com/sgl-project/sglang/pull/27267) | `hicache-host-memory-preflight` | 38.6min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41648750312) |
| #41563694377<br>[#47120 [Fix] multimodal: Preserve strong identities across VLM caches](https://github.com/sgl-project/sglang/pull/47120) | `codex/vlm-strong-identity-1028` | 38.6min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41563694377) |
| #41598133867 | `followup/qwen35-megakernel-runtime-v3-runtime` | 38.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41598133867) |
| #41586662810<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 38.0min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41586662810) |
| #41542989716<br>[#47990 [Refactor] imports: Import names from where they are defined; remove re-export shims](https://github.com/sgl-project/sglang/pull/47990) | `lsyin/indirect-imports` | 37.9min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41542989716) |
| #41592885006<br>[#39784 [Feat] [NPU] HiCache: support DeepSeek V4 L3 with MemCache](https://github.com/sgl-project/sglang/pull/39784) | `lc-dsv4-l3-upstream` | 37.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41592885006) |
| #41544600168<br>[#42254 [Perf] Foundry: adding the adapter of foundry to enable fast CUDA graph save/load](https://github.com/sgl-project/sglang/pull/42254) | `foundry-dep` | 37.0min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41544600168) |
| #41572148925<br>[#47992 [CI] lint: Reject importing a name through a module that only re-imports it](https://github.com/sgl-project/sglang/pull/47992) | `lsyin/indirect-import-lint` | 36.8min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41572148925) |
| #41586218471<br>[#44394 [Feat] [CPU] cpu-graph: Add prefill torch compile graph and dynamic graph support](https://github.com/sgl-project/sglang/pull/44394) | `ecao/cpu_graph_prefill2` | 36.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41586218471) |
| #41527221106<br>[#47731 [Perf] imports: Keep light modules off HF patches, model configs, and the scheduler](https://github.com/sgl-project/sglang/pull/47731) | `lsyin/import-bootstrap` | 36.5min | 3 | multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41527221106) |
| #41644572183<br>[#47960 [Perf] [NVIDIA] dsv4/topk_v2: Exactness modes (fast / exact / deterministic) and an exact cluster path](https://github.com/sgl-project/sglang/pull/47960) | `topk-v2-exact-modes` | 35.5min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41644572183) |
| #41627725299<br>[#48129 [Feat] PD: Validate peer compatibility for Mistral Large 4](https://github.com/sgl-project/sglang/pull/48129) | `xinyuan/pd-peer-fingerprint` | 35.0min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41627725299) |
| #41591191285 | `followup/qwen35-megakernel-runtime-v3-runtime` | 34.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41591191285) |
| #41588879309<br>[#45828 [Perf] fp8: Hopper small-M GEMV, fused KDA output quant, CUDA grouped top-k, partial-block tails](https://github.com/sgl-project/sglang/pull/45828) | `feat/ling3-fp8-decode-kernels` | 34.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41588879309) |
| #41606300368<br>[#46858 [Feat] lfm3: Add text, vision, audio and Omni support](https://github.com/sgl-project/sglang/pull/46858) | `lfm3` | 33.7min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41606300368) |
| #41589307217<br>[#44684 [Feat] HiSparse: Support DeepSeek-V4 with MTP and DSpark](https://github.com/sgl-project/sglang/pull/44684) | `dsv4_hisparse_dspark` | 33.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41589307217) |
| #41541182001 | `codex/dp-lora-routing-sync` | 30.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41541182001) |
| #41586371049 | `followup/qwen35-megakernel-runtime-v3-runtime` | 29.6min | 8 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41586371049) |
| #41611374139<br>[#36591 [Fix] hisparse: state-preserving retraction and recovery for DSV4](https://github.com/sgl-project/sglang/pull/36591) | `fix/hisparse-cpu-copy-retraction` | 29.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41611374139) |
| #41561813623 | `followup/qwen35-megakernel-runtime-v3-binding` | 27.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41561813623) |
| #41596210368<br>[#45601 [Perf] [AMD] deterministic: Allow AITER prefill attention on gfx950](https://github.com/sgl-project/sglang/pull/45601) | `rocm-deterministic-aiter-prefill-gfx950` | 27.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41596210368) |
| #41545073885 | `gfx1151-quark-w4a16-kernels` | 27.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41545073885) |
| #41537572081<br>[#43904 [Refactor] scheduler: Check request ownership once at step launch](https://github.com/sgl-project/sglang/pull/43904) | `lsyin/sched-pr10` | 26.5min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41537572081) |
| #41559214453<br>[#47553 [Perf] R3: Skip routed-expert capture on ranks that send no rows (2/3)](https://github.com/sgl-project/sglang/pull/47553) | `byron/r3-host-rows-output-rank` | 26.0min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41559214453) |
| #41600451297<br>[#48041 [Fix] moe: Skip hash layers before topk_config in prefill routing paths](https://github.com/sgl-project/sglang/pull/48041) | `fix/hash-topk-dual-stream` | 25.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41600451297) |
| #41594316193<br>[#44394 [Feat] [CPU] cpu-graph: Add prefill torch compile graph and dynamic graph support](https://github.com/sgl-project/sglang/pull/44394) | `ecao/cpu_graph_prefill2` | 24.9min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41594316193) |
| #41636145222<br>[#46610 [Feat] [Intel] mem_cache: Enable the HiCache Mamba host pool on XPU](https://github.com/sgl-project/sglang/pull/46610) | `jeeja/add_mamba_xpu` | 24.0min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41636145222) |
| #41602037859<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 23.9min | 4 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41602037859) |
| #41597855779<br>[#46327 [Perf] [AMD] unquant: Pad gfx115x linear and lm_head weight rows to avoid cache aliasing](https://github.com/sgl-project/sglang/pull/46327) | `amd/gfx11-pad-linear-weights` | 23.2min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41597855779) |
| #41596763082<br>[#48087 [Perf] imports: Keep the detokenizer off TokenizerManager and the tokenizer off schedule_batch](https://github.com/sgl-project/sglang/pull/48087) | `lsyin/cpu-process-imports` | 23.1min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41596763082) |
| #41595854524 | `followup/qwen35-megakernel-runtime-v3-runtime` | 21.9min | 6 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41595854524) |
| #41583771116<br>[#46548 [Fix] PD/PP: Fix consensus checker failure while using PP prefill](https://github.com/sgl-project/sglang/pull/46548) | `fix_pp_pd_hicache_consensus_checker_1026` | 20.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41583771116) |
| #41524437131<br>[#43903 [Refactor] scheduler: Hold a launched prefill in one list until its next holder takes it](https://github.com/sgl-project/sglang/pull/43903) | `lsyin/sched-pr09` | 20.3min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41524437131) |
| #41586237615<br>[#47891 [Feat] [XPU] graph: add context-aware support for XPU graph](https://github.com/sgl-project/sglang/pull/47891) | `ecao/xpu_graph_context_aware_opt` | 18.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41586237615) |
| #41591638339<br>[#44394 [Feat] [CPU] cpu-graph: Add prefill torch compile graph and dynamic graph support](https://github.com/sgl-project/sglang/pull/44394) | `ecao/cpu_graph_prefill2` | 17.2min | 4 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41591638339) |
| #41581647824<br>[#47891 [Feat] [XPU] graph: add context-aware support for XPU graph](https://github.com/sgl-project/sglang/pull/47891) | `ecao/xpu_graph_context_aware_opt` | 16.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41581647824) |
| #41521451036<br>[#37472 [Fix] dspark: Keep verify bookkeeping in range for rows without candidates](https://github.com/sgl-project/sglang/pull/37472) | `dspark-vocab-verify-guards` | 16.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41521451036) |
| #41504870199<br>[#44576 [Fix] disaggregation: Release multimodal features when PD prefill finishes a request](https://github.com/sgl-project/sglang/pull/44576) | `pd-prefill-release-mm-features` | 15.8min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41504870199) |
| #41557681616<br>[#47183 [Feat] Spark2.5: Support Spark2.5 Dspark](https://github.com/sgl-project/sglang/pull/47183) | `feature/spark2_5_dspark` | 15.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41557681616) |
| #41598769744<br>[#48087 [Perf] imports: Keep the detokenizer off TokenizerManager and the tokenizer off schedule_batch](https://github.com/sgl-project/sglang/pull/48087) | `lsyin/cpu-process-imports` | 14.8min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41598769744) |
| #41590538906<br>[#46610 [Feat] [Intel] mem_cache: Enable the HiCache Mamba host pool on XPU](https://github.com/sgl-project/sglang/pull/46610) | `jeeja/add_mamba_xpu` | 14.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41590538906) |
| #41481113005<br>[#37273 [Feat] scheduler: Add opt-in DP-attention phase lockstep](https://github.com/sgl-project/sglang/pull/37273) | `dp-attn-phase-lockstep` | 14.4min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41481113005) |
| #41597732832<br>[#43908 [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43908) | `lsyin/sched-pr14` | 13.9min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41597732832) |
| #41481110584<br>[#47494 [Perf] dspark: Refresh Mamba tracking once per verification step](https://github.com/sgl-project/sglang/pull/47494) | `c/dspark-prepare-tracking-once` | 13.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41481110584) |
| #41563231013<br>[#39784 [Feat] [NPU] HiCache: support DeepSeek V4 L3 with MemCache](https://github.com/sgl-project/sglang/pull/39784) | `lc-dsv4-l3-upstream` | 12.9min | 4 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41563231013) |
| #41599290834<br>[#48109 [Fix] moe: Match padded-row indices to token-count dtype](https://github.com/sgl-project/sglang/pull/48109) | `fix/moe-topk-arange-dtype` | 12.0min | 5 | base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41599290834) |
| #41483261313<br>[#43417 [Fix] cutedsl-mla: Use CuTeDSL MLA for draft prefill and extend](https://github.com/sgl-project/sglang/pull/43417) | `c/cutedsl-mla-draft-extend` | 10.8min | 5 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41483261313) |
| #41525301036<br>[#47731 [Perf] imports: Keep light modules off HF patches, model configs, and the scheduler](https://github.com/sgl-project/sglang/pull/47731) | `lsyin/import-bootstrap` | 10.7min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), pr-test-npu-finish | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41525301036) |
| #41593286482<br>[#44394 [Feat] [CPU] cpu-graph: Add prefill torch compile graph and dynamic graph support](https://github.com/sgl-project/sglang/pull/44394) | `ecao/cpu_graph_prefill2` | 10.6min | 3 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41593286482) |
| #41550825027<br>[#47990 [Refactor] imports: Import names from where they are defined; remove re-export shims](https://github.com/sgl-project/sglang/pull/47990) | `lsyin/indirect-imports` | 10.6min | 7 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41550825027) |
| #41483261916<br>[#37273 [Feat] scheduler: Add opt-in DP-attention phase lockstep](https://github.com/sgl-project/sglang/pull/37273) | `dp-attn-phase-lockstep` | 10.5min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41483261916) |
| #41596403073<br>[#43908 [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43908) | `lsyin/sched-pr14` | 10.3min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41596403073) |
| #41596210773<br>[#48087 [Perf] imports: Keep the detokenizer off TokenizerManager and the tokenizer off schedule_batch](https://github.com/sgl-project/sglang/pull/48087) | `lsyin/cpu-process-imports` | 10.3min | 10 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41596210773) |
| #41594662982<br>[#43908 [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43908) | `lsyin/sched-pr14` | 9.3min | 8 | multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41594662982) |
| #41551374167<br>[#43905 [Fix] scheduler: Abort held decode requests, and read live requests from the lists](https://github.com/sgl-project/sglang/pull/43905) | `lsyin/sched-pr11` | 9.3min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41551374167) |
| #41501755031<br>[#47960 [Perf] [NVIDIA] dsv4/topk_v2: Exactness modes (fast / exact / deterministic) and an exact cluster path](https://github.com/sgl-project/sglang/pull/47960) | `topk-v2-exact-modes` | 8.2min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41501755031) |
| #41570670828 | `ecao/xpu_graph_context_aware_opt` | 8.0min | 2 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41570670828) |
| #41586144373<br>[#45601 [Perf] [AMD] deterministic: Allow AITER prefill attention on gfx950](https://github.com/sgl-project/sglang/pull/45601) | `rocm-deterministic-aiter-prefill-gfx950` | 7.8min | 2 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41586144373) |
| #41604956623<br>[#43908 [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43908) | `lsyin/sched-pr14` | 7.7min | 2 | base-a-test-npu, Recommend tests from coverage | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41604956623) |
| #41594170024<br>[#41521 [Perf] [Intel] dp: Routes all_gather_into_tensor and reduce_scatter_tensor to shm kernels](https://github.com/sgl-project/sglang/pull/41521) | `chunyuan/dp_frontend` | 7.4min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41594170024) |
| #41591937404<br>[#47955 [Perf] srt: Record per request whether an extend row completes its prompt](https://github.com/sgl-project/sglang/pull/47955) | `oss-sync-e54877d341` | 7.4min | 0 |  | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41591937404) |
| #41592788376<br>[#47785 [Perf] [NVIDIA] qwen3: Fuse prefill QK norm and RoPE with contiguous Q](https://github.com/sgl-project/sglang/pull/47785) | `mani1106/fuse-qwen3-prefill` | 6.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41592788376) |
| #41553023950<br>[#47960 [Perf] [NVIDIA] dsv4/topk_v2: Exactness modes (fast / exact / deterministic) and an exact cluster path](https://github.com/sgl-project/sglang/pull/47960) | `topk-v2-exact-modes` | 6.3min | 4 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41553023950) |
| #41597227675<br>[#43908 [Refactor] scheduler: Hold wrapped requests in request lists and abort through each list](https://github.com/sgl-project/sglang/pull/43908) | `lsyin/sched-pr14` | 5.6min | 2 | Recommend tests from coverage, base-a-test-npu | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41597227675) |
| #41526614181<br>[#47731 [Perf] imports: Keep light modules off HF patches, model configs, and the scheduler](https://github.com/sgl-project/sglang/pull/47731) | `lsyin/import-bootstrap` | 5.6min | 2 | base-a-test-npu, Recommend tests from coverage | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41526614181) |

---


## [Run #41648750312](https://github.com/sgl-project/sglang/actions/runs/41648750312)
- **分支**: `hicache-host-memory-preflight`
- **总耗时**: 38.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41648750312

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.8min | 代码错误 | 测试用例 test_npu_return_indexer_topk_deepseek_v4.py 执行失败，导致作业退出码为1。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488938) |

- **base-b-test-2-npu-a3 / run (0)**: TIMINGS 显示 test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py 的 passed 为 false（耗时68秒），其余用例均通过，最终进程以 exit code 1 结束，属于该测试用例本身的代码/断言失败。
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488938

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125961216019) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125961216027) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488647) |
| multimodal-gen-test-4-npu-a3 (0) | 33.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488769) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488895) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488914) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488918) |
| base-b-test-1-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962488969) |
| base-b-test-4-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962489069) |
| base-b-test-4-npu-a3 / run (1) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962489131) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41648750312/job/125962489370) |


## [Run #41644572183](https://github.com/sgl-project/sglang/actions/runs/41644572183)
- **分支**: `topk-v2-exact-modes`
- **总耗时**: 35.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41644572183

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 1.2min | 环境问题 | 下载 actions/checkout 时 GitHub 返回 429 限流，重试3次仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947945951) |
| multimodal-gen-test-4-npu-a3 (1) | 1.3min | 环境问题 | 下载 actions/checkout 时 GitHub 返回 429 限流，重试3次仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946050) |
| base-b-test-8-npu-a3 / run (0) | 1.8min | 环境问题 | 下载 actions/checkout 时 GitHub 返回 429 限流，重试3次仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946379) |
| base-b-test-4-npu-a3 / run (0) | 1.4min | 环境问题 | 下载 actions/checkout 动作时 GitHub 返回 429 限流，重试 3 次仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946578) |
| base-b-test-16-npu-a3 / run (0) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946586) |
| base-b-test-4-npu-a3 / run (1) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946661) |
| base-b-test-1-npu-a3 / run (0) | 1.3min | 环境问题 | 下载 actions/checkout 动作时 GitHub 返回 429 限流，重试3次仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946764) |
| base-b-test-2-npu-a3 / run (0) | 1.1min | 环境问题 | 下载 actions/checkout 时 GitHub 返回 429 限流，重试3次仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946780) |

- **multimodal-gen-test-1-npu-a3 (1)**: Runner 通过代理下载 actions/checkout@v4 归档时，codeload.github.com 连续返回 429 Too Many Requests，退避重试3次后仍失败，作业在准备阶段即中止，与代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947945951

- **multimodal-gen-test-4-npu-a3 (1)**: Runner 通过代理下载 actions/checkout@v4 归档时，codeload.github.com 连续返回 429 Too Many Requests，退避重试3次后仍失败，作业在准备阶段即中止，与代码或模型无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946050

- **base-b-test-8-npu-a3 / run (0)**: Runner 通过代理下载 actions/checkout@v4 归档时，codeload.github.com 连续返回 429 Too Many Requests，退避重试3次后仍失败，作业在准备阶段即中止，与代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946379

- **base-b-test-4-npu-a3 / run (0)**: Runner 通过代理下载 actions/checkout@v4 归档时，codeload.github.com 连续返回 429 Too Many Requests，退避重试 3 次后仍失败，作业在准备阶段即中止，与代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946578



- **base-b-test-1-npu-a3 / run (0)**: Runner 通过代理下载 actions/checkout@v4 归档时，codeload.github.com 连续返回 429 Too Many Requests，退避重试3次后仍失败，作业在准备阶段即中止，与代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946764

- **base-b-test-2-npu-a3 / run (0)**: Runner 通过代理下载 actions/checkout@v4 归档时，codeload.github.com 连续返回 429 Too Many Requests，退避重试3次后仍失败，作业在准备阶段即中止，与代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946780

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125946652680) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125946652763) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946038) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41644572183/job/125947946135) |


## [Run #41641870450](https://github.com/sgl-project/sglang/actions/runs/41641870450)
- **分支**: `lfm3`
- **总耗时**: 45.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41641870450

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311905) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311944) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938312124) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125937357927) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125937358027) |
| multimodal-gen-test-4-npu-a3 (0) | 42.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311493) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311539) |
| multimodal-gen-test-1-npu-a3 (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311583) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311647) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311819) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938311963) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41641870450/job/125938312128) |


## [Run #41636145222](https://github.com/sgl-project/sglang/actions/runs/41636145222)
- **分支**: `jeeja/add_mamba_xpu`
- **总耗时**: 24.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41636145222

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 7.3min | 代码错误 | NPU EPLB 最小重平衡利用率阈值测试失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833257) |

- **base-b-test-8-npu-a3 / run (0)**: test_npu_eplb_min_rebalancing_utilization_threshold.py 运行约199秒后返回退出码5，测试汇总0/1通过，导致作业以退出码1结束。退出码5通常表示pytest未收集到测试或测试内部断言/异常失败，需检查该用例的EPLB阈值逻辑或测试收集条件。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833257

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125917955851) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125917956088) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918832655) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918832800) |
| base-b-test-1-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833012) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833025) |
| base-b-test-4-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833062) |
| base-b-test-2-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833106) |
| base-b-test-16-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41636145222/job/125918833313) |


## [Run #41631717492](https://github.com/sgl-project/sglang/actions/runs/41631717492)
- **分支**: `work/k3-mixed-reuse-flow-20261102`
- **总耗时**: 11.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41631717492

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976394) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976419) |
| multimodal-gen-test-4-npu-a3 (1) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976462) |
| base-b-test-16-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976487) |
| base-b-test-4-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976501) |
| base-b-test-4-npu-a3 / run (1) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976540) |
| base-b-test-2-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976761) |
| base-b-test-1-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125923976838) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125922791403) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41631717492/job/125922791602) |


## [Run #41627725299](https://github.com/sgl-project/sglang/actions/runs/41627725299)
- **分支**: `xinyuan/pd-peer-fingerprint`
- **总耗时**: 35.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41627725299

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.3min | 代码错误 | 测试用例 test_npu_return_indexer_topk_deepseek_v4.py 执行失败，导致作业退出码为1。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493929) |

- **base-b-test-2-npu-a3 / run (0)**: TIMINGS 显示 test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py 的 passed 为 false（耗时70秒），其余用例均通过，最终进程以 exit code 1 结束，属于该测试用例本身的代码/断言失败。
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493929

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125889401852) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125889402072) |
| base-b-test-1-npu-a3 / run (0) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493856) |
| multimodal-gen-test-4-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493878) |
| multimodal-gen-test-1-npu-a3 (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493930) |
| multimodal-gen-test-1-npu-a3 (1) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493938) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890493948) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890494018) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890494046) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890494071) |
| base-b-test-16-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41627725299/job/125890494133) |


## [Run #41623078729](https://github.com/sgl-project/sglang/actions/runs/41623078729)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 57.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41623078729

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.1min | 精度回归 | GLM5 top64 pruned 精度测试脚本以退出码5失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306619) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 作业中 2 个精度用例仅 1 个通过；test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 运行 363 秒后返回 exit code 5（pytest 无测试收集/用例未找到），导致作业退出码 1。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306619

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125873664322) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125873664476) |
| multimodal-gen-test-1-npu-a3 (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622320) |
| multimodal-gen-test-4-npu-a3 (0) | 34.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622384) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622407) |
| base-b-test-16-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622437) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622452) |
| base-b-test-2-npu-a3 / run (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622454) |
| multimodal-gen-test-4-npu-a3 (1) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622474) |
| base-b-test-4-npu-a3 / run (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622552) |
| base-b-test-1-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622571) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125874622620) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306494) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41623078729/job/125888306900) |


## [Run #41611374139](https://github.com/sgl-project/sglang/actions/runs/41611374139)
- **分支**: `fix/hisparse-cpu-copy-retraction`
- **总耗时**: 29.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41611374139

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020763) |
| base-b-test-16-npu-a3 / run (0) | 1.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020802) |
| base-b-test-4-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020861) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020894) |
| base-b-test-4-npu-a3 / run (1) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020900) |
| base-b-test-2-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020912) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125834044934) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125834045138) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020653) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41611374139/job/125835020879) |


## [Run #41608777768](https://github.com/sgl-project/sglang/actions/runs/41608777768)
- **分支**: `fix/hash-topk-dual-stream`
- **总耗时**: 97.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41608777768

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.2min | 精度回归 | GLM5 top64 pruned 的 GSM8K 精度测试失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906270) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 套件中 2 个用例仅 1 个通过：deepseek_v4_flash w8a8 gpqa 通过，glm5_top64_pruned bf16 8p gsm8k 返回 exit code 5 失败，导致作业退出码 1。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906270

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125825488684) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125825488728) |
| base-b-test-2-npu-a3 / run (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125826426200) |
| base-b-test-4-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125826426243) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125826426340) |
| base-b-test-4-npu-a3 / run (1) | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125826426419) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906288) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608777768/job/125847906476) |


## [Run #41608332411](https://github.com/sgl-project/sglang/actions/runs/41608332411)
- **分支**: `shreyasm/mamba2-spec-replay-pr`
- **总耗时**: 46.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41608332411

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926410) |
| base-b-test-2-npu-a3 / run (0) | 9.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926507) |
| base-b-test-1-npu-a3 / run (0) | 9.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926509) |
| base-b-test-16-npu-a3 / run (0) | 9.5min | 环境问题 | 自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926652) |
| base-b-test-4-npu-a3 / run (0) | 12.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926668) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926689) |

- **base-b-test-8-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器执行环境故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926410

- **base-b-test-2-npu-a3 / run (0)**: 服务已正常启动并返回 200，但随后报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926507

- **base-b-test-1-npu-a3 / run (0)**: 模型权重分片加载完成后，日志报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926509

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 Scheduler watchdog 超时（soft），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，并非模型精度或代码逻辑问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926652

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试正常进行时突然报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非测试用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926668

- **base-b-test-4-npu-a3 / run (1)**: 日志中 Test Summary 为 2/2 passed，两个 NPU 测试均通过，仅存在 Node.js 弃用警告，未出现失败或错误信息，可能是作业状态误报或日志不完整。
  链接: https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926689

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125823825102) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125823825171) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824925991) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926141) |
| multimodal-gen-test-4-npu-a3 (0) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926169) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41608332411/job/125824926260) |


## [Run #41606300368](https://github.com/sgl-project/sglang/actions/runs/41606300368)
- **分支**: `lfm3`
- **总耗时**: 33.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41606300368

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 22.8min | 其他 | 作业未产出 diffusion-failures 目录，且从 pod 复制 _temp 失败，导致无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957142) |
| multimodal-gen-test-1-npu-a3 (1) | 23.6min | 其他 | 作业失败但日志未显示具体错误，仅提示未找到 diffusion-failures/ 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957147) |
| multimodal-gen-test-4-npu-a3 (1) | 23.0min | 其他 | 作业失败但日志未显示具体错误，仅提示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957225) |
| multimodal-gen-test-4-npu-a3 (0) | 22.1min | 其他 | 作业日志中未显示具体测试失败原因，仅显示上传产物路径 diffusion-failures/ 下无文件。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957260) |
| base-b-test-16-npu-a3 / run (0) | 25.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957467) |
| base-b-test-4-npu-a3 / run (1) | 25.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957505) |
| base-b-test-4-npu-a3 / run (0) | 25.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957628) |
| base-b-test-8-npu-a3 / run (0) | 25.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957655) |
| base-b-test-2-npu-a3 / run (0) | 25.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957658) |
| base-b-test-1-npu-a3 / run (0) | 25.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957681) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示未找到 diffusion-failures/ 路径，无 artifact 上传；随后警告从 pod 复制 _temp 失败。中间省略部分可能含真实测试失败原因，但可见信息仅表明产物缺失与 pod 复制异常，无法定位具体测试错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957142

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示“No files were found with the provided path: diffusion-failures/”，说明测试未生成失败产物目录，可能测试未实际执行或提前退出；中间省略部分可能含真实错误，需查看完整日志定位。
  链接: https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957147

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中仅有 Node.js 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或路径配置有误；中间省略部分可能含真正失败原因，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957225

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，无法看到实际测试报错；末尾仅提示未找到 diffusion-failures/ 目录下的文件，导致 artifact 上传为空。需查看完整日志确认测试是否失败或产物路径配置有误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817957260







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817009293) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41606300368/job/125817009444) |


## [Run #41605997897](https://github.com/sgl-project/sglang/actions/runs/41605997897)
- **分支**: `halops_sglang`
- **总耗时**: 64.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41605997897

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061563) |
| base-b-test-4-npu-a3 / run (1) | 8.3min | 代码错误 | NPU PD分离测试用例执行失败，返回退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061570) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061598) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061660) |
| base-b-test-1-npu-a3 / run (0) | 1.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061677) |


- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行203秒后报错（errors=1），2个测试全部未通过，导致作业以退出码1结束。需查看该用例具体报错堆栈定位问题。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061570




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125816018131) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125816018224) |
| multimodal-gen-test-1-npu-a3 (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061414) |
| multimodal-gen-test-4-npu-a3 (0) | 28.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061492) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061506) |
| base-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061555) |
| multimodal-gen-test-4-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605997897/job/125817061585) |


## [Run #41605782782](https://github.com/sgl-project/sglang/actions/runs/41605782782)
- **分支**: `lsyin/sched-pr15`
- **总耗时**: 7.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41605782782

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816181293) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816181405) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816181781) |
| base-b-test-4-npu-a3 / run (1) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816181903) |
| base-b-test-4-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816181931) |
| base-b-test-1-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816182002) |
| base-b-test-8-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816182111) |
| base-b-test-16-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125816182292) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125815343661) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41605782782/job/125815343756) |


## [Run #41604956623](https://github.com/sgl-project/sglang/actions/runs/41604956623)
- **分支**: `lsyin/sched-pr14`
- **总耗时**: 7.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41604956623

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-a-test-npu | 1.5min | 其他 | 测试全部通过后作业被外部取消，非测试失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41604956623/job/125814778329) |
| Recommend tests from coverage | 1.3min | 其他 | 日志中未见失败步骤，作业实际成功完成并上传了推荐测试报告 | [job link](https://github.com/sgl-project/sglang/actions/runs/41604956623/job/125814778494) |

- **base-a-test-npu**: 第4/10项 test_npu_graph_runner.py 的24个用例全部通过（24 passed），随后日志出现 The operation was canceled，作业被取消，属于外部取消或超时/中断，而非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41604956623/job/125814778329

- **Recommend tests from coverage**: 日志显示 checkout、上传 artifact、设置 job outputs 均成功，仅有 Node.js 20 弃用警告，无报错或失败退出码，失败可能由其他隐藏步骤或外部因素导致，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41604956623/job/125814778494


## [Run #41602037859](https://github.com/sgl-project/sglang/actions/runs/41602037859)
- **分支**: `new-model-support`
- **总耗时**: 23.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41602037859

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 20.4min | 其他 | 多模态生成测试失败，且未生成失败产物目录 | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804122981) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | 其他 | 日志中未出现明确失败原因，仅显示产物目录为空、未上传任何文件。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804122997) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | 环境问题 | 自托管 runner 执行自定义容器失败，非测试代码本身问题 | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123175) |
| base-b-test-1-npu-a3 / run (0) | 18.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123185) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业运行约20分钟后失败，日志中仅显示未找到 diffusion-failures/ 目录，无具体报错信息，无法定位根因，需查看中间省略的测试输出。
  链接: https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804122981

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾显示 diffusion-failures/ 路径下未找到文件，未上传产物；其余均为 Node.js 弃用警告和清理步骤，缺少实际测试失败的错误信息，无法定位具体原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804122997

- **base-b-test-2-npu-a3 / run (0)**: 服务已正常启动并返回 200，但随后报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，属于 runner/容器环境故障，与 NPU 测试逻辑无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123175

- **base-b-test-1-npu-a3 / run (0)**: 模型权重加载完成后，日志报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或精度问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123185

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125803238857) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125803239008) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123078) |
| multimodal-gen-test-1-npu-a3 (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123216) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123322) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123334) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123351) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41602037859/job/125804123354) |


## [Run #41600451297](https://github.com/sgl-project/sglang/actions/runs/41600451297)
- **分支**: `fix/hash-topk-dual-stream`
- **总耗时**: 25.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41600451297

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 7.0min | 代码错误 | NPU MLA FIA HiCache 测试脚本执行失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721908) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 运行 102 秒后返回退出码 5（pytest 无测试收集或内部错误），5 个测试全部未通过，导致作业失败。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721908

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125797840636) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125797840664) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721801) |
| base-b-test-4-npu-a3 / run (1) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721878) |
| base-b-test-16-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41600451297/job/125798721950) |


## [Run #41599290834](https://github.com/sgl-project/sglang/actions/runs/41599290834)
- **分支**: `fix/moe-topk-arange-dtype`
- **总耗时**: 12.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41599290834

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 8.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800794893) |
| base-b-test-16-npu-a3 / run (0) | 6.6min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800794976) |
| base-b-test-1-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795037) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795119) |
| base-b-test-2-npu-a3 / run (0) | 7.3min | 环境问题 | 测试本身通过，但自定义容器执行失败，属于自托管 runner 环境问题 | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795211) |

- **base-b-test-8-npu-a3 / run (0)**: 服务启动后 /health_generate 返回 503，随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，并非测试代码本身的问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800794893

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载到约29%时，报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境故障，并非测试代码或模型本身的问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800794976

- **base-b-test-1-npu-a3 / run (0)**: 模型权重分片加载完成后，日志报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，属于 runner/容器环境故障，并非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795037

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型权重加载刚开始（0/7 分片）即报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，而非代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795119

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 Ran 1 test in 162.323s，结果为 OK，说明测试用例已通过；随后报错 Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner 容器环境异常，而非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795211

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125799692789) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125799692799) |
| base-b-test-4-npu-a3 / run (1) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41599290834/job/125800795123) |


## [Run #41598769744](https://github.com/sgl-project/sglang/actions/runs/41598769744)
- **分支**: `lsyin/cpu-process-imports`
- **总耗时**: 14.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41598769744

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 5.3min | 其他 | 测试未生成 diffusion-failures 目录，产物上传失败，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122337) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 其他 | 作业未产生 diffusion-failures 目录，上传产物时无文件可传，但日志未显示明确失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122358) |
| multimodal-gen-test-1-npu-a3 (1) | 5.2min | 其他 | 测试失败但日志中未显示具体错误，仅提示未找到 diffusion-failures 目录，无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122416) |
| multimodal-gen-test-4-npu-a3 (1) | 4.3min | 其他 | 多模态生成测试未产出 diffusion-failures 目录，导致产物上传失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122435) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业在环境准备阶段中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122493) |
| base-b-test-1-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122572) |
| base-b-test-16-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器实现失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122605) |
| base-b-test-8-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122681) |
| base-b-test-4-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122796) |
| base-b-test-4-npu-a3 / run (1) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122901) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示“No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.”，说明多模态生成测试未产出预期失败样本目录，导致 upload-artifact 步骤无文件可传，作业判定失败。其余仅为 Node 弃用警告，非根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122337

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中仅见 Node.js 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试未生成失败产物目录；中间省略部分可能包含真正的测试失败信息，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122358

- **multimodal-gen-test-1-npu-a3 (1)**: 日志被省略，未见实际报错信息。末尾显示 'No files were found with the provided path: diffusion-failures/'，说明测试失败后未生成失败产物目录，无法定位根因，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122416

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中仅见“No files were found with the provided path: diffusion-failures/”，说明测试未生成失败样本目录或测试提前退出；日志被截断，无法确认具体测试报错，需查看中间省略部分定位根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122435

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 apt 下载依赖过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或测试本身失败，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122493

- **base-b-test-1-npu-a3 / run (0)**: 日志显示在解包 apt 依赖包过程中出现“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境异常，并非代码或测试本身失败，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122572

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 custom container 安装 custom_transformer 算子包后报错“Executing the custom container implementation failed”，属于 runner/容器环境问题，非代码或精度问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122605

- **base-b-test-8-npu-a3 / run (0)**: 日志显示在解包 apt 依赖包过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或测试本身失败，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122681

- **base-b-test-4-npu-a3 / run (0)**: 日志显示在安装依赖包过程中报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境问题，需联系 runner 管理员排查，并非代码或测试本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122796

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 CANN 9.1.0 与 memfabric-hybrid 安装完成后，报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125795122901

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125794210158) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598769744/job/125794210174) |


## [Run #41598701821](https://github.com/sgl-project/sglang/actions/runs/41598701821)
- **分支**: `lsyin/sched-pr14`
- **总耗时**: 57.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41598701821

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 6.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125805101822) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125805101847) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | 代码错误 | 测试脚本中整数比较语法错误导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125805102167) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示“Executing the custom container implementation failed”，发生在 k8s runner 启动容器时，约7分钟后失败，测试尚未开始，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125805101822

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示推理请求均返回 200 OK，随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时/基础设施故障，非测试用例或代码本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125805101847

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试套件未找到任何用例（0/0），随后脚本第223行执行 `[: 0 0: integer expression expected`，因变量值含换行或空格导致整数比较失败，属CI脚本逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125805102167

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125794118755) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125794118811) |
| multimodal-gen-test-4-npu-a3 (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795024839) |
| base-b-test-2-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795024958) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795025002) |
| base-b-test-8-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795025008) |
| base-b-test-4-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795025072) |
| base-b-test-16-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795025088) |
| multimodal-gen-test-4-npu-a3 (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795025105) |
| base-b-test-4-npu-a3 / run (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598701821/job/125795025663) |


## [Run #41598133867](https://github.com/sgl-project/sglang/actions/runs/41598133867)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 38.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41598133867

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 1.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843650) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125790956556) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125790956711) |
| multimodal-gen-test-1-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843407) |
| multimodal-gen-test-1-npu-a3 (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843471) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843473) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843482) |
| base-b-test-1-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843557) |
| multimodal-gen-test-4-npu-a3 (0) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843577) |
| base-b-test-8-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843583) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791843642) |
| base-b-test-4-npu-a3 / run (0) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41598133867/job/125791844259) |


## [Run #41597855779](https://github.com/sgl-project/sglang/actions/runs/41597855779)
- **分支**: `amd/gfx11-pad-linear-weights`
- **总耗时**: 23.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41597855779

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | 其他 | 多模态生成测试失败，且未生成 diffusion-failures 目录，无失败产物可上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348435) |
| multimodal-gen-test-1-npu-a3 (1) | 13.4min | 其他 | 日志中未出现明确的测试失败信息，仅显示产物目录为空。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348477) |
| multimodal-gen-test-4-npu-a3 (0) | 14.5min | 其他 | 作业失败但日志未显示具体错误，仅提示未找到 diffusion-failures 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348506) |
| base-b-test-1-npu-a3 / run (0) | 16.9min | 其他 | 日志中未出现实际测试执行或失败信息，作业在 checkout 后即结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348509) |
| multimodal-gen-test-4-npu-a3 (1) | 13.3min | 其他 | 日志中未出现明确的测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348550) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348615) |
| base-b-test-4-npu-a3 / run (0) | 11.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348655) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348681) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348692) |
| base-b-test-2-npu-a3 / run (0) | 16.8min | 环境问题 | 作业在 checkout 后执行 k8s 步骤时异常退出，未进入实际测试。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348774) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示测试作业执行后未找到 diffusion-failures/ 路径，说明测试失败但未产出失败样本或目录未创建；日志中段被省略，无法看到具体报错，仅能确认产物缺失，需查看完整日志定位测试失败根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348435

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示未找到 diffusion-failures/ 路径下的文件，因此没有上传任何产物；但日志中未包含具体的测试断言失败或错误堆栈，无法确定根因，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348477

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中仅有 Node.js 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或测试步骤未正常执行，缺少关键错误信息，无法定位具体失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348506

- **base-b-test-1-npu-a3 / run (0)**: 日志仅显示 runner 启动、下载 action、checkout 代码及运行 k8s 脚本，随后清理进程结束，无测试报错或超时记录，失败原因无法从所给日志判定，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348509

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明失败产物目录不存在，但真正的测试失败原因在省略的中间日志中，当前信息不足以判定具体失败类型。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348550

- **base-b-test-8-npu-a3 / run (0)**: 日志中测试 1/1 通过，耗时243秒，随后正常清理退出，仅出现 Node.js 弃用警告，未发现失败或报错信息，可能是作业状态标记异常或日志截断。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348615

- **base-b-test-4-npu-a3 / run (0)**: 日志显示推理仍在正常输出 prefill 吞吐，随后报错“Executing the custom container implementation failed”，属于 runner 容器执行环境异常，非代码或性能问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348655

- **base-b-test-16-npu-a3 / run (0)**: 日志显示容器内各 TP/EP 进程已获取 PYTHONPATH 环境变量，随后报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，属于 runner/容器环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348681

- **base-b-test-4-npu-a3 / run (1)**: 日志中 Test Summary 为 2/2 passed，两个 NPU 测试均通过，耗时正常，后续仅为清理和 Node.js 弃用警告，未出现失败步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348692

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 checkout 成功，随后运行 /home/runner/k8s/index.js 仅输出 Node 弃用警告，紧接着清理孤儿进程并结束，无测试执行记录，疑似 runner 或 k8s 环境异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125790348774

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125789469368) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41597855779/job/125789469463) |


## [Run #41597732832](https://github.com/sgl-project/sglang/actions/runs/41597732832)
- **分支**: `lsyin/sched-pr14`
- **总耗时**: 13.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41597732832

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | 其他 | 日志中未见明确失败原因，仅显示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295693) |
| multimodal-gen-test-4-npu-a3 (1) | 5.3min | 其他 | 测试失败但日志未显示具体错误，仅提示未找到 diffusion-failures 目录下的文件 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295706) |
| base-b-test-16-npu-a3 / run (0) | 7.0min | 环境问题 | 作业在 checkout 后执行 k8s 脚本时异常退出，未进入实际测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295819) |
| base-b-test-8-npu-a3 / run (0) | 9.5min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295834) |
| base-b-test-1-npu-a3 / run (0) | 9.4min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295860) |
| base-b-test-2-npu-a3 / run (0) | 9.4min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295893) |
| base-b-test-4-npu-a3 / run (1) | 5.3min | 环境问题 | 自托管 runner 执行自定义容器失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295894) |
| base-b-test-4-npu-a3 / run (0) | 9.1min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790296175) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，中间省略部分可能包含真正失败信息。可见部分仅有 Node.js 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物目录，无法定位具体失败点，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295693

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中无明确报错信息，仅显示上传产物时未找到 diffusion-failures/ 路径下的文件，说明测试可能已失败但失败详情被省略，需查看完整日志定位具体原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295706

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 checkout 成功，随后运行 /home/runner/k8s/index.js 时仅出现 Node.js 弃用警告，紧接着清理孤儿进程并结束，无测试输出，疑似 runner 环境或 k8s 启动脚本异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295819




- **base-b-test-4-npu-a3 / run (1)**: 日志显示在解包 apt 依赖包过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，非代码或测试本身问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125790295894


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125789432097) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41597732832/job/125789432172) |


## [Run #41597227675](https://github.com/sgl-project/sglang/actions/runs/41597227675)
- **分支**: `lsyin/sched-pr14`
- **总耗时**: 5.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41597227675

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| Recommend tests from coverage | 1.5min | 其他 | 日志中未见失败步骤，作业实际成功完成 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597227675/job/125788426608) |
| base-a-test-npu | 2.3min | 其他 | 日志中所有NPU单元测试均通过，未发现失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41597227675/job/125788426713) |

- **Recommend tests from coverage**: 日志显示工件上传成功、输出变量设置完成、清理正常，仅有 Node.js 20 弃用警告，未出现错误或失败信息，可能是日志截断或失败原因在省略部分。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597227675/job/125788426608

- **base-a-test-npu**: TIMINGS显示11个测试文件全部passed，作业正常清理退出，无报错。仅有的警告是Node.js 20弃用提示，不影响结果。日志片段可能不完整，需查看省略部分确认实际失败点。
  链接: https://github.com/sgl-project/sglang/actions/runs/41597227675/job/125788426713


## [Run #41596763082](https://github.com/sgl-project/sglang/actions/runs/41596763082)
- **分支**: `lsyin/cpu-process-imports`
- **总耗时**: 23.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41596763082

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 10.8min | 其他 | 作业失败但日志中未显示具体错误，仅提示未找到 diffusion-failures 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788708879) |
| multimodal-gen-test-1-npu-a3 (0) | 10.4min | 其他 | 多模态生成测试失败，且未生成失败产物目录，无法上传 artifact。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788708880) |
| multimodal-gen-test-4-npu-a3 (0) | 10.4min | 其他 | 测试未生成 diffusion-failures 目录，产物上传失败，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788708989) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | 其他 | 测试失败但未生成 diffusion-failures 目录，导致无产物可上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709049) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装后中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709148) |
| base-b-test-2-npu-a3 / run (0) | 13.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709235) |
| base-b-test-4-npu-a3 / run (0) | 13.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709238) |
| base-b-test-1-npu-a3 / run (0) | 9.3min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709250) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709356) |
| base-b-test-16-npu-a3 / run (0) | 9.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709454) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示“No files were found with the provided path: diffusion-failures/”，说明测试失败后未生成失败产物目录，可能测试提前异常退出；中间省略部分可能包含真正错误，但可见日志未暴露具体失败原因，需查看完整日志定位。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788708879

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示测试步骤执行后未找到 diffusion-failures/ 目录，说明测试未产出预期失败样本或测试提前异常退出；日志中段被省略，无法定位具体报错，需查看完整日志确认测试失败根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788708880

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明多模态生成测试未产出预期失败样本目录，可能是测试未执行或未生成该目录，导致 upload-artifact 步骤无文件可传。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788708989

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示“No files were found with the provided path: diffusion-failures/”，说明多模态生成测试未产出失败样本目录，可能测试未实际执行或提前退出；日志中段被省略，无法定位具体报错，需查看完整日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709049

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 安装 memcache-hybrid 成功后立即报错“Executing the custom container implementation failed”，属于 runner 容器执行环境异常，非代码或测试本身问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709148



- **base-b-test-1-npu-a3 / run (0)**: 日志显示在容器内安装依赖后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时/环境故障，非代码或测试本身问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709250

- **base-b-test-8-npu-a3 / run (0)**: 日志显示在解包 deb 包过程中出现“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境故障，并非代码或测试本身的问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709356

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 pip 安装依赖过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非代码或测试本身问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125788709454

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125787847648) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596763082/job/125787847713) |


## [Run #41596403073](https://github.com/sgl-project/sglang/actions/runs/41596403073)
- **分支**: `lsyin/sched-pr14`
- **总耗时**: 10.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41596403073

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 2.4min | 其他 | 日志中未出现实际测试执行或失败信息，作业在检出代码后即结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120290) |
| base-b-test-16-npu-a3 / run (0) | 3.2min | 环境问题 | git fetch 因 shallow 文件被并发修改而失败，重试后成功，但作业仍以失败结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120321) |
| multimodal-gen-test-4-npu-a3 (0) | 3.3min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120344) |
| base-b-test-8-npu-a3 / run (0) | 3.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120360) |
| base-b-test-2-npu-a3 / run (0) | 3.3min | 环境问题 | 自托管 runner 执行自定义容器失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120406) |
| base-b-test-1-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120444) |
| base-b-test-4-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120455) |
| base-b-test-4-npu-a3 / run (1) | 3.2min | 环境问题 | 作业在 checkout 后执行 k8s 启动脚本时异常退出，未进入实际测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120604) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅包含 runner 初始化、下载 action、git fetch/checkout 等准备步骤，随后清理孤儿进程结束，未见测试运行或报错。可能是作业被取消、超时或日志截断，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120290

- **base-b-test-16-npu-a3 / run (0)**: checkout 阶段首次 fetch 报错 'fatal: shallow file has changed since we read it'（exit 128），疑似多个 runner 共享同一 git 缓存目录导致并发冲突；重试后 fetch 成功，但作业最终仍失败，需检查后续步骤或 runner 缓存隔离。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120321

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或路径配置有误，缺少实际报错信息，无法判定具体失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120344


- **base-b-test-2-npu-a3 / run (0)**: 日志显示在解包 apt 依赖包过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非代码或测试本身问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120406

- **base-b-test-1-npu-a3 / run (0)**: 日志显示在解包 apt 依赖包过程中报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境异常，非代码或测试本身问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120444

- **base-b-test-4-npu-a3 / run (0)**: 日志显示在解包 apt 依赖包过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，并非代码或测试本身问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120455

- **base-b-test-4-npu-a3 / run (1)**: 日志显示代码检出成功后运行 /home/runner/k8s/index.js，随即出现 Node.js 弃用警告并清理孤儿进程，作业终止，未见测试执行或报错堆栈，疑似 runner 环境或启动脚本问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125786120604

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125785252025) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596403073/job/125785252046) |


## [Run #41596278362](https://github.com/sgl-project/sglang/actions/runs/41596278362)
- **分支**: `yanbing/cpu-fp8-quant-support`
- **总耗时**: 55.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41596278362

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125794973674) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 推理服务运行正常（吞吐正常、请求返回200），但随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时/基础设施故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125794973674

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125784411433) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125784411446) |
| multimodal-gen-test-4-npu-a3 (0) | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233613) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233646) |
| base-b-test-1-npu-a3 / run (0) | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233648) |
| base-b-test-2-npu-a3 / run (0) | 26.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233660) |
| multimodal-gen-test-1-npu-a3 (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233667) |
| multimodal-gen-test-4-npu-a3 (1) | 27.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233675) |
| base-b-test-16-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233737) |
| base-b-test-4-npu-a3 / run (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233785) |
| base-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233810) |
| base-b-test-8-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125785233921) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125794973763) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596278362/job/125794974086) |


## [Run #41596210773](https://github.com/sgl-project/sglang/actions/runs/41596210773)
- **分支**: `lsyin/cpu-process-imports`
- **总耗时**: 10.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41596210773

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.7min | 环境问题 | Git 拉取代码时浅克隆文件状态异常导致 checkout 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075660) |
| multimodal-gen-test-1-npu-a3 (1) | 5.6min | 环境问题 | 作业在拉取代码后、执行测试前异常终止，未见测试输出 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075717) |
| multimodal-gen-test-1-npu-a3 (0) | 6.5min | 环境问题 | git fetch 因 shallow 文件被并发修改而失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075761) |
| multimodal-gen-test-4-npu-a3 (1) | 6.7min | 环境问题 | Git 拉取代码时 shallow 文件被并发修改导致 fetch 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075771) |
| base-b-test-8-npu-a3 / run (0) | 6.0min | 环境问题 | Git 拉取代码时内部 CDN 代理返回 502 错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075780) |
| base-b-test-16-npu-a3 / run (0) | 6.0min | 环境问题 | 拉取代码时内部 Git 镜像服务返回 502，重试后成功但作业仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075788) |
| base-b-test-1-npu-a3 / run (0) | 4.9min | 环境问题 | 作业在 checkout 后执行 k8s 脚本时异常退出，未进入实际测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075810) |
| base-b-test-4-npu-a3 / run (0) | 5.0min | 环境问题 | 作业在 checkout 后运行 k8s 索引脚本时异常退出，未进入实际测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075848) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075861) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | Git 拉取代码时内部 CDN 服务返回 502 错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075980) |

- **multimodal-gen-test-4-npu-a3 (0)**: git fetch 报错 'fatal: shallow file has changed since we read it'（exit 128），重试后虽完成 checkout，但作业在后续步骤异常终止，属 runner/缓存环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075660

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 checkout 完成后再次运行 k8s 脚本即清理孤儿进程并结束，无任何测试执行或报错信息，疑似 runner 环境/容器启动异常导致作业提前终止，需查看被省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075717

- **multimodal-gen-test-1-npu-a3 (0)**: checkout 阶段执行 git fetch 时报错 'fatal: shallow file has changed since we read it'（exit 128），重试后成功，但作业最终仍失败，属于 runner 环境/并发导致的 git 仓库状态异常，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075761

- **multimodal-gen-test-4-npu-a3 (1)**: checkout 阶段执行 git fetch 时报错 'fatal: shallow file has changed since we read it'（退出码128），重试后成功。属于 runner 上 git 仓库缓存/并发访问的环境问题，非代码或测试本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075771

- **base-b-test-8-npu-a3 / run (0)**: checkout 阶段访问 git-cdn-service 返回 502，首次 fetch 失败，重试后成功；随后作业在运行 k8s 脚本后异常结束，属基础设施/网络代理问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075780

- **base-b-test-16-npu-a3 / run (0)**: git fetch 访问内部 git-cdn-service 返回 502 错误，重试后拉取成功；随后 k8s 步骤执行后作业结束，失败原因指向基础设施/网络不稳定，而非代码或测试本身。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075788

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 git fetch 耗时约2分钟，checkout 成功后运行 /home/runner/k8s/index.js 仅输出 Node 弃用警告便清理孤儿进程结束，无测试执行记录，疑似 runner 环境或 k8s 启动脚本异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075810

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 git checkout 成功后执行 /home/runner/k8s/index.js，仅出现 Node.js 弃用警告，随后清理孤儿进程并结束，无测试输出，疑似 runner 环境或 k8s 脚本执行失败导致作业中止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075848

- **base-b-test-4-npu-a3 / run (1)**: 日志显示在容器内安装 python3.10 包后报错“Executing the custom container implementation failed”，属于 runner 容器环境/配置问题，非代码或测试本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075861

- **base-b-test-2-npu-a3 / run (0)**: checkout 阶段访问 git-cdn-service 返回 502 Bad Gateway，首次 fetch 失败退出码 128，重试后成功，但作业最终仍失败，属于 CI 基础设施/网络代理问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125785075980

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125784205893) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210773/job/125784206157) |


## [Run #41596210368](https://github.com/sgl-project/sglang/actions/runs/41596210368)
- **分支**: `rocm-deterministic-aiter-prefill-gfx950`
- **总耗时**: 27.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41596210368

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.6min | 代码错误 | NPU MLA FIA HiCache 测试用例执行失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864234) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864367) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 运行约96秒后返回退出码5，8个测试全部未通过（0/8 passed），导致作业以退出码1失败。退出码5通常表示pytest未收集到测试或测试内部错误，需检查该用例在A3 NPU环境下的兼容性。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864234


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125964670191) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125964670238) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965863917) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864041) |
| base-b-test-4-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864267) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864330) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864374) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41596210368/job/125965864409) |


## [Run #41595854524](https://github.com/sgl-project/sglang/actions/runs/41595854524)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 21.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41595854524

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 18.5min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714648) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures/ 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714665) |
| multimodal-gen-test-4-npu-a3 (0) | 18.4min | 其他 | 多模态生成测试未产出 diffusion-failures 目录，上传产物时无文件可传，作业失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714767) |
| base-b-test-1-npu-a3 / run (0) | 18.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714806) |
| base-b-test-2-npu-a3 / run (0) | 18.7min | 环境问题 | 自托管 runner 执行自定义容器失败，非测试代码本身报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714853) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714917) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被省略，未见测试执行或报错内容；仅提示未找到 diffusion-failures/ 路径，无产物上传。作业失败原因无法从现有日志确定，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714648

- **multimodal-gen-test-1-npu-a3 (1)**: 作业日志被省略，未见明确报错；末尾提示未找到 diffusion-failures/ 路径，无 artifact 上传，随后正常清理。失败原因无法从现有日志确定，需查看中间省略部分。
  链接: https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714665

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾显示“No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.”，说明测试未生成预期失败样本目录，可能是测试用例未触发失败或输出路径配置不符，导致产物上传步骤无文件而失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714767

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在执行第6个测试 test_npu_eagle3.py 时，属于 runner 容器环境故障，非测试代码本身报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714806

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境故障，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714853

- **base-b-test-4-npu-a3 / run (0)**: 模型分片加载到 67% 时，runner 报错“Executing the custom container implementation failed”，属于自托管 runner/容器环境故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714917

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783050301) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783050328) |
| multimodal-gen-test-1-npu-a3 (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714669) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714781) |
| base-b-test-8-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714861) |
| base-b-test-4-npu-a3 / run (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41595854524/job/125783714935) |


## [Run #41594662982](https://github.com/sgl-project/sglang/actions/runs/41594662982)
- **分支**: `lsyin/sched-pr14`
- **总耗时**: 9.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41594662982

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | 环境问题 | 作业在代码检出后立即被清理，未执行任何测试步骤 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744073) |
| base-b-test-1-npu-a3 / run (0) | 4.5min | 环境问题 | 作业在 checkout 后执行 k8s 索引脚本时异常退出，未进入实际测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744130) |
| base-b-test-8-npu-a3 / run (0) | 5.1min | 环境问题 | git fetch 因浅克隆文件被并发修改而失败，重试后成功，但作业随后异常终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744192) |
| multimodal-gen-test-4-npu-a3 (1) | 6.2min | 环境问题 | Git 拉取代码时浅克隆文件被并发修改，导致 checkout 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744242) |
| base-b-test-4-npu-a3 / run (1) | 4.2min | 环境问题 | 作业在 checkout 后执行 k8s 索引脚本时异常退出，未进入实际测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744248) |
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | Git 检出时残留 shallow.lock 文件导致 fetch 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744250) |
| base-b-test-16-npu-a3 / run (0) | 5.9min | 环境问题 | Git 拉取代码时 shallow 文件异常导致 checkout 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744327) |
| base-b-test-4-npu-a3 / run (0) | 5.2min | 环境问题 | git fetch 时浅克隆文件被并发修改导致失败，重试后成功 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744375) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 checkout 完成后，k8s 脚本运行即触发 orphan 进程清理并结束作业，无测试输出或报错信息，疑似 runner 环境或 k8s 调度异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744073

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 git fetch/checkout 成功，随后运行 /home/runner/k8s/index.js 时仅输出 Node.js 弃用警告便清理孤儿进程结束，未执行任何 NPU 测试，属于 CI 运行环境/脚本异常，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744130

- **base-b-test-8-npu-a3 / run (0)**: 首次 git fetch 报错“shallow file has changed since we read it”（exit 128），重试后拉取成功并完成 checkout；随后运行 k8s 脚本时仅出现 Node.js 弃用警告，日志未显示具体测试失败原因，疑似 runner 环境或基础设施异常导致作业中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744192

- **multimodal-gen-test-4-npu-a3 (1)**: git fetch 报错 'fatal: shallow file has changed since we read it'（exit 128），重试后成功。属于 runner 上并发 git 操作或缓存代理导致的仓库状态冲突，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744242

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 checkout 成功，随后运行 /home/runner/k8s/index.js 后立即出现清理孤儿进程并结束，无测试输出，疑似 runner 环境或 k8s 启动脚本异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744248

- **base-b-test-2-npu-a3 / run (0)**: checkout 阶段 git fetch 报错：.git/shallow.lock 文件已存在，疑似有残留 git 进程或上次运行崩溃遗留锁文件；重试后成功，但作业仍失败，属 runner 环境/缓存残留问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744250

- **base-b-test-16-npu-a3 / run (0)**: git fetch 首次报错 fatal: shallow file has changed since we read it，退出码 128；重试后成功，但作业随后在运行 k8s 脚本后异常结束，属 CI 环境/基础设施问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744327

- **base-b-test-4-npu-a3 / run (0)**: 首次 git fetch 报错 'fatal: shallow file has changed since we read it'（exit 128），疑似多个作业共享同一仓库目录或缓存导致浅克隆状态冲突；15 秒后重试成功，checkout 正常完成。属基础设施/环境问题，非代码缺陷。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125781744375

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125780977848) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594662982/job/125780977877) |


## [Run #41594316193](https://github.com/sgl-project/sglang/actions/runs/41594316193)
- **分支**: `ecao/cpu_graph_prefill2`
- **总耗时**: 24.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41594316193

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures/ 目录，无产物可上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457282) |
| multimodal-gen-test-4-npu-a3 (0) | 16.5min | 其他 | 多模态生成测试失败，且未生成失败产物目录 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457337) |
| multimodal-gen-test-1-npu-a3 (1) | 14.3min | 其他 | 作业失败但日志中未见明确错误，仅显示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457394) |
| base-b-test-2-npu-a3 / run (0) | 15.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457395) |
| base-b-test-1-npu-a3 / run (0) | 15.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457471) |
| multimodal-gen-test-4-npu-a3 (1) | 14.7min | 其他 | 多模态生成测试未产出 diffusion-failures 目录，导致产物上传失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457509) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457536) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457589) |

- **multimodal-gen-test-1-npu-a3 (0)**: 作业日志被截断，未见实际测试报错；末尾仅提示未找到 diffusion-failures/ 路径，无 artifact 上传，随后正常清理退出。需查看完整日志确认测试是否真正执行或失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457282

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示测试作业运行约16分钟后结束，上传产物时提示未找到 diffusion-failures/ 路径，说明测试失败但未按预期生成失败样本目录；日志中段被省略，无法定位具体报错，需查看完整日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457337

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示 'No files were found with the provided path: diffusion-failures/'，说明测试可能未生成失败产物目录；中间省略部分可能包含真正失败原因，需查看完整日志确认。其余均为 Node.js 弃用警告，非失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457394

- **base-b-test-2-npu-a3 / run (0)**: 前3个测试均通过，第4个测试启动后约4秒报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非测试代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457395

- **base-b-test-1-npu-a3 / run (0)**: 模型权重加载完成后，日志报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员。这属于 runner 容器环境异常，并非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457471

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示测试阶段未生成 diffusion-failures/ 目录，upload-artifact 报“No files were found”，作业因此失败；中间省略部分可能包含真正的测试报错，需查看完整日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457509

- **base-b-test-16-npu-a3 / run (0)**: 模型权重加载完成后，日志报错“Executing the custom container implementation failed”，属于 runner/容器环境异常，非代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457536

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner 容器环境异常，非代码或精度问题；此前 mamba 导入告警为可忽略的模型加载提示。
  链接: https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457589

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125778613592) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125778613599) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457424) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594316193/job/125779457526) |


## [Run #41594170024](https://github.com/sgl-project/sglang/actions/runs/41594170024)
- **分支**: `chunyuan/dp_frontend`
- **总耗时**: 7.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41594170024

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 3.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125778600023) |
| base-b-test-8-npu-a3 / run (0) | 1.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125778600030) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125778600094) |
| base-b-test-2-npu-a3 / run (0) | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125778600144) |
| base-b-test-4-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125778601053) |






### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125777743192) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41594170024/job/125777743195) |


## [Run #41593286482](https://github.com/sgl-project/sglang/actions/runs/41593286482)
- **分支**: `ecao/cpu_graph_prefill2`
- **总耗时**: 10.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41593286482

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 2.3min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081237) |
| multimodal-gen-test-1-npu-a3 (1) | 5.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081281) |
| multimodal-gen-test-4-npu-a3 (1) | 5.3min | 其他 | 测试未生成 diffusion-failures 目录，产物上传时无文件可传，作业失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081304) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | 其他 | 作业未找到 diffusion-failures 目录，无产物可上传，但日志未显示明确失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081334) |
| base-b-test-2-npu-a3 / run (0) | 3.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081368) |
| base-b-test-8-npu-a3 / run (0) | 3.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081409) |
| base-b-test-16-npu-a3 / run (0) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081417) |
| base-b-test-4-npu-a3 / run (0) | 3.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081436) |
| base-b-test-4-npu-a3 / run (1) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081464) |
| base-b-test-1-npu-a3 / run (0) | 3.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081479) |

- **multimodal-gen-test-1-npu-a3 (0)**: 作业日志主要为 Node.js 弃用警告和 git 清理步骤，未包含实际测试执行或报错内容；唯一异常是“No files were found with the provided path: diffusion-failures/”，说明预期产物目录不存在，但不足以判定测试失败原因，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081237


- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明多模态生成测试未产出预期失败样本目录，可能是测试未执行或提前退出，导致上传产物步骤无文件而失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081304

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示上传产物时提示 'No files were found with the provided path: diffusion-failures/'，说明测试未生成失败产物目录；其余均为 Node.js 弃用警告和清理步骤，缺少实际测试失败的错误信息，需查看被省略的中间日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125776081334







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125775291809) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41593286482/job/125775291813) |


## [Run #41592931472](https://github.com/sgl-project/sglang/actions/runs/41592931472)
- **分支**: `amd/gfx11-pad-linear-weights`
- **总耗时**: 42.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41592931472

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556465) |
| base-b-test-4-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556526) |
| base-b-test-2-npu-a3 / run (0) | 3.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556554) |
| base-b-test-1-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556555) |
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556584) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556677) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125773722856) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125773722867) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556381) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556393) |
| multimodal-gen-test-4-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556430) |
| multimodal-gen-test-4-npu-a3 (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592931472/job/125774556523) |


## [Run #41592906386](https://github.com/sgl-project/sglang/actions/runs/41592906386)
- **分支**: `new-model-support`
- **总耗时**: 81.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41592906386

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125794936703) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 /generate 请求均返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非测试用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125794936703

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125773637023) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125773637055) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462184) |
| base-b-test-1-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462187) |
| multimodal-gen-test-1-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462203) |
| multimodal-gen-test-1-npu-a3 (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462219) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462233) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462239) |
| base-b-test-4-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462247) |
| base-b-test-2-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462285) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462361) |
| base-b-test-16-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125774462464) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125784940944) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125784940961) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125784940990) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592906386/job/125794936730) |


## [Run #41592885006](https://github.com/sgl-project/sglang/actions/runs/41592885006)
- **分支**: `lc-dsv4-l3-upstream`
- **总耗时**: 37.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41592885006

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265207) |
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265230) |
| base-b-test-2-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265310) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265377) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265378) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265428) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125773578873) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125773578904) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774264620) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774264645) |
| multimodal-gen-test-4-npu-a3 (0) | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774264946) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592885006/job/125774265042) |


## [Run #41592788376](https://github.com/sgl-project/sglang/actions/runs/41592788376)
- **分支**: `mani1106/fuse-qwen3-prefill`
- **总耗时**: 6.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41592788376

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592788376/job/125773897141) |
| base-b-test-4-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592788376/job/125773897245) |
| base-b-test-4-npu-a3 / run (1) | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41592788376/job/125773897295) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592788376/job/125773314957) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592788376/job/125773315008) |


## [Run #41592686275](https://github.com/sgl-project/sglang/actions/runs/41592686275)
- **分支**: `oss-sync-e54877d341`
- **总耗时**: 47.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41592686275

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.6min | 精度回归 | GLM5 top64 pruned 8p GSM8K 精度测试失败，退出码5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125781965145) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: accuracy 测试套件中 test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 运行约467秒后返回退出码5，0/2通过；后续脚本因变量含换行导致整数比较报错，最终作业退出码1。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125781965145

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125772934537) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125772934571) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772831) |
| multimodal-gen-test-4-npu-a3 (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772851) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772939) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772944) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772963) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772971) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773772988) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125773773005) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125781964989) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41592686275/job/125781965148) |


## [Run #41591937404](https://github.com/sgl-project/sglang/actions/runs/41591937404)
- **分支**: `oss-sync-e54877d341`
- **总耗时**: 7.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41591937404

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265646) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265692) |
| base-b-test-16-npu-a3 / run (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265707) |
| base-b-test-4-npu-a3 / run (1) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265725) |
| base-b-test-4-npu-a3 / run (0) | 1.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265820) |
| base-b-test-1-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265821) |
| base-b-test-2-npu-a3 / run (0) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265831) |
| base-b-test-8-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125771265900) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125770558540) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591937404/job/125770558677) |


## [Run #41591638339](https://github.com/sgl-project/sglang/actions/runs/41591638339)
- **分支**: `ecao/cpu_graph_prefill2`
- **总耗时**: 17.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41591638339

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 13.3min | 其他 | 日志中未见明确失败原因，仅显示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770513938) |
| multimodal-gen-test-4-npu-a3 (1) | 13.4min | 其他 | 多模态生成测试未产出 diffusion-failures 目录，导致产物上传失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770513954) |
| multimodal-gen-test-1-npu-a3 (1) | 12.3min | 其他 | 多模态生成测试失败，且未生成 diffusion-failures 目录，导致无失败产物可上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770513961) |
| multimodal-gen-test-1-npu-a3 (0) | 12.5min | 其他 | 作业失败但日志中未见明确错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514006) |
| base-b-test-2-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514124) |
| base-b-test-4-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514163) |
| base-b-test-1-npu-a3 / run (0) | 3.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514185) |
| base-b-test-4-npu-a3 / run (1) | 2.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514347) |
| base-b-test-16-npu-a3 / run (0) | 2.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514718) |
| base-b-test-8-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514855) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业日志被省略，可见部分只有 Node.js 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或测试未正常执行，无法定位具体失败点，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770513938

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示测试阶段未生成 diffusion-failures/ 目录，upload-artifact 报“No files were found”，无产物可上传；日志中未见具体测试报错，失败原因需查看被省略的中间测试输出。
  链接: https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770513954

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示测试作业执行后未找到 diffusion-failures/ 路径，说明测试失败但未产出失败样本或目录未创建；日志中段被省略，无法定位具体报错，需查看完整日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770513961

- **multimodal-gen-test-1-npu-a3 (0)**: 日志末尾仅提示未找到 diffusion-failures/ 路径、无产物上传，并伴随 Node.js 弃用警告；中间省略部分可能含真正失败原因，但可见信息不足以判定为性能/精度/环境/代码错误或超时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125770514006







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125769618745) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591638339/job/125769618846) |


## [Run #41591191285](https://github.com/sgl-project/sglang/actions/runs/41591191285)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 34.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41591191285

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 3.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053805) |
| base-b-test-8-npu-a3 / run (0) | 3.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053827) |
| base-b-test-4-npu-a3 / run (1) | 3.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053844) |
| base-b-test-4-npu-a3 / run (0) | 3.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053860) |
| base-b-test-1-npu-a3 / run (0) | 3.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053911) |
| base-b-test-16-npu-a3 / run (0) | 3.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769054029) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125768219875) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125768219909) |
| multimodal-gen-test-4-npu-a3 (1) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053595) |
| multimodal-gen-test-1-npu-a3 (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053637) |
| multimodal-gen-test-1-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053709) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41591191285/job/125769053754) |


## [Run #41590538906](https://github.com/sgl-project/sglang/actions/runs/41590538906)
- **分支**: `jeeja/add_mamba_xpu`
- **总耗时**: 14.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41590538906

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767019962) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767020034) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767020043) |
| base-b-test-4-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767020068) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767020078) |
| base-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767020083) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125766137898) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125766137947) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767019885) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41590538906/job/125767019927) |


## [Run #41589307217](https://github.com/sgl-project/sglang/actions/runs/41589307217)
- **分支**: `dsv4_hisparse_dspark`
- **总耗时**: 33.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41589307217

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154356) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154417) |
| base-b-test-4-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154463) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154498) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154505) |
| base-b-test-8-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154624) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125762287924) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125762288084) |
| multimodal-gen-test-4-npu-a3 (0) | 29.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154243) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154307) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154353) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41589307217/job/125763154383) |


## [Run #41588879309](https://github.com/sgl-project/sglang/actions/runs/41588879309)
- **分支**: `feat/ling3-fp8-decode-kernels`
- **总耗时**: 34.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41588879309

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761500012) |
| base-b-test-2-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761500160) |
| base-b-test-16-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761500165) |
| base-b-test-8-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761500181) |
| base-b-test-4-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761500234) |
| base-b-test-4-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761500265) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125760812737) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125760812898) |
| multimodal-gen-test-4-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761497684) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761497751) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761497978) |
| multimodal-gen-test-1-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41588879309/job/125761498117) |


## [Run #41586662810](https://github.com/sgl-project/sglang/actions/runs/41586662810)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 38.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41586662810

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 9.5min | 代码错误 | NPU PD分离测试用例执行失败，返回退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572710) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行321秒后报错（errors=1），2个测试0通过，进程退出码1导致作业失败。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572710

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125753762338) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125753762440) |
| multimodal-gen-test-1-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572617) |
| multimodal-gen-test-4-npu-a3 (1) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572646) |
| multimodal-gen-test-1-npu-a3 (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572658) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572665) |
| base-b-test-1-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572690) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572760) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572788) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572837) |
| multimodal-gen-test-4-npu-a3 (0) | 32.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586662810/job/125754572885) |


## [Run #41586371049](https://github.com/sgl-project/sglang/actions/runs/41586371049)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 29.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41586371049

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | 其他 | 多模态生成测试失败，且未生成 diffusion-failures 目录，无失败产物可上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994359) |
| multimodal-gen-test-4-npu-a3 (1) | 16.4min | 其他 | 日志中未出现明确失败原因，仅显示产物目录为空且作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994384) |
| multimodal-gen-test-4-npu-a3 (0) | 16.3min | 其他 | 多模态生成测试未产出 diffusion-failures 目录，导致产物上传失败，作业失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994436) |
| base-b-test-8-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型加载阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994446) |
| base-b-test-4-npu-a3 / run (0) | 14.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994474) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994492) |
| base-b-test-1-npu-a3 / run (0) | 12.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994507) |
| base-b-test-2-npu-a3 / run (0) | 12.3min | 环境问题 | 自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994508) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示测试作业运行约16分钟后结束，上传产物时提示未找到 diffusion-failures/ 路径，说明测试未产出预期失败样本目录，可能测试提前失败或未执行到产物生成步骤；日志中段被省略，无法定位具体报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994359

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，未捕获到实际报错；作业在约16分钟后进入清理阶段，疑似测试未产出失败产物或进程异常退出，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994384

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示测试阶段未生成 diffusion-failures/ 目录，upload-artifact 报“No files were found”，无产物可上传；中间省略部分可能含测试失败或未执行，需查看完整日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994436

- **base-b-test-8-npu-a3 / run (0)**: 日志显示各 TP/EP 进程正在加载权重时，runner 报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994446

- **base-b-test-4-npu-a3 / run (0)**: 日志显示推理任务仍在正常输出吞吐量，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，而非测试用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994474

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾显示 Test Summary: 1/1 passed，测试文件 test_npu_speculative_moe_a2a_backend.py 成功，耗时640.8s，仅存在 Node.js 弃用警告，未见失败信息。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994492

- **base-b-test-1-npu-a3 / run (0)**: 测试本身已通过（Ran 1 test, OK），但随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时/基础设施故障，并非代码或模型问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994507

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试请求均返回200 OK，随后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于自托管 runner 的容器运行时故障，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994508

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754432623) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754432647) |
| multimodal-gen-test-1-npu-a3 (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994439) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586371049/job/125754994574) |


## [Run #41586237615](https://github.com/sgl-project/sglang/actions/runs/41586237615)
- **分支**: `ecao/xpu_graph_context_aware_opt`
- **总耗时**: 18.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41586237615

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009142) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009144) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009163) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009182) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009214) |
| base-b-test-4-npu-a3 / run (0) | 2.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009251) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125752388673) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125752389584) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009018) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586237615/job/125753009028) |


## [Run #41586218471](https://github.com/sgl-project/sglang/actions/runs/41586218471)
- **分支**: `ecao/cpu_graph_prefill2`
- **总耗时**: 36.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41586218471

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076240) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076242) |
| base-b-test-4-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076293) |
| base-b-test-4-npu-a3 / run (0) | 2.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076296) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076319) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076701) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125752372822) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125752372967) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076139) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076207) |
| multimodal-gen-test-4-npu-a3 (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076212) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586218471/job/125753076320) |


## [Run #41586144373](https://github.com/sgl-project/sglang/actions/runs/41586144373)
- **分支**: `rocm-deterministic-aiter-prefill-gfx950`
- **总耗时**: 7.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41586144373

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | 其他 | 测试失败但日志中未见具体错误，仅显示未找到 diffusion-failures 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733578) |
| multimodal-gen-test-4-npu-a3 (1) | 4.3min | 其他 | 多模态生成测试未产出 diffusion-failures 目录，疑似测试未执行或提前失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733587) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733649) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733674) |
| base-b-test-4-npu-a3 / run (1) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733680) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733701) |
| base-b-test-2-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733728) |
| base-b-test-4-npu-a3 / run (0) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733883) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能失败但未生成失败产物目录，无法定位具体原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733578

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中仅见上传 artifact 时提示未找到 diffusion-failures/ 路径，无明确报错堆栈；中间省略部分可能含真实失败原因，需查看完整日志确认测试是否启动或崩溃。
  链接: https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752733587







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752142650) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41586144373/job/125752142776) |


## [Run #41583771116](https://github.com/sgl-project/sglang/actions/runs/41583771116)
- **分支**: `fix_pp_pd_hicache_consensus_checker_1026`
- **总耗时**: 20.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41583771116

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41583771116/job/125745284258) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41583771116/job/125745284440) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41583771116/job/125744484540) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41583771116/job/125744484846) |


## [Run #41582774906](https://github.com/sgl-project/sglang/actions/runs/41582774906)
- **分支**: `lsyin/sched-pr13`
- **总耗时**: 77.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41582774906

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 15.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125759064605) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 19.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125759064625) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示推理请求均返回 200 OK，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非测试用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125759064605

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示推理服务正常返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非测试用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125759064625

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125741515866) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125741515879) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742262847) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742262897) |
| base-b-test-4-npu-a3 / run (0) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742263015) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742263036) |
| base-b-test-16-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742263071) |
| base-b-test-2-npu-a3 / run (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742263121) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742263125) |
| base-b-test-8-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125742263152) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582774906/job/125759064595) |


## [Run #41582087367](https://github.com/sgl-project/sglang/actions/runs/41582087367)
- **分支**: `fix/llava_and_blip`
- **总耗时**: 54.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41582087367

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.1min | 超时 | NPU DP attention 测试因服务进程被 SIGKILL 终止而失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014600) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行约 502 秒后，fixture 检测到 server 进程 rc=-9（被 SIGKILL，疑似 OOM 或超时被杀），触发 fail-fast，测试以 exit code 137 失败，0/2 通过。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014600

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125739232431) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125739232539) |
| multimodal-gen-test-1-npu-a3 (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014440) |
| multimodal-gen-test-1-npu-a3 (1) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014444) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014454) |
| base-b-test-2-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014555) |
| multimodal-gen-test-4-npu-a3 (1) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014567) |
| base-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014579) |
| base-b-test-16-npu-a3 / run (0) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014580) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014640) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41582087367/job/125740014704) |


## [Run #41581999028](https://github.com/sgl-project/sglang/actions/runs/41581999028)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 44.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41581999028

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587932) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587956) |
| base-b-test-2-npu-a3 / run (0) | 0.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587974) |
| base-b-test-16-npu-a3 / run (0) | 3.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587982) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587996) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739588086) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125738909347) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125738909361) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587713) |
| multimodal-gen-test-4-npu-a3 (0) | 41.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587781) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587814) |
| multimodal-gen-test-4-npu-a3 (1) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581999028/job/125739587835) |


## [Run #41581647824](https://github.com/sgl-project/sglang/actions/runs/41581647824)
- **分支**: `ecao/xpu_graph_context_aware_opt`
- **总耗时**: 16.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41581647824

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601176) |
| base-b-test-2-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601305) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601309) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601324) |
| base-b-test-1-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601345) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601348) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125737756829) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125737756834) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601150) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581647824/job/125738601181) |


## [Run #41581444357](https://github.com/sgl-project/sglang/actions/runs/41581444357)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 47.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41581444357

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740124950) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125031) |
| base-b-test-4-npu-a3 / run (1) | 17.4min | 代码错误 | NPU PD分离测试用例执行失败，退出码5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125040) |
| base-b-test-2-npu-a3 / run (0) | 14.7min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125066) |
| base-b-test-4-npu-a3 / run (0) | 9.7min | 超时 | NPU DP attention 测试因服务进程被 SIGKILL 终止而失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125162) |



- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行646秒后返回退出码5（pytest无测试收集或全部失败），2个用例0通过，导致作业失败。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125040

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型加载和 tokenizer 初始化正常，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境故障，并非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125066

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行约170秒后，server 进程 rc=-9（SIGKILL）退出，触发 fail-fast，测试返回 exit code 137，疑似 OOM 或资源不足导致进程被杀。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125162

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125739420236) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125739420240) |
| multimodal-gen-test-1-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740124744) |
| multimodal-gen-test-4-npu-a3 (0) | 36.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740124758) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740124805) |
| multimodal-gen-test-4-npu-a3 (1) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740124816) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41581444357/job/125740125042) |


## [Run #41575235496](https://github.com/sgl-project/sglang/actions/runs/41575235496)
- **分支**: `c/cutedsl-mla-draft-extend`
- **总耗时**: 57.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41575235496

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 17.8min | 精度回归 | GLM5 top64 pruned 精度测试用例失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125728754099) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 作业中 2 个精度用例仅 1 个通过；test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 返回 exit code 5（pytest 无用例收集/未通过），耗时 370s，导致作业整体退出码 1 失败。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125728754099

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717186330) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717186364) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917413) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917467) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917562) |
| base-b-test-2-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917568) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917614) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917631) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917650) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125717917678) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125728754058) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575235496/job/125728754121) |


## [Run #41575190385](https://github.com/sgl-project/sglang/actions/runs/41575190385)
- **分支**: `halops_sglang`
- **总耗时**: 75.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41575190385

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125752969106) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 推理任务正常输出后，日志报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非测试用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125752969106

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738075903) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738075978) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663714) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663756) |
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663787) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663808) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663814) |
| base-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663899) |
| base-b-test-8-npu-a3 / run (0) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663909) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663939) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738663959) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125738664003) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125752969087) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41575190385/job/125752969163) |


## [Run #41572148925](https://github.com/sgl-project/sglang/actions/runs/41572148925)
- **分支**: `lsyin/indirect-import-lint`
- **总耗时**: 36.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41572148925

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125716826258) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 apt 下载依赖过程中报错“Executing the custom container implementation failed”，属于 runner/容器环境问题，非代码或性能回归，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125716826258

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125707782144) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125707782197) |
| base-b-test-1-npu-a3 / run (0) | 6.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125708546301) |
| base-b-test-2-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125708546304) |
| base-b-test-4-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125708546327) |
| base-b-test-4-npu-a3 / run (1) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41572148925/job/125708546336) |


## [Run #41571699769](https://github.com/sgl-project/sglang/actions/runs/41571699769)
- **分支**: `wuyaole/fix-prefill-reservation-budget`
- **总耗时**: 53.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41571699769

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.6min | 精度回归 | GLM5 top64 pruned 8p GSM8K 精度测试失败，退出码 5，0/2 通过 | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125716594742) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 运行约 459 秒后返回 exit code 5，测试汇总 0/2 通过，属于精度用例失败；后续 shell 因汇总值含换行报 integer expression expected，导致作业退出码 1。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125716594742

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706041760) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706041823) |
| multimodal-gen-test-1-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918583) |
| multimodal-gen-test-4-npu-a3 (0) | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918593) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918653) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918687) |
| base-b-test-2-npu-a3 / run (0) | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918710) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918731) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918764) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918860) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918889) |
| base-b-test-8-npu-a3 / run (0) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125706918932) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125716594666) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571699769/job/125716594727) |


## [Run #41571425060](https://github.com/sgl-project/sglang/actions/runs/41571425060)
- **分支**: `ecao/xpu_graph_context_aware_opt`
- **总耗时**: 40.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41571425060

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 9.0min | 代码错误 | NPU EPLB 最小重平衡利用率阈值测试用例执行失败，退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400496) |
| base-b-test-4-npu-a3 / run (1) | 14.8min | 代码错误 | NPU PD 分离测试用例 test_npu_pd_disaggregation.py 运行失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400635) |

- **base-b-test-8-npu-a3 / run (0)**: test_npu_eplb_min_rebalancing_utilization_threshold.py 运行 281 秒后返回退出码 1，测试汇总为 0/1 通过，属于用例断言或逻辑失败，并非超时或环境问题。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400496

- **base-b-test-4-npu-a3 / run (1)**: 该测试文件执行 646 秒后返回 exit code 5（pytest 无测试被收集/全部跳过或内部错误），2 个用例 0 通过，导致作业失败。需检查该用例在 A3 环境下的启动参数与用例收集情况。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400635

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125705265630) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125705265658) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400354) |
| base-b-test-16-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400501) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400533) |
| base-b-test-2-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400542) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400612) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41571425060/job/125706400668) |


## [Run #41570881929](https://github.com/sgl-project/sglang/actions/runs/41570881929)
- **分支**: `lsyin/indirect-import-lint`
- **总耗时**: 7.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41570881929

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 5.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570881929/job/125705194289) |
| base-b-test-4-npu-a3 / run (1) | 5.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570881929/job/125705194319) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570881929/job/125705194321) |
| base-b-test-1-npu-a3 / run (0) | 5.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570881929/job/125705194366) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41570881929/job/125704491516) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41570881929/job/125704491732) |


## [Run #41570670828](https://github.com/sgl-project/sglang/actions/runs/41570670828)
- **分支**: `ecao/xpu_graph_context_aware_opt`
- **总耗时**: 8.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41570670828

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 3.2min | 其他 | 作业失败但日志中未见明确错误，仅显示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394631) |
| multimodal-gen-test-4-npu-a3 (0) | 3.2min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394641) |
| base-b-test-1-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394710) |
| base-b-test-4-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394713) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394715) |
| base-b-test-16-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394733) |
| base-b-test-8-npu-a3 / run (0) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394820) |
| base-b-test-4-npu-a3 / run (1) | 4.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394837) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被省略，可见部分只有 Node.js 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或提前退出，具体失败原因需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394631

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试产物目录不存在，可能是测试未生成失败样本或路径配置有误，但缺少实际报错信息，无法确定根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125703394641







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125702688144) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41570670828/job/125702688147) |


## [Run #41567832278](https://github.com/sgl-project/sglang/actions/runs/41567832278)
- **分支**: `xlm-roberta-masked-lm-embedding`
- **总耗时**: 84.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41567832278

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 20.7min | 精度回归 | GLM5 top64 pruned 精度测试用例失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125709955669) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 作业中 2 个精度用例仅 1 个通过；test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 返回 exit code 5（pytest 无用例收集/未执行），耗时 309s，导致作业失败。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125709955669

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125693661058) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125693661067) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490083) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490098) |
| multimodal-gen-test-1-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490102) |
| base-b-test-16-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490136) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490137) |
| base-b-test-1-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490222) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490258) |
| base-b-test-4-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490267) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490337) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125694490363) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125709955710) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567832278/job/125709955749) |


## [Run #41567481151](https://github.com/sgl-project/sglang/actions/runs/41567481151)
- **分支**: `mori_epv2_asyncll_tbo`
- **总耗时**: 124.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41567481151

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.8min | 其他 | 日志中所有性能测试均通过，作业本身未见失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125720465135) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 三个性能测试用例均标记 passed=true，作业正常结束并进入清理阶段，日志中无报错或失败信息，失败可能由外部状态或日志截断导致，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125720465135

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125692550009) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125692550039) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693398951) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399022) |
| multimodal-gen-test-4-npu-a3 (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399062) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399096) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399128) |
| base-b-test-16-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399133) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399296) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399312) |
| base-b-test-2-npu-a3 / run (0) | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399338) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125693399388) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125705309095) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125705309122) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125705309148) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41567481151/job/125720465169) |


## [Run #41563694377](https://github.com/sgl-project/sglang/actions/runs/41563694377)
- **分支**: `codex/vlm-strong-identity-1028`
- **总耗时**: 38.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41563694377

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 7.7min | 代码错误 | NPU MLA FIA HiCache 测试脚本执行失败，返回退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867814) |
| base-b-test-16-npu-a3 / run (0) | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867867) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867889) |
| base-b-test-4-npu-a3 / run (1) | 14.8min | 代码错误 | NPU PD分离测试用例 test_npu_pd_disaggregation.py 执行失败，退出码5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867893) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 运行 92.54 秒后以退出码 5 失败，8 个测试全部未通过（0/8 passed），导致作业以退出码 1 结束。退出码 5 通常表示 pytest 未收集到任何测试或测试用例被跳过，需检查该测试文件的用例收集与 NPU 环境配置。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867814



- **base-b-test-4-npu-a3 / run (1)**: base-b-test-4-npu-a3 作业中，test_npu_pd_disaggregation.py 运行约643秒后返回退出码5，2个用例0通过，导致作业以退出码1结束。属测试用例本身失败，非环境或超时问题。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867893

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680145524) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680145569) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867716) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867733) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867757) |
| base-b-test-8-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867811) |
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867826) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563694377/job/125680867933) |


## [Run #41563491502](https://github.com/sgl-project/sglang/actions/runs/41563491502)
- **分支**: `gdn-spec-decode-xpu`
- **总耗时**: 48.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41563491502

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 15.3min | 代码错误 | NPU PD分离测试用例 test_npu_pd_disaggregation.py 执行失败，退出码5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503803) |
| base-b-test-2-npu-a3 / run (0) | 17.8min | 代码错误 | NPU 测试用例 test_npu_tp2_fia_bf16.py 执行失败，退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503815) |
| base-b-test-1-npu-a3 / run (0) | 6.9min | 其他 | NPU采样后端测试进程被杀死（exit code 137），疑似OOM或资源不足 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503851) |

- **base-b-test-4-npu-a3 / run (1)**: 该测试文件运行约632秒后返回退出码5（pytest无测试被收集或全部失败），Test Summary显示0/2通过，导致作业以exit code 1结束。属测试用例本身失败，非环境或超时问题。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503803

- **base-b-test-2-npu-a3 / run (0)**: 在 base-b-test-2-npu-a3 作业中，test/registered/npu/basic_function/runtime_opts/test_npu_tp2_fia_bf16.py 运行 75 秒后以退出码 1 失败，导致整个作业失败；其余测试均通过，属于该用例本身的代码或断言错误。
  - 失败用例: npu_tp2_fia_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503815

- **base-b-test-1-npu-a3 / run (0)**: test_npu_sampling_backend.py 返回 exit code 137（SIGKILL），通常为内存/显存耗尽被系统杀死，非代码断言失败；8个测试仅1个通过，作业以 exit code 1 结束。
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503851

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125679582648) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125679582663) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503626) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503797) |
| multimodal-gen-test-4-npu-a3 (0) | 6.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503830) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503841) |
| base-b-test-4-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563491502/job/125680503867) |


## [Run #41563231013](https://github.com/sgl-project/sglang/actions/runs/41563231013)
- **分支**: `lc-dsv4-l3-upstream`
- **总耗时**: 12.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41563231013

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 8.4min | 其他 | 测试失败但日志中未显示具体错误，仅提示未找到 diffusion-failures 目录，无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561554) |
| multimodal-gen-test-1-npu-a3 (1) | 5.3min | 其他 | 作业未找到 diffusion-failures 目录，产物上传失败，但日志未显示测试本身报错。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561642) |
| multimodal-gen-test-4-npu-a3 (0) | 8.3min | 其他 | 日志中未出现明确的测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561648) |
| multimodal-gen-test-1-npu-a3 (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561699) |
| base-b-test-1-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561745) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 的自定义容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561870) |
| base-b-test-16-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561899) |
| base-b-test-2-npu-a3 / run (0) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561907) |
| base-b-test-4-npu-a3 / run (1) | 8.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679562161) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被省略，未见实际测试报错信息。末尾显示 'No files were found with the provided path: diffusion-failures/'，说明测试失败后未生成失败产物目录，无法定位具体原因，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561554

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示“No files were found with the provided path: diffusion-failures/”，说明测试未生成失败产物目录，可能测试未实际执行或提前退出；日志中无明确测试失败或超时信息，需查看省略的中间日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561642

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，未见具体报错；结尾仅提示未找到 diffusion-failures/ 路径，无产物上传，其余为 Node 弃用警告和清理步骤，无法定位真实失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561648



- **base-b-test-4-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非代码或精度问题；此前模型导入告警均为可忽略项。
  链接: https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561870




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125678665699) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125678665714) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41563231013/job/125679561829) |


## [Run #41561813623](https://github.com/sgl-project/sglang/actions/runs/41561813623)
- **分支**: `followup/qwen35-megakernel-runtime-v3-binding`
- **总耗时**: 27.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41561813623

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 17.6min | 代码错误 | NPU 基础功能测试 test_npu_moe_dense_tp_size.py 执行失败，退出码为 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170984) |

- **base-b-test-2-npu-a3 / run (0)**: 在 base-b-test-2-npu-a3 作业中，test_npu_moe_dense_tp_size.py 运行 158 秒后以退出码 5 失败（pytest 中通常表示未收集到测试或用例异常），导致作业整体退出码为 1。其余两个用例通过，属测试用例本身问题。
  - 失败用例: npu_moe_dense_tp_size.py, npu_moe_dense_tp_size.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170984

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170800) |
| base-b-test-1-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170831) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170976) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754170977) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754171517) |
| multimodal-gen-test-4-npu-a3 (1) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754172097) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754172171) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754172184) |
| multimodal-gen-test-1-npu-a3 (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754172555) |
| base-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754172610) |
| multimodal-gen-test-4-npu-a3 (0) | 24.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41561813623/job/125754172707) |


## [Run #41560652430](https://github.com/sgl-project/sglang/actions/runs/41560652430)
- **分支**: `lsyin/sched-pr12`
- **总耗时**: 57.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41560652430

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125684783142) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 16.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125684783154) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125684783188) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125670847718) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125670847768) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693169) |
| base-b-test-16-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693274) |
| base-b-test-2-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693297) |
| base-b-test-8-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693317) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693342) |
| multimodal-gen-test-4-npu-a3 (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693346) |
| base-b-test-4-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693478) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41560652430/job/125671693553) |


## [Run #41559214453](https://github.com/sgl-project/sglang/actions/runs/41559214453)
- **分支**: `byron/r3-host-rows-output-rank`
- **总耗时**: 26.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41559214453

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 14.8min | 代码错误 | 测试用例 test_npu_moe_dense_tp_size.py 执行失败，退出码为 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525171) |
| base-b-test-4-npu-a3 / run (0) | 8.9min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 5，0/2 用例通过 | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525237) |

- **base-b-test-2-npu-a3 / run (0)**: 在 NPU A3 基础功能测试中，并行策略专家并行目录下的 test_npu_moe_dense_tp_size.py 运行失败，退出码为 5（通常表示 pytest 未收集到测试用例或测试内部错误），导致整个作业以退出码 1 结束。
  - 失败用例: npu_moe_dense_tp_size.py, npu_moe_dense_tp_size.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525171

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Qwen3-32B 服务后运行约 173 秒即返回 exit code 5（pytest 无测试被收集/全部失败），导致 0/2 通过，作业以 exit code 1 结束。需检查该用例的启动参数与断言。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525237

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125665618116) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125665618153) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525072) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525097) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525135) |
| base-b-test-16-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525159) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525173) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41559214453/job/125666525353) |


## [Run #41557681616](https://github.com/sgl-project/sglang/actions/runs/41557681616)
- **分支**: `feature/spark2_5_dspark`
- **总耗时**: 15.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41557681616

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 4.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405091) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405183) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405266) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405329) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405344) |






### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125660607250) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125660607293) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661404900) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405078) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41557681616/job/125661405165) |


## [Run #41554553662](https://github.com/sgl-project/sglang/actions/runs/41554553662)
- **分支**: `cryang/pr/sparsity-pd-disagg-LRU`
- **总耗时**: 41.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41554553662

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.8min | 超时 | NPU DP注意力测试因服务进程被杀死而超时失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331479) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行540秒后退出码137（SIGKILL），服务端连接中断、进程被强制终止，疑似超时或OOM导致，最终0/2通过。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331479

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125650346170) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125650346376) |
| base-b-test-1-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331324) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331349) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331370) |
| multimodal-gen-test-4-npu-a3 (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331393) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331436) |
| base-b-test-16-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331444) |
| base-b-test-4-npu-a3 / run (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41554553662/job/125651331490) |


## [Run #41553611334](https://github.com/sgl-project/sglang/actions/runs/41553611334)
- **分支**: `topk-v2-exact-modes`
- **总耗时**: 52.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41553611334

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.4min | 精度回归 | GLM5 top64 pruned 精度测试用例失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125656859483) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 作业中 2 个精度用例仅 1 个通过；test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 返回 exit code 5（pytest 无用例收集/未通过），耗时 314s，导致作业退出码 1 失败。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125656859483

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125647713677) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125647713760) |
| multimodal-gen-test-1-npu-a3 (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648551762) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648551833) |
| multimodal-gen-test-4-npu-a3 (0) | 32.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648551849) |
| multimodal-gen-test-1-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648551904) |
| base-b-test-1-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648551998) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648552029) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648552030) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648552050) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648552109) |
| base-b-test-16-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125648552152) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125656859169) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553611334/job/125656859279) |


## [Run #41553023950](https://github.com/sgl-project/sglang/actions/runs/41553023950)
- **分支**: `topk-v2-exact-modes`
- **总耗时**: 6.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41553023950

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 2.3min | 其他 | 作业未找到 diffusion-failures 目录，无产物可上传，但日志未显示测试本身失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646197819) |
| multimodal-gen-test-1-npu-a3 (0) | 2.2min | 其他 | 作业日志中未出现实际测试执行或失败信息，仅显示产物上传时未找到 diffusion-failures 目录。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646197889) |
| multimodal-gen-test-4-npu-a3 (1) | 2.3min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646197892) |
| base-b-test-8-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198023) |
| base-b-test-1-npu-a3 / run (0) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198149) |
| base-b-test-2-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198196) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198224) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198232) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198294) |
| multimodal-gen-test-4-npu-a3 (0) | 2.3min | 其他 | 作业未找到 diffusion-failures 目录，无产物可上传，但日志未显示具体测试失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198642) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志仅显示上传产物时提示 'No files were found with the provided path: diffusion-failures/'，说明测试未生成失败产物目录；其余均为 Node.js 弃用警告和 git 清理步骤，缺少实际测试执行与报错信息，无法定位具体失败点。
  链接: https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646197819

- **multimodal-gen-test-1-npu-a3 (0)**: 日志仅包含 runner 初始化、action 下载、Node 弃用警告及清理步骤，未显示测试运行或报错；唯一异常是上传产物时提示未找到 diffusion-failures/ 路径，无文件可上传。失败原因无法从该日志确定，可能为测试未产生预期输出目录或作业被提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646197889

- **multimodal-gen-test-4-npu-a3 (1)**: 作业日志主要为 Node 弃用警告和 git 清理步骤，未包含实际测试执行或报错内容；仅提示 diffusion-failures/ 路径无文件，无法上传 artifact。失败原因需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646197892







- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示上传产物时提示 'No files were found with the provided path: diffusion-failures/'，说明测试未生成失败样本目录，可能测试未实际执行或提前退出；中间省略部分可能包含真正错误，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125646198642

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125645219696) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41553023950/job/125645219794) |


## [Run #41551508199](https://github.com/sgl-project/sglang/actions/runs/41551508199)
- **分支**: `lsyin/indirect-imports`
- **总耗时**: 43.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41551508199

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 16.0min | 代码错误 | NPU MoE runner backend 测试用例执行失败，退出码为 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468952) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_moe_runner_backend.py 运行 149 秒后失败，退出码 5（通常表示 pytest 未收集到测试或测试内部错误），其余 3 个用例均通过，作业因该用例失败以退出码 1 结束。
  - 失败用例: npu_moe_runner_backend.py, npu_moe_runner_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468952

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125642188289) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125642188311) |
| multimodal-gen-test-4-npu-a3 (0) | 33.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468704) |
| multimodal-gen-test-1-npu-a3 (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468723) |
| multimodal-gen-test-1-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468799) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468873) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468875) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468974) |
| base-b-test-4-npu-a3 / run (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643468993) |
| multimodal-gen-test-4-npu-a3 (1) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643469007) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551508199/job/125643469026) |


## [Run #41551374167](https://github.com/sgl-project/sglang/actions/runs/41551374167)
- **分支**: `lsyin/sched-pr11`
- **总耗时**: 9.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41551374167

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | 其他 | 作业未产生 diffusion-failures 目录，上传产物时无文件可传，导致作业失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641804938) |
| multimodal-gen-test-4-npu-a3 (1) | 5.2min | 其他 | 作业日志中未见明确测试失败原因，仅显示未找到 diffusion-failures 目录导致无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805004) |
| base-b-test-1-npu-a3 / run (0) | 6.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805063) |
| base-b-test-8-npu-a3 / run (0) | 6.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805090) |
| base-b-test-16-npu-a3 / run (0) | 6.3min | 环境问题 | 自托管 runner 的自定义容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805107) |
| base-b-test-2-npu-a3 / run (0) | 6.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805198) |
| base-b-test-4-npu-a3 / run (1) | 5.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805206) |
| base-b-test-4-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 执行自定义容器失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805241) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示“No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.”，说明测试未生成预期失败产物目录，upload-artifact 步骤无文件可传而失败；其余仅为 Node 弃用警告，非根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641804938

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被省略，无法定位具体失败点；末尾仅提示未找到 diffusion-failures/ 路径，无 artifact 上传，随后正常清理。需查看完整日志确认失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805004

- **base-b-test-1-npu-a3 / run (0)**: 日志显示推理请求正常返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805063

- **base-b-test-8-npu-a3 / run (0)**: 日志显示推理请求已成功返回（POST /generate 200 OK），随后报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805090

- **base-b-test-16-npu-a3 / run (0)**: 构建 sglang 及 xatlas 过程中，日志报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非代码或测试本身的问题，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805107

- **base-b-test-2-npu-a3 / run (0)**: 模型权重加载到67%时，日志报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员。这属于 runner 容器环境异常，并非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805198

- **base-b-test-4-npu-a3 / run (1)**: 日志显示“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明 k8s runner 无法启动指定的 CANN 容器镜像，属于 runner/容器环境问题，并非测试代码或精度失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805206

- **base-b-test-4-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，即 k8s 自托管 runner 无法启动自定义容器（CANN 镜像），属于 runner/容器环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125641805241

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125640886973) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41551374167/job/125640887045) |


## [Run #41550825027](https://github.com/sgl-project/sglang/actions/runs/41550825027)
- **分支**: `lsyin/indirect-imports`
- **总耗时**: 10.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41550825027

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 5.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639095894) |
| multimodal-gen-test-4-npu-a3 (0) | 2.6min | 其他 | 作业未执行实际测试，仅完成环境准备后即结束，未发现测试失败信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639095914) |
| multimodal-gen-test-1-npu-a3 (1) | 1.6min | 超时 | 作业在下载 action 阶段被取消，疑似超时或基础设施中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639095934) |
| multimodal-gen-test-4-npu-a3 (1) | 2.7min | 环境问题 | 日志中未见实际测试执行，作业在准备阶段结束，疑似运行环境或调度异常。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096041) |
| base-b-test-1-npu-a3 / run (0) | 2.7min | 其他 | 日志在 checkout 后执行 k8s 脚本时中断，未显示具体失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096136) |
| base-b-test-16-npu-a3 / run (0) | 2.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096204) |
| base-b-test-4-npu-a3 / run (0) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096243) |
| base-b-test-2-npu-a3 / run (0) | 2.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096272) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装后中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096309) |
| base-b-test-8-npu-a3 / run (0) | 2.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096551) |


- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示 runner 初始化、下载 action、git 配置和清理步骤，中间省略部分可能包含测试执行，但可见部分无测试失败或报错；仅提示 diffusion-failures/ 目录无文件可上传，属正常告警。建议查看省略的中间日志确认测试是否真正运行。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639095914

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示下载 actions/checkout 和 upload-artifact 后出现 'A task was canceled'，未进入实际测试步骤，属于 runner 侧任务取消/超时，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639095934

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅显示 runner 启动、下载 action、checkout 代码及 k8s 脚本调用，随后出现清理孤儿进程并结束，未进入多模态测试步骤，也无报错堆栈，判断为环境/调度侧提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096041

- **base-b-test-1-npu-a3 / run (0)**: 日志仅显示 checkout 完成并开始运行 /home/runner/k8s/index.js，随后出现 Node.js 弃用警告和清理孤儿进程，缺少实际测试输出与错误信息，无法定位具体失败点，需查看完整日志或后续步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096136

- **base-b-test-16-npu-a3 / run (0)**: 日志显示在安装 torch-npu 过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或测试本身的问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096204

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 pip 安装依赖正常完成后，报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境问题，需联系 runner 管理员排查，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096243


- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 安装 memcache-hybrid 成功后立即报错“Executing the custom container implementation failed”，属于 runner 容器执行环境异常，非代码或测试本身问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125639096309


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125637852772) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41550825027/job/125637852778) |


## [Run #41545073885](https://github.com/sgl-project/sglang/actions/runs/41545073885)
- **分支**: `gfx1151-quark-w4a16-kernels`
- **总耗时**: 27.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41545073885

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 21.0min | 代码错误 | 测试用例 test_npu_return_indexer_topk_deepseek_v4.py 执行失败，导致作业退出码为1。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600563) |

- **base-b-test-2-npu-a3 / run (0)**: TIMINGS 显示 test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py 的 passed 为 false（耗时73秒），其余用例均通过；该用例失败使进程以 exit code 1 结束，属于测试代码或被测功能错误，而非环境或超时问题。
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600563

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125618750707) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125618750732) |
| multimodal-gen-test-4-npu-a3 (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600422) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600444) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600480) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600511) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600556) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600580) |
| base-b-test-16-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41545073885/job/125619600630) |


## [Run #41544600168](https://github.com/sgl-project/sglang/actions/runs/41544600168)
- **分支**: `foundry-dep`
- **总耗时**: 37.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41544600168

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 16.3min | 代码错误 | NPU PD 分离测试脚本执行失败，返回退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246128) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | 超时 | NPU DP attention 测试因服务进程被 SIGKILL（exit 137）而失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246216) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行约 643 秒后以退出码 5 失败，2 个用例 0 通过，导致作业以退出码 1 结束；退出码 5 通常表示 pytest 未收集到任何测试或测试内部异常，需检查该用例的启动参数与日志。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246128

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行约245秒后，server 进程 rc=-9（exit 137，疑似 OOM 或被杀），fixture 触发 fail-fast，0/2 通过，作业以 exit code 1 结束。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246216

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125617228372) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125617228629) |
| multimodal-gen-test-1-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618245965) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246099) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246112) |
| multimodal-gen-test-4-npu-a3 (0) | 32.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246168) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246214) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246238) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246266) |
| base-b-test-16-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41544600168/job/125618246281) |


## [Run #41542989716](https://github.com/sgl-project/sglang/actions/runs/41542989716)
- **分支**: `lsyin/indirect-imports`
- **总耗时**: 37.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41542989716

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 15.0min | 代码错误 | NPU PD分离测试用例执行失败，退出码5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269211) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行631秒后返回退出码5（pytest无测试收集或全部失败），2个用例0通过，导致作业失败。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269211

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125614925660) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125614925744) |
| multimodal-gen-test-4-npu-a3 (1) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617268829) |
| multimodal-gen-test-1-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617268839) |
| multimodal-gen-test-1-npu-a3 (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617268884) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617268975) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269147) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269164) |
| base-b-test-2-npu-a3 / run (0) | 27.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269218) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269279) |
| base-b-test-16-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41542989716/job/125617269302) |


## [Run #41541182001](https://github.com/sgl-project/sglang/actions/runs/41541182001)
- **分支**: `codex/dp-lora-routing-sync`
- **总耗时**: 30.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41541182001

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.1min | 代码错误 | NPU基础功能测试用例 test_npu_basic_sanity_eagle3.py 执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860431) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 speculative_inference/test_npu_basic_sanity_eagle3.py 的 passed 为 false，耗时 86 秒，导致进程以退出码 1 结束；其余用例均通过，属于该测试用例本身的代码或断言失败。
  - 失败用例: npu_basic_sanity_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860431

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125605651969) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125605652048) |
| multimodal-gen-test-4-npu-a3 (0) | 6.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860172) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860342) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860384) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860505) |
| base-b-test-4-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860556) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860559) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41541182001/job/125606860666) |


## [Run #41537658781](https://github.com/sgl-project/sglang/actions/runs/41537658781)
- **分支**: `perf/ltx23-alias-free-gap`
- **总耗时**: 47.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41537658781

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 21.9min | 精度回归 | GLM5 top64 pruned 精度测试脚本以退出码5失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125604912192) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 作业中 2 个精度测试仅 1 个通过；test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 返回 exit code 5（pytest 无测试收集/用例未执行），耗时 383s，导致作业退出码 1。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125604912192

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125593714025) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125593714085) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893411) |
| multimodal-gen-test-1-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893459) |
| multimodal-gen-test-4-npu-a3 (0) | 28.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893564) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893607) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893637) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893705) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893719) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893739) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893747) |
| base-b-test-16-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125594893816) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125604912229) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537658781/job/125604912442) |


## [Run #41537572081](https://github.com/sgl-project/sglang/actions/runs/41537572081)
- **分支**: `lsyin/sched-pr10`
- **总耗时**: 26.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41537572081

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 11.0min | 代码错误 | NPU EPLB 最小重平衡利用率阈值测试用例执行失败，退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087660) |
| base-b-test-2-npu-a3 / run (0) | 3.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087838) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087865) |

- **base-b-test-8-npu-a3 / run (0)**: test_npu_eplb_min_rebalancing_utilization_threshold.py 运行 332 秒后返回退出码 1，测试汇总为 0/1 通过，导致作业失败；日志未显示具体断言或异常信息，需查看该用例详细输出以定位问题。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087660



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125593847211) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125593847369) |
| multimodal-gen-test-4-npu-a3 (1) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087432) |
| base-b-test-16-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087609) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087622) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087727) |
| base-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41537572081/job/125595087777) |


## [Run #41534708310](https://github.com/sgl-project/sglang/actions/runs/41534708310)
- **分支**: `fix/dcp-disable-unused-quickallreduce`
- **总耗时**: 53.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41534708310

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 20.3min | 精度回归 | GLM5 top64 pruned 精度测试用例失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125599319442) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: base-c-test-acc-16-npu-a3 作业中 2 个精度用例仅 1 个通过；test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py 返回 exit code 5（pytest 无用例收集/未通过），耗时 383s，导致作业退出码 1 失败。
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125599319442

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125583748221) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125583748384) |
| multimodal-gen-test-1-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008546) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008660) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008769) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008801) |
| base-b-test-1-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008865) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008872) |
| base-b-test-2-npu-a3 / run (0) | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008943) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585008994) |
| base-b-test-16-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585009001) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125585009061) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125599319292) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41534708310/job/125599319479) |


## [Run #41527221106](https://github.com/sgl-project/sglang/actions/runs/41527221106)
- **分支**: `lsyin/import-bootstrap`
- **总耗时**: 36.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41527221106

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 26.3min | 其他 | 作业未找到 diffusion-failures 目录，无产物上传，但日志未显示具体测试失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353504) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353657) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | 其他 | 日志中所有测试均通过，作业本身未见失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353943) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示上传产物时未找到 diffusion-failures/ 路径，无 artifacts 上传；中间省略部分可能含真实失败信息，但可见日志中无明确报错，无法定位具体失败原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353504

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型加载和 Tokenizer 初始化正常，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境故障，并非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353657

- **base-b-test-1-npu-a3 / run (0)**: 日志显示各测试文件 passed 均为 true，TIMINGS END 正常输出，随后进入 Post job cleanup，无报错或失败步骤。失败可能由日志省略部分或作业级状态判定导致，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353943

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125558856175) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125559531668) |
| Recommend tests from coverage | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125559531751) |
| multimodal-gen-test-1-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353433) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353574) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353623) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353681) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353866) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561353979) |
| base-b-test-16-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41527221106/job/125561354001) |


## [Run #41526614181](https://github.com/sgl-project/sglang/actions/runs/41526614181)
- **分支**: `lsyin/import-bootstrap`
- **总耗时**: 5.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41526614181

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-a-test-npu | 1.6min | 超时 | 作业在运行第3个测试文件时被外部取消，并非测试失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41526614181/job/125557392669) |
| Recommend tests from coverage | 2.6min | 其他 | 日志中未见失败步骤，作业实际成功完成 | [job link](https://github.com/sgl-project/sglang/actions/runs/41526614181/job/125557392741) |

- **base-a-test-npu**: 前两个测试文件均通过（19 passed），执行到 graph_runner/test_npu_cudagraph_backend.py 时日志出现 'The operation was canceled'，随后清理并终止 python3 进程，属于作业被取消/超时，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41526614181/job/125557392669

- **Recommend tests from coverage**: 日志显示产物上传成功、输出变量已设置、清理正常，仅有 Node.js 20 弃用警告，无报错信息，失败原因无法从所给日志判断，可能为后续步骤或外部状态导致。
  链接: https://github.com/sgl-project/sglang/actions/runs/41526614181/job/125557392741


## [Run #41525795413](https://github.com/sgl-project/sglang/actions/runs/41525795413)
- **分支**: `fix/retract-keeps-new-token-ratio`
- **总耗时**: 46.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41525795413

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399632) |
| base-b-test-2-npu-a3 / run (0) | 5.8min | 代码错误 | NPU MLA FIA HiCache 测试脚本执行失败，退出码 5 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399665) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399691) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399793) |


- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 运行 110 秒后返回退出码 5，8 个测试全部未通过（0/8 passed），导致作业以退出码 1 结束。退出码 5 通常表示 pytest 未收集到任何测试或测试内部异常，需检查该用例的模型加载与 MLA/HiCache 配置。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399665



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125695460341) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125695460407) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399515) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399559) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399673) |
| base-b-test-16-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525795413/job/125696399810) |


## [Run #41525301036](https://github.com/sgl-project/sglang/actions/runs/41525301036)
- **分支**: `lsyin/import-bootstrap`
- **总耗时**: 10.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41525301036

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 4.7min | 其他 | 测试失败后未生成 diffusion-failures 目录，导致产物上传步骤找不到文件。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586289) |
| multimodal-gen-test-1-npu-a3 (1) | 4.0min | 其他 | 作业未找到 diffusion-failures 目录，导致产物上传失败，但日志中未见实际测试失败原因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586293) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | 其他 | 作业失败但日志中未见明确错误，仅显示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586331) |
| multimodal-gen-test-4-npu-a3 (1) | 4.2min | 其他 | 多模态生成测试未产生 diffusion-failures 目录，上传产物时无文件可传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586438) |
| base-b-test-4-npu-a3 / run (1) | 4.9min | 环境问题 | 自托管 runner 执行自定义容器失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586517) |
| base-b-test-2-npu-a3 / run (0) | 4.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586531) |
| base-b-test-16-npu-a3 / run (0) | 4.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586560) |
| base-b-test-8-npu-a3 / run (0) | 4.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试后异常终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586616) |
| base-b-test-1-npu-a3 / run (0) | 4.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586631) |
| base-b-test-4-npu-a3 / run (0) | 4.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586744) |
| pr-test-npu-finish | 0.9min | 其他 | 汇总作业检测到依赖的 NPU 测试作业被取消，因此主动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125556522347) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示“No files were found with the provided path: diffusion-failures/”，说明多模态生成测试未产出失败样本目录，作业因此失败；日志中未见具体测试报错，需查看被省略的中间日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586289

- **multimodal-gen-test-1-npu-a3 (1)**: 日志仅显示“No files were found with the provided path: diffusion-failures/”，说明测试未生成失败产物目录，可能测试未执行或提前退出；其余均为 Node.js 弃用警告，无明确报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586293

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产出失败样本目录，或测试本身未运行/提前退出，具体失败原因需查看省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586331

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示测试阶段未生成 diffusion-failures/ 目录，upload-artifact 报“No files were found”，说明测试用例未按预期产出失败样本或测试提前退出，需检查测试脚本执行与输出路径。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586438

- **base-b-test-4-npu-a3 / run (1)**: 日志显示自定义容器实现执行失败（Executing the custom container implementation failed），提示联系自托管 runner 管理员。CANN 自定义算子安装已成功，失败发生在容器启动/执行阶段，属 runner 环境或容器配置问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586517


- **base-b-test-16-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明 runner 的容器实现异常，并非测试代码或精度问题；测试刚开始即报错退出，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586560

- **base-b-test-8-npu-a3 / run (0)**: 日志显示测试脚本已开始执行，但随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非测试代码本身失败，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125553586616



- **pr-test-npu-finish**: pr-test-npu-finish 脚本遍历 needs 结果，发现 base-b-test-1-npu-a3 等多个作业状态为 cancelled，按逻辑执行 exit 1 导致作业失败；根因是上游测试作业被取消，而非本作业代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125556522347

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125551659453) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41525301036/job/125551659463) |


## [Run #41524437131](https://github.com/sgl-project/sglang/actions/runs/41524437131)
- **分支**: `lsyin/sched-pr09`
- **总耗时**: 20.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41524437131

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | 其他 | 多模态生成测试失败，且未生成失败产物目录 | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142407) |
| base-b-test-16-npu-a3 / run (0) | 8.9min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142679) |
| base-b-test-4-npu-a3 / run (0) | 12.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142708) |
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142858) |
| base-b-test-1-npu-a3 / run (0) | 6.8min | 环境问题 | 自托管 runner 执行自定义容器失败，服务启动后作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142942) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550143080) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示测试作业运行约11分钟后结束，上传产物时提示未找到 diffusion-failures/ 目录，说明测试用例失败但未产生预期失败产物；日志中未见具体报错堆栈，需查看被省略的中间日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142407

- **base-b-test-16-npu-a3 / run (0)**: 日志显示各 TP/EP 进程已启动并读取环境变量，随后报错“Executing the custom container implementation failed”，属于 runner 容器运行时/基础设施故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142679

- **base-b-test-4-npu-a3 / run (0)**: 日志显示推理任务正常运行中（prefill 吞吐正常），随后报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142708

- **base-b-test-2-npu-a3 / run (0)**: 前序测试均通过，在开始第2个测试文件时出现“Executing the custom container implementation failed”，属于 runner 容器环境异常，非测试代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142858

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器执行环境异常，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142942

- **base-b-test-4-npu-a3 / run (1)**: 模型权重加载到45%时，日志报错“Executing the custom container implementation failed”，随后作业进入清理阶段。该错误来自自托管 runner 的容器运行时，并非模型或测试代码本身的问题，需要联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550143080

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125548722422) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125548723064) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142447) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41524437131/job/125550142949) |


## [Run #41521451036](https://github.com/sgl-project/sglang/actions/runs/41521451036)
- **分支**: `dspark-vocab-verify-guards`
- **总耗时**: 16.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41521451036

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 4.3min | 代码错误 | NPU 测试 test_dspark_npu_dispatch.py 断言失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41521451036/job/125540085615) |

- **base-b-test-1-npu-a3 / run (0)**: 该测试文件运行 2 个用例，其中 1 个失败（FAILED failures=1），导致进程退出码 1，作业失败。属于测试断言/代码逻辑问题，非环境或超时。
  - 失败用例: dspark_npu_dispatch.py, dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41521451036/job/125540085615

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521451036/job/125538525056) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521451036/job/125538525128) |


## [Run #41521441760](https://github.com/sgl-project/sglang/actions/runs/41521441760)
- **分支**: `kurt/allocate-intermediate-ssm`
- **总耗时**: 41.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41521441760

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 10.2min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539531586) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125538461617) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125538461622) |
| multimodal-gen-test-1-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539527929) |
| multimodal-gen-test-1-npu-a3 (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539528004) |
| multimodal-gen-test-4-npu-a3 (0) | 37.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539528154) |
| multimodal-gen-test-4-npu-a3 (1) | 25.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539528360) |
| base-b-test-2-npu-a3 / run (0) | 26.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539529600) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539530004) |
| base-b-test-16-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539530148) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539530257) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41521441760/job/125539530380) |


## [Run #41504870199](https://github.com/sgl-project/sglang/actions/runs/41504870199)
- **分支**: `pd-prefill-release-mm-features`
- **总耗时**: 15.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41504870199

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.2min | 代码错误 | NPU DP attention 测试用例执行失败，退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125483563864) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Moonlight-16B-A3B-Instruct 服务后运行失败，耗时 373 秒，退出码为 1，测试汇总为 0/1 通过；日志未给出具体报错堆栈，需查看该用例详细输出以定位问题。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125483563864

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125481914916) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125481914966) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125483563223) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125483563256) |
| base-b-test-4-npu-a3 / run (1) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41504870199/job/125483563263) |


## [Run #41501755031](https://github.com/sgl-project/sglang/actions/runs/41501755031)
- **分支**: `topk-v2-exact-modes`
- **总耗时**: 8.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41501755031

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 3.4min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399152) |
| multimodal-gen-test-1-npu-a3 (1) | 3.2min | 其他 | 作业未产生 diffusion-failures 目录，上传产物时无文件可传，导致作业失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399237) |
| multimodal-gen-test-4-npu-a3 (0) | 3.4min | 其他 | 作业未发现失败错误，仅上传产物时未找到 diffusion-failures 目录文件 | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399310) |
| multimodal-gen-test-4-npu-a3 (1) | 3.0min | 其他 | 日志中未出现测试失败信息，仅显示未找到 diffusion-failures 目录导致无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399334) |
| base-b-test-2-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472400247) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472400279) |
| base-b-test-16-npu-a3 / run (0) | 2.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472400329) |
| base-b-test-8-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472400377) |
| base-b-test-4-npu-a3 / run (1) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472400390) |
| base-b-test-4-npu-a3 / run (0) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472400411) |

- **multimodal-gen-test-1-npu-a3 (0)**: 作业日志主要为 Node.js 弃用警告和清理步骤，未包含实际测试执行或报错内容；唯一异常是 'No files were found with the provided path: diffusion-failures/'，说明预期产物目录不存在，但不足以判定测试失败原因，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399152

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示“No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.”，说明测试未生成预期的失败样本目录，可能是测试未执行或未产生输出，属于测试产物缺失问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399237

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中无测试失败或异常退出，唯一异常是 upload-artifact 提示未找到 diffusion-failures/ 路径下文件，导致无产物上传；其余均为 Node.js 弃用警告和清理步骤，作业本身未报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399310

- **multimodal-gen-test-4-npu-a3 (1)**: 作业日志主要为 Node 弃用警告和 git 清理步骤，未包含实际测试执行或报错内容；唯一异常是 'No files were found with the provided path: diffusion-failures/'，说明预期失败产物目录不存在，无法判定具体失败原因，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125472399334







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125470965081) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41501755031/job/125470965275) |


## [Run #41494594784](https://github.com/sgl-project/sglang/actions/runs/41494594784)
- **分支**: `jsheng/score-embedding-features`
- **总耗时**: 53.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41494594784

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125471639640) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125471639708) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | 其他 | 测试套件未找到任何用例，脚本对空结果做整数比较报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125471639947) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试脚本已开始执行，但随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非测试用例本身的精度或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125471639640

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 模型分片加载完成后，日志报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员。该错误发生在容器执行阶段，与测试代码或精度无关，属于 runner/容器环境故障。
  链接: https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125471639708

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 hw=NPU、suite=base-c-test-acc-2-npu-a3 未找到测试（0/0），属增量迁移预期跳过；随后 shell 第223行对空值/非整数做 [ ] 比较，报 integer expression expected，导致作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125471639947

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125446399264) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125446399291) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782376) |
| multimodal-gen-test-1-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782432) |
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782461) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782486) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782608) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782683) |
| base-b-test-16-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782778) |
| base-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447782865) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447783163) |
| base-b-test-2-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41494594784/job/125447783801) |


## [Run #41484593681](https://github.com/sgl-project/sglang/actions/runs/41484593681)
- **分支**: `perf/ltx23-alias-free-gap`
- **总耗时**: 82.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41484593681

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125445053505) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125413280882) |
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125413281082) |
| multimodal-gen-test-4-npu-a3 (0) | 36.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613706) |
| multimodal-gen-test-4-npu-a3 (1) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613756) |
| base-b-test-4-npu-a3 / run (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613847) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613893) |
| base-b-test-8-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613929) |
| multimodal-gen-test-1-npu-a3 (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613966) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414613986) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414614002) |
| base-b-test-4-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414614402) |
| multimodal-gen-test-1-npu-a3 (1) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125414614451) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125445053595) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41484593681/job/125445053723) |


## [Run #41483261916](https://github.com/sgl-project/sglang/actions/runs/41483261916)
- **分支**: `dp-attn-phase-lockstep`
- **总耗时**: 10.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41483261916

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 2.4min | 其他 | 作业未找到 diffusion-failures/ 目录，无产物可上传，但日志未显示具体测试失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532603) |
| multimodal-gen-test-4-npu-a3 (1) | 1.9min | 其他 | 日志中未出现实际测试执行或失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532638) |
| multimodal-gen-test-4-npu-a3 (0) | 3.9min | 其他 | 作业未找到 diffusion-failures 目录，无产物上传，但日志未显示具体测试失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532696) |
| base-b-test-2-npu-a3 / run (0) | 2.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532728) |
| multimodal-gen-test-1-npu-a3 (1) | 2.4min | 其他 | 作业未找到 diffusion-failures 目录，无产物上传，但日志未显示具体测试失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532884) |
| base-b-test-1-npu-a3 / run (0) | 2.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532901) |
| base-b-test-4-npu-a3 / run (0) | 2.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532948) |
| base-b-test-8-npu-a3 / run (0) | 2.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409533100) |
| base-b-test-4-npu-a3 / run (1) | 2.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409533226) |
| base-b-test-16-npu-a3 / run (0) | 2.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409533342) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志仅显示上传产物时提示未找到 diffusion-failures/ 路径，无 artifacts 上传；中间省略部分可能包含实际测试失败信息，但可见日志中无明确报错，无法定位具体失败原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532603

- **multimodal-gen-test-4-npu-a3 (1)**: 日志主要为 runner 初始化、action 下载和 Node.js 弃用警告；唯一异常是“No files were found with the provided path: diffusion-failures/”，说明测试可能未运行或未生成失败产物，缺少明确失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532638

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示上传产物时未找到 diffusion-failures/ 路径，无 artifacts 上传；中间省略部分可能包含实际失败信息，但可见日志中无明确报错，无法定位具体失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532696


- **multimodal-gen-test-1-npu-a3 (1)**: 日志仅显示上传产物时未找到 diffusion-failures/ 路径，无 artifacts 上传；中间省略部分可能包含实际测试失败信息，但可见日志中无明确错误，无法判定为性能/精度/代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125409532884






### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125407959412) |
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261916/job/125407959459) |


## [Run #41483261313](https://github.com/sgl-project/sglang/actions/runs/41483261313)
- **分支**: `c/cutedsl-mla-draft-extend`
- **总耗时**: 10.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41483261313

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 3.5min | 其他 | 日志中未出现明确的测试失败信息，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409747633) |
| multimodal-gen-test-4-npu-a3 (1) | 3.3min | 其他 | 作业未找到 diffusion-failures 目录，无产物可上传，但日志未显示具体测试失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409747924) |
| base-b-test-16-npu-a3 / run (0) | 1.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409752875) |
| base-b-test-1-npu-a3 / run (0) | 4.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409752917) |
| base-b-test-2-npu-a3 / run (0) | 4.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409752992) |
| base-b-test-4-npu-a3 / run (0) | 4.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409753016) |
| base-b-test-4-npu-a3 / run (1) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业在环境准备阶段中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409753041) |
| base-b-test-8-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409753075) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或未执行到该步骤，缺少关键报错信息，无法定位具体失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409747633

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅显示上传产物时未找到 diffusion-failures/ 路径，说明测试可能未生成失败产物或提前退出；中间省略部分可能含真实错误，需查看完整日志确认测试是否实际执行及失败点。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409747924

- **base-b-test-16-npu-a3 / run (0)**: 日志显示在解包 apt 依赖包过程中报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，属于 runner/容器环境故障，而非代码或测试本身问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409752875




- **base-b-test-4-npu-a3 / run (1)**: 日志显示 apt 下载依赖过程中报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器运行时故障，非代码或测试本身问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409753041

- **base-b-test-8-npu-a3 / run (0)**: 日志显示在容器内安装 libpython3.10-stdlib 时出现 find: '/usr/lib/python3': No such file or directory，随后报错“Executing the custom container implementation failed”，属于 runner/容器环境异常，非代码或测试本身问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125409753075

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125408074825) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41483261313/job/125408075075) |


## [Run #41481113005](https://github.com/sgl-project/sglang/actions/runs/41481113005)
- **分支**: `dp-attn-phase-lockstep`
- **总耗时**: 14.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41481113005

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 9.6min | 其他 | 作业失败但日志中未显示具体错误，仅见产物目录缺失警告 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401395547) |
| multimodal-gen-test-1-npu-a3 (0) | 9.7min | 其他 | 日志中未见明确报错，仅显示未找到 diffusion-failures 目录导致无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401395664) |
| multimodal-gen-test-4-npu-a3 (0) | 9.8min | 其他 | 日志中未显示具体测试失败原因，仅提示未找到 diffusion-failures 目录，无产物上传。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401395836) |
| multimodal-gen-test-4-npu-a3 (1) | 9.4min | 其他 | 日志中未发现明确的测试失败原因，仅显示产物目录为空。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396063) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | 其他 | 日志显示测试全部通过，作业本身无失败原因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396100) |
| base-b-test-1-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396110) |
| base-b-test-16-npu-a3 / run (0) | 9.7min | 超时 | TokenizerManager 看门狗超时，导致自定义容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396125) |
| base-b-test-2-npu-a3 / run (0) | 9.6min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396136) |
| base-b-test-4-npu-a3 / run (1) | 8.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396240) |
| base-b-test-4-npu-a3 / run (0) | 7.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396463) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾仅显示未找到 diffusion-failures/ 目录、无产物上传，以及 Node.js 弃用警告，未包含实际测试失败的错误信息，无法定位根因，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401395547

- **multimodal-gen-test-1-npu-a3 (0)**: 作业日志被截断，中间省略部分可能包含真正失败原因。可见信息仅有：上传产物时提示未找到 diffusion-failures/ 路径，无 artifacts 上传；其余均为 Node.js 弃用警告和清理步骤，无法定位具体失败点，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401395664

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，可见部分只有 Node 弃用警告和“No files were found with the provided path: diffusion-failures/”，说明测试可能未产生失败产物或提前退出，无法定位具体失败点，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401395836

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾显示未找到 diffusion-failures/ 路径下的文件，无产物上传；中间省略部分可能包含真正失败原因，但可见日志中无报错信息，无法定位具体失败点。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396063

- **base-b-test-8-npu-a3 / run (0)**: 日志中测试摘要为 1/1 passed，目标用例 PASSED，耗时 239 秒，随后正常执行清理。仅存在 Node.js 弃用警告，不影响结果。失败可能由日志未覆盖的后续步骤或外部状态导致，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396100

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务启动后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非测试代码或模型本身的问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396110

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TokenizerManager watchdog timeout（watchdog_timeout=300，soft=True），随后报错“Executing the custom container implementation failed”，作业在约9分钟后终止，属于服务卡死或响应超时，而非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396125

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务初始化正常后报错“Executing the custom container implementation failed”，属于 runner 容器环境问题，需联系自托管 runner 管理员排查，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396136

- **base-b-test-4-npu-a3 / run (1)**: 前序测试均通过（Ran 2 tests OK），在开始运行 test_npu_speculative_multi_npu.py 后约16秒报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非测试代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396240

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner 容器环境问题，并非测试代码或精度失败；NPU 算子回退仅为警告。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125401396463

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125399738722) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41481113005/job/125399738823) |


## [Run #41481110584](https://github.com/sgl-project/sglang/actions/runs/41481110584)
- **分支**: `c/dspark-prepare-tracking-once`
- **总耗时**: 13.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41481110584

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41481110584/job/125401426026) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示在安装依赖过程中报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41481110584/job/125401426026

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41481110584/job/125399714532) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41481110584/job/125399715862) |


## [Run #41410159938](https://github.com/sgl-project/sglang/actions/runs/41410159938)
- **分支**: `fix/top-k-top-p-filtering`
- **总耗时**: 84.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41410159938

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125606216290) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575666383) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575667669) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575668146) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575668669) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575668851) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575668924) |
| base-b-test-16-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575669132) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575669281) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575669327) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125575669842) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125589634003) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125589634197) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125589634261) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41410159938/job/125606216268) |


---
*Auto-generated by ci_monitor.py*