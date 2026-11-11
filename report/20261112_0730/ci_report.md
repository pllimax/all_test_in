# NPU CI 执行监控（2026-11-11）
**生成时间**: 2026-11-12 07:23
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-11 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 227

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 2068 个 | 失败 248 个 | 成功 Job 平均耗时 15.0min
- **Run 执行情况**: 成功 133 个 | 失败 94 个 | 成功 Run 平均耗时 63.5min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 74.2min | #42972508749 | [job link](https://github.com/sgl-project/sglang/actions/runs/42972508749/job/130453348392) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 56.6min | #43028556506 | [job link](https://github.com/sgl-project/sglang/actions/runs/43028556506/job/130562726302) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 51.9min | #43003381557 | [job link](https://github.com/sgl-project/sglang/actions/runs/43003381557/job/130477410346) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 51.7min | #43026939232 | [job link](https://github.com/sgl-project/sglang/actions/runs/43026939232/job/130557495568) |
| multimodal-gen-test-4-npu-a3 (0) | 49.4min | #43026939232 | [job link](https://github.com/sgl-project/sglang/actions/runs/43026939232/job/130545403432) |
| multimodal-gen-test-4-npu-a3 (0) | 49.3min | #43027021646 | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614154) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.8min | #43027021646 | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130558681935) |
| multimodal-gen-test-4-npu-a3 (0) | 46.9min | #43027008183 | [job link](https://github.com/sgl-project/sglang/actions/runs/43027008183/job/130545258359) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 45.0min | #43006604646 | [job link](https://github.com/sgl-project/sglang/actions/runs/43006604646/job/130487529672) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 45.0min | #42890889059 | [job link](https://github.com/sgl-project/sglang/actions/runs/42890889059/job/130106428442) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (1) | 64.0min | #42985398644 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407630918) |
| multimodal-gen-test-4-npu-a3 (0) | 45.1min | #42901415249 | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600217) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.1min | #42909600314 | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130172061669) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.5min | #42966776253 | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130355640436) |
| base-b-test-16-npu-a3 / run (0) | 32.0min | #42982694955 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616205) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 31.7min | #42841361446 | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361736701) |
| base-b-test-1-npu-a3 / run (0) | 31.1min | #42866087149 | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214312) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.9min | #43027021646 | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130585097066) |
| base-b-test-1-npu-a3 / run (0) | 29.8min | #42957049132 | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428188) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.2min | #42940197542 | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493420) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-1-npu-a3 / run (0) | 161 | 103 | 40 | 2 | 16 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300120)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022585)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882321)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631021) |
| base-b-test-2-npu-a3 / run (0) | 159 | 127 | 16 | 2 | 14 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300145)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022531)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882362)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631149)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287928) |
| base-b-test-4-npu-a3 / run (0) | 164 | 137 | 9 | 3 | 15 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300118)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022630)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882214)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631146)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616187) |
| base-b-test-16-npu-a3 / run (0) | 139 | 119 | 5 | 5 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022507)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882373)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631189)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616205)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176129) |
| base-b-test-4-npu-a3 / run (1) | 164 | 144 | 6 | 4 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882322)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631167)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616255)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439876)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176183) |
| base-b-test-8-npu-a3 / run (0) | 141 | 128 | 6 | 3 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882437)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631105)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616196)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786087)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160798) |
| multimodal-gen-test-4-npu-a3 (0) | 188 | 172 | 3 | 0 | 13 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43006682848/job/130476747279)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42871417129/job/130024686298)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42849997169/job/129949060003) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 83 | 69 | 3 | 0 | 11 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130585097066)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130527922412)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361736701) |
| multimodal-gen-test-4-npu-a3 (1) | 187 | 174 | 2 | 0 | 11 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407630918)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396785900) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 78 | 71 | 2 | 0 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493420)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130199658241) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 140 | 137 | 1 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130413402213) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `dspark_npu_dispatch.py` | 40 | 10 | 30 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811281)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396166304)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749029) |
| `npu_mla_fia_hicache_bf16.py` | 74 | 64 | 10 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300145)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022531)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882362) |
| `npu_dp_attention.py` | 70 | 61 | 9 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300118)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022630)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882214) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 80 | 74 | 6 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882437)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631105)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616196) |
| `npu_pd_disaggregation.py` | 77 | 71 | 6 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882322)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631167)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616255) |
| `npu_speculative_moe_a2a_backend.py` | 70 | 65 | 5 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022507)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882373)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631189) |
| `npu_hicache_mha.py` | 73 | 69 | 4 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300120)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631021)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786079) |
| `npu_return_indexer_topk_deepseek_v4.py` | 58 | 55 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733139)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439760)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428287) |
| `npu_autoround_moe.py` | 65 | 62 | 3 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882321)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616295)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176113) |
| `minimax_h3_t2va_2npu` | 46 | 43 | 3 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/43006682848/job/130476747279)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42871417129/job/130024686298)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42849997169/job/129949060003) |
| `npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py` | 3 | 0 | 3 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130585097066)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130527922412)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361736701) |
| `npu_tp2_bf16.py` | 61 | 59 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287928)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139049) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 13 | 11 | 2 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493420)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130199658241) |
| `flux_2_image_t2i_2npu` | 48 | 47 | 1 | [multimodal-gen-test-4-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255641) |
| `npu_expert_distribution_recorder_mode.py` | 62 | 61 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587155) |
| `npu_sampling_backend.py` | 66 | 65 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139080) |
| `npu_eagle3.py` | 64 | 63 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022585) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 16 | 15 | 1 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130413402213) |
| `test_qwen38_packed_prefill_selection` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |
| `qwen3.8-flash-next-decode-b2-attn-tp4-cap65536` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |
| `qwen3.8-flash-next-verify-t4-attn-tp8-cap65536` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |
| `paged` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |
| `fia` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |
| `qsa_npu.py` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |
| `TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance` | 1 | 0 | 1 | [multimodal-gen-test-4-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396785900) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43027021646<br>[#49664 [Perf] dflash: Keep a sliding-window MLA draft's KV in a per-request ring](https://github.com/sgl-project/sglang/pull/49664) | `port/dflash-draft-kv-ring` | 114.2min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43027021646) |
| #42969215315<br>[#49621 [Feat] dflash: Serve the Kimi-K3.1 DFlash2 sliding-window MLA draft](https://github.com/sgl-project/sglang/pull/49621) | `port/dflash-k31-draft` | 90.4min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42969215315) |
| #43013108179<br>[#47052 [Perf] [AMD] qwen3: Fuse prefill QK-norm + RoPE on ROCm with the JIT qknorm_rope kernel](https://github.com/sgl-project/sglang/pull/47052) | `perf/qwen3-hip-qknorm-rope` | 88.0min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43013108179) |
| #42989463995<br>[#46855 [Fix] scheduler: Reserve member rows of beam leaders admitted in the same prefill](https://github.com/sgl-project/sglang/pull/46855) | `fix/beam-admission-member-rows` | 81.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42989463995) |
| #42973841319<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 79.7min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42973841319) |
| #42960648144<br>[#49621 [Feat] dflash: Serve the Kimi-K3.1 DFlash2 sliding-window MLA draft](https://github.com/sgl-project/sglang/pull/49621) | `port/dflash-k31-draft` | 79.5min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42960648144) |
| #42983315495<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 76.9min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42983315495) |
| #42909742340 | `oss-sync-91ba7c57b3` | 72.8min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42909742340) |
| #42985398644<br>[#48031 [Feat] [NPU] hicache: Support AIV transfers for MLA and DeepSeek V4](https://github.com/sgl-project/sglang/pull/48031) | `npu/hicache-sparse-copy` | 70.8min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42985398644) |
| #43036392408 | `dark/carv2-symm-workspace` | 70.4min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43036392408) |
| #42940197542<br>[#46185 [Feat] gdn: run DFLASH and DSPARK verify on the ReplaySSM spec ring](https://github.com/sgl-project/sglang/pull/46185) | `codex/av-2` | 66.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42940197542) |
| #42910762862 | `oss-sync-6883c8d753` | 66.1min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42910762862) |
| #42909600314<br>[#49623 [Refactor] scheduler: Each request records the list that holds it](https://github.com/sgl-project/sglang/pull/49623) | `lsyin/sched-pr39` | 63.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42909600314) |
| #42966776253<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 63.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42966776253) |
| #42942998525<br>[#49695 [Refactor] mem_cache: Tag full-only KV frees that release a tree node's value, and commit load-backs through one method](https://github.com/sgl-project/sglang/pull/49695) | `oss-sync-1bff57c019` | 59.9min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42942998525) |
| #42940237319<br>[#45894 [Feat] sampling: Add per-request SynthID Text watermarking](https://github.com/sgl-project/sglang/pull/45894) | `vedantjh2/synthid-oss` | 58.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42940237319) |
| #42918454715 | `port/dflash-draft-kv-ring` | 54.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42918454715) |
| #42901415249<br>[#48777 [Feat] kimi-k3: Shape chat responses to the K3 wire format](https://github.com/sgl-project/sglang/pull/48777) | `lsyin/k3-response-shape` | 48.3min | 2 | multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42901415249) |
| #42923400756<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 46.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42923400756) |
| #42852561384<br>[#49430 [Feat] mem_cache: Evict Mamba states by GreedyDual-Size (--radix-eviction-policy gds)](https://github.com/sgl-project/sglang/pull/49430) | `feat/mamba-hybrid-state-eviction` | 46.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42852561384) |
| #42935787881 | `dark/carv2-symm-workspace` | 46.1min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42935787881) |
| #42919268472<br>[#49623 [Refactor] scheduler: Each request records the list that holds it](https://github.com/sgl-project/sglang/pull/49623) | `lsyin/sched-pr39` | 45.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42919268472) |
| #42938269569<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 44.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42938269569) |
| #42926873675<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 44.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42926873675) |
| #42937755723<br>[#44349 [Feat] beam-search: Add trie head and shared-context attention](https://github.com/sgl-project/sglang/pull/44349) | `feat/trie-head-shared-attention` | 44.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42937755723) |
| #42926566397<br>[#44396 [Perf] kda-replayssm: Reuse the verify-fused commit step indices](https://github.com/sgl-project/sglang/pull/44396) | `mmangkad/kda-replayssm-commit-prepared-step-indices` | 43.6min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42926566397) |
| #42984421655<br>[#49751 [Refactor] scheduler: Remove the remaining direct request-list edits](https://github.com/sgl-project/sglang/pull/49751) | `lsyin/sched-pr41` | 42.6min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42984421655) |
| #42989534605<br>[#47765 [Perf] dflash: Fuse the simulated-acceptance overwrite into one kernel](https://github.com/sgl-project/sglang/pull/47765) | `akhilg/dflash-sim-accept-fused` | 41.5min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42989534605) |
| #42963075912 | `feat/dsv41-native-dynamic-tools` | 40.5min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42963075912) |
| #42860224567 | `refactor/graph-break-recorder` | 39.7min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42860224567) |
| #42943098980<br>[#49677 [Refactor] scheduler: Edit request lists only through move and the retirer](https://github.com/sgl-project/sglang/pull/49677) | `lsyin/sched-pr40` | 39.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42943098980) |
| #43017336310<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 39.3min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43017336310) |
| #42982694955<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 38.8min | 6 | base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42982694955) |
| #42907077802<br>[#45737 [Feat] kv-events: Report caller multimodal routing labels as block spans](https://github.com/sgl-project/sglang/pull/45737) | `feat/mm-routing-label-spans` | 38.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42907077802) |
| #43019232629<br>[#49277 [Fix] [NPU] MoE: Optimize Ascend MoE AllGather](https://github.com/sgl-project/sglang/pull/49277) | `main` | 38.5min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43019232629) |
| #42960338368<br>[#49704 [Perf] [AMD] muse-spark: Prefill and decode optimization](https://github.com/sgl-project/sglang/pull/49704) | `pr/muse-spark-prefill-decode-opt` | 38.3min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42960338368) |
| #42879327215<br>[#33111 [Feat] elastic-ep: Runtime scale-down that retires EP ranks via Mooncake deactivate_ranks](https://github.com/sgl-project/sglang/pull/33111) | `qkang/elastic-ep-mooncake-scale-down` | 38.1min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42879327215) |
| #42962896376<br>[#35259 [Fix] model-loader: Harden startup weight-load overlap and expand coverage](https://github.com/sgl-project/sglang/pull/35259) | `startup-weight-load-overlap-hardening` | 37.5min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42962896376) |
| #42948726151<br>[#40333 [Feat] [NVIDIA] deepseek-v4.1: Support prefill CP with BCG in PD serving (2/N)](https://github.com/sgl-project/sglang/pull/40333) | `main-v4.1-cp-bcg` | 37.1min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42948726151) |
| #42919759545<br>[#35259 [Fix] model-loader: Harden startup weight-load overlap and expand coverage](https://github.com/sgl-project/sglang/pull/35259) | `startup-weight-load-overlap-hardening` | 36.9min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42919759545) |
| #42913868826<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 36.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42913868826) |
| #42905897886 | `feat/dsv41-native-dynamic-tools` | 36.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42905897886) |
| #43040565381<br>[#48648 [Perf] [AMD] Qwen4-Exp/HC: Fuse decode-sized hyper-connection norm and inject into FlyDSL mix](https://github.com/sgl-project/sglang/pull/48648) | `perf/amd-qwen4-fused-hc-decode` | 35.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43040565381) |
| #42996093563<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 35.6min | 6 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42996093563) |
| #42866087149 | `xpu/weekly-simple-model-enablement-2026-11-09` | 35.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42866087149) |
| #42910541209<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 34.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42910541209) |
| #42956860020 | `refactor/graph-break-recorder` | 34.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42956860020) |
| #42962827591 | `refactor/graph-break-recorder` | 33.8min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42962827591) |
| #42998159633<br>[#45643 [Feat] metrics: count requests that meet latency SLOs for goodput](https://github.com/sgl-project/sglang/pull/45643) | `pr/goodput-metric` | 33.6min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42998159633) |
| #42957049132<br>[#49621 [Feat] dflash: Serve the Kimi-K3.1 DFlash2 sliding-window MLA draft](https://github.com/sgl-project/sglang/pull/49621) | `port/dflash-k31-draft` | 33.3min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42957049132) |
| #42982959437<br>[#49621 [Feat] dflash: Serve the Kimi-K3.1 DFlash2 sliding-window MLA draft](https://github.com/sgl-project/sglang/pull/49621) | `port/dflash-k31-draft` | 32.3min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42982959437) |
| #42841361446<br>[#44492 [Feat] [AMD] mori: Run MORI EPv2 dispatch/combine on AsyncLL kernels for TBO](https://github.com/sgl-project/sglang/pull/44492) | `mori_epv2_asyncll_tbo` | 32.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42841361446) |
| #42903786738<br>[#49564 [CI] diffusion: Stabilize test execution and resource usage](https://github.com/sgl-project/sglang/pull/49564) | `codex/fix-health-wait-cascade-1110` | 30.7min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42903786738) |
| #42951176938<br>[#47221 [Perf] dsa: Elide shared-layer index-K under HiSparse decode to raise batch size](https://github.com/sgl-project/sglang/pull/47221) | `feature/dsa-index-k-elision-hisparse-decode` | 29.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42951176938) |
| #42926786352<br>[#49677 [Refactor] scheduler: Edit request lists only through move and the retirer](https://github.com/sgl-project/sglang/pull/49677) | `lsyin/sched-pr40` | 28.7min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42926786352) |
| #42902609396<br>[#49496 [Refactor] scheduler: Move a request between owner lists in one call](https://github.com/sgl-project/sglang/pull/49496) | `lsyin/sched-pr38` | 28.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42902609396) |
| #42947247676<br>[#43527 [Feat] QSA: Add cache sharding for Qwen3.8 hybrid models](https://github.com/sgl-project/sglang/pull/43527) | `feat/qsa-cache-sharding` | 28.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42947247676) |
| #42928094258<br>[#46186 [Perf] spec: radix top-k for speculative verify target probabilities](https://github.com/sgl-project/sglang/pull/46186) | `codex/av-3` | 28.0min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42928094258) |
| #42893677681 | `amd/aiter-gdn-chunked-prefill` | 27.8min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42893677681) |
| #42922509692<br>[#43360 [Feat] [AMD] fp4: Select the Quark MXFP4 dense GEMM with --fp4-gemm-backend aiter|triton](https://github.com/sgl-project/sglang/pull/43360) | `feat/cli-fp4-gemm-backend-aiter-triton` | 27.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42922509692) |
| #42943259440<br>[#45320 [Perf] [AMD] aiter: Run 12-head MLA decode and 8-token verify on fp8-Q ASM](https://github.com/sgl-project/sglang/pull/45320) | `k3-mla-fp8-q-asm` | 27.4min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42943259440) |
| #43016895553<br>[#37570 [Feat] [NPU] Qwen3.8-Flash-Next: Support graph replay, MTP, and Triton kernels](https://github.com/sgl-project/sglang/pull/37570) | `pr-36601` | 27.1min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43016895553) |
| #42960854852<br>[#49677 [Refactor] scheduler: Edit request lists only through move and the retirer](https://github.com/sgl-project/sglang/pull/49677) | `lsyin/sched-pr40` | 27.1min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42960854852) |
| #42979747154<br>[#49621 [Feat] dflash: Serve the Kimi-K3.1 DFlash2 sliding-window MLA draft](https://github.com/sgl-project/sglang/pull/49621) | `port/dflash-k31-draft` | 26.7min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42979747154) |
| #42967434877<br>[#44447 [Feat] KVShard: Enable KV cache sharding for Qwen3.8 Flash Next](https://github.com/sgl-project/sglang/pull/44447) | `kvshard/qwen38-flash-next` | 25.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42967434877) |
| #42792156440 | `dark/carv2-symm-workspace` | 25.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42792156440) |
| #42963715520<br>[#49677 [Refactor] scheduler: Edit request lists only through move and the retirer](https://github.com/sgl-project/sglang/pull/49677) | `lsyin/sched-pr40` | 25.4min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42963715520) |
| #42929097955 | `port/dflash-draft-kv-ring` | 25.3min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42929097955) |
| #42994459197<br>[#45643 [Feat] metrics: count requests that meet latency SLOs for goodput](https://github.com/sgl-project/sglang/pull/45643) | `pr/goodput-metric` | 25.0min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42994459197) |
| #42820342485<br>[#43851 [Feat] [NVIDIA] dsv4.1: [1/N] Add packed FP4 Main KV storage for Hopper.](https://github.com/sgl-project/sglang/pull/43851) | `feat/dsv41-packed-main-kv` | 24.8min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42820342485) |
| #42961915568<br>[#49715 [Refactor] mm: import MM_PAD_SHIFT_VALUE instead of re-declaring it](https://github.com/sgl-project/sglang/pull/49715) | `mm-pad-shift-single-source` | 24.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42961915568) |
| #42862746462<br>[#42978 [Feat] [NPU] dsa: Token shard, every head for this rank's slice of the tokens (2/2)](https://github.com/sgl-project/sglang/pull/42978) | `npu-dsa-token-shard` | 24.7min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42862746462) |
| #42941580649<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 24.1min | 6 | base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42941580649) |
| #42935786405<br>[#49370 [Refactor] custom-ar-v2: Move the DPX pair stages into their own header](https://github.com/sgl-project/sglang/pull/49370) | `dark/carv2-dpx-pair-header` | 23.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42935786405) |
| #43006682848<br>[#49353 [Perf] [NPU] MiniMax-H3: optimize RMSNorm and SwiGLU](https://github.com/sgl-project/sglang/pull/49353) | `minimax_npu_rmsnorm_path` | 21.9min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43006682848) |
| #42930546073<br>[#49566 [Perf] [AMD] rotary_embedding: tile fused RoPE and KV write for large T on gfx1250](https://github.com/sgl-project/sglang/pull/49566) | `pr-gfx1250-fused-rope-kv-tiled` | 21.9min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42930546073) |
| #43025718555 | `fix_npu_diffusion_failure_analyzer` | 19.5min | 9 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43025718555) |
| #42910832969<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 19.4min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42910832969) |
| #42936005713<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 18.4min | 5 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42936005713) |
| #42980546125<br>[#43312 [Feat] [XPU] LongCat-Flash: Enable on Intel XPU and fix stale ngram skip mask in decode](https://github.com/sgl-project/sglang/pull/43312) | `xpu/longcat-flash-ngram` | 17.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42980546125) |
| #42871417129<br>[#49353 [Perf] [NPU] MiniMax-H3: optimize RMSNorm and SwiGLU](https://github.com/sgl-project/sglang/pull/49353) | `minimax_npu_rmsnorm_path` | 17.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42871417129) |
| #43040345382<br>[#48412 [Feat] pp: Relay routed experts through pipeline-parallel stages](https://github.com/sgl-project/sglang/pull/48412) | `pp-routed-experts-relay` | 17.1min | 8 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-1-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43040345382) |
| #42992547635<br>[#44883 [Feat] [NPU] multimodal: Enable device-side multimodal feature transport via torch_npu IPC](https://github.com/sgl-project/sglang/pull/44883) | `main` | 16.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42992547635) |
| #42849997169 | `minimax_npu_rmsnorm_path` | 13.7min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42849997169) |
| #42970139826<br>[#49677 [Refactor] scheduler: Edit request lists only through move and the retirer](https://github.com/sgl-project/sglang/pull/49677) | `lsyin/sched-pr40` | 12.8min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42970139826) |
| #42917966949<br>[#35259 [Fix] model-loader: Harden startup weight-load overlap and expand coverage](https://github.com/sgl-project/sglang/pull/35259) | `startup-weight-load-overlap-hardening` | 12.8min | 9 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42917966949) |
| #42982477905<br>[#47308 [Fix] scheduler: reserve SPF capacity against both token budgets](https://github.com/sgl-project/sglang/pull/47308) | `wuyaole/fix-prefill-reservation-budget` | 11.4min | 4 | multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42982477905) |
| #42930415612<br>[#48778 [Fix] multimodal: Fail bad client media with a client error](https://github.com/sgl-project/sglang/pull/48778) | `lsyin/media-input-errors` | 11.0min | 7 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42930415612) |
| #42977245206<br>[#49758 [Fix] tokenizer_manager: Reject logprob_start_len below -1 with a 400](https://github.com/sgl-project/sglang/pull/49758) | `lsyin/validate-logprob-start-len` | 8.7min | 4 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42977245206) |
| #42977240998<br>[#49756 [Fix] server_args: Reject --scheduler-recv-interval above 1 with pipeline parallelism](https://github.com/sgl-project/sglang/pull/49756) | `lsyin/pp-reject-recv-interval` | 8.3min | 4 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42977240998) |
| #43049611662 | `fix_npu_diffusion_failure_analyzer` | 7.3min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43049611662) |
| #42971799630 | `rbrugaro/mla-absorb-bf16` | 7.0min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42971799630) |
| #43050738323 | `fix_npu_diffusion_failure_analyzer` | 6.3min | 10 | multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43050738323) |
| #42971584723<br>[#49677 [Refactor] scheduler: Edit request lists only through move and the retirer](https://github.com/sgl-project/sglang/pull/49677) | `lsyin/sched-pr40` | 5.0min | 8 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42971584723) |

---


## [Run #43050738323](https://github.com/sgl-project/sglang/actions/runs/43050738323)
- **分支**: `fix_npu_diffusion_failure_analyzer`
- **总耗时**: 6.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43050738323

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 2.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587089) |
| base-b-test-16-npu-a3 / run (0) | 2.2min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587106) |
| multimodal-gen-test-4-npu-a3 (1) | 2.7min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587145) |
| multimodal-gen-test-4-npu-a3 (0) | 2.6min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587164) |
| multimodal-gen-test-1-npu-a3 (0) | 2.6min | 环境问题 | 作业日志中未见测试执行错误，仅提示未找到 diffusion-failures/ 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587172) |
| base-b-test-8-npu-a3 / run (0) | 2.4min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587189) |
| base-b-test-4-npu-a3 / run (0) | 2.0min | 环境问题 | 测试日志文件未生成，疑似测试进程异常退出导致无日志可上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587254) |
| base-b-test-4-npu-a3 / run (1) | 2.1min | 环境问题 | 测试日志文件未生成，用例脚本退出码5，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587287) |
| base-b-test-2-npu-a3 / run (0) | 2.7min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587288) |
| base-b-test-1-npu-a3 / run (0) | 2.6min | 环境问题 | 测试日志文件未生成，用例脚本异常退出，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587349) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587089

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无产物上传；结合退出码 5 及 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL）的常见原因，判断为环境/资源问题导致测试未正常执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587106

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅含 runner 初始化、action 下载与清理，无 unittest 输出或 Traceback；upload-artifact 提示未找到 diffusion-failures/ 路径，说明测试脚本未产生失败产物，作业可能因环境/启动问题未真正运行用例。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587145

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，缺少真实错误信息；仅见 upload-artifact 提示未找到 diffusion-failures/ 路径，无 Traceback 或退出码 5 的用例错误，无法确认具体失败原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587164

