# NPU CI 执行监控（2026-11-13）
**生成时间**: 2026-11-14 07:13
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-13 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 114

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1188 个 | 失败 139 个 | 成功 Job 平均耗时 15.6min
- **Run 执行情况**: 成功 65 个 | 失败 49 个 | 成功 Run 平均耗时 80.5min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-4-npu-a3 / run (0) | 63.8min | #43423972912 | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796783) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 62.8min | #43373746618 | [job link](https://github.com/sgl-project/sglang/actions/runs/43373746618/job/131765569195) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 62.5min | #43385354670 | [job link](https://github.com/sgl-project/sglang/actions/runs/43385354670/job/131763442797) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 60.2min | #43222264231 | [job link](https://github.com/sgl-project/sglang/actions/runs/43222264231/job/131265961110) |
| base-b-test-1-npu-a3 / run (0) | 55.5min | #43423972912 | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796755) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 48.6min | #43343022135 | [job link](https://github.com/sgl-project/sglang/actions/runs/43343022135/job/131627857368) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 44.4min | #43405454992 | [job link](https://github.com/sgl-project/sglang/actions/runs/43405454992/job/131830191865) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 43.9min | #43385466479 | [job link](https://github.com/sgl-project/sglang/actions/runs/43385466479/job/131763429931) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 41.2min | #43381296224 | [job link](https://github.com/sgl-project/sglang/actions/runs/43381296224/job/131749259911) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.7min | #43353972591 | [job link](https://github.com/sgl-project/sglang/actions/runs/43353972591/job/131660851887) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-1-npu-a3 / run (0) | 96.9min | #43416174523 | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052220) |
| base-b-test-16-npu-a3 / run (0) | 31.1min | #43379546878 | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759904) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | #43303906520 | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483506931) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 30.8min | #43309559279 | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669213712) |
| multimodal-gen-test-4-npu-a3 (0) | 30.8min | #43258629091 | [job link](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775765) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.8min | #43357476873 | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131684421136) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.9min | #43327941220 | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131579549597) |
| base-b-test-4-npu-a3 / run (0) | 28.6min | #43408723868 | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629346) |
| multimodal-gen-test-4-npu-a3 (0) | 28.5min | #43442379604 | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424891) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.2min | #43395838536 | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799370065) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-2-npu-a3 / run (0) | 93 | 66 | 16 | 3 | 8 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720022)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796953)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045116)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173888)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942167) |
| base-b-test-4-npu-a3 / run (0) | 95 | 74 | 10 | 5 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012518)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064546)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629346)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942771)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927444) |
| base-b-test-1-npu-a3 / run (0) | 90 | 69 | 9 | 4 | 8 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173946)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052220)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629331)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849705)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759805) |
| base-b-test-16-npu-a3 / run (0) | 87 | 69 | 5 | 5 | 8 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173545)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055805)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333144)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083800)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759904) |
| base-b-test-4-npu-a3 / run (1) | 95 | 83 | 4 | 2 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830229)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842460)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540827894)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131529975432) |
| base-b-test-8-npu-a3 / run (0) | 88 | 81 | 1 | 4 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720351) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 52 | 47 | 4 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131787422832)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131684421136)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131574972898)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669213712) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 56 | 51 | 2 | 0 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799370065)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131320022689) |
| multimodal-gen-test-4-npu-a3 (0) | 91 | 81 | 1 | 0 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775765) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 102 | 98 | 1 | 0 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131779781468) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_dp_attention.py` | 30 | 26 | 4 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064546)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333073)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759843) |
| `npu_mla_fia_hicache_bf16.py` | 32 | 28 | 4 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796953)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333134)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759774) |
| `npu_return_indexer_topk_deepseek_v4.py` | 25 | 22 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953200)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098042)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842442) |
| `npu_device_barrier.py` | 3 | 0 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173888)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849654)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131731181173) |
| `npu_memory_occupation.py` | 3 | 0 | 3 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173946)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849705)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131731181253) |
| `npu_eagle3.py` | 28 | 26 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052220)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842980) |
| `npu_speculative_moe_a2a_backend.py` | 30 | 28 | 2 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333144)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759904) |
| `npu_pd_disaggregation.py` | 36 | 34 | 2 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830229)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540827894) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 8 | 6 | 2 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799370065)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131320022689) |
| `npu_dsv4_hicache_l2_pool.py` | 3 | 1 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759805)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555127) |
| `npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py` | 2 | 0 | 2 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131787422832)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131574972898) |
| `npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py` | 2 | 0 | 2 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131684421136)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669213712) |
| `minimax_h3_t2va_2npu` | 24 | 23 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775765) |
| `npu_sampling_backend.py` | 29 | 28 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201282) |
| `npu_w4a4_quantization.py` | 26 | 25 | 1 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942771) |
| `npu_speculative_multi_npu.py` | 34 | 33 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842460) |
| `npu_expert_distribution_recorder_mode.py` | 28 | 27 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201245) |
| `npu_moe_dense_tp_size.py` | 27 | 26 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942167) |
| `npu_moe_runner_backend.py` | 26 | 25 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390608802) |
| `npu_return_indexer_topk_glm52.py` | 22 | 21 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045116) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43386176541<br>[#44576 [Fix] disaggregation: Release multimodal features when PD prefill finishes a request](https://github.com/sgl-project/sglang/pull/44576) | `pd-prefill-release-mm-features` | 102.5min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43386176541) |
| #43416174523<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 101.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43416174523) |
| #43432772826<br>[#41677 [Perf] [AMD] qwen3_5: enable GDN fused decode projection+Conv1D on HIP](https://github.com/sgl-project/sglang/pull/41677) | `rocm-gdn-fused-decode-proj-conv` | 95.2min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43432772826) |
| #43368610640<br>[#44237 [Fix] embedding: Do not reuse prefixes or split prefills for encoder models](https://github.com/sgl-project/sglang/pull/44237) | `fix/encoder-embedding-prefix-reuse` | 93.2min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43368610640) |
| #43357476873<br>[#48950 [Fix] mem_cache: Hybrid SWA HiCache fixes and --hicache-swa-host-ratio](https://github.com/sgl-project/sglang/pull/48950) | `hicache-hybrid-swa-fixes` | 92.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43357476873) |
| #43322304564<br>[#44823 [Fix] scheduler: Park a chunked prefill continuation when its chunk or KV budget is spent](https://github.com/sgl-project/sglang/pull/44823) | `erik/prefill-chunk-fit-free-pool` | 76.9min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43322304564) |
| #43388545447<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 74.4min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43388545447) |
| #43423972912<br>[#49913 [Feat] kimi_k3: Serve Kimi-K3.1 on the unified memory pool](https://github.com/sgl-project/sglang/pull/49913) | `main` | 67.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43423972912) |
| #43327941220<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 60.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43327941220) |
| #43395838536<br>[#33815 [Feat] [Intel] diffusion: Add rotary embedding kernel for CPU](https://github.com/sgl-project/sglang/pull/33815) | `sgl-diffusion-rope` | 57.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43395838536) |
| #43397442061<br>[#47221 [Perf] dsa: Elide shared-layer index-K under HiSparse decode to raise batch size](https://github.com/sgl-project/sglang/pull/47221) | `feature/dsa-index-k-elision-hisparse-decode` | 57.0min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43397442061) |
| #43363991240<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 50.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43363991240) |
| #43252798396<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 45.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43252798396) |
| #43421967630<br>[#50122 [Feat] mem_cache: Add opt-in GreedyDual-Size eviction for Mamba states (--radix-eviction-policy gds)](https://github.com/sgl-project/sglang/pull/50122) | `feat/mamba-gds-eviction-option` | 39.0min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43421967630) |
| #43408723868<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 39.0min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43408723868) |
| #43388170016<br>[#49214 [Feat] [MLU] attention: Add GQA and MLA support](https://github.com/sgl-project/sglang/pull/49214) | `feat/mlu-paged-gqa-fused-ops` | 38.4min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43388170016) |
| #43341529968<br>[#50203 [CI] [NPU] dependencies: Install bundled kernels from post4](https://github.com/sgl-project/sglang/pull/50203) | `main` | 36.9min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43341529968) |
| #43361257219<br>[#40333 [Feat] [NVIDIA] deepseek-v4.1: Support prefill CP with BCG in PD serving (2/N)](https://github.com/sgl-project/sglang/pull/40333) | `main-v4.1-cp-bcg` | 36.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43361257219) |
| #43442379604<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 36.2min | 4 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43442379604) |
| #43378856497<br>[#47856 [Fix] [NPU] profiler: :bug: Fix patches and daemon trace parsing](https://github.com/sgl-project/sglang/pull/47856) | `junlin/diffusion-npu-profiler` | 36.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43378856497) |
| #43269121740<br>[#50191 [Refactor] distributed: One PP relay for the HiCache, bootstrap and grammar PP syncs](https://github.com/sgl-project/sglang/pull/50191) | `fix-45351-pp-sync-window` | 36.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43269121740) |
| #43379546878<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 35.9min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43379546878) |
| #43448070730<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 35.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43448070730) |
| #43316841148<br>[#50176 [CI] disaggregation: Launch sgl-router instead of sgl-model-gateway in the PD tests](https://github.com/sgl-project/sglang/pull/50176) | `lsyin/ci-sgl-router` | 34.6min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43316841148) |
| #43303906520<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 34.2min | 3 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43303906520) |
| #43402870959<br>[#47856 [Fix] [NPU] profiler: :bug: Fix patches and daemon trace parsing](https://github.com/sgl-project/sglang/pull/47856) | `junlin/diffusion-npu-profiler` | 34.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43402870959) |
| #43258629091<br>[#49353 [Perf] [NPU] MiniMax-H3: optimize RMSNorm and SwiGLU](https://github.com/sgl-project/sglang/pull/49353) | `minimax_npu_rmsnorm_path` | 33.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43258629091) |
| #43370777229<br>[#49905 [Perf] gdn: Fuse MIS mapped gates into QKV preparation](https://github.com/sgl-project/sglang/pull/49905) | `mani1106/gdn-mis-mapped-gating` | 33.0min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43370777229) |
| #43432715715<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 32.5min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43432715715) |
| #43309559279<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 31.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43309559279) |
| #43286211201<br>[#49600 [Feat] function_call: Add granite_toolcall_parser for Granite 4.2](https://github.com/sgl-project/sglang/pull/49600) | `granite-toolcall-parser` | 28.9min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43286211201) |
| #43368981615<br>[#45488 [Fix] [NVIDIA] kvcache: Gate fused FP8 prefix-valid commit kernel on SM89+](https://github.com/sgl-project/sglang/pull/45488) | `sm86-prefix-valid-gate` | 28.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43368981615) |
| #43406779570<br>[#43579 [Feat] [NPU] sparse-kv: Extend offload with PD disaggregation and LRU caching](https://github.com/sgl-project/sglang/pull/43579) | `cryang/pr/sparsity-pd-disagg-LRU` | 27.1min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43406779570) |
| #43388944084<br>[#33815 [Feat] [Intel] diffusion: Add rotary embedding kernel for CPU](https://github.com/sgl-project/sglang/pull/33815) | `sgl-diffusion-rope` | 26.3min | 5 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43388944084) |
| #43277283729<br>[#49413 [Perf] multi-item-scoring: avoid host syncs in label-logprob readback and embed overrides](https://github.com/sgl-project/sglang/pull/49413) | `perf/mis-host-syncs` | 25.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43277283729) |
| #43320451285<br>[#49686 [Feat] disaggregation: Make the PD top-logprobs metadata width configurable](https://github.com/sgl-project/sglang/pull/49686) | `pd-max-top-logprobs-num` | 24.8min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43320451285) |
| #43393631424<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 24.6min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43393631424) |
| #43310250031<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 19.2min | 6 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43310250031) |
| #43268612793<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 18.8min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43268612793) |
| #43419857096<br>[#49289 [Test] [NPU] rl: Add P0 RLHF lifecycle coverage](https://github.com/sgl-project/sglang/pull/49289) | `test/rlhf-test-coverage` | 18.6min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43419857096) |
| #43350355739<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 18.0min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43350355739) |
| #43388308218 | `test/rlhf-test-coverage` | 17.9min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43388308218) |
| #43419287784<br>[#46408 [Refactor] multimodal: [MM refactor 2/9] Initialize multimodal processors from a processor config](https://github.com/sgl-project/sglang/pull/46408) | `rockdu-dev-mm-v2/02-processor-config` | 17.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43419287784) |
| #43358941806 | `test/rlhf-test-coverage` | 15.6min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43358941806) |
| #43359661383<br>[#40333 [Feat] [NVIDIA] deepseek-v4.1: Support prefill CP with BCG in PD serving (2/N)](https://github.com/sgl-project/sglang/pull/40333) | `main-v4.1-cp-bcg` | 15.1min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43359661383) |
| #43271977620<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 14.7min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43271977620) |
| #43392260910<br>[#33815 [Feat] [Intel] diffusion: Add rotary embedding kernel for CPU](https://github.com/sgl-project/sglang/pull/33815) | `sgl-diffusion-rope` | 14.4min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43392260910) |
| #43407726275<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 13.8min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43407726275) |
| #43394081243 | `sgl-diffusion-rope` | 11.9min | 10 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43394081243) |

---


## [Run #43448070730](https://github.com/sgl-project/sglang/actions/runs/43448070730)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 35.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43448070730

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 10.3min | 环境问题 | 依赖下载时网络超时导致安装失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720022) |

- **base-b-test-2-npu-a3 / run (0)**: uv 下载 asttokens==3.0.2 时网络超时（UV_HTTP_TIMEOUT 30s），解压失败，进程退出码 1，属代理/网络环境问题，非代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720022

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131963146463) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131963146833) |
| multimodal-gen-test-4-npu-a3 (0) | 30.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964719215) |
| multimodal-gen-test-4-npu-a3 (1) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964719338) |
| multimodal-gen-test-1-npu-a3 (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964719399) |
| multimodal-gen-test-1-npu-a3 (1) | 26.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964719962) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964719981) |
| base-b-test-1-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720169) |
| base-b-test-4-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720171) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720240) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43448070730/job/131964720399) |


## [Run #43442379604](https://github.com/sgl-project/sglang/actions/runs/43442379604)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 36.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43442379604

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.5min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424891) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装 pip 后中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131961177628) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131961177653) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.5min | 环境问题 | 自托管 runner 容器执行失败，作业在安装 triton-ascend 时中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131961177758) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424891

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 pip 安装完成后报错 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131961177628

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 pip 正在安装 triton-ascend 等依赖时，报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131961177653

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示下载 triton-ascend 3.2.2 wheel 后立即报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131961177758

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131943139464) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131943139575) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424527) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424569) |
| multimodal-gen-test-4-npu-a3 (1) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424714) |
| base-b-test-16-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424870) |
| base-b-test-2-npu-a3 / run (0) | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424878) |
| base-b-test-4-npu-a3 / run (1) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424879) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424973) |
| base-b-test-4-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944424996) |
| base-b-test-1-npu-a3 / run (0) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43442379604/job/131944425415) |


## [Run #43439300151](https://github.com/sgl-project/sglang/actions/runs/43439300151)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 19.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43439300151

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933900645) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933900747) |
| multimodal-gen-test-4-npu-a3 (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933900780) |
| multimodal-gen-test-4-npu-a3 (1) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933900966) |
| base-b-test-2-npu-a3 / run (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933901028) |
| base-b-test-16-npu-a3 / run (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933901030) |
| base-b-test-8-npu-a3 / run (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933901122) |
| base-b-test-4-npu-a3 / run (1) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933901183) |
| base-b-test-1-npu-a3 / run (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933901190) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131933901234) |











### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131932558846) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43439300151/job/131932558979) |


## [Run #43432772826](https://github.com/sgl-project/sglang/actions/runs/43432772826)
- **分支**: `rocm-gdn-fused-decode-proj-conv`
- **总耗时**: 95.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43432772826

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.4min | 环境问题 | 容器内未安装 sglang 模块，导致测试脚本导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173545) |

- **base-b-test-16-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/环境中 sglang 未正确安装或 PYTHONPATH 未包含源码目录，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173545

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131910381031) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131910381119) |
| base-b-test-4-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173325) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173361) |
| multimodal-gen-test-4-npu-a3 (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173363) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173416) |
| base-b-test-1-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173532) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173533) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432772826/job/131911173549) |


## [Run #43432715715](https://github.com/sgl-project/sglang/actions/runs/43432715715)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 32.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43432715715

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 23.9min | 环境问题 | 代理服务器返回503导致依赖包下载失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012518) |

- **base-b-test-4-npu-a3 / run (0)**: 作业通过squid代理下载ops-transformer依赖包时，代理返回503 Service Unavailable，wget退出码1，容器执行失败。属CI网络/代理环境问题，非代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012518

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131910083480) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131910083525) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012288) |
| multimodal-gen-test-4-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012414) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012455) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012466) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012488) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012523) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012567) |
| base-b-test-8-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012808) |
| multimodal-gen-test-4-npu-a3 (0) | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43432715715/job/131911012902) |


## [Run #43423972912](https://github.com/sgl-project/sglang/actions/runs/43423972912)
- **分支**: `main`
- **总耗时**: 67.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43423972912

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 9.4min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796953) |

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796953

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131880793445) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796494) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796510) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796580) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796718) |
| base-b-test-1-npu-a3 / run (0) | 55.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796755) |
| base-b-test-4-npu-a3 / run (0) | 63.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796783) |
| base-b-test-16-npu-a3 / run (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796802) |
| base-b-test-8-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881796833) |
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43423972912/job/131881797009) |


## [Run #43421967630](https://github.com/sgl-project/sglang/actions/runs/43421967630)
- **分支**: `feat/mamba-gds-eviction-option`
- **总耗时**: 39.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43421967630

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 21.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045116) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_glm52.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045116

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131874091096) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131874091195) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875044819) |
| multimodal-gen-test-1-npu-a3 (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875044882) |
| multimodal-gen-test-4-npu-a3 (0) | 35.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875044884) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875044903) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875044993) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045067) |
| base-b-test-4-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045117) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045172) |
| base-b-test-1-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43421967630/job/131875045214) |


## [Run #43419857096](https://github.com/sgl-project/sglang/actions/runs/43419857096)
- **分支**: `test/rlhf-test-coverage`
- **总耗时**: 18.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43419857096

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 15.1min | 代码错误 | test_npu_device_barrier.py 测试失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173888) |
| base-b-test-1-npu-a3 / run (0) | 7.7min | 代码错误 | NPU 内存占用测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173946) |

- **base-b-test-2-npu-a3 / run (0)**: 3 个用例仅 1 个通过，test_npu_device_barrier.py 返回 exit code 1 导致作业失败；日志未显示具体 Traceback，需查看该用例详细输出定位原因。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173888

- **base-b-test-1-npu-a3 / run (0)**: test_npu_memory_occupation.py 运行 204 秒后 FAILED (errors=1)，2 个用例 0 通过，进程以退出码 1 结束，导致作业失败；日志未显示具体 Traceback，需查看该用例 setUpClass 阶段 server 启动或内存占用相关报错。
  - 失败用例: npu_memory_occupation.py, npu_memory_occupation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131868173946

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131867038775) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419857096/job/131867038799) |


## [Run #43419287784](https://github.com/sgl-project/sglang/actions/runs/43419287784)
- **分支**: `rockdu-dev-mm-v2/02-processor-config`
- **总耗时**: 17.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43419287784

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 14.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064546) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064546

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131865094242) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131865094266) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064364) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064442) |
| base-b-test-4-npu-a3 / run (1) | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43419287784/job/131866064453) |


## [Run #43416174523](https://github.com/sgl-project/sglang/actions/runs/43416174523)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 101.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43416174523

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 96.9min | 代码错误 | test_npu_eagle3.py 测试失败，退出码 5 表示 unittest 存在 errors | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052220) |

- **base-b-test-1-npu-a3 / run (0)**: speculative_inference/test_npu_eagle3.py 运行 35 秒后失败，退出码 5 表示 unittest 存在 errors，常见于 setUpClass 阶段 sglang server 启动失败（如 OOM 或进程被 SIGKILL），需查看日志中的 Traceback 确认具体错误。
  - 失败用例: npu_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052220

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131854656313) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131854656392) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052023) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052069) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052072) |
| base-b-test-2-npu-a3 / run (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052245) |
| base-b-test-16-npu-a3 / run (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052247) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052291) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052315) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052403) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43416174523/job/131856052430) |


## [Run #43408723868](https://github.com/sgl-project/sglang/actions/runs/43408723868)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 39.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43408723868

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 25.1min | 环境问题 | git fetch 拉取代码耗时约6分钟，作业在 checkout 后启动 k8s 步骤时被清理，疑似超时或环境异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629331) |
| base-b-test-4-npu-a3 / run (0) | 28.6min | 环境问题 | 日志在 checkout 后执行 k8s 脚本时中断，未出现测试用例错误信息，疑似 runner/容器环境异常导致作业提前终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629346) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 fetch 从 10:54:41 持续到 11:00:30 才完成，随后执行 k8s index.js 后立即出现 Cleaning up orphan processes，作业未进入实际测试阶段即终止，无测试错误输出，判断为环境/基础设施问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629331

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾仅显示运行 /home/runner/k8s/index.js 后清理孤儿进程，无 Traceback 或退出码 5 的用例错误，失败发生在测试执行前的环境准备阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629346

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131831634602) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131831634650) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629118) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629172) |
| multimodal-gen-test-4-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629216) |
| base-b-test-16-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629274) |
| multimodal-gen-test-4-npu-a3 (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629294) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629314) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629329) |
| base-b-test-8-npu-a3 / run (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43408723868/job/131832629470) |


## [Run #43407726275](https://github.com/sgl-project/sglang/actions/runs/43407726275)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 13.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43407726275

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 5.1min | 环境问题 | multimodal-gen 测试失败，diffusion-failures 目录无文件，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246406) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | 环境问题 | 测试脚本未生成 diffusion-failures 目录，疑似用例执行阶段失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246436) |
| multimodal-gen-test-1-npu-a3 (0) | 4.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246474) |
| multimodal-gen-test-4-npu-a3 (1) | 5.5min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246527) |
| base-b-test-2-npu-a3 / run (0) | 10.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246605) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246634) |
| base-b-test-4-npu-a3 / run (1) | 5.1min | 环境问题 | 下载 GitHub Action 时任务被取消，作业未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246652) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246683) |
| base-b-test-1-npu-a3 / run (0) | 1.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246760) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246786) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 路径文件，说明测试用例未正常产出失败样本；结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246406

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明用例未产出失败样本；结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246436

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约4分钟结束，无明确Traceback。结合退出码5，最可能是setUpClass中server启动失败（如host OOM或进程被SIGKILL），属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246474

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中未见具体 Traceback，但退出码5表明 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。另 upload-artifact 未找到 diffusion-failures/ 目录，无产物上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246527



- **base-b-test-4-npu-a3 / run (1)**: 日志显示在下载 actions/github-script@v8 后出现 'A task was canceled.'，作业在准备阶段即被取消，未执行任何测试用例，属于 runner/网络环境问题，而非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131827246652




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131826197775) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43407726275/job/131826198346) |


## [Run #43406779570](https://github.com/sgl-project/sglang/actions/runs/43406779570)
- **分支**: `cryang/pr/sparsity-pd-disagg-LRU`
- **总耗时**: 27.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43406779570

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 2.9min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055805) |

- **base-b-test-16-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 包未安装或 PYTHONPATH 未包含仓库路径，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055805

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131823132186) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131823132195) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055432) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055556) |
| base-b-test-1-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055655) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055725) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055736) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055818) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43406779570/job/131824055942) |


## [Run #43402870959](https://github.com/sgl-project/sglang/actions/runs/43402870959)
- **分支**: `junlin/diffusion-npu-profiler`
- **总耗时**: 34.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43402870959

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141833) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141862) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141975) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141978) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811142000) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811142060) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131810056115) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131810056155) |
| multimodal-gen-test-4-npu-a3 (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141592) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141610) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141697) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43402870959/job/131811141786) |


## [Run #43397442061](https://github.com/sgl-project/sglang/actions/runs/43397442061)
- **分支**: `feature/dsa-index-k-elision-hisparse-decode`
- **总耗时**: 57.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43397442061

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 14.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942167) |
| base-b-test-4-npu-a3 / run (0) | 21.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942771) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moe_dense_tp_size.py, npu_moe_dense_tp_size.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942167

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_w4a4_quantization.py, npu_w4a4_quantization.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942771

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131791924643) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131791924645) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942021) |
| multimodal-gen-test-1-npu-a3 (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942057) |
| multimodal-gen-test-4-npu-a3 (0) | 38.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942147) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942148) |
| multimodal-gen-test-4-npu-a3 (1) | 28.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942199) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942274) |
| base-b-test-16-npu-a3 / run (0) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942308) |
| base-b-test-1-npu-a3 / run (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43397442061/job/131792942369) |


## [Run #43395838536](https://github.com/sgl-project/sglang/actions/runs/43395838536)
- **分支**: `sgl-diffusion-rope`
- **总耗时**: 57.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43395838536

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799370065) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799370065

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131786838730) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131786838840) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787848794) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787848853) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787848866) |
| multimodal-gen-test-4-npu-a3 (0) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787848917) |
| base-b-test-16-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787849076) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787849134) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787849138) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787849331) |
| base-b-test-1-npu-a3 / run (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787849380) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131787849471) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799363190) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395838536/job/131799363508) |


## [Run #43394081243](https://github.com/sgl-project/sglang/actions/runs/43394081243)
- **分支**: `sgl-diffusion-rope`
- **总耗时**: 11.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43394081243

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 8.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781926934) |
| multimodal-gen-test-1-npu-a3 (1) | 8.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927029) |
| multimodal-gen-test-4-npu-a3 (1) | 6.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927067) |
| multimodal-gen-test-1-npu-a3 (0) | 8.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927077) |
| base-b-test-16-npu-a3 / run (0) | 8.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927182) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927197) |
| base-b-test-1-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在初始化阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927303) |
| base-b-test-4-npu-a3 / run (1) | 7.9min | 环境问题 | 自定义容器执行失败，作业在启动下一个测试文件时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927390) |
| base-b-test-4-npu-a3 / run (0) | 2.7min | 环境问题 | 容器内未安装 sglang 模块，导致测试脚本导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927444) |
| base-b-test-2-npu-a3 / run (0) | 2.8min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927572) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781926934

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927029

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例退出码5（unittest errors），常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志末尾仅见 diffusion-failures/ 目录无文件、artifact 未上传，未捕获到具体 Traceback，需查看中间省略部分确认真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927067

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以unittest errors退出（退出码5），常见于setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927077

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在容器内环境变量打印后、测试尚未真正开始，属于 runner/容器基础设施故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927182

- **base-b-test-8-npu-a3 / run (0)**: 日志中测试 1/1 passed，退出正常，仅出现 Node.js 弃用警告，未发现 Traceback 或错误，作业失败可能由日志截断或后续步骤导致，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927197

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；此前仅有 Gloo 连接与模型导入告警，未出现用例 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927303

- **base-b-test-4-npu-a3 / run (1)**: 前序测试均通过（Ran 2 tests OK），在开始运行 test_npu_speculative_multi_npu.py 后立即报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927390

- **base-b-test-4-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/环境中未正确安装 sglang 包，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927444

- **base-b-test-2-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 包未安装或 PYTHONPATH 未包含源码目录，属环境/依赖配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131781927572

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131780965015) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43394081243/job/131780965026) |


## [Run #43393631424](https://github.com/sgl-project/sglang/actions/runs/43393631424)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 24.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43393631424

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.2min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333073) |
| base-b-test-2-npu-a3 / run (0) | 7.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333134) |
| base-b-test-16-npu-a3 / run (0) | 20.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333144) |

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333073

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333134

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333144

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131779380866) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131779380986) |
| base-b-test-4-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780332979) |
| base-b-test-1-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780332984) |
| base-b-test-8-npu-a3 / run (0) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43393631424/job/131780333198) |


## [Run #43392260910](https://github.com/sgl-project/sglang/actions/runs/43392260910)
- **分支**: `sgl-diffusion-rope`
- **总耗时**: 14.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43392260910

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 10.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121694) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121714) |
| multimodal-gen-test-1-npu-a3 (1) | 10.6min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121743) |
| multimodal-gen-test-4-npu-a3 (0) | 10.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121745) |
| base-b-test-1-npu-a3 / run (0) | 10.5min | 环境问题 | 自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121820) |
| base-b-test-2-npu-a3 / run (0) | 10.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121902) |
| base-b-test-4-npu-a3 / run (0) | 10.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在初始化阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121977) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776122005) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | 环境问题 | 自定义容器执行失败，疑似 NPU 驱动/CANN 环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776122048) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约10分钟内结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121694

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业约10分钟结束，退出码5表明 unittest errors，最常见为 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121714

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中 upload-artifact 提示未找到 diffusion-failures/ 目录，说明测试用例未正常产出结果；结合退出码5，最可能是 setUpClass 阶段 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121743

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact，说明测试用例执行失败。退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121745

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时/环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器实现。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121820

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题；需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121902

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 DetokenizerManager 初始化后立即报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121977

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载过程中出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776122005

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，且此前出现 CANN 与 HDK 驱动版本需 32 字节 padding 处理的警告，容器运行环境异常导致作业提前终止，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776122048

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131775032456) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131775032486) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43392260910/job/131776121995) |


## [Run #43388944084](https://github.com/sgl-project/sglang/actions/runs/43388944084)
- **分支**: `sgl-diffusion-rope`
- **总耗时**: 26.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43388944084

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 18.3min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207028) |
| multimodal-gen-test-4-npu-a3 (1) | 18.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207061) |
| base-b-test-16-npu-a3 / run (0) | 20.3min | 环境问题 | 容器执行失败，TokenizerManager 看门狗超时，疑似服务启动阶段资源不足或进程异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207189) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在初始化阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207207) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207234) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约18分钟后结束，未找到 diffusion-failures/ 产物；退出码5表示 unittest 存在 errors，最常见为 setUpClass 阶段 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207028

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；退出码5 表示 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207061

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TokenizerManager watchdog timeout（soft=True），随后报错“Executing the custom container implementation failed”，DeepseekV3 权重加载耗时约 870 秒，疑似 host 资源不足或容器进程被终止导致 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207189

- **base-b-test-1-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员；此前 NPU 初始化正常，未见用例 Traceback，属 runner/容器环境故障，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207207

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 Gloo 初始化正常完成后报错 'Executing the custom container implementation failed'，提示联系 self-hosted runner 管理员，属于 runner/容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207234

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131764393572) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131764393590) |
| multimodal-gen-test-1-npu-a3 (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765206985) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207065) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207175) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207212) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388944084/job/131765207235) |


## [Run #43388545447](https://github.com/sgl-project/sglang/actions/runs/43388545447)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 74.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43388545447

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | 环境问题 | 日志在 checkout 后即结束，未进入测试阶段，疑似 runner 或容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131779781468) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾仅显示 checkout 完成及 k8s 脚本启动，随后出现清理 orphan 进程，无测试执行或错误 Traceback，无法确认具体失败点，倾向环境/runner 问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131779781468

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131762839414) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131762839628) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800509) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800552) |
| multimodal-gen-test-4-npu-a3 (0) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800564) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800608) |
| base-b-test-16-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800641) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800762) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800773) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800775) |
| base-b-test-1-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800825) |
| base-b-test-4-npu-a3 / run (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131763800878) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131779781374) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 30.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388545447/job/131779781456) |


## [Run #43388308218](https://github.com/sgl-project/sglang/actions/runs/43388308218)
- **分支**: `test/rlhf-test-coverage`
- **总耗时**: 17.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43388308218

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 14.9min | 代码错误 | test_npu_device_barrier.py 测试失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849654) |
| base-b-test-1-npu-a3 / run (0) | 7.9min | 代码错误 | test_npu_memory_occupation.py 测试失败，unittest 报 errors=1，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849705) |

- **base-b-test-2-npu-a3 / run (0)**: 3 个用例仅 1 个通过，test_npu_device_barrier.py 返回退出码 1（耗时 222s），日志未显示具体 Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849654

- **base-b-test-1-npu-a3 / run (0)**: 日志显示该用例 Ran 1 test，FAILED (errors=1)，耗时约 229 秒后返回退出码 1，导致 0/2 通过。错误发生在测试执行阶段（可能为 setUpClass 中 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_memory_occupation.py, npu_memory_occupation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762849705

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762077607) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388308218/job/131762077638) |


## [Run #43388170016](https://github.com/sgl-project/sglang/actions/runs/43388170016)
- **分支**: `feat/mlu-paged-gqa-fused-ops`
- **总耗时**: 38.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43388170016

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 2.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083707) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083775) |
| base-b-test-16-npu-a3 / run (0) | 2.6min | 环境问题 | 容器内未安装 sglang 模块，导致测试脚本导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083800) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083880) |



- **base-b-test-16-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/依赖安装步骤未正确安装 sglang 包，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083800


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131778187176) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131778187289) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083572) |
| multimodal-gen-test-1-npu-a3 (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083573) |
| multimodal-gen-test-4-npu-a3 (0) | 34.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083575) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083595) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083678) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43388170016/job/131779083813) |


## [Run #43386176541](https://github.com/sgl-project/sglang/actions/runs/43386176541)
- **分支**: `pd-prefill-release-mm-features`
- **总耗时**: 102.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43386176541

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.1min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 执行失败，退出码 1，3 个用例全部未通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131787422832) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本运行 551 秒后返回 exit code 1，Test Summary 为 0/3 passed，属于用例执行失败；日志未给出具体 Traceback，无法确认是性能回归还是环境问题，需查看该用例详细输出。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131787422832

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131755269999) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131755270034) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225231) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225333) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225335) |
| base-b-test-16-npu-a3 / run (0) | 35.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225371) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225401) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225404) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225424) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131756225431) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131770409869) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131770409891) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 39.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131770409979) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43386176541/job/131787422816) |


## [Run #43379546878](https://github.com/sgl-project/sglang/actions/runs/43379546878)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 35.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43379546878

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 7.2min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759774) |
| base-b-test-1-npu-a3 / run (0) | 13.7min | 代码错误 | HiCache 测试用例 test_npu_dsv4_hicache_l2_pool.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759805) |
| base-b-test-4-npu-a3 / run (0) | 13.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759843) |
| base-b-test-16-npu-a3 / run (0) | 31.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759904) |

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759774

- **base-b-test-1-npu-a3 / run (0)**: 4 个用例中 2 个通过，HiCache 的 test_npu_dsv4_hicache_l2_pool.py 仅运行 16 秒即退出码 1 失败，导致作业整体失败；日志省略部分未显示具体 Traceback，需查看该用例详细报错定位。
  - 失败用例: npu_dsv4_hicache_l2_pool.py, npu_dsv4_hicache_l2_pool.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759805

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759843

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734759904

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734001917) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734001920) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734760142) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43379546878/job/131734760254) |


## [Run #43378856497](https://github.com/sgl-project/sglang/actions/runs/43378856497)
- **分支**: `junlin/diffusion-npu-profiler`
- **总耗时**: 36.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43378856497

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448582) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448593) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448609) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448641) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448650) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448661) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131731829530) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131731829931) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448451) |
| multimodal-gen-test-4-npu-a3 (0) | 33.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448452) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448454) |
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43378856497/job/131732448456) |


## [Run #43370777229](https://github.com/sgl-project/sglang/actions/runs/43370777229)
- **分支**: `mani1106/gdn-mis-mapped-gating`
- **总耗时**: 33.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43370777229

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 8.2min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报 errors=1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830229) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 228 秒后 FAILED (errors=1)，退出码 1，2 个用例 0 通过。日志省略了具体 Traceback，推测为 setUpClass 阶段 server 启动失败或 PD 分离逻辑异常，需查看完整错误堆栈定位。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830229

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131705931366) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131705931410) |
| multimodal-gen-test-4-npu-a3 (0) | 29.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706829895) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706829970) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830012) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830024) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830047) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830191) |
| base-b-test-16-npu-a3 / run (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830200) |
| base-b-test-4-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830337) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43370777229/job/131706830375) |


## [Run #43368981615](https://github.com/sgl-project/sglang/actions/runs/43368981615)
- **分支**: `sm86-prefix-valid-gate`
- **总耗时**: 28.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43368981615

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953200) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953200

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700193468) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700193528) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700952852) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700952917) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953119) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953171) |
| base-b-test-16-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953184) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953194) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368981615/job/131700953224) |


## [Run #43368610640](https://github.com/sgl-project/sglang/actions/runs/43368610640)
- **分支**: `fix/encoder-embedding-prefix-reuse`
- **总耗时**: 93.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43368610640

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 25.6min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131722253687) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示服务端推理请求均返回 200 OK，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131722253687

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131698987275) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131698987294) |
| multimodal-gen-test-4-npu-a3 (0) | 29.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634232) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634256) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634267) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634313) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634370) |
| base-b-test-16-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634371) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634381) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634423) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634484) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131699634541) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131708806897) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131708806915) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 38.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131708806951) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43368610640/job/131722253679) |


## [Run #43363991240](https://github.com/sgl-project/sglang/actions/runs/43363991240)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 50.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43363991240

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098042) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098042

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131684115920) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131684116029) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685097808) |
| multimodal-gen-test-1-npu-a3 (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685097849) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685097873) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685097898) |
| base-b-test-4-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685097980) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098012) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098020) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098082) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43363991240/job/131685098110) |


## [Run #43361257219](https://github.com/sgl-project/sglang/actions/runs/43361257219)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 36.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43361257219

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 9.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201245) |
| base-b-test-1-npu-a3 / run (0) | 7.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201282) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201245

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201282

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131675330740) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131675330785) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201146) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201193) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201199) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201221) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201261) |
| base-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201275) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201303) |
| base-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43361257219/job/131676201354) |


## [Run #43359661383](https://github.com/sgl-project/sglang/actions/runs/43359661383)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 15.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43359661383

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 11.9min | 环境问题 | multimodal-gen 测试失败，diffusion-failures 目录无文件，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815214) |
| multimodal-gen-test-1-npu-a3 (1) | 11.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815253) |
| multimodal-gen-test-4-npu-a3 (0) | 11.9min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815274) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | 环境问题 | Scheduler watchdog 超时，容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815384) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | 环境问题 | 自定义容器执行失败，作业在测试运行中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815458) |
| base-b-test-4-npu-a3 / run (0) | 11.8min | 环境问题 | 自定义容器执行失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815460) |
| base-b-test-2-npu-a3 / run (0) | 11.7min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815598) |
| base-b-test-1-npu-a3 / run (0) | 11.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815654) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670816214) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示上传 diffusion-failures/ 时无文件，说明测试用例未产出失败样本；结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），属环境/资源问题，需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815214

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，按约定表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815253

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约11分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815274

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP14 EP14 Scheduler watchdog timeout（watchdog_timeout=300），随后报错“Executing the custom container implementation failed”，属于运行环境/容器异常导致作业失败，非用例收集问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815384

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 NPU 算子回退警告后出现 'Executing the custom container implementation failed'，属自托管 runner 容器环境异常，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815458

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非用例代码问题；此前仅有 torch_npu 的 ImportWarning/RuntimeWarning，无实际 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815460

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 health_generate 返回 503，随后报错 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815598

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到 0% 时出现 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码错误；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815654

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例以退出码5结束（unittest errors），且未生成 diffusion-failures 目录产物，说明测试在 setUpClass 阶段即失败，最可能是 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670816214

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670024333) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670024456) |
| base-b-test-8-npu-a3 / run (0) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43359661383/job/131670815560) |


## [Run #43358941806](https://github.com/sgl-project/sglang/actions/runs/43358941806)
- **分支**: `test/rlhf-test-coverage`
- **总耗时**: 15.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43358941806

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 12.4min | 代码错误 | NPU设备屏障测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131731181173) |
| base-b-test-1-npu-a3 / run (0) | 4.4min | 环境问题 | 测试脚本 unittest 报错（errors=1），疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131731181253) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_device_barrier.py 返回退出码1，3个用例仅1个通过；日志未显示具体Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131731181173

- **base-b-test-1-npu-a3 / run (0)**: test_npu_memory_occupation.py 运行 0 个用例、FAILED (errors=1)，退出码 5，说明 unittest 存在 error，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看日志中真实 Traceback 确认。
  - 失败用例: npu_memory_occupation.py, npu_memory_occupation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131731181253

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131730224150) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43358941806/job/131730224272) |


## [Run #43357476873](https://github.com/sgl-project/sglang/actions/runs/43357476873)
- **分支**: `hicache-hybrid-swa-fixes`
- **总耗时**: 92.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43357476873

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.8min | 性能回归 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 退出码为 1，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131684421136) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 3 个性能用例中 1 个通过、1 个失败（exit code 1），失败用例为 qwen3_6_27b 1p in1024x1024_30 out1024_50ms，耗时 896s；日志未给出具体 Traceback，需查看该用例详细输出以确认是性能不达标还是 server 启动异常。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131684421136

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663171879) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663172087) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843639) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843706) |
| base-b-test-16-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843768) |
| base-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843821) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843850) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843870) |
| base-b-test-2-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843889) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131663843982) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131672652233) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131672652261) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131672652576) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43357476873/job/131684421231) |


## [Run #43350355739](https://github.com/sgl-project/sglang/actions/runs/43350355739)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 18.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43350355739

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 8.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555048) |
| base-b-test-4-npu-a3 / run (0) | 11.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555088) |
| base-b-test-16-npu-a3 / run (0) | 14.9min | 环境问题 | 自定义容器执行失败，作业在容器启动阶段报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555122) |
| base-b-test-1-npu-a3 / run (0) | 14.7min | 代码错误 | HiCache 测试 test_npu_dsv4_hicache_l2_pool.py 运行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555127) |

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555048

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555088

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，runner 无法正常启动自定义容器，导致测试未真正执行，属于自托管 runner/容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555122

- **base-b-test-1-npu-a3 / run (0)**: 4 个用例中 2 个通过，HiCache 的 test_npu_dsv4_hicache_l2_pool.py 仅运行 18 秒即退出码 1 失败，其余 quant 用例正常，属该测试脚本自身执行错误，需查看其 Traceback 定位。
  - 失败用例: npu_dsv4_hicache_l2_pool.py, npu_dsv4_hicache_l2_pool.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555127

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131639838773) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131639838836) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555030) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43350355739/job/131640555081) |


## [Run #43341529968](https://github.com/sgl-project/sglang/actions/runs/43341529968)
- **分支**: `main`
- **总耗时**: 36.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43341529968

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 28.0min | 代码错误 | NPU 用例 test_npu_return_indexer_topk_deepseek_v4.py 执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842442) |
| base-b-test-4-npu-a3 / run (1) | 14.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842460) |
| base-b-test-1-npu-a3 / run (0) | 18.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842980) |

- **base-b-test-2-npu-a3 / run (0)**: TIMINGS 显示 test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py 的 passed 为 false（耗时 141s），其余用例均通过，最终进程以 exit code 1 结束。日志未给出该用例的 Traceback，需查看该用例详细输出以确认是 setUpClass 阶段 server 启动失败还是断言失败。
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842442

- **base-b-test-4-npu-a3 / run (1)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_multi_npu.py, npu_speculative_multi_npu.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842460

- **base-b-test-1-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842980

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131614861407) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131614861442) |
| multimodal-gen-test-4-npu-a3 (0) | 33.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842224) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842270) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842296) |
| base-b-test-16-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842298) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842317) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842353) |
| base-b-test-4-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43341529968/job/131615842516) |


## [Run #43327941220](https://github.com/sgl-project/sglang/actions/runs/43327941220)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 60.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43327941220

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.9min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131579549597) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示服务正常推理后突然报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131579549597

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131565298391) |
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131565298724) |
| multimodal-gen-test-4-npu-a3 (1) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761395) |
| multimodal-gen-test-4-npu-a3 (0) | 35.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761413) |
| multimodal-gen-test-1-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761429) |
| base-b-test-1-npu-a3 / run (0) | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761606) |
| base-b-test-16-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761667) |
| multimodal-gen-test-1-npu-a3 (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761775) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761793) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761878) |
| base-b-test-2-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761964) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131566761999) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131579549491) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43327941220/job/131579549533) |


## [Run #43322304564](https://github.com/sgl-project/sglang/actions/runs/43322304564)
- **分支**: `erik/prefill-chunk-fit-free-pool`
- **总耗时**: 76.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43322304564

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.6min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 执行失败，退出码 1，3 个用例全部未通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131574972898) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本运行约 552 秒后返回退出码 1，Test Summary 为 0/3 passed，但省略部分未包含具体 Traceback，无法确定是 server 启动失败、OOM 还是性能指标不达标，需查看完整日志定位。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131574972898

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131546040351) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131546040460) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322023) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322100) |
| base-b-test-16-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322266) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322295) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322307) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322317) |
| base-b-test-2-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322371) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131547322450) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131559786664) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131559786674) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131559786688) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43322304564/job/131574973022) |


## [Run #43320451285](https://github.com/sgl-project/sglang/actions/runs/43320451285)
- **分支**: `pd-max-top-logprobs-num`
- **总耗时**: 24.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43320451285

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540827894) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540827894

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131539709048) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131539709053) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540827865) |
| base-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540827914) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540828063) |
| base-b-test-16-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540828074) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540828149) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540828165) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43320451285/job/131540829519) |


## [Run #43316841148](https://github.com/sgl-project/sglang/actions/runs/43316841148)
- **分支**: `lsyin/ci-sgl-router`
- **总耗时**: 34.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43316841148

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 1.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131529975391) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 环境问题 | 本地 action 目录 download-sgl-router 缺少 action.yml，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131529975432) |


- **base-b-test-4-npu-a3 / run (1)**: 日志报错：Can't find 'action.yml'/'action.yaml'/'Dockerfile' under .github/actions/download-sgl-router，说明该本地 action 未正确检出或目录缺失，属于 CI 配置/环境问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131529975432

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131527227956) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131527228008) |
| sgl-router-build-aarch64 / Build sgl-router | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131527355292) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528579935) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528579951) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528580017) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528580034) |
| base-b-test-1-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528580144) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528580215) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528580255) |
| base-b-test-16-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43316841148/job/131528580318) |


## [Run #43310250031](https://github.com/sgl-project/sglang/actions/runs/43310250031)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 19.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43310250031

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 16.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505430836) |
| multimodal-gen-test-4-npu-a3 (1) | 16.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505430873) |
| base-b-test-2-npu-a3 / run (0) | 16.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431097) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431122) |
| base-b-test-8-npu-a3 / run (0) | 1.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431141) |
| multimodal-gen-test-1-npu-a3 (1) | 16.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431195) |
| base-b-test-1-npu-a3 / run (0) | 16.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431239) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505432286) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505430836

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例未正常产出失败产物；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505430873

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例本身已通过（Ran 2 tests OK），但在开始第4个用例时出现 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431097

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，并非用例断言失败；此前 dp_attention 用例已结束，w4a4 量化用例刚开始即中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431122


- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431195

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已启动完成，但随后报错“Executing the custom container implementation failed”，属 runner/容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431239


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131504375766) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131504375961) |
| multimodal-gen-test-1-npu-a3 (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505430751) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43310250031/job/131505431316) |


## [Run #43309559279](https://github.com/sgl-project/sglang/actions/runs/43309559279)
- **分支**: `new-model-support`
- **总耗时**: 31.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43309559279

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 30.8min | 性能回归 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669213712) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 3 个性能用例中 1 个通过、1 个失败（in1024x1024_30_out1024_50ms，耗时 961s，退出码 1），日志未显示具体 Traceback，需查看该用例详细输出以确认是性能不达标还是 server 启动异常。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669213712

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669211978) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212005) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212074) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212354) |
| base-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212440) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212554) |
| base-b-test-4-npu-a3 / run (1) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212555) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212567) |
| base-b-test-16-npu-a3 / run (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212639) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212656) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212784) |
| base-b-test-2-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669212853) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669214122) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669214209) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 35.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669214275) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43309559279/job/131669215065) |


## [Run #43303906520](https://github.com/sgl-project/sglang/actions/runs/43303906520)
- **分支**: `new-model-support`
- **总耗时**: 34.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43303906520

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483506931) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131497133355) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131497133634) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾显示diffusion-failures/目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483506931

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载至74%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例本身失败，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131497133355

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示依赖安装完成后报错“Executing the custom container implementation failed”，属 runner/容器环境问题，非用例代码或精度失败，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131497133634

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131482215583) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131482215684) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483506964) |
| multimodal-gen-test-1-npu-a3 (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507002) |
| multimodal-gen-test-4-npu-a3 (1) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507048) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507168) |
| base-b-test-16-npu-a3 / run (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507255) |
| base-b-test-2-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507274) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507355) |
| base-b-test-4-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507421) |
| base-b-test-4-npu-a3 / run (1) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131483507550) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43303906520/job/131497133406) |


## [Run #43286211201](https://github.com/sgl-project/sglang/actions/runs/43286211201)
- **分支**: `granite-toolcall-parser`
- **总耗时**: 28.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43286211201

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 4.1min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720277) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720314) |
| base-b-test-8-npu-a3 / run (0) | 3.9min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720351) |

- **base-b-test-4-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 包未安装或 PYTHONPATH 未包含源码目录，属于环境/安装配置问题，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720277


- **base-b-test-8-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 未正确安装或 PYTHONPATH 未包含源码目录，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720351

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131836795477) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131836795541) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720191) |
| base-b-test-1-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720378) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720465) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720467) |
| base-b-test-2-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43286211201/job/131837720752) |


## [Run #43277283729](https://github.com/sgl-project/sglang/actions/runs/43277283729)
- **分支**: `perf/mis-host-syncs`
- **总耗时**: 25.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43277283729

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 16.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390608802) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moe_runner_backend.py, npu_moe_runner_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390608802

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131389224665) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131389224832) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390608595) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390608600) |
| base-b-test-1-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390609168) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390609176) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390609237) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390609268) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43277283729/job/131390609666) |


## [Run #43271977620](https://github.com/sgl-project/sglang/actions/runs/43271977620)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 14.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43271977620

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372683458) |
| base-b-test-4-npu-a3 / run (0) | 10.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684153) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | 环境问题 | 自定义容器执行失败，作业在加载模型分片时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684253) |
| base-b-test-16-npu-a3 / run (0) | 10.1min | 超时 | Scheduler watchdog 超时，容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684283) |
| base-b-test-2-npu-a3 / run (0) | 10.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684347) |
| base-b-test-1-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372685018) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例退出码5（FAILED errors=N），常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）；且未生成 diffusion-failures/ 目录，无产物上传。需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372683458

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在容器内进程刚启动、尚未进入测试用例阶段，属于 runner/容器环境故障，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684153

- **base-b-test-4-npu-a3 / run (1)**: 日志显示“Executing the custom container implementation failed”，发生在多线程加载模型分片约73%时，属于自托管 runner 容器环境异常，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684253

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP12 EP12 调度器 watchdog 超时（watchdog_timeout=300，soft=True），随后报错“Executing the custom container implementation failed”，作业因超时/容器执行失败终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684283

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载到约31%时出现“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner/容器环境故障，并非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684347

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到25%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器运行时故障，并非用例或代码本身报错，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372685018

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131371315652) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131371315963) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684129) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43271977620/job/131372684339) |


## [Run #43269121740](https://github.com/sgl-project/sglang/actions/runs/43269121740)
- **分支**: `fix-45351-pp-sync-window`
- **总耗时**: 36.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43269121740

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 2.7min | 环境问题 | pip 安装 triton-ascend 依赖 scipy==1.13.1 时找不到匹配版本，导致依赖安装失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362550588) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 ERROR: Could not find a version that satisfies the requirement scipy==1.13.1 (from triton-ascend)，from versions: none，随后 No matching distribution found，进程退出码 1。属于依赖源/镜像缺少该包的环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362550588

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131360886486) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131360886556) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362549146) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362549161) |
| multimodal-gen-test-4-npu-a3 (0) | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362549406) |
| multimodal-gen-test-4-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362549490) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362549882) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362550056) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362550309) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362550333) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43269121740/job/131362550499) |


## [Run #43268612793](https://github.com/sgl-project/sglang/actions/runs/43268612793)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 18.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43268612793

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 14.7min | 环境问题 | 测试用例全部通过，但自定义容器执行失败导致作业报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502483) |
| base-b-test-4-npu-a3 / run (0) | 14.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502585) |
| base-b-test-1-npu-a3 / run (0) | 14.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502667) |
| base-b-test-2-npu-a3 / run (0) | 14.5min | 环境问题 | 自定义容器执行失败，作业被 runner 异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502949) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示测试 1/1 通过，随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器环境问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502483

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题；此前推理日志正常，无 Traceback 或退出码 5 等用例失败证据。
  链接: https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502585

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502667

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 返回 200 OK），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502949

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 3.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131359457957) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131359458055) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502218) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502518) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502571) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43268612793/job/131361502784) |


## [Run #43258629091](https://github.com/sgl-project/sglang/actions/runs/43258629091)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 33.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43258629091

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.8min | 其他 | 日志被截断，未见真实错误，无法确定失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775765) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示 artifact 上传成功和 Node.js 弃用警告，中间省略部分可能含 Traceback；退出码 5 提示 unittest 有 errors，常见为 setUpClass 中 sglang server 启动失败（如 OOM/SIGKILL），但需查看完整日志确认。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775765

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131323849803) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775403) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775505) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43258629091/job/131324775563) |


## [Run #43252798396](https://github.com/sgl-project/sglang/actions/runs/43252798396)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 45.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43252798396

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 8.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131320022689) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131320022689

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131303248267) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131303248344) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880076) |
| multimodal-gen-test-4-npu-a3 (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880162) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880214) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880321) |
| base-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880397) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880456) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880460) |
| base-b-test-4-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880475) |
| base-b-test-1-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880488) |
| base-b-test-16-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131304880542) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131320022622) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43252798396/job/131320022762) |


---
*Auto-generated by ci_monitor.py*