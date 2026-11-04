# NPU CI 执行监控（2026-11-04）
**生成时间**: 2026-11-05 07:19
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-04 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 156

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1649 个 | 失败 178 个 | 成功 Job 平均耗时 13.7min
- **Run 执行情况**: 成功 102 个 | 失败 54 个 | 成功 Run 平均耗时 62.7min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 56.3min | #41710323566 | [job link](https://github.com/sgl-project/sglang/actions/runs/41710323566/job/126190808216) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 52.5min | #41621617064 | [job link](https://github.com/sgl-project/sglang/actions/runs/41621617064/job/126055971547) |
| multimodal-gen-test-4-npu-a3 (0) | 49.0min | #41698494794 | [job link](https://github.com/sgl-project/sglang/actions/runs/41698494794/job/126137119487) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 48.0min | #41751190078 | [job link](https://github.com/sgl-project/sglang/actions/runs/41751190078/job/126326158289) |
| multimodal-gen-test-4-npu-a3 (0) | 47.9min | #41779296174 | [job link](https://github.com/sgl-project/sglang/actions/runs/41779296174/job/126407865778) |
| multimodal-gen-test-4-npu-a3 (0) | 46.8min | #41744532063 | [job link](https://github.com/sgl-project/sglang/actions/runs/41744532063/job/126295336835) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.5min | #41758590943 | [job link](https://github.com/sgl-project/sglang/actions/runs/41758590943/job/126350829160) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 45.7min | #41760650253 | [job link](https://github.com/sgl-project/sglang/actions/runs/41760650253/job/126360471900) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 44.4min | #41844678894 | [job link](https://github.com/sgl-project/sglang/actions/runs/41844678894/job/126641168079) |
| multimodal-gen-test-4-npu-a3 (0) | 44.3min | #41772067718 | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384944) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-4-npu-a3 / run (0) | 63.7min | #41828020202 | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005640) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.1min | #41759510680 | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126357495076) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 32.5min | #41790515878 | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126454478194) |
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | #41705053416 | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286687) |
| multimodal-gen-test-4-npu-a3 (1) | 31.6min | #41772067718 | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384954) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.4min | #41807933675 | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126509257191) |
| multimodal-gen-test-4-npu-a3 (0) | 29.4min | #41700041966 | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158646) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.3min | #41731704756 | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126262568075) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.9min | #41825612134 | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126571525797) |
| multimodal-gen-test-4-npu-a3 (0) | 25.4min | #41691550158 | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113147929) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-2-npu-a3 / run (0) | 132 | 105 | 9 | 9 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833536)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116323)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520137270)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814901)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408637) |
| base-b-test-1-npu-a3 / run (0) | 129 | 107 | 1 | 11 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473979) |
| base-b-test-4-npu-a3 / run (0) | 134 | 113 | 3 | 8 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005640)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833643)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392438) |
| base-b-test-16-npu-a3 / run (0) | 108 | 88 | 0 | 10 | 10 | - |
| base-b-test-4-npu-a3 / run (1) | 134 | 119 | 1 | 9 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005600) |
| base-b-test-8-npu-a3 / run (0) | 107 | 95 | 1 | 5 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126550000280) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 158 | 145 | 2 | 2 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126450599664)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126190249185) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 87 | 72 | 1 | 1 | 13 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126341433481) |
| multimodal-gen-test-4-npu-a3 (1) | 114 | 104 | 1 | 0 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384954) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 85 | 82 | 0 | 1 | 2 | - |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_mla_fia_hicache_bf16.py` | 31 | 26 | 5 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833536)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408637)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193741082) |
| `npu_expert_distribution_recorder_mode.py` | 24 | 22 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116323)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382804) |
| `npu_moe_dense_tp_size.py` | 23 | 21 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520137270)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814901) |
| `npu_dp_attention.py` | 30 | 28 | 2 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833643)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392438) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 9 | 7 | 2 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126450599664)<br>[base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126190249185) |
| `flux_2_image_t2i_2npu` | 29 | 28 | 1 | [multimodal-gen-test-4-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286549) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 36 | 35 | 1 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126550000280) |
| `npu_pd_disaggregation.py` | 36 | 35 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005600) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 6 | 5 | 1 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126341433481) |
| `TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance` | 1 | 0 | 1 | [multimodal-gen-test-4-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384954) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #41759510680<br>[#44394 [Feat] [CPU] cpu-graph: Add prefill torch compile graph and dynamic graph support](https://github.com/sgl-project/sglang/pull/44394) | `ecao/cpu_graph_prefill2` | 88.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41759510680) |
| #41767967939<br>[#48283 [Refactor] scheduler: Retire every queued abort through one RequestRetirer entry](https://github.com/sgl-project/sglang/pull/48283) | `lsyin/sched-pr18` | 70.0min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41767967939) |
| #41828020202<br>[#45885 [Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models](https://github.com/sgl-project/sglang/pull/45885) | `main` | 67.3min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41828020202) |
| #41756297347<br>[#48264 [Feat] beam: support LoRA for BF16 and FP8](https://github.com/sgl-project/sglang/pull/48264) | `yanbin/beam-lora-main` | 65.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41756297347) |
| #41790217718<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 65.2min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41790217718) |
| #41710208047<br>[#37273 [Feat] scheduler: Add opt-in DP-attention phase lockstep](https://github.com/sgl-project/sglang/pull/37273) | `dp-attn-phase-lockstep` | 59.2min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41710208047) |
| #41807933675<br>[#48328 [Fix] mamba: Give a lazy boundary snapshot its own slot instead of overwriting the keep slot](https://github.com/sgl-project/sglang/pull/48328) | `lsyin/sched-pr21` | 58.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41807933675) |
| #41825612134<br>[#44615 [Perf] NIXL: KV packing for TP-heterogeneous transfer (Muse Spark Open)](https://github.com/sgl-project/sglang/pull/44615) | `wj/nixl-kv-packing` | 56.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41825612134) |
| #41790515878<br>[#48343 [Fix] openai: Tool schema ids, explicit include_usage=false, and Kimi-K3 prompt fidelity](https://github.com/sgl-project/sglang/pull/48343) | `lsyin/openai-misc-fixes` | 56.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41790515878) |
| #41731704756<br>[#43910 [Refactor] scheduler: Hold the waiting queue and the chunked slot in request lists](https://github.com/sgl-project/sglang/pull/43910) | `lsyin/sched-pr16` | 53.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41731704756) |
| #41760392663<br>[#44416 [Perf] [AMD] GLM-5.3-Flash: One-launch MoE router and narrower KDA V tile for MTP verify](https://github.com/sgl-project/sglang/pull/44416) | `jacob/glm53-flash-moe-router-kda` | 47.6min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41760392663) |
| #41772067718<br>[#47907 [Perf] diffusion: Avoid upscaling native H3 references by default](https://github.com/sgl-project/sglang/pull/47907) | `h3-reference-max-default` | 46.7min | 1 | multimodal-gen-test-4-npu-a3 (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41772067718) |
| #41813700327<br>[#40333 [Feat] [NVIDIA] deepseek-v4.1: Support prefill CP with BCG in PD serving (2/N)](https://github.com/sgl-project/sglang/pull/40333) | `main-v4.1-cp-bcg` | 46.0min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41813700327) |
| #41801261120<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 44.1min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41801261120) |
| #41780850706<br>[#46730 [Feat] [Intel] moe: Run --moe-a2a-backend mooncake on Intel XPU](https://github.com/sgl-project/sglang/pull/46730) | `xpu-mooncake-ep` | 38.8min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41780850706) |
| #41765673077 | `main-v4.1-cp-bcg` | 38.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41765673077) |
| #41705053416<br>[#48217 [Refactor] custom-ar-v2: Single-word push epoch and consume-style pull semaphores](https://github.com/sgl-project/sglang/pull/48217) | `comm-push-epoch-protocol` | 37.7min | 3 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41705053416) |
| #41696104415<br>[#47200 [Perf] [NVIDIA] speculative-decoding: Add generic CUDA runtime fast paths](https://github.com/sgl-project/sglang/pull/47200) | `followup/qwen35-megakernel-runtime-v3-runtime` | 36.9min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41696104415) |
| #41722043068<br>[#43910 [Refactor] scheduler: Hold the waiting queue and the chunked slot in request lists](https://github.com/sgl-project/sglang/pull/43910) | `lsyin/sched-pr16` | 36.3min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41722043068) |
| #41761849462<br>[#46091 [Feat] usage: align prompt and cache accounting across APIs](https://github.com/sgl-project/sglang/pull/46091) | `wuyaole/feat-measured-cache-writes` | 35.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41761849462) |
| #41822547633<br>[#45885 [Feat] nemotron3-embed: Support Nemotron-3-Embed embedding models](https://github.com/sgl-project/sglang/pull/45885) | `anmolgupt/nemotron3-embed-model-support` | 35.0min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41822547633) |
| #41803533568<br>[#40822 [Feat] [Intel] Mistral: Enable Mistral series models on CPU](https://github.com/sgl-project/sglang/pull/40822) | `mistral-enable` | 35.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41803533568) |
| #41761633379<br>[#44526 [Feat] linker: Support runtime attach and detach of the unified cache external linker](https://github.com/sgl-project/sglang/pull/44526) | `feat/linker-runtime-attach` | 34.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41761633379) |
| #41681564052<br>[#43579 [Feat] [NPU] sparse-kv: Extend offload with PD disaggregation and LRU caching](https://github.com/sgl-project/sglang/pull/43579) | `cryang/pr/sparsity-pd-disagg-LRU` | 34.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41681564052) |
| #41772979847<br>[#43579 [Feat] [NPU] sparse-kv: Extend offload with PD disaggregation and LRU caching](https://github.com/sgl-project/sglang/pull/43579) | `cryang/pr/sparsity-pd-disagg-LRU` | 34.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41772979847) |
| #41700041966<br>[#48217 [Refactor] custom-ar-v2: Single-word push epoch and consume-style pull semaphores](https://github.com/sgl-project/sglang/pull/48217) | `comm-push-epoch-protocol` | 33.0min | 4 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41700041966) |
| #41793629847<br>[#48129 [Feat] PD: Validate speculative KV layout](https://github.com/sgl-project/sglang/pull/48129) | `xinyuan/pd-peer-fingerprint` | 32.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41793629847) |
| #41804628820<br>[#36788 [Feat] [AMD] quantization: Add dense NVFP4 support for gfx1201](https://github.com/sgl-project/sglang/pull/36788) | `feat/rdna4-nvfp4` | 31.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41804628820) |
| #41826482232<br>[#48390 [Feat] bailing: add TP-only FP8 and native Ling3 serving support](https://github.com/sgl-project/sglang/pull/48390) | `feat/ling3-model-pr` | 30.1min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41826482232) |
| #41691550158 | `followup/qwen35-megakernel-runtime-v3-runtime` | 30.0min | 4 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41691550158) |
| #41769286304<br>[#47859 [Feat] moe: Add Mooncake Elastic EP scale-up support](https://github.com/sgl-project/sglang/pull/47859) | `elastic-base` | 29.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41769286304) |
| #41714723081<br>[#46496 [Fix] scheduler: Keep the new-token ratio at its floor after a KV-full retraction](https://github.com/sgl-project/sglang/pull/46496) | `fix/retract-keeps-new-token-ratio` | 26.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41714723081) |
| #41822443978<br>[#48044 [Perf] [AMD] qwen3-next: Fuse the full-attention Q/K GemmaRMSNorm and partial RoPE into one Triton kernel on gfx950](https://github.com/sgl-project/sglang/pull/48044) | `feature/leixin/qwen3next-qknorm-rope-v2` | 24.7min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41822443978) |
| #41803475024<br>[#48375 [Feat] PD: Publish spec_kv_layout so DSpark/DFlash prefill and decode must match](https://github.com/sgl-project/sglang/pull/48375) | `pd-spec-kv-layout` | 23.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41803475024) |
| #41813697401<br>[#48129 [Feat] PD: Validate speculative KV layout](https://github.com/sgl-project/sglang/pull/48129) | `xinyuan/pd-peer-fingerprint` | 21.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41813697401) |
| #41630759939<br>[#43851 [Feat] [NVIDIA] dsv4.1: [1/N] Add packed FP4 Main KV storage for Hopper.](https://github.com/sgl-project/sglang/pull/43851) | `feat/dsv41-packed-main-kv` | 21.4min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41630759939) |
| #41721874254<br>[#48119 [Refactor] tokenizer: Fold `TokenizerWorker` into `TokenizerManager`](https://github.com/sgl-project/sglang/pull/48119) | `lsyin/multi-tokenizer-dedup` | 21.2min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41721874254) |
| #41728983717<br>[#43910 [Refactor] scheduler: Hold the waiting queue and the chunked slot in request lists](https://github.com/sgl-project/sglang/pull/43910) | `lsyin/sched-pr16` | 19.9min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41728983717) |
| #41776833181 | `ecao/xpu_graph_context_aware_opt` | 18.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41776833181) |
| #41675516929<br>[#39315 [Perf] scheduler: Throttle the fully-idle load snapshot publish](https://github.com/sgl-project/sglang/pull/39315) | `fix/load-snapshot-idle-publish-floor` | 17.8min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41675516929) |
| #41725341550 | `dsv4-dspark-verify-merged-mixed` | 17.7min | 8 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41725341550) |
| #41764609108<br>[#48298 [Fix] spec: Draw `SGLANG_SIMULATE_ACC_LEN` once per step from the server seed](https://github.com/sgl-project/sglang/pull/48298) | `lsyin/spec-sim-draws` | 16.6min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41764609108) |
| #41833322741<br>[#44883 [Feat] [NPU] multimodal: Enable device-side multimodal feature transport via torch_npu IPC](https://github.com/sgl-project/sglang/pull/44883) | `main` | 15.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41833322741) |
| #41771882371<br>[#47867 [Feat] [AMD] hicache: Add --hicache-mamba-size-gb to pin the HiCache Mamba host pool size](https://github.com/sgl-project/sglang/pull/47867) | `k3/hicache-mamba-size-gb` | 14.8min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41771882371) |
| #41766969309<br>[#48111 [Perf] spec: Default `SGLANG_SPEC_TP_SYNC` to `init`](https://github.com/sgl-project/sglang/pull/48111) | `dspark-auto-skip-accept-sample-sync` | 14.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41766969309) |
| #41727311458<br>[#43910 [Refactor] scheduler: Hold the waiting queue and the chunked slot in request lists](https://github.com/sgl-project/sglang/pull/43910) | `lsyin/sched-pr16` | 12.0min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41727311458) |
| #41806096601<br>[#48328 [Fix] mamba: Give a lazy boundary snapshot its own slot instead of overwriting the keep slot](https://github.com/sgl-project/sglang/pull/48328) | `lsyin/sched-pr21` | 11.5min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41806096601) |
| #41672554090<br>[#46586 [Fix] srt: Promptly abort running requests on client disconnect (#46517)](https://github.com/sgl-project/sglang/pull/46586) | `fix/chat-disconnect-abort` | 10.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41672554090) |
| #41777926812<br>[#47416 [Fix] metrics: Correct MFU/MBU bandwidth overcounting and GraniteMoE AutoTokenizer fallback](https://github.com/sgl-project/sglang/pull/47416) | `fix/mfu-decode-weight-bytes-tp-sharding` | 10.4min | 3 | multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41777926812) |
| #41695461650<br>[#46586 [Fix] srt: Promptly abort running requests on client disconnect (#46517)](https://github.com/sgl-project/sglang/pull/46586) | `fix/chat-disconnect-abort` | 9.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41695461650) |
| #41814298219<br>[#48328 [Fix] mamba: Give a lazy boundary snapshot its own slot instead of overwriting the keep slot](https://github.com/sgl-project/sglang/pull/48328) | `lsyin/sched-pr21` | 8.1min | 10 | base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41814298219) |
| #41793941982<br>[#36591 [Fix] hisparse: state-preserving retraction and recovery for DSV4](https://github.com/sgl-project/sglang/pull/36591) | `fix/hisparse-cpu-copy-retraction` | 7.4min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41793941982) |
| #41815039747<br>[#48328 [Fix] mamba: Give a lazy boundary snapshot its own slot instead of overwriting the keep slot](https://github.com/sgl-project/sglang/pull/48328) | `lsyin/sched-pr21` | 6.5min | 9 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41815039747) |
| #41765631132<br>[#40373 [Fix] json-schema: Add depth and state bounds validation](https://github.com/sgl-project/sglang/pull/40373) | `fix/json-schema-depth-explosion` | 6.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41765631132) |

---


## [Run #41833322741](https://github.com/sgl-project/sglang/actions/runs/41833322741)
- **分支**: `main`
- **总耗时**: 15.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41833322741

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587069146) |
| base-b-test-4-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587069242) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587069289) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587069343) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587069352) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587069406) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126586033499) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126586033622) |
| multimodal-gen-test-4-npu-a3 (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587067646) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41833322741/job/126587067789) |


## [Run #41828020202](https://github.com/sgl-project/sglang/actions/runs/41828020202)
- **分支**: `main`
- **总耗时**: 67.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41828020202

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005600) |
| base-b-test-4-npu-a3 / run (0) | 63.7min | 超时 | test_npu_dp_attention.py 运行超过 3600 秒超时失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005640) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005600

- **base-b-test-4-npu-a3 / run (0)**: 日志显示该用例 elapsed=3600，被标记 TIMEOUT after 3600 seconds，测试汇总 0/2 passed，进程退出码 1。属于单文件超时，非用例收集失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005640

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126567831747) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005139) |
| multimodal-gen-test-4-npu-a3 (0) | 39.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005283) |
| multimodal-gen-test-4-npu-a3 (1) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005349) |
| multimodal-gen-test-1-npu-a3 (1) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005430) |
| base-b-test-8-npu-a3 / run (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005470) |
| base-b-test-1-npu-a3 / run (0) | 43.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005667) |
| base-b-test-16-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005678) |
| base-b-test-2-npu-a3 / run (0) | 36.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41828020202/job/126569005796) |


## [Run #41826482232](https://github.com/sgl-project/sglang/actions/runs/41826482232)
- **分支**: `feat/ling3-model-pr`
- **总耗时**: 30.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41826482232

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833536) |
| base-b-test-4-npu-a3 / run (0) | 7.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833643) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833536

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833643

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126562610043) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126562610239) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833254) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833489) |
| base-b-test-1-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833524) |
| multimodal-gen-test-4-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833533) |
| multimodal-gen-test-4-npu-a3 (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833557) |
| base-b-test-16-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833569) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833721) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41826482232/job/126563833747) |


## [Run #41825612134](https://github.com/sgl-project/sglang/actions/runs/41825612134)
- **分支**: `wj/nixl-kv-packing`
- **总耗时**: 56.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41825612134

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126571525797) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器基础设施故障，非用例本身失败；此前推理仍在正常输出。
  链接: https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126571525797

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126559678209) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126559678241) |
| multimodal-gen-test-4-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831007) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831180) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831267) |
| base-b-test-16-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831273) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831306) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831562) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831628) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831726) |
| base-b-test-4-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831779) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126560831828) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126571525636) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41825612134/job/126571525902) |


## [Run #41822547633](https://github.com/sgl-project/sglang/actions/runs/41822547633)
- **分支**: `anmolgupt/nemotron3-embed-model-support`
- **总耗时**: 35.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41822547633

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 11.2min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126559777998) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 11.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126559778080) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试请求正常返回200，随后报错“Executing the custom container implementation failed”，属自托管 runner 容器环境异常，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126559777998

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示大量请求返回 200 后突然报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126559778080

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126549221859) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126549221909) |
| multimodal-gen-test-1-npu-a3 (1) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369224) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369263) |
| multimodal-gen-test-4-npu-a3 (0) | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369302) |
| multimodal-gen-test-4-npu-a3 (1) | 25.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369345) |
| base-b-test-16-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369571) |
| base-b-test-1-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369609) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369644) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369670) |
| base-b-test-2-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369675) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126550369834) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822547633/job/126559777963) |


## [Run #41822443978](https://github.com/sgl-project/sglang/actions/runs/41822443978)
- **分支**: `feature/leixin/qwen3next-qknorm-rope-v2`
- **总耗时**: 24.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41822443978

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 8.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126550000280) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126550000280

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126548858894) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126548858958) |
| multimodal-gen-test-4-npu-a3 (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549998967) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549999041) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549999042) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549999073) |
| base-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549999089) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549999227) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41822443978/job/126549999234) |


## [Run #41815039747](https://github.com/sgl-project/sglang/actions/runs/41815039747)
- **分支**: `lsyin/sched-pr21`
- **总耗时**: 6.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41815039747

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 1.2min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524934577) |
| multimodal-gen-test-1-npu-a3 (0) | 1.6min | 环境问题 | 日志被截断，未见真实错误，但作业在 checkout 后立即清理孤儿进程退出，疑似 runner 环境异常。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524934733) |
| multimodal-gen-test-1-npu-a3 (1) | 1.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524934907) |
| base-b-test-1-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524935172) |
| base-b-test-4-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524935267) |
| base-b-test-2-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524935846) |
| base-b-test-4-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524936532) |
| base-b-test-16-npu-a3 / run (0) | 1.6min | 环境问题 | 作业在 checkout 后执行 k8s 索引脚本时异常退出，未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524937126) |
| base-b-test-8-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524937267) |
| multimodal-gen-test-4-npu-a3 (0) | 1.2min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524938403) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 Node 弃用警告，最后提示未找到 diffusion-failures/ 路径、无 artifact 上传，随后进入清理阶段。缺少 unittest 报错或退出码 5 的 Traceback，无法确认是 server 启动失败还是用例本身问题，需查看完整日志中段。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524934577

- **multimodal-gen-test-1-npu-a3 (0)**: 日志仅显示 checkout 完成及 Node.js 弃用警告，随后清理孤儿进程结束，无测试执行或 Traceback。结合退出码 5 背景，可能 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），但日志未提供证据，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524934733

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524934907

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 apt 升级 libpython3.10 时出现 find: '/usr/lib/python3': No such file or directory，随后报错 Executing the custom container implementation failed，属 runner/容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524935172


- **base-b-test-2-npu-a3 / run (0)**: 日志显示安装依赖包过程中出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524935846

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 apt 安装依赖后报错 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码失败；后续仅为清理步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524936532

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 checkout 成功后运行 /home/runner/k8s/index.js，随后出现 Node 弃用警告并清理孤儿进程，作业即结束，无测试输出与退出码 5 的用例错误，疑似 runner/k8s 环境或脚本异常导致提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524937126

- **base-b-test-8-npu-a3 / run (0)**: 日志显示在解包 deb 包时出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524937267

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和清理，未出现 Traceback/RuntimeError。upload-artifact 提示 diffusion-failures/ 不存在，说明测试未产出失败产物，疑似 setUpClass 阶段 server 启动失败或作业提前退出，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524938403

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524152300) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41815039747/job/126524193257) |


## [Run #41814298219](https://github.com/sgl-project/sglang/actions/runs/41814298219)
- **分支**: `lsyin/sched-pr21`
- **总耗时**: 8.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41814298219

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522343677) |
| multimodal-gen-test-4-npu-a3 (1) | 3.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344187) |
| base-b-test-4-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344269) |
| multimodal-gen-test-4-npu-a3 (0) | 3.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344277) |
| base-b-test-1-npu-a3 / run (0) | 3.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在构建阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344513) |
| multimodal-gen-test-1-npu-a3 (0) | 3.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344629) |
| multimodal-gen-test-1-npu-a3 (1) | 3.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344925) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522345117) |
| base-b-test-8-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522345138) |
| base-b-test-2-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522345960) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522343677

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业提前结束。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344187

- **base-b-test-4-npu-a3 / run (0)**: 日志显示自定义容器实现执行失败（Executing the custom container implementation failed），提示联系自托管 runner 管理员；此前 CANN 自定义算子安装与校验均成功，失败发生在容器启动/运行阶段，属 runner 环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344269

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业提前结束。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344277

- **base-b-test-1-npu-a3 / run (0)**: 日志显示构建 xatlas 后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344513

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见明确 Traceback，但退出码5对应 unittest errors，常见于 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL）；同时 diffusion-failures/ 目录无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344629

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522344925

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 卸载 numpy/scipy 等包后报错“Executing the custom container implementation failed”，属 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522345117

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 SHA256 校验通过后报错 'Executing the custom container implementation failed'，提示联系自托管 runner 管理员，属于 CI 基础设施/容器运行时问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522345138

- **base-b-test-2-npu-a3 / run (0)**: 日志显示容器镜像拉取校验完成后报错“Executing the custom container implementation failed”，属 runner/容器环境问题，非用例代码失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126522345960

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126521314217) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41814298219/job/126521452767) |


## [Run #41813700327](https://github.com/sgl-project/sglang/actions/runs/41813700327)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 46.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41813700327

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116298) |
| base-b-test-2-npu-a3 / run (0) | 10.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116323) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116788) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520120855) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520130048) |


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116323




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126519164996) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126519165550) |
| multimodal-gen-test-1-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520115623) |
| multimodal-gen-test-4-npu-a3 (1) | 32.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116235) |
| multimodal-gen-test-4-npu-a3 (0) | 42.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116320) |
| multimodal-gen-test-1-npu-a3 (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520116488) |
| base-b-test-8-npu-a3 / run (0) | 7.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813700327/job/126520118148) |


## [Run #41813697401](https://github.com/sgl-project/sglang/actions/runs/41813697401)
- **分支**: `xinyuan/pd-peer-fingerprint`
- **总耗时**: 21.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41813697401

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520134148) |
| base-b-test-2-npu-a3 / run (0) | 11.1min | 环境问题 | test_npu_moe_dense_tp_size.py 退出码 5，setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520137270) |


- **base-b-test-2-npu-a3 / run (0)**: 该用例以 exit code 5 失败（unittest errors），按背景知识最常见原因是 setUpClass 中 sglang server 启动失败，如 host OOM 或进程被 SIGKILL；日志未给出具体 Traceback，需查看该用例详细输出确认。
  - 失败用例: npu_moe_dense_tp_size.py, npu_moe_dense_tp_size.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520137270

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126519159702) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126519160786) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520134563) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520135178) |
| multimodal-gen-test-4-npu-a3 (0) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520135420) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520136187) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520138671) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41813697401/job/126520139923) |


## [Run #41807933675](https://github.com/sgl-project/sglang/actions/runs/41807933675)
- **分支**: `lsyin/sched-pr21`
- **总耗时**: 58.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41807933675

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.4min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126509257191) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于自托管 runner 的容器运行时故障，并非用例断言失败；此前 decode 日志正常，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126509257191

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126500352821) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126500352848) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506002) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506104) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506125) |
| multimodal-gen-test-4-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506131) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506152) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506171) |
| base-b-test-16-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506225) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506250) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506256) |
| base-b-test-1-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126501506563) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126509256809) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41807933675/job/126509256855) |


## [Run #41806096601](https://github.com/sgl-project/sglang/actions/runs/41806096601)
- **分支**: `lsyin/sched-pr21`
- **总耗时**: 11.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41806096601

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494655915) |
| base-b-test-4-npu-a3 / run (1) | 8.3min | 环境问题 | 自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494655942) |
| base-b-test-16-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656050) |
| base-b-test-1-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656103) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656425) |
| base-b-test-4-npu-a3 / run (0) | 7.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656438) |
| base-b-test-2-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656805) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约7分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494655915

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，随后 server 收到 SIGTERM 优雅退出，属于自托管 runner 容器环境异常，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494655942

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器执行环境异常，非用例代码问题；随后进入清理流程，未产生测试结果。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656050

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656103

- **base-b-test-8-npu-a3 / run (0)**: 日志显示模型分片加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656425

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 sglang 服务已启动，随后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境故障，并非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656438

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在权重加载阶段（Multi-thread loading shards 0%），属于 runner/容器环境故障，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494656805

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126493548127) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126493548221) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41806096601/job/126494655993) |


## [Run #41804628820](https://github.com/sgl-project/sglang/actions/runs/41804628820)
- **分支**: `feat/rdna4-nvfp4`
- **总耗时**: 31.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41804628820

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926570) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926622) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926948) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126497896571) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126497896583) |
| multimodal-gen-test-1-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926235) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926295) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926343) |
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926406) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926479) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926521) |
| base-b-test-4-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41804628820/job/126498926569) |


## [Run #41803533568](https://github.com/sgl-project/sglang/actions/runs/41803533568)
- **分支**: `mistral-enable`
- **总耗时**: 35.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41803533568

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486061016) |
| base-b-test-1-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486061151) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126485039598) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126485039655) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486060782) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486060817) |
| multimodal-gen-test-4-npu-a3 (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486060863) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486060923) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486060933) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486060964) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486061157) |
| base-b-test-4-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803533568/job/126486061207) |


## [Run #41803475024](https://github.com/sgl-project/sglang/actions/runs/41803475024)
- **分支**: `pd-spec-kv-layout`
- **总耗时**: 23.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41803475024

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485998156) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126484847019) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126484847034) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485997928) |
| base-b-test-16-npu-a3 / run (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485997955) |
| base-b-test-1-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485998007) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485998049) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485998076) |
| base-b-test-4-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485998106) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41803475024/job/126485998348) |


## [Run #41801261120](https://github.com/sgl-project/sglang/actions/runs/41801261120)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 44.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41801261120

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | 环境问题 | 测试用例执行失败，未生成 diffusion-failures 目录，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639797) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639827) |
| multimodal-gen-test-4-npu-a3 (0) | 19.5min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639998) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620641369) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 6.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在依赖安装阶段被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126637363295) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.2min | 环境问题 | 自托管 runner 的自定义容器启动失败，作业未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126637363672) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示未找到 diffusion-failures/ 路径，无产物上传，且从 pod 复制 _temp 失败；结合退出码 5 推断 unittest 存在 errors，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639797

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约20分钟后结束。退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639827

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾显示未找到 diffusion-failures/ 目录，无产物上传；中间省略部分应含 Traceback/RuntimeError。退出码5表示 unittest errors，最常见为 setUpClass 时 server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段真实异常确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639998

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件、_temp从pod复制失败，说明用例未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620641369

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 pip 安装 evalscope 依赖时突然报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126637363295

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，runner 无法启动容器镜像，测试用例未执行，属 CI 基础设施/环境问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126637363672

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126619243395) |
| Recommend tests from coverage | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126619243518) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620639995) |
| base-b-test-16-npu-a3 / run (0) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620640228) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620640233) |
| base-b-test-2-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620640348) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620640399) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126620704153) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41801261120/job/126637363252) |


## [Run #41793941982](https://github.com/sgl-project/sglang/actions/runs/41793941982)
- **分支**: `fix/hisparse-cpu-copy-retraction`
- **总耗时**: 7.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41793941982

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 3.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531544) |
| multimodal-gen-test-4-npu-a3 (1) | 3.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531559) |
| base-b-test-8-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531588) |
| base-b-test-1-npu-a3 / run (0) | 3.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531604) |
| base-b-test-2-npu-a3 / run (0) | 3.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531642) |
| base-b-test-4-npu-a3 / run (1) | 3.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖下载阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531651) |
| base-b-test-4-npu-a3 / run (0) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531838) |
| base-b-test-16-npu-a3 / run (0) | 3.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531849) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531544

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531559

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531588

- **base-b-test-1-npu-a3 / run (0)**: 日志显示构建 sglang 及 xatlas 过程中报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531604

- **base-b-test-2-npu-a3 / run (0)**: 日志显示构建 sglang 及 xatlas 后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531642

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 正在访问 pypi 下载依赖时，报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531651

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 pip 安装依赖过程中报错 'Executing the custom container implementation failed'，属于 runner/容器环境问题，非用例代码错误，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531838

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 runner 无法启动指定的 CANN 容器镜像，属于基础设施/环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126454531849

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126453667058) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793941982/job/126453667112) |


## [Run #41793629847](https://github.com/sgl-project/sglang/actions/runs/41793629847)
- **分支**: `xinyuan/pd-peer-fingerprint`
- **总耗时**: 32.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41793629847

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.3min | 环境问题 | 容器内未安装 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473979) |

- **base-b-test-1-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明测试镜像/环境中 sglang 包未正确安装或 PYTHONPATH 未包含源码目录，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473979

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126452659370) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126452659613) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473799) |
| multimodal-gen-test-4-npu-a3 (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473847) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473909) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473935) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473943) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473974) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453473980) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453474056) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41793629847/job/126453474117) |


## [Run #41790515878](https://github.com/sgl-project/sglang/actions/runs/41790515878)
- **分支**: `lsyin/openai-misc-fixes`
- **总耗时**: 56.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41790515878

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 32.5min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126454478194) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志中 Test Summary 为 2/2 passed，两个精度用例均 PASSED，退出码正常，仅存在 Node.js 弃用警告，未发现失败或错误信息。
  链接: https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126454478194

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126445982782) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126445982787) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802200) |
| multimodal-gen-test-4-npu-a3 (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802206) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802259) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802355) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802394) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802423) |
| base-b-test-4-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802448) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802466) |
| base-b-test-1-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802472) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126446802486) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126454478084) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790515878/job/126454478218) |


## [Run #41790217718](https://github.com/sgl-project/sglang/actions/runs/41790217718)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 65.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41790217718

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126450599664) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126450599664

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126441774745) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126441774896) |
| multimodal-gen-test-4-npu-a3 (0) | 33.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454199) |
| multimodal-gen-test-4-npu-a3 (1) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454237) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454254) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454397) |
| base-b-test-16-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454422) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454427) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454448) |
| base-b-test-4-npu-a3 / run (1) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454517) |
| base-b-test-2-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442454591) |
| multimodal-gen-test-1-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126442455024) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126450599541) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41790217718/job/126450599600) |


## [Run #41780850706](https://github.com/sgl-project/sglang/actions/runs/41780850706)
- **分支**: `xpu-mooncake-ep`
- **总耗时**: 38.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41780850706

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 13.4min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126419888535) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 13.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126419888538) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 chat/completions 请求均返回 200，随后报错 'Executing the custom container implementation failed'，属于自托管 runner/容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126419888535

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在依赖安装后、测试执行前，属 runner/容器环境问题，非用例或代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126419888538

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126411928710) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126411928869) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613735) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613776) |
| base-b-test-16-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613866) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613871) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613886) |
| base-b-test-1-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613906) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613938) |
| base-b-test-4-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126412613940) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41780850706/job/126419888489) |


## [Run #41777926812](https://github.com/sgl-project/sglang/actions/runs/41777926812)
- **分支**: `fix/mfu-decode-weight-bytes-tp-sharding`
- **总耗时**: 10.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41777926812

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316712) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316755) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316825) |
| base-b-test-2-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316872) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316882) |
| base-b-test-16-npu-a3 / run (0) | 6.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片时中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316897) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403317019) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未生成产物；结合退出码5，最可能是setUpClass阶段server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316712


- **base-b-test-8-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner 容器环境/基础设施故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316825



- **base-b-test-16-npu-a3 / run (0)**: 日志显示 Multi-thread loading shards 进行到 44% 时出现 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316897


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126402654397) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126402654578) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41777926812/job/126403316713) |


## [Run #41776833181](https://github.com/sgl-project/sglang/actions/runs/41776833181)
- **分支**: `ecao/xpu_graph_context_aware_opt`
- **总耗时**: 18.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41776833181

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862842) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862895) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862898) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399189430) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399189475) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862720) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862751) |
| base-b-test-4-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862886) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862942) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41776833181/job/126399862991) |


## [Run #41772979847](https://github.com/sgl-project/sglang/actions/runs/41772979847)
- **分支**: `cryang/pr/sparsity-pd-disagg-LRU`
- **总耗时**: 34.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41772979847

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644296) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644330) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644370) |
| base-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644379) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644416) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644475) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126386874632) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126386874697) |
| multimodal-gen-test-1-npu-a3 (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644182) |
| multimodal-gen-test-4-npu-a3 (0) | 30.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644238) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644249) |
| multimodal-gen-test-1-npu-a3 (1) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772979847/job/126387644310) |


## [Run #41772067718](https://github.com/sgl-project/sglang/actions/runs/41772067718)
- **分支**: `h3-reference-max-default`
- **总耗时**: 46.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41772067718

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 31.6min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384954) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  - 失败用例: TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance, TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance, TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance, TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance
  链接: https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384954

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126383963425) |
| multimodal-gen-test-1-npu-a3 (0) | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384913) |
| multimodal-gen-test-1-npu-a3 (1) | 34.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384933) |
| multimodal-gen-test-4-npu-a3 (0) | 44.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41772067718/job/126384384944) |


## [Run #41771882371](https://github.com/sgl-project/sglang/actions/runs/41771882371)
- **分支**: `k3/hicache-mamba-size-gb`
- **总耗时**: 14.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41771882371

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 11.3min | 环境问题 | 日志中未见测试用例执行的真实错误，仅显示未找到 diffusion-failures/ 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107783) |
| multimodal-gen-test-4-npu-a3 (0) | 11.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107803) |
| multimodal-gen-test-1-npu-a3 (1) | 11.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107854) |
| base-b-test-2-npu-a3 / run (0) | 11.2min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107932) |
| base-b-test-4-npu-a3 / run (0) | 11.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107942) |
| base-b-test-1-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107965) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384108028) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384108055) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被省略，缺少 Traceback/RuntimeError 等真实错误信息；仅见 'No files were found with the provided path: diffusion-failures/'，说明失败产物目录未生成，疑似 setUpClass 阶段 server 启动失败或环境异常，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107783

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107803

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业约10分钟后结束，退出码5表明 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107854

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 Gloo 初始化正常完成后报错 'Executing the custom container implementation failed'，属 self-hosted runner 容器运行时故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107932

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Prefill 正常推理后突然报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107942

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重分片加载完成后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107965

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约11分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384108028

- **base-b-test-16-npu-a3 / run (0)**: 日志显示在加载模型分片约86%时出现“Executing the custom container implementation failed”，属于自托管 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384108055

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126383390556) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126383390692) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384107991) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41771882371/job/126384108013) |


## [Run #41769286304](https://github.com/sgl-project/sglang/actions/runs/41769286304)
- **分支**: `elastic-base`
- **总耗时**: 29.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41769286304

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 16.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814901) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moe_dense_tp_size.py, npu_moe_dense_tp_size.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814901

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375066784) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375066832) |
| multimodal-gen-test-4-npu-a3 (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814788) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814793) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814920) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814927) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814981) |
| base-b-test-1-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375814999) |
| base-b-test-16-npu-a3 / run (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41769286304/job/126375815000) |


## [Run #41767967939](https://github.com/sgl-project/sglang/actions/runs/41767967939)
- **分支**: `lsyin/sched-pr18`
- **总耗时**: 70.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41767967939

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126392047956) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在构建 sglang 元数据阶段中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126392049061) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 SHA256 校验通过后立即报错“Executing the custom container implementation failed”，属 runner/容器环境问题，非用例代码或性能回归；需联系自托管 runner 管理员排查容器实现。
  链接: https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126392047956

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码或性能回归问题，需联系自托管 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126392049061

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126370861198) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126370861233) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731189) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731312) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731438) |
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731465) |
| base-b-test-4-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731500) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731518) |
| base-b-test-1-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731529) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126371731645) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126378352588) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126378352718) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 39.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41767967939/job/126378353606) |


## [Run #41766969309](https://github.com/sgl-project/sglang/actions/runs/41766969309)
- **分支**: `dspark-auto-skip-accept-sample-sync`
- **总耗时**: 14.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41766969309

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41766969309/job/126368693880) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 server 已启动完成，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例本身失败，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41766969309/job/126368693880

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41766969309/job/126367871326) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41766969309/job/126367871548) |


## [Run #41765673077](https://github.com/sgl-project/sglang/actions/runs/41765673077)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 38.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41765673077

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150296) |
| base-b-test-16-npu-a3 / run (0) | 4.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150387) |
| base-b-test-1-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150396) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150475) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150476) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150554) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126363484484) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126363484637) |
| multimodal-gen-test-1-npu-a3 (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150181) |
| multimodal-gen-test-4-npu-a3 (0) | 32.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150185) |
| multimodal-gen-test-1-npu-a3 (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150261) |
| multimodal-gen-test-4-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765673077/job/126364150297) |


## [Run #41765631132](https://github.com/sgl-project/sglang/actions/runs/41765631132)
- **分支**: `fix/json-schema-depth-explosion`
- **总耗时**: 6.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41765631132

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765631132/job/126364139162) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41765631132/job/126364139191) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765631132/job/126363364232) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41765631132/job/126363364240) |


## [Run #41764609108](https://github.com/sgl-project/sglang/actions/runs/41764609108)
- **分支**: `lsyin/spec-sim-draws`
- **总耗时**: 16.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41764609108

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360788089) |
| base-b-test-4-npu-a3 / run (0) | 6.4min | 其他 | 日志显示测试全部通过，作业实际未失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360788180) |
| base-b-test-4-npu-a3 / run (1) | 3.8min | 其他 | 该作业未找到任何测试用例，属增量迁移预期跳过，非真实失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360788210) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360788089

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾显示 test_npu_speculative_multi_npu.py 通过，Test Summary: 1/1 passed，退出码为0，仅存在 Node.js 弃用警告，无失败错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360788180

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 No tests found for hw=NPU, suite=base-b-test-4-npu-a3, nightly=False，并注明增量迁移期间属预期跳过，Test Summary 0/0 passed，无 Traceback 或错误退出码，故非代码或环境故障。
  链接: https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360788210

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360086285) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41764609108/job/126360086368) |


## [Run #41761849462](https://github.com/sgl-project/sglang/actions/runs/41761849462)
- **分支**: `wuyaole/feat-measured-cache-writes`
- **总耗时**: 35.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41761849462

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020387) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020461) |
| base-b-test-2-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020486) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020582) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020591) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020631) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126351262907) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126351262989) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020300) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020343) |
| multimodal-gen-test-4-npu-a3 (0) | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020348) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761849462/job/126352020429) |


## [Run #41761633379](https://github.com/sgl-project/sglang/actions/runs/41761633379)
- **分支**: `feat/linker-runtime-attach`
- **总耗时**: 34.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41761633379

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408513) |
| base-b-test-2-npu-a3 / run (0) | 5.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408637) |


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408637

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126350566572) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126350566645) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408395) |
| base-b-test-1-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408462) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408465) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408526) |
| base-b-test-4-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408532) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41761633379/job/126351408580) |


## [Run #41760392663](https://github.com/sgl-project/sglang/actions/runs/41760392663)
- **分支**: `jacob/glm53-flash-moe-router-kda`
- **总耗时**: 47.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41760392663

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 10.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382804) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382804

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126346613254) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126346613384) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382701) |
| multimodal-gen-test-1-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382739) |
| multimodal-gen-test-4-npu-a3 (0) | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382748) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382795) |
| base-b-test-16-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382852) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382865) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347382970) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347383013) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41760392663/job/126347383171) |


## [Run #41759510680](https://github.com/sgl-project/sglang/actions/runs/41759510680)
- **分支**: `ecao/cpu_graph_prefill2`
- **总耗时**: 88.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41759510680

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.1min | 其他 | 日志显示测试全部通过，作业失败疑似清理阶段告警或退出码异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126357495076) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志中2/2用例均PASSED，无Traceback或RuntimeError；仅出现'Failed to copy _temp from pod'告警和Node.js弃用警告，未见明确失败原因，需查看被省略的中间日志确认退出码来源。
  链接: https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126357495076

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126343720313) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126343720464) |
| multimodal-gen-test-1-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591503) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591512) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591586) |
| multimodal-gen-test-4-npu-a3 (1) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591613) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591626) |
| base-b-test-4-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591631) |
| base-b-test-4-npu-a3 / run (1) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591691) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591726) |
| base-b-test-2-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344591788) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126344593183) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126357495024) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41759510680/job/126357495047) |


## [Run #41756297347](https://github.com/sgl-project/sglang/actions/runs/41756297347)
- **分支**: `yanbin/beam-lora-main`
- **总耗时**: 65.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41756297347

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 12.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126341433481) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126341433481

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126333216641) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126333216706) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083778) |
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083830) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083833) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083840) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083908) |
| base-b-test-16-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083950) |
| base-b-test-4-npu-a3 / run (1) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334083977) |
| base-b-test-8-npu-a3 / run (0) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334084017) |
| base-b-test-4-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334084088) |
| base-b-test-1-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126334084151) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126341433503) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41756297347/job/126341433548) |


## [Run #41731704756](https://github.com/sgl-project/sglang/actions/runs/41731704756)
- **分支**: `lsyin/sched-pr16`
- **总耗时**: 53.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41731704756

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126262568075) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试请求正常返回 200 OK 后，出现 'Executing the custom container implementation failed'，属于自托管 runner 容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126262568075

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126251113072) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126251484172) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126251484182) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590438) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590461) |
| base-b-test-4-npu-a3 / run (1) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590554) |
| base-b-test-4-npu-a3 / run (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590631) |
| base-b-test-16-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590640) |
| base-b-test-1-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590704) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590826) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126252590831) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126262567950) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41731704756/job/126262567992) |


## [Run #41728983717](https://github.com/sgl-project/sglang/actions/runs/41728983717)
- **分支**: `lsyin/sched-pr16`
- **总耗时**: 19.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41728983717

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 15.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049318) |
| base-b-test-1-npu-a3 / run (0) | 14.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在初始化阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049406) |
| base-b-test-4-npu-a3 / run (0) | 15.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049440) |
| base-b-test-16-npu-a3 / run (0) | 15.4min | 超时 | Scheduler 看门狗超时导致容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049454) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在权重加载阶段，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049318

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 Init parallel 完成后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049406

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题；此前 server 已初始化，随后容器执行异常退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049440

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP8 EP8 Scheduler watchdog timeout（watchdog_timeout=300，soft=True），随后报错“Executing the custom container implementation failed”，作业因调度器看门狗超时失败，属超时类问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049454

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126241812896) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126241813078) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049096) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049210) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049513) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41728983717/job/126243049522) |


## [Run #41727311458](https://github.com/sgl-project/sglang/actions/runs/41727311458)
- **分支**: `lsyin/sched-pr16`
- **总耗时**: 12.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41727311458

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 6.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238056346) |
| base-b-test-16-npu-a3 / run (0) | 6.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057608) |
| base-b-test-4-npu-a3 / run (0) | 6.3min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057713) |
| base-b-test-8-npu-a3 / run (0) | 5.3min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057734) |
| base-b-test-1-npu-a3 / run (0) | 5.3min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057748) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057853) |
| base-b-test-4-npu-a3 / run (1) | 5.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057882) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败且未生成失败产物。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238056346

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载过程中报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057608

- **base-b-test-4-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed”，属于自托管 runner 的容器环境异常，并非用例断言失败；测试在 DP attention 用例执行中突然中断，建议联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057713

- **base-b-test-8-npu-a3 / run (0)**: 日志显示模型加载正常后报错“Executing the custom container implementation failed”，属 self-hosted runner 容器实现故障，非用例代码问题，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057734

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已正常启动并 ready，随后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057748

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务已正常启动（Uvicorn 监听 11000），随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057853

- **base-b-test-4-npu-a3 / run (1)**: 日志显示服务已启动并进入 batch capture 阶段，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238057882

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126236269367) |
| base-a-test-npu | 3.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126236269558) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41727311458/job/126238056373) |


## [Run #41725341550](https://github.com/sgl-project/sglang/actions/runs/41725341550)
- **分支**: `dsv4-dspark-verify-merged-mixed`
- **总耗时**: 17.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41725341550

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 13.3min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256300) |
| multimodal-gen-test-4-npu-a3 (0) | 13.3min | 环境问题 | 日志中未见测试用例的 Traceback，仅显示 diffusion-failures 目录无文件可上传，作业失败原因不明确。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256308) |
| multimodal-gen-test-4-npu-a3 (1) | 13.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256382) |
| base-b-test-1-npu-a3 / run (0) | 13.3min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256455) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | 环境问题 | 自定义容器执行失败，作业在容器内运行阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256596) |
| base-b-test-2-npu-a3 / run (0) | 13.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256689) |
| base-b-test-4-npu-a3 / run (0) | 13.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256723) |
| multimodal-gen-test-1-npu-a3 (0) | 13.3min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230257098) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试未产出失败样本；结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256300

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，缺少真实错误信息；仅见 artifact 路径 diffusion-failures/ 无文件，无法确认是 server 启动失败还是其他原因，需查看完整日志中的 Traceback/退出码。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256308

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256382

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属 self-hosted runner 容器执行故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256455

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed'，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256596

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员。作业在容器启动阶段失败，未进入用例执行，与代码或精度无关，属 runner/容器环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256689

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非用例断言失败；此前推理服务仍在正常输出 prefill/decode 日志，随后容器执行失败导致作业终止，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256723

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 路径，说明测试用例在 setUpClass 阶段即失败（退出码 5 对应 unittest errors），常见原因为 sglang server 启动失败（host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230257098

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126228882282) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126228882575) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256612) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41725341550/job/126230256771) |


## [Run #41722043068](https://github.com/sgl-project/sglang/actions/runs/41722043068)
- **分支**: `lsyin/sched-pr16`
- **总耗时**: 36.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41722043068

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 8.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126230570933) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126230570979) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 pip 安装依赖过程中报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126230570933

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示容器内服务正常返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner/容器基础设施异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126230570979

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126217309035) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126217309168) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800095) |
| base-b-test-1-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800209) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800211) |
| base-b-test-16-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800415) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800440) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800548) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800602) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126218800653) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41722043068/job/126230570960) |


## [Run #41721874254](https://github.com/sgl-project/sglang/actions/runs/41721874254)
- **分支**: `lsyin/multi-tokenizer-dedup`
- **总耗时**: 21.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41721874254

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 7.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126223501373) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例断言失败或性能回归；此前 server 请求均返回 200，flush_cache 也成功。
  链接: https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126223501373

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126216474366) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126216990169) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126216990296) |
| base-b-test-2-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126218160087) |
| base-b-test-4-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126218160096) |
| base-b-test-4-npu-a3 / run (1) | 6.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126218160102) |
| base-b-test-1-npu-a3 / run (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41721874254/job/126218160361) |


## [Run #41714723081](https://github.com/sgl-project/sglang/actions/runs/41714723081)
- **分支**: `fix/retract-keeps-new-token-ratio`
- **总耗时**: 26.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41714723081

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193741082) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193741082

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126191955387) |
| base-a-test-npu | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126191955408) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740582) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740607) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740645) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740648) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740693) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740718) |
| base-b-test-16-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41714723081/job/126193740796) |


## [Run #41710208047](https://github.com/sgl-project/sglang/actions/runs/41710208047)
- **分支**: `dp-attn-phase-lockstep`
- **总耗时**: 59.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41710208047

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126190249185) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126190249185

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126176270821) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126176271142) |
| multimodal-gen-test-1-npu-a3 (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726324) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726375) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726484) |
| multimodal-gen-test-1-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726520) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726544) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726556) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726588) |
| multimodal-gen-test-4-npu-a3 (0) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726596) |
| base-b-test-16-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726617) |
| base-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126177726780) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126190248957) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41710208047/job/126190249072) |


## [Run #41705053416](https://github.com/sgl-project/sglang/actions/runs/41705053416)
- **分支**: `comm-push-epoch-protocol`
- **总耗时**: 37.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41705053416

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | 环境问题 | 作业日志中未见测试用例执行，仅显示产物目录 diffusion-failures/ 不存在、从 pod 复制 _temp 失败，疑似容器/pod 环境异常导致测试未产出结果。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286687) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126172994936) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126172995075) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，无 Traceback 或退出码信息；仅见 'No files were found with the provided path: diffusion-failures/' 与 'Failed to copy _temp from pod'，说明测试产物未生成、pod 复制失败，属环境/基础设施问题，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286687

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载至86%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码或精度问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126172994936

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示服务端请求正常返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126172995075

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126158900281) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126158900446) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286422) |
| multimodal-gen-test-1-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286459) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286463) |
| base-b-test-16-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286520) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286534) |
| multimodal-gen-test-4-npu-a3 (1) | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286549) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286558) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286577) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126160286659) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41705053416/job/126172995087) |


## [Run #41700041966](https://github.com/sgl-project/sglang/actions/runs/41700041966)
- **分支**: `comm-push-epoch-protocol`
- **总耗时**: 33.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41700041966

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158646) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126155685875) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126155686000) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 3.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126155686037) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示用例以退出码5结束（unittest errors），且未生成 diffusion-failures/ 目录产物。最常见原因是 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略部分的 Traceback/RuntimeError 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158646

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 SHA256 校验通过后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126155685875

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed'，发生在 pip 卸载/安装依赖过程中，属 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126155686000

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在容器启动阶段，尚未进入测试用例执行，属 runner/容器环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126155686037

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126140974796) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126140974814) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158572) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158630) |
| base-b-test-1-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158766) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158771) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142158865) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142159098) |
| base-b-test-2-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142159131) |
| base-b-test-4-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142159150) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41700041966/job/126142159414) |


## [Run #41696104415](https://github.com/sgl-project/sglang/actions/runs/41696104415)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 36.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41696104415

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392438) |
| base-b-test-2-npu-a3 / run (0) | 5.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392448) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392438

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392448

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126127784754) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126128296158) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126128296298) |
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392072) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392084) |
| multimodal-gen-test-1-npu-a3 (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392125) |
| multimodal-gen-test-4-npu-a3 (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392175) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392403) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392465) |
| base-b-test-16-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392468) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41696104415/job/126129392674) |


## [Run #41695461650](https://github.com/sgl-project/sglang/actions/runs/41695461650)
- **分支**: `fix/chat-disconnect-abort`
- **总耗时**: 9.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41695461650

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41695461650/job/126126500125) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41695461650/job/126126500125

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41695461650/job/126124680307) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41695461650/job/126125135394) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41695461650/job/126125135493) |


## [Run #41691550158](https://github.com/sgl-project/sglang/actions/runs/41691550158)
- **分支**: `followup/qwen35-megakernel-runtime-v3-runtime`
- **总耗时**: 30.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41691550158

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 25.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113147929) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 3.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126125311374) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.3min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，作业在容器启动阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126125311450) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126125311539) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业约25分钟后结束，diffusion-failures目录无文件，未上传artifact。退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113147929

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 reflink 操作不支持（os error 95）后出现 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码或精度问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126125311374

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 CANN 自定义算子安装成功后，报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，测试尚未开始执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126125311450

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 runner 无法启动指定的 CANN 容器镜像，属于 CI 基础设施/环境问题，尚未进入用例执行阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126125311539

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126111140372) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126111559348) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126111559392) |
| multimodal-gen-test-1-npu-a3 (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113147853) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113147866) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148049) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148050) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148222) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148243) |
| base-b-test-1-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148271) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148386) |
| base-b-test-4-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41691550158/job/126113148499) |


## [Run #41681564052](https://github.com/sgl-project/sglang/actions/runs/41681564052)
- **分支**: `cryang/pr/sparsity-pd-disagg-LRU`
- **总耗时**: 34.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41681564052

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064481) |
| base-b-test-8-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064518) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064540) |
| base-b-test-2-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064574) |
| base-b-test-4-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064618) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064810) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| check-changes | 0.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126076272205) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126076740481) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126076740684) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064117) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064125) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064206) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41681564052/job/126078064249) |


## [Run #41676141466](https://github.com/sgl-project/sglang/actions/runs/41676141466)
- **分支**: `perf/kandinsky6-fused-elementwise`
- **总耗时**: 5.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41676141466

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| pr-gate / pr-gate | 5.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41676141466/job/126057322630) |



## [Run #41675516929](https://github.com/sgl-project/sglang/actions/runs/41675516929)
- **分支**: `fix/load-snapshot-idle-publish-floor`
- **总耗时**: 17.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41675516929

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 13.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646103) |
| base-b-test-1-npu-a3 / run (0) | 14.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646106) |
| base-b-test-4-npu-a3 / run (0) | 14.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646421) |
| base-b-test-2-npu-a3 / run (0) | 14.0min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646428) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示测试本身已通过（Ran 1 test, OK），随后启动 sglang server 时出现 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646103

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载刚开始（Multi-thread loading shards 0%），随即报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner/容器环境故障，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646106

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在运行 test_npu_w4a4_quantization.py 期间，属 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646421

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646428

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126055284828) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126055284965) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056645838) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646209) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646242) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41675516929/job/126056646249) |


## [Run #41672554090](https://github.com/sgl-project/sglang/actions/runs/41672554090)
- **分支**: `fix/chat-disconnect-abort`
- **总耗时**: 10.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41672554090

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41672554090/job/126050247792) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41672554090/job/126044886630) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41672554090/job/126044886664) |
| base-b-test-2-npu-a3 / run (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41672554090/job/126046399053) |


## [Run #41630759939](https://github.com/sgl-project/sglang/actions/runs/41630759939)
- **分支**: `feat/dsv41-packed-main-kv`
- **总耗时**: 21.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41630759939

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126336547731) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126336547741) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126336547786) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-2-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329715798) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329715850) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329715931) |
| multimodal-gen-test-4-npu-a3 (0) | 36.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329716741) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329716829) |
| base-b-test-16-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329716926) |
| multimodal-gen-test-1-npu-a3 (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329717020) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329717078) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329717138) |
| multimodal-gen-test-1-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329717381) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329717681) |
| multimodal-gen-test-4-npu-a3 (1) | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41630759939/job/126329717738) |


---
*Auto-generated by ci_monitor.py*