- **multimodal-gen-test-1-npu-a3 (0)**: 日志仅显示 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，未出现 Traceback 或退出码 5 等真实错误，失败原因信息不足，疑似测试未产生预期产物目录或作业提前结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587172

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），但日志中未见具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587189

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无产物上传；结合退出码5提示 unittest errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致测试未产生日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587254

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 unittest 出现 errors。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587287

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志中未捕获具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587288

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无测试产物上传；结合退出码 5 提示 unittest 存在 errors，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略部分确认 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130628587349

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130627330411) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43050738323/job/130627330496) |


## [Run #43049611662](https://github.com/sgl-project/sglang/actions/runs/43049611662)
- **分支**: `fix_npu_diffusion_failure_analyzer`
- **总耗时**: 7.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43049611662

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 3.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624652837) |
| multimodal-gen-test-4-npu-a3 (0) | 3.5min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624652927) |
| multimodal-gen-test-4-npu-a3 (1) | 3.9min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624652968) |
| base-b-test-16-npu-a3 / run (0) | 3.9min | 环境问题 | 日志中未见测试执行失败的具体错误，作业在 artifact 上传后正常清理，失败原因需查看省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653016) |
| base-b-test-2-npu-a3 / run (0) | 3.9min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653026) |
| multimodal-gen-test-1-npu-a3 (1) | 3.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653045) |
| base-b-test-8-npu-a3 / run (0) | 3.9min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653175) |
| base-b-test-4-npu-a3 / run (1) | 4.0min | 环境问题 | 测试日志文件未生成，用例脚本异常退出，疑似 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653240) |
| base-b-test-1-npu-a3 / run (0) | 3.9min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653252) |
| base-b-test-4-npu-a3 / run (0) | 4.0min | 环境问题 | 日志中未见测试执行失败的具体错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653854) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例未正常产出结果。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624652837

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中未见具体 Traceback，但退出码5表示 unittest errors，常见于 setUpClass 时 server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624652927

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业在约3分钟内结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624652968

