# NPU CI 执行监控（2026-11-05）
**生成时间**: 2026-11-06 09:41
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-05 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 183

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1829 个 | 失败 216 个 | 成功 Job 平均耗时 14.2min
- **Run 执行情况**: 成功 121 个 | 失败 62 个 | 成功 Run 平均耗时 66.7min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 71.4min | #42025942121 | [job link](https://github.com/sgl-project/sglang/actions/runs/42025942121/job/127270784613) |
| base-b-test-4-npu-a3 / run (0) | 60.0min | #42025942121 | [job link](https://github.com/sgl-project/sglang/actions/runs/42025942121/job/127241337372) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 52.2min | #41950224030 | [job link](https://github.com/sgl-project/sglang/actions/runs/41950224030/job/127000124818) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 52.1min | #41993688205 | [job link](https://github.com/sgl-project/sglang/actions/runs/41993688205/job/127143204230) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 48.5min | #41943137686 | [job link](https://github.com/sgl-project/sglang/actions/runs/41943137686/job/126978507047) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.8min | #42030352848 | [job link](https://github.com/sgl-project/sglang/actions/runs/42030352848/job/127268424132) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.6min | #41970890950 | [job link](https://github.com/sgl-project/sglang/actions/runs/41970890950/job/127068088500) |
| multimodal-gen-test-4-npu-a3 (0) | 45.6min | #41864283856 | [job link](https://github.com/sgl-project/sglang/actions/runs/41864283856/job/126695619919) |
| base-b-test-2-npu-a3 / run (0) | 44.9min | #42025942121 | [job link](https://github.com/sgl-project/sglang/actions/runs/42025942121/job/127241337409) |
| multimodal-gen-test-4-npu-a3 (0) | 44.6min | #41944747212 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944747212/job/126975007896) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 35.4min | #41943510711 | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859188) |
| multimodal-gen-test-4-npu-a3 (0) | 25.4min | #42013140381 | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927294) |
| base-b-test-2-npu-a3 / run (0) | 24.1min | #41796589214 | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856673) |
| multimodal-gen-test-1-npu-a3 (0) | 22.4min | #42009851464 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268299) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | #41990375586 | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192526) |
| base-b-test-4-npu-a3 / run (0) | 21.5min | #42021480795 | [job link](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127226379123) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | #42009851464 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268518) |
| multimodal-gen-test-1-npu-a3 (1) | 20.5min | #42009851464 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268195) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | #42009851464 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268210) |
| base-b-test-16-npu-a3 / run (0) | 20.4min | #42009851464 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268645) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-2-npu-a3 / run (0) | 146 | 112 | 6 | 16 | 12 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287186107)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035074)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192526)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761454)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085331) |
| base-b-test-4-npu-a3 / run (0) | 150 | 121 | 2 | 15 | 12 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127226379123)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225915244) |
| base-b-test-1-npu-a3 / run (0) | 144 | 117 | 2 | 14 | 11 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035749)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41938193052/job/126952998776) |
| base-b-test-4-npu-a3 / run (1) | 150 | 124 | 3 | 13 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938264)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470598)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693234180) |
| base-b-test-8-npu-a3 / run (0) | 116 | 98 | 3 | 9 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442649)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760086044)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233983) |
| base-b-test-16-npu-a3 / run (0) | 117 | 94 | 0 | 11 | 12 | - |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 92 | 81 | 3 | 2 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127262950290)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127208407501)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127234980836) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 168 | 160 | 2 | 0 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127284515722)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127062123462) |
| multimodal-gen-test-1-npu-a3 (1) | 91 | 81 | 1 | 0 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697768) |
| multimodal-gen-test-1-npu-a3 (0) | 91 | 81 | 1 | 0 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697863) |
| multimodal-gen-test-4-npu-a3 (1) | 132 | 121 | 1 | 0 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697748) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_pd_disaggregation.py` | 32 | 28 | 4 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127226379123)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938264)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470598) |
| `npu_mla_fia_hicache_bf16.py` | 29 | 26 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287186107)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761454)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085331) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 34 | 31 | 3 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442649)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760086044)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233983) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 9 | 7 | 2 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127284515722)<br>[base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127062123462) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 6 | 4 | 2 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127262950290)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127208407501) |
| `npu_hicache_mha.py` | 30 | 29 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035749) |
| `npu_expert_distribution_recorder_mode.py` | 24 | 23 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035074) |
| `npu_dp_attention.py` | 29 | 28 | 1 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225915244) |
| `npu_return_indexer_topk_deepseek_v4.py` | 24 | 23 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192526) |
| `npu_return_indexer_topk_glm52.py` | 22 | 21 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856673) |
| `ernie_image_t2i_1npu` | 27 | 26 | 1 | [multimodal-gen-test-1-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449091) |
| `dspark_npu_dispatch.py` | 22 | 21 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/41938193052/job/126952998776) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #42003156015<br>[#46483 [Perf] [NPU] attention: Avoid CPU sequence length synchronization for Kimi K3](https://github.com/sgl-project/sglang/pull/46483) | `perf/npuseqlens-false-k3` | 97.5min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42003156015) |
| #42009583209 | `yihou/kv-metrics-nonblocking-20261027` | 69.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42009583209) |
| #41969320337<br>[#47984 [Fix] mem_cache: Chunk MambaPool temporal state copy to avoid OOM spike](https://github.com/sgl-project/sglang/pull/47984) | `fix-mamba-copy-from-temporal-oom` | 68.4min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41969320337) |
| #42033446434<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 63.6min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42033446434) |
| #41805487696<br>[#33873 [Perf] [AMD] kimi-k2.5: Fuse MLA value projection with MXFP4 output quantization](https://github.com/sgl-project/sglang/pull/33873) | `yuychang/rocm-kimi-mla-fusion-mxfp4` | 61.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41805487696) |
| #41931726281<br>[#48328 [Fix] mamba: Give a lazy boundary snapshot its own slot instead of overwriting the keep slot](https://github.com/sgl-project/sglang/pull/48328) | `lsyin/sched-pr21` | 57.2min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41931726281) |
| #41984911470<br>[#47309 [Perf] [AMD] dsa: Row-split the DCP indexer, run owned sparse MLA on the aiter asm kernel, and pipeline the a2a](https://github.com/sgl-project/sglang/pull/47309) | `amd/dcp-owned-by-row` | 53.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41984911470) |
| #41969675523<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 47.2min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41969675523) |
| #41964964623<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 46.2min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41964964623) |
| #42028942178<br>[#46953 [Feat] weight_cache: Add the vmm_fd transport](https://github.com/sgl-project/sglang/pull/46953) | `weight-cache-vmm-fd-upstream` | 43.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42028942178) |
| #41961638538 | `pr/minimax-h3-vae-fp8-decoder` | 43.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41961638538) |
| #41796589214<br>[#47040 [Fix] [AMD] hicache: Size the Mamba host share by persistent checkpoint bytes](https://github.com/sgl-project/sglang/pull/47040) | `k3/hicache-mamba-host-pool` | 42.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41796589214) |
| #41943510711<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 42.1min | 3 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41943510711) |
| #41979605326 | `feat/hicache-mamba-request-end` | 41.4min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41979605326) |
| #41885188470<br>[#48433 [Feat] weight_update: Let platforms serve weight transports through /plugin_weight_update](https://github.com/sgl-project/sglang/pull/48433) | `hejian/plugin-weight-update` | 40.8min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41885188470) |
| #41950749707<br>[#45560 [elastic ep] live serving during scale](https://github.com/sgl-project/sglang/pull/45560) | `qkang/elastic-ep-mooncake-scale-down` | 39.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41950749707) |
| #41956296204<br>[#47984 [Fix] mem_cache: Chunk MambaPool temporal state copy to avoid OOM spike](https://github.com/sgl-project/sglang/pull/47984) | `fix-mamba-copy-from-temporal-oom` | 39.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41956296204) |
| #41990375586<br>[#48491 [Refactor] scheduler: Release every PD disaggregation exit through RequestRetirer](https://github.com/sgl-project/sglang/pull/48491) | `lsyin/sched-pr22` | 38.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41990375586) |
| #41955745984<br>[#47308 [Feat] scheduler: add mixed-prefill resource controls](https://github.com/sgl-project/sglang/pull/47308) | `wuyaole/fix-prefill-reservation-budget` | 38.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41955745984) |
| #41959745764<br>[#27267 [Feat] mem_cache: Add hugepage preflight and allocation modes for host pools](https://github.com/sgl-project/sglang/pull/27267) | `hicache-host-memory-preflight` | 37.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41959745764) |
| #41863403215<br>[#48415 [Feat] model: Add basic Kimi-K3.1 support (NV, AMD)](https://github.com/sgl-project/sglang/pull/48415) | `kimi-k3.1-support` | 36.9min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41863403215) |
| #42038225096<br>[#48654 [Fix] scheduler: Match arrival prefixes on every PP stage](https://github.com/sgl-project/sglang/pull/48654) | `codex/pp-arrival-match-main` | 36.8min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42038225096) |
| #41949995195<br>[#48468 [Chore] [NVIDIA] deps: Bump FlashInfer to 0.7.3 and migrate the NVLink one-sided all-to-all to flashinfer.moe_ep](https://github.com/sgl-project/sglang/pull/48468) | `flashinfer-0.7.3-moe-ep` | 36.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41949995195) |
| #41893040645<br>[#47308 [Feat] scheduler: add mixed-prefill resource controls](https://github.com/sgl-project/sglang/pull/47308) | `wuyaole/fix-prefill-reservation-budget` | 36.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41893040645) |
| #41895182570<br>[#37273 [Feat] scheduler: Add opt-in DP-attention phase lockstep](https://github.com/sgl-project/sglang/pull/37273) | `dp-attn-phase-lockstep` | 35.1min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41895182570) |
| #42013140381 | `k31-decode-moe-main` | 34.3min | 4 | multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42013140381) |
| #41971072852 | `oss-sync-5f33eae5cc` | 33.8min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41971072852) |
| #41880178049 | `feat/hicache-mamba-request-end` | 33.8min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41880178049) |
| #42021251629<br>[#46663 [Fix] gemma4: Fix Bolt E4B and Gemma4 prefill CUDA graphs](https://github.com/sgl-project/sglang/pull/46663) | `fix/gemma4-shared-kv-graphs` | 33.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42021251629) |
| #41861557871<br>[#48415 [Feat] model: Add basic Kimi-K3.1 support (NV, AMD)](https://github.com/sgl-project/sglang/pull/48415) | `kimi-k3.1-support` | 32.9min | 9 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41861557871) |
| #42009851464<br>[#48074 [Feat] [Intel] video_decoder: Decode video on the XPU media engine via torchcodec-xpu](https://github.com/sgl-project/sglang/pull/48074) | `xpu-video-decode` | 32.3min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42009851464) |
| #42024348292<br>[#43279 [Feat] wan2.2-s2v: Add Wan2.2-S2V-14B speech-to-video (port of #21609)](https://github.com/sgl-project/sglang/pull/43279) | `wan2_s2v_port` | 31.7min | 3 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42024348292) |
| #41959656555<br>[#48043 [Perf] [AMD] qwen3: Fuse the 1x128 FP8 input quant into RMSNorm and SiLU-and-mul for block-FP8 linears on gfx950](https://github.com/sgl-project/sglang/pull/48043) | `feature/leixin/qwen3-blockfp8-quant-fusion` | 31.4min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41959656555) |
| #41982168899<br>[#48501 [Feat] dsa: Kernel prerequisites for a DCP-sharded indexer](https://github.com/sgl-project/sglang/pull/48501) | `lsyin/indexer-dcp-prep` | 30.7min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41982168899) |
| #42021480795<br>[#44615 [Perf] NIXL: KV packing for TP-heterogeneous transfer (Muse Spark Open)](https://github.com/sgl-project/sglang/pull/44615) | `wj/nixl-kv-packing` | 28.7min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42021480795) |
| #41917552869 | `oss-sync-5ac6bc3c22` | 25.0min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41917552869) |
| #42039341941<br>[#46586 [Fix] srt: Promptly abort running requests on client disconnect (#46517)](https://github.com/sgl-project/sglang/pull/46586) | `fix/chat-disconnect-abort` | 23.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42039341941) |
| #42000458797<br>[#45388 [Fix] [CPU] qk_norm: Fall back for BF16 without AVX-512 BF16](https://github.com/sgl-project/sglang/pull/45388) | `main_cpu` | 22.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42000458797) |
| #41988146075<br>[#48491 [Refactor] scheduler: Release every PD disaggregation exit through RequestRetirer](https://github.com/sgl-project/sglang/pull/48491) | `lsyin/sched-pr22` | 22.2min | 6 | multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41988146075) |
| #41944363897<br>[#48481 [Fix] kimi-k3: Validate message-level tools and let a forced call override JSON response_format](https://github.com/sgl-project/sglang/pull/48481) | `lsyin/kimi-k3-request-checks` | 21.1min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41944363897) |
| #41944346810<br>[#48480 [Fix] kimi-k3: Make tool_choice required and none grammars end the turn](https://github.com/sgl-project/sglang/pull/48480) | `lsyin/kimi-k3-forced-tool-call` | 21.1min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41944346810) |
| #41958340319<br>[#47052 [Perf] [AMD] qwen3: Fuse prefill QK-norm + RoPE on ROCm with the JIT qknorm_rope kernel](https://github.com/sgl-project/sglang/pull/47052) | `perf/qwen3-hip-qknorm-rope` | 20.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41958340319) |
| #41941146572<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 20.5min | 9 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41941146572) |
| #42001422237<br>[#46483 [Perf] [NPU] attention: Avoid CPU sequence length synchronization for Kimi K3](https://github.com/sgl-project/sglang/pull/46483) | `perf/npuseqlens-false-k3` | 17.8min | 7 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42001422237) |
| #41962327668 | `add_mxfp8_xpu_support` | 15.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41962327668) |
| #41963525366<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 15.4min | 4 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41963525366) |
| #41909156736<br>[#48366 [Refactor] kernels/diffusion/tests: Prune new dead code and make silently skipped tests run](https://github.com/sgl-project/sglang/pull/48366) | `bbuf/cleanup-round2` | 13.3min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41909156736) |
| #41996717847<br>[#47469 [Perf] [NVIDIA] attention: Add opt-in LiteTopK prefill indexer top-k for DSA (FP8) and DeepSeek-V4.1 (FP4) on SM100](https://github.com/sgl-project/sglang/pull/47469) | `litetopk-prefill` | 12.7min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41996717847) |
| #41985688848<br>[#44399 [Feat] gemma4: per-layer attention backend](https://github.com/sgl-project/sglang/pull/44399) | `feat/fa3-fa4-hybrid-gemma4` | 12.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41985688848) |
| #41980950444<br>[#48501 [Feat] dsa: Kernel prerequisites for a DCP-sharded indexer](https://github.com/sgl-project/sglang/pull/48501) | `lsyin/indexer-dcp-prep` | 11.7min | 5 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41980950444) |
| #41997636084<br>[#37909 [Fix] disaggregation: Fix Gloo collective mismatch in disagg prefill bootstrap when TP/CP > 1](https://github.com/sgl-project/sglang/pull/37909) | `align-queue-per-rank` | 9.9min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/41997636084) |
| #41951230115<br>[#45534 [Fix] [NVIDIA] DeepSeek-v4.1: scatter the replay tail before the prefill CP gather with DSpark](https://github.com/sgl-project/sglang/pull/45534) | `fix/dsv41-cuda-cp-replay-tail` | 9.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41951230115) |
| #42032893282<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 8.9min | 6 | base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42032893282) |
| #41938193052<br>[#37472 [Fix] dspark: Keep verify bookkeeping in range for rows without candidates](https://github.com/sgl-project/sglang/pull/37472) | `dspark-vocab-verify-guards` | 8.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41938193052) |
| #42052447066 | `k31-decode-moe-main` | 7.8min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42052447066) |
| #41956917380 | `oss-sync-5a3f5544c6` | 6.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41956917380) |
| #41964313373<br>[#46486 [Perf] [AMD] dsa: Run the GLM-5 decode MLA chain as Gluon kernels on gfx950](https://github.com/sgl-project/sglang/pull/46486) | `feature/amd-glm5-dsa-mla-decode-gfx950` | 6.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41964313373) |
| #41957259580<br>[#48404 [Fix] eplb: reject incompatible recorder modes](https://github.com/sgl-project/sglang/pull/48404) | `fix/eplb-recorder-mode-48403` | 6.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41957259580) |
| #41958044865<br>[#46499 [Feat] UnifiedL3: support mooncake storage backend](https://github.com/sgl-project/sglang/pull/46499) | `page-unified/mooncake-storage` | 6.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41958044865) |
| #41959086008<br>[#43480 [Perf] [AMD] DSV4.1: Fuse wo_b's GEMM with its all-reduce via mori cco on gfx950](https://github.com/sgl-project/sglang/pull/43480) | `xiangch/fused-wo-b-gemm-ar-main` | 5.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41959086008) |
| #41967254543 | `bench-serving-per-run-accept-length` | 5.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41967254543) |
| #41955019901<br>[#34394 [Perf] [AMD] dsa: Merge indexer wk and weights_proj](https://github.com/sgl-project/sglang/pull/34394) | `jacob/glm5-dsa-indexer-aiter-fuse` | 5.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41955019901) |

---


## [Run #42052447066](https://github.com/sgl-project/sglang/actions/runs/42052447066)
- **分支**: `k31-decode-moe-main`
- **总耗时**: 7.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42052447066

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 3.5min | 环境问题 | 日志中未见测试用例执行，仅显示 artifact 路径 diffusion-failures/ 无文件可上传，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333789451) |
| multimodal-gen-test-1-npu-a3 (0) | 3.5min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333789607) |
| multimodal-gen-test-4-npu-a3 (0) | 3.3min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333789659) |
| multimodal-gen-test-4-npu-a3 (1) | 3.3min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790223) |
| base-b-test-1-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装 Rust 工具链时中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790334) |
| base-b-test-2-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790339) |
| base-b-test-4-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在容器启动阶段即报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790442) |
| base-b-test-16-npu-a3 / run (0) | 3.2min | 环境问题 | 自定义容器执行失败，作业在容器启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790463) |
| base-b-test-8-npu-a3 / run (0) | 3.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在解压 custom-ops 后中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790512) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器初始化阶段中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790646) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 Node 弃用警告，最后提示 diffusion-failures/ 目录无文件、无 artifact 上传，随后进入 cleanup。缺少 unittest 退出码 5 及 Traceback 等真实错误信息，无法确认是 server 启动失败还是其他原因，需查看完整日志中省略的测试执行段。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333789451

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，缺少真实错误信息。仅见 'No files were found with the provided path: diffusion-failures/'，说明测试未产生失败产物目录，可能用例未运行或提前退出；需查看完整日志中的 Traceback/RuntimeError 确认是否为 setUpClass 阶段 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333789607

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 artifact 上传提示“No files were found with the provided path: diffusion-failures/”，没有测试脚本输出或 Traceback，无法确认具体失败原因，疑似环境或脚本未产生预期产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333789659

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，可见部分只有 runner 初始化、action 下载和清理，未出现 Traceback 或退出码 5 的测试输出；upload-artifact 提示 diffusion-failures/ 不存在，说明测试产物未生成，疑似 setUpClass 阶段 server 启动失败或作业未真正运行测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790223

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 rustup 下载组件过程中报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790334

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790339

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在依赖安装后、测试执行前，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790442

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错 'Executing the custom container implementation failed'，属 self-hosted runner 容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790463

- **base-b-test-8-npu-a3 / run (0)**: 日志显示解压 CANN-custom_ops 后立即报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790512

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 apt 安装依赖后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127333790646

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127332146081) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42052447066/job/127332146188) |


## [Run #42039341941](https://github.com/sgl-project/sglang/actions/runs/42039341941)
- **分支**: `fix/chat-disconnect-abort`
- **总耗时**: 23.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42039341941

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287186107) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287186107

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127285945798) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127285945950) |
| base-b-test-4-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287185891) |
| base-b-test-4-npu-a3 / run (1) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287185986) |
| base-b-test-1-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42039341941/job/127287186077) |


## [Run #42038225096](https://github.com/sgl-project/sglang/actions/runs/42038225096)
- **分支**: `codex/pp-arrival-match-main`
- **总耗时**: 36.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42038225096

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 12.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035074) |
| base-b-test-1-npu-a3 / run (0) | 10.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035749) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035074

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035749

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127282132936) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127282132957) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283034922) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283034957) |
| base-b-test-8-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035066) |
| base-b-test-16-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035164) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035219) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42038225096/job/127283035403) |


## [Run #42033446434](https://github.com/sgl-project/sglang/actions/runs/42033446434)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 63.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42033446434

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 8.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127284515722) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127284515795) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127284515722


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127268261372) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127268261424) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269231749) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269231877) |
| multimodal-gen-test-4-npu-a3 (0) | 37.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269231934) |
| base-b-test-16-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269231968) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269232029) |
| base-b-test-2-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269232047) |
| base-b-test-8-npu-a3 / run (0) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269232083) |
| multimodal-gen-test-1-npu-a3 (1) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269232093) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269232098) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127269232208) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42033446434/job/127284515780) |


## [Run #42032893282](https://github.com/sgl-project/sglang/actions/runs/42032893282)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 8.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42032893282

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 1.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679258) |
| multimodal-gen-test-1-npu-a3 (0) | 1.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679375) |
| multimodal-gen-test-4-npu-a3 (0) | 1.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679382) |
| base-b-test-2-npu-a3 / run (0) | 2.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679384) |
| base-b-test-8-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679388) |
| base-b-test-1-npu-a3 / run (0) | 1.6min | 环境问题 | 日志在 checkout 后即清理孤儿进程结束，未见测试执行，疑似 runner/容器环境异常导致作业提前终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679390) |
| multimodal-gen-test-4-npu-a3 (1) | 1.4min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679464) |
| base-b-test-4-npu-a3 / run (1) | 5.3min | 环境问题 | git fetch 从内部 CDN 服务拉取代码时多次返回 HTTP 500，重试后才成功，作业最终被清理退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679522) |
| base-b-test-4-npu-a3 / run (0) | 6.4min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679523) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679548) |




- **base-b-test-2-npu-a3 / run (0)**: 日志显示 pip 安装依赖过程中报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679384

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 apt 安装依赖后、容器初始化阶段，属 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679388

- **base-b-test-1-npu-a3 / run (0)**: 日志仅显示代码检出成功，随后执行 k8s index.js 并立即清理孤儿进程，无任何测试用例输出或 Traceback，未出现退出码 5 相关错误，判断为 runner 环境或作业调度异常，而非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679390


- **base-b-test-4-npu-a3 / run (1)**: checkout 阶段 git fetch 访问 git-cdn-service 返回 HTTP 500（error reading section header 'shallow-info'），重试两次后第三次成功；随后 k8s 步骤执行完即清理孤儿进程，未见测试用例实际运行，属基础设施/网络异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679522


- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 k8s runner 启动容器阶段，未进入测试执行，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127264679548

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127263731927) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42032893282/job/127263731963) |


## [Run #42028942178](https://github.com/sgl-project/sglang/actions/runs/42028942178)
- **分支**: `weight-cache-vmm-fd-upstream`
- **总耗时**: 43.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42028942178

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 8.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127262950290) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127262950290

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127250331702) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127250331847) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540068) |
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540088) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540152) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540288) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540450) |
| base-b-test-8-npu-a3 / run (0) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540592) |
| base-b-test-1-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540601) |
| base-b-test-2-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540659) |
| base-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540814) |
| base-b-test-4-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127251540968) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127262950377) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42028942178/job/127262950697) |


## [Run #42027302275](https://github.com/sgl-project/sglang/actions/runs/42027302275)
- **分支**: `codex/pp-arrival-match-main`
- **总耗时**: 75.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42027302275

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 7.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127278189899) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 7.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127278190052) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127244810132) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127244810195) |
| multimodal-gen-test-4-npu-a3 (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985661) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985673) |
| base-b-test-1-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985726) |
| base-b-test-16-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985905) |
| base-b-test-4-npu-a3 / run (1) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985916) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985921) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245985949) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127245986285) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127259202373) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 35.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127259202414) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42027302275/job/127259202586) |


## [Run #42024348292](https://github.com/sgl-project/sglang/actions/runs/42024348292)
- **分支**: `wan2_s2v_port`
- **总耗时**: 31.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42024348292

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 8.8min | 环境问题 | git fetch 访问内部 CDN 返回 502，重试后成功，但作业最终失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697748) |
| multimodal-gen-test-1-npu-a3 (1) | 10.5min | 环境问题 | git fetch 访问内部 git-cdn 服务返回 502，重试后成功但作业已失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697768) |
| multimodal-gen-test-1-npu-a3 (0) | 11.1min | 环境问题 | git fetch 访问内部 git-cdn 服务返回 502，重试后成功但作业仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697863) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 git fetch 访问 git-cdn-service 返回 502 错误，重试后成功检出代码；随后 k8s 步骤结束并清理进程，未见测试执行或明确错误，疑似环境/基础设施异常导致作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697748

- **multimodal-gen-test-1-npu-a3 (1)**: checkout 阶段 git fetch 访问 http://git-cdn-service...:8000 返回 502 Bad Gateway，等待10秒重试后成功拉取，但该错误已导致作业失败，属基础设施/网络问题，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697768

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 git fetch 访问 git-cdn-service 返回 502 错误（exit 128），重试后拉取成功并完成 checkout，随后作业在 k8s 步骤后结束，属基础设施/网络代理问题，非代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697863

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127234936716) |
| multimodal-gen-test-4-npu-a3 (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42024348292/job/127235697775) |


## [Run #42021480795](https://github.com/sgl-project/sglang/actions/runs/42021480795)
- **分支**: `wj/nixl-kv-packing`
- **总耗时**: 28.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42021480795

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 21.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127226379123) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127226379123

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127225241348) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127225241558) |
| base-b-test-4-npu-a3 / run (1) | 6.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021480795/job/127226379161) |


## [Run #42021251629](https://github.com/sgl-project/sglang/actions/runs/42021251629)
- **分支**: `fix/gemma4-shared-kv-graphs`
- **总耗时**: 33.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42021251629

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225915244) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225915244

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127224768731) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127224768997) |
| multimodal-gen-test-4-npu-a3 (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225913818) |
| multimodal-gen-test-4-npu-a3 (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225913839) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225913885) |
| base-b-test-16-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225913971) |
| base-b-test-1-npu-a3 / run (0) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225914028) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225914035) |
| base-b-test-4-npu-a3 / run (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42021251629/job/127225914099) |


## [Run #42013140381](https://github.com/sgl-project/sglang/actions/runs/42013140381)
- **分支**: `k31-decode-moe-main`
- **总耗时**: 34.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42013140381

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 25.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927294) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | 其他 | 日志中所有用例均通过，作业实际成功，无失败原因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927439) |
| base-b-test-16-npu-a3 / run (0) | 17.0min | 环境问题 | TokenizerManager 看门狗超时，容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927487) |
| base-b-test-2-npu-a3 / run (0) | 17.7min | 环境问题 | 自定义容器执行失败，作业在启动阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927615) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约25分钟后结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927294

- **base-b-test-1-npu-a3 / run (0)**: 日志显示各测试文件 passed 均为 true，TIMINGS END 正常输出，随后进入 Post job cleanup，未出现 Traceback、RuntimeError 或退出码 5 等错误，作业本身未见失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927439

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TokenizerManager watchdog timeout（watchdog_timeout=300），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927487

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器执行环境故障，非用例代码问题；此前 server 初始化日志正常，随后容器实现报错退出，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927615

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197118540) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197118682) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927212) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927297) |
| base-b-test-8-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927421) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927437) |
| base-b-test-4-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927526) |
| base-b-test-4-npu-a3 / run (1) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42013140381/job/127197927840) |


## [Run #42009851464](https://github.com/sgl-project/sglang/actions/runs/42009851464)
- **分支**: `xpu-video-decode`
- **总耗时**: 32.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42009851464

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 20.5min | 环境问题 | 测试用例执行失败，diffusion-failures 目录无产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268195) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268210) |
| multimodal-gen-test-4-npu-a3 (0) | 20.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268242) |
| multimodal-gen-test-1-npu-a3 (0) | 22.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268299) |
| base-b-test-8-npu-a3 / run (0) | 24.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268468) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268518) |
| base-b-test-4-npu-a3 / run (0) | 24.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268578) |
| base-b-test-4-npu-a3 / run (1) | 24.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268592) |
| base-b-test-16-npu-a3 / run (0) | 20.4min | 环境问题 | 自定义容器执行失败，作业在容器启动/运行阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268645) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示未找到 diffusion-failures/ 路径文件，无 artifact 上传，且复制 _temp 失败。结合退出码 5 提示 unittest 存在 errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268195

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业约20分钟后结束，退出码5表明 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268210

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业约20分钟后结束，退出码5表示unittest有errors，常见于setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL）。日志中未见diffusion-failures目录，无产物上传，需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268242

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268299


- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在第6个用例启动后，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268518



- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于自托管 runner 的容器运行时故障，非用例代码或精度问题；此前仅有 Ascend 算子脚本的 SyntaxWarning，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268645

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127186025945) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127186025971) |
| base-b-test-1-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009851464/job/127187268484) |


## [Run #42009583209](https://github.com/sgl-project/sglang/actions/runs/42009583209)
- **分支**: `yihou/kv-metrics-nonblocking-20261027`
- **总耗时**: 69.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42009583209

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 18.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127208407501) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127208407501

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185110388) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185110434) |
| multimodal-gen-test-4-npu-a3 (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987390) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987464) |
| base-b-test-2-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987531) |
| base-b-test-16-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987590) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987592) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987596) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987609) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127185987731) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127208407454) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42009583209/job/127208407484) |


## [Run #42003156015](https://github.com/sgl-project/sglang/actions/runs/42003156015)
- **分支**: `perf/npuseqlens-false-k3`
- **总耗时**: 97.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42003156015

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127257511386) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127257511631) |


- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能问题；此前 perf 用例仍在正常捕获 batch。
  链接: https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127257511631

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127223116870) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127223116913) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247196) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247242) |
| base-b-test-1-npu-a3 / run (0) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247264) |
| base-b-test-4-npu-a3 / run (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247341) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247423) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247424) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247477) |
| base-b-test-4-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127224247487) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127240675081) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127240675090) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42003156015/job/127240675242) |


## [Run #42001422237](https://github.com/sgl-project/sglang/actions/runs/42001422237)
- **分支**: `perf/npuseqlens-false-k3`
- **总耗时**: 17.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42001422237

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 7.2min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业以退出码 5 结束，疑似 setUpClass 阶段 server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158629751) |
| multimodal-gen-test-4-npu-a3 (1) | 9.7min | 环境问题 | 日志中未见测试用例执行，仅显示上传产物路径 diffusion-failures/ 无文件，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158629777) |
| base-b-test-16-npu-a3 / run (0) | 9.3min | 环境问题 | 自定义容器执行失败，作业在容器启动阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630065) |
| base-b-test-8-npu-a3 / run (0) | 9.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630075) |
| base-b-test-4-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630165) |
| base-b-test-2-npu-a3 / run (0) | 6.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630172) |
| base-b-test-4-npu-a3 / run (1) | 6.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630239) |
| base-b-test-1-npu-a3 / run (0) | 6.3min | 环境问题 | 自定义容器执行失败，作业在运行测试时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630254) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志省略了关键错误段，仅见 'No files were found with the provided path: diffusion-failures/'，无 Traceback。退出码 5 表示 unittest 存在 errors，最常见为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158629751

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 artifact 上传失败（No files were found with the provided path: diffusion-failures/），没有测试脚本输出或 Traceback，无法确认具体失败原因，疑似环境/产物路径问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158629777

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630065


- **base-b-test-4-npu-a3 / run (0)**: 日志显示 KV Cache 分配正常后立即报错 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630165

- **base-b-test-2-npu-a3 / run (0)**: 日志报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630172

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员。测试脚本刚打印 Begin 后容器执行即失败，属 runner/容器环境问题，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630239

- **base-b-test-1-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed”，发生在运行 test_npu_sampling_backend.py 期间，属于自托管 runner 容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127158630254

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127157524379) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42001422237/job/127157524476) |


## [Run #42000458797](https://github.com/sgl-project/sglang/actions/runs/42000458797)
- **分支**: `main_cpu`
- **总耗时**: 22.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42000458797

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 3.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155481071) |
| base-b-test-4-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155481082) |
| base-b-test-1-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155481115) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155481191) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155481252) |
| base-b-test-16-npu-a3 / run (0) | 8.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155481638) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127154303399) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127154303452) |
| multimodal-gen-test-4-npu-a3 (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155480787) |
| multimodal-gen-test-4-npu-a3 (0) | 6.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42000458797/job/127155480848) |


## [Run #41997636084](https://github.com/sgl-project/sglang/actions/runs/41997636084)
- **分支**: `align-queue-per-rank`
- **总耗时**: 9.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41997636084

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 6.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/41997636084/job/127145931009) |
| base-b-test-4-npu-a3 / run (1) | 6.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41997636084/job/127145931017) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器运行时环境故障，测试尚未开始执行，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41997636084/job/127145931009

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器执行环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41997636084/job/127145931017

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41997636084/job/127144822580) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41997636084/job/127144822672) |


## [Run #41996717847](https://github.com/sgl-project/sglang/actions/runs/41996717847)
- **分支**: `litetopk-prefill`
- **总耗时**: 12.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41996717847

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 4.7min | 环境问题 | 日志被截断，无法看到真实错误，但作业在 checkout 后即结束，疑似 runner 环境或代理问题导致作业异常终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032172) |
| multimodal-gen-test-1-npu-a3 (0) | 4.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032173) |
| multimodal-gen-test-4-npu-a3 (1) | 5.2min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032212) |
| base-b-test-1-npu-a3 / run (0) | 8.3min | 环境问题 | git fetch 因 shallow 文件被并发修改而失败，重试后成功，但作业最终失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032240) |
| base-b-test-16-npu-a3 / run (0) | 6.4min | 环境问题 | 作业在 checkout 后执行 k8s 脚本时异常退出，未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032284) |
| base-b-test-4-npu-a3 / run (1) | 8.6min | 环境问题 | git fetch 因 shallow 文件被并发修改而失败，重试后成功，但作业最终失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032349) |
| base-b-test-2-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032375) |
| base-b-test-4-npu-a3 / run (0) | 4.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032378) |
| base-b-test-8-npu-a3 / run (0) | 5.8min | 环境问题 | 日志在 checkout 后即结束，未进入测试执行，疑似 runner 环境或容器启动异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032420) |
| multimodal-gen-test-4-npu-a3 (0) | 4.2min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032477) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志仅显示 checkout 完成及 Node.js 弃用警告，未见测试执行或 Traceback；中间省略部分可能含真实错误，需完整日志确认是否为 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL）。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032172

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业在约4分钟内结束，未找到diffusion-failures/目录产物，无artifact上传。退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032173

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示未找到 diffusion-failures/ 目录，无产物上传；结合退出码5，最可能是 setUpClass 中 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032212

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 git fetch 报错 'fatal: shallow file has changed since we read it'（exit 128），重试后 fetch 和 checkout 均成功。失败发生在后续 k8s 步骤，日志被截断，无法看到真实错误。建议查看完整日志确认退出码 5 对应的 unittest errors 详情。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032240

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 checkout 完成后运行 /home/runner/k8s/index.js，随即出现 Node 弃用警告并清理孤儿进程，作业终止，未见测试用例执行或 Traceback，疑似 runner/k8s 环境或脚本异常导致提前退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032284

- **base-b-test-4-npu-a3 / run (1)**: checkout 阶段首次 git fetch 报 'fatal: shallow file has changed since we read it'（exit 128），重试后成功拉取代码；随后 k8s 步骤运行后作业失败，日志未显示具体测试错误，疑似环境/runner 侧问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032349

- **base-b-test-2-npu-a3 / run (0)**: 日志显示安装依赖后出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032375

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 apt 解包 llvm-14-dev 等包时出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032378

- **base-b-test-8-npu-a3 / run (0)**: 日志仅显示代码检出完成及 k8s 脚本启动，随后出现 Node.js 弃用警告和清理孤儿进程，无任何测试输出或退出码 5 的 unittest 错误信息，说明失败发生在测试执行前的环境/容器阶段，而非用例本身。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032420

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，缺少真实错误信息；仅见上传产物路径 diffusion-failures/ 不存在，无 Traceback。需查看完整日志确认是否为 server 启动失败或环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127143032477

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127141746235) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41996717847/job/127141746668) |


## [Run #41990375586](https://github.com/sgl-project/sglang/actions/runs/41990375586)
- **分支**: `lsyin/sched-pr22`
- **总耗时**: 38.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41990375586

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 22.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192526) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192526

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127122213577) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127122213654) |
| multimodal-gen-test-4-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192447) |
| base-b-test-16-npu-a3 / run (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192490) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192502) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192506) |
| base-b-test-4-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192515) |
| base-b-test-1-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192532) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41990375586/job/127123192613) |


## [Run #41988146075](https://github.com/sgl-project/sglang/actions/runs/41988146075)
- **分支**: `lsyin/sched-pr22`
- **总耗时**: 22.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41988146075

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806672) |
| base-b-test-2-npu-a3 / run (0) | 14.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806707) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806715) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | 其他 | 日志显示测试全部通过，作业本身无失败迹象，失败可能由日志未覆盖的退出码或清理阶段引起。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806741) |
| base-b-test-1-npu-a3 / run (0) | 14.3min | 环境问题 | 自定义容器执行失败，疑似 runner 容器异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806811) |
| base-b-test-4-npu-a3 / run (0) | 12.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806841) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，缺少真实错误信息；仅见 'No files were found with the provided path: diffusion-failures/'，说明测试未产出失败产物目录，可能 setUpClass 阶段 server 启动失败或测试未运行，需查看完整日志中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806672

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境问题，非用例代码失败；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806707

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载完成后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806715

- **base-b-test-8-npu-a3 / run (0)**: 日志中测试 1/1 passed，无 Traceback 或错误；仅见 Node.js 弃用警告。若作业失败，可能因退出码 5 对应 setUpClass 阶段 server 启动失败，但本段日志未体现，需查看省略部分。
  链接: https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806741

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到25%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器执行异常，非用例代码报错，需联系 runner 管理员排查容器/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806811

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题；此前推理服务仍在正常输出吞吐日志，随后容器执行异常终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806841

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127113853694) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127113853884) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806508) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41988146075/job/127114806753) |


## [Run #41985688848](https://github.com/sgl-project/sglang/actions/runs/41985688848)
- **分支**: `feat/fa3-fa4-hybrid-gemma4`
- **总耗时**: 12.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41985688848

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41985688848/job/127106676097) |
| base-b-test-4-npu-a3 / run (0) | 4.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41985688848/job/127106676188) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41985688848/job/127105929214) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41985688848/job/127105929229) |
| base-b-test-2-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41985688848/job/127106676273) |
| base-b-test-4-npu-a3 / run (1) | 5.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41985688848/job/127106676322) |


## [Run #41984911470](https://github.com/sgl-project/sglang/actions/runs/41984911470)
- **分支**: `amd/dcp-owned-by-row`
- **总耗时**: 53.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41984911470

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104189928) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127103448533) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127103448782) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104189485) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104189564) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104189567) |
| base-b-test-16-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104189788) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104189918) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104190000) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104190022) |
| multimodal-gen-test-4-npu-a3 (0) | 40.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104190074) |
| base-b-test-1-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41984911470/job/127104190154) |


## [Run #41982168899](https://github.com/sgl-project/sglang/actions/runs/41982168899)
- **分支**: `lsyin/indexer-dcp-prep`
- **总耗时**: 30.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41982168899

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在启动 evalscope 后立即中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127102608186) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127102608230) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 evalscope 进程刚 spawn 即报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127102608186

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载至约59%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码或精度问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127102608230

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127094964970) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127094965094) |
| base-b-test-16-npu-a3 / run (0) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127095738334) |
| base-b-test-2-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127095738346) |
| base-b-test-1-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127095738368) |
| base-b-test-4-npu-a3 / run (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127095738414) |
| base-b-test-8-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127095738440) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127095738509) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41982168899/job/127102608364) |


## [Run #41980950444](https://github.com/sgl-project/sglang/actions/runs/41980950444)
- **分支**: `lsyin/indexer-dcp-prep`
- **总耗时**: 11.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41980950444

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 8.3min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556454) |
| base-b-test-2-npu-a3 / run (0) | 8.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556488) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556494) |
| base-b-test-4-npu-a3 / run (1) | 8.4min | 环境问题 | 自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556549) |
| base-b-test-16-npu-a3 / run (0) | 8.3min | 环境问题 | 自定义容器执行失败，作业在加载模型分片过程中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556577) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器环境问题，并非用例或代码本身失败，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556454

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在权重加载阶段，属于 runner/容器环境故障，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556488

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题；此时 tokenizer 刚初始化，测试尚未真正执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556494

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，属于自托管 runner 的容器环境问题，并非用例本身的代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556549

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载至38%时出现“Executing the custom container implementation failed”，属自托管 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556577

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127090816182) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127090816238) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41980950444/job/127091556493) |


## [Run #41979605326](https://github.com/sgl-project/sglang/actions/runs/41979605326)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 41.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41979605326

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127095062331) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 16.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127095062353) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示精度测试 gsm8k 已跑到约96%时，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127095062331

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型权重分片加载到约26%时出现“Executing the custom container implementation failed”，属于 runner/容器基础设施异常，非用例断言失败，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127095062353

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127086579926) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127086579952) |
| multimodal-gen-test-1-npu-a3 (1) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449091) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449104) |
| multimodal-gen-test-4-npu-a3 (0) | 33.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449136) |
| base-b-test-16-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449189) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449201) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449260) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449280) |
| base-b-test-4-npu-a3 / run (1) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449335) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449352) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127087449396) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41979605326/job/127095062535) |


## [Run #41971072852](https://github.com/sgl-project/sglang/actions/runs/41971072852)
- **分支**: `oss-sync-5f33eae5cc`
- **总耗时**: 33.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41971072852

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 16.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938264) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938264

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059353227) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059353342) |
| multimodal-gen-test-4-npu-a3 (0) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059937938) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059937986) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059937994) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938106) |
| base-b-test-1-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938140) |
| base-b-test-16-npu-a3 / run (0) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938230) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938261) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938265) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41971072852/job/127059938489) |


## [Run #41969675523](https://github.com/sgl-project/sglang/actions/runs/41969675523)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 47.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41969675523

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 16.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127064605788) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127064605919) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示服务端推理正常（吞吐约197 token/s），随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127064605788

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示服务端推理请求均返回 200 OK，随后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127064605919

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055183671) |
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055183781) |
| multimodal-gen-test-1-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055979819) |
| multimodal-gen-test-1-npu-a3 (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055979884) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055979989) |
| multimodal-gen-test-4-npu-a3 (1) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055979993) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055980011) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055980016) |
| base-b-test-16-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055980053) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055980095) |
| base-b-test-1-npu-a3 / run (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055980156) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127055980178) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969675523/job/127064605815) |


## [Run #41969320337](https://github.com/sgl-project/sglang/actions/runs/41969320337)
- **分支**: `fix-mamba-copy-from-temporal-oom`
- **总耗时**: 68.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41969320337

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127062123462) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127062123462

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127053725279) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127053725386) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054456915) |
| multimodal-gen-test-1-npu-a3 (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054456916) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054456977) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457025) |
| base-b-test-1-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457066) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457086) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457116) |
| base-b-test-16-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457133) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457199) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127054457226) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127062123370) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41969320337/job/127062123413) |


## [Run #41967254543](https://github.com/sgl-project/sglang/actions/runs/41967254543)
- **分支**: `bench-serving-per-run-accept-length`
- **总耗时**: 5.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41967254543

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047751441) |
| base-b-test-16-npu-a3 / run (0) | 1.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047751448) |
| base-b-test-8-npu-a3 / run (0) | 2.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047751515) |
| base-b-test-4-npu-a3 / run (1) | 2.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047751571) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047751637) |
| base-b-test-4-npu-a3 / run (0) | 1.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047751933) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047148200) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41967254543/job/127047148214) |


## [Run #41964964623](https://github.com/sgl-project/sglang/actions/runs/41964964623)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 46.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41964964623

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 18.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127048916553) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | 其他 | 日志显示测试实际通过（1/1 passed），作业失败原因未在日志中体现 | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127048916569) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例或代码本身失败；此前推理请求均返回 200 OK。
  链接: https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127048916553

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾显示 moonlight_16b_a3b 精度测试 1/1 通过，耗时807秒，随后正常执行 post job cleanup，未见 Traceback、RuntimeError 或退出码5等错误信息。失败可能发生在省略的中间日志或作业收尾阶段，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127048916569

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127040225588) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127040225699) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041054843) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041054854) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041054855) |
| multimodal-gen-test-4-npu-a3 (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041054875) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041054922) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041054942) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041055033) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041055054) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041055076) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127041055087) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964964623/job/127048916598) |


## [Run #41964313373](https://github.com/sgl-project/sglang/actions/runs/41964313373)
- **分支**: `feature/amd-glm5-dsa-mla-decode-gfx950`
- **总耗时**: 6.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41964313373

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41964313373/job/127038595334) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41964313373/job/127038595402) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41964313373/job/127038595420) |
| base-b-test-4-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41964313373/job/127038595465) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964313373/job/127037798510) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41964313373/job/127037798520) |


## [Run #41963525366](https://github.com/sgl-project/sglang/actions/runs/41963525366)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 15.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41963525366

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169633) |
| multimodal-gen-test-1-npu-a3 (0) | 11.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169647) |
| multimodal-gen-test-1-npu-a3 (1) | 11.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169698) |
| base-b-test-16-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169719) |
| base-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169738) |
| base-b-test-2-npu-a3 / run (0) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169744) |
| multimodal-gen-test-4-npu-a3 (0) | 11.3min | 环境问题 | diffusion 测试失败且未生成失败产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169750) |
| base-b-test-4-npu-a3 / run (1) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169799) |
| base-b-test-8-npu-a3 / run (0) | 1.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169822) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169892) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169633

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中无明确Traceback，但退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。同时diffusion-failures目录无文件，artifact上传为空。
  链接: https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169647

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169698




- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试脚本异常退出（退出码 5，unittest errors），最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127036169750




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127035313677) |
| Recommend tests from coverage | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41963525366/job/127035313904) |


## [Run #41962327668](https://github.com/sgl-project/sglang/actions/runs/41962327668)
- **分支**: `add_mxfp8_xpu_support`
- **总耗时**: 15.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41962327668

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226372) |
| base-b-test-8-npu-a3 / run (0) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226406) |
| base-b-test-16-npu-a3 / run (0) | 2.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226422) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226435) |
| base-b-test-4-npu-a3 / run (0) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226645) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226647) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127031480237) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127031480307) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226114) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41962327668/job/127032226200) |


## [Run #41961638538](https://github.com/sgl-project/sglang/actions/runs/41961638538)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 43.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41961638538

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 2.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130288) |
| base-b-test-4-npu-a3 / run (0) | 2.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130296) |
| base-b-test-2-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130328) |
| base-b-test-1-npu-a3 / run (0) | 2.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130339) |
| base-b-test-8-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130364) |
| base-b-test-4-npu-a3 / run (1) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130412) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127029249496) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127029249510) |
| multimodal-gen-test-1-npu-a3 (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130163) |
| multimodal-gen-test-4-npu-a3 (0) | 35.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130229) |
| multimodal-gen-test-4-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130240) |
| multimodal-gen-test-1-npu-a3 (1) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41961638538/job/127030130247) |


## [Run #41959745764](https://github.com/sgl-project/sglang/actions/runs/41959745764)
- **分支**: `hicache-host-memory-preflight`
- **总耗时**: 37.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41959745764

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083495) |
| base-b-test-16-npu-a3 / run (0) | 2.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083512) |
| base-b-test-8-npu-a3 / run (0) | 2.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083515) |
| base-b-test-2-npu-a3 / run (0) | 4.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083517) |
| base-b-test-4-npu-a3 / run (1) | 3.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083575) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083646) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127023188672) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127023188738) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083278) |
| multimodal-gen-test-4-npu-a3 (1) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083294) |
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083307) |
| multimodal-gen-test-1-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959745764/job/127024083395) |


## [Run #41959656555](https://github.com/sgl-project/sglang/actions/runs/41959656555)
- **分支**: `feature/leixin/qwen3-blockfp8-quant-fusion`
- **总耗时**: 31.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41959656555

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 1.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003701) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027004024) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127026046035) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127026046202) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003510) |
| multimodal-gen-test-1-npu-a3 (1) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003533) |
| multimodal-gen-test-4-npu-a3 (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003600) |
| base-b-test-16-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003603) |
| multimodal-gen-test-4-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003620) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003692) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027003717) |
| base-b-test-1-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959656555/job/127027004110) |


## [Run #41959086008](https://github.com/sgl-project/sglang/actions/runs/41959086008)
- **分支**: `xiangch/fused-wo-b-gemm-ar-main`
- **总耗时**: 5.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41959086008

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41959086008/job/127021846581) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959086008/job/127021038682) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41959086008/job/127021038714) |


## [Run #41958340319](https://github.com/sgl-project/sglang/actions/runs/41958340319)
- **分支**: `perf/qwen3-hip-qknorm-rope`
- **总耗时**: 20.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41958340319

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41958340319/job/127019309401) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41958340319/job/127018646911) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41958340319/job/127018646985) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41958340319/job/127019309277) |
| base-b-test-4-npu-a3 / run (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41958340319/job/127019309339) |


## [Run #41958044865](https://github.com/sgl-project/sglang/actions/runs/41958044865)
- **分支**: `page-unified/mooncake-storage`
- **总耗时**: 6.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41958044865

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41958044865/job/127019692135) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41958044865/job/127019692199) |
| base-b-test-4-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41958044865/job/127019692263) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41958044865/job/127019692322) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41958044865/job/127018833321) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41958044865/job/127018833368) |


## [Run #41957259580](https://github.com/sgl-project/sglang/actions/runs/41957259580)
- **分支**: `fix/eplb-recorder-mode-48403`
- **总耗时**: 6.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41957259580

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41957259580/job/127016009047) |
| base-b-test-2-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41957259580/job/127016009111) |
| base-b-test-1-npu-a3 / run (0) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41957259580/job/127016009127) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41957259580/job/127016009169) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41957259580/job/127015187371) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41957259580/job/127015187410) |


## [Run #41956917380](https://github.com/sgl-project/sglang/actions/runs/41956917380)
- **分支**: `oss-sync-5a3f5544c6`
- **总耗时**: 6.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41956917380

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 2.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956917380/job/127014905131) |
| base-b-test-2-npu-a3 / run (0) | 2.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956917380/job/127014905148) |
| base-b-test-4-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956917380/job/127014905159) |
| base-b-test-1-npu-a3 / run (0) | 3.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956917380/job/127014905295) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956917380/job/127014058830) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956917380/job/127014058923) |


## [Run #41956296204](https://github.com/sgl-project/sglang/actions/runs/41956296204)
- **分支**: `fix-mamba-copy-from-temporal-oom`
- **总耗时**: 39.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41956296204

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648328) |
| base-b-test-16-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648353) |
| base-b-test-4-npu-a3 / run (1) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648377) |
| base-b-test-4-npu-a3 / run (0) | 1.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648408) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012040638) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012040708) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648135) |
| multimodal-gen-test-1-npu-a3 (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648143) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648228) |
| multimodal-gen-test-4-npu-a3 (0) | 35.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648301) |
| base-b-test-2-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648312) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41956296204/job/127012648511) |


## [Run #41955745984](https://github.com/sgl-project/sglang/actions/runs/41955745984)
- **分支**: `wuyaole/fix-prefill-reservation-budget`
- **总耗时**: 38.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41955745984

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923574) |
| base-b-test-2-npu-a3 / run (0) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923624) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010250249) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010250255) |
| multimodal-gen-test-1-npu-a3 (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923392) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923455) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923578) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923629) |
| base-b-test-1-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923638) |
| base-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923649) |
| multimodal-gen-test-4-npu-a3 (0) | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923670) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955745984/job/127010923902) |


## [Run #41955019901](https://github.com/sgl-project/sglang/actions/runs/41955019901)
- **分支**: `jacob/glm5-dsa-indexer-aiter-fuse`
- **总耗时**: 5.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41955019901

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 2.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41955019901/job/127008778307) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955019901/job/127007926053) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41955019901/job/127007926074) |


## [Run #41951310966](https://github.com/sgl-project/sglang/actions/runs/41951310966)
- **分支**: `amd/hip-gdn-prefill-layout`
- **总耗时**: 6.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41951310966

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 3.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41951310966/job/126996694484) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 3.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41951310966/job/126996694542) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41951310966/job/126995813973) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41951310966/job/126995814123) |


## [Run #41951230115](https://github.com/sgl-project/sglang/actions/runs/41951230115)
- **分支**: `fix/dsv41-cuda-cp-replay-tail`
- **总耗时**: 9.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41951230115

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41951230115/job/127003961074) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41951230115/job/127000958813) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41951230115/job/127000958892) |
| base-b-test-2-npu-a3 / run (0) | 5.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41951230115/job/127001893302) |


## [Run #41950749707](https://github.com/sgl-project/sglang/actions/runs/41950749707)
- **分支**: `qkang/elastic-ep-mooncake-scale-down`
- **总耗时**: 39.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41950749707

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761454) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761459) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761463) |
| base-b-test-8-npu-a3 / run (0) | 1.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761577) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761454




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126993992706) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126993992710) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761299) |
| multimodal-gen-test-4-npu-a3 (0) | 35.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761300) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761305) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761402) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761408) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41950749707/job/126994761514) |


## [Run #41949995195](https://github.com/sgl-project/sglang/actions/runs/41949995195)
- **分支**: `flashinfer-0.7.3-moe-ep`
- **总耗时**: 36.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41949995195

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992448111) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992448151) |
| base-b-test-16-npu-a3 / run (0) | 2.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992448163) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992448195) |
| base-b-test-2-npu-a3 / run (0) | 1.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992448214) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992448224) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126991565194) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126991565291) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992447825) |
| multimodal-gen-test-1-npu-a3 (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992447865) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992447945) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41949995195/job/126992447951) |


## [Run #41944363897](https://github.com/sgl-project/sglang/actions/runs/41944363897)
- **分支**: `lsyin/kimi-k3-request-checks`
- **总耗时**: 21.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41944363897

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532032) |
| multimodal-gen-test-4-npu-a3 (0) | 17.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532081) |
| multimodal-gen-test-1-npu-a3 (1) | 17.3min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532150) |
| multimodal-gen-test-4-npu-a3 (1) | 17.6min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532164) |
| base-b-test-1-npu-a3 / run (0) | 17.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532245) |
| base-b-test-4-npu-a3 / run (0) | 16.5min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532286) |
| base-b-test-2-npu-a3 / run (0) | 17.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532290) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | 超时 | Scheduler watchdog 超时导致容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532392) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532032

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532081

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试未产出失败样本；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志被省略，缺少具体 Traceback，需查看中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532150

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532164

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 test_npu_tp1_bf16 用例执行期间，属于 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532245

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾 Test Summary: 2/2 passed，两个 NPU 用例均 PASSED，耗时 654s 和 99s，未见 Traceback 或非零退出码；仅存在 Node.js 弃用警告，不影响结果。建议核对作业最终状态是否被误判为失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532286

- **base-b-test-2-npu-a3 / run (0)**: 日志显示加载权重分片到 44% 时出现 'Executing the custom container implementation failed'，属于 runner 容器环境异常，并非用例代码错误；随后进入清理阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532290

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP6 EP6 Scheduler watchdog timeout（watchdog_timeout=300），随后报错 custom container implementation failed，作业因调度器看门狗超时中断，属超时类失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532392

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126974551866) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126974552011) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532197) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944363897/job/126975532300) |


## [Run #41944346810](https://github.com/sgl-project/sglang/actions/runs/41944346810)
- **分支**: `lsyin/kimi-k3-forced-tool-call`
- **总耗时**: 21.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41944346810

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 7.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41944346810/job/126978461427) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示模型分片加载到20%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，并非用例或代码本身报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/41944346810/job/126978461427

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944346810/job/126974440535) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944346810/job/126974440604) |
| base-b-test-2-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41944346810/job/126975421626) |


## [Run #41943510711](https://github.com/sgl-project/sglang/actions/runs/41943510711)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 42.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41943510711

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 35.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859188) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 12.9min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126981205631) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 13.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126981205810) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859188

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例本身的精度或代码问题；此时 gsm8k 评测仍在正常进行，作业被外部中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126981205631

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例断言失败；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126981205810

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126970661478) |
| Recommend tests from coverage | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126970661582) |
| multimodal-gen-test-4-npu-a3 (1) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859031) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859044) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859204) |
| base-b-test-16-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859233) |
| base-b-test-8-npu-a3 / run (0) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859243) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859297) |
| base-b-test-1-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859341) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859349) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126971859376) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41943510711/job/126981205736) |


## [Run #41941146572](https://github.com/sgl-project/sglang/actions/runs/41941146572)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 20.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41941146572

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 14.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259048) |
| multimodal-gen-test-4-npu-a3 (0) | 15.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259100) |
| multimodal-gen-test-1-npu-a3 (1) | 14.3min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259169) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | 环境问题 | 测试产物目录 diffusion-failures 不存在，且从 pod 复制 _temp 失败，作业未产出结果 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259202) |
| base-b-test-1-npu-a3 / run (0) | 15.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259221) |
| base-b-test-2-npu-a3 / run (0) | 15.3min | 环境问题 | 自定义容器执行失败，作业被 runner 中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259227) |
| base-b-test-16-npu-a3 / run (0) | 15.3min | 超时 | Scheduler watchdog 超时，容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259320) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259342) |
| base-b-test-4-npu-a3 / run (1) | 14.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259428) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259048

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259100

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成该目录（可能用例未产出失败样本或路径配置错误），导致 upload-artifact 步骤无文件可传而失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259169

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/'，随后 'Failed to copy _temp from pod'，说明容器内测试未生成预期产物或 pod 拷贝异常，属环境/执行环境问题，非用例收集问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259202

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题；需联系自托管 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259221

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属自托管 runner 容器环境异常，非用例代码问题；此前 sglang 初始化正常，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259227

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP12 EP12 Scheduler watchdog timeout（watchdog_timeout=300，soft=True），随后报错“Executing the custom container implementation failed”，作业因调度器看门狗超时终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259320

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed'，发生在推理正常输出后，属 runner/容器环境故障，非用例代码或性能问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259342

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 health_generate 返回 503，随后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259428

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126962169724) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126962169751) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41941146572/job/126963259286) |


## [Run #41939053028](https://github.com/sgl-project/sglang/actions/runs/41939053028)
- **分支**: `lsyin/sched-pr21`
- **总耗时**: 5.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41939053028

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| check-changes | 5.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/41939053028/job/126955111999) |



## [Run #41938193052](https://github.com/sgl-project/sglang/actions/runs/41938193052)
- **分支**: `dspark-vocab-verify-guards`
- **总耗时**: 8.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41938193052

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 5.8min | 代码错误 | test_dspark_npu_dispatch.py 中 2 个用例有 1 个失败，导致该文件退出码 1。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41938193052/job/126952998776) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示该测试文件 Ran 2 tests，FAILED (failures=1)，返回 exit code 1，属于用例断言失败而非环境或超时问题，需查看具体 Traceback 定位失败用例。
  - 失败用例: dspark_npu_dispatch.py, dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41938193052/job/126952998776

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41938193052/job/126952076984) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41938193052/job/126952077121) |


## [Run #41931726281](https://github.com/sgl-project/sglang/actions/runs/41931726281)
- **分支**: `lsyin/sched-pr21`
- **总耗时**: 57.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41931726281

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126953640578) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126953640811) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 pip 安装依赖过程中报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码或性能回归问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126953640578

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示在解包 deb 包时出现 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126953640811

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126930223136) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126930223702) |
| multimodal-gen-test-1-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342144) |
| multimodal-gen-test-1-npu-a3 (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342327) |
| multimodal-gen-test-4-npu-a3 (0) | 32.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342328) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342363) |
| base-b-test-1-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342414) |
| base-b-test-4-npu-a3 / run (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342454) |
| base-b-test-16-npu-a3 / run (0) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342460) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342500) |
| base-b-test-2-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342521) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126931342555) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126940564457) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126940564518) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41931726281/job/126940564573) |


## [Run #41917552869](https://github.com/sgl-project/sglang/actions/runs/41917552869)
- **分支**: `oss-sync-5ac6bc3c22`
- **总耗时**: 25.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41917552869

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 10.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442649) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442649

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126881361002) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126881361130) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442219) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442267) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442398) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442476) |
| base-b-test-16-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442486) |
| base-b-test-4-npu-a3 / run (1) | 6.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442502) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41917552869/job/126882442504) |


## [Run #41909156736](https://github.com/sgl-project/sglang/actions/runs/41909156736)
- **分支**: `bbuf/cleanup-round2`
- **总耗时**: 13.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41909156736

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 8.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621859) |
| multimodal-gen-test-1-npu-a3 (1) | 8.3min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621895) |
| multimodal-gen-test-4-npu-a3 (0) | 9.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621897) |
| multimodal-gen-test-4-npu-a3 (1) | 9.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621930) |
| base-b-test-16-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622278) |
| base-b-test-4-npu-a3 / run (0) | 9.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622363) |
| base-b-test-2-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622507) |
| base-b-test-1-npu-a3 / run (0) | 9.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622512) |
| base-b-test-4-npu-a3 / run (1) | 8.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622730) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621859

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示 diffusion-failures/ 目录无文件可上传，说明测试未正常产出；退出码5对应 unittest errors，常见于 setUpClass 中 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621895

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败且未生成失败产物；退出码5表明unittest存在errors，最常见为setUpClass阶段server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621897

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853621930

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载至48%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622278

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 server 已启动成功，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622363

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在模型权重多线程加载阶段（0/16），属于 runner/容器环境异常，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622507

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例或代码本身的问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622512

- **base-b-test-4-npu-a3 / run (1)**: 日志显示测试用例本身已通过（Ran 2 tests OK），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，并非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622730

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126852043482) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126852043729) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41909156736/job/126853622384) |


## [Run #41895182570](https://github.com/sgl-project/sglang/actions/runs/41895182570)
- **分支**: `dp-attn-phase-lockstep`
- **总耗时**: 35.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41895182570

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 7.4min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470598) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 193 秒后 FAILED (errors=1)，2 个用例 0 通过，进程退出码 1，导致作业失败；具体错误需查看省略的 Traceback，疑似 setUpClass 阶段 server 启动失败。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470598

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126802960064) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126802960098) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470255) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470357) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470404) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470530) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470537) |
| multimodal-gen-test-1-npu-a3 (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470569) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470635) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804470767) |
| base-b-test-16-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41895182570/job/126804471002) |


## [Run #41893040645](https://github.com/sgl-project/sglang/actions/runs/41893040645)
- **分支**: `wuyaole/fix-prefill-reservation-budget`
- **总耗时**: 36.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41893040645

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754171) |
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754364) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754447) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126795512235) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126795512498) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796753938) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796753956) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754022) |
| base-b-test-4-npu-a3 / run (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754157) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754225) |
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754236) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41893040645/job/126796754485) |


## [Run #41885188470](https://github.com/sgl-project/sglang/actions/runs/41885188470)
- **分支**: `hejian/plugin-weight-update`
- **总耗时**: 40.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41885188470

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126801362015) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126801362260) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 pip 安装依赖过程中报错 'Executing the custom container implementation failed'，属于自托管 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126801362015

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试请求正常返回 200，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126801362260

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126784302320) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126784302466) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785748706) |
| multimodal-gen-test-4-npu-a3 (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785748722) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785748914) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785748941) |
| base-b-test-2-npu-a3 / run (0) | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785748965) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785748977) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785749086) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126785749611) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41885188470/job/126801362004) |


## [Run #41880178049](https://github.com/sgl-project/sglang/actions/runs/41880178049)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 33.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41880178049

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085331) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760086044) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085331

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760086044

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126758674690) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126758674862) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760084982) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085217) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085243) |
| base-b-test-1-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085251) |
| multimodal-gen-test-1-npu-a3 (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085334) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085432) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085443) |
| multimodal-gen-test-4-npu-a3 (1) | 27.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41880178049/job/126760085520) |


## [Run #41863403215](https://github.com/sgl-project/sglang/actions/runs/41863403215)
- **分支**: `kimi-k3.1-support`
- **总耗时**: 36.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41863403215

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 8.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233983) |
| base-b-test-4-npu-a3 / run (1) | 15.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693234180) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233983

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693234180

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126691965770) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126691965987) |
| multimodal-gen-test-1-npu-a3 (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233421) |
| multimodal-gen-test-4-npu-a3 (0) | 32.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233550) |
| multimodal-gen-test-1-npu-a3 (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233554) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233592) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233772) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693233821) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693234084) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41863403215/job/126693234280) |


## [Run #41861557871](https://github.com/sgl-project/sglang/actions/runs/41861557871)
- **分支**: `kimi-k3.1-support`
- **总耗时**: 32.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41861557871

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 9.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809339) |
| multimodal-gen-test-4-npu-a3 (0) | 10.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809363) |
| multimodal-gen-test-4-npu-a3 (1) | 10.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809408) |
| base-b-test-2-npu-a3 / run (0) | 10.4min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809517) |
| multimodal-gen-test-1-npu-a3 (0) | 9.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809550) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809611) |
| base-b-test-16-npu-a3 / run (0) | 10.3min | 超时 | Scheduler watchdog 超时，容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809621) |
| base-b-test-4-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809713) |
| base-b-test-1-npu-a3 / run (0) | 10.3min | 环境问题 | 自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809933) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809339

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809363

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809408

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题；server 启动后作业即被中断，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809517

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见具体 Traceback，但退出码5表示 unittest errors，常见于 setUpClass 时 server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传失败产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809550

- **base-b-test-4-npu-a3 / run (1)**: 日志显示前序用例已通过（Ran 2 tests OK），在启动 test_npu_speculative_multi_npu.py 后报错 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809611

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP8 EP8 Scheduler watchdog timeout（watchdog_timeout=300，soft=True），随后报错“Executing the custom container implementation failed”，作业因调度器看门狗超时失败，属超时类问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809621

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能问题；此前推理日志正常，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809713

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境问题，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809933

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126684679417) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126684679450) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41861557871/job/126685809660) |


## [Run #41805487696](https://github.com/sgl-project/sglang/actions/runs/41805487696)
- **分支**: `yuychang/rocm-kimi-mla-fusion-mxfp4`
- **总耗时**: 61.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41805487696

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.8min | 环境问题 | Git 拉取代码时 CDN 服务返回 502，重试后成功，但作业最终失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127234980836) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 git fetch 访问 git-cdn-service 返回 502 错误，重试后成功检出代码；随后运行 k8s 脚本时作业结束，未见测试执行或明确错误，疑似环境/基础设施问题导致作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127234980836

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127216047488) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127216047509) |
| multimodal-gen-test-1-npu-a3 (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071450) |
| multimodal-gen-test-4-npu-a3 (1) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071457) |
| multimodal-gen-test-1-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071499) |
| base-b-test-1-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071569) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071741) |
| base-b-test-4-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071742) |
| base-b-test-16-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071764) |
| base-b-test-2-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071805) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071873) |
| multimodal-gen-test-4-npu-a3 (0) | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127217071913) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127234980957) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41805487696/job/127234981039) |


## [Run #41796589214](https://github.com/sgl-project/sglang/actions/runs/41796589214)
- **分支**: `k3/hicache-mamba-host-pool`
- **总耗时**: 42.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41796589214

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 24.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856673) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_glm52.py
  链接: https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856673

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127214870571) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127214870606) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856317) |
| multimodal-gen-test-4-npu-a3 (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856383) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856612) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856648) |
| base-b-test-16-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856649) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856710) |
| base-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41796589214/job/127215856715) |


---
*Auto-generated by ci_monitor.py*