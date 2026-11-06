# NPU CI 执行监控（2026-11-06）
**生成时间**: 2026-11-07 07:24
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-06 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 263

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 2474 个 | 失败 264 个 | 成功 Job 平均耗时 13.3min
- **Run 执行情况**: 成功 166 个 | 失败 97 个 | 成功 Run 平均耗时 69.8min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 74.5min | #42193106219 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193106219/job/127822767522) |
| base-b-test-4-npu-a3 / run (0) | 59.1min | #42216674902 | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537278) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 53.7min | #42152141758 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152141758/job/127693806141) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 50.5min | #42185338349 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185338349/job/127795890718) |
| multimodal-gen-test-4-npu-a3 (0) | 49.9min | #42146956606 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146956606/job/127661650727) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.7min | #41607308105 | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127890932945) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.5min | #42163721064 | [job link](https://github.com/sgl-project/sglang/actions/runs/42163721064/job/127730640837) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.4min | #42141965873 | [job link](https://github.com/sgl-project/sglang/actions/runs/42141965873/job/127653484838) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.1min | #42218899378 | [job link](https://github.com/sgl-project/sglang/actions/runs/42218899378/job/127920021282) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.4min | #42053549169 | [job link](https://github.com/sgl-project/sglang/actions/runs/42053549169/job/127351903636) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.2min | #42188605678 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127804908972) |
| multimodal-gen-test-1-npu-a3 (1) | 30.6min | #42126617967 | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376347) |
| multimodal-gen-test-1-npu-a3 (0) | 30.3min | #42126617967 | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376290) |
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | #42182940684 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778063988) |
| multimodal-gen-test-4-npu-a3 (0) | 28.8min | #42208574201 | [job link](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862119100) |
| multimodal-gen-test-4-npu-a3 (1) | 28.5min | #42126617967 | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376146) |
| multimodal-gen-test-4-npu-a3 (0) | 28.4min | #42093810892 | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479894933) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.2min | #42150018137 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127838150021) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | #42185413202 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473143) |
| multimodal-gen-test-4-npu-a3 (1) | 26.9min | #42185413202 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473296) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-4-npu-a3 / run (1) | 214 | 175 | 15 | 5 | 19 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536176)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127811544294)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943366)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257788)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212948) |
| base-b-test-16-npu-a3 / run (0) | 168 | 128 | 1 | 16 | 23 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660615) |
| base-b-test-2-npu-a3 / run (0) | 219 | 178 | 12 | 3 | 26 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040985)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114567)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085785)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319643)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42185365009/job/127785131517) |
| base-b-test-8-npu-a3 / run (0) | 168 | 138 | 6 | 8 | 16 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918339)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974789)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690530)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270387)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312173) |
| base-b-test-1-npu-a3 / run (0) | 202 | 162 | 9 | 4 | 27 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941833)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377624)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212876)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188707)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111333) |
| base-b-test-4-npu-a3 / run (0) | 214 | 178 | 5 | 6 | 25 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943365)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624205)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127693673920)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127583229152)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197751) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 127 | 104 | 10 | 0 | 13 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127983007861)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127915417946)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127893664302)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42192330172/job/127808084628)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42190297303/job/127801509104) |
| multimodal-gen-test-4-npu-a3 (0) | 185 | 153 | 5 | 0 | 27 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906851910)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627038)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786515)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862119100)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606449) |
| multimodal-gen-test-4-npu-a3 (1) | 185 | 156 | 3 | 0 | 26 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786500)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666343)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637307) |
| multimodal-gen-test-1-npu-a3 (1) | 108 | 92 | 2 | 0 | 14 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627014)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637141) |
| multimodal-gen-test-1-npu-a3 (0) | 108 | 91 | 2 | 0 | 15 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627116)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786391) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 216 | 203 | 2 | 0 | 11 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127655059481)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243492) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 121 | 114 | 0 | 1 | 6 | - |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 95 | 90 | 0 | 1 | 4 | - |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_pd_disaggregation.py` | 73 | 57 | 16 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536176)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127811544294)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943366) |
| `npu_mla_fia_hicache_bf16.py` | 66 | 59 | 7 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114567)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377653)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922118) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 15 | 9 | 6 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127983007861)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127804908972)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127838150021) |
| `npu_hicache_mha.py` | 64 | 59 | 5 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941833)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377624)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188707) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 65 | 60 | 5 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974789)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690530)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270387) |
| `npu_return_indexer_topk_deepseek_v4.py` | 54 | 51 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040985)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085785)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319643) |
| `npu_sampling_backend.py` | 54 | 52 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212876)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111333) |
| `npu_tp1_bf16.py` | 52 | 50 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690581)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521463) |
| `npu_dp_attention.py` | 61 | 59 | 2 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943365)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197751) |
| `npu_deepseek_v4_flash_w8a8_8p_gpqa.py` | 15 | 13 | 2 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42192330172/job/127808084628)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42190297303/job/127801509104) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 21 | 19 | 2 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127655059481)<br>[base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243492) |
| `qwen_image_t2i_2npu` | 39 | 38 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637325) |
| `wan2_2_t2v_14b_w8a8_2npu` | 36 | 35 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862119100) |
| `minimax_h3_t2va_2npu` | 33 | 32 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862119100) |
| `flux_image_t2i_npu` | 40 | 39 | 1 | [multimodal-gen-test-1-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906851788) |
| `npu_w4a4_quantization.py` | 64 | 63 | 1 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624205) |
| `npu_speculative_multi_npu.py` | 55 | 54 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521314) |
| `npu_return_indexer_topk_glm52.py` | 53 | 52 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419605) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #41607308105<br>[#48118 [Perf] [AMD] gdn: Add an aiter backend for linear-chain target verify](https://github.com/sgl-project/sglang/pull/48118) | `feature/yunkai/gdn-verify-aiter` | 139.0min | 2 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/41607308105) |
| #42219155484<br>[#48701 [Perf] [AMD] kimi-k3: Run KDA target verify through AITER's fused FlyDSL kernel](https://github.com/sgl-project/sglang/pull/48701) | `k3-pr1-quark-weights` | 134.7min | 3 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42219155484) |
| #42221883221<br>[#47129 [Perf] [NVIDIA] muse-spark: Bound B200 projection dispatch and allocator compilation](https://github.com/sgl-project/sglang/pull/47129) | `codex/muse-b200-b1-runtime` | 126.4min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42221883221) |
| #42157073849<br>[#48399 [Refactor] env: Dispatch on the GPU architecture instead of env vars that restate it](https://github.com/sgl-project/sglang/pull/48399) | `bbuf/env-arch-dispatch` | 99.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42157073849) |
| #42157284079<br>[#44017 [Feat] [XPU] GDN: support speculative decoding](https://github.com/sgl-project/sglang/pull/44017) | `gdn-spec-decode-xpu` | 95.9min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42157284079) |
| #42126617967 | `oss-sync-219fe11113` | 85.8min | 3 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42126617967) |
| #42125781320 | `oss-sync-65c40d1f0e` | 85.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42125781320) |
| #42216674902<br>[#44399 [Feat] gemma4: per-layer attention backend](https://github.com/sgl-project/sglang/pull/44399) | `main` | 84.7min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42216674902) |
| #42135808011<br>[#48457 [Feat] rust-server: Write --crash-dump-folder dumps from the Rust frontend](https://github.com/sgl-project/sglang/pull/48457) | `oss-sync-65c40d1f0e` | 84.4min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42135808011) |
| #42125241773 | `oss-sync-700891a42b` | 80.0min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42125241773) |
| #42176662893<br>[#48399 [Refactor] env: Dispatch on the GPU architecture instead of env vars that restate it](https://github.com/sgl-project/sglang/pull/48399) | `bbuf/env-arch-dispatch` | 78.9min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42176662893) |
| #42125015575<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 78.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42125015575) |
| #42124206422<br>[#48061 [Fix] batch-invariant: restore the dispatcher state when a scope exits](https://github.com/sgl-project/sglang/pull/48061) | `oss-sync-3d772da99f` | 77.5min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42124206422) |
| #42175870641<br>[#48547 [Feat] model: Support ERNIE 5.5 Flash](https://github.com/sgl-project/sglang/pull/48547) | `ernie-55-flash-day0` | 76.2min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42175870641) |
| #42129499669 | `oss-sync-5f33eae5cc` | 68.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42129499669) |
| #42156761699<br>[#47538 [Feat] http_server: Dispatch SageMaker /invocations to completions and embeddings by request body](https://github.com/sgl-project/sglang/pull/47538) | `sagemaker-invocations-dispatch` | 67.6min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42156761699) |
| #42214846330<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 64.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42214846330) |
| #42165696031<br>[#46953 [Feat] weight_cache: Add the vmm_fd transport](https://github.com/sgl-project/sglang/pull/46953) | `weight-cache-vmm-fd-upstream` | 63.8min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42165696031) |
| #42155947813<br>[#46291 [Feat] rust-server: multimodal (image) preprocessing through sglang-processor](https://github.com/sgl-project/sglang/pull/46291) | `processor-mm-qwen-vl` | 63.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42155947813) |
| #42150018137<br>[#48375 [Feat] PD: Publish spec_kv_layout so DSpark/DFlash prefill and decode must match](https://github.com/sgl-project/sglang/pull/48375) | `pd-spec-kv-layout` | 63.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42150018137) |
| #42153483517 | `feature/leixin/qwen3-blockfp8-quant-fusion` | 62.7min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42153483517) |
| #42219169517<br>[#47867 [Feat] [AMD] hicache: Add --hicache-mamba-size-gb to pin the HiCache Mamba host pool size](https://github.com/sgl-project/sglang/pull/47867) | `k3/hicache-mamba-size-gb` | 62.0min | 3 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42219169517) |
| #42116222387<br>[#48606 [Refactor] scheduler: Release retracted, paused and chunked-aborted requests through RequestRetirer](https://github.com/sgl-project/sglang/pull/48606) | `lsyin/sched-pr23` | 61.7min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42116222387) |
| #42116152423 | `oss-sync-5ac6bc3c22` | 61.2min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42116152423) |
| #42156543094<br>[#48721 [Feat] kimi-k3.1: DSA decode context parallelism runtime](https://github.com/sgl-project/sglang/pull/48721) | `kpham/k31-dcp-decode-runtime` | 61.0min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42156543094) |
| #42155370408<br>[#42388 [Feat] gdn: Add --enable-linear-lossless-verify for bit-exact tuple replay in spec verify](https://github.com/sgl-project/sglang/pull/42388) | `lossless-gdn-tuple-verify` | 60.4min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42155370408) |
| #42188605678<br>[#48217 [Refactor] custom-ar-v2: Single-word push epoch and consume-style pull semaphores](https://github.com/sgl-project/sglang/pull/48217) | `comm-push-epoch-protocol` | 60.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42188605678) |
| #42123925351 | `oss-sync-fa6ceed880` | 58.3min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42123925351) |
| #42142008951<br>[#48693 [Fix] hicache: Do not count staged-prefetch deferrals while KV awaits a PD transfer](https://github.com/sgl-project/sglang/pull/48693) | `oss-sync-fa6ceed880` | 56.3min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42142008951) |
| #42156645522<br>[#43851 [Feat] [NVIDIA] dsv4.1: [1/N] Add packed FP4 Main KV storage for Hopper.](https://github.com/sgl-project/sglang/pull/43851) | `feat/dsv41-packed-main-kv` | 55.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42156645522) |
| #42222690037<br>[#48642 [Feat] paged-experts: keep experts on disk so later starts skip loading them](https://github.com/sgl-project/sglang/pull/48642) | `feature/paged-experts-expert-cache` | 52.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42222690037) |
| #42098676255<br>[#48952 [CI] ep: Port the manual FlashInfer dispatcher test to flashinfer.moe_ep](https://github.com/sgl-project/sglang/pull/48952) | `flashinfer-0.7.3-moe-ep` | 51.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42098676255) |
| #42122889541<br>[#48952 [CI] ep: Port the manual FlashInfer dispatcher test to flashinfer.moe_ep](https://github.com/sgl-project/sglang/pull/48952) | `flashinfer-0.7.3-moe-ep` | 50.7min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42122889541) |
| #42155048261<br>[#48547 [Feat] model: Support ERNIE 5.5 Flash](https://github.com/sgl-project/sglang/pull/48547) | `ernie-55-flash-day0` | 50.3min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42155048261) |
| #42137432746<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 48.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42137432746) |
| #42153160933<br>[#48781 [Refactor] utils: Split `common.py` into topic modules and owner packages](https://github.com/sgl-project/sglang/pull/48781) | `lsyin/srt-utils-split-common` | 48.6min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42153160933) |
| #42114357010<br>[#48715 [Feat] linker: Deduplicate Kimi-K3.1 prefill-CP L3 pages and read them over RDMA](https://github.com/sgl-project/sglang/pull/48715) | `k31/linker-pcp-l3` | 47.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42114357010) |
| #42185109137<br>[#48399 [Refactor] env: Dispatch on the GPU architecture instead of env vars that restate it](https://github.com/sgl-project/sglang/pull/48399) | `bbuf/env-arch-dispatch` | 46.8min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42185109137) |
| #42133526452 | `bench-serving-per-run-accept-length` | 45.5min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42133526452) |
| #42121134606<br>[#48734 [Fix] spec: Make per-step draft `out_cache_loc` contiguous for KV writes](https://github.com/sgl-project/sglang/pull/48734) | `lsyin/fix-draft-loc-contiguous` | 45.3min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42121134606) |
| #42196662209<br>[#43465 [Feat] [AMD] DeepSeek-v4.1: Support prefill context parallel](https://github.com/sgl-project/sglang/pull/43465) | `fangyuan/dsv4p1_pcp` | 44.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42196662209) |
| #42153930501<br>[#48507 [Fix] multimodal: Cap receive-time CUDA VMM feature copies per GPU and stage the rest in pinned host memory](https://github.com/sgl-project/sglang/pull/48507) | `oss-sync-94d8b244ad` | 44.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42153930501) |
| #42139587595<br>[#48518 [Fix] server-args: Redact the access keys from /server_info, logs, launch_command and crash dumps](https://github.com/sgl-project/sglang/pull/48518) | `oss-sync-5f33eae5cc` | 44.0min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42139587595) |
| #42193400872<br>[#47052 [Perf] [AMD] qwen3: Fuse prefill QK-norm + RoPE on ROCm with the JIT qknorm_rope kernel](https://github.com/sgl-project/sglang/pull/47052) | `perf/qwen3-hip-qknorm-rope` | 43.8min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42193400872) |
| #42198192387<br>[#48762 [Refactor] scheduler: Run every state check through SchedulerInvariantChecker.run](https://github.com/sgl-project/sglang/pull/48762) | `lsyin/sched-pr25` | 43.2min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42198192387) |
| #42150345686<br>[#45803 [Fix] parser: Fix reasoning/tool-call grammar handoff and GLM-4.5 argument parsing](https://github.com/sgl-project/sglang/pull/45803) | `feat/ling3-pub-parser` | 41.5min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42150345686) |
| #42188229259<br>[#48952 [CI] ep: Port the manual FlashInfer dispatcher test to flashinfer.moe_ep](https://github.com/sgl-project/sglang/pull/48952) | `flashinfer-0.7.3-moe-ep` | 41.2min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42188229259) |
| #42136228226 | `hicache/scheduler-thread-agreement` | 40.9min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42136228226) |
| #42072668339<br>[#47930 [Feat] [NVIDIA] megakernel: Support prefill and extend steps](https://github.com/sgl-project/sglang/pull/47930) | `megakernel-prefill-extend` | 40.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42072668339) |
| #42185413202<br>[#47930 [Feat] [NVIDIA] megakernel: Support prefill and extend steps](https://github.com/sgl-project/sglang/pull/47930) | `megakernel-prefill-extend` | 39.5min | 4 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42185413202) |
| #42132343178<br>[#48433 [Feat] weight_update: Let platforms serve weight transports through /plugin_weight_update](https://github.com/sgl-project/sglang/pull/48433) | `hejian/plugin-weight-update` | 36.8min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42132343178) |
| #42149874285<br>[#48579 [Perf] io_struct: Validate an input_embeds body against one union member](https://github.com/sgl-project/sglang/pull/48579) | `perf/input-embeds-one-union-member` | 36.0min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42149874285) |
| #42173802571<br>[#43851 [Feat] [NVIDIA] dsv4.1: [1/N] Add packed FP4 Main KV storage for Hopper.](https://github.com/sgl-project/sglang/pull/43851) | `feat/dsv41-packed-main-kv` | 35.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42173802571) |
| #42136249293<br>[#47621 [Fix] hicache: buffer_only cuts an oversized storage hit to the prefix that fits](https://github.com/sgl-project/sglang/pull/47621) | `hicache/scheduler-thread-alloc` | 34.9min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42136249293) |
| #42136394141<br>[#48721 [Feat] kimi-k3.1: DSA decode context parallelism runtime](https://github.com/sgl-project/sglang/pull/48721) | `kpham/k31-dcp-decode-runtime` | 34.7min | 4 | multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42136394141) |
| #42215269419<br>[#48895 [Perf] [NVIDIA] dsa/dcp: Fused DCP8 indexer top-k for decode](https://github.com/sgl-project/sglang/pull/48895) | `dcp-fused-topk-main` | 33.6min | 2 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42215269419) |
| #42240598347<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 33.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42240598347) |
| #42093810892<br>[#48952 [CI] ep: Port the manual FlashInfer dispatcher test to flashinfer.moe_ep](https://github.com/sgl-project/sglang/pull/48952) | `flashinfer-0.7.3-moe-ep` | 32.0min | 4 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42093810892) |
| #42182940684<br>[#48827 [Refactor] utils: Keep sglang.srt and sglang.kernels off sglang.utils](https://github.com/sgl-project/sglang/pull/48827) | `lsyin/srt-no-sglang-utils` | 31.9min | 2 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42182940684) |
| #42208574201<br>[#44753 [Refactor] RoPE: Support RotaryEmbedding class usage for DiT models](https://github.com/sgl-project/sglang/pull/44753) | `rope_support_dits` | 31.5min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42208574201) |
| #42134506049<br>[#48755 [Chore] utils: Guard `srt.utils` imports and remove dead code](https://github.com/sgl-project/sglang/pull/48755) | `lsyin/srt-utils-cleanup` | 29.6min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42134506049) |
| #42194497774<br>[#45891 [Perf] dsa: Run the packed prefill top-k on CUDA](https://github.com/sgl-project/sglang/pull/45891) | `topk-v2-packed-cuda` | 29.2min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42194497774) |
| #42119857635<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 29.2min | 6 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42119857635) |
| #42183989696<br>[#48547 [Feat] model: Support ERNIE 5.5 Flash](https://github.com/sgl-project/sglang/pull/48547) | `ernie-55-flash-day0` | 28.9min | 3 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42183989696) |
| #42198282384<br>[#48642 [Feat] paged-experts: keep experts on disk so later starts skip loading them](https://github.com/sgl-project/sglang/pull/48642) | `feature/paged-experts-expert-cache` | 28.6min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42198282384) |
| #42146000072<br>[#48715 [Feat] linker: Deduplicate Kimi-K3.1 prefill-CP L3 pages and read them over RDMA](https://github.com/sgl-project/sglang/pull/48715) | `k31/linker-pcp-l3` | 27.4min | 5 | multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42146000072) |
| #42191830571<br>[#47469 [Perf] [NVIDIA] attention: Add opt-in LiteTopK prefill indexer top-k for DSA (FP8) and DeepSeek-V4.1 (FP4) on SM100](https://github.com/sgl-project/sglang/pull/47469) | `litetopk-prefill` | 26.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42191830571) |
| #42123605224<br>[#48446 [Fix] io_struct: Give each request its own sampling_params dict during normalization](https://github.com/sgl-project/sglang/pull/48446) | `oss-sync-71332a38e2` | 26.2min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42123605224) |
| #42081204286 | `oss-sync-fa6ceed880` | 26.2min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42081204286) |
| #42119853992<br>[#47862 [Feat] [AMD] aiter: One folder of in-tree aiter tuned rows for every model](https://github.com/sgl-project/sglang/pull/47862) | `m31-amd/aiter-tuned-tables` | 24.9min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42119853992) |
| #42119850375<br>[#46693 [Feat] [AMD] minimax: Support MiniMax-M3.1-Flash on MI350X / MI355X (gfx950)](https://github.com/sgl-project/sglang/pull/46693) | `m31-amd/integration` | 24.9min | 5 | multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42119850375) |
| #42163136117<br>[#38749 [Feat] kernels: Add out-of-tree dispatch for gated RMSNorm](https://github.com/sgl-project/sglang/pull/38749) | `vincent/gated-rmsnorm-oot` | 24.8min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42163136117) |
| #42186436710 | `feature/leixin/qwen3-blockfp8-quant-fusion` | 24.7min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42186436710) |
| #42172946961<br>[#48781 [Refactor] utils: Split `common.py` into topic modules and owner packages](https://github.com/sgl-project/sglang/pull/48781) | `lsyin/srt-utils-split-common` | 24.7min | 9 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42172946961) |
| #42191959970<br>[#41635 [Feat] gemma4: Add out-of-tree MoE expert executor selection](https://github.com/sgl-project/sglang/pull/41635) | `add-oot-moe-expert-executor` | 24.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42191959970) |
| #42186665438<br>[#46663 [Fix] gemma4: Fix Bolt E4B and Gemma4 prefill CUDA graphs](https://github.com/sgl-project/sglang/pull/46663) | `fix/gemma4-shared-kv-graphs` | 24.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42186665438) |
| #42124851659<br>[#48737 [Chore] ci: Cut deprecation warnings and TBO debug logs from CI output](https://github.com/sgl-project/sglang/pull/48737) | `lsyin/ci-warning-noise` | 20.0min | 5 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42124851659) |
| #42074484922<br>[#44360 [Perf] [AMD] kimi-k3: Run the merged MoE front through AITER tuned BF16 GEMM](https://github.com/sgl-project/sglang/pull/44360) | `k3/tuned-moe-front` | 17.8min | 8 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42074484922) |
| #42145343246<br>[#48758 [Refactor] utils: Move domain-dependent modules out of `srt.utils`](https://github.com/sgl-project/sglang/pull/48758) | `lsyin/srt-utils-owners` | 17.7min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42145343246) |
| #42193012336<br>[#48757 [Fix] scheduler: Abort beam groups on a retract pause and close three request-drop gaps](https://github.com/sgl-project/sglang/pull/48757) | `lsyin/sched-pr24` | 17.2min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42193012336) |
| #42134760422 | `hicache/scheduler-thread-agreement` | 17.1min | 4 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42134760422) |
| #42190015350<br>[#47469 [Perf] [NVIDIA] attention: Add opt-in LiteTopK prefill indexer top-k for DSA (FP8) and DeepSeek-V4.1 (FP4) on SM100](https://github.com/sgl-project/sglang/pull/47469) | `litetopk-prefill` | 15.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42190015350) |
| #42146398132<br>[#48399 [Refactor] env: Dispatch on the GPU architecture instead of env vars that restate it](https://github.com/sgl-project/sglang/pull/48399) | `bbuf/env-arch-dispatch` | 15.5min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42146398132) |
| #42123117918<br>[#48737 [Chore] ci: Cut deprecation warnings and TBO debug logs from CI output](https://github.com/sgl-project/sglang/pull/48737) | `lsyin/ci-warning-noise` | 13.7min | 6 | base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42123117918) |
| #42192330172<br>[#48763 [Feat] dflash: Serve MoE FFN drafts for DFlash and DSpark](https://github.com/sgl-project/sglang/pull/48763) | `dflash-family-moe-ffn` | 10.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42192330172) |
| #42190297303<br>[#48763 [Feat] dflash: Serve MoE FFN drafts for DFlash and DSpark](https://github.com/sgl-project/sglang/pull/48763) | `dflash-family-moe-ffn` | 9.6min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42190297303) |
| #42150682537<br>[#44416 [Perf] [AMD] GLM-5.3-Flash: One-launch MoE router and narrower KDA V tile for MTP verify](https://github.com/sgl-project/sglang/pull/44416) | `jacob/glm53-flash-moe-router-kda` | 9.4min | 4 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42150682537) |
| #42152325582<br>[#48781 [Refactor] utils: Split `common.py` into topic modules and owner packages](https://github.com/sgl-project/sglang/pull/48781) | `lsyin/srt-utils-split-common` | 9.3min | 2 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42152325582) |
| #42183321329<br>[#36153 [Feat] [Intel] diffusion: Add packed QKV kernel and enable Ulysses SP on CPU](https://github.com/sgl-project/sglang/pull/36153) | `cpu-ulysses-pack-qkv` | 8.9min | 3 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42183321329) |
| #42115220323<br>[#48606 [Refactor] scheduler: Release retracted, paused and chunked-aborted requests through RequestRetirer](https://github.com/sgl-project/sglang/pull/48606) | `lsyin/sched-pr23` | 8.0min | 8 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42115220323) |
| #42151442828<br>[#47469 [Perf] [NVIDIA] attention: Add opt-in LiteTopK prefill indexer top-k for DSA (FP8) and DeepSeek-V4.1 (FP4) on SM100](https://github.com/sgl-project/sglang/pull/47469) | `litetopk-prefill` | 7.5min | 4 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42151442828) |
| #42182616481<br>[#36153 [Feat] [Intel] diffusion: Add packed QKV kernel and enable Ulysses SP on CPU](https://github.com/sgl-project/sglang/pull/36153) | `cpu-ulysses-pack-qkv` | 7.0min | 2 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42182616481) |
| #42185365009<br>[#48093 [Perf] [AMD] dsv4: Cut HIP prefill and verify host overhead](https://github.com/sgl-project/sglang/pull/48093) | `dsv4-host-overhead-gfx1250_di_5/N` | 6.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42185365009) |
| #42182041205<br>[#36153 [Feat] [Intel] diffusion: Add packed QKV kernel and enable Ulysses SP on CPU](https://github.com/sgl-project/sglang/pull/36153) | `cpu-ulysses-pack-qkv` | 6.5min | 3 | multimodal-gen-test-1-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42182041205) |
| #42188804555<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 6.0min | 6 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42188804555) |
| #42123287188<br>[#46693 [Feat] [AMD] minimax: Support MiniMax-M3.1-Flash on MI350X / MI355X (gfx950)](https://github.com/sgl-project/sglang/pull/46693) | `m31-amd/integration` | 5.7min | 1 | base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42123287188) |
| #42209509299<br>[#45529 [Perf] [AMD] qwen3.5: Fuse self-attn prepare on gfx950 (norm+RoPE+gate)](https://github.com/sgl-project/sglang/pull/45529) | `opt/qwen35_fuse_norm_rotary` | 5.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42209509299) |

---


## [Run #42240598347](https://github.com/sgl-project/sglang/actions/runs/42240598347)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 33.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42240598347

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 18.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040985) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040985

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127969769732) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127969769838) |
| multimodal-gen-test-4-npu-a3 (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040440) |
| multimodal-gen-test-1-npu-a3 (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040457) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040613) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971040953) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971041077) |
| base-b-test-16-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971041116) |
| base-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971041264) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971041347) |
| multimodal-gen-test-4-npu-a3 (1) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42240598347/job/127971042092) |


## [Run #42222690037](https://github.com/sgl-project/sglang/actions/runs/42222690037)
- **分支**: `feature/paged-experts-expert-cache`
- **总耗时**: 52.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42222690037

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 22.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127983007861) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127983007861

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127967273699) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127967273710) |
| multimodal-gen-test-4-npu-a3 (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359163) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359312) |
| base-b-test-2-npu-a3 / run (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359357) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359458) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359480) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359559) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968359804) |
| base-b-test-16-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127968360499) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127983007872) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42222690037/job/127983008085) |


## [Run #42221883221](https://github.com/sgl-project/sglang/actions/runs/42221883221)
- **分支**: `codex/muse-b200-b1-runtime`
- **总耗时**: 126.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42221883221

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906851910) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906851910

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127905901832) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127905901963) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906851788) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906851799) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852029) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852552) |
| base-b-test-16-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852597) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852676) |
| base-b-test-4-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852745) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852750) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127906852798) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 38.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127924404635) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127924404683) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127924404777) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127943386665) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42221883221/job/127943386912) |


## [Run #42219169517](https://github.com/sgl-project/sglang/actions/runs/42219169517)
- **分支**: `k3/hicache-mamba-size-gb`
- **总耗时**: 62.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42219169517

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 6.1min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业本身未报失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627014) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627038) |
| multimodal-gen-test-1-npu-a3 (0) | 6.5min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627116) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志被截断，可见部分只有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback 或退出码信息。推测测试脚本未生成失败产物目录，可能 setUpClass 阶段 server 启动失败或测试未真正执行，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627014

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业在约3分钟内结束，未上传 diffusion-failures 产物（目录不存在），说明用例未正常执行到产出阶段。退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627038

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627116

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127896845765) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127896845916) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627079) |
| base-b-test-2-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627256) |
| base-b-test-4-npu-a3 / run (1) | 6.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627355) |
| base-b-test-1-npu-a3 / run (0) | 5.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627464) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127897627481) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219169517/job/127905390975) |


## [Run #42219155484](https://github.com/sgl-project/sglang/actions/runs/42219155484)
- **分支**: `k3-pr1-quark-weights`
- **总耗时**: 134.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42219155484

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 4.0min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786391) |
| multimodal-gen-test-4-npu-a3 (1) | 3.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786500) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786515) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业以退出码5结束（unittest errors），且未生成 diffusion-failures/ 目录产物。最常见原因是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略部分的 Traceback/RuntimeError 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786391

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行异常。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786500

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786515

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127896750683) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127896750840) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786474) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786532) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786570) |
| base-b-test-16-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786667) |
| base-b-test-1-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786668) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786762) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127897786874) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127920158516) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127920158591) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127920158626) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127942153518) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42219155484/job/127942153826) |


## [Run #42216674902](https://github.com/sgl-project/sglang/actions/runs/42216674902)
- **分支**: `main`
- **总耗时**: 84.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42216674902

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 6.3min | 环境问题 | pip 安装依赖失败，找不到 psutil==6.0.0 版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127915417946) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 安装 triton-ascend 依赖时，pip 报错 Could not find a version that satisfies the requirement psutil==6.0.0（from versions: none），导致依赖安装失败、作业退出码 1。属于依赖源/镜像环境问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127915417946

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127888471106) |
| multimodal-gen-test-4-npu-a3 (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537085) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537143) |
| multimodal-gen-test-1-npu-a3 (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537179) |
| multimodal-gen-test-1-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537195) |
| base-b-test-2-npu-a3 / run (0) | 38.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537248) |
| base-b-test-4-npu-a3 / run (0) | 59.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537278) |
| base-b-test-16-npu-a3 / run (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537297) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537311) |
| base-b-test-1-npu-a3 / run (0) | 44.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537338) |
| base-b-test-8-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127889537515) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127915417922) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42216674902/job/127915418048) |


## [Run #42215269419](https://github.com/sgl-project/sglang/actions/runs/42215269419)
- **分支**: `dcp-fused-topk-main`
- **总耗时**: 33.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42215269419

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666343) |
| base-b-test-16-npu-a3 / run (0) | 22.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666532) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666343

- **base-b-test-16-npu-a3 / run (0)**: 日志显示各 TP/EP 权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境问题，并非用例或代码本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666532

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127883765407) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127883766547) |
| multimodal-gen-test-4-npu-a3 (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666315) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666426) |
| base-b-test-1-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666492) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666575) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666669) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42215269419/job/127884666929) |


## [Run #42214846330](https://github.com/sgl-project/sglang/actions/runs/42214846330)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 64.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42214846330

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.1min | 环境问题 | pip 安装 pytest 依赖 packaging 时找不到可用版本，依赖安装失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127893664302) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 pip 解析 pytest 依赖 packaging 时提示 Could not find a version that satisfies the requirement packaging，无匹配发行版，导致依赖安装步骤退出码 1，作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127893664302

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127882367028) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127882367047) |
| multimodal-gen-test-1-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883442996) |
| multimodal-gen-test-1-npu-a3 (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443038) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443054) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443058) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443066) |
| multimodal-gen-test-4-npu-a3 (0) | 33.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443095) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443150) |
| base-b-test-16-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443211) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443240) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127883443299) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127893664277) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42214846330/job/127893664343) |


## [Run #42209509299](https://github.com/sgl-project/sglang/actions/runs/42209509299)
- **分支**: `opt/qwen35_fuse_norm_rotary`
- **总耗时**: 5.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42209509299

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42209509299/job/127865666220) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42209509299/job/127865666240) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42209509299/job/127864591986) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42209509299/job/127864592067) |


## [Run #42208574201](https://github.com/sgl-project/sglang/actions/runs/42208574201)
- **分支**: `rope_support_dits`
- **总耗时**: 31.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42208574201

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.8min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862119100) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中作业退出并上传 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行出错；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862119100

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127861461984) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862118695) |
| multimodal-gen-test-4-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862118814) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42208574201/job/127862118944) |


## [Run #42198282384](https://github.com/sgl-project/sglang/actions/runs/42198282384)
- **分支**: `feature/paged-experts-expert-cache`
- **总耗时**: 28.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42198282384

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 1.5min | 环境问题 | git fetch 首次连接 git-cdn-service 端口 8000 被拒绝，重试后成功，作业最终失败原因需看后续日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918339) |
| base-b-test-4-npu-a3 / run (0) | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918427) |
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918445) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918548) |

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 checkout 阶段 git fetch 首次报 Connection refused（git-cdn-service:8000），17 秒后重试成功并完成 checkout；随后运行 k8s index.js 后作业结束，仅见 Node.js 弃用警告，未见明确测试错误。失败可能源于环境/基础设施不稳定，需结合后续日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918339




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827122010) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827122036) |
| multimodal-gen-test-4-npu-a3 (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918175) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918248) |
| base-b-test-16-npu-a3 / run (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918328) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198282384/job/127827918378) |


## [Run #42198192387](https://github.com/sgl-project/sglang/actions/runs/42198192387)
- **分支**: `lsyin/sched-pr25`
- **总耗时**: 43.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42198192387

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.7min | 环境问题 | git 拉取代码时连接内部 git-cdn 服务被拒绝，重试后成功，但作业随后异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660615) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 git fetch 访问 git-cdn-service:8000 出现 Connection refused，重试后成功检出代码；随后运行 k8s 脚本后仅出现 Node 弃用警告即清理进程，未见测试执行或明确错误，疑似 runner/环境侧异常导致作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660615

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127826805222) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127826805354) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660445) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660453) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660605) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660643) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660652) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660723) |
| multimodal-gen-test-4-npu-a3 (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42198192387/job/127827660744) |


## [Run #42196662209](https://github.com/sgl-project/sglang/actions/runs/42196662209)
- **分支**: `fangyuan/dsv4p1_pcp`
- **总耗时**: 44.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42196662209

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114565) |
| base-b-test-2-npu-a3 / run (0) | 5.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114567) |


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114567

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127821893099) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127821893121) |
| multimodal-gen-test-4-npu-a3 (0) | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114422) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114492) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114523) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114588) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114592) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114599) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114745) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42196662209/job/127823114787) |


## [Run #42194497774](https://github.com/sgl-project/sglang/actions/runs/42194497774)
- **分支**: `topk-v2-packed-cuda`
- **总耗时**: 29.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42194497774

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536176) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536176

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127814448928) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127814449002) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536038) |
| base-b-test-16-npu-a3 / run (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536087) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536166) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536230) |
| base-b-test-1-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536235) |
| base-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536241) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42194497774/job/127815536273) |


## [Run #42193400872](https://github.com/sgl-project/sglang/actions/runs/42193400872)
- **分支**: `perf/qwen3-hip-qknorm-rope`
- **总耗时**: 43.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42193400872

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 16.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127811544294) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127811544294

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127810827138) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127810827204) |
| base-b-test-1-npu-a3 / run (0) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127811544356) |
| base-b-test-4-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193400872/job/127811544519) |


## [Run #42193012336](https://github.com/sgl-project/sglang/actions/runs/42193012336)
- **分支**: `lsyin/sched-pr24`
- **总耗时**: 17.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42193012336

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 9.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606326) |
| base-b-test-4-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在测试中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606359) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606365) |
| base-b-test-2-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606405) |
| multimodal-gen-test-4-npu-a3 (0) | 1.8min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606449) |
| base-b-test-1-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606474) |
| base-b-test-16-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载过程中被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606546) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606326

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Capturing batches 进度到 75% 时出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606359

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；此前仅有 SymmetricMemory 不支持 cuda 的告警。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606365

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在加载权重阶段，属于 runner/容器环境故障，非代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606405

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中未见具体 Traceback，但退出码5表明 unittest 有 errors，常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606449

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 test_npu_autoround_moe.py 执行期间，属于 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606474

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载至64%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码错误；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606546

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127809540826) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127809541023) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42193012336/job/127810606398) |


## [Run #42192330172](https://github.com/sgl-project/sglang/actions/runs/42192330172)
- **分支**: `dflash-family-moe-ffn`
- **总耗时**: 10.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42192330172

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.1min | 环境问题 | 精度测试用例退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42192330172/job/127808084628) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py 运行50秒后退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。后续脚本还因变量含换行报integer expression expected错误。
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42192330172/job/127808084628

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42192330172/job/127807304206) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42192330172/job/127807304207) |


## [Run #42191959970](https://github.com/sgl-project/sglang/actions/runs/42191959970)
- **分支**: `add-oot-moe-expert-executor`
- **总耗时**: 24.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42191959970

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085785) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085785

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127806090593) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127806090784) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085597) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085672) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085708) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085753) |
| base-b-test-16-npu-a3 / run (0) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085763) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807085797) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191959970/job/127807086030) |


## [Run #42191830571](https://github.com/sgl-project/sglang/actions/runs/42191830571)
- **分支**: `litetopk-prefill`
- **总耗时**: 26.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42191830571

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42191830571/job/127809833311) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试请求正常返回 200，随后报错 'Executing the custom container implementation failed'，属于自托管 runner/K8s 容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42191830571/job/127809833311

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191830571/job/127805854093) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191830571/job/127805854168) |
| base-b-test-2-npu-a3 / run (0) | 6.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42191830571/job/127806912528) |


## [Run #42190297303](https://github.com/sgl-project/sglang/actions/runs/42190297303)
- **分支**: `dflash-family-moe-ffn`
- **总耗时**: 9.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42190297303

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.3min | 环境问题 | 精度测试用例退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42190297303/job/127801509104) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py 返回退出码5（unittest errors），通常为 setUpClass 中 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。后续脚本还因变量含换行报 integer expression expected，导致作业退出码1。
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42190297303/job/127801509104

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42190297303/job/127800518086) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42190297303/job/127800518096) |


## [Run #42190015350](https://github.com/sgl-project/sglang/actions/runs/42190015350)
- **分支**: `litetopk-prefill`
- **总耗时**: 15.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42190015350

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 3.2min | 环境问题 | 自托管 runner 的自定义容器启动失败，作业未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/42190015350/job/127804357315) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，与测试用例本身无关，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42190015350/job/127804357315

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42190015350/job/127799584423) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42190015350/job/127799584440) |
| base-b-test-2-npu-a3 / run (0) | 6.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42190015350/job/127800246095) |


## [Run #42188804555](https://github.com/sgl-project/sglang/actions/runs/42188804555)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 6.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42188804555

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 3.3min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441609) |
| multimodal-gen-test-1-npu-a3 (0) | 3.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441655) |
| multimodal-gen-test-4-npu-a3 (1) | 3.3min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441771) |
| base-b-test-8-npu-a3 / run (0) | 2.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441779) |
| multimodal-gen-test-1-npu-a3 (1) | 3.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441783) |
| base-b-test-4-npu-a3 / run (0) | 2.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441826) |
| base-b-test-2-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441827) |
| base-b-test-16-npu-a3 / run (0) | 2.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441848) |
| base-b-test-1-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441892) |
| base-b-test-4-npu-a3 / run (1) | 2.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441898) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和清理，未出现 Traceback 或 RuntimeError；upload-artifact 提示 diffusion-failures/ 无文件，说明测试产物未生成，疑似 setUpClass 阶段 server 启动失败或作业异常退出，需查看省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441609

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试未正常产出结果；退出码5对应 unittest errors，常见于 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441655

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，仅见 artifact 上传时提示 No files were found with the provided path: diffusion-failures/，无 Traceback 或退出码信息，无法确认具体失败原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441771


- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约3分钟即结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441783


- **base-b-test-2-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441827


- **base-b-test-1-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，并非用例或代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127796441892


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127795620204) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188804555/job/127795620212) |


## [Run #42188605678](https://github.com/sgl-project/sglang/actions/runs/42188605678)
- **分支**: `comm-push-epoch-protocol`
- **总耗时**: 60.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42188605678

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127804908972) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127804908972

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127794974001) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127794974006) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796024942) |
| multimodal-gen-test-4-npu-a3 (1) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796024954) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796024978) |
| base-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025021) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025049) |
| base-b-test-16-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025078) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025106) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025108) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025129) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127796025191) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127804908907) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188605678/job/127804908929) |


## [Run #42188229259](https://github.com/sgl-project/sglang/actions/runs/42188229259)
- **分支**: `flashinfer-0.7.3-moe-ep`
- **总耗时**: 41.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42188229259

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 12.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127804430218) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 13.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127804430387) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示服务端推理请求均返回 200，随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127804430218

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 k8s runner 无法启动/执行自定义容器（镜像 cann:9.1.0-a3），属 runner 环境问题，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127804430387

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127793735653) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127793736531) |
| multimodal-gen-test-4-npu-a3 (0) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794759689) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794759716) |
| multimodal-gen-test-1-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794759789) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794759835) |
| base-b-test-16-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794759887) |
| base-b-test-1-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794760032) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794760083) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794760104) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794760105) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127794760225) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42188229259/job/127804430319) |


## [Run #42186665438](https://github.com/sgl-project/sglang/actions/runs/42186665438)
- **分支**: `fix/gemma4-shared-kv-graphs`
- **总耗时**: 24.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42186665438

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 17.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319643) |
| base-b-test-16-npu-a3 / run (0) | 16.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319649) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319643


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127788697016) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127788697085) |
| multimodal-gen-test-4-npu-a3 (1) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319479) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319619) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319652) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319722) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319747) |
| base-b-test-4-npu-a3 / run (1) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186665438/job/127789319787) |


## [Run #42186436710](https://github.com/sgl-project/sglang/actions/runs/42186436710)
- **分支**: `feature/leixin/qwen3-blockfp8-quant-fusion`
- **总耗时**: 24.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42186436710

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 19.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943232) |
| base-b-test-4-npu-a3 / run (0) | 7.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943365) |
| base-b-test-4-npu-a3 / run (1) | 14.4min | 环境问题 | PD分离测试用例退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943366) |


- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943365

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行629秒后返回exit code 5，表明unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/2用例通过。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943366

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127787987824) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127787988001) |
| multimodal-gen-test-4-npu-a3 (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943045) |
| multimodal-gen-test-1-npu-a3 (0) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943061) |
| multimodal-gen-test-4-npu-a3 (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943065) |
| multimodal-gen-test-1-npu-a3 (1) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943205) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943277) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943344) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42186436710/job/127788943392) |


## [Run #42185413202](https://github.com/sgl-project/sglang/actions/runs/42185413202)
- **分支**: `megakernel-prefill-extend`
- **总耗时**: 39.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42185413202

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | 环境问题 | 日志中未见明确 Traceback，仅显示 diffusion-failures 目录无文件、artifact 上传为空，作业失败原因被省略段掩盖。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473143) |
| multimodal-gen-test-4-npu-a3 (1) | 26.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473296) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | 其他 | 测试套件未找到任何用例，脚本因空值比较报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127796373061) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127796373137) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 3.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127796373268) |

- **multimodal-gen-test-4-npu-a3 (0)**: 可见日志仅有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无真实错误堆栈；中间省略段可能含退出码 5 的 unittest errors（如 setUpClass 中 server 启动失败/OOM）。需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473143

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件、Failed to copy _temp from pod，说明容器内测试异常退出；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473296

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 No tests found for hw=NPU, suite=base-c-test-acc-2-npu-a3，0/0 通过；随后 shell 第223行对空变量做整数比较报 integer expression expected，导致作业失败。属用例未迁移/配置问题，非精度回归。
  链接: https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127796373061

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员。作业在容器启动阶段失败，尚未进入测试用例执行，非精度或代码问题，属 runner/容器环境故障。
  链接: https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127796373137


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127784631494) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127784631594) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473346) |
| base-b-test-16-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473372) |
| base-b-test-1-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473396) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473418) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473423) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473430) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473480) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185413202/job/127785473586) |


## [Run #42185365009](https://github.com/sgl-project/sglang/actions/runs/42185365009)
- **分支**: `dsv4-host-overhead-gfx1250_di_5/N`
- **总耗时**: 6.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42185365009

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 0.8min | 环境问题 | Kubernetes 创建作业 Pod 超时，容器未启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185365009/job/127785131517) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 failed to create job pod，请求超时（context deadline exceeded），Pod spec 被 k8s API 拒绝或调度失败，测试代码未执行，属基础设施/环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42185365009/job/127785131517

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185365009/job/127784489961) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185365009/job/127784489995) |


## [Run #42185109137](https://github.com/sgl-project/sglang/actions/runs/42185109137)
- **分支**: `bbuf/env-arch-dispatch`
- **总耗时**: 46.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42185109137

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941790) |
| base-b-test-1-npu-a3 / run (0) | 5.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941833) |


- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941833

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784220746) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784220846) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941530) |
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941650) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941688) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941707) |
| base-b-test-2-npu-a3 / run (0) | 26.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941740) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941858) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941883) |
| base-b-test-4-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42185109137/job/127784941987) |


## [Run #42183989696](https://github.com/sgl-project/sglang/actions/runs/42183989696)
- **分支**: `ernie-55-flash-day0`
- **总耗时**: 28.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42183989696

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 24.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257641) |
| multimodal-gen-test-4-npu-a3 (1) | 23.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257726) |
| base-b-test-4-npu-a3 / run (1) | 17.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257788) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，作业以退出码5结束，符合unittest errors特征，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257641

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约23分钟后结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257726

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257788

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127780454592) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127780454713) |
| multimodal-gen-test-1-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257672) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257693) |
| base-b-test-16-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257694) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257697) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257704) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257753) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183989696/job/127781257766) |


## [Run #42183321329](https://github.com/sgl-project/sglang/actions/runs/42183321329)
- **分支**: `cpu-ulysses-pack-qkv`
- **总耗时**: 8.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42183321329

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 1.6min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778794869) |
| multimodal-gen-test-1-npu-a3 (0) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778794913) |
| multimodal-gen-test-4-npu-a3 (0) | 2.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778794925) |
| base-b-test-16-npu-a3 / run (0) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795064) |
| base-b-test-4-npu-a3 / run (1) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795066) |
| base-b-test-4-npu-a3 / run (0) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795068) |
| multimodal-gen-test-1-npu-a3 (1) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795081) |
| base-b-test-1-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795087) |
| base-b-test-8-npu-a3 / run (0) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795106) |
| base-b-test-2-npu-a3 / run (0) | 4.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795244) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，可见部分只有 runner 初始化、action 下载和清理，未出现 Traceback 或退出码 5 的 unittest 错误；upload-artifact 提示 diffusion-failures/ 不存在，说明测试脚本可能未产出失败目录或未真正运行，需查看完整日志确认 server 启动情况。
  链接: https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778794869


- **multimodal-gen-test-4-npu-a3 (0)**: 日志中未见具体Traceback，但退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。另diffusion-failures目录无文件，artifact上传为空。
  链接: https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778794925





- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在测试用例启动后约10秒，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778795087



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778033494) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42183321329/job/127778033546) |


## [Run #42182940684](https://github.com/sgl-project/sglang/actions/runs/42182940684)
- **分支**: `lsyin/srt-no-sglang-utils`
- **总耗时**: 31.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42182940684

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778063988) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127786192949) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.5min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127786192971) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127786193029) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778063988



- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 pip 安装 triton-ascend 等依赖时卸载 numpy/psutil 后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127786193029

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127777352144) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127777352175) |
| multimodal-gen-test-1-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778063984) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064060) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064106) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064112) |
| base-b-test-16-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064163) |
| base-b-test-4-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064180) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064203) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064207) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182940684/job/127778064242) |


## [Run #42182616481](https://github.com/sgl-project/sglang/actions/runs/42182616481)
- **分支**: `cpu-ulysses-pack-qkv`
- **总耗时**: 7.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42182616481

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 3.3min | 环境问题 | 作业日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648458) |
| multimodal-gen-test-1-npu-a3 (1) | 2.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648510) |
| multimodal-gen-test-4-npu-a3 (0) | 2.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648564) |
| multimodal-gen-test-4-npu-a3 (1) | 2.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648590) |
| base-b-test-16-npu-a3 / run (0) | 2.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648618) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648633) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648639) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648658) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648695) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648756) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，缺少真实错误信息。仅见 upload-artifact 提示未找到 diffusion-failures/ 路径，无 Traceback 或退出码 5 相关记录，无法判定为用例失败或环境问题，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648458


- **multimodal-gen-test-4-npu-a3 (0)**: 日志中未见具体Traceback，但退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。另diffusion-failures目录无文件，artifact上传为空。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776648564








### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776006209) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182616481/job/127776006322) |


## [Run #42182041205](https://github.com/sgl-project/sglang/actions/runs/42182041205)
- **分支**: `cpu-ulysses-pack-qkv`
- **总耗时**: 6.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42182041205

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 3.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426426) |
| multimodal-gen-test-4-npu-a3 (0) | 3.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426437) |
| multimodal-gen-test-4-npu-a3 (1) | 3.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426478) |
| multimodal-gen-test-1-npu-a3 (0) | 1.3min | 环境问题 | 作业在测试执行阶段失败，日志中未见具体 Traceback，仅显示未找到 diffusion-failures/ 目录，疑似 sglang server 启动失败导致用例 error。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426484) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426491) |
| base-b-test-2-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426517) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426571) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426585) |
| base-b-test-1-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426691) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426949) |




- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，缺少真实错误信息。upload-artifact 提示未找到 diffusion-failures/ 路径，说明测试未产出失败用例文件；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426484


- **base-b-test-2-npu-a3 / run (0)**: 日志显示 pip 卸载 numpy/scipy 等包后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426517



- **base-b-test-1-npu-a3 / run (0)**: 日志显示 CANN 自定义算子安装成功后，报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127774426691


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127773791193) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42182041205/job/127773791222) |


## [Run #42176662893](https://github.com/sgl-project/sglang/actions/runs/42176662893)
- **分支**: `bbuf/env-arch-dispatch`
- **总耗时**: 78.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42176662893

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 8.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127780888478) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 6.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127780888496) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，并非用例断言失败；此前 generate 请求均返回 200，随后容器执行报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127780888478

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示模型分片加载到47%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码或性能回归问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127780888496

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127758371774) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127758371835) |
| multimodal-gen-test-1-npu-a3 (1) | 33.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759209996) |
| multimodal-gen-test-1-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210020) |
| multimodal-gen-test-4-npu-a3 (1) | 34.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210077) |
| multimodal-gen-test-4-npu-a3 (0) | 44.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210099) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210189) |
| base-b-test-1-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210199) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210263) |
| base-b-test-4-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210302) |
| base-b-test-16-npu-a3 / run (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210307) |
| base-b-test-2-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127759210359) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127768667541) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127768667635) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42176662893/job/127768667687) |


## [Run #42175870641](https://github.com/sgl-project/sglang/actions/runs/42175870641)
- **分支**: `ernie-55-flash-day0`
- **总耗时**: 76.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42175870641

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 19.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在模型分片加载中途被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127773095466) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 19.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127773095579) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示模型权重分片加载到 23% 时出现 'Executing the custom container implementation failed'，属于 runner/容器基础设施异常，并非用例断言失败；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127773095466

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 Capturing batches 阶段后报错 'Executing the custom container implementation failed'，属 runner/容器环境异常，非用例代码或性能回归问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127773095579

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127754228577) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127754228586) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114599) |
| multimodal-gen-test-1-npu-a3 (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114661) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114697) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114732) |
| multimodal-gen-test-1-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114757) |
| base-b-test-1-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114785) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114823) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114849) |
| base-b-test-2-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755114870) |
| multimodal-gen-test-4-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127755115529) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127763617493) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127763617517) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42175870641/job/127763617591) |


## [Run #42173802571](https://github.com/sgl-project/sglang/actions/runs/42173802571)
- **分支**: `feat/dsv41-packed-main-kv`
- **总耗时**: 35.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42173802571

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 19.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624205) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_w4a4_quantization.py, npu_w4a4_quantization.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624205

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127791892280) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127791892394) |
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792623850) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792623879) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624028) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624033) |
| base-b-test-1-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624077) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624167) |
| base-b-test-2-npu-a3 / run (0) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42173802571/job/127792624208) |


## [Run #42172946961](https://github.com/sgl-project/sglang/actions/runs/42172946961)
- **分支**: `lsyin/srt-utils-split-common`
- **总耗时**: 24.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42172946961

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 5.7min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784395) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784469) |
| multimodal-gen-test-1-npu-a3 (1) | 6.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784497) |
| multimodal-gen-test-1-npu-a3 (0) | 5.9min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784527) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784615) |
| base-b-test-2-npu-a3 / run (0) | 16.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784618) |
| base-b-test-1-npu-a3 / run (0) | 15.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784654) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784673) |
| base-b-test-4-npu-a3 / run (0) | 12.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784693) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业在约6分钟内结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784395

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业约6分钟结束，退出码5表示unittest存在errors，常见于setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。日志中未见diffusion-failures目录，无产物上传，需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784469

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中未见明确 Traceback，但退出码5表示 unittest errors，常见于 setUpClass 时 server 启动失败（如 host OOM 或进程被 SIGKILL）；且 diffusion-failures/ 目录无文件，未上传失败产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784497

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试脚本未产出失败样本；结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784527

- **base-b-test-8-npu-a3 / run (0)**: 日志中唯一用例 test_npu_eplb_min_rebalancing_utilization_threshold.py 通过（1/1 passed），随后正常执行 Post job cleanup，未见 Traceback、RuntimeError 或非零退出码。若作业被判失败，可能为后续清理/上报步骤或外部状态导致，需查看被省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784615

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例代码或精度问题；此时正在运行第6个用例，作业随即终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784618

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例断言失败；此时正在运行第4个用例 test_npu_gptq_moe.py，作业随即终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784654

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 pip 卸载/安装依赖后报错“Executing the custom container implementation failed”，属 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784673

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题；此前推理日志正常，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784693

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127744920450) |
| Recommend tests from coverage | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127744920649) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42172946961/job/127745784572) |


## [Run #42165696031](https://github.com/sgl-project/sglang/actions/runs/42165696031)
- **分支**: `weight-cache-vmm-fd-upstream`
- **总耗时**: 63.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42165696031

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377624) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377647) |
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377653) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377655) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377624


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377653


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127721680804) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127721680822) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377411) |
| multimodal-gen-test-1-npu-a3 (1) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377456) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377511) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377600) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377651) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42165696031/job/127722377755) |


## [Run #42163136117](https://github.com/sgl-project/sglang/actions/runs/42163136117)
- **分支**: `vincent/gated-rmsnorm-oot`
- **总耗时**: 24.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42163136117

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 17.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714143904) |
| base-b-test-1-npu-a3 / run (0) | 13.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714143919) |
| base-b-test-2-npu-a3 / run (0) | 13.3min | 环境问题 | 自定义容器执行失败，疑似 runner 容器异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714143990) |
| base-b-test-8-npu-a3 / run (0) | 17.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714144028) |
| base-b-test-4-npu-a3 / run (0) | 7.4min | 环境问题 | 自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714144117) |


- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例本身报错；此时正在执行第4个测试文件 test_npu_gptq_moe.py，作业随即终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714143919

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 server 启动并成功响应 /generate 后，立即报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境故障，并非用例断言失败或代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714143990


- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /v1/chat/completions 返回200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714144117

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127713440746) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127713440761) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42163136117/job/127714143938) |


## [Run #42157284079](https://github.com/sgl-project/sglang/actions/runs/42157284079)
- **分支**: `gdn-spec-decode-xpu`
- **总耗时**: 95.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42157284079

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212876) |
| base-b-test-4-npu-a3 / run (1) | 14.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212948) |
| base-b-test-16-npu-a3 / run (0) | 26.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695213269) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212876

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212948


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127694469237) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127694469254) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212785) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212797) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212840) |
| base-b-test-4-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212864) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157284079/job/127695212942) |


## [Run #42157073849](https://github.com/sgl-project/sglang/actions/runs/42157073849)
- **分支**: `bbuf/env-arch-dispatch`
- **总耗时**: 99.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42157073849

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 18.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127748991393) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示模型分片加载到92%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例或代码问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127748991393

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725972238) |
| base-b-test-16-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725972296) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725972322) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725972460) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725973437) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725973477) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725973561) |
| multimodal-gen-test-4-npu-a3 (1) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725973646) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725973789) |
| multimodal-gen-test-4-npu-a3 (0) | 41.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725974085) |
| base-b-test-4-npu-a3 / run (1) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725974318) |
| base-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127725974337) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127736644900) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127736644932) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127736644942) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42157073849/job/127748991432) |


## [Run #42156761699](https://github.com/sgl-project/sglang/actions/runs/42156761699)
- **分支**: `sagemaker-invocations-dispatch`
- **总耗时**: 67.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42156761699

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 16.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127693673920) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127693673920

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127692798544) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127692798589) |
| base-b-test-2-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127693673930) |
| base-b-test-4-npu-a3 / run (1) | 6.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127693673993) |
| base-b-test-1-npu-a3 / run (0) | 6.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156761699/job/127693674024) |


## [Run #42156645522](https://github.com/sgl-project/sglang/actions/runs/42156645522)
- **分支**: `feat/dsv41-packed-main-kv`
- **总耗时**: 55.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42156645522

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969565) |
| base-b-test-2-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969569) |
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969586) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969614) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969659) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969665) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692425492) |
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692425683) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969499) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156645522/job/127692969581) |


## [Run #42156543094](https://github.com/sgl-project/sglang/actions/runs/42156543094)
- **分支**: `kpham/k31-dcp-decode-runtime`
- **总耗时**: 61.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42156543094

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922118) |
| base-b-test-16-npu-a3 / run (0) | 3.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922176) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922118


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692109078) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692109186) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692921929) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692921990) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922187) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922193) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922205) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156543094/job/127692922226) |


## [Run #42156035915](https://github.com/sgl-project/sglang/actions/runs/42156035915)
- **分支**: `kpham/k31-dcp-decode-runtime`
- **总耗时**: 5.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42156035915

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196695) |
| multimodal-gen-test-4-npu-a3 (1) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196803) |
| base-b-test-1-npu-a3 / run (0) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196806) |
| base-b-test-16-npu-a3 / run (0) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196816) |
| base-b-test-8-npu-a3 / run (0) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196894) |
| base-b-test-2-npu-a3 / run (0) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196908) |
| base-b-test-4-npu-a3 / run (0) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691196916) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127691197038) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127690437950) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42156035915/job/127690437984) |


## [Run #42155947813](https://github.com/sgl-project/sglang/actions/runs/42155947813)
- **分支**: `processor-mm-qwen-vl`
- **总耗时**: 63.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42155947813

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974760) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974789) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974760

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974789

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690142225) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690142384) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974612) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974653) |
| multimodal-gen-test-4-npu-a3 (0) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974696) |
| multimodal-gen-test-1-npu-a3 (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974705) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974708) |
| base-b-test-4-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974752) |
| base-b-test-1-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974883) |
| base-b-test-16-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155947813/job/127690974905) |


## [Run #42155370408](https://github.com/sgl-project/sglang/actions/runs/42155370408)
- **分支**: `lossless-gdn-tuple-verify`
- **总耗时**: 60.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42155370408

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188620) |
| base-b-test-16-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188704) |
| base-b-test-1-npu-a3 / run (0) | 6.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188707) |



- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188707

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127688318692) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127688318914) |
| multimodal-gen-test-1-npu-a3 (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188419) |
| multimodal-gen-test-4-npu-a3 (1) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188506) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188573) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188590) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188640) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188643) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155370408/job/127689188723) |


## [Run #42155048261](https://github.com/sgl-project/sglang/actions/runs/42155048261)
- **分支**: `ernie-55-flash-day0`
- **总耗时**: 50.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42155048261

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111329) |
| base-b-test-1-npu-a3 / run (0) | 8.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111333) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111344) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111443) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111329

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111333



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127687232828) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127687232887) |
| multimodal-gen-test-1-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111127) |
| multimodal-gen-test-1-npu-a3 (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111134) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111177) |
| multimodal-gen-test-4-npu-a3 (0) | 34.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111243) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111279) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42155048261/job/127688111294) |


## [Run #42153930501](https://github.com/sgl-project/sglang/actions/runs/42153930501)
- **分支**: `oss-sync-94d8b244ad`
- **总耗时**: 44.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42153930501

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500292) |
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500295) |


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500295

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127683603425) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127683603445) |
| multimodal-gen-test-4-npu-a3 (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500088) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500228) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500371) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500383) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684500395) |
| base-b-test-1-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153930501/job/127684501502) |


## [Run #42153614046](https://github.com/sgl-project/sglang/actions/runs/42153614046)
- **分支**: `fix/json-schema-depth-explosion`
- **总耗时**: 11.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42153614046

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42153614046/job/127683250419) |
| base-b-test-4-npu-a3 / run (1) | 9.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42153614046/job/127683250469) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153614046/job/127682600183) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153614046/job/127682600207) |


## [Run #42153483517](https://github.com/sgl-project/sglang/actions/runs/42153483517)
- **分支**: `feature/leixin/qwen3-blockfp8-quant-fusion`
- **总耗时**: 62.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42153483517

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690408) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690530) |
| base-b-test-1-npu-a3 / run (0) | 18.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690581) |


- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690530

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_tp1_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690581

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127699874287) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127699874321) |
| multimodal-gen-test-1-npu-a3 (1) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690219) |
| multimodal-gen-test-4-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690271) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690371) |
| multimodal-gen-test-1-npu-a3 (0) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690378) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690470) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690591) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153483517/job/127700690622) |


## [Run #42153160933](https://github.com/sgl-project/sglang/actions/runs/42153160933)
- **分支**: `lsyin/srt-utils-split-common`
- **总耗时**: 48.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42153160933

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 16.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164471) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164471

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127681469277) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127681469341) |
| multimodal-gen-test-4-npu-a3 (1) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164122) |
| multimodal-gen-test-4-npu-a3 (0) | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164145) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164165) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164193) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164214) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164295) |
| base-b-test-16-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164307) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164346) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42153160933/job/127682164390) |


## [Run #42152325582](https://github.com/sgl-project/sglang/actions/runs/42152325582)
- **分支**: `lsyin/srt-utils-split-common`
- **总耗时**: 9.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42152325582

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 2.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260643) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260652) |
| base-b-test-8-npu-a3 / run (0) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260686) |
| multimodal-gen-test-4-npu-a3 (1) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260691) |
| base-b-test-16-npu-a3 / run (0) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260725) |
| base-b-test-1-npu-a3 / run (0) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260735) |
| base-b-test-2-npu-a3 / run (0) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260746) |
| multimodal-gen-test-1-npu-a3 (1) | 1.2min | 环境问题 | diffusion-failures 目录不存在，未生成任何失败产物，疑似测试未实际执行或产物路径配置错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260748) |
| base-b-test-4-npu-a3 / run (0) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260789) |
| base-b-test-4-npu-a3 / run (1) | 5.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260838) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260643







- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，无 Traceback 或 RuntimeError 信息，作业在约1分钟内结束，推测测试用例未真正运行或产物目录未生成，需检查测试脚本执行与产物路径配置。
  链接: https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127679260748



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127678395601) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42152325582/job/127678395648) |


## [Run #42151442828](https://github.com/sgl-project/sglang/actions/runs/42151442828)
- **分支**: `litetopk-prefill`
- **总耗时**: 7.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42151442828

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 3.3min | 环境问题 | 未找到 diffusion-failures 目录，测试产物缺失，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211724) |
| multimodal-gen-test-4-npu-a3 (0) | 2.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211775) |
| multimodal-gen-test-1-npu-a3 (1) | 2.2min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略的中间日志确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211858) |
| multimodal-gen-test-1-npu-a3 (0) | 2.2min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211884) |
| base-b-test-4-npu-a3 / run (0) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211949) |
| base-b-test-4-npu-a3 / run (1) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211988) |
| base-b-test-1-npu-a3 / run (0) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676212004) |
| base-b-test-2-npu-a3 / run (0) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676212009) |
| base-b-test-8-npu-a3 / run (0) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676212020) |
| base-b-test-16-npu-a3 / run (0) | 4.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676212131) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/'，说明测试未生成失败产物目录，可能 setUpClass 阶段 server 启动失败或测试未正常执行，导致上传产物步骤无文件可传。
  链接: https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211724

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致用例error而非正常执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211775

- **multimodal-gen-test-1-npu-a3 (1)**: 日志可见部分只有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback/RuntimeError。退出码 5 提示 unittest 有 errors，可能为 setUpClass 中 server 启动失败，但关键错误在省略段中，无法确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211858

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 Node.js 弃用警告，最后提示未找到 diffusion-failures/ 路径，无 artifact 上传。缺少 unittest 报错或退出码 5 的 Traceback，无法确认具体失败点，疑似测试脚本未产出结果或环境/路径配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127676211884







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127675524873) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42151442828/job/127675525277) |


## [Run #42150682537](https://github.com/sgl-project/sglang/actions/runs/42150682537)
- **分支**: `jacob/glm53-flash-moe-router-kda`
- **总耗时**: 9.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42150682537

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 3.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813039) |
| multimodal-gen-test-1-npu-a3 (0) | 2.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813144) |
| multimodal-gen-test-4-npu-a3 (0) | 2.3min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业本身未报失败原因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813187) |
| base-b-test-2-npu-a3 / run (0) | 5.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813216) |
| base-b-test-16-npu-a3 / run (0) | 5.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813277) |
| multimodal-gen-test-1-npu-a3 (1) | 2.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813329) |
| base-b-test-1-npu-a3 / run (0) | 5.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813383) |
| base-b-test-4-npu-a3 / run (0) | 5.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813421) |
| base-b-test-4-npu-a3 / run (1) | 5.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813429) |
| base-b-test-8-npu-a3 / run (0) | 5.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813442) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中未见具体 Traceback，但退出码5表明 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。另 upload-artifact 未找到 diffusion-failures/ 目录，无产物上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813039

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示未找到 diffusion-failures/ 目录，无产物上传；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813144

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅含 Node 弃用警告和 artifact 路径缺失提示，无 Traceback/RuntimeError，无法定位用例失败；需查看被省略的中间日志确认退出码 5 的真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813187



- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127812813329





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127811890767) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150682537/job/127811890872) |


## [Run #42150345686](https://github.com/sgl-project/sglang/actions/runs/42150345686)
- **分支**: `feat/ling3-pub-parser`
- **总耗时**: 41.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42150345686

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509331) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509331

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127671937507) |
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127671937596) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672508975) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509110) |
| base-b-test-8-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509256) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509324) |
| base-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509393) |
| base-b-test-16-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509397) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150345686/job/127672509442) |


## [Run #42150018137](https://github.com/sgl-project/sglang/actions/runs/42150018137)
- **分支**: `pd-spec-kv-layout`
- **总耗时**: 63.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42150018137

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127838150021) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127838150021

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-16-npu-a3 / run (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823469938) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823470057) |
| base-b-test-4-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823470146) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823470156) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823470175) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823470977) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823472053) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823472668) |
| base-b-test-1-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823472715) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127823472844) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127838149956) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42150018137/job/127838150044) |


## [Run #42149874285](https://github.com/sgl-project/sglang/actions/runs/42149874285)
- **分支**: `perf/input-embeds-one-union-member`
- **总耗时**: 36.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42149874285

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122202) |
| base-b-test-4-npu-a3 / run (1) | 16.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122253) |
| base-b-test-1-npu-a3 / run (0) | 5.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122431) |


- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122253

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122431

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127670367432) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127670367590) |
| multimodal-gen-test-4-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671121909) |
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671121915) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122081) |
| multimodal-gen-test-1-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122103) |
| base-b-test-2-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122308) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122324) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42149874285/job/127671122374) |


## [Run #42147955932](https://github.com/sgl-project/sglang/actions/runs/42147955932)
- **分支**: `bbuf/env-arch-dispatch`
- **总耗时**: 87.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42147955932

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 3.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127692646725) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 3.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127692646739) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127664333930) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127664334048) |
| multimodal-gen-test-1-npu-a3 (1) | 37.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135370) |
| multimodal-gen-test-4-npu-a3 (1) | 38.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135479) |
| multimodal-gen-test-4-npu-a3 (0) | 35.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135543) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135584) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135614) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135673) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135676) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135695) |
| multimodal-gen-test-1-npu-a3 (0) | 34.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135741) |
| base-b-test-16-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127665135839) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127676208399) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127676208450) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42147955932/job/127676208476) |


## [Run #42146398132](https://github.com/sgl-project/sglang/actions/runs/42146398132)
- **分支**: `bbuf/env-arch-dispatch`
- **总耗时**: 15.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42146398132

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659815773) |
| multimodal-gen-test-4-npu-a3 (0) | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659815789) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659815842) |
| multimodal-gen-test-1-npu-a3 (0) | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659815850) |
| base-b-test-2-npu-a3 / run (0) | 9.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659815963) |
| base-b-test-1-npu-a3 / run (0) | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816077) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816129) |
| base-b-test-4-npu-a3 / run (1) | 8.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在启动阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816194) |
| base-b-test-4-npu-a3 / run (0) | 9.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816292) |





- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载正常完成后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659815963



- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，提示联系自托管 runner 管理员，说明容器运行时/镜像启动异常，并非用例代码或精度问题；此前仅有 torch_npu 的警告，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816194

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 tokenizer 初始化后报错“Executing the custom container implementation failed”，属 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816292

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127658949411) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127658949503) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146398132/job/127659816096) |


## [Run #42146000072](https://github.com/sgl-project/sglang/actions/runs/42146000072)
- **分支**: `k31/linker-pcp-l3`
- **总耗时**: 27.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42146000072

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | 环境问题 | multimodal-gen 测试作业失败，未生成 diffusion-failures 产物，疑似 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273882) |
| base-b-test-2-npu-a3 / run (0) | 16.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273955) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273994) |
| base-b-test-1-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658274023) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | 环境问题 | 自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658274076) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见 upload-artifact 提示未找到 diffusion-failures/ 目录，说明测试用例未正常产出失败样本；结合退出码 5（unittest errors），最可能是 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL），属环境问题，需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273882

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 server 已正常启动并响应请求，随后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273955

- **base-b-test-16-npu-a3 / run (0)**: 日志中 test_npu_speculative_moe_a2a_backend.py 显示 PASSED，Test Summary: 1/1 passed，退出码正常，仅存在 Node.js 弃用警告，未见任何错误或失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273994

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658274023

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658274076

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127657631455) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127657631457) |
| multimodal-gen-test-4-npu-a3 (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273785) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273909) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42146000072/job/127658273983) |


## [Run #42145343246](https://github.com/sgl-project/sglang/actions/runs/42145343246)
- **分支**: `lsyin/srt-utils-owners`
- **总耗时**: 17.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42145343246

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270100) |
| multimodal-gen-test-1-npu-a3 (1) | 14.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270145) |
| multimodal-gen-test-4-npu-a3 (0) | 14.3min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270227) |
| multimodal-gen-test-4-npu-a3 (1) | 14.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270240) |
| base-b-test-1-npu-a3 / run (0) | 14.3min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270358) |
| base-b-test-2-npu-a3 / run (0) | 13.3min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270359) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270387) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270424) |
| base-b-test-4-npu-a3 / run (0) | 14.3min | 环境问题 | 自定义容器执行失败，作业在容器启动/运行阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270469) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约14分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270100

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明用例未正常产出结果；退出码5对应 unittest errors，最常见为 setUpClass 中 server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270145

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成该目录，可能用例未执行或提前失败；日志中未见具体 Traceback，需查看被省略的中间日志确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270227

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业约14分钟后结束，退出码5表示unittest有errors，常见于setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。日志中未见具体Traceback，且diffusion-failures目录无文件，需查看中间省略部分确认真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270240

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属 self-hosted runner 容器实现故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270358

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器环境异常，并非用例代码或精度问题；server 刚启动即中断，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270359

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270387


- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属自托管 runner 容器环境问题；此前仅有 falcon_mamba 导入告警（被忽略），非用例失败。需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270469

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127655518124) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127655518199) |
| base-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42145343246/job/127656270398) |


## [Run #42142008951](https://github.com/sgl-project/sglang/actions/runs/42142008951)
- **分支**: `oss-sync-fa6ceed880`
- **总耗时**: 56.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42142008951

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127655059481) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127655059481

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127644487105) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127644487354) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645393965) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645393992) |
| base-b-test-2-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645394057) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645394090) |
| base-b-test-4-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645394124) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645394225) |
| base-b-test-16-npu-a3 / run (0) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645394233) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127645394247) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127655059456) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 26.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42142008951/job/127655059461) |


## [Run #42139587595](https://github.com/sgl-project/sglang/actions/runs/42139587595)
- **分支**: `oss-sync-5f33eae5cc`
- **总耗时**: 44.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42139587595

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 20.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243467) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243492) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试请求均返回 200 OK，随后报错 'Executing the custom container implementation failed'，属 runner/容器基础设施故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243467

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243492

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127636442180) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127636442187) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251783) |
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251821) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251830) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251892) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251950) |
| base-b-test-4-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251955) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251965) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251974) |
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251990) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127637251991) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42139587595/job/127645243517) |


## [Run #42137432746](https://github.com/sgl-project/sglang/actions/runs/42137432746)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 48.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42137432746

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 19.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127640220517) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127640220517

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629197123) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629197256) |
| multimodal-gen-test-4-npu-a3 (1) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999081) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999102) |
| multimodal-gen-test-1-npu-a3 (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999111) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999137) |
| base-b-test-2-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999172) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999177) |
| base-b-test-4-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999190) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999199) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999235) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127629999283) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127640220454) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42137432746/job/127640220582) |


## [Run #42136394141](https://github.com/sgl-project/sglang/actions/runs/42136394141)
- **分支**: `kpham/k31-dcp-decode-runtime`
- **总耗时**: 34.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42136394141

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 12.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684368) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | 其他 | 日志显示测试全部通过，作业本身无失败迹象，失败可能发生在日志未覆盖的环节。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684433) |
| base-b-test-1-npu-a3 / run (0) | 12.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684485) |
| base-b-test-2-npu-a3 / run (0) | 5.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684519) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业约12分钟后结束，未找到diffusion-failures/目录产物，无Traceback细节；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684368

- **base-b-test-8-npu-a3 / run (0)**: 可见日志中 test_npu_eplb_min_rebalancing_utilization_threshold.py 通过（1/1 passed），随后正常执行 Post job cleanup，未见 Traceback、RuntimeError 或退出码 5 等错误，无法从现有日志定位失败原因，需查看被省略的中间日志或作业最终状态。
  链接: https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684433

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 test_npu_gptq_moe.py 的 TestAscendGPTQMoEInt4.test_a_gsm8k 执行期间，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684485

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684519

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127625690331) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127625690416) |
| multimodal-gen-test-4-npu-a3 (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684349) |
| base-b-test-16-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684439) |
| base-b-test-4-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684510) |
| base-b-test-4-npu-a3 / run (1) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136394141/job/127626684548) |


## [Run #42136249293](https://github.com/sgl-project/sglang/actions/runs/42136249293)
- **分支**: `hicache/scheduler-thread-alloc`
- **总耗时**: 34.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42136249293

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229559) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229559

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127625217478) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127625217491) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229215) |
| base-b-test-16-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229438) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229446) |
| base-b-test-1-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229542) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229561) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229574) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136249293/job/127626229651) |


## [Run #42136228226](https://github.com/sgl-project/sglang/actions/runs/42136228226)
- **分支**: `hicache/scheduler-thread-agreement`
- **总耗时**: 40.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42136228226

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312036) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312055) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312066) |
| base-b-test-16-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312084) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312173) |





- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312173

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127627229754) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127627229794) |
| multimodal-gen-test-4-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628311909) |
| multimodal-gen-test-4-npu-a3 (0) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628311924) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628311972) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312048) |
| base-b-test-2-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42136228226/job/127628312169) |


## [Run #42135808011](https://github.com/sgl-project/sglang/actions/runs/42135808011)
- **分支**: `oss-sync-65c40d1f0e`
- **总耗时**: 84.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42135808011

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 11.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127651867944) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 11.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127651868080) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，并非用例断言失败；此前 generate 请求均返回 200，随后作业被中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127651867944

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例断言失败；此前 perf 测试仍在正常输出吞吐日志，随后容器执行失败导致作业终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127651868080

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127625791831) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127625792163) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685023) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685041) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685057) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685070) |
| base-b-test-4-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685071) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685231) |
| base-b-test-2-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685233) |
| base-b-test-1-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127626685274) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127640649104) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127640649162) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 29.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42135808011/job/127640649197) |


## [Run #42134774902](https://github.com/sgl-project/sglang/actions/runs/42134774902)
- **分支**: `hicache/scheduler-thread-alloc`
- **总耗时**: 12.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42134774902

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143584) |
| multimodal-gen-test-4-npu-a3 (0) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143723) |
| base-b-test-8-npu-a3 / run (0) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143784) |
| base-b-test-1-npu-a3 / run (0) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143789) |
| base-b-test-4-npu-a3 / run (1) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143812) |
| base-b-test-4-npu-a3 / run (0) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143879) |
| base-b-test-2-npu-a3 / run (0) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143894) |
| base-b-test-16-npu-a3 / run (0) | 9.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127621143921) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127620207952) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134774902/job/127620208007) |


## [Run #42134764634](https://github.com/sgl-project/sglang/actions/runs/42134764634)
- **分支**: `hicache/scheduler-thread-transfers`
- **总耗时**: 12.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42134764634

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 9.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134764634/job/127620926147) |
| base-b-test-4-npu-a3 / run (0) | 9.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134764634/job/127620926195) |
| base-b-test-2-npu-a3 / run (0) | 9.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134764634/job/127620926331) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134764634/job/127620926539) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134764634/job/127620150561) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134764634/job/127620150669) |


## [Run #42134760422](https://github.com/sgl-project/sglang/actions/runs/42134760422)
- **分支**: `hicache/scheduler-thread-agreement`
- **总耗时**: 17.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42134760422

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 5.0min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124953) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124955) |
| base-b-test-1-npu-a3 / run (0) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124956) |
| multimodal-gen-test-1-npu-a3 (0) | 5.7min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124966) |
| base-b-test-4-npu-a3 / run (0) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125033) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125049) |
| base-b-test-2-npu-a3 / run (0) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125059) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125061) |
| multimodal-gen-test-1-npu-a3 (1) | 5.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125070) |
| base-b-test-16-npu-a3 / run (0) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125085) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示上传产物时未找到 diffusion-failures/ 路径，说明测试用例未正常产出失败样本；结合退出码 5 的常见原因，推测 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124953

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约6分钟结束，无明确Traceback。退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124955


- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约6分钟结束，无明确Traceback。退出码5表明unittest有errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621124966





- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约6分钟结束，退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127621125070


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127620164740) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134760422/job/127620165782) |


## [Run #42134506049](https://github.com/sgl-project/sglang/actions/runs/42134506049)
- **分支**: `lsyin/srt-utils-cleanup`
- **总耗时**: 29.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42134506049

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | 环境问题 | 作业在容器内执行阶段失败，未生成 diffusion-failures 产物，且从 pod 复制 _temp 失败，疑似 NPU 容器/服务启动异常。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419324) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | 环境问题 | 作业失败，未找到 diffusion-failures 目录产物，且从 pod 复制 _temp 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419382) |
| multimodal-gen-test-4-npu-a3 (0) | 18.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419428) |
| base-b-test-4-npu-a3 / run (1) | 9.4min | 其他 | 日志显示全部用例通过，作业本身无失败迹象 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419797) |
| base-b-test-2-npu-a3 / run (0) | 12.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419848) |
| base-b-test-16-npu-a3 / run (0) | 10.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片过程中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419856) |
| base-b-test-4-npu-a3 / run (0) | 12.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419886) |
| base-b-test-1-npu-a3 / run (0) | 12.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620421547) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 路径，随后警告 Failed to copy _temp from pod，说明容器内测试未正常产出结果，可能 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419324

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/' 及 'Failed to copy _temp from pod'，说明测试产物未生成或 pod 文件复制异常，疑似 setUpClass 阶段 server 启动失败或 pod 环境问题，导致用例报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419382

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业约18分钟后结束，退出码5表示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。日志中未找到diffusion-failures目录，无产物上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419428

- **base-b-test-4-npu-a3 / run (1)**: 日志中 Test Summary 为 2/2 passed，两个 NPU 用例均 PASSED，耗时正常，仅出现 Node.js 弃用警告，未发现 Traceback 或非零退出码，失败原因需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419797

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419848

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载到47%时出现“Executing the custom container implementation failed”，属于自托管 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419856

- **base-b-test-4-npu-a3 / run (0)**: 日志显示服务端推理正常进行中，随后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码或性能问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419886

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在模型服务启动后不久，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620421547

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127619524012) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127619524113) |
| multimodal-gen-test-1-npu-a3 (1) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620419392) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42134506049/job/127620420100) |


## [Run #42133526452](https://github.com/sgl-project/sglang/actions/runs/42133526452)
- **分支**: `bench-serving-per-run-accept-length`
- **总耗时**: 45.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42133526452

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 14.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976715) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976715

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616024949) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616024988) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976320) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976409) |
| base-b-test-16-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976466) |
| base-b-test-4-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976502) |
| base-b-test-1-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42133526452/job/127616976539) |


## [Run #42132343178](https://github.com/sgl-project/sglang/actions/runs/42132343178)
- **分支**: `hejian/plugin-weight-update`
- **总耗时**: 36.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42132343178

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 15.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670220) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670220

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127611968026) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127611968113) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612669976) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670031) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670068) |
| base-b-test-1-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670164) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670214) |
| base-b-test-16-npu-a3 / run (0) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670237) |
| base-b-test-2-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42132343178/job/127612670261) |


## [Run #42129499669](https://github.com/sgl-project/sglang/actions/runs/42129499669)
- **分支**: `oss-sync-5f33eae5cc`
- **总耗时**: 68.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42129499669

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419605) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_glm52.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419605

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127602440166) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127602440291) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419246) |
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419302) |
| multimodal-gen-test-1-npu-a3 (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419324) |
| base-b-test-1-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419398) |
| base-b-test-16-npu-a3 / run (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419443) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419451) |
| multimodal-gen-test-4-npu-a3 (1) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419510) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419589) |
| base-b-test-4-npu-a3 / run (1) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42129499669/job/127603419708) |


## [Run #42126617967](https://github.com/sgl-project/sglang/actions/runs/42126617967)
- **分支**: `oss-sync-219fe11113`
- **总耗时**: 85.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42126617967

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 28.5min | 环境问题 | 作业在运行测试前失败，未找到 diffusion-failures 目录且无法从 pod 复制 _temp，疑似 pod/容器环境异常导致测试未正常执行。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376146) |
| multimodal-gen-test-1-npu-a3 (0) | 30.3min | 环境问题 | 作业在容器内执行阶段失败，未生成 diffusion-failures 产物，疑似 sglang server 启动失败导致用例报错。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376290) |
| multimodal-gen-test-1-npu-a3 (1) | 30.6min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376347) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/' 及 'Failed to copy _temp from pod'，说明测试产物未生成、pod 内文件复制失败，作业在清理阶段结束，未见具体用例 Traceback，判断为运行环境/pod 异常而非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376146

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见上传产物路径 diffusion-failures/ 无文件、复制 _temp 失败等收尾告警；结合退出码 5 的约定，最可能是 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376290

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试脚本未产出失败用例文件；结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376347

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127592519515) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127592519527) |
| multimodal-gen-test-4-npu-a3 (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376153) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376273) |
| base-b-test-1-npu-a3 / run (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376333) |
| base-b-test-4-npu-a3 / run (1) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376390) |
| base-b-test-2-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127593376437) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42126617967/job/127606698402) |


## [Run #42125781320](https://github.com/sgl-project/sglang/actions/runs/42125781320)
- **分支**: `oss-sync-65c40d1f0e`
- **总耗时**: 85.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42125781320

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127605754112) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型权重分片加载到约72%时，报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境异常，并非用例断言失败或代码错误，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127605754112

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127589690591) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127589690604) |
| multimodal-gen-test-4-npu-a3 (0) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590641816) |
| multimodal-gen-test-4-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590641874) |
| base-b-test-8-npu-a3 / run (0) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590642028) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590642158) |
| base-b-test-4-npu-a3 / run (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590642204) |
| base-b-test-1-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590642239) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590642293) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127590642363) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127605754100) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125781320/job/127605754220) |


## [Run #42125324458](https://github.com/sgl-project/sglang/actions/runs/42125324458)
- **分支**: `oss-sync-9f5a63e975`
- **总耗时**: 14.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42125324458

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 12.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42125324458/job/127589062540) |
| base-b-test-4-npu-a3 / run (0) | 12.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42125324458/job/127589062602) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125324458/job/127588105474) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125324458/job/127588105558) |


## [Run #42125241773](https://github.com/sgl-project/sglang/actions/runs/42125241773)
- **分支**: `oss-sync-700891a42b`
- **总耗时**: 80.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42125241773

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 11.6min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127600691064) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志中 Test Summary: 1/1 passed，用例耗时465s正常完成，退出码为0；末尾仅有 Node.js 20 弃用警告，属非致命提示，未发现 Traceback 或错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127600691064

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127587818886) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127587818996) |
| base-b-test-1-npu-a3 / run (0) | 6.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127588993254) |
| base-b-test-4-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127588993324) |
| base-b-test-4-npu-a3 / run (1) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127588993346) |
| base-b-test-2-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125241773/job/127588993507) |


## [Run #42125015575](https://github.com/sgl-project/sglang/actions/runs/42125015575)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 78.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42125015575

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127604468600) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127604468600

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127587293399) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127587293454) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281365) |
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281448) |
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281453) |
| base-b-test-4-npu-a3 / run (1) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281521) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281580) |
| multimodal-gen-test-4-npu-a3 (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281598) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281661) |
| base-b-test-4-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281693) |
| base-b-test-1-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281694) |
| base-b-test-2-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127588281760) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127604462201) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42125015575/job/127604462205) |


## [Run #42124851659](https://github.com/sgl-project/sglang/actions/runs/42124851659)
- **分支**: `lsyin/ci-warning-noise`
- **总耗时**: 20.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42124851659

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 11.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012526) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012594) |
| base-b-test-1-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012683) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012734) |
| base-b-test-16-npu-a3 / run (0) | 6.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012742) |
| base-b-test-8-npu-a3 / run (0) | 11.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012795) |
| base-b-test-4-npu-a3 / run (1) | 7.3min | 环境问题 | 容器执行失败，SMEM 连接断开导致进程被终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012815) |
| base-b-test-2-npu-a3 / run (0) | 6.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012869) |



- **base-b-test-1-npu-a3 / run (0)**: 日志显示 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员。失败发生在 test_npu_autoround_dense.py 的 test_a_gsm8k 开始后约12秒，并非用例断言失败或超时，属于 runner/容器环境异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012683

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 VLM 用例已通过（POST 200 OK），随后报错 'Executing the custom container implementation failed'，属 self-hosted runner 容器实现故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012734

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码错误；随后仅执行清理，未进入测试逻辑。
  链接: https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012742


- **base-b-test-4-npu-a3 / run (1)**: 日志显示 SMEM 多次 link broken 且重连失败（ReConnectAfterBroken result: -1），随后 kill_process_tree 关闭 server，最终报错“Executing the custom container implementation failed”，属自托管 runner 容器/网络环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012815

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明容器运行时异常退出，并非用例断言失败；需联系 runner 管理员排查容器/节点环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127588012869

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127586934908) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124851659/job/127586935043) |


## [Run #42124364385](https://github.com/sgl-project/sglang/actions/runs/42124364385)
- **分支**: `lsyin/sched-pr23`
- **总耗时**: 14.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42124364385

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332156) |
| base-b-test-2-npu-a3 / run (0) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332172) |
| base-b-test-8-npu-a3 / run (0) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332175) |
| base-b-test-1-npu-a3 / run (0) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332182) |
| multimodal-gen-test-4-npu-a3 (0) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332195) |
| base-b-test-4-npu-a3 / run (1) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332224) |
| base-b-test-4-npu-a3 / run (0) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332252) |
| base-b-test-16-npu-a3 / run (0) | 6.3min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127588332331) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127587188113) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124364385/job/127587188290) |


## [Run #42124206422](https://github.com/sgl-project/sglang/actions/runs/42124206422)
- **分支**: `oss-sync-3d772da99f`
- **总耗时**: 77.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42124206422

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 8.1min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315622) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 235 秒后 FAILED (errors=1)，2 个用例 0 通过，进程以退出码 1 结束，导致作业失败；具体错误需查看被省略的 Traceback，常见为 setUpClass 阶段 server 启动失败。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315622

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127584267949) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127584267951) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315189) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315306) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315423) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315451) |
| multimodal-gen-test-4-npu-a3 (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315474) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315589) |
| base-b-test-16-npu-a3 / run (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315666) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315709) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42124206422/job/127585315746) |


## [Run #42123925351](https://github.com/sgl-project/sglang/actions/runs/42123925351)
- **分支**: `oss-sync-fa6ceed880`
- **总耗时**: 58.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42123925351

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150485) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150542) |
| base-b-test-4-npu-a3 / run (1) | 2.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150586) |
| base-b-test-1-npu-a3 / run (0) | 6.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150620) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150630) |
| base-b-test-2-npu-a3 / run (0) | 6.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150668) |




- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150620


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150668

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127583340040) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127583340109) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150452) |
| multimodal-gen-test-4-npu-a3 (0) | 7.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123925351/job/127584150524) |


## [Run #42123605224](https://github.com/sgl-project/sglang/actions/runs/42123605224)
- **分支**: `oss-sync-71332a38e2`
- **总耗时**: 26.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42123605224

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 14.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127583229152) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127583229152

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127582204595) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127582204611) |
| base-b-test-4-npu-a3 / run (1) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127583229018) |
| base-b-test-1-npu-a3 / run (0) | 6.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127583229141) |
| base-b-test-2-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123605224/job/127583229454) |


## [Run #42123287188](https://github.com/sgl-project/sglang/actions/runs/42123287188)
- **分支**: `m31-amd/integration`
- **总耗时**: 5.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42123287188

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481557) |
| multimodal-gen-test-1-npu-a3 (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481627) |
| multimodal-gen-test-4-npu-a3 (1) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481641) |
| base-b-test-4-npu-a3 / run (1) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481745) |
| base-b-test-4-npu-a3 / run (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481754) |
| multimodal-gen-test-4-npu-a3 (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481766) |
| base-b-test-1-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481787) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481808) |
| base-b-test-2-npu-a3 / run (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481811) |
| base-b-test-8-npu-a3 / run (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481879) |







- **base-b-test-1-npu-a3 / run (0)**: 日志显示在解包 deb 包时出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127582481787




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127581338273) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123287188/job/127581338489) |


## [Run #42123117918](https://github.com/sgl-project/sglang/actions/runs/42123117918)
- **分支**: `lsyin/ci-warning-noise`
- **总耗时**: 13.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42123117918

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 10.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428153) |
| multimodal-gen-test-4-npu-a3 (1) | 10.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428276) |
| base-b-test-16-npu-a3 / run (0) | 7.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428331) |
| base-b-test-2-npu-a3 / run (0) | 8.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428537) |
| base-b-test-1-npu-a3 / run (0) | 8.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428621) |
| base-b-test-4-npu-a3 / run (1) | 7.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428635) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428666) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428713) |



- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载到25%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428331

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在加载权重阶段，属于 runner/容器环境故障，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428537

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在第3个用例 test_npu_autoround_moe.py 启动后约11秒，属 runner/容器基础设施异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428621

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 Capturing batches 阶段后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428635

- **base-b-test-8-npu-a3 / run (0)**: 日志显示模型权重加载过程中出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428666

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境故障，非用例代码问题；此前 /generate 请求均返回 200。
  链接: https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127581428713

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127580574965) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42123117918/job/127580575072) |


## [Run #42122889541](https://github.com/sgl-project/sglang/actions/runs/42122889541)
- **分支**: `flashinfer-0.7.3-moe-ep`
- **总耗时**: 50.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42122889541

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 12.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521314) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521463) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_speculative_multi_npu.py, npu_speculative_multi_npu.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521314

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_tp1_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521463

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127579717468) |
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127579717472) |
| multimodal-gen-test-4-npu-a3 (0) | 28.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521073) |
| multimodal-gen-test-1-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521133) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521199) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521302) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521359) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521409) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521471) |
| base-b-test-16-npu-a3 / run (0) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42122889541/job/127580521489) |


## [Run #42121134606](https://github.com/sgl-project/sglang/actions/runs/42121134606)
- **分支**: `lsyin/fix-draft-loc-contiguous`
- **总耗时**: 45.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42121134606

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 7.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127587160897) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 11.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127587160965) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 11.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127587161014) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明是自托管 runner 的容器运行时故障，而非用例或代码问题；此前 chat/completions 请求均返回 200，服务运行正常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127587160897



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127573680990) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127573681247) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934616) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934673) |
| base-b-test-4-npu-a3 / run (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934728) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934767) |
| base-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934770) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934795) |
| base-b-test-16-npu-a3 / run (0) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574934923) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42121134606/job/127574935088) |


## [Run #42119857635](https://github.com/sgl-project/sglang/actions/runs/42119857635)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 29.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42119857635

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 18.3min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541120) |
| multimodal-gen-test-4-npu-a3 (0) | 17.3min | 环境问题 | multimodal-gen 测试作业失败，未生成 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541257) |
| base-b-test-1-npu-a3 / run (0) | 18.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541297) |
| base-b-test-16-npu-a3 / run (0) | 18.3min | 其他 | 日志显示测试全部通过，作业本身无失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541370) |
| base-b-test-2-npu-a3 / run (0) | 17.3min | 环境问题 | 自定义容器执行失败，疑似 NPU 容器运行时异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541398) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541525) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成该目录（可能用例未执行或提前失败），导致 upload-artifact 步骤无产物可传而失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541120

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，仅见 upload-artifact 提示未找到 diffusion-failures/ 目录，无 Traceback 可见。结合退出码 5 的常见原因，推测为 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 unittest 出现 errors，需查看省略段确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541257

- **base-b-test-1-npu-a3 / run (0)**: 日志显示测试正常执行中（Eagle3 并发请求测试），随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541297

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾显示 Test Summary: 1/1 passed，唯一用例 test_npu_speculative_moe_a2a_backend.py 通过（耗时845s），随后正常执行 Post job cleanup，未见 Traceback 或非零退出码。若作业被判失败，可能是后续清理/上报步骤或外部状态问题，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541370

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 server 启动后仅数秒即报 'Executing the custom container implementation failed'，属 runner 容器层错误，非用例断言失败；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541398

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例断言失败；此前推理服务仍在正常输出 prefill/decode 日志，随后容器执行异常终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541525

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127569292325) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127569292391) |
| multimodal-gen-test-1-npu-a3 (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570540939) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541101) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541270) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119857635/job/127570541434) |


## [Run #42119853992](https://github.com/sgl-project/sglang/actions/runs/42119853992)
- **分支**: `m31-amd/aiter-tuned-tables`
- **总耗时**: 24.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42119853992

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 20.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282494) |
| base-b-test-1-npu-a3 / run (0) | 20.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282629) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282494

- **base-b-test-1-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明容器运行时（k8s runner）异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282629

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127569312279) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127569312453) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282173) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282316) |
| base-b-test-16-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282417) |
| base-b-test-4-npu-a3 / run (1) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282448) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282510) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119853992/job/127570282885) |


## [Run #42119850375](https://github.com/sgl-project/sglang/actions/runs/42119850375)
- **分支**: `m31-amd/integration`
- **总耗时**: 24.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42119850375

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 20.4min | 环境问题 | 日志中未见明确错误，但上传产物路径 diffusion-failures/ 不存在，作业以非零码退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382246) |
| base-b-test-2-npu-a3 / run (0) | 19.3min | 其他 | 日志中所有用例均通过，作业正常结束，未见失败错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382326) |
| base-b-test-4-npu-a3 / run (1) | 16.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382424) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382470) |
| base-b-test-1-npu-a3 / run (0) | 18.7min | 其他 | 日志中所有测试用例均通过，作业正常完成清理，未见失败错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570383464) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，仅见 'No files were found with the provided path: diffusion-failures/'，说明测试失败后未生成失败产物目录；结合退出码5，推测 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），需查看完整日志中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382246

- **base-b-test-2-npu-a3 / run (0)**: 日志显示各测试文件 passed=true，TIMINGS END 后进入 Post job cleanup，无 Traceback/RuntimeError/退出码 5 等失败信息，失败原因无法从所给日志判定，可能为上游步骤或日志截断所致。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382326

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382424

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382470

- **base-b-test-1-npu-a3 / run (0)**: 日志显示各测试文件 passed 均为 true，TIMINGS 正常结束，随后执行 Post job cleanup，无 Traceback 或非零退出码，失败原因无法从所给日志判定，可能为日志截断或上游判定逻辑问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570383464

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127569263033) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127569263242) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382031) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382069) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382159) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382229) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42119850375/job/127570382439) |


## [Run #42116222387](https://github.com/sgl-project/sglang/actions/runs/42116222387)
- **分支**: `lsyin/sched-pr23`
- **总耗时**: 61.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42116222387

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127570925730) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 14.4min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127570925889) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明自托管 runner 的容器实现异常，导致作业在 decode 阶段被中断，并非用例本身的精度或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127570925730

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例本身的精度或代码问题；此前服务请求均返回 200，随后作业被强制终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127570925889

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127557316992) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127557317185) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639534) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639575) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639641) |
| base-b-test-4-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639673) |
| base-b-test-16-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639687) |
| base-b-test-2-npu-a3 / run (0) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639696) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639787) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127558639972) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116222387/job/127570925912) |


## [Run #42116152423](https://github.com/sgl-project/sglang/actions/runs/42116152423)
- **分支**: `oss-sync-5ac6bc3c22`
- **总耗时**: 61.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42116152423

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 11.1min | 环境问题 | 自托管 runner 的容器执行失败，作业在模型 batch 捕获阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127571141238) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 13.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127571141355) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，发生在 Capturing batches 17% 时，属 runner/容器环境异常（可能 OOM 或进程被杀），非用例收集问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127571141238

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试请求正常返回 200，随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127571141355

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127556461501) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127556461809) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557441340) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557441550) |
| base-b-test-2-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557441745) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557441896) |
| base-b-test-16-npu-a3 / run (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557441905) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557442077) |
| base-b-test-1-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557442079) |
| base-b-test-4-npu-a3 / run (1) | 6.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127557442107) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42116152423/job/127571141222) |


## [Run #42115220323](https://github.com/sgl-project/sglang/actions/runs/42115220323)
- **分支**: `lsyin/sched-pr23`
- **总耗时**: 8.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42115220323

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 3.9min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略的中间日志确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554520810) |
| multimodal-gen-test-4-npu-a3 (0) | 4.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554520823) |
| base-b-test-1-npu-a3 / run (0) | 4.2min | 环境问题 | 自定义容器执行失败，导致测试作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521042) |
| base-b-test-8-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521046) |
| base-b-test-4-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521147) |
| base-b-test-16-npu-a3 / run (0) | 1.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521188) |
| base-b-test-2-npu-a3 / run (0) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521220) |
| base-b-test-4-npu-a3 / run (1) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521309) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾仅提示未找到 diffusion-failures/ 路径、无 artifact 上传，并伴随 Node.js 弃用警告；未见 Traceback 或退出码 5 的 unittest 错误，失败点应在被省略的中间日志中，当前片段不足以判定为代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554520810

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业在约4分钟内结束，无明确Traceback。结合退出码5，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554520823

- **base-b-test-1-npu-a3 / run (0)**: 日志显示测试方法 TestAscendMhaHicache.test_a_gsm8k 开始后立即报错“Executing the custom container implementation failed”，属于自托管 runner 的容器环境问题，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521042

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码问题；后续仅为清理步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521046

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，容器未能正常启动，未进入测试执行阶段，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521147

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 apt 安装 python3.10 后报错 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521188

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，容器未能正常启动，测试尚未执行，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521220

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，容器未能正常启动，测试尚未执行；属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127554521309

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127553192670) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42115220323/job/127553192765) |


## [Run #42114357010](https://github.com/sgl-project/sglang/actions/runs/42114357010)
- **分支**: `k31/linker-pcp-l3`
- **总耗时**: 47.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42114357010

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 22.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127562547537) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例本身失败；前一个精度用例已通过，后一个用例刚开始即中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127562547537

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127550132576) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127550132658) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551399593) |
| multimodal-gen-test-4-npu-a3 (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551399696) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551399851) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551399896) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551399900) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551399994) |
| base-b-test-16-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551400001) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127551400037) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127562547643) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42114357010/job/127562547789) |


## [Run #42098676255](https://github.com/sgl-project/sglang/actions/runs/42098676255)
- **分支**: `flashinfer-0.7.3-moe-ep`
- **总耗时**: 51.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42098676255

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.3min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127509734782) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例断言失败；此前 decode 推理正常，无 Traceback，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127509734782

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127496304706) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127496304893) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417568) |
| multimodal-gen-test-1-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417674) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417829) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417841) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417847) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417871) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417876) |
| multimodal-gen-test-4-npu-a3 (0) | 29.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417914) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497417927) |
| base-b-test-16-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127497418094) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127509734721) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42098676255/job/127509734757) |


## [Run #42093810892](https://github.com/sgl-project/sglang/actions/runs/42093810892)
- **分支**: `flashinfer-0.7.3-moe-ep`
- **总耗时**: 32.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42093810892

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 28.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479894933) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127493557390) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 3.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在编译阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127493557415) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在构建阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127493557515) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479894933

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 SHA256 校验通过后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，测试尚未开始执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127493557390

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示构建 xatlas C++ 对象时出现 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127493557415

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示构建 sglang 及 xatlas 过程中报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127493557515

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127478723984) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127478724303) |
| multimodal-gen-test-1-npu-a3 (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479894895) |
| multimodal-gen-test-4-npu-a3 (1) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479894903) |
| multimodal-gen-test-1-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895038) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895148) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895172) |
| base-b-test-2-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895174) |
| base-b-test-1-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895186) |
| base-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895240) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42093810892/job/127479895258) |


## [Run #42081204286](https://github.com/sgl-project/sglang/actions/runs/42081204286)
- **分支**: `oss-sync-fa6ceed880`
- **总耗时**: 26.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42081204286

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197751) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197751

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127434666517) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127434666552) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197018) |
| multimodal-gen-test-4-npu-a3 (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197027) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197186) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197433) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197435) |
| base-b-test-16-npu-a3 / run (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197684) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42081204286/job/127436197710) |


## [Run #42074484922](https://github.com/sgl-project/sglang/actions/runs/42074484922)
- **分支**: `k3/tuned-moe-front`
- **总耗时**: 17.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42074484922

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 14.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412250538) |
| multimodal-gen-test-4-npu-a3 (0) | 14.3min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412250553) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412250724) |
| multimodal-gen-test-1-npu-a3 (1) | 14.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251253) |
| base-b-test-1-npu-a3 / run (0) | 14.3min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251465) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251483) |
| base-b-test-2-npu-a3 / run (0) | 14.2min | 环境问题 | 自定义容器执行失败，疑似 runner 容器异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251639) |
| base-b-test-4-npu-a3 / run (0) | 14.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251756) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约14分钟结束，退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412250538

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业以退出码5结束（unittest errors），且未生成 diffusion-failures/ 目录产物。中间省略部分应含 Traceback/RuntimeError，最可能是 setUpClass 时 sglang server 启动失败（host OOM 或进程被 SIGKILL），属环境/资源问题而非用例收集失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412250553

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412250724

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出结果；退出码5对应 unittest errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251253

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 server 已正常启动并 ready，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251465

- **base-b-test-16-npu-a3 / run (0)**: 日志显示各 TP 权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251483

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 返回 200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251639

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题；此前推理仍在正常输出吞吐日志，随后容器执行失败导致作业终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251756

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127411198892) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127411199187) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251374) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42074484922/job/127412251776) |


## [Run #42072668339](https://github.com/sgl-project/sglang/actions/runs/42072668339)
- **分支**: `megakernel-prefill-extend`
- **总耗时**: 40.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42072668339

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 11.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127418609171) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127418609171

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127405443715) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127405443836) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406739633) |
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406739646) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406739653) |
| multimodal-gen-test-1-npu-a3 (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406739862) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406739949) |
| base-b-test-4-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406740081) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406740097) |
| base-b-test-1-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406740132) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406740232) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127406740392) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127418608995) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42072668339/job/127418609180) |


## [Run #41607308105](https://github.com/sgl-project/sglang/actions/runs/41607308105)
- **分支**: `feature/yunkai/gdn-verify-aiter`
- **总耗时**: 139.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/41607308105

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 2.9min | 环境问题 | 上传产物时未找到 diffusion-failures/ 目录，测试用例执行失败且无产物生成 | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637141) |
| multimodal-gen-test-4-npu-a3 (1) | 2.6min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637307) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/'，说明多模态生成测试未产出预期失败样本目录，结合退出码5推测 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），导致用例 error 且无产物可上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637141

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅包含 runner 初始化、action 下载和清理过程，未出现测试脚本输出或 Traceback；upload-artifact 提示未找到 diffusion-failures/ 路径，说明测试阶段未产生预期产物，疑似环境或前置步骤异常导致作业未正常执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637307

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127877612351) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127877612408) |
| multimodal-gen-test-1-npu-a3 (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637201) |
| multimodal-gen-test-4-npu-a3 (0) | 43.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637325) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637374) |
| base-b-test-16-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637396) |
| base-b-test-1-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637479) |
| base-b-test-4-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637497) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637534) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127878637558) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127890932659) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127890932940) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127890932945) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127922583013) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 34.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/41607308105/job/127922583134) |


---
*Auto-generated by ci_monitor.py*