- **base-b-test-16-npu-a3 / run (0)**: 可见部分仅显示 checkout、artifact 上传成功及 Node.js 弃用警告，无 Traceback/RuntimeError。退出码 5 提示 unittest errors，可能为 setUpClass 中 sglang server 启动失败（如 OOM/SIGKILL），但需查看省略日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653016

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无产物上传；结合退出码 5 推断 setUpClass 阶段 server 启动失败（如 OOM 或进程被 SIGKILL），但日志中未捕获具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653026

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact，说明测试用例执行失败。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653045

- **base-b-test-8-npu-a3 / run (0)**: 可见日志仅包含 runner 初始化、action 下载、artifact 上传（176字节）和清理阶段，中间省略部分才是测试执行与报错所在。退出码5提示 unittest 存在 errors，通常为 setUpClass 中 sglang server 启动失败，但需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653175

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 无文件可上传，说明测试脚本未正常产出日志；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志中未捕获到具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653240

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无产物上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM 或进程被 SIGKILL），但日志中未出现具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653252

- **base-b-test-4-npu-a3 / run (0)**: 可见日志仅包含 runner 初始化、action 下载、artifact 上传（176字节）和清理，无 Traceback/RuntimeError。退出码5对应 unittest errors，通常为 setUpClass 中 sglang server 启动失败（如 OOM/SIGKILL），但具体错误在被省略的中间日志中，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130624653854

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130623132296) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43049611662/job/130623132416) |


## [Run #43040565381](https://github.com/sgl-project/sglang/actions/runs/43040565381)
- **分支**: `perf/amd-qwen4-fused-hc-decode`
- **总耗时**: 35.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43040565381

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 22.0min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500342) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500886) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示用例以退出码5结束（FAILED errors=N），且未生成 diffusion-failures 目录产物，说明测试在 setUpClass 阶段即失败，常见原因为 server 启动失败（host OOM 或进程被 SIGKILL）。日志中未见具体 Traceback，需查看省略部分确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500342


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130591171810) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130591171928) |
| multimodal-gen-test-1-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500379) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500423) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500464) |
| base-b-test-2-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500671) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500747) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500795) |
| base-b-test-4-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500817) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040565381/job/130592500859) |


## [Run #43040345382](https://github.com/sgl-project/sglang/actions/runs/43040345382)
- **分支**: `pp-routed-experts-relay`
- **总耗时**: 17.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43040345382

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 11.0min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666423) |
| multimodal-gen-test-1-npu-a3 (0) | 10.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666443) |
| base-b-test-1-npu-a3 / run (0) | 13.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型权重加载后被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666574) |
| multimodal-gen-test-4-npu-a3 (0) | 5.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666591) |
| multimodal-gen-test-4-npu-a3 (1) | 10.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666624) |
| base-b-test-16-npu-a3 / run (0) | 13.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666631) |
| base-b-test-4-npu-a3 / run (0) | 13.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666724) |
| base-b-test-2-npu-a3 / run (0) | 13.6min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666743) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约10分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666423

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666443

- **base-b-test-1-npu-a3 / run (0)**: 日志显示权重分片加载完成后报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码错误，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666574

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中未见具体 Traceback，但退出码5表明 unittest 有 errors，常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，artifact 未上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666591

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约10分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666624

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP12/EP12 等进程启动后约3分钟出现 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码错误；随后进入清理阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666631

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，并非用例代码或精度问题；此前推理日志正常，随后容器执行报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666724

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在第3个测试文件开始后约20秒，属于 runner/容器基础设施故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666743

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130590440788) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130590440827) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666727) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43040345382/job/130591666886) |


## [Run #43036392408](https://github.com/sgl-project/sglang/actions/runs/43036392408)
- **分支**: `dark/carv2-symm-workspace`
- **总耗时**: 70.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43036392408

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在性能测试中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130610131054) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 8.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130610131240) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示性能测试（Capturing batches）进行到约82%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码或精度/性能回归问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130610131054

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 Capturing batches 阶段后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130610131240

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130576494845) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130576494848) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577870517) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577870548) |
| multimodal-gen-test-4-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577870632) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577870793) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577870850) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577871011) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577871060) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577871258) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577871823) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130577872180) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130591805336) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130591805369) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43036392408/job/130591805411) |


## [Run #43027021646](https://github.com/sgl-project/sglang/actions/runs/43027021646)
- **分支**: `port/dflash-draft-kv-ring`
- **总耗时**: 114.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43027021646

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.9min | 性能回归 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130585097066) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 3 个性能用例中 1 个通过、1 个失败（w8a8 64k 通过，1024x1024_30_out1024 用例 exit code 1，耗时 911s）。日志省略了具体 Traceback，无法确认是性能不达标还是 server 启动异常，需查看该用例详细输出。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130585097066

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130544415259) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130544415453) |
| multimodal-gen-test-4-npu-a3 (1) | 38.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614066) |
| multimodal-gen-test-4-npu-a3 (0) | 49.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614154) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614208) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614286) |
| base-b-test-1-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614345) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614346) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614433) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545614485) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545615434) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130545616883) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130558681935) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130558682102) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130558682191) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43027021646/job/130585096694) |


## [Run #43025718555](https://github.com/sgl-project/sglang/actions/runs/43025718555)
- **分支**: `fix_npu_diffusion_failure_analyzer`
- **总耗时**: 19.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43025718555

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 15.4min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541360841) |
| multimodal-gen-test-4-npu-a3 (0) | 15.7min | 环境问题 | 多模态生成测试用例执行失败，上传了diffusion-failures产物，疑似server启动失败导致unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541360872) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541360878) |
| multimodal-gen-test-4-npu-a3 (1) | 15.6min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361045) |
| base-b-test-1-npu-a3 / run (0) | 15.8min | 其他 | 日志片段未包含实际测试失败信息，仅显示产物上传与清理成功，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361100) |
| base-b-test-4-npu-a3 / run (0) | 15.4min | 环境问题 | 日志中未见测试失败的具体错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361117) |
| base-b-test-4-npu-a3 / run (1) | 14.9min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361213) |
| base-b-test-2-npu-a3 / run (0) | 15.8min | 其他 | 日志末尾仅显示清理与 Node.js 弃用警告，未包含实际测试失败的错误信息，无法定位具体原因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361233) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | 其他 | 日志片段未包含实际测试失败信息，仅显示产物上传和清理成功 | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361322) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示作业退出并上传 diffusion-failures-npu-1-part1-1.zip 失败产物，说明测试用例执行出错（退出码 5，unittest errors）。中间省略部分应含 Traceback/RuntimeError，最常见为 setUpClass 阶段 sglang server 启动失败（host OOM 或进程被 SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541360841

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，未见具体Traceback；但作业上传了diffusion-failures-npu-2-part0-1.zip失败产物，且用例退出码5对应unittest errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。需查看省略段日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541360872

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part0-1.zip 失败工件，作业以非零退出。结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段中的 Traceback/RuntimeError 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541360878

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part1-1.zip 失败产物，退出码 5 提示 unittest 存在 errors，常见于 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361045

- **base-b-test-1-npu-a3 / run (0)**: 可见日志均为 runner 初始化、下载 action、上传 artifact 和 post job 清理，未出现 Traceback/RuntimeError 或退出码 5 的上下文；中间省略部分可能含真实错误，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361100

- **base-b-test-4-npu-a3 / run (0)**: 可见日志仅显示 checkout、artifact 上传成功及 post job cleanup，无 Traceback/RuntimeError。退出码 5 提示 unittest errors，可能为 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），但真实错误在被省略的中间日志中，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361117

- **base-b-test-4-npu-a3 / run (1)**: 可见日志仅包含 runner 初始化、action 下载、artifact 上传和清理等正常步骤，中间省略部分未显示 Traceback/RuntimeError 等真实错误，无法判断是 setUpClass 启动失败还是其他原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361213

- **base-b-test-2-npu-a3 / run (0)**: 日志中段被省略，可见部分只有 artifact 上传成功和 post job cleanup，没有 Traceback/RuntimeError 或退出码 5 的上下文，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361233

- **base-b-test-16-npu-a3 / run (0)**: 提供的日志被省略了中间部分，可见内容只有 runner 初始化、下载 action、上传 artifact 和 post job cleanup，均正常完成，没有 Traceback/RuntimeError 或退出码 5 的相关记录，无法定位具体失败原因，需查看省略的测试执行段日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361322

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130540031601) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130540031605) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43025718555/job/130541361178) |


## [Run #43019232629](https://github.com/sgl-project/sglang/actions/runs/43019232629)
- **分支**: `main`
- **总耗时**: 38.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43019232629

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300118) |
| base-b-test-1-npu-a3 / run (0) | 6.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300120) |
| base-b-test-2-npu-a3 / run (0) | 6.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300145) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300118

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300120

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300145

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130518111596) |
| multimodal-gen-test-1-npu-a3 (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519299929) |
| multimodal-gen-test-4-npu-a3 (0) | 35.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519299993) |
| multimodal-gen-test-4-npu-a3 (1) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300000) |
| multimodal-gen-test-1-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300012) |
| base-b-test-16-npu-a3 / run (0) | 28.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300110) |
| base-b-test-8-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300166) |
| base-b-test-4-npu-a3 / run (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43019232629/job/130519300279) |


## [Run #43017336310](https://github.com/sgl-project/sglang/actions/runs/43017336310)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 39.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43017336310

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 25.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022507) |
| base-b-test-2-npu-a3 / run (0) | 7.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022531) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022585) |
| base-b-test-4-npu-a3 / run (0) | 12.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022630) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022507

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022531

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022585

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022630

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130511792424) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130511792827) |
| multimodal-gen-test-4-npu-a3 (0) | 35.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022330) |
| multimodal-gen-test-4-npu-a3 (1) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022343) |
| multimodal-gen-test-1-npu-a3 (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022352) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022491) |
| multimodal-gen-test-1-npu-a3 (1) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022570) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43017336310/job/130513022605) |


## [Run #43016895553](https://github.com/sgl-project/sglang/actions/runs/43016895553)
- **分支**: `pr-36601`
- **总耗时**: 27.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43016895553

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.8min | 代码错误 | test_qsa_npu.py 用例执行失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/attention/qsa/test_qsa_npu.py 的 passed 为 false（耗时 40s），其余用例均通过，最终进程以退出码 1 结束。需查看该用例的 Traceback 以定位具体失败原因。
  - 失败用例: test_qwen38_packed_prefill_selection, qwen3.8-flash-next-decode-b2-attn-tp4-cap65536, qwen3.8-flash-next-verify-t4-attn-tp8-cap65536, paged, fia
  链接: https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270967

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130537190336) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130537190392) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270342) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270364) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270605) |
| base-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270657) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270687) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270772) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43016895553/job/130538270976) |


## [Run #43013108179](https://github.com/sgl-project/sglang/actions/runs/43013108179)
- **分支**: `perf/qwen3-hip-qknorm-rope`
- **总耗时**: 88.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43013108179

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 21.9min | 其他 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 运行约1074秒后以退出码1失败，3个用例全部未通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130527922412) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本返回 exit code 1，Test Summary 为 0/3 passed，耗时约1074秒。中间省略部分可能含真实 Traceback，需查看完整日志确认是 server 启动失败、OOM 还是性能阈值未达标。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130527922412

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130497581409) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130497581570) |
| multimodal-gen-test-1-npu-a3 (1) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737358) |
| multimodal-gen-test-1-npu-a3 (0) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737371) |
| multimodal-gen-test-4-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737377) |
| multimodal-gen-test-4-npu-a3 (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737406) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737456) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737532) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737599) |
| base-b-test-4-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737623) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737656) |
| base-b-test-1-npu-a3 / run (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130498737680) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130512449143) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130512449173) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130512449208) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43013108179/job/130527922427) |


## [Run #43006682848](https://github.com/sgl-project/sglang/actions/runs/43006682848)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 21.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43006682848

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 14.0min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43006682848/job/130476747279) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；作业退出码 5 表示 unittest 存在 errors，最常见为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。已上传 diffusion-failures-npu-2-part0-1.zip 产物，需查看该产物中的真实错误定位。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43006682848/job/130476747279

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43006682848/job/130475980832) |
| multimodal-gen-test-4-npu-a3 (1) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43006682848/job/130476747207) |


## [Run #42998159633](https://github.com/sgl-project/sglang/actions/runs/42998159633)
- **分支**: `pr/goodput-metric`
- **总耗时**: 33.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42998159633

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 18.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130453522456) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，并非用例或代码本身失败；此前推理请求均返回 200。
  链接: https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130453522456

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130447693003) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130447693079) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130448759678) |
| base-b-test-1-npu-a3 / run (0) | 6.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130448759708) |
| base-b-test-2-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130448759731) |
| base-b-test-4-npu-a3 / run (1) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130448759748) |
| base-b-test-4-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42998159633/job/130448760012) |


## [Run #42996093563](https://github.com/sgl-project/sglang/actions/runs/42996093563)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 35.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42996093563

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 13.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882214) |
| base-b-test-1-npu-a3 / run (0) | 13.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882321) |
| base-b-test-4-npu-a3 / run (1) | 14.6min | 环境问题 | PD分离测试用例执行失败，退出码5表明unittest存在errors，疑似setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882322) |
| base-b-test-2-npu-a3 / run (0) | 7.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882362) |
| base-b-test-16-npu-a3 / run (0) | 20.4min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882373) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882437) |

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882214

- **base-b-test-1-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882321

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py运行638秒后返回exit code 5，0/2通过。退出码5表示unittest有errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882322

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882362

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882373

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882437

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130472718110) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130472718517) |
| multimodal-gen-test-1-npu-a3 (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882082) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882129) |
| multimodal-gen-test-4-npu-a3 (0) | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882233) |
| multimodal-gen-test-1-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42996093563/job/130473882247) |


## [Run #42994459197](https://github.com/sgl-project/sglang/actions/runs/42994459197)
- **分支**: `pr/goodput-metric`
- **总耗时**: 25.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42994459197

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 10.9min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130442162019) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 Decode 阶段正常输出后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，非用例代码或性能问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130442162019

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130435862168) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130435862226) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130436755816) |
| base-b-test-4-npu-a3 / run (1) | 7.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130436755971) |
| base-b-test-1-npu-a3 / run (0) | 6.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130436755995) |
| base-b-test-4-npu-a3 / run (0) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130436756043) |
| base-b-test-2-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994459197/job/130436756798) |


## [Run #42992547635](https://github.com/sgl-project/sglang/actions/runs/42992547635)
- **分支**: `main`
- **总耗时**: 16.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42992547635

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822424) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822428) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822479) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822517) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822573) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822580) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130428878490) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130428878532) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822247) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42992547635/job/130429822318) |


## [Run #42989534605](https://github.com/sgl-project/sglang/actions/runs/42989534605)
- **分支**: `akhilg/dflash-sim-accept-fused`
- **总耗时**: 41.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42989534605

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130432746001) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.0min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130432746220) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试运行中（decode 正常，吞吐约 206 token/s）突然报错 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130432746001

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，并非用例断言失败；测试进行中作业被中断，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130432746220

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130419597647) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130419597652) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631702) |
| multimodal-gen-test-1-npu-a3 (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631737) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631827) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631921) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631953) |
| multimodal-gen-test-4-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631960) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420631979) |
| base-b-test-16-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420632020) |
| base-b-test-4-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420632028) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130420632310) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989534605/job/130432746129) |


## [Run #42989463995](https://github.com/sgl-project/sglang/actions/runs/42989463995)
- **分支**: `fix/beam-admission-member-rows`
- **总耗时**: 81.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42989463995

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 14.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130480530200) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 9.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130480530297) |


- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器实现异常，并非用例断言失败；此前 perf 测试仍在正常输出 prefill 吞吐，随后容器执行报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130480530297

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130449646242) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130449646305) |
| multimodal-gen-test-4-npu-a3 (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810020) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810031) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810074) |
| base-b-test-16-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810160) |
| base-b-test-8-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810168) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810208) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810290) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130450810291) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130461964520) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130461964548) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 39.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42989463995/job/130461964573) |


## [Run #42985398644](https://github.com/sgl-project/sglang/actions/runs/42985398644)
- **分支**: `npu/hicache-sparse-copy`
- **总耗时**: 70.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42985398644

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 64.0min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407630918) |
| base-b-test-1-npu-a3 / run (0) | 4.9min | 代码错误 | HiCache MHA 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631021) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631105) |
| base-b-test-4-npu-a3 / run (0) | 5.4min | 环境问题 | NPU DP attention 测试用例退出码5，setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631146) |
| base-b-test-2-npu-a3 / run (0) | 5.3min | 环境问题 | 测试脚本返回退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631149) |
| base-b-test-4-npu-a3 / run (1) | 14.9min | 环境问题 | PD分离测试脚本退出码5，setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631167) |
| base-b-test-16-npu-a3 / run (0) | 8.3min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631189) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例以退出码5结束（unittest errors），且未生成 diffusion-failures 目录产物。常见原因为 setUpClass 中 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略部分的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407630918

- **base-b-test-1-npu-a3 / run (0)**: test_npu_hicache_mha.py 启动 HiCache 服务后运行失败，返回 exit code 1，9 个用例 0 通过，耗时 62 秒，属测试用例本身失败而非超时或环境问题。
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631021

- **base-b-test-8-npu-a3 / run (0)**: test_npu_eplb_min_rebalancing_utilization_threshold.py返回exit code 5，表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631105

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 返回 exit code 5，表示 unittest 存在 errors，通常为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 0/2 用例通过。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631146

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回 exit code 5，表示 unittest 存在 errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 0/8 用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631149

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行639秒后返回exit code 5，表明unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631167

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行93秒后返回退出码1，测试汇总0/1通过。日志省略了具体Traceback，需查看该用例完整输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407631189

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130406595510) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130406595521) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42985398644/job/130407630985) |


## [Run #42984421655](https://github.com/sgl-project/sglang/actions/runs/42984421655)
- **分支**: `lsyin/sched-pr41`
- **总耗时**: 42.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42984421655

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 17.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287928) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_tp2_bf16.py, npu_tp2_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287928

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130402264240) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130402264525) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287768) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287881) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287893) |
| base-b-test-4-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287896) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287908) |
| base-b-test-1-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287951) |
| base-b-test-16-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42984421655/job/130403287953) |


## [Run #42983315495](https://github.com/sgl-project/sglang/actions/runs/42983315495)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 76.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42983315495

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 10.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130413402213) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130413402213

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130398853856) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130398853862) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399608699) |
| multimodal-gen-test-4-npu-a3 (1) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399608759) |
| multimodal-gen-test-4-npu-a3 (0) | 35.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399608809) |
| multimodal-gen-test-1-npu-a3 (1) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399608821) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399608929) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399608935) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399609067) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399609088) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399609098) |
| base-b-test-2-npu-a3 / run (0) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130399609132) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130413402167) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 39.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42983315495/job/130413402242) |


## [Run #42982959437](https://github.com/sgl-project/sglang/actions/runs/42982959437)
- **分支**: `port/dflash-k31-draft`
- **总耗时**: 32.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42982959437

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 11.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587155) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587155

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130397723231) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130397723239) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587052) |
| base-b-test-1-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587147) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587150) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587205) |
| base-b-test-16-npu-a3 / run (0) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587213) |
| base-b-test-4-npu-a3 / run (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587273) |
| base-b-test-4-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982959437/job/130398587460) |


## [Run #42982694955](https://github.com/sgl-project/sglang/actions/runs/42982694955)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 38.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42982694955

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616187) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616196) |
| base-b-test-16-npu-a3 / run (0) | 32.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616205) |
| base-b-test-4-npu-a3 / run (1) | 14.7min | 环境问题 | PD分离测试用例退出码5，setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616255) |
| base-b-test-1-npu-a3 / run (0) | 14.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616295) |
| base-b-test-2-npu-a3 / run (0) | 7.2min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616333) |

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616187

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616196

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616205

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行639秒后返回exit code 5，表明unittest存在errors，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/2用例通过。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616255

- **base-b-test-1-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616295

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616333

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130396746131) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130396746155) |
| multimodal-gen-test-1-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616022) |
| multimodal-gen-test-1-npu-a3 (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616081) |
| multimodal-gen-test-4-npu-a3 (0) | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616118) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982694955/job/130397616164) |


## [Run #42982477905](https://github.com/sgl-project/sglang/actions/runs/42982477905)
- **分支**: `wuyaole/fix-prefill-reservation-budget`
- **总耗时**: 11.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42982477905

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 8.1min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396785900) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786061) |
| base-b-test-1-npu-a3 / run (0) | 6.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786079) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786087) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786132) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786137) |
| base-b-test-2-npu-a3 / run (0) | 7.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786139) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以unittest errors退出（退出码5），最常见原因是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  - 失败用例: TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance, TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance, TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance, TestGlmImageDistributedNpu::test_external_ar_batching_multi_output_disaggregation_performance
  链接: https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396785900


- **base-b-test-1-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786079

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786087



- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786139

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396033090) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396033410) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42982477905/job/130396786002) |


## [Run #42980546125](https://github.com/sgl-project/sglang/actions/runs/42980546125)
- **分支**: `xpu/longcat-flash-ngram`
- **总耗时**: 17.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42980546125

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 1.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598300) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598323) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598328) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598354) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598392) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598414) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130389860586) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130389860630) |
| multimodal-gen-test-4-npu-a3 (1) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598153) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42980546125/job/130390598332) |


## [Run #42979747154](https://github.com/sgl-project/sglang/actions/runs/42979747154)
- **分支**: `port/dflash-k31-draft`
- **总耗时**: 26.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42979747154

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 23.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290759) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | 环境问题 | 自定义容器执行失败，作业在运行第6个用例时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290798) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例已开始执行（POST /generate 返回 200），随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290759

- **base-b-test-1-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed”，属于自托管 runner 的容器环境异常，并非用例断言失败；第6个用例 test_npu_eagle3.py 刚开始即中断，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290798

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130387437920) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130387438038) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290462) |
| multimodal-gen-test-4-npu-a3 (1) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290527) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290634) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290664) |
| base-b-test-16-npu-a3 / run (0) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290668) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42979747154/job/130388290724) |


## [Run #42977245206](https://github.com/sgl-project/sglang/actions/runs/42977245206)
- **分支**: `lsyin/validate-logprob-start-len`
- **总耗时**: 8.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42977245206

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 5.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380576968) |
| base-b-test-1-npu-a3 / run (0) | 5.4min | 环境问题 | 自定义容器执行失败，sglang server 健康检查返回 503，服务未就绪 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380576974) |
| base-b-test-4-npu-a3 / run (1) | 5.4min | 环境问题 | 自定义容器执行失败，作业在启动阶段即被终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380576987) |
| base-b-test-2-npu-a3 / run (0) | 5.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380577015) |

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，说明容器启动/执行环节异常，非用例本身失败，属 runner 环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380576968

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 /health_generate 返回 503 Service Unavailable，随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380576974

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器启动/运行环境故障，非用例代码问题；此前仅有 CANN 库的 SyntaxWarning，无 Traceback 或退出码 5 的用例错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380576987

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在容器启动阶段，未进入用例执行，属 runner/容器环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130380577015

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130379624956) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42977245206/job/130379624959) |


## [Run #42977240998](https://github.com/sgl-project/sglang/actions/runs/42977240998)
- **分支**: `lsyin/pp-reject-recv-interval`
- **总耗时**: 8.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42977240998

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 5.5min | 环境问题 | 自定义容器执行失败，测试进程被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366361) |
| base-b-test-2-npu-a3 / run (0) | 5.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在启动阶段即被终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366372) |
| base-b-test-4-npu-a3 / run (0) | 5.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366415) |
| base-b-test-4-npu-a3 / run (1) | 5.6min | 环境问题 | 自托管 runner 的容器执行失败，作业在模型权重加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366655) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示执行自定义容器实现失败（Executing the custom container implementation failed），发生在 TestAscendMhaHicache.test_a_gsm8k 开始后约14秒，属 runner/容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366361

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；此前仅有 mamba 模块导入告警，未出现测试断言失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366372

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型权重加载过程中出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366415

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 Multi-thread loading shards 加载到 22% 时出现 'Executing the custom container implementation failed'，属于 runner/容器环境异常（非用例断言失败），需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130380366655

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130379592321) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42977240998/job/130379592340) |


## [Run #42973841319](https://github.com/sgl-project/sglang/actions/runs/42973841319)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 79.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42973841319

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 10.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130394310942) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 10.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130394310964) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例本身失败；此前推理请求均返回 200 OK。
  链接: https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130394310942

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 server 已启动成功并返回 200，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator'，属于 runner/容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130394310964

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130368486286) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130368486319) |
| multimodal-gen-test-1-npu-a3 (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369299960) |
| multimodal-gen-test-4-npu-a3 (0) | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300014) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300047) |
| base-b-test-16-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300137) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300162) |
| base-b-test-1-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300167) |
| base-b-test-4-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300170) |
| base-b-test-2-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300199) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300284) |
| multimodal-gen-test-1-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130369300302) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 38.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130378882962) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 27.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130378883040) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42973841319/job/130378883131) |


## [Run #42971799630](https://github.com/sgl-project/sglang/actions/runs/42971799630)
- **分支**: `rbrugaro/mla-absorb-bf16`
- **总耗时**: 7.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42971799630

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 3.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637554) |
| multimodal-gen-test-4-npu-a3 (0) | 3.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637573) |
| multimodal-gen-test-1-npu-a3 (0) | 3.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637581) |
| multimodal-gen-test-4-npu-a3 (1) | 3.4min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败导致用例 error | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637622) |
| base-b-test-8-npu-a3 / run (0) | 3.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637705) |
| base-b-test-16-npu-a3 / run (0) | 3.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637732) |
| base-b-test-2-npu-a3 / run (0) | 3.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637762) |
| base-b-test-1-npu-a3 / run (0) | 3.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637800) |
| base-b-test-4-npu-a3 / run (0) | 3.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637831) |
| base-b-test-4-npu-a3 / run (1) | 3.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637858) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637554

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业提前结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637573

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以unittest errors退出（退出码5），最常见原因是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637581

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试未产出失败样本目录；结合退出码 5 与 setUpClass 启动 sglang server 失败的常见原因（host OOM/进程被 SIGKILL），判断为环境/资源问题导致用例 error，而非用例未收集。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637622

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 k8s 容器启动步骤，测试尚未真正运行，属 runner/容器环境问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637705

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 k8s runner 无法启动指定 CANN 镜像容器，属 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637732

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637762

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637800

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637831

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 侧容器启动失败，非用例代码问题，需联系 runner 管理员排查容器/镜像环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130362637858

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130361908942) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42971799630/job/130361909018) |


## [Run #42971584723](https://github.com/sgl-project/sglang/actions/runs/42971584723)
- **分支**: `lsyin/sched-pr40`
- **总耗时**: 5.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42971584723

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 1.5min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业本身未报失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100482) |
| multimodal-gen-test-4-npu-a3 (0) | 1.5min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略的中间日志确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100509) |
| base-b-test-4-npu-a3 / run (1) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100582) |
| base-b-test-4-npu-a3 / run (0) | 1.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100599) |
| base-b-test-1-npu-a3 / run (0) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100602) |
| base-b-test-2-npu-a3 / run (0) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100613) |
| base-b-test-16-npu-a3 / run (0) | 1.2min | 环境问题 | 日志在 checkout 后即清理孤儿进程结束，未进入测试阶段，疑似 runner/容器环境异常导致作业提前终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100615) |
| base-b-test-8-npu-a3 / run (0) | 1.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器初始化阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100621) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅含 Node 弃用警告和 artifact 路径缺失提示（No files were found with diffusion-failures/），无 Traceback/RuntimeError，无法确认用例失败；疑似测试未产出失败目录或 setUpClass 阶段 server 启动异常未打印，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100482

- **multimodal-gen-test-4-npu-a3 (0)**: 日志可见部分仅有 Node.js 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback 或退出码信息；中间日志被省略，无法定位真实失败点，疑似测试未产出失败目录或 setUpClass 阶段异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100509

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 apt 解包 llvm-14-dev 等包后报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100582

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 apt 安装依赖后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100599

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 apt 安装依赖后报错“Executing the custom container implementation failed”，属 runner/容器环境问题，非用例代码失败，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100602

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 apt 安装依赖后出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属 runner/容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100613

- **base-b-test-16-npu-a3 / run (0)**: 日志仅显示 checkout 完成及 Node 弃用警告，随后 Cleaning up orphan processes 结束，无测试执行或 Traceback，无法确认退出码 5 的具体错误，判断为环境/runner 侧异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100615

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 apt 安装依赖（locales、ca-certificates 等）过程中，属 runner 容器环境/镜像问题，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130362100621

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130361292461) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42971584723/job/130361292662) |


## [Run #42970139826](https://github.com/sgl-project/sglang/actions/runs/42970139826)
- **分支**: `lsyin/sched-pr40`
- **总耗时**: 12.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42970139826

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 9.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253472) |
| base-b-test-16-npu-a3 / run (0) | 9.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载过程中被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253604) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253630) |
| base-b-test-4-npu-a3 / run (0) | 9.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253670) |
| base-b-test-2-npu-a3 / run (0) | 10.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253686) |
| base-b-test-1-npu-a3 / run (0) | 10.0min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357254094) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约10分钟内结束，无明确Traceback。退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253472

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载到64%时出现“Executing the custom container implementation failed”，属于自托管 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253604

- **base-b-test-4-npu-a3 / run (1)**: 日志显示模型权重加载刚开始（0/11 分片）即报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253630

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，并非用例代码或精度问题；此前 server 仍在正常 prefill，随后容器执行报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253670

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型分片加载至75%时出现 ##[error]Executing the custom container implementation failed，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253686

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 test_npu_autoround_moe.py 执行期间，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357254094

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130356600300) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130356601167) |
| multimodal-gen-test-4-npu-a3 (0) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357253580) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42970139826/job/130357254168) |


## [Run #42969215315](https://github.com/sgl-project/sglang/actions/runs/42969215315)
- **分支**: `port/dflash-k31-draft`
- **总耗时**: 90.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42969215315

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 22.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130378122869) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 22.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130378123220) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例代码或性能回归问题；此前 decode 吞吐正常，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130378122869

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例断言或性能回归；此前 decode 吞吐正常，随后容器执行报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130378123220

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130353726812) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130353726944) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354386945) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354386959) |
| base-b-test-16-npu-a3 / run (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354387093) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354387142) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354387148) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354387241) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354387509) |
| base-b-test-4-npu-a3 / run (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130354387857) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130363105737) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130363105795) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42969215315/job/130363105821) |


## [Run #42967434877](https://github.com/sgl-project/sglang/actions/runs/42967434877)
- **分支**: `kvshard/qwen38-flash-next`
- **总耗时**: 25.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42967434877

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733139) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733139

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130347947896) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130347947915) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348732932) |
| multimodal-gen-test-4-npu-a3 (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348732986) |
| base-b-test-1-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733086) |
| base-b-test-16-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733223) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733274) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733276) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42967434877/job/130348733280) |


## [Run #42966776253](https://github.com/sgl-project/sglang/actions/runs/42966776253)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 63.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42966776253

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.5min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130355640436) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试正常进行中（decode 吞吐约197 token/s），随后报错“Executing the custom container implementation failed”，属于 runner/容器基础设施故障，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130355640436

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130345842054) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130345842069) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734004) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734018) |
| multimodal-gen-test-4-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734127) |
| base-b-test-1-npu-a3 / run (0) | 25.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734172) |
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734189) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734230) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734252) |
| base-b-test-4-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734280) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734288) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130346734320) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130355640501) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42966776253/job/130355640510) |


## [Run #42963715520](https://github.com/sgl-project/sglang/actions/runs/42963715520)
- **分支**: `lsyin/sched-pr40`
- **总耗时**: 25.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42963715520

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 18.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139049) |
| base-b-test-1-npu-a3 / run (0) | 8.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139080) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_tp2_bf16.py, npu_tp2_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139049

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139080

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130336196438) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130336196493) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337138974) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139027) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139070) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139112) |
| base-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139136) |
| base-b-test-16-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963715520/job/130337139189) |


## [Run #42963075912](https://github.com/sgl-project/sglang/actions/runs/42963075912)
- **分支**: `feat/dsv41-native-dynamic-tools`
- **总耗时**: 40.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42963075912

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.9min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130345196504) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 8.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130345196528) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型权重分片加载至约54%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例断言失败；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130345196504

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示依赖安装后出现 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码错误；后续仅为清理步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130345196528

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334080766) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334080790) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892397) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892405) |
| multimodal-gen-test-4-npu-a3 (0) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892483) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892501) |
| base-b-test-4-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892504) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892512) |
| base-b-test-1-npu-a3 / run (0) | 28.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892567) |
| base-b-test-2-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892601) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892618) |
| base-b-test-8-npu-a3 / run (0) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130334892644) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42963075912/job/130345196530) |


## [Run #42962896376](https://github.com/sgl-project/sglang/actions/runs/42962896376)
- **分支**: `startup-weight-load-overlap-hardening`
- **总耗时**: 37.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42962896376

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 20.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439760) |
| base-b-test-4-npu-a3 / run (1) | 14.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439876) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439760

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439876

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130333530640) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130333530708) |
| multimodal-gen-test-1-npu-a3 (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439605) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439623) |
| multimodal-gen-test-4-npu-a3 (0) | 33.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439635) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439686) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439761) |
| base-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439762) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439809) |
| base-b-test-4-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962896376/job/130334439975) |


## [Run #42962827591](https://github.com/sgl-project/sglang/actions/runs/42962827591)
- **分支**: `refactor/graph-break-recorder`
- **总耗时**: 33.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42962827591

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 9.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160798) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160798

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130333332990) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130333333041) |
| multimodal-gen-test-4-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160765) |
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160768) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160774) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160845) |
| multimodal-gen-test-4-npu-a3 (0) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160864) |
| base-b-test-2-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160869) |
| base-b-test-16-npu-a3 / run (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160886) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160919) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42962827591/job/130334160989) |


## [Run #42961915568](https://github.com/sgl-project/sglang/actions/runs/42961915568)
- **分支**: `mm-pad-shift-single-source`
- **总耗时**: 24.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42961915568

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951098) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951098

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330321700) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330321741) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330950961) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330950964) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951031) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951048) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951078) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951092) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42961915568/job/130330951096) |


## [Run #42960854852](https://github.com/sgl-project/sglang/actions/runs/42960854852)
- **分支**: `lsyin/sched-pr40`
- **总耗时**: 27.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42960854852

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.2min | 环境问题 | 自定义容器执行失败，疑似 runner 容器异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677912) |
| base-b-test-4-npu-a3 / run (0) | 23.9min | 环境问题 | 自定义容器执行失败，作业在启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677926) |
| base-b-test-2-npu-a3 / run (0) | 23.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327678043) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 server 启动后执行测试时出现 'Executing the custom container implementation failed'，属 self-hosted runner 容器层故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677912

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器环境问题，非用例代码错误；NPU 进程刚启动即被中断，未出现 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677926

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327678043

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130326905648) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130326905824) |
| multimodal-gen-test-4-npu-a3 (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677650) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677682) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677907) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677921) |
| base-b-test-16-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960854852/job/130327677983) |


## [Run #42960648144](https://github.com/sgl-project/sglang/actions/runs/42960648144)
- **分支**: `port/dflash-k31-draft`
- **总耗时**: 79.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42960648144

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 13.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130348866315) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130348866410) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 Decode 阶段吞吐正常，随后报错 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例或代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130348866315

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，非用例本身失败；此前 perf 测试仍在正常输出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130348866410

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130326343021) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130326343031) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140250) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140312) |
| base-b-test-1-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140349) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140356) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140370) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140377) |
| base-b-test-16-npu-a3 / run (0) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140412) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130327140454) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130336283095) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 35.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130336283156) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960648144/job/130336283215) |


## [Run #42960338368](https://github.com/sgl-project/sglang/actions/runs/42960338368)
- **分支**: `pr/muse-spark-prefill-decode-opt`
- **总耗时**: 38.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42960338368

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 5.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120487) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120487

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130325228410) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130325228412) |
| multimodal-gen-test-4-npu-a3 (0) | 34.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120306) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120343) |
| multimodal-gen-test-4-npu-a3 (1) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120382) |
| multimodal-gen-test-1-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120391) |
| base-b-test-2-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120396) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120516) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120600) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120627) |
| base-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42960338368/job/130326120633) |


## [Run #42957049132](https://github.com/sgl-project/sglang/actions/runs/42957049132)
- **分支**: `port/dflash-k31-draft`
- **总耗时**: 33.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42957049132

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 29.8min | 其他 | 日志中所有用例均通过，作业失败原因未在可见日志中体现 | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428188) |
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428205) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428213) |
| base-b-test-2-npu-a3 / run (0) | 19.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428287) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示全部 8 个用例 passed=true，无 Traceback/RuntimeError，退出码 5 的报错段落被省略，无法定位具体失败点，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428188



- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428287

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130314653960) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130314653974) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428028) |
| multimodal-gen-test-4-npu-a3 (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428046) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428147) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42957049132/job/130315428258) |


## [Run #42956860020](https://github.com/sgl-project/sglang/actions/runs/42956860020)
- **分支**: `refactor/graph-break-recorder`
- **总耗时**: 34.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42956860020

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 27.2min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811281) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 51s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811281

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314043059) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314043126) |
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811057) |
| multimodal-gen-test-1-npu-a3 (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811140) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811184) |
| multimodal-gen-test-4-npu-a3 (1) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811203) |
| base-b-test-4-npu-a3 / run (1) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811278) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811288) |
| base-b-test-4-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811300) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811311) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956860020/job/130314811325) |


## [Run #42951176938](https://github.com/sgl-project/sglang/actions/runs/42951176938)
- **分支**: `feature/dsa-index-k-elision-hisparse-decode`
- **总耗时**: 29.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42951176938

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 28.8min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396166304) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以退出码 1 结束，容器执行随之报错。需查看该用例的 Traceback 以定位具体断言或异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396166304

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396167453) |
| multimodal-gen-test-1-npu-a3 (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396167506) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396167522) |
| multimodal-gen-test-4-npu-a3 (0) | 34.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396168240) |
| base-b-test-4-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396168384) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396168429) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396168573) |
| multimodal-gen-test-1-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396168678) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396168791) |
| multimodal-gen-test-4-npu-a3 (1) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396169589) |
| base-b-test-16-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42951176938/job/130396171096) |


## [Run #42948726151](https://github.com/sgl-project/sglang/actions/runs/42948726151)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 37.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42948726151

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749029) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 49 秒），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749029

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130287830631) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130287830687) |
| multimodal-gen-test-4-npu-a3 (0) | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288748849) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288748868) |
| multimodal-gen-test-1-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288748896) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288748916) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749000) |
| base-b-test-16-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749055) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749070) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749072) |
| base-b-test-4-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42948726151/job/130288749081) |


## [Run #42947247676](https://github.com/sgl-project/sglang/actions/runs/42947247676)
- **分支**: `feat/qsa-cache-sharding`
- **总耗时**: 28.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42947247676

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 27.4min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394070526) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过；该用例失败使进程退出码为 1，容器执行失败。需查看该用例的 Traceback 以定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394070526

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394071204) |
| base-b-test-16-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072175) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072195) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072207) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072220) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072359) |
| base-b-test-4-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072443) |
| multimodal-gen-test-1-npu-a3 (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072532) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072594) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072761) |
| base-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42947247676/job/130394072970) |


## [Run #42943259440](https://github.com/sgl-project/sglang/actions/runs/42943259440)
- **分支**: `k3-mla-fp8-q-asm`
- **总耗时**: 27.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42943259440

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 0.5min | 环境问题 | 自托管 runner 的容器实现执行失败，jobPod 未设置导致作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962864) |
| multimodal-gen-test-4-npu-a3 (0) | 1.4min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略的中间日志确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962869) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | 环境问题 | 自定义容器执行失败，NPU 服务健康检查返回 503，作业被 runner 终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962997) |
| multimodal-gen-test-1-npu-a3 (1) | 0.7min | 环境问题 | 自托管 runner 的容器实现失败，jobPod 未创建，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270963041) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 'Executing the custom container implementation failed' 和 'jobPod must be set - ensure prepareJob completed successfully'，说明 k8s runner 的 prepareJob 阶段失败，容器未成功创建，属于 runner 基础设施/环境问题，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962864

- **multimodal-gen-test-4-npu-a3 (0)**: 日志可见部分只有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback/RuntimeError。中间省略段可能含真实失败原因（如 server 启动失败、退出码 5），需查看完整日志定位。
  链接: https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962869

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 /health_generate 返回 503 Service Unavailable，随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962997

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 'Executing the custom container implementation failed' 及 'jobPod must be set - ensure prepareJob completed successfully'，说明 k8s runner 在准备容器阶段失败，测试脚本未执行，属 runner 环境/基础设施问题，需联系自托管 runner 管理员。
  链接: https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270963041

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270024677) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270024864) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962922) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270962999) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270963054) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270963070) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943259440/job/130270963128) |


## [Run #42943098980](https://github.com/sgl-project/sglang/actions/runs/42943098980)
- **分支**: `lsyin/sched-pr40`
- **总耗时**: 39.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42943098980

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.5min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280558) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过；该用例失败使进程以 exit code 1 结束，容器执行报错。需查看该用例的 Traceback 定位具体断言或异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280558

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130269482053) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130269482115) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280363) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280438) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280440) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280489) |
| multimodal-gen-test-4-npu-a3 (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280587) |
| base-b-test-16-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280597) |
| base-b-test-2-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42943098980/job/130270280614) |


## [Run #42942998525](https://github.com/sgl-project/sglang/actions/runs/42942998525)
- **分支**: `oss-sync-1bff57c019`
- **总耗时**: 59.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42942998525

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156372) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156409) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156372

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44s），其余用例均通过，最终进程以退出码1结束，属该用例自身失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156409

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130269166121) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130269166217) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156225) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156241) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156283) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156350) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156379) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156395) |
| base-b-test-16-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156401) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42942998525/job/130270156430) |


## [Run #42941580649](https://github.com/sgl-project/sglang/actions/runs/42941580649)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 24.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42941580649

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 7.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176107) |
| base-b-test-1-npu-a3 / run (0) | 16.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176113) |
| base-b-test-16-npu-a3 / run (0) | 23.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176129) |
| base-b-test-2-npu-a3 / run (0) | 7.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176167) |
| base-b-test-4-npu-a3 / run (0) | 10.4min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176179) |
| base-b-test-4-npu-a3 / run (1) | 14.9min | 环境问题 | PD分离测试用例退出码5，setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176183) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176107

- **base-b-test-1-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176113

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176129

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176167

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176179

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行638秒后返回exit code 5，0/2通过。按约定退出码5表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176183

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289176826) |
| multimodal-gen-test-1-npu-a3 (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289177199) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289177348) |
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289177626) |
| multimodal-gen-test-1-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289177901) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42941580649/job/130289177948) |


## [Run #42940237319](https://github.com/sgl-project/sglang/actions/runs/42940237319)
- **分支**: `vedantjh2/synthid-oss`
- **总耗时**: 58.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42940237319

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.5min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210920) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时42s），其余用例均通过，最终进程以 exit code 1 结束，属该用例自身失败，需查看其 Traceback 定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210920

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130260221042) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130260221117) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210800) |
| multimodal-gen-test-1-npu-a3 (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210825) |
| multimodal-gen-test-4-npu-a3 (0) | 34.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210828) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210925) |
| base-b-test-16-npu-a3 / run (0) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210942) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210944) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210951) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261210987) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940237319/job/130261211196) |


## [Run #42940197542](https://github.com/sgl-project/sglang/actions/runs/42940197542)
- **分支**: `codex/av-2`
- **总耗时**: 66.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42940197542

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493420) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493420

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260050759) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260050777) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958173) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958181) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958184) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958195) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958211) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958231) |
| base-b-test-16-npu-a3 / run (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958238) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130260958334) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493490) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42940197542/job/130272493538) |


## [Run #42938269569](https://github.com/sgl-project/sglang/actions/runs/42938269569)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 44.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42938269569

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.4min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254895001) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过，最终进程以退出码1结束，属于该用例本身的代码或断言失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254895001

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130253901261) |
| Recommend tests from coverage | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130253901306) |
| multimodal-gen-test-1-npu-a3 (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894743) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894827) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894828) |
| multimodal-gen-test-4-npu-a3 (0) | 34.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894884) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894918) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894962) |
| base-b-test-16-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894967) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254894980) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42938269569/job/130254895021) |


## [Run #42937755723](https://github.com/sgl-project/sglang/actions/runs/42937755723)
- **分支**: `feat/trie-head-shared-attention`
- **总耗时**: 44.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42937755723

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.4min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090802) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时46秒），其余用例均通过，该用例失败使进程以退出码1结束；日志未给出具体 Traceback，需查看该用例详细输出定位原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090802

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130252099164) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130252099266) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090390) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090409) |
| multimodal-gen-test-4-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090428) |
| multimodal-gen-test-4-npu-a3 (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090510) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090621) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090729) |
| base-b-test-4-npu-a3 / run (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090761) |
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090855) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42937755723/job/130253090895) |


## [Run #42936005713](https://github.com/sgl-project/sglang/actions/runs/42936005713)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 18.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42936005713

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.8min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331043) |
| multimodal-gen-test-4-npu-a3 (0) | 15.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331121) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331208) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331225) |
| base-b-test-16-npu-a3 / run (0) | 12.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331393) |
| base-b-test-4-npu-a3 / run (0) | 14.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331400) |
| base-b-test-2-npu-a3 / run (0) | 14.7min | 环境问题 | 自定义容器执行失败，疑似 runner 容器异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331489) |
| base-b-test-1-npu-a3 / run (0) | 14.8min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331492) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业约7分钟后结束，未上传diffusion-failures/产物（无文件），说明测试用例在setUpClass阶段即报错，最可能是NPU上sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331043




- **base-b-test-16-npu-a3 / run (0)**: 日志显示测试本身已通过（Ran 1 test, OK），随后启动 sglang server 时出现 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331393

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 NPU 推理正常进行中，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331400

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 返回 200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331489

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 test_npu_gptq_moe.py 运行期间，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331492

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130246298603) |
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130246298623) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331335) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42936005713/job/130247331433) |


## [Run #42935787881](https://github.com/sgl-project/sglang/actions/runs/42935787881)
- **分支**: `dark/carv2-symm-workspace`
- **总耗时**: 46.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42935787881

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660658) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660690) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时41秒），其余用例均通过，该用例失败使进程以退出码1结束，属用例本身报错，需查看该用例日志定位具体异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660658

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660690

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130245606964) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130245607048) |
| multimodal-gen-test-1-npu-a3 (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660241) |
| multimodal-gen-test-1-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660329) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660379) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660446) |
| base-b-test-16-npu-a3 / run (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660569) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660588) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246660765) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935787881/job/130246661047) |


## [Run #42935786405](https://github.com/sgl-project/sglang/actions/runs/42935786405)
- **分支**: `dark/carv2-dpx-pair-header`
- **总耗时**: 23.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42935786405

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.8min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383867462) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383867462

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-4-npu-a3 / run (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383868073) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383868660) |
| multimodal-gen-test-1-npu-a3 (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383868992) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869008) |
| multimodal-gen-test-4-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869314) |
| base-b-test-16-npu-a3 / run (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869361) |
| multimodal-gen-test-1-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869467) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869564) |
| multimodal-gen-test-4-npu-a3 (0) | 34.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869575) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383869722) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42935786405/job/130383870083) |


## [Run #42930546073](https://github.com/sgl-project/sglang/actions/runs/42930546073)
- **分支**: `pr-gfx1250-fused-rope-kv-tiled`
- **总耗时**: 21.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42930546073

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.4min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609501590) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时43秒），其余用例均通过，最终进程以退出码1结束，属该用例自身失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609501590

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609501445) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609502437) |
| multimodal-gen-test-1-npu-a3 (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609503102) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609503313) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609503781) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609503838) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609504027) |
| base-b-test-16-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609504397) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609504806) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609504889) |
| multimodal-gen-test-4-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930546073/job/130609506297) |


## [Run #42930415612](https://github.com/sgl-project/sglang/actions/runs/42930415612)
- **分支**: `lsyin/media-input-errors`
- **总耗时**: 11.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42930415612

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228795910) |
| multimodal-gen-test-4-npu-a3 (0) | 7.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228795937) |
| multimodal-gen-test-1-npu-a3 (0) | 7.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228795988) |
| multimodal-gen-test-1-npu-a3 (1) | 7.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796054) |
| base-b-test-4-npu-a3 / run (1) | 7.4min | 环境问题 | 自定义容器执行失败，作业被 runner 异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796090) |
| base-b-test-4-npu-a3 / run (0) | 7.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796105) |
| base-b-test-2-npu-a3 / run (0) | 7.4min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796106) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败且未生成失败产物。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228795910

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约7分钟结束，退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228795937

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228795988

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产生输出。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796054

- **base-b-test-4-npu-a3 / run (1)**: 日志显示请求正常返回200后出现“Executing the custom container implementation failed”，属自托管 runner 容器环境异常，非用例断言失败；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796090

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，发生在推理请求正常返回后，属于 runner/容器基础设施异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796105

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在模型权重加载阶段，属于自托管 runner 容器环境异常，非代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796106

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130227619455) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130227619492) |
| base-b-test-1-npu-a3 / run (0) | 6.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42930415612/job/130228796145) |


## [Run #42929097955](https://github.com/sgl-project/sglang/actions/runs/42929097955)
- **分支**: `port/dflash-draft-kv-ring`
- **总耗时**: 25.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42929097955

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392815) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392815

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130223204396) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130223204514) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392463) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392566) |
| base-b-test-4-npu-a3 / run (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392621) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392664) |
| base-b-test-1-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392674) |
| base-b-test-16-npu-a3 / run (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392801) |
| base-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42929097955/job/130224392817) |


## [Run #42928094258](https://github.com/sgl-project/sglang/actions/runs/42928094258)
- **分支**: `codex/av-3`
- **总耗时**: 28.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42928094258

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 8.3min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809530) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 251 秒后 FAILED (errors=1)，2 个用例 0 通过，进程退出码 1，导致作业失败；日志省略了具体 Traceback，需查看该用例 setUpClass 阶段 server 启动或断言错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809530

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130219793465) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130219796439) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809344) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809442) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809548) |
| base-b-test-16-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809562) |
| base-b-test-1-npu-a3 / run (0) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809591) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809669) |
| base-b-test-4-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42928094258/job/130220809885) |


## [Run #42926873675](https://github.com/sgl-project/sglang/actions/runs/42926873675)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 44.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42926873675

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.3min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216540005) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例的详细输出以定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216540005

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130215649204) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130215649323) |
| multimodal-gen-test-1-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216539525) |
| multimodal-gen-test-1-npu-a3 (0) | 26.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216539560) |
| multimodal-gen-test-4-npu-a3 (1) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216539708) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216539814) |
| base-b-test-2-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216539819) |
| multimodal-gen-test-4-npu-a3 (0) | 41.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216539888) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216540050) |
| base-b-test-16-npu-a3 / run (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216540054) |
| base-b-test-4-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926873675/job/130216540126) |


## [Run #42926786352](https://github.com/sgl-project/sglang/actions/runs/42926786352)
- **分支**: `lsyin/sched-pr40`
- **总耗时**: 28.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42926786352

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 25.2min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518806) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44s），其余用例均通过，该用例失败使进程以退出码1结束，属测试用例本身报错。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518806

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130215351511) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130215352118) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518346) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518390) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518766) |
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518809) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518843) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216518916) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926786352/job/130216519275) |


## [Run #42926566397](https://github.com/sgl-project/sglang/actions/runs/42926566397)
- **分支**: `mmangkad/kda-replayssm-commit-prepared-step-indices`
- **总耗时**: 43.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42926566397

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 9.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载过程中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130228957567) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130228957618) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示模型分片加载到 73% 时出现 'Executing the custom container implementation failed'，属于自托管 runner/容器环境异常，非用例代码或性能回归问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130228957567

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示模型分片加载到65%时出现“Executing the custom container implementation failed”，属于 runner/容器环境异常，非用例代码或性能回归问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130228957618

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130214642580) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130214642678) |
| base-b-test-4-npu-a3 / run (1) | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130215658583) |
| base-b-test-4-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130215658669) |
| base-b-test-1-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130215658689) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42926566397/job/130220203836) |


## [Run #42923400756](https://github.com/sgl-project/sglang/actions/runs/42923400756)
- **分支**: `new-model-support`
- **总耗时**: 46.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42923400756

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.5min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721263) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 46s），其余用例均通过；该用例失败使进程以退出码 1 结束，日志未给出具体 Traceback，需查看该用例详细输出定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721263

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130203828870) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130203828881) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204720932) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204720963) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721013) |
| multimodal-gen-test-4-npu-a3 (0) | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721065) |
| base-b-test-16-npu-a3 / run (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721128) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721144) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721266) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721267) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42923400756/job/130204721274) |


## [Run #42922509692](https://github.com/sgl-project/sglang/actions/runs/42922509692)
- **分支**: `feat/cli-fp4-gemm-backend-aiter-triton`
- **总耗时**: 27.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42922509692

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 26.9min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513565745) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 44s），其余用例均通过，最终进程以 exit code 1 结束。需查看该用例的 Traceback 定位具体断言或异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513565745

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513566276) |
| multimodal-gen-test-1-npu-a3 (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513567091) |
| multimodal-gen-test-4-npu-a3 (0) | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513567484) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513567527) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513568357) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513568416) |
| multimodal-gen-test-1-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513568472) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513568567) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513568699) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513568757) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42922509692/job/130513569023) |


## [Run #42919759545](https://github.com/sgl-project/sglang/actions/runs/42919759545)
- **分支**: `startup-weight-load-overlap-hardening`
- **总耗时**: 36.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42919759545

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 27.7min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255818) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例的详细输出以定位根因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255818

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130241251083) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130241251089) |
| multimodal-gen-test-4-npu-a3 (0) | 33.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255522) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255531) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255559) |
| multimodal-gen-test-4-npu-a3 (1) | 27.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255641) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255775) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255904) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242255922) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242256027) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919759545/job/130242256038) |


## [Run #42919268472](https://github.com/sgl-project/sglang/actions/runs/42919268472)
- **分支**: `lsyin/sched-pr39`
- **总耗时**: 45.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42919268472

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 18.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130202515559) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明是 runner 侧容器执行异常（非用例断言失败），需联系自托管 runner 管理员排查容器/节点环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130202515559

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130189998679) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130189998736) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226221) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226291) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226379) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226393) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226423) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226442) |
| base-b-test-16-npu-a3 / run (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226476) |
| base-b-test-4-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130191226495) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130202515534) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42919268472/job/130202515591) |


## [Run #42918454715](https://github.com/sgl-project/sglang/actions/runs/42918454715)
- **分支**: `port/dflash-draft-kv-ring`
- **总耗时**: 54.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42918454715

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130199658241) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130199658241

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130187101384) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130187101431) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188199613) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188199624) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188199998) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188200096) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188200183) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188200256) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188200321) |
| base-b-test-16-npu-a3 / run (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130188200648) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130199658209) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42918454715/job/130199658287) |


## [Run #42917966949](https://github.com/sgl-project/sglang/actions/runs/42917966949)
- **分支**: `startup-weight-load-overlap-hardening`
- **总耗时**: 12.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42917966949

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 9.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467134) |
| multimodal-gen-test-1-npu-a3 (0) | 9.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467206) |
| multimodal-gen-test-4-npu-a3 (0) | 9.3min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467224) |
| base-b-test-2-npu-a3 / run (0) | 9.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467285) |
| multimodal-gen-test-1-npu-a3 (1) | 9.3min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467369) |
| base-b-test-16-npu-a3 / run (0) | 9.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467382) |
| base-b-test-4-npu-a3 / run (0) | 9.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467401) |
| base-b-test-4-npu-a3 / run (1) | 9.3min | 环境问题 | 自定义容器执行失败，疑似 NPU 驱动/CANN 环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467421) |
| base-b-test-1-npu-a3 / run (0) | 9.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467484) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467134

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467206

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业以退出码5结束，符合 unittest errors（如 setUpClass 中 server 启动失败、host OOM 或进程被 SIGKILL）的特征，需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467224

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 TokenizerManager 初始化后报错 'Executing the custom container implementation failed'，属于 runner 容器环境问题，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467285

- **multimodal-gen-test-1-npu-a3 (1)**: 日志末尾显示未找到 diffusion-failures/ 路径，无产物上传；结合退出码 5 提示 unittest errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），需查看中间省略段的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467369

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题；测试进程在容器执行阶段被终止，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467382

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明是 runner 侧容器启动或运行异常，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467401

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，且此前出现 CANN 与 HDK 驱动版本需 32 字节 padding 处理的警告，作业在测试启动阶段即被中断，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467421

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器执行环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467484

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130185431576) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130185431649) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42917966949/job/130186467456) |


## [Run #42913868826](https://github.com/sgl-project/sglang/actions/runs/42913868826)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 36.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42913868826

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.1min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862209) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时41秒），其余用例均通过，该用例失败使进程以退出码1结束；日志未给出具体 Traceback，需查看该用例详细输出定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862209

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130171497699) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130171498167) |
| multimodal-gen-test-4-npu-a3 (0) | 32.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172861907) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172861988) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862065) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862158) |
| base-b-test-2-npu-a3 / run (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862205) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862254) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862265) |
| multimodal-gen-test-1-npu-a3 (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862268) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42913868826/job/130172862349) |


## [Run #42910832969](https://github.com/sgl-project/sglang/actions/runs/42910832969)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 19.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42910832969

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004502) |
| multimodal-gen-test-4-npu-a3 (0) | 15.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004531) |
| multimodal-gen-test-4-npu-a3 (1) | 14.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004583) |
| multimodal-gen-test-1-npu-a3 (1) | 16.0min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004592) |
| base-b-test-2-npu-a3 / run (0) | 15.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004604) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | 环境问题 | 自定义容器执行失败，作业被 runner 中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004611) |
| base-b-test-1-npu-a3 / run (0) | 14.7min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004725) |
| base-b-test-4-npu-a3 / run (0) | 14.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004870) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业运行约14分钟后结束，退出码5表示unittest有errors，常见于setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。日志中未见diffusion-failures目录，无产物上传，需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004502

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出结果；退出码5对应 unittest errors，最常见为 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004531

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾显示 diffusion-failures/ 目录无文件可上传，说明用例执行阶段已失败；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004583

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出结果；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004592

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例本身已通过（OK），随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004604

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，说明自托管 runner 的容器启动/运行异常，并非用例断言失败；此前仅有 Ascend 算子脚本的 SyntaxWarning，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004611

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属 self-hosted runner 容器实现故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004725

- **base-b-test-4-npu-a3 / run (0)**: 日志显示服务正常推理后突然报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器基础设施故障，非用例代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004870

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130160966794) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130160966861) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004619) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910832969/job/130162004781) |


## [Run #42910762862](https://github.com/sgl-project/sglang/actions/runs/42910762862)
- **分支**: `oss-sync-6883c8d753`
- **总耗时**: 66.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42910762862

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 10.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130189551572) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 10.2min | 超时 | TokenizerManager watchdog 超时，容器执行失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130189551613) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示服务端推理正常（chat/completions 返回 200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130189551572

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 TokenizerManager watchdog timeout（watchdog_timeout=300），随后报错 custom container implementation failed，属于服务启动/运行阶段超时，非用例收集问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130189551613

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130160725552) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130160725730) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161984959) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161985645) |
| base-b-test-16-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161985713) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161986022) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161986055) |
| base-b-test-2-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161986123) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161986168) |
| multimodal-gen-test-4-npu-a3 (1) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130161986510) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130174616397) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130174616453) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910762862/job/130174616484) |


## [Run #42910541209](https://github.com/sgl-project/sglang/actions/runs/42910541209)
- **分支**: `new-model-support`
- **总耗时**: 34.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42910541209

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.1min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155947) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 46s），其余用例均通过；该用例失败使进程以退出码 1 结束，容器实现报错。需查看该用例的 Traceback 以定位具体断言或异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155947

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130159974578) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130159974617) |
| multimodal-gen-test-1-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155269) |
| multimodal-gen-test-1-npu-a3 (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155351) |
| multimodal-gen-test-4-npu-a3 (1) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155528) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155594) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155627) |
| base-b-test-2-npu-a3 / run (0) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155648) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155737) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155753) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42910541209/job/130161155763) |


## [Run #42909742340](https://github.com/sgl-project/sglang/actions/runs/42909742340)
- **分支**: `oss-sync-91ba7c57b3`
- **总耗时**: 72.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42909742340

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 4.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130192518440) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 4.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130192518669) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，测试脚本刚启动即中断，属 runner/容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130192518440

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，非用例代码或性能回归；测试尚未真正执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130192518669

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130157168253) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130157168385) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158493948) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494142) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494268) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494349) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494379) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494408) |
| multimodal-gen-test-4-npu-a3 (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494491) |
| base-b-test-4-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130158494535) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130173242931) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130173242946) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909742340/job/130173242980) |


## [Run #42909600314](https://github.com/sgl-project/sglang/actions/runs/42909600314)
- **分支**: `lsyin/sched-pr39`
- **总耗时**: 63.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42909600314

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.1min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130172061669) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明自托管 runner 的容器运行时异常，导致作业在测试进行中被强制终止，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130172061669

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130156734106) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130156734287) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041081) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041181) |
| base-b-test-16-npu-a3 / run (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041196) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041198) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041251) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041329) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041353) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130158041359) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130172061781) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42909600314/job/130172061821) |


## [Run #42907077802](https://github.com/sgl-project/sglang/actions/runs/42907077802)
- **分支**: `feat/mm-routing-label-spans`
- **总耗时**: 38.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42907077802

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 20.9min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420052) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时42秒），其余用例均通过，最终进程以退出码1结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出以定位是断言失败还是 setUpClass 阶段 server 启动异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420052

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130147996841) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130147996949) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149419833) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149419875) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149419883) |
| multimodal-gen-test-4-npu-a3 (1) | 35.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149419909) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420066) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420073) |
| base-b-test-2-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420075) |
| base-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420087) |
| base-b-test-16-npu-a3 / run (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42907077802/job/130149420117) |


## [Run #42905897886](https://github.com/sgl-project/sglang/actions/runs/42905897886)
- **分支**: `feat/dsv41-native-dynamic-tools`
- **总耗时**: 36.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42905897886

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.8min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017235) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过；该用例失败使进程以 exit code 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017235

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130210893640) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130210893702) |
| multimodal-gen-test-1-npu-a3 (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212016978) |
| multimodal-gen-test-1-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017003) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017012) |
| multimodal-gen-test-4-npu-a3 (0) | 32.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017096) |
| base-b-test-4-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017127) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017197) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017216) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017237) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42905897886/job/130212017246) |


## [Run #42903786738](https://github.com/sgl-project/sglang/actions/runs/42903786738)
- **分支**: `codex/fix-health-wait-cascade-1110`
- **总耗时**: 30.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42903786738

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980679) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980808) |


- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过；该用例失败使进程以退出码1结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980808

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130136623689) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130136623867) |
| multimodal-gen-test-1-npu-a3 (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137979895) |
| multimodal-gen-test-4-npu-a3 (0) | 27.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980036) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980124) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980152) |
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980392) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980525) |
| base-b-test-8-npu-a3 / run (0) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980565) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42903786738/job/130137980752) |


## [Run #42902609396](https://github.com/sgl-project/sglang/actions/runs/42902609396)
- **分支**: `lsyin/sched-pr38`
- **总耗时**: 28.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42902609396

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.5min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169770) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的 Traceback，需查看该用例详细输出以定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169770

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130132534281) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130132534406) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134168906) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134168979) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169838) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169844) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169921) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169933) |
| base-b-test-4-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42902609396/job/130134169939) |


## [Run #42901415249](https://github.com/sgl-project/sglang/actions/runs/42901415249)
- **分支**: `lsyin/k3-response-shape`
- **总耗时**: 48.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42901415249

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 45.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600217) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600534) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾显示未找到diffusion-failures/目录，无产物上传；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600217

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 44s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600534

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130128291114) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130128291144) |
| multimodal-gen-test-1-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129599981) |
| multimodal-gen-test-1-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600019) |
| multimodal-gen-test-4-npu-a3 (1) | 35.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600203) |
| base-b-test-4-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600263) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600349) |
| base-b-test-2-npu-a3 / run (0) | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600521) |
| base-b-test-16-npu-a3 / run (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600528) |
| base-b-test-8-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42901415249/job/130129600569) |


## [Run #42893677681](https://github.com/sgl-project/sglang/actions/runs/42893677681)
- **分支**: `amd/aiter-gdn-chunked-prefill`
- **总耗时**: 27.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42893677681

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 24.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42893677681/job/130102742588) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 24.2min | 其他 | 测试实际全部通过，作业失败疑似清理阶段复制 _temp 失败导致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42893677681/job/130102742750) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示测试用例本身已正常完成（/generate 返回 200 OK），随后报错 'Executing the custom container implementation failed'，属于 runner 容器环境/基础设施故障，非用例代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42893677681/job/130102742588

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 1/1 用例 PASSED，耗时 1129s，测试正常结束；随后 Post job cleanup 出现 'Failed to copy _temp from pod' 警告，作业被判失败，属基础设施/清理阶段问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42893677681/job/130102742750

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42893677681/job/130101350807) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42893677681/job/130101350834) |


## [Run #42879327215](https://github.com/sgl-project/sglang/actions/runs/42879327215)
- **分支**: `qkang/elastic-ep-mooncake-scale-down`
- **总耗时**: 38.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42879327215

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.9min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547421) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以退出码 1 结束，属于用例级代码或断言失败，需查看该用例的 Traceback 定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547421

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130051329628) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130051329650) |
| multimodal-gen-test-4-npu-a3 (0) | 35.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547345) |
| multimodal-gen-test-1-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547348) |
| multimodal-gen-test-1-npu-a3 (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547393) |
| multimodal-gen-test-4-npu-a3 (1) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547440) |
| base-b-test-4-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547551) |
| base-b-test-2-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547729) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052547889) |
| base-b-test-16-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052548028) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42879327215/job/130052548122) |


## [Run #42871417129](https://github.com/sgl-project/sglang/actions/runs/42871417129)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 17.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42871417129

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 14.6min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42871417129/job/130024686298) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾仅显示上传 diffusion-failures-npu-2-part0-1.zip 产物并正常清理，未直接给出 Traceback；结合退出码 5 与产物名，判断为用例执行中 server 启动失败（如 host OOM/进程被 SIGKILL）导致 unittest errors，需查看上传产物中的失败日志确认具体异常。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42871417129/job/130024686298

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42871417129/job/130023745784) |
| multimodal-gen-test-4-npu-a3 (1) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42871417129/job/130024686208) |


## [Run #42866087149](https://github.com/sgl-project/sglang/actions/runs/42866087149)
- **分支**: `xpu/weekly-simple-model-enablement-2026-11-09`
- **总耗时**: 35.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42866087149

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 31.1min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214312) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 166s），其余用例均通过，最终进程以 exit code 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214312

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130004927018) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130004927135) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214040) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214087) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214117) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214151) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214256) |
| base-b-test-8-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214265) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214306) |
| base-b-test-4-npu-a3 / run (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214351) |
| base-b-test-4-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42866087149/job/130006214385) |


## [Run #42862746462](https://github.com/sgl-project/sglang/actions/runs/42862746462)
- **分支**: `npu-dsa-token-shard`
- **总耗时**: 24.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42862746462

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716515) |
| base-b-test-2-npu-a3 / run (0) | 5.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716677) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716515

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716677

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129993242856) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129993242961) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716263) |
| multimodal-gen-test-4-npu-a3 (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716412) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716525) |
| base-b-test-16-npu-a3 / run (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716559) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716575) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42862746462/job/129994716745) |


## [Run #42860224567](https://github.com/sgl-project/sglang/actions/runs/42860224567)
- **分支**: `refactor/graph-break-recorder`
- **总耗时**: 39.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42860224567

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.1min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871520) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 46s），其余用例均通过，因此该用例失败使进程退出码为 1；日志未给出具体 Traceback，需查看该用例详细输出以定位根因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871520

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129984365144) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129984365365) |
| multimodal-gen-test-1-npu-a3 (1) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871237) |
| multimodal-gen-test-4-npu-a3 (1) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871242) |
| multimodal-gen-test-4-npu-a3 (0) | 36.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871314) |
| multimodal-gen-test-1-npu-a3 (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871319) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871394) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871416) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985871493) |
| base-b-test-16-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985872149) |
| base-b-test-2-npu-a3 / run (0) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42860224567/job/129985872238) |


## [Run #42852561384](https://github.com/sgl-project/sglang/actions/runs/42852561384)
- **分支**: `feat/mamba-hybrid-state-eviction`
- **总耗时**: 46.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42852561384

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403605) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43 秒），其余用例均通过；该用例失败使进程以退出码 1 结束，容器执行报错。需查看该用例的 Traceback 以定位具体原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403605

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129957244047) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129957244212) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958402109) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958402127) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958402167) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958402531) |
| base-b-test-16-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403775) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403855) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403945) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403970) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42852561384/job/129958403984) |


## [Run #42849997169](https://github.com/sgl-project/sglang/actions/runs/42849997169)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 13.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42849997169

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 10.3min | 环境问题 | 多模态生成测试失败，失败产物已上传，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42849997169/job/129949060003) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业退出码 5（unittest errors），并上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行中出错；最常见原因是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看上传产物中的 Traceback 确认。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42849997169/job/129949060003

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42849997169/job/129948050941) |
| multimodal-gen-test-4-npu-a3 (1) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42849997169/job/129949060119) |


## [Run #42841361446](https://github.com/sgl-project/sglang/actions/runs/42841361446)
- **分支**: `mori_epv2_asyncll_tbo`
- **总耗时**: 32.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42841361446

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 31.7min | 其他 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 执行失败，退出码 1，3 个用例仅 1 个通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361736701) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 该作业为 NPU 性能测试，失败用例退出码 1（非 5），日志省略了具体 Traceback。同套件另一用例通过，说明环境基本可用，失败集中在特定 1024x1024 输入场景，需查看完整日志确认是性能不达标还是运行异常。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361736701

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361734678) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361734744) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361734814) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361734879) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361735078) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361735272) |
| base-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361735366) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361735486) |
| base-b-test-1-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361735743) |
| base-b-test-16-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361735883) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361736518) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361737278) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361737379) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42841361446/job/130361739072) |


## [Run #42820342485](https://github.com/sgl-project/sglang/actions/runs/42820342485)
- **分支**: `feat/dsv41-packed-main-kv`
- **总耗时**: 24.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42820342485

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.1min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943110356) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时43秒），其余用例均通过，最终进程以 exit code 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出以定位是断言失败还是 setUpClass 中 server 启动异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943110356

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943112811) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943113172) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943113692) |
| multimodal-gen-test-4-npu-a3 (0) | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943113704) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943113755) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943113827) |
| base-b-test-2-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943113895) |
| base-b-test-16-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943114065) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943114348) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943114361) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42820342485/job/129943114710) |


## [Run #42792156440](https://github.com/sgl-project/sglang/actions/runs/42792156440)
- **分支**: `dark/carv2-symm-workspace`
- **总耗时**: 25.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42792156440

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 25.0min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002834321) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44s），其余用例均通过，最终进程以 exit code 1 结束。需查看该用例的具体 Traceback 以定位是 kernel 逻辑错误还是环境问题。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002834321

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002835791) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836367) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836372) |
| base-b-test-16-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836629) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836646) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836652) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836693) |
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836800) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002836887) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002837202) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42792156440/job/130002838130) |


---
*Auto-generated by ci_monitor.py*