# NPU CI 执行监控（2026-11-10）
**生成时间**: 2026-11-11 07:22
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-10 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 193

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1620 个 | 失败 349 个 | 成功 Job 平均耗时 14.1min
- **Run 执行情况**: 成功 74 个 | 失败 119 个 | 成功 Run 平均耗时 68.0min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 54.1min | #42645541472 | [job link](https://github.com/sgl-project/sglang/actions/runs/42645541472/job/129285082520) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 53.5min | #42740388491 | [job link](https://github.com/sgl-project/sglang/actions/runs/42740388491/job/129599281686) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 53.4min | #42646027813 | [job link](https://github.com/sgl-project/sglang/actions/runs/42646027813/job/129284997583) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 50.9min | #42747165375 | [job link](https://github.com/sgl-project/sglang/actions/runs/42747165375/job/129649723883) |
| multimodal-gen-test-4-npu-a3 (0) | 47.9min | #42718874778 | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508646981) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 47.0min | #42660671592 | [job link](https://github.com/sgl-project/sglang/actions/runs/42660671592/job/129338173380) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.6min | #42744285950 | [job link](https://github.com/sgl-project/sglang/actions/runs/42744285950/job/129605220955) |
| multimodal-gen-test-4-npu-a3 (0) | 45.8min | #42743626663 | [job link](https://github.com/sgl-project/sglang/actions/runs/42743626663/job/129591441704) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 45.6min | #42645373443 | [job link](https://github.com/sgl-project/sglang/actions/runs/42645373443/job/129276912559) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 45.4min | #42658428702 | [job link](https://github.com/sgl-project/sglang/actions/runs/42658428702/job/129317124935) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 56.8min | #42796560160 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587079) |
| base-b-test-1-npu-a3 / run (0) | 54.0min | #42814561076 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825565145) |
| multimodal-gen-test-4-npu-a3 (0) | 42.4min | #42807237864 | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800765118) |
| multimodal-gen-test-4-npu-a3 (0) | 36.6min | #42702537306 | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129453996480) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 32.2min | #42765036878 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129660205409) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | #42658924559 | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621645) |
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | #42818281834 | [job link](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038403) |
| base-b-test-1-npu-a3 / run (0) | 28.7min | #42764195582 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489103) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.5min | #42687587573 | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877400) |
| base-b-test-1-npu-a3 / run (0) | 26.9min | #42763321181 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757066928) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-2-npu-a3 / run (0) | 150 | 78 | 65 | 1 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682074)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725053)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564737)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634279)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833266) |
| base-b-test-4-npu-a3 / run (0) | 152 | 90 | 54 | 1 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725108)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564856)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634180)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833631)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522846) |
| base-b-test-1-npu-a3 / run (0) | 142 | 77 | 51 | 1 | 13 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816029)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635923)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868435551)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682094)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725058) |
| base-b-test-16-npu-a3 / run (0) | 129 | 91 | 25 | 3 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031323)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758488)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035038)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157367)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443349) |
| multimodal-gen-test-4-npu-a3 (0) | 151 | 126 | 8 | 0 | 17 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42827782256/job/129870498842)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42822933607/job/129854022520)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800765118)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587079)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152226) |
| base-b-test-8-npu-a3 / run (0) | 135 | 124 | 4 | 2 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101519)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351408286)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695948)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263707) |
| base-b-test-4-npu-a3 / run (1) | 152 | 139 | 4 | 1 | 8 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998827)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111826)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858429)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342696000) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 55 | 48 | 4 | 1 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129890037704)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129660205409)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129502244969)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129493639889) |
| multimodal-gen-test-1-npu-a3 (1) | 111 | 93 | 3 | 0 | 15 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998661)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152114)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732704) |
| multimodal-gen-test-4-npu-a3 (1) | 152 | 133 | 2 | 0 | 17 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152329)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351408386) |
| multimodal-gen-test-1-npu-a3 (0) | 112 | 96 | 2 | 0 | 14 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152181)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407660) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 49 | 47 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129586965855)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877400) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 49 | 46 | 0 | 2 | 1 | - |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 71 | 70 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817475433) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_mla_fia_hicache_bf16.py` | 98 | 36 | 62 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725053)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564737)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634279) |
| `npu_dp_attention.py` | 89 | 35 | 54 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725108)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564856)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634180) |
| `dspark_npu_dispatch.py` | 54 | 6 | 48 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816029)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635923)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868435551) |
| `npu_speculative_moe_a2a_backend.py` | 84 | 60 | 24 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031323)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758488)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035038) |
| `minimax_h3_t2va_2npu` | 66 | 60 | 6 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42827782256/job/129870498842)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42822933607/job/129854022520)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038403) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 90 | 87 | 3 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101519)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695948)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263707) |
| `npu_pd_disaggregation.py` | 92 | 90 | 2 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998827)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111826) |
| `npu_speculative_multi_npu.py` | 85 | 83 | 2 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858429)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342696000) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 7 | 5 | 2 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129586965855)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877400) |
| `npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py` | 5 | 3 | 2 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129890037704)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129502244969) |
| `npu_autoround_moe.py` | 81 | 80 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349623) |
| `npu_gptq_moe.py` | 80 | 79 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713013) |
| `npu_eagle3.py` | 77 | 76 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101619) |
| `npu_basic_sanity_eagle3.py` | 78 | 77 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758526) |
| `npu_moe_runner_backend.py` | 35 | 34 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682074) |
| `npu_return_indexer_topk_deepseek_v4.py` | 33 | 32 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395094) |
| `npu_return_indexer_topk_glm52.py` | 32 | 31 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613588) |
| `mova_360p_ti2va_2npu` | 62 | 61 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587079) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 7 | 6 | 1 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817475433) |
| `npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py` | 5 | 4 | 1 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129493639889) |
| `npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py` | 4 | 3 | 1 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129660205409) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #42821381972<br>[#47287 [Perf] [AMD] Qwen3.5: enable fused GDN decode unpack + Conv1D for ROCm platform](https://github.com/sgl-project/sglang/pull/47287) | `opt/qwen35_gdn_decode_fused_proj_conv` | 109.0min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42821381972) |
| #42705053125<br>[#48648 [Perf] [AMD] Qwen4-Exp/HC: Fuse decode-sized hyper-connection norm and inject into FlyDSL mix](https://github.com/sgl-project/sglang/pull/48648) | `perf/amd-qwen4-fused-hc-decode` | 82.5min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42705053125) |
| #42699506676 | `users/wenkaidu/carv2-2shot-push-gfx1250` | 78.0min | 2 | multimodal-gen-test-1-npu-a3 (1), base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42699506676) |
| #42658924559<br>[#44738 [Feat] [NPU] Diffusion: support online W8A8 INT8 quantization](https://github.com/sgl-project/sglang/pull/44738) | `int8_diffusion_online_quantization` | 73.1min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42658924559) |
| #42796560160<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 71.0min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42796560160) |
| #42814561076<br>[#47917 [Feat] [NPU] longcat: Support Longcat2.0 for arch22 NPU](https://github.com/sgl-project/sglang/pull/47917) | `main` | 57.7min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42814561076) |
| #42687587573<br>[#47554 [Perf] R3: Gather DeepEP routed-expert ids once per forward (3/3)](https://github.com/sgl-project/sglang/pull/47554) | `byron/r3-deepep-gather-once` | 54.6min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42687587573) |
| #42718874778 | `xpu/weekly-simple-model-enablement-2026-11-09` | 51.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42718874778) |
| #42702537306 | `minimax_npu_rmsnorm_path` | 49.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42702537306) |
| #42739609182<br>[#48933 [Perf] [Apple] mps: Encode and prefill the next Unlimited-OCR v2 window under the current decode](https://github.com/sgl-project/sglang/pull/48933) | `uocr2-mlx` | 49.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42739609182) |
| #42743590407<br>[#47371 [Feat] [AMD] muse-spark: Add the ROCm day0 implementation](https://github.com/sgl-project/sglang/pull/47371) | `pr/muse-spark-rocm-sa-1027` | 46.6min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42743590407) |
| #42807237864 | `minimax_npu_rmsnorm_path` | 46.0min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42807237864) |
| #42835229692<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 45.7min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42835229692) |
| #42713709280 | `hicache/scheduler-thread-bounded-calls` | 44.6min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42713709280) |
| #42757391891 | `refactor/graph-break-recorder` | 44.4min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42757391891) |
| #42781331186<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 44.1min | 5 | multimodal-gen-test-1-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42781331186) |
| #42763383553<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 42.9min | 4 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42763383553) |
| #42765036878<br>[#38806 [Perf] [AMD] gdn: Optimize Qwen3.5 prefill preparation and Triton recurrence](https://github.com/sgl-project/sglang/pull/38806) | `amd/hip-gdn-prefill-layout` | 41.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42765036878) |
| #42733896979<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 41.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42733896979) |
| #42810523072<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 41.0min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42810523072) |
| #42702934954 | `dark/carv2-dpx-pair-header` | 40.6min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42702934954) |
| #42765132333<br>[#49214 [Feat] [MLU] attention: Add paged GQA attention support](https://github.com/sgl-project/sglang/pull/49214) | `feat/mlu-paged-gqa-fused-ops` | 40.2min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42765132333) |
| #42780359233<br>[#48787 [Perf] [XPU] fp8: Run FP8 dense layers weight-only (W8A16) through sgl_kernel.fp8_linear](https://github.com/sgl-project/sglang/pull/48787) | `upr/xpu-fp8-w8a16-linear-v3` | 39.9min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42780359233) |
| #42736645521<br>[#47371 [Feat] [AMD] muse-spark: Add the ROCm day0 implementation](https://github.com/sgl-project/sglang/pull/47371) | `pr/muse-spark-rocm-sa-1027` | 38.9min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42736645521) |
| #42789068687<br>[#48353 [Fix] [XPU] compressed-tensors: Support W8A8 int8 on XPU and quantize Whisper MLP linears.](https://github.com/sgl-project/sglang/pull/48353) | `fix/xpu-whisper-w8a8-int8` | 38.5min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42789068687) |
| #42717017070<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 38.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42717017070) |
| #42778916692<br>[#45927 [Perf] [XPU] linear: Use torch scaled_mm for MXFP8 linear](https://github.com/sgl-project/sglang/pull/45927) | `ecao/xpu_mxfp8_scaled_mm_v2` | 37.7min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42778916692) |
| #42758762191<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 37.3min | 4 | base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42758762191) |
| #42811037470<br>[#49481 [Feat] [NPU] prefill: breakable prefill graph for DSV4 and ascend_ops MoE](https://github.com/sgl-project/sglang/pull/49481) | `prefill_graph_ascend_ops_on_main` | 36.9min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42811037470) |
| #42787658983<br>[#49370 [Refactor] custom-ar-v2: Move the DPX pair stages into their own header](https://github.com/sgl-project/sglang/pull/49370) | `dark/carv2-dpx-pair-header` | 36.8min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42787658983) |
| #42782980150<br>[#47183 [Feat] Spark2.5: Support Spark2.5 Dspark](https://github.com/sgl-project/sglang/pull/47183) | `feature/spark2_5_dspark` | 36.8min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42782980150) |
| #42814047545<br>[#43851 [Feat] [NVIDIA] dsv4.1: [1/N] Add packed FP4 Main KV storage for Hopper.](https://github.com/sgl-project/sglang/pull/43851) | `feat/dsv41-packed-main-kv` | 36.6min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42814047545) |
| #42814579721<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 36.2min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42814579721) |
| #42783582113<br>[#49264 [Feat] [NPU] memory-saver: Release device communication domains on sleep mode](https://github.com/sgl-project/sglang/pull/49264) | `feat/hccl-clean-new` | 36.2min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42783582113) |
| #42751910982 | `dark/carv2-dpx-pair-header` | 36.2min | 5 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42751910982) |
| #42723588649<br>[#44615 [Perf] NIXL: KV packing for TP-heterogeneous transfer (Muse Spark Open)](https://github.com/sgl-project/sglang/pull/44615) | `wj/nixl-kv-packing` | 36.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42723588649) |
| #42776748416<br>[#48047 [Perf] hicache: optional minimum tokens per write_back allocation-driven eviction](https://github.com/sgl-project/sglang/pull/48047) | `hicache-evict-headroom` | 36.1min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42776748416) |
| #42764382060<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 36.1min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42764382060) |
| #42681165596<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 36.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42681165596) |
| #42775218652<br>[#47371 [Feat] [AMD] muse-spark: Add the ROCm day0 implementation](https://github.com/sgl-project/sglang/pull/47371) | `pr/muse-spark-rocm-sa-1027` | 35.8min | 4 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42775218652) |
| #42800160081<br>[#41794 [Perf] [AMD] kimi-k3: Run the fused KDA decode with a BF16 state and Quark weights](https://github.com/sgl-project/sglang/pull/41794) | `k3-pr1-quark-weights` | 35.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42800160081) |
| #42758944406<br>[#38344 [Feat] CP: Prefill context parallelism for Kimi K3](https://github.com/sgl-project/sglang/pull/38344) | `linear-attn-prefill-cp-ulysses` | 35.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42758944406) |
| #42764195582<br>[#49370 [Refactor] custom-ar-v2: Move the DPX pair stages into their own header](https://github.com/sgl-project/sglang/pull/49370) | `dark/carv2-dpx-pair-header` | 35.4min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42764195582) |
| #42827000424<br>[#49277 [Fix][NPU]moe: Optimize Ascend MoE AllGather dispatch and combine](https://github.com/sgl-project/sglang/pull/49277) | `feat/dev_ascend_ops` | 35.3min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42827000424) |
| #42755788989<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 35.1min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42755788989) |
| #42822167900<br>[#44360 [Perf] [AMD] kimi-k3: Run the merged MoE front through AITER tuned BF16 GEMM](https://github.com/sgl-project/sglang/pull/44360) | `k3/tuned-moe-front` | 34.9min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42822167900) |
| #42772832351<br>[#45737 [Feat] kv-events: Report caller multimodal routing labels as block spans](https://github.com/sgl-project/sglang/pull/45737) | `feat/mm-routing-label-spans` | 34.9min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42772832351) |
| #42767501673<br>[#38362 [Fix] hicache: Include persisted KV dtype in storage keys](https://github.com/sgl-project/sglang/pull/38362) | `stmatengss/mooncake-kvcache-dtype-cb2a` | 34.9min | 4 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42767501673) |
| #42669362795<br>[#49083 [PD] Fix PD + Mooncake linker on a shared transfer engine by sharing its memory registrations](https://github.com/sgl-project/sglang/pull/49083) | `shuwen/fix-mooncake-shared-te-registration` | 34.9min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42669362795) |
| #42757697151 | `openai-tokenize-api` | 34.7min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42757697151) |
| #42798232485<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 34.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42798232485) |
| #42795535677<br>[#47867 [Feat] [AMD] hicache: Add --hicache-mamba-size-gb to pin the HiCache Mamba host pool size](https://github.com/sgl-project/sglang/pull/47867) | `k3/hicache-mamba-size-gb` | 34.3min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42795535677) |
| #42751232924<br>[#48047 [Perf] hicache: optional minimum tokens per write_back allocation-driven eviction](https://github.com/sgl-project/sglang/pull/48047) | `hicache-evict-headroom` | 34.2min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42751232924) |
| #42558320866<br>[#47437 [Perf] [AMD] aiter: Run the DSpark MHA draft on non-causal unified_attention](https://github.com/sgl-project/sglang/pull/47437) | `k3/dspark-draft-unified-attn` | 34.1min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42558320866) |
| #42739229421<br>[#44360 [Perf] [AMD] kimi-k3: Run the merged MoE front through AITER tuned BF16 GEMM](https://github.com/sgl-project/sglang/pull/44360) | `k3/tuned-moe-front` | 33.7min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42739229421) |
| #42766376254<br>[#45947 [Feat] Comm: Add gated allgather in kv cache sharding](https://github.com/sgl-project/sglang/pull/45947) | `comm/gated-allgather` | 33.6min | 4 | base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42766376254) |
| #42774974433<br>[#44737 [Fix] responses: fix reasoning.effort in non-streaming responses and max_output_tokens=1 validation](https://github.com/sgl-project/sglang/pull/44737) | `fix/responses-reasoning-effort` | 32.9min | 4 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42774974433) |
| #42747016375<br>[#41329 [Feat] [CPU] quantization: Add CPU FP8/INT8 quant ops and compressed-tensors support](https://github.com/sgl-project/sglang/pull/41329) | `yanbing/cpu-fp8-quant-support` | 32.7min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42747016375) |
| #42802563229<br>[#36426  [NPU][Quant] Fix ModelSlim W8A8 loading for Qwen3.8-27B-W8A8: resolve fused in_proj_qkvz scheme, quantize vision encoder, flatten 3-D inputs in NPU W8A8 kernels](https://github.com/sgl-project/sglang/pull/36426) | `fix/modelslim-w8a8-loading-clean` | 32.3min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42802563229) |
| #42818281834 | `minimax_npu_rmsnorm_path` | 32.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42818281834) |
| #42765581304<br>[#39754 [Fix] embedding: Keep the trailing [SEP] on auto-truncation and accumulate MEAN pooling in fp32](https://github.com/sgl-project/sglang/pull/39754) | `model-serve/encoder-sep-truncation` | 31.6min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42765581304) |
| #42758071741<br>[#49436 [Fix] dspark: Write deferred draft KV only for carried requests](https://github.com/sgl-project/sglang/pull/49436) | `lsyin/sched-dspark-rows` | 31.4min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42758071741) |
| #42739445307<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 31.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42739445307) |
| #42789214551<br>[#48938 [Fix] watchdog: Let py-spy attach to watched processes in CI](https://github.com/sgl-project/sglang/pull/48938) | `fix-pyspy-ptrace-ci` | 30.4min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42789214551) |
| #42762751287<br>[#36591 [Fix] hisparse: state-preserving retraction and recovery for DSV4](https://github.com/sgl-project/sglang/pull/36591) | `fix/hisparse-cpu-copy-retraction` | 30.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42762751287) |
| #42757218854<br>[#47859 [Feat] moe: Add Mooncake Elastic EP scale-up support](https://github.com/sgl-project/sglang/pull/47859) | `elastic-base` | 29.7min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42757218854) |
| #42842534328<br>[#31170 [Feat] dp-attention: Add prefix_affinity load balancing for routing-key/session affinity](https://github.com/sgl-project/sglang/pull/31170) | `feat/dp-prefix-affinity` | 27.8min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42842534328) |
| #42794977664<br>[#34153 [Scheduler] Fix final chunked-prefill abort commit race](https://github.com/sgl-project/sglang/pull/34153) | `jeremyzhang866/fix-chunked-prefill-abort-commit` | 27.4min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42794977664) |
| #42763321181<br>[#49430 [Feat] mem_cache: Evict Mamba states by GreedyDual-Size (--radix-eviction-policy gds)](https://github.com/sgl-project/sglang/pull/49430) | `feat/mamba-hybrid-state-eviction` | 27.4min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42763321181) |
| #42715925425<br>[#49402 [Refactor] graph: Introduce device-neutral graph backend bases (1/3)](https://github.com/sgl-project/sglang/pull/49402) | `refactor/graph-neutral-backends` | 27.1min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42715925425) |
| #42810175143<br>[#48409 [Feat] scheduler: add fixed-batch bounded LPM policy](https://github.com/sgl-project/sglang/pull/48409) | `codex/bounded-lpm-window` | 27.0min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42810175143) |
| #42752868509<br>[#47308 [Fix] scheduler: reserve SPF capacity against both token budgets](https://github.com/sgl-project/sglang/pull/47308) | `wuyaole/fix-prefill-reservation-budget` | 26.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42752868509) |
| #42726478322<br>[#30893 [Refactor] hisparse: unify device-pool mapping and selection](https://github.com/sgl-project/sglang/pull/30893) | `codex/23602-hisparse-pool` | 26.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42726478322) |
| #42749819313<br>[#49420 [Fix] [NVIDIA] jit: Build sm_107a on CC 10.7, keeping sm_100f only for modules that use CUTLASS](https://github.com/sgl-project/sglang/pull/49420) | `jit-sm107a-per-module` | 26.3min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42749819313) |
| #42767216558<br>[#43527 [Feat] QSA: Add cache sharding for Qwen3.8 hybrid models](https://github.com/sgl-project/sglang/pull/43527) | `feat/qsa-cache-sharding` | 26.2min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42767216558) |
| #42708776271<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 26.2min | 5 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42708776271) |
| #42804078462<br>[#49496 [Refactor] scheduler: Move a request between owner lists in one call](https://github.com/sgl-project/sglang/pull/49496) | `lsyin/sched-pr38` | 26.1min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42804078462) |
| #42758401032<br>[#44447 [Feat] KVShard: Enable KV cache sharding for Qwen3.8 Flash Next](https://github.com/sgl-project/sglang/pull/44447) | `kvshard/qwen38-flash-next` | 26.1min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42758401032) |
| #42747738764<br>[#44170 [Fix] memory: Reserve the symmetric-memory prealloc out of the KV budget](https://github.com/sgl-project/sglang/pull/44170) | `fix/symm-mem-kv-budget-44106` | 26.0min | 3 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42747738764) |
| #42824178718<br>[#49552 [Feat] diffusion/model: Support MiniMaxAI/MiniMax-H3-Image](https://github.com/sgl-project/sglang/pull/49552) | `qfw/h3-image-day0` | 25.8min | 4 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42824178718) |
| #42740256301<br>[#40732 [Fix] hisparse: Rebootstrap retracted PD decode requests instead of offloading KV](https://github.com/sgl-project/sglang/pull/40732) | `fix/hisparse-decode-retract-rebootstrap` | 25.4min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42740256301) |
| #42753567883<br>[#47859 [Feat] moe: Add Mooncake Elastic EP scale-up support](https://github.com/sgl-project/sglang/pull/47859) | `elastic-base` | 25.3min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42753567883) |
| #42743079130<br>[#42199 [Fix] scheduler: Stop the prefill delayer's queue trigger from ending its own delay](https://github.com/sgl-project/sglang/pull/42199) | `fix/prefill-delayer-queue-trigger` | 25.1min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42743079130) |
| #42789061908<br>[#44684 [Feat] HiSparse: Support DeepSeek-V4 with MTP and DSpark](https://github.com/sgl-project/sglang/pull/44684) | `dsv4_hisparse_dspark` | 24.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42789061908) |
| #42796650355<br>[#48776 [Feat] kimi-k3: Read the `thinking` object and map reasoning effort onto K3 tiers](https://github.com/sgl-project/sglang/pull/48776) | `lsyin/k3-request-validation` | 24.6min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42796650355) |
| #42740687104<br>[#49430 [Feat] mem_cache: Evict Mamba states by GreedyDual-Size (--radix-eviction-policy gds)](https://github.com/sgl-project/sglang/pull/49430) | `feat/mamba-hybrid-state-eviction` | 24.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42740687104) |
| #42763871106<br>[#45947 [Feat] Comm: Add gated allgather in kv cache sharding](https://github.com/sgl-project/sglang/pull/45947) | `comm/gated-allgather` | 24.5min | 6 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42763871106) |
| #42743763880<br>[#48095 [Perf] [AMD] dspark: Speed up the DSPARK draft step](https://github.com/sgl-project/sglang/pull/48095) | `dspark-draft-gfx1250_di_7/N` | 24.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42743763880) |
| #42822933607 | `minimax_npu_rmsnorm_path` | 24.4min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42822933607) |
| #42779628867<br>[#42199 [Fix] scheduler: Stop the prefill delayer's queue trigger from ending its own delay](https://github.com/sgl-project/sglang/pull/42199) | `fix/prefill-delayer-queue-trigger` | 24.3min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42779628867) |
| #42767892232<br>[#47626 [Fix] hicache: settle storage backups at the rank-agreed written prefix](https://github.com/sgl-project/sglang/pull/47626) | `hicache/scheduler-thread-bounded-calls` | 23.9min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42767892232) |
| #42827782256 | `minimax_npu_rmsnorm_path` | 21.8min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42827782256) |
| #42807648592<br>[#49496 [Refactor] scheduler: Move a request between owner lists in one call](https://github.com/sgl-project/sglang/pull/49496) | `lsyin/sched-pr38` | 19.9min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42807648592) |
| #42771038056 | `openai-tokenize-api` | 19.7min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42771038056) |
| #42778998981<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 18.8min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42778998981) |
| #42815405149 | `minimax_npu_rmsnorm_path` | 17.0min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42815405149) |
| #42819781038<br>[#49552 [Feat] diffusion/model: Support MiniMaxAI/MiniMax-H3-Image](https://github.com/sgl-project/sglang/pull/49552) | `qfw/h3-image-day0` | 16.4min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42819781038) |
| #42647673269<br>[#46754 [Fix] attention: Isolate GDN MIS item state from delimiters](https://github.com/sgl-project/sglang/pull/46754) | `mani1106/gdn-mis-delimiter-isolation` | 16.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42647673269) |
| #42766004150<br>[#41496 [Feat] [NPU] layernorm-sp: Support sequence parallel on NPU](https://github.com/sgl-project/sglang/pull/41496) | `feat/npu-layernorm-sp` | 15.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42766004150) |
| #42782835433<br>[#48385 [Fix] multimodal: keep placeholder token ids at multimodal positions of input_ids](https://github.com/sgl-project/sglang/pull/48385) | `qwen38-ple-mm-placeholder-ids` | 15.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42782835433) |
| #42732752403<br>[#45894 [Feat] sampling: Add per-request SynthID Text watermarking](https://github.com/sgl-project/sglang/pull/45894) | `vedantjh2/synthid-oss` | 14.4min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42732752403) |
| #42822130553<br>[#49552 [Feat] diffusion/model: Support MiniMaxAI/MiniMax-H3-Image](https://github.com/sgl-project/sglang/pull/49552) | `qfw/h3-image-day0` | 13.9min | 4 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42822130553) |
| #42770061389<br>[#47617 [Fix] hicache: keep the storage ack sequence on backend failures, stop workers in lockstep, fail the rank when a worker dies](https://github.com/sgl-project/sglang/pull/47617) | `hicache/scheduler-thread-agreement` | 13.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42770061389) |
| #42735083488<br>[#47371 [Feat] [AMD] muse-spark: Add the ROCm day0 implementation](https://github.com/sgl-project/sglang/pull/47371) | `pr/muse-spark-rocm-sa-1027` | 13.6min | 8 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42735083488) |
| #42758953221<br>[#46499 [Feat] UnifiedL3: support mooncake storage backend](https://github.com/sgl-project/sglang/pull/46499) | `page-unified/mooncake-storage` | 13.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42758953221) |
| #42767876044 | `hicache/scheduler-thread-agreement` | 12.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42767876044) |
| #42773412162<br>[#49043 [Fix] linker: Renew Mooncake read leases that lapse during a load](https://github.com/sgl-project/sglang/pull/49043) | `fix/linker-mooncake-lease-renewal` | 12.3min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42773412162) |
| #42781532860<br>[#48775 [Feat] kimi-k3: Stream tool-call arguments incrementally](https://github.com/sgl-project/sglang/pull/48775) | `lsyin/k3-tool-call-parsing` | 12.1min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42781532860) |
| #42733637030<br>[#47371 [Feat] [AMD] muse-spark: Add the ROCm day0 implementation](https://github.com/sgl-project/sglang/pull/47371) | `pr/muse-spark-rocm-sa-1027` | 12.0min | 10 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42733637030) |
| #42732549856<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 11.0min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42732549856) |
| #42789289538<br>[#49414 [Fix] logprobs: Bound top_logprobs to [0,vocab_size]](https://github.com/sgl-project/sglang/pull/49414) | `validate-top-logprobs-num` | 10.8min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42789289538) |
| #42783271713<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 10.8min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42783271713) |
| #42765547620<br>[#46740 [Fix] [XPU] spec: Start NEXTN/MTP drafts on XPU and stop silent greedy verify](https://github.com/sgl-project/sglang/pull/46740) | `siju/xpu-mtp-spec-fixes` | 9.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42765547620) |
| #42575746641<br>[#46540 [Fix] hicache: Move NIXL pages that are not whole O_DIRECT blocks](https://github.com/sgl-project/sglang/pull/46540) | `nixl-odirect-zero-copy` | 9.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42575746641) |
| #42739490867 | `feat/mlu-paged-gqa-fused-ops` | 8.1min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42739490867) |
| #42673402805 | `xpu-monokernel-framework` | 8.1min | 5 | multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-1-npu-a3 (0), base-b-test-8-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42673402805) |
| #42826704005 | `minimax_npu_rmsnorm_path` | 7.4min | 2 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42826704005) |
| #42731861763<br>[#44588 [Feat] spec: Online acceptance estimator for DSpark confidence-scheduled verification](https://github.com/sgl-project/sglang/pull/44588) | `adaptive-verification-online-estimator` | 6.2min | 9 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42731861763) |
| #42773791885<br>[#48807 [Test] [Ascend] npu: GLM-5.3 1P1D accuracy cases + weekday gsm8k](https://github.com/sgl-project/sglang/pull/48807) | `test/glm5-3-eplb-gpqa` | 5.6min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42773791885) |

---


## [Run #42842534328](https://github.com/sgl-project/sglang/actions/runs/42842534328)
- **分支**: `feat/dp-prefix-affinity`
- **总耗时**: 27.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42842534328

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.2min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816029) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过，最终进程以 exit code 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816029

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129921584539) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129921584593) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922815671) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922815740) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922815988) |
| base-b-test-16-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922815990) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816046) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816170) |
| base-b-test-4-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42842534328/job/129922816571) |


## [Run #42835229692](https://github.com/sgl-project/sglang/actions/runs/42835229692)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 45.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42835229692

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.7min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635923) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635923

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129895826478) |
| Recommend tests from coverage | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129895826513) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897634905) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635130) |
| multimodal-gen-test-1-npu-a3 (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635343) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635707) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635781) |
| base-b-test-16-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635879) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635902) |
| base-b-test-4-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897635928) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42835229692/job/129897636034) |


## [Run #42827782256](https://github.com/sgl-project/sglang/actions/runs/42827782256)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 21.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42827782256

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 11.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42827782256/job/129870498842) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试未正常产出结果；退出码5对应unittest errors，常见于setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42827782256/job/129870498842

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827782256/job/129869883166) |
| multimodal-gen-test-4-npu-a3 (1) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827782256/job/129870499090) |


## [Run #42827000424](https://github.com/sgl-project/sglang/actions/runs/42827000424)
- **分支**: `feat/dev_ascend_ops`
- **总耗时**: 35.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42827000424

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.8min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868435551) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过，最终进程以退出码 1 结束。日志未给出具体 Traceback，需查看该用例的详细输出以定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868435551

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129867053143) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129867053440) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434344) |
| multimodal-gen-test-1-npu-a3 (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434386) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434430) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434509) |
| base-b-test-16-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434636) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434669) |
| base-b-test-4-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434672) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434687) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42827000424/job/129868434810) |


## [Run #42826704005](https://github.com/sgl-project/sglang/actions/runs/42826704005)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 7.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42826704005

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42826704005/job/129866784822) |
| multimodal-gen-test-4-npu-a3 (1) | 4.9min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42826704005/job/129866784854) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业在约4分钟后结束，未上传 diffusion-failures/ 产物（无文件），说明用例未正常产出失败样本；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段中的 Traceback/RuntimeError 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42826704005/job/129866784822

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约4分钟结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42826704005/job/129866784854

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42826704005/job/129866058971) |


## [Run #42824178718](https://github.com/sgl-project/sglang/actions/runs/42824178718)
- **分支**: `qfw/h3-image-day0`
- **总耗时**: 25.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42824178718

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 14.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392203) |
| multimodal-gen-test-4-npu-a3 (1) | 14.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392212) |
| multimodal-gen-test-1-npu-a3 (1) | 14.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392288) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | 环境问题 | diffusion 测试失败且未生成失败产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392334) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示用例执行后退出码5（unittest errors），且未生成diffusion-failures目录产物，说明测试在setUpClass阶段即失败，常见原因为host OOM或server进程被SIGKILL，需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392203

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392212

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392288

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试脚本异常退出（退出码 5，unittest errors），最常见为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129858392334

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42824178718/job/129857388976) |


## [Run #42822933607](https://github.com/sgl-project/sglang/actions/runs/42822933607)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 24.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42822933607

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 14.4min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例 error | [job link](https://github.com/sgl-project/sglang/actions/runs/42822933607/job/129854022520) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；但作业上传了 diffusion-failures-npu-2-part0-1.zip 失败工件，且退出码 5 通常对应 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。需查看该工件与中间日志确认根因。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42822933607/job/129854022520

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822933607/job/129853144933) |
| multimodal-gen-test-4-npu-a3 (1) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822933607/job/129854022609) |


## [Run #42822167900](https://github.com/sgl-project/sglang/actions/runs/42822167900)
- **分支**: `k3/tuned-moe-front`
- **总耗时**: 34.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42822167900

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 18.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682074) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682094) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_moe_runner_backend.py, npu_moe_runner_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682074

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682094

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129850449222) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129850449273) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851681808) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851681893) |
| multimodal-gen-test-1-npu-a3 (1) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851681899) |
| multimodal-gen-test-4-npu-a3 (0) | 29.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851681942) |
| base-b-test-16-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851681998) |
| base-b-test-8-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682044) |
| base-b-test-4-npu-a3 / run (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682054) |
| base-b-test-4-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822167900/job/129851682057) |


## [Run #42822130553](https://github.com/sgl-project/sglang/actions/runs/42822130553)
- **分支**: `qfw/h3-image-day0`
- **总耗时**: 13.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42822130553

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 10.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851419855) |
| multimodal-gen-test-1-npu-a3 (0) | 10.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851419968) |
| multimodal-gen-test-4-npu-a3 (1) | 10.6min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851420134) |
| multimodal-gen-test-4-npu-a3 (0) | 9.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851420220) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业以退出码5结束，按背景知识为 unittest errors，最常见原因是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851419855

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851419968

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约10分钟后结束。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851420134

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129851420220

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42822130553/job/129850395808) |


## [Run #42821381972](https://github.com/sgl-project/sglang/actions/runs/42821381972)
- **分支**: `opt/qwen35_gdn_decode_fused_proj_conv`
- **总耗时**: 109.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42821381972

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.5min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 执行失败，退出码 1，3 个用例全部未通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129890037704) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本运行约 570 秒后返回 exit code 1，Test Summary 为 0/3 passed，但省略部分未给出具体 Traceback，无法确定是精度/性能阈值不达标还是 server 启动失败，需查看完整日志确认根因。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129890037704

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129847748908) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129847748995) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093262) |
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093362) |
| base-b-test-2-npu-a3 / run (0) | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093436) |
| base-b-test-16-npu-a3 / run (0) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093639) |
| base-b-test-1-npu-a3 / run (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093716) |
| base-b-test-4-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093719) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849093759) |
| base-b-test-4-npu-a3 / run (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129849094022) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 44.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129863916310) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129863916340) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129863916398) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42821381972/job/129890037788) |


## [Run #42819781038](https://github.com/sgl-project/sglang/actions/runs/42819781038)
- **分支**: `qfw/h3-image-day0`
- **总耗时**: 16.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42819781038

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181510) |
| multimodal-gen-test-4-npu-a3 (0) | 13.3min | 环境问题 | 日志中未见测试用例的 Traceback，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明确。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181648) |
| multimodal-gen-test-1-npu-a3 (1) | 13.0min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181659) |
| multimodal-gen-test-4-npu-a3 (1) | 13.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181728) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示用例以退出码5结束（FAILED errors=N），且未生成 diffusion-failures 目录产物，说明测试在 setUpClass 阶段即失败，常见原因为 host OOM 或 server 进程被 SIGKILL，需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181510

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被省略，缺少真实错误信息；仅见 upload-artifact 提示未找到 diffusion-failures/ 路径，无 unittest 报错细节，无法判定为代码或精度问题，倾向环境/脚本产物路径问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181648

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中未见 pytest 收集失败，退出码5对应 unittest errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志省略了中间 Traceback，需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181659

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业失败且未找到diffusion-failures/产物，结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129843181728

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42819781038/job/129842262589) |


## [Run #42818281834](https://github.com/sgl-project/sglang/actions/runs/42818281834)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 32.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42818281834

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | 其他 | 多模态生成测试失败，上传了 diffusion-failures 产物，但日志省略了具体错误。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038403) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业退出码5表示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。日志中间被省略，未见Traceback，需查看上传的diffusion-failures-npu-2-part0-1.zip产物确认具体错误。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038403

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129837230312) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038238) |
| multimodal-gen-test-1-npu-a3 (1) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038331) |
| multimodal-gen-test-4-npu-a3 (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42818281834/job/129838038523) |


## [Run #42815405149](https://github.com/sgl-project/sglang/actions/runs/42815405149)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 17.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42815405149

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | 环境问题 | 作业日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035375) |
| multimodal-gen-test-1-npu-a3 (1) | 14.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035448) |
| multimodal-gen-test-4-npu-a3 (0) | 14.5min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，无法上传产物，作业失败原因不明。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035498) |
| multimodal-gen-test-4-npu-a3 (1) | 14.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035530) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，仅见 artifact 上传时提示 'No files were found with the provided path: diffusion-failures/'，无 Traceback 或退出码信息，无法定位真实失败原因，需查看完整日志确认是否为 server 启动失败或 OOM。
  链接: https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035375

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业在约14分钟后结束。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035448

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，缺少关键错误信息。末尾仅提示未找到 diffusion-failures/ 路径，无 artifact 上传；未见 Traceback 或退出码 5 的 unittest 错误，无法确认具体失败原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035498

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例执行后退出码5（FAILED errors=N），且未生成 diffusion-failures 目录产物，说明测试在 setUpClass 阶段即失败，常见原因为 server 启动失败（host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129828035530

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42815405149/job/129827312432) |


## [Run #42814579721](https://github.com/sgl-project/sglang/actions/runs/42814579721)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 36.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42814579721

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725053) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725058) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725108) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 运行61秒后返回退出码5，表示 unittest 存在 errors，最常见为 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL）。日志未显示具体 Traceback，需查看该用例详细输出确认根因。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725053

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 44s），其余用例均通过，最终进程以退出码 1 结束，属该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725058

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时约 244 秒后返回 exit code 1，需查看该用例具体 Traceback 定位是服务启动还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725108

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129824487220) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129824487326) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825724896) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825724915) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825724916) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725018) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725041) |
| base-b-test-16-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725110) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814579721/job/129825725374) |


## [Run #42814561076](https://github.com/sgl-project/sglang/actions/runs/42814561076)
- **分支**: `main`
- **总耗时**: 57.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42814561076

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564737) |
| base-b-test-4-npu-a3 / run (0) | 12.4min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 运行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564856) |
| base-b-test-1-npu-a3 / run (0) | 54.0min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825565145) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例全部未通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564737

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后执行失败，耗时约 524 秒，2 个用例 0 通过，进程以 exit code 1 结束，导致作业失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564856

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过，该用例失败使进程以退出码 1 结束；日志未给出具体 Traceback，需查看该用例详细输出定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825565145

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129824406729) |
| multimodal-gen-test-1-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564541) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564570) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564571) |
| base-b-test-16-npu-a3 / run (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564608) |
| multimodal-gen-test-4-npu-a3 (0) | 33.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564662) |
| base-b-test-8-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564725) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814561076/job/129825564843) |


## [Run #42814047545](https://github.com/sgl-project/sglang/actions/runs/42814047545)
- **分支**: `feat/dsv41-packed-main-kv`
- **总耗时**: 36.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42814047545

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.0min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634180) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634187) |
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634279) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时约 309 秒后返回 exit code 1，需查看该用例 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634180

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 44s），其余用例均通过，最终进程以退出码 1 结束，属于该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634187

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回exit code 5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例全部未通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634279

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129822699442) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129822699458) |
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823633938) |
| multimodal-gen-test-1-npu-a3 (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823633984) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634087) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634095) |
| base-b-test-4-npu-a3 / run (1) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634169) |
| base-b-test-16-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634224) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42814047545/job/129823634258) |


## [Run #42811037470](https://github.com/sgl-project/sglang/actions/runs/42811037470)
- **分支**: `prefill_graph_ascend_ops_on_main`
- **总耗时**: 36.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42811037470

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833266) |
| base-b-test-1-npu-a3 / run (0) | 25.8min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833392) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833631) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833266

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过；该用例失败使进程以退出码 1 结束，日志未给出具体 Traceback，需查看该用例详细输出定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833392

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，--enable-dp-attention）后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 239 秒。日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833631

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129815638257) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129815639987) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833055) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833068) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833101) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833277) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833347) |
| multimodal-gen-test-4-npu-a3 (0) | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833355) |
| base-b-test-16-npu-a3 / run (0) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42811037470/job/129816833413) |


## [Run #42810523072](https://github.com/sgl-project/sglang/actions/runs/42810523072)
- **分支**: `clearing_console_output`
- **总耗时**: 41.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42810523072

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522667) |
| base-b-test-4-npu-a3 / run (0) | 8.7min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522846) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522667

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 279 秒，需查看该用例 Traceback 定位具体错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522846

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129810665517) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129810665535) |
| multimodal-gen-test-4-npu-a3 (0) | 38.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522518) |
| multimodal-gen-test-4-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522531) |
| multimodal-gen-test-1-npu-a3 (1) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522534) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522538) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522574) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522803) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811522857) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810523072/job/129811523204) |


## [Run #42810175143](https://github.com/sgl-project/sglang/actions/runs/42810175143)
- **分支**: `codex/bounded-lpm-window`
- **总耗时**: 27.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42810175143

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本返回退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429241) |
| base-b-test-4-npu-a3 / run (0) | 8.0min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 运行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429303) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回 exit code 5，表示 unittest 存在 errors，最常见为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），导致 0/8 用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429241

- **base-b-test-4-npu-a3 / run (0)**: base-b-test-4-npu-a3 作业中，test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行约 247 秒失败，返回退出码 1，2 个用例 0 通过。日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429303

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129809536266) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129809536273) |
| multimodal-gen-test-4-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429080) |
| base-b-test-8-npu-a3 / run (0) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429155) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429172) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429178) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429217) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42810175143/job/129810429467) |


## [Run #42807648592](https://github.com/sgl-project/sglang/actions/runs/42807648592)
- **分支**: `lsyin/sched-pr38`
- **总耗时**: 19.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42807648592

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349352) |
| base-b-test-4-npu-a3 / run (0) | 8.0min | 代码错误 | NPU DP attention 测试用例执行失败，退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349448) |
| base-b-test-1-npu-a3 / run (0) | 15.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349623) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349352

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例全部未通过，耗时约 263 秒，进程以 exit code 1 结束，需查看该用例的 Traceback 以定位具体错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349448

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349623

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129801157580) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129801157643) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349227) |
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349297) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349570) |
| base-b-test-4-npu-a3 / run (1) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802349992) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807648592/job/129802350709) |


## [Run #42807237864](https://github.com/sgl-project/sglang/actions/runs/42807237864)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 46.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42807237864

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 42.4min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 NPU 上 server 启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800765118) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见具体 Traceback；作业以失败结束并上传 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例运行中出错（可能 setUpClass 阶段 server 启动失败或进程被杀），需查看产物与完整日志确认。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800765118

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129799568008) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129799568198) |
| multimodal-gen-test-1-npu-a3 (1) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800764873) |
| multimodal-gen-test-1-npu-a3 (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800765021) |
| multimodal-gen-test-4-npu-a3 (1) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42807237864/job/129800765272) |


## [Run #42804078462](https://github.com/sgl-project/sglang/actions/runs/42804078462)
- **分支**: `lsyin/sched-pr38`
- **总耗时**: 26.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42804078462

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.4min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173270) |
| base-b-test-2-npu-a3 / run (0) | 5.1min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173302) |
| base-b-test-1-npu-a3 / run (0) | 22.1min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173703) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时约 272 秒后返回 exit code 1，需查看该用例 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173270

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，通常为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173302

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173703

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129788855297) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129788855360) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790172981) |
| multimodal-gen-test-4-npu-a3 (1) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173099) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173232) |
| base-b-test-16-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173283) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42804078462/job/129790173328) |


## [Run #42802563229](https://github.com/sgl-project/sglang/actions/runs/42802563229)
- **分支**: `fix/modelslim-w8a8-loading-clean`
- **总耗时**: 32.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42802563229

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924889) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时274秒，2个用例0通过，进程以退出码1结束，需查看该用例具体报错定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924889

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129783738533) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129783738573) |
| multimodal-gen-test-1-npu-a3 (0) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924530) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924600) |
| multimodal-gen-test-1-npu-a3 (1) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924634) |
| base-b-test-2-npu-a3 / run (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924787) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924802) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924817) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924829) |
| base-b-test-16-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924831) |
| multimodal-gen-test-4-npu-a3 (0) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42802563229/job/129784924835) |


## [Run #42800160081](https://github.com/sgl-project/sglang/actions/runs/42800160081)
- **分支**: `k3-pr1-quark-weights`
- **总耗时**: 35.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42800160081

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | NPU 测试用例 test_npu_mla_fia_hicache_bf16.py 退出码 5，setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379816) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379912) |

- **base-b-test-2-npu-a3 / run (0)**: 该用例返回 exit code 5，表示 unittest 存在 errors，通常为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL）。日志显示 0/8 通过，需查看 Traceback 确认具体异常。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379816

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的 Traceback，需查看该用例详细输出以定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379912

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129833219590) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129833226790) |
| multimodal-gen-test-1-npu-a3 (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379212) |
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379240) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379366) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379434) |
| base-b-test-8-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834379931) |
| base-b-test-16-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834380031) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834380087) |
| base-b-test-4-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42800160081/job/129834380145) |


## [Run #42798232485](https://github.com/sgl-project/sglang/actions/runs/42798232485)
- **分支**: `clearing_console_output`
- **总耗时**: 34.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42798232485

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.7min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093546) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093546

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129768986331) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129768986455) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093417) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093427) |
| multimodal-gen-test-1-npu-a3 (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093565) |
| multimodal-gen-test-1-npu-a3 (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093652) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093692) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093722) |
| multimodal-gen-test-4-npu-a3 (0) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093744) |
| base-b-test-4-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770093812) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42798232485/job/129770094045) |


## [Run #42796650355](https://github.com/sgl-project/sglang/actions/runs/42796650355)
- **分支**: `lsyin/k3-request-validation`
- **总耗时**: 24.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42796650355

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764931835) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764931956) |
| multimodal-gen-test-4-npu-a3 (0) | 19.8min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932027) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932201) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932296) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | 环境问题 | 自托管 runner 的容器执行失败，作业在运行第6个用例时被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932337) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约19分钟结束，退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764931835

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约21分钟后结束，退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764931956

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以unittest errors退出（码5），最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932027

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932201

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 266 秒，属测试用例本身执行报错。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932296

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器基础设施故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932337

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129763678168) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129763678244) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764931837) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932119) |
| base-b-test-16-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932165) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796650355/job/129764932290) |


## [Run #42796560160](https://github.com/sgl-project/sglang/actions/runs/42796560160)
- **分支**: `F4_support`
- **总耗时**: 71.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42796560160

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 56.8min | 环境问题 | diffusion-failures 目录无文件，测试用例未产生失败产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587079) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/'，说明测试未生成失败产物；结合退出码 5（unittest errors），最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例报错而非正常执行。
  - 失败用例: mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu, mova_360p_ti2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587079

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129763308208) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129763308421) |
| multimodal-gen-test-1-npu-a3 (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764586978) |
| multimodal-gen-test-1-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587001) |
| multimodal-gen-test-4-npu-a3 (1) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587100) |
| base-b-test-16-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587156) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587247) |
| base-b-test-8-npu-a3 / run (0) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587286) |
| base-b-test-4-npu-a3 / run (1) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129764587707) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129775310073) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129785479091) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42796560160/job/129785479137) |


## [Run #42795535677](https://github.com/sgl-project/sglang/actions/runs/42795535677)
- **分支**: `k3/hicache-mamba-size-gb`
- **总耗时**: 34.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42795535677

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.9min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847612) |
| base-b-test-4-npu-a3 / run (0) | 9.1min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847628) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847729) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44s），其余用例均通过，最终进程以退出码1结束，属该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847612

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，DP attention）后运行 321 秒返回退出码 1，2 个用例全部未通过；日志未给出具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847628

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847729

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129759861725) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129759861743) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847241) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847304) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847396) |
| multimodal-gen-test-1-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847432) |
| base-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847619) |
| base-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847668) |
| base-b-test-16-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42795535677/job/129760847767) |


## [Run #42794977664](https://github.com/sgl-project/sglang/actions/runs/42794977664)
- **分支**: `jeremyzhang866/fix-chunked-prefill-abort-commit`
- **总耗时**: 27.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42794977664

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.8min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095245) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095304) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时约285秒，2个用例0通过，进程以退出码1结束，需查看该用例具体 Traceback 定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095245

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095304

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129757945602) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129757945646) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759094867) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759094913) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095196) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095291) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095388) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42794977664/job/129759095425) |


## [Run #42789289538](https://github.com/sgl-project/sglang/actions/runs/42789289538)
- **分支**: `validate-top-logprobs-num`
- **总耗时**: 10.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42789289538

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789289538/job/129739583978) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/2用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789289538/job/129739583978

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789289538/job/129738716145) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789289538/job/129738716208) |
| base-b-test-4-npu-a3 / run (1) | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789289538/job/129739583762) |
| base-b-test-4-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789289538/job/129739583900) |


## [Run #42789214551](https://github.com/sgl-project/sglang/actions/runs/42789214551)
- **分支**: `fix-pyspy-ptrace-ci`
- **总耗时**: 30.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42789214551

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604487) |
| base-b-test-4-npu-a3 / run (0) | 8.8min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 运行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604688) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604487

- **base-b-test-4-npu-a3 / run (0)**: base-b-test-4-npu-a3 作业中，test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行约 300 秒失败，退出码 1，2 个用例 0 通过；日志未给出具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604688

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129738287316) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129738287832) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604386) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604411) |
| base-b-test-1-npu-a3 / run (0) | 26.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604501) |
| base-b-test-4-npu-a3 / run (1) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604585) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604635) |
| base-b-test-16-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789214551/job/129739604740) |


## [Run #42789068687](https://github.com/sgl-project/sglang/actions/runs/42789068687)
- **分支**: `fix/xpu-whisper-w8a8-int8`
- **总耗时**: 38.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42789068687

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.1min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751040) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751101) |
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751365) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751040

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时45秒），其余用例均通过，因此该用例失败导致进程退出码为1。日志未给出具体 Traceback，需查看该用例详细输出以定位是断言失败还是 setUpClass 阶段 server 启动异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751101

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时约 266 秒，需查看该用例 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751365

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129737772889) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129737772905) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738750736) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738750819) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738750846) |
| multimodal-gen-test-4-npu-a3 (0) | 35.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751006) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751075) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751111) |
| base-b-test-16-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789068687/job/129738751205) |


## [Run #42789061908](https://github.com/sgl-project/sglang/actions/runs/42789061908)
- **分支**: `dsv4_hisparse_dspark`
- **总耗时**: 24.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42789061908

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808076) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808194) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808076

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 266 秒；日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808194

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129737747385) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129737747436) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738807972) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808091) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808187) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808273) |
| base-b-test-16-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808298) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42789061908/job/129738808461) |


## [Run #42787658983](https://github.com/sgl-project/sglang/actions/runs/42787658983)
- **分支**: `dark/carv2-dpx-pair-header`
- **总耗时**: 36.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42787658983

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.2min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039336) |
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039385) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 52s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039336

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时约 269 秒，2 个用例 0 通过，进程以 exit code 1 结束，需查看该用例 Traceback 定位具体报错。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039385

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129733043127) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129733043208) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734038996) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039013) |
| multimodal-gen-test-4-npu-a3 (0) | 33.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039053) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039157) |
| base-b-test-16-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039176) |
| base-b-test-4-npu-a3 / run (1) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039463) |
| base-b-test-2-npu-a3 / run (0) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039804) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42787658983/job/129734039940) |


## [Run #42783582113](https://github.com/sgl-project/sglang/actions/runs/42783582113)
- **分支**: `feat/hccl-clean-new`
- **总耗时**: 36.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42783582113

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.0min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788554963) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时约 246 秒。日志未显示具体 Traceback，需查看该用例详细输出定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788554963

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129787279421) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129787279463) |
| multimodal-gen-test-1-npu-a3 (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788554821) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788554850) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788554876) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788554965) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788555021) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788555036) |
| base-b-test-1-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788555056) |
| base-b-test-2-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788555142) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783582113/job/129788555740) |


## [Run #42783271713](https://github.com/sgl-project/sglang/actions/runs/42783271713)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 10.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42783271713

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 4.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719219831) |
| multimodal-gen-test-1-npu-a3 (1) | 7.5min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719219868) |
| multimodal-gen-test-4-npu-a3 (0) | 7.8min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719219883) |
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220030) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220087) |
| base-b-test-1-npu-a3 / run (0) | 7.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220168) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型加载阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220190) |
| multimodal-gen-test-4-npu-a3 (1) | 7.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220209) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片时中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220232) |
| base-b-test-4-npu-a3 / run (1) | 7.8min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220257) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见用例收集失败，退出码5表示 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。diffusion-failures/ 无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719219831

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业以 unittest errors（退出码5）失败，最常见原因是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719219868

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示用例退出码5（FAILED errors=N），常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）；且未生成 diffusion-failures/ 目录，无产物上传。需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719219883

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中真实Traceback确认。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220030

- **base-b-test-8-npu-a3 / run (0)**: 日志显示测试请求已返回 200 OK，随后报错 'Executing the custom container implementation failed'，属于 runner 容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220087

- **base-b-test-1-npu-a3 / run (0)**: 日志显示测试用例执行中报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220168

- **base-b-test-16-npu-a3 / run (0)**: 日志报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 ModelSlimW8A8Int8 模型加载过程中，属 runner/容器环境异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220190

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产出结果。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220209

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型分片加载到 59% 时出现 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码错误；建议联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220232

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时/基础设施故障，并非用例断言失败；此前 HiCache 请求均正常，随后作业直接报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129719220257

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129718373529) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42783271713/job/129718373619) |


## [Run #42782980150](https://github.com/sgl-project/sglang/actions/runs/42782980150)
- **分支**: `feature/spark2_5_dspark`
- **总耗时**: 36.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42782980150

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.2min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468488) |
| base-b-test-2-npu-a3 / run (0) | 5.1min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468667) |
| base-b-test-1-npu-a3 / run (0) | 22.4min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468731) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，--enable-dp-attention）后运行失败，耗时约 264 秒，退出码 1，2 个用例 0 通过。日志未显示具体 Traceback，需查看该用例详细输出定位 server 启动或推理报错。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468488

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468667

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过，该用例失败使进程以退出码1结束。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468731

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129717426880) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129717426883) |
| multimodal-gen-test-1-npu-a3 (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468249) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468297) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468324) |
| multimodal-gen-test-4-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468339) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468456) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468485) |
| base-b-test-8-npu-a3 / run (0) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782980150/job/129718468558) |


## [Run #42782835433](https://github.com/sgl-project/sglang/actions/runs/42782835433)
- **分支**: `qwen38-ple-mm-placeholder-ids`
- **总耗时**: 15.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42782835433

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.3min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129718211143) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时331秒返回退出码1，测试汇总0/1通过；日志未显示具体 Traceback，需查看该用例详细输出定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129718211143

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129717320220) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129717320252) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129718210495) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129718210582) |
| base-b-test-4-npu-a3 / run (1) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42782835433/job/129718211197) |


## [Run #42781532860](https://github.com/sgl-project/sglang/actions/runs/42781532860)
- **分支**: `lsyin/k3-tool-call-parsing`
- **总耗时**: 12.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42781532860

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 5.5min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132575) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132611) |
| multimodal-gen-test-1-npu-a3 (1) | 5.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132666) |
| multimodal-gen-test-4-npu-a3 (1) | 5.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133026) |
| base-b-test-1-npu-a3 / run (0) | 9.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133029) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133048) |
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU dp_attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133056) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在测试启动阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133066) |
| base-b-test-16-npu-a3 / run (0) | 9.2min | 环境问题 | 自定义容器执行失败，作业在启动阶段异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133072) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业约5分钟后结束，未找到 diffusion-failures/ 产物，说明用例未正常执行；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132575

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产出结果；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132611

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行异常。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132666

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133026

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在执行第3个测试文件 test_npu_autoround_moe.py 时，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133029

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133048

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 266 秒，属测试用例本身执行错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133056

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 NPU 内存分配告警后报错“Executing the custom container implementation failed”，属 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133066

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器启动/运行环境故障，非用例代码问题；随后进入清理流程，未出现测试断言或精度错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721133072

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129720260286) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129720260309) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781532860/job/129721132981) |


## [Run #42781331186](https://github.com/sgl-project/sglang/actions/runs/42781331186)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 44.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42781331186

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | 环境问题 | 自托管 runner 的 k8s 容器实现异常，临时文件丢失导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998661) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998768) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998807) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998815) |
| base-b-test-4-npu-a3 / run (1) | 14.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998827) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998975) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，随后 runner 报 ENOENT 打开 _runner_file_commands 下 .nfs 临时文件失败，Node 进程退出码 1，属 runner 环境/文件系统问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998661


- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过；该用例失败使进程以 exit code 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998807

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998815

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998827

- **base-b-test-4-npu-a3 / run (0)**: base-b-test-4-npu-a3 作业中 test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时约 257 秒，导致作业失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998975

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712126647) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712126680) |
| multimodal-gen-test-4-npu-a3 (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998550) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998628) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998668) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42781331186/job/129712998984) |


## [Run #42780359233](https://github.com/sgl-project/sglang/actions/runs/42780359233)
- **分支**: `upr/xpu-fp8-w8a16-linear-v3`
- **总耗时**: 39.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42780359233

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.2min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812907) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812919) |
| base-b-test-2-npu-a3 / run (0) | 5.3min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812926) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812950) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812976) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时约 312 秒，2 个用例 0 通过，进程以 exit code 1 结束，导致作业失败。日志未显示具体 Traceback，需查看该用例详细输出定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812907


- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812926


- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 41s），其余用例均通过，最终进程以退出码 1 结束，属该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812976

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129708830617) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129708830905) |
| multimodal-gen-test-1-npu-a3 (1) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812783) |
| multimodal-gen-test-4-npu-a3 (0) | 36.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812792) |
| multimodal-gen-test-1-npu-a3 (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812802) |
| multimodal-gen-test-4-npu-a3 (1) | 25.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812908) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42780359233/job/129709812983) |


## [Run #42779628867](https://github.com/sgl-project/sglang/actions/runs/42779628867)
- **分支**: `fix/prefill-delayer-queue-trigger`
- **总耗时**: 24.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42779628867

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929896843) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 44s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929896843

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929899250) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929899396) |
| multimodal-gen-test-1-npu-a3 (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929899662) |
| base-b-test-16-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929899913) |
| base-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929900178) |
| base-b-test-4-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929900215) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929900405) |
| multimodal-gen-test-4-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929900638) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929900694) |
| base-b-test-2-npu-a3 / run (0) | 26.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929901427) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42779628867/job/129929901581) |


## [Run #42778998981](https://github.com/sgl-project/sglang/actions/runs/42778998981)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 18.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42778998981

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 13.0min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398468) |
| multimodal-gen-test-1-npu-a3 (1) | 13.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398507) |
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本返回退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398530) |
| base-b-test-4-npu-a3 / run (0) | 8.6min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398677) |
| multimodal-gen-test-4-npu-a3 (0) | 15.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398751) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | 环境问题 | Scheduler watchdog 超时，容器执行失败，疑似 NPU 进程卡死或 host 资源异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398756) |
| multimodal-gen-test-4-npu-a3 (1) | 14.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398846) |
| base-b-test-1-npu-a3 / run (0) | 14.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705399053) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 路径，说明测试用例在 setUpClass 阶段即失败（退出码 5 对应 unittest errors），常见原因为 sglang server 启动失败（host OOM 或进程被 SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398468

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示用例以 errors 结束（退出码5），且未生成 diffusion-failures/ 目录产物，说明测试在 setUpClass 启动 server 阶段即失败，可能为 host OOM 或进程被 SIGKILL，需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398507

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回 exit code 5，表示 unittest 存在 errors，最常见为 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致 0/8 用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398530

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时约 294 秒，需查看该脚本内 Traceback 定位具体错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398677

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产生输出。退出码5表示unittest存在errors，最常见为setUpClass阶段server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398751

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP15 EP15 的 Scheduler watchdog timeout（watchdog_timeout=300, soft=True），随后报错 'Executing the custom container implementation failed'，属于运行环境/容器层面的异常，而非用例断言失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398756

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约14分钟结束，退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398846

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705399053

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129704367891) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129704367922) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398567) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778998981/job/129705398604) |


## [Run #42778916692](https://github.com/sgl-project/sglang/actions/runs/42778916692)
- **分支**: `ecao/xpu_mxfp8_scaled_mm_v2`
- **总耗时**: 37.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42778916692

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.6min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031323) |
| base-b-test-1-npu-a3 / run (0) | 25.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031420) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031592) |
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031687) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行84秒后返回退出码1，测试汇总0/1通过。日志未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031323

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过，因此该用例失败使进程以退出码 1 结束。日志未给出具体 Traceback，需查看该用例详细输出以定位原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031420

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031592

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时 264 秒后返回 exit code 1，需查看该脚本 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031687

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129704086798) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129704086845) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031183) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031209) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031255) |
| multimodal-gen-test-4-npu-a3 (0) | 33.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031273) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031432) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42778916692/job/129705031747) |


## [Run #42776748416](https://github.com/sgl-project/sglang/actions/runs/42776748416)
- **分支**: `hicache-evict-headroom`
- **总耗时**: 36.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42776748416

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.4min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758488) |
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758517) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758526) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758613) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.87秒后返回退出码1，测试汇总0/1通过。日志省略了具体Traceback，需查看该用例完整输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758488

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758517

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_basic_sanity_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758526

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758613

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697092157) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697092207) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758373) |
| multimodal-gen-test-4-npu-a3 (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758540) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758551) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758567) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758589) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42776748416/job/129697758652) |


## [Run #42775218652](https://github.com/sgl-project/sglang/actions/runs/42775218652)
- **分支**: `pr/muse-spark-rocm-sa-1027`
- **总耗时**: 35.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42775218652

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.8min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035017) |
| base-b-test-4-npu-a3 / run (0) | 8.5min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035019) |
| base-b-test-16-npu-a3 / run (0) | 5.6min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035038) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035043) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过，最终进程以退出码1结束，属于该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035017

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时约 267 秒后返回 exit code 1，需查看该用例 Traceback 定位具体报错。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035019

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83秒后返回退出码1，测试汇总0/1通过。日志未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035038

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回exit code 5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035043

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129692143473) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129692143506) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693034791) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693034813) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693034885) |
| multimodal-gen-test-4-npu-a3 (0) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693034886) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035000) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42775218652/job/129693035024) |


## [Run #42774974433](https://github.com/sgl-project/sglang/actions/runs/42774974433)
- **分支**: `fix/responses-reasoning-effort`
- **总耗时**: 32.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42774974433

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.8min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157159) |
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157254) |
| base-b-test-1-npu-a3 / run (0) | 24.0min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157295) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 代码错误 | NPU speculative MoE a2a backend 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157367) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时 294 秒后返回 exit code 1，需查看该用例具体 Traceback 定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157159

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，通常为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157254

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43 秒），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157295

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行 84 秒后返回退出码 1，测试汇总 0/1 通过。日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157367

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129691394540) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129691394586) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692156979) |
| multimodal-gen-test-1-npu-a3 (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157055) |
| multimodal-gen-test-4-npu-a3 (0) | 29.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157068) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157138) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157140) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42774974433/job/129692157270) |


## [Run #42773791885](https://github.com/sgl-project/sglang/actions/runs/42773791885)
- **分支**: `test/glm5-3-eplb-gpqa`
- **总耗时**: 5.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42773791885

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.0min | 环境问题 | 精度测试用例退出码5，setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817475433) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: test_npu_moonlight_16b_a3b_bf16_1p_gsm8k.py 返回exit code 5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL）。后续shell脚本因变量含换行报integer expression expected，属连带错误。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817475433

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817475537) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817475722) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817477343) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773791885/job/129817477621) |


## [Run #42773412162](https://github.com/sgl-project/sglang/actions/runs/42773412162)
- **分支**: `fix/linker-mooncake-lease-renewal`
- **总耗时**: 12.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42773412162

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129687289115) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致3个用例全部未通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129687289115

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129686402324) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129686402374) |
| base-b-test-4-npu-a3 / run (1) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129687289139) |
| base-b-test-1-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129687289171) |
| base-b-test-4-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42773412162/job/129687289231) |


## [Run #42772832351](https://github.com/sgl-project/sglang/actions/runs/42772832351)
- **分支**: `feat/mm-routing-label-spans`
- **总耗时**: 34.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42772832351

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443349) |
| base-b-test-4-npu-a3 / run (0) | 8.4min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443431) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443456) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败导致unittest报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443468) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.7秒后返回退出码1，测试汇总0/1通过。日志省略了具体Traceback，需查看该用例完整输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443349

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时约 278 秒后返回 exit code 1，需查看该用例 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443431

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 44s），其余用例均通过，因此该用例失败导致进程退出码为 1；日志未给出具体 Traceback，需查看该用例输出以定位原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443456

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443468

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129684559605) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129684559748) |
| multimodal-gen-test-4-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443213) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443262) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443267) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443274) |
| base-b-test-4-npu-a3 / run (1) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443415) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42772832351/job/129685443523) |


## [Run #42771038056](https://github.com/sgl-project/sglang/actions/runs/42771038056)
- **分支**: `openai-tokenize-api`
- **总耗时**: 19.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42771038056

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 16.4min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569408) |
| multimodal-gen-test-1-npu-a3 (1) | 16.3min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569417) |
| multimodal-gen-test-4-npu-a3 (1) | 16.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569422) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569458) |
| base-b-test-1-npu-a3 / run (0) | 16.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569487) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569499) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569531) |
| base-b-test-4-npu-a3 / run (0) | 8.0min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569576) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成该目录，可能用例未执行或提前失败；日志中未见具体 Traceback，需查看省略部分确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569408

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试未产出失败样本；结合退出码 5 常见于 setUpClass 中 sglang server 启动失败（如 OOM/SIGKILL），但日志被省略，无法确认具体 Traceback，需查看中间段真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569417

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569422

- **multimodal-gen-test-1-npu-a3 (0)**: 日志末尾显示 diffusion-failures/ 目录无文件可上传，说明用例未正常产出失败产物；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569458

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner/容器环境故障，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569487

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.71秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该用例Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569499

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569531

- **base-b-test-4-npu-a3 / run (0)**: base-b-test-4-npu-a3 作业中 test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 267s，导致作业失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569576

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129678794665) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129678794748) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569497) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42771038056/job/129679569516) |


## [Run #42770061389](https://github.com/sgl-project/sglang/actions/runs/42770061389)
- **分支**: `hicache/scheduler-thread-agreement`
- **总耗时**: 13.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42770061389

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129676703486) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129676703486

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129675660894) |
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129675660964) |
| base-b-test-1-npu-a3 / run (0) | 6.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129676703415) |
| base-b-test-4-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129676703483) |
| base-b-test-4-npu-a3 / run (1) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42770061389/job/129676703557) |


## [Run #42767892232](https://github.com/sgl-project/sglang/actions/runs/42767892232)
- **分支**: `hicache/scheduler-thread-bounded-calls`
- **总耗时**: 23.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42767892232

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561066) |
| base-b-test-4-npu-a3 / run (0) | 7.9min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561111) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致6个用例全部未通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561066

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时约 240 秒后返回退出码 1，测试汇总 0/1 通过；日志未显示具体 Traceback，需查看该用例详细输出定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561111

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129668747255) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129668747572) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669560869) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669560991) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561087) |
| base-b-test-4-npu-a3 / run (1) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561096) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767892232/job/129669561181) |


## [Run #42767876044](https://github.com/sgl-project/sglang/actions/runs/42767876044)
- **分支**: `hicache/scheduler-thread-agreement`
- **总耗时**: 12.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42767876044

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.1min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129669475176) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129669475176

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129668681880) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129668682094) |
| base-b-test-4-npu-a3 / run (1) | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129669475206) |
| base-b-test-1-npu-a3 / run (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129669475226) |
| base-b-test-4-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767876044/job/129669475244) |


## [Run #42767501673](https://github.com/sgl-project/sglang/actions/runs/42767501673)
- **分支**: `stmatengss/mooncake-kvcache-dtype-cb2a`
- **总耗时**: 34.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42767501673

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.0min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361140) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361150) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361226) |
| base-b-test-16-npu-a3 / run (0) | 5.0min | 代码错误 | NPU 投机推理 MoE a2a 后端测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361273) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 41s），其余用例均通过，该用例失败使进程以退出码 1 结束。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361140

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时约 269 秒后返回 exit code 1，需查看该脚本 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361150

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，unittest存在errors，通常为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361226

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行 83 秒后返回退出码 1，测试汇总 0/1 通过；日志省略段未显示具体 Traceback，需查看该用例完整输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361273

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129667485891) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129667486009) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361032) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361077) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361085) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361113) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361154) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767501673/job/129668361186) |


## [Run #42767216558](https://github.com/sgl-project/sglang/actions/runs/42767216558)
- **分支**: `feat/qsa-cache-sharding`
- **总耗时**: 26.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42767216558

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本返回退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778941895) |
| base-b-test-1-npu-a3 / run (0) | 24.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778941929) |
| base-b-test-4-npu-a3 / run (0) | 8.9min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778942111) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过，作业最终exit code 1。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778941895

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过，最终进程以退出码1结束，属于该用例本身执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778941929

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，--enable-dp-attention）后运行约 305 秒返回退出码 1，测试汇总 0/2 通过，属用例本身失败，需查看该用例 Traceback 定位具体错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778942111

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-16-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778941800) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778942816) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778943421) |
| multimodal-gen-test-1-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778943669) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778943779) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778943826) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778944508) |
| multimodal-gen-test-4-npu-a3 (0) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778945051) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42767216558/job/129778945269) |


## [Run #42766376254](https://github.com/sgl-project/sglang/actions/runs/42766376254)
- **分支**: `comm/gated-allgather`
- **总耗时**: 33.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42766376254

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.5min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605142) |
| base-b-test-16-npu-a3 / run (0) | 5.1min | 代码错误 | NPU投机推理MoE A2A后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605200) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败导致unittest报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605219) |
| base-b-test-4-npu-a3 / run (0) | 8.7min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 运行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605251) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时41秒），其余用例均通过，最终进程以退出码1结束。日志未给出该用例的具体 Traceback，需查看该用例输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605142

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83秒后返回退出码1，测试汇总0/1通过。日志省略了具体Traceback，需查看该用例详细报错定位是server启动失败还是断言失败。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605200

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），8个用例0通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605219

- **base-b-test-4-npu-a3 / run (0)**: base-b-test-4-npu-a3 作业中，test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行约 271 秒失败，返回退出码 1，2 个用例 0 通过；日志省略了具体 Traceback，需查看该用例完整输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605251

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129663992192) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129663992233) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605094) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605095) |
| multimodal-gen-test-4-npu-a3 (0) | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605164) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605189) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605210) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766376254/job/129664605242) |


## [Run #42766004150](https://github.com/sgl-project/sglang/actions/runs/42766004150)
- **分支**: `feat/npu-layernorm-sp`
- **总耗时**: 15.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42766004150

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.7min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787826793) |
| base-b-test-4-npu-a3 / run (0) | 8.7min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787827251) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787826793

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时 286 秒后返回 exit code 1，需查看该用例 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787827251

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787826673) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787826690) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787827089) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787827706) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787828395) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787828501) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787829259) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42766004150/job/129787829429) |


## [Run #42765581304](https://github.com/sgl-project/sglang/actions/runs/42765581304)
- **分支**: `model-serve/encoder-sep-truncation`
- **总耗时**: 31.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42765581304

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 7.6min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696539) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696568) |
| base-b-test-16-npu-a3 / run (0) | 5.0min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696654) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时 247 秒后退出码 1，需查看该用例 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696539

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，通常为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696568

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.79秒后返回退出码1，测试汇总0/1通过。日志省略部分未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696654

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129661366916) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129661366994) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696266) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696331) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696393) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696463) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765581304/job/129663696535) |


## [Run #42765547620](https://github.com/sgl-project/sglang/actions/runs/42765547620)
- **分支**: `siju/xpu-mtp-spec-fixes`
- **总耗时**: 9.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42765547620

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | K8s 服务账号权限不足，无法创建 selfsubjectaccessreviews，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129662023694) |

- **base-b-test-2-npu-a3 / run (0)**: runner-service-account 缺少 authorization.k8s.io 的 selfsubjectaccessreviews 创建权限，K8s API 返回 403 Forbidden，重试 4 次仍失败，作业在启动阶段即中止，属 CI 基础设施权限配置问题。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129662023694

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129661271018) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129661271062) |
| base-b-test-1-npu-a3 / run (0) | 6.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129662023703) |
| base-b-test-4-npu-a3 / run (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129662023721) |
| base-b-test-4-npu-a3 / run (1) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765547620/job/129662023733) |


## [Run #42765132333](https://github.com/sgl-project/sglang/actions/runs/42765132333)
- **分支**: `feat/mlu-paged-gqa-fused-ops`
- **总耗时**: 40.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42765132333

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671757) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671791) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE A2A后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671843) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671757

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时约275秒，2个用例0通过，进程以退出码1结束，需查看该脚本内部 Traceback 定位具体错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671791

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.91秒后返回退出码1，测试汇总0/1通过。日志未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671843

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129659850053) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129659850119) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671630) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671635) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671648) |
| multimodal-gen-test-4-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671672) |
| base-b-test-1-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671748) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671750) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765132333/job/129660671758) |


## [Run #42765036878](https://github.com/sgl-project/sglang/actions/runs/42765036878)
- **分支**: `amd/hip-gdn-prefill-layout`
- **总耗时**: 41.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42765036878

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 32.2min | 其他 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 退出码为 1，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129660205409) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 3 个性能用例中 1 个通过、1 个失败（qwen3_6_27b 1024x1024 用例 exit code 1，耗时 972s），日志省略部分未显示具体 Traceback，需查看该用例详细日志确认是性能不达标还是 server 启动异常。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129660205409

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129659556056) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129659556167) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42765036878/job/129660205655) |


## [Run #42764382060](https://github.com/sgl-project/sglang/actions/runs/42764382060)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 36.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42764382060

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.1min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159315) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159347) |
| base-b-test-4-npu-a3 / run (0) | 8.0min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159389) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159315

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 50s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159347

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，2 个用例 0 通过，耗时 249 秒后返回 exit code 1，需查看该用例 Traceback 定位具体报错。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159389

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129657427440) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129657427583) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159220) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159265) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159288) |
| multimodal-gen-test-4-npu-a3 (0) | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159304) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159321) |
| base-b-test-16-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159328) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764382060/job/129658159385) |


## [Run #42764195582](https://github.com/sgl-project/sglang/actions/runs/42764195582)
- **分支**: `dark/carv2-dpx-pair-header`
- **总耗时**: 35.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42764195582

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.4min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489053) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489060) |
| base-b-test-1-npu-a3 / run (0) | 28.7min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489103) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489167) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该脚本Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489053

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489060

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过，最终进程退出码为1。日志未给出该用例的具体 Traceback，需查看该用例详细输出以定位根因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489103

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489167

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129656828850) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129656828879) |
| multimodal-gen-test-1-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657488810) |
| multimodal-gen-test-1-npu-a3 (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657488853) |
| multimodal-gen-test-4-npu-a3 (0) | 32.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657488942) |
| multimodal-gen-test-4-npu-a3 (1) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489010) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489127) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42764195582/job/129657489255) |


## [Run #42763871106](https://github.com/sgl-project/sglang/actions/runs/42763871106)
- **分支**: `comm/gated-allgather`
- **总耗时**: 24.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42763871106

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | 环境问题 | 测试用例执行失败，diffusion-failures 目录无产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656533888) |
| multimodal-gen-test-4-npu-a3 (0) | 20.8min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656533901) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534050) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534066) |
| base-b-test-4-npu-a3 / run (0) | 8.0min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534088) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534106) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例退出码 5（unittest errors），且上传产物时提示 diffusion-failures/ 无文件，说明测试未正常产出失败样本，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656533888

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact，说明测试用例执行阶段出错。退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656533901

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致8个用例全部未通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534050

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行约84秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该用例Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534066

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，DP attention）后运行 261 秒返回退出码 1，2 个用例全部失败，属测试用例/代码执行错误，非超时或环境问题。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534088

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境问题，非用例代码失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534106

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129655783888) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129655783948) |
| multimodal-gen-test-1-npu-a3 (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656533876) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656533906) |
| base-b-test-4-npu-a3 / run (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534077) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763871106/job/129656534119) |


## [Run #42763383553](https://github.com/sgl-project/sglang/actions/runs/42763383553)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 42.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42763383553

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.4min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925151) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925205) |
| base-b-test-4-npu-a3 / run (0) | 8.6min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925268) |
| base-b-test-16-npu-a3 / run (0) | 5.6min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925347) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时42秒），其余用例均通过，最终进程以退出码1结束，属于该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925151

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925205

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，--enable-cuda-graph --device npu）后运行失败，耗时 284s 返回 exit code 1，2 个用例 0 通过；日志未给出具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925268

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83秒后返回退出码1，测试汇总0/1通过。日志省略了具体Traceback，需查看该用例详细输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925347

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654210675) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654210773) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925061) |
| multimodal-gen-test-1-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925116) |
| multimodal-gen-test-1-npu-a3 (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925133) |
| multimodal-gen-test-4-npu-a3 (0) | 38.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925182) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925247) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763383553/job/129654925310) |


## [Run #42763321181](https://github.com/sgl-project/sglang/actions/runs/42763321181)
- **分支**: `feat/mamba-hybrid-state-eviction`
- **总耗时**: 27.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42763321181

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.7min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757066871) |
| base-b-test-1-npu-a3 / run (0) | 26.9min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757066928) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757066871

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时44秒），其余用例均通过，最终进程以退出码1结束，属于该用例执行失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757066928

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757066988) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757068355) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757068499) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757068926) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757068990) |
| multimodal-gen-test-1-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757069661) |
| multimodal-gen-test-4-npu-a3 (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757069739) |
| base-b-test-4-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757069817) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757069973) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42763321181/job/129757070003) |


## [Run #42762751287](https://github.com/sgl-project/sglang/actions/runs/42762751287)
- **分支**: `fix/hisparse-cpu-copy-retraction`
- **总耗时**: 30.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42762751287

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.5min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958160) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 282 秒。日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958160

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652235839) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652235918) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652957926) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652957970) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958073) |
| base-b-test-2-npu-a3 / run (0) | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958087) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958097) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958121) |
| base-b-test-16-npu-a3 / run (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42762751287/job/129652958220) |


## [Run #42758953221](https://github.com/sgl-project/sglang/actions/runs/42758953221)
- **分支**: `page-unified/mooncake-storage`
- **总耗时**: 13.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42758953221

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.3min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129640769182) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 运行61秒后返回退出码5，按约定表示unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129640769182

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129639968643) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129639968673) |
| base-b-test-1-npu-a3 / run (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129640769126) |
| base-b-test-4-npu-a3 / run (1) | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129640769128) |
| base-b-test-4-npu-a3 / run (0) | 9.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758953221/job/129640769140) |


## [Run #42758944406](https://github.com/sgl-project/sglang/actions/runs/42758944406)
- **分支**: `linear-attn-prefill-cp-ulysses`
- **总耗时**: 35.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42758944406

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.3min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745552) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致3个用例全部未通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745552

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129639922014) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129639922095) |
| multimodal-gen-test-1-npu-a3 (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745417) |
| multimodal-gen-test-4-npu-a3 (1) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745448) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745458) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745496) |
| base-b-test-4-npu-a3 / run (0) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745524) |
| base-b-test-4-npu-a3 / run (1) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745610) |
| base-b-test-1-npu-a3 / run (0) | 6.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758944406/job/129640745655) |


## [Run #42758762191](https://github.com/sgl-project/sglang/actions/runs/42758762191)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 37.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42758762191

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 7.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101519) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101522) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101591) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101619) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101519

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行约83秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该用例Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101522

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101591

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101619

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129639347948) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129639347975) |
| multimodal-gen-test-1-npu-a3 (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101402) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101414) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101453) |
| multimodal-gen-test-4-npu-a3 (0) | 34.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101462) |
| base-b-test-4-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101579) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758762191/job/129640101588) |


## [Run #42758401032](https://github.com/sgl-project/sglang/actions/runs/42758401032)
- **分支**: `kvshard/qwen38-flash-next`
- **总耗时**: 26.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42758401032

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 8.1min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950953) |
| base-b-test-2-npu-a3 / run (0) | 6.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950959) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，DP attention）后运行约 262 秒返回退出码 1，2 个用例 0 通过，导致作业失败；日志未显示具体 Traceback，需查看该用例详细输出定位 server 启动或断言错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950953

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950959

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638206493) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638206533) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950768) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950806) |
| base-b-test-1-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950836) |
| base-b-test-16-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950900) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950951) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758401032/job/129638950976) |


## [Run #42758071741](https://github.com/sgl-project/sglang/actions/runs/42758071741)
- **分支**: `lsyin/sched-dspark-rows`
- **总耗时**: 31.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42758071741

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.5min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060835) |
| base-b-test-4-npu-a3 / run (0) | 12.7min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060867) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行84秒后返回退出码1，测试汇总0/1通过。日志省略部分未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060835

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时 411 秒，退出码 1，2 个用例全部未通过；日志未显示具体 Traceback，需查看该用例详细输出以定位是服务启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060867

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129637254962) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129637254970) |
| multimodal-gen-test-4-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060685) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060721) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060791) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060805) |
| base-b-test-4-npu-a3 / run (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060809) |
| base-b-test-2-npu-a3 / run (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42758071741/job/129638060815) |


## [Run #42757697151](https://github.com/sgl-project/sglang/actions/runs/42757697151)
- **分支**: `openai-tokenize-api`
- **总耗时**: 34.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42757697151

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693216) |
| base-b-test-16-npu-a3 / run (0) | 5.7min | 代码错误 | NPU投机推理测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693229) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693270) |
| base-b-test-4-npu-a3 / run (0) | 8.8min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 运行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693328) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693216

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行约83秒后返回退出码1，测试汇总0/1通过，导致作业失败；日志未显示具体Traceback，需查看该用例详细输出定位根因。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693229

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出以定位是断言失败还是 setUpClass 阶段 server 启动异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693270

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在 NPU 上启动 server 后执行失败，耗时约 265 秒，2 个用例 0 通过，进程以 exit code 1 结束，导致作业失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693328

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129635973145) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129635973241) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636692995) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693050) |
| multimodal-gen-test-4-npu-a3 (0) | 31.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693081) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693103) |
| base-b-test-4-npu-a3 / run (1) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693175) |
| base-b-test-8-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757697151/job/129636693196) |


## [Run #42757391891](https://github.com/sgl-project/sglang/actions/runs/42757391891)
- **分支**: `refactor/graph-break-recorder`
- **总耗时**: 44.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42757391891

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593760) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593790) |
| base-b-test-4-npu-a3 / run (0) | 8.5min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593805) |
| base-b-test-1-npu-a3 / run (0) | 26.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593824) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593760

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行约84秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该用例Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593790

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 263 秒，需查看该用例具体 Traceback 定位原因。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593805

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，因此该用例失败导致进程退出码为 1；日志未给出具体 Traceback，需查看该用例详细输出。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593824

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129655929865) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129655929943) |
| multimodal-gen-test-1-npu-a3 (1) | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593686) |
| multimodal-gen-test-4-npu-a3 (1) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593695) |
| multimodal-gen-test-4-npu-a3 (0) | 40.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593726) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593737) |
| multimodal-gen-test-1-npu-a3 (0) | 26.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593739) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757391891/job/129656593809) |


## [Run #42757218854](https://github.com/sgl-project/sglang/actions/runs/42757218854)
- **分支**: `elastic-base`
- **总耗时**: 29.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42757218854

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.9min | 环境问题 | 测试脚本返回退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562589) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 代码错误 | NPU投机推理测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562718) |
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU DP attention 测试脚本 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562753) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 退出码5表示unittest存在errors，通常为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过，作业以exit code 1结束。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562589

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行约94秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该脚本Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562718

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，耗时约 267 秒，2 个用例 0 通过，进程以退出码 1 结束，导致作业失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562753

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129676635797) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129676635837) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562520) |
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562569) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562679) |
| base-b-test-1-npu-a3 / run (0) | 25.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562725) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42757218854/job/129677562905) |


## [Run #42755788989](https://github.com/sgl-project/sglang/actions/runs/42755788989)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 35.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42755788989

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.1min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645760) |
| base-b-test-4-npu-a3 / run (0) | 9.2min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645788) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645801) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时52秒），其余用例均通过；该用例失败使进程以退出码1结束，具体报错需查看该用例日志。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645760

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行约315秒后返回退出码1，2个用例0通过，日志未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645788

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645801

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129629870278) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129629870320) |
| multimodal-gen-test-4-npu-a3 (0) | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645617) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645622) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645627) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645659) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645776) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645901) |
| base-b-test-16-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42755788989/job/129630645947) |


## [Run #42753567883](https://github.com/sgl-project/sglang/actions/runs/42753567883)
- **分支**: `elastic-base`
- **总耗时**: 25.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42753567883

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713004) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713013) |
| base-b-test-4-npu-a3 / run (0) | 9.6min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713077) |
| base-b-test-16-npu-a3 / run (0) | 21.5min | 环境问题 | 测试用例全部通过，但容器执行结束时自定义容器实现失败，导致作业报错。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713103) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713004

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_gptq_moe.py, npu_gptq_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713013

- **base-b-test-4-npu-a3 / run (0)**: 日志显示该测试文件返回 exit code 1，测试汇总 0/2 通过，耗时约 330 秒后失败；日志省略了具体 Traceback，无法确定根因，需查看完整日志确认是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713077

- **base-b-test-16-npu-a3 / run (0)**: 日志显示测试 1/1 通过，随后报错“Executing the custom container implementation failed”，属于自托管 runner 的容器执行环境问题，并非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713103

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129622763223) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129622763272) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623712882) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623712920) |
| base-b-test-4-npu-a3 / run (1) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713111) |
| base-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42753567883/job/129623713122) |


## [Run #42752868509](https://github.com/sgl-project/sglang/actions/runs/42752868509)
- **分支**: `wuyaole/fix-prefill-reservation-budget`
- **总耗时**: 26.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42752868509

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363886) |
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU speculative MoE a2a backend 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363967) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363886

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行 83 秒后返回 exit code 1，测试汇总 0/1 通过，属用例本身失败，需查看该脚本 Traceback 定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363967

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129620491433) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129620491481) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363806) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363832) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363871) |
| base-b-test-1-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363872) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363882) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42752868509/job/129621363891) |


## [Run #42751910982](https://github.com/sgl-project/sglang/actions/runs/42751910982)
- **分支**: `dark/carv2-dpx-pair-header`
- **总耗时**: 36.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42751910982

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111782) |
| base-b-test-4-npu-a3 / run (1) | 14.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111826) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111879) |
| base-b-test-4-npu-a3 / run (0) | 8.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111891) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618112034) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.7秒后返回退出码1，测试汇总0/1通过，属用例本身执行失败，需查看该用例Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111782

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111826

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111879

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111891

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618112034

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129617389301) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129617389312) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111643) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111740) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111746) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111750) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751910982/job/129618111842) |


## [Run #42751232924](https://github.com/sgl-project/sglang/actions/runs/42751232924)
- **分支**: `hicache-evict-headroom`
- **总耗时**: 34.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42751232924

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.1min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068705) |
| base-b-test-4-npu-a3 / run (0) | 8.6min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068751) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068784) |
| base-b-test-16-npu-a3 / run (0) | 5.5min | 代码错误 | NPU投机推理测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068814) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回退出码5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068705

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 sglang server（Kimi-VL-A3B-Instruct，--enable-dp-attention）后运行失败，耗时约 279 秒，2 个用例 0 通过，进程以退出码 1 结束，导致作业失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068751

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以退出码 1 结束，容器执行报错。需查看该用例的 Traceback 以定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068784

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83秒后返回退出码1，测试汇总0/1通过，属用例自身失败，需查看该脚本Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068814

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129615239203) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129615239211) |
| multimodal-gen-test-1-npu-a3 (1) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068527) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068556) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068557) |
| multimodal-gen-test-4-npu-a3 (0) | 30.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068583) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068743) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42751232924/job/129616068827) |


## [Run #42749819313](https://github.com/sgl-project/sglang/actions/runs/42749819313)
- **分支**: `jit-sm107a-per-module`
- **总耗时**: 26.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42749819313

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.3min | 代码错误 | NPU投机推理MoE a2a后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349401) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83.78秒后返回exit code 1，测试汇总0/1通过。日志省略部分未显示具体Traceback，需查看完整日志确认是server启动失败还是断言错误。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349401

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129610697995) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129610698139) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349349) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349351) |
| base-b-test-2-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349357) |
| base-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349410) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42749819313/job/129611349529) |


## [Run #42747738764](https://github.com/sgl-project/sglang/actions/runs/42747738764)
- **分支**: `fix/symm-mem-kv-budget-44106`
- **总耗时**: 26.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42747738764

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.2min | 代码错误 | NPU 投机推理 MoE a2a 后端测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011052) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 代码错误 | NPU DP attention 测试用例 test_npu_dp_attention.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011061) |
| base-b-test-2-npu-a3 / run (0) | 5.2min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011132) |

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行 83 秒后返回 exit code 1，测试汇总 0/1 通过；日志省略段未显示具体 Traceback，需查看该用例完整输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011052

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 test_npu_dp_attention.py 返回 exit code 1，Test Summary 0/2 passed，该用例在启动 Kimi-VL-A3B-Instruct 服务后失败，耗时 247s，具体错误被省略，需查看完整日志中的 Traceback 定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011061

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011132

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129666068096) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129666068160) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667010923) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667010956) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011016) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011064) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747738764/job/129667011135) |


## [Run #42747016375](https://github.com/sgl-project/sglang/actions/runs/42747016375)
- **分支**: `yanbing/cpu-fp8-quant-support`
- **总耗时**: 32.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42747016375

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.4min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394505) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时43秒），其余用例均通过，该用例失败使进程以退出码1结束，属用例本身报错，需查看其 Traceback 定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394505

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129601597677) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129601597850) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394365) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394395) |
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394408) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394420) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394502) |
| base-b-test-16-npu-a3 / run (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394543) |
| base-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394552) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394615) |
| base-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42747016375/job/129602394740) |


## [Run #42743763880](https://github.com/sgl-project/sglang/actions/runs/42743763880)
- **分支**: `dspark-draft-gfx1250_di_7/N`
- **总耗时**: 24.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42743763880

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.0min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704412932) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704412932

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704413362) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704413649) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704414488) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704414508) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704414963) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704414982) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704415115) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704415160) |
| base-b-test-16-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743763880/job/129704415380) |


## [Run #42743590407](https://github.com/sgl-project/sglang/actions/runs/42743590407)
- **分支**: `pr/muse-spark-rocm-sa-1027`
- **总耗时**: 46.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42743590407

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 25.7min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395030) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395094) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时46秒），其余用例均通过，该用例失败使进程以退出码1结束；日志未给出具体 Traceback，需查看该用例详细输出定位原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395030

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395094

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129590481745) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129590481888) |
| multimodal-gen-test-1-npu-a3 (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591394883) |
| multimodal-gen-test-1-npu-a3 (1) | 31.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591394927) |
| multimodal-gen-test-4-npu-a3 (1) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591394951) |
| multimodal-gen-test-4-npu-a3 (0) | 43.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591394977) |
| base-b-test-16-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395067) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395188) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395221) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743590407/job/129591395312) |


## [Run #42743079130](https://github.com/sgl-project/sglang/actions/runs/42743079130)
- **分支**: `fix/prefill-delayer-queue-trigger`
- **总耗时**: 25.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42743079130

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.5min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691334619) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以 exit code 1 结束。需查看该用例的 Traceback 定位具体断言或异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691334619

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691335094) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691335693) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691335817) |
| multimodal-gen-test-4-npu-a3 (0) | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691335830) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691335846) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691335939) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691336635) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691336656) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691336725) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691337005) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42743079130/job/129691337446) |


## [Run #42740687104](https://github.com/sgl-project/sglang/actions/runs/42740687104)
- **分支**: `feat/mamba-hybrid-state-eviction`
- **总耗时**: 24.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42740687104

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.4min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612968588) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612968588

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612969549) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612969684) |
| base-b-test-4-npu-a3 / run (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612969686) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612969716) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612969774) |
| multimodal-gen-test-4-npu-a3 (0) | 31.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612970194) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612970327) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612970448) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612970742) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612970758) |
| base-b-test-4-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740687104/job/129612970824) |


## [Run #42740256301](https://github.com/sgl-project/sglang/actions/runs/42740256301)
- **分支**: `fix/hisparse-decode-retract-rebootstrap`
- **总耗时**: 25.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42740256301

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.0min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666446969) |
| base-b-test-4-npu-a3 / run (0) | 7.8min | 代码错误 | NPU DP attention 测试脚本执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447211) |
| base-b-test-16-npu-a3 / run (0) | 5.2min | 代码错误 | NPU投机推理MoE a2a后端测试脚本执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447254) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666446969

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 242 秒。日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447211

- **base-b-test-16-npu-a3 / run (0)**: test_npu_speculative_moe_a2a_backend.py 运行83秒后返回退出码1，测试汇总0/1通过，属用例自身执行失败，需查看该用例Traceback定位具体异常。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447254

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129665759125) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129665759166) |
| multimodal-gen-test-4-npu-a3 (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666446911) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666446966) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447168) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447188) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42740256301/job/129666447313) |


## [Run #42739609182](https://github.com/sgl-project/sglang/actions/runs/42739609182)
- **分支**: `uocr2-mlx`
- **总耗时**: 49.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42739609182

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 23.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129586965855) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129586965855

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129577295828) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129577295835) |
| multimodal-gen-test-1-npu-a3 (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578302976) |
| multimodal-gen-test-4-npu-a3 (1) | 25.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303124) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303158) |
| multimodal-gen-test-1-npu-a3 (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303173) |
| base-b-test-16-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303267) |
| base-b-test-4-npu-a3 / run (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303366) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303371) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303478) |
| base-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303483) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129578303884) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129586965715) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739609182/job/129586965788) |


## [Run #42739490867](https://github.com/sgl-project/sglang/actions/runs/42739490867)
- **分支**: `feat/mlu-paged-gqa-fused-ops`
- **总耗时**: 8.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42739490867

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 4.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766863) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766882) |
| multimodal-gen-test-1-npu-a3 (0) | 4.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766906) |
| base-b-test-16-npu-a3 / run (0) | 4.7min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766946) |
| multimodal-gen-test-4-npu-a3 (1) | 4.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766962) |
| base-b-test-4-npu-a3 / run (0) | 4.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767034) |
| base-b-test-8-npu-a3 / run (0) | 4.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767093) |
| base-b-test-4-npu-a3 / run (1) | 4.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767094) |
| base-b-test-2-npu-a3 / run (0) | 4.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767147) |
| base-b-test-1-npu-a3 / run (0) | 4.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767235) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产出结果。退出码5表示unittest存在errors，最常见为setUpClass阶段server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766863

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中未见具体 Traceback，但退出码5表明 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766882

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约4分钟结束，无明确Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766906

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器环境异常，非用例代码本身报错，需联系 runner 管理员排查容器启动问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766946

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577766962

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器执行环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767034

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767093

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器运行时/环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767094

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，测试尚未真正运行，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767147

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在测试脚本启动后约10秒，属 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129577767235

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129576908461) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739490867/job/129576908506) |


## [Run #42739445307](https://github.com/sgl-project/sglang/actions/runs/42739445307)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 31.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42739445307

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 23.8min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421949) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时43秒），其余用例均通过，最终进程以退出码1结束。需查看该用例的 Traceback 以定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421949

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129576745899) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129576745917) |
| multimodal-gen-test-4-npu-a3 (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421719) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421724) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421763) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421827) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421885) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421888) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421898) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421916) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739445307/job/129577421939) |


## [Run #42739229421](https://github.com/sgl-project/sglang/actions/runs/42739229421)
- **分支**: `k3/tuned-moe-front`
- **总耗时**: 33.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42739229421

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728262) |
| base-b-test-1-npu-a3 / run (0) | 25.0min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728273) |
| base-b-test-4-npu-a3 / run (0) | 8.8min | 代码错误 | NPU DP attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728320) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py返回exit code 5，表示unittest存在errors，通常为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728262

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43 秒），其余用例均通过；该用例失败使进程以退出码 1 结束，容器执行失败。需查看该用例的 Traceback 以定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728273

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时约 296 秒，属测试用例本身执行报错，需查看具体 Traceback 定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728320

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129711723563) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129711723726) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728148) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728269) |
| multimodal-gen-test-4-npu-a3 (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728271) |
| base-b-test-4-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728321) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728364) |
| base-b-test-16-npu-a3 / run (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728366) |
| multimodal-gen-test-1-npu-a3 (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42739229421/job/129712728444) |


## [Run #42736645521](https://github.com/sgl-project/sglang/actions/runs/42736645521)
- **分支**: `pr/muse-spark-rocm-sa-1027`
- **总耗时**: 38.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42736645521

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613475) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613588) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 47s），其余用例均通过；该用例失败使进程以退出码 1 结束，属用例自身报错，需查看该用例 Traceback 定位。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613475

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_glm52.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613588

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129567647698) |
| Recommend tests from coverage | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129567647790) |
| multimodal-gen-test-1-npu-a3 (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613368) |
| multimodal-gen-test-1-npu-a3 (1) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613369) |
| multimodal-gen-test-4-npu-a3 (1) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613436) |
| multimodal-gen-test-4-npu-a3 (0) | 35.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613458) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613478) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613509) |
| base-b-test-4-npu-a3 / run (1) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613521) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42736645521/job/129568613549) |


## [Run #42735083488](https://github.com/sgl-project/sglang/actions/runs/42735083488)
- **分支**: `pr/muse-spark-rocm-sa-1027`
- **总耗时**: 13.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42735083488

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 9.6min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596144) |
| multimodal-gen-test-1-npu-a3 (0) | 9.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596233) |
| multimodal-gen-test-4-npu-a3 (0) | 9.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596273) |
| base-b-test-2-npu-a3 / run (0) | 9.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596287) |
| multimodal-gen-test-4-npu-a3 (1) | 9.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596312) |
| base-b-test-4-npu-a3 / run (0) | 8.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596389) |
| base-b-test-1-npu-a3 / run (0) | 9.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596431) |
| base-b-test-16-npu-a3 / run (0) | 9.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596435) |
| base-b-test-4-npu-a3 / run (1) | 8.7min | 环境问题 | 自定义容器执行失败，作业在测试启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596507) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约9分钟结束，退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596144

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596233

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业约9分钟后结束，未找到diffusion-failures/目录，无artifact上传。退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596273

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型分片加载到81%时出现“Executing the custom container implementation failed”，属于 runner 容器环境故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596287

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未生成产物；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596312

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例已正常执行并返回 200 OK，随后报错 'Executing the custom container implementation failed'，属于 runner 容器环境/基础设施故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596389

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在执行 test_npu_autoround_moe.py 时，属于 runner 容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596431


- **base-b-test-4-npu-a3 / run (1)**: 日志显示“Executing the custom container implementation failed”，随后作业清理退出，未见用例断言或代码异常；NPU 分配器仅告警。属自托管 runner 容器环境故障，需联系管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596507

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129562562122) |
| Recommend tests from coverage | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129562562151) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42735083488/job/129563596420) |


## [Run #42733896979](https://github.com/sgl-project/sglang/actions/runs/42733896979)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 41.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42733896979

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.1min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732276) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以 exit code 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732276

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129558649171) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129558649187) |
| multimodal-gen-test-1-npu-a3 (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732000) |
| multimodal-gen-test-4-npu-a3 (0) | 37.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732110) |
| multimodal-gen-test-1-npu-a3 (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732128) |
| multimodal-gen-test-4-npu-a3 (1) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732150) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732318) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732338) |
| base-b-test-4-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732353) |
| base-b-test-4-npu-a3 / run (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732399) |
| base-b-test-16-npu-a3 / run (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733896979/job/129559732535) |


## [Run #42733637030](https://github.com/sgl-project/sglang/actions/runs/42733637030)
- **分支**: `pr/muse-spark-rocm-sa-1027`
- **总耗时**: 12.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42733637030

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689623) |
| multimodal-gen-test-1-npu-a3 (1) | 8.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689649) |
| multimodal-gen-test-4-npu-a3 (0) | 7.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689712) |
| base-b-test-4-npu-a3 / run (1) | 8.4min | 环境问题 | 测试用例本身通过，但自定义容器执行失败导致作业报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689844) |
| base-b-test-16-npu-a3 / run (0) | 8.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689846) |
| multimodal-gen-test-1-npu-a3 (0) | 8.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689858) |
| base-b-test-1-npu-a3 / run (0) | 8.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689861) |
| base-b-test-2-npu-a3 / run (0) | 8.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689882) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689936) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558690097) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业以退出码5结束（unittest errors），且未生成diffusion-failures目录，无artifact上传。中间省略部分可能含server启动失败Traceback，需查看完整日志确认是否host OOM或进程被SIGKILL。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689623

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示作业以退出码5结束（unittest存在errors），且未找到diffusion-failures/目录产物。最常见原因是setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689649

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689712

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 Ran 2 tests, OK，用例全部通过；随后报错 'Executing the custom container implementation failed'，属于自托管 runner 的容器执行环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689844

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载完成后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689846

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact，说明测试用例执行中出错。退出码5对应unittest errors，常见于setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689858

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 test_npu_autoround_dense.py 的 test_a_gsm8k 执行期间，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689861

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载到 38% 时出现 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689882

- **base-b-test-8-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题；此前测试仍在正常输出 Expert Balancedness 日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558689936

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在权重加载过程中，属于 runner/容器环境异常，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129558690097

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129557639117) |
| Recommend tests from coverage | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42733637030/job/129557639132) |


## [Run #42732752403](https://github.com/sgl-project/sglang/actions/runs/42732752403)
- **分支**: `vedantjh2/synthid-oss`
- **总耗时**: 14.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42732752403

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 10.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792088) |
| multimodal-gen-test-1-npu-a3 (1) | 10.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792105) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792118) |
| multimodal-gen-test-4-npu-a3 (0) | 9.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792176) |
| base-b-test-4-npu-a3 / run (0) | 10.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792226) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | 环境问题 | 自定义容器执行失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792346) |
| base-b-test-2-npu-a3 / run (0) | 10.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792370) |
| base-b-test-1-npu-a3 / run (0) | 10.5min | 环境问题 | 自托管容器执行失败，作业在模型权重加载中途被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792384) |
| base-b-test-16-npu-a3 / run (0) | 10.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792386) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792088

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示用例以退出码5结束（FAILED errors=N），且未生成 diffusion-failures/ 目录，说明测试在 setUpClass 阶段即失败，最可能是 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792105

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行异常。退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792118

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未生成产物。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792176

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题；此前仅有 torch_npu 警告，无 Traceback 或退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792226

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器启动/运行环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792346

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非用例断言失败；此前 server 请求均返回 200，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792370

- **base-b-test-1-npu-a3 / run (0)**: 日志显示加载权重到50%时出现“Executing the custom container implementation failed”，属自托管 runner 容器异常退出，非用例断言失败；另有 mamba 模块导入告警但被忽略。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792384

- **base-b-test-16-npu-a3 / run (0)**: 日志显示各 TP/EP 进程权重加载完成后，报错“Executing the custom container implementation failed”，属 runner 容器环境问题，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792386

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129554787086) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129554787117) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42732752403/job/129555792237) |


## [Run #42732549856](https://github.com/sgl-project/sglang/actions/runs/42732549856)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 11.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42732549856

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 6.6min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319637) |
| multimodal-gen-test-4-npu-a3 (1) | 6.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319667) |
| multimodal-gen-test-1-npu-a3 (1) | 7.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319700) |
| multimodal-gen-test-4-npu-a3 (0) | 6.8min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319773) |
| base-b-test-16-npu-a3 / run (0) | 6.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319810) |
| base-b-test-8-npu-a3 / run (0) | 6.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319831) |
| base-b-test-4-npu-a3 / run (0) | 7.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319856) |
| base-b-test-2-npu-a3 / run (0) | 6.8min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319863) |
| base-b-test-1-npu-a3 / run (0) | 7.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319913) |
| base-b-test-4-npu-a3 / run (1) | 7.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319924) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成该目录（可能用例未执行或提前失败），导致 upload-artifact 步骤无产物可传而失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319637

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产出结果；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319667

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示作业以退出码5结束（unittest errors），且未找到diffusion-failures/目录产物。中间省略部分应含server启动失败的Traceback，常见原因为host OOM或进程被SIGKILL，属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319700

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例未正常产出失败产物；退出码5对应 unittest errors，最常见为 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319773

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载到约25%时出现“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319810

- **base-b-test-8-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题；此前测试仍在正常输出 Expert Balancedness 日志，无 Traceback 或退出码 5 等用例失败证据。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319831

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，测试在 TestDPAttentionDP2TP2 用例执行时容器异常退出，属 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319856

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码问题；需联系自托管 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319863

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319913

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器实现异常，非用例代码问题；随后仅执行清理，未进入测试阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129555319924

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129554246878) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42732549856/job/129554246972) |


## [Run #42731861763](https://github.com/sgl-project/sglang/actions/runs/42731861763)
- **分支**: `adaptive-verification-online-estimator`
- **总耗时**: 6.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42731861763

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 2.2min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业本身未报失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552680917) |
| multimodal-gen-test-1-npu-a3 (0) | 2.6min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552680964) |
| multimodal-gen-test-1-npu-a3 (1) | 2.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552680997) |
| base-b-test-16-npu-a3 / run (0) | 2.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在容器启动阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681043) |
| base-b-test-8-npu-a3 / run (0) | 1.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在安装 uv 后中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681097) |
| base-b-test-2-npu-a3 / run (0) | 2.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681115) |
| base-b-test-4-npu-a3 / run (0) | 2.9min | 环境问题 | 自托管 runner 执行自定义容器实现失败，作业在容器启动阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681216) |
| base-b-test-1-npu-a3 / run (0) | 1.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681290) |
| base-b-test-4-npu-a3 / run (1) | 2.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681464) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅含 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback 或退出码信息，无法定位具体失败；需查看被省略的中间日志确认 server 启动或 OOM 等真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552680917

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见用例收集失败，而是 unittest 报 errors（退出码5），常见于 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL）；同时 diffusion-failures/ 目录无文件，artifact 上传为空。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552680964

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552680997

- **base-b-test-16-npu-a3 / run (0)**: 日志显示下载 custom-ops 压缩包后立即报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681043

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 pip 安装 uv 后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681097

- **base-b-test-2-npu-a3 / run (0)**: 日志显示安装 torch-npu 时出现 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681115

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 custom container implementation 执行失败（##[error]），发生在 ops_custom 安装完成后、测试尚未开始，属 runner/容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681216

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 MemFabric 安装后报错 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码失败；后续仅为清理步骤。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681290

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 安装依赖后出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129552681464

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129551762669) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42731861763/job/129551762689) |


## [Run #42726478322](https://github.com/sgl-project/sglang/actions/runs/42726478322)
- **分支**: `codex/23602-hisparse-pool`
- **总耗时**: 26.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42726478322

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.7min | 代码错误 | test_dspark_npu_dispatch.py 用例失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395727) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过，最终进程以退出码 1 结束。日志未给出该用例的具体 Traceback，需查看该用例的详细输出以定位是断言失败还是 setUpClass 阶段 server 启动异常。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395727

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129533477884) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129533478021) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395509) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395703) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395722) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395756) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534395903) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534396016) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42726478322/job/129534397039) |


## [Run #42723588649](https://github.com/sgl-project/sglang/actions/runs/42723588649)
- **分支**: `wj/nixl-kv-packing`
- **总耗时**: 36.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42723588649

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.5min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646341) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时41秒），其余用例均通过，该用例失败使进程以退出码1结束，属用例级代码/断言失败，需查看该用例具体报错。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646341

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129523594146) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129523594172) |
| multimodal-gen-test-1-npu-a3 (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646234) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646300) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646324) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646338) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646383) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646413) |
| base-b-test-16-npu-a3 / run (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646414) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646451) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42723588649/job/129524646532) |


## [Run #42718874778](https://github.com/sgl-project/sglang/actions/runs/42718874778)
- **分支**: `xpu/weekly-simple-model-enablement-2026-11-09`
- **总耗时**: 51.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42718874778

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647159) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 43s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647159

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129507649209) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129507649286) |
| multimodal-gen-test-1-npu-a3 (1) | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508646708) |
| multimodal-gen-test-4-npu-a3 (1) | 36.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508646910) |
| multimodal-gen-test-1-npu-a3 (0) | 32.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508646940) |
| multimodal-gen-test-4-npu-a3 (0) | 47.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508646981) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647087) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647098) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647171) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647194) |
| base-b-test-4-npu-a3 / run (1) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42718874778/job/129508647263) |


## [Run #42717017070](https://github.com/sgl-project/sglang/actions/runs/42717017070)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 38.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42717017070

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157341) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过，最终进程以 exit code 1 结束，属于该用例自身失败。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157341

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129501256164) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129501256235) |
| multimodal-gen-test-1-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157190) |
| multimodal-gen-test-1-npu-a3 (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157210) |
| multimodal-gen-test-4-npu-a3 (0) | 34.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157370) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157405) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157472) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157505) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157558) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157603) |
| base-b-test-16-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42717017070/job/129502157687) |


## [Run #42715925425](https://github.com/sgl-project/sglang/actions/runs/42715925425)
- **分支**: `refactor/graph-neutral-backends`
- **总耗时**: 27.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42715925425

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 26.6min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651894756) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 45s），其余用例均通过；该用例失败使进程以退出码 1 结束，具体报错需查看该用例的 Traceback。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651894756

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651895612) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651895816) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651895863) |
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651895912) |
| multimodal-gen-test-1-npu-a3 (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651895925) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651896011) |
| multimodal-gen-test-1-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651896025) |
| base-b-test-16-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651896073) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651896091) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651896149) |
| multimodal-gen-test-4-npu-a3 (0) | 35.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42715925425/job/129651945442) |


## [Run #42713709280](https://github.com/sgl-project/sglang/actions/runs/42713709280)
- **分支**: `hicache/scheduler-thread-bounded-calls`
- **总耗时**: 44.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42713709280

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 15.6min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129502244969) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 该性能用例运行约 651 秒后返回退出码 1，测试汇总 0/1 通过。日志省略了具体 Traceback，无法确定是 server 启动失败、OOM 还是性能阈值未达标，需查看完整日志中的真实错误。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129502244969

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129489861369) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129489861399) |
| base-b-test-1-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129490964992) |
| base-b-test-2-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129490965067) |
| base-b-test-4-npu-a3 / run (1) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129490965081) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129490965086) |
| base-b-test-4-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42713709280/job/129490965104) |


## [Run #42708776271](https://github.com/sgl-project/sglang/actions/runs/42708776271)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 26.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42708776271

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 4.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152114) |
| multimodal-gen-test-1-npu-a3 (0) | 4.0min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152181) |
| multimodal-gen-test-4-npu-a3 (0) | 3.9min | 环境问题 | diffusion 测试失败，未生成 diffusion-failures 目录，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152226) |
| multimodal-gen-test-4-npu-a3 (1) | 4.1min | 环境问题 | multimodal-gen 测试失败，diffusion-failures 目录无文件，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152329) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | 代码错误 | test_dspark_npu_dispatch.py 用例失败导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152526) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152114

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试脚本未产出失败用例文件；结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），但日志中未捕获具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152181

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 路径，说明测试用例未产出失败样本；结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152226

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示上传 diffusion-failures/ 时无文件，说明测试用例未产出失败产物；结合退出码 5（unittest errors），最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152329

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时 42s），其余用例均通过；该用例失败使进程以退出码 1 结束，容器执行随之报错。需查看该用例的 Traceback 定位具体错误。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152526

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129472728035) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129472728041) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152313) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152320) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152331) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152409) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42708776271/job/129474152452) |


## [Run #42705053125](https://github.com/sgl-project/sglang/actions/runs/42705053125)
- **分支**: `perf/amd-qwen4-fused-hc-decode`
- **总耗时**: 82.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42705053125

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 5.1min | 环境问题 | 性能测试用例 setUpClass 阶段 sglang server 启动失败，导致 unittest 报 errors（退出码 5） | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129493639889) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 10.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129493639905) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: test_npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py 运行 71s 后以 exit code 5 失败，3 个用例 0 通过；退出码 5 表示 unittest 存在 errors，通常为 setUpClass 中 server 启动失败（如 host OOM、进程被 SIGKILL）。后续 shell 还因变量为多行 '0\n0' 报 integer expression expected，最终作业退出码 1。
  - 失败用例: npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py, npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129493639889


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129459793003) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129459793123) |
| multimodal-gen-test-1-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461170966) |
| multimodal-gen-test-1-npu-a3 (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461170984) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171085) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171182) |
| base-b-test-2-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171226) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171339) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171491) |
| base-b-test-16-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171505) |
| base-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171586) |
| base-b-test-1-npu-a3 / run (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129461171606) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129477128098) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129477128121) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42705053125/job/129477128226) |


## [Run #42702934954](https://github.com/sgl-project/sglang/actions/runs/42702934954)
- **分支**: `dark/carv2-dpx-pair-header`
- **总耗时**: 40.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42702934954

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 13.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858429) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_speculative_multi_npu.py, npu_speculative_multi_npu.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858429

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129452466203) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129452466235) |
| multimodal-gen-test-4-npu-a3 (0) | 32.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858034) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858068) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858069) |
| multimodal-gen-test-4-npu-a3 (1) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858117) |
| base-b-test-16-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858336) |
| base-b-test-1-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858353) |
| base-b-test-2-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858405) |
| base-b-test-4-npu-a3 / run (0) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453858415) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702934954/job/129453859689) |


## [Run #42702537306](https://github.com/sgl-project/sglang/actions/runs/42702537306)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 49.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42702537306

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 36.6min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129453996480) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中上传了 diffusion-failures-npu-2-part0-2.zip 工件，说明测试用例执行失败并收集了失败产物；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看工件中的 Traceback 确认具体错误。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129453996480

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129452763400) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129452763420) |
| multimodal-gen-test-1-npu-a3 (1) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129453996331) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129453996443) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42702537306/job/129453996641) |


## [Run #42699506676](https://github.com/sgl-project/sglang/actions/runs/42699506676)
- **分支**: `users/wenkaidu/carv2-2shot-push-gfx1250`
- **总耗时**: 78.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42699506676

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | 环境问题 | 自托管 runner 容器执行失败，临时文件丢失导致作业异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732704) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 18.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129482447298) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，随后 runner 报 ENOENT 打开 _temp/_runner_file_commands 下 .nfs 文件失败，Node 进程退出码 1，属 runner 环境/文件系统异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732704

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示服务已正常启动并响应 /v1/models 与 /model_info，随后报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129482447298

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129450186089) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129450186466) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732512) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732661) |
| multimodal-gen-test-1-npu-a3 (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732668) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732887) |
| base-b-test-4-npu-a3 / run (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732945) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451732955) |
| base-b-test-1-npu-a3 / run (0) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451733026) |
| base-b-test-16-npu-a3 / run (0) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451733054) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129451733088) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129465201353) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129465201469) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129465202373) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42699506676/job/129482447094) |


## [Run #42687587573](https://github.com/sgl-project/sglang/actions/runs/42687587573)
- **分支**: `byron/r3-deepep-gather-once`
- **总耗时**: 54.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42687587573

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877400) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877400

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129398674760) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129398674870) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399970676) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399970900) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399970907) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399970989) |
| base-b-test-4-npu-a3 / run (1) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399971087) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399971138) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399971227) |
| base-b-test-16-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129399971320) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877384) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42687587573/job/129412877573) |


## [Run #42681165596](https://github.com/sgl-project/sglang/actions/runs/42681165596)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 36.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42681165596

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377590998) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377591009) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377591206) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377591276) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377591378) |
| base-b-test-1-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377591574) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129376063250) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129376063276) |
| multimodal-gen-test-1-npu-a3 (1) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377590397) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377590530) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377590684) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42681165596/job/129377590700) |


## [Run #42677719857](https://github.com/sgl-project/sglang/actions/runs/42677719857)
- **分支**: `mani1106/gdn-mis-delimiter-isolation`
- **总耗时**: 5.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42677719857

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42677719857/job/129365110201) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/42677719857/job/129365110288) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42677719857/job/129363785031) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42677719857/job/129363785142) |


## [Run #42673402805](https://github.com/sgl-project/sglang/actions/runs/42673402805)
- **分支**: `xpu-monokernel-framework`
- **总耗时**: 8.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42673402805

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 2.5min | 环境问题 | git config 写入 /etc/gitconfig 权限不足导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407355) |
| base-b-test-16-npu-a3 / run (0) | 1.6min | 环境问题 | git config 写入系统级配置文件 /etc/gitconfig 时权限不足，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407422) |
| multimodal-gen-test-1-npu-a3 (0) | 2.4min | 环境问题 | git config 写入 /etc/gitconfig 权限不足导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407660) |
| base-b-test-8-npu-a3 / run (0) | 1.6min | 环境问题 | git 配置系统级文件权限不足导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351408286) |
| multimodal-gen-test-4-npu-a3 (1) | 2.5min | 环境问题 | git config 写入 /etc/gitconfig 权限不足导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351408386) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业在 checkout 后执行 git config --system --add safe.directory 时，因无权限写 /etc/gitconfig 报 Permission denied，退出码 255，属 runner 环境权限配置问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407355

- **base-b-test-16-npu-a3 / run (0)**: 步骤执行 git config --system --add safe.directory 时报错 error: could not lock config file /etc/gitconfig: Permission denied，退出码 255。原因是 runner 用户对 /etc/gitconfig 无写权限，属于 CI 环境配置问题，与代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407422

- **multimodal-gen-test-1-npu-a3 (0)**: 作业在 checkout 后执行 git config --system --add safe.directory 时，因无 /etc/gitconfig 写权限报 Permission denied，退出码 255，后续测试未运行，属 runner 环境权限配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351407660

- **base-b-test-8-npu-a3 / run (0)**: 执行 git config --system --add safe.directory 时无法写入 /etc/gitconfig，报 Permission denied，退出码 255，作业在 checkout 后立即失败，属 runner 环境权限配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351408286

- **multimodal-gen-test-4-npu-a3 (1)**: 执行 git config --system --add safe.directory 时提示 could not lock config file /etc/gitconfig: Permission denied，退出码 255，runner 用户无系统级配置写权限，属环境/权限配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129351408386

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42673402805/job/129350878714) |


## [Run #42669362795](https://github.com/sgl-project/sglang/actions/runs/42669362795)
- **分支**: `shuwen/fix-mooncake-shared-te-registration`
- **总耗时**: 34.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42669362795

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 6.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695948) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342696000) |

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695948

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_speculative_multi_npu.py, npu_speculative_multi_npu.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342696000

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129341732033) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129341732162) |
| multimodal-gen-test-1-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695489) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695507) |
| multimodal-gen-test-4-npu-a3 (0) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695661) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695851) |
| base-b-test-2-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695857) |
| multimodal-gen-test-4-npu-a3 (1) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342695870) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342696015) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42669362795/job/129342696251) |


## [Run #42658924559](https://github.com/sgl-project/sglang/actions/runs/42658924559)
- **分支**: `int8_diffusion_online_quantization`
- **总耗时**: 73.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42658924559

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | 环境问题 | 日志中未见明确错误，但上传了 diffusion-failures 产物，推测测试用例失败并产生失败样本 | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621645) |

- **multimodal-gen-test-4-npu-a3 (0)**: 作业退出码5表示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL）。日志末尾上传了diffusion-failures-npu-2-part0-1.zip失败产物，说明测试执行中产生失败样本，需查看该产物及中间省略的Traceback定位具体错误。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621645

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129305112229) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129305112362) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621530) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621536) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621751) |
| base-b-test-1-npu-a3 / run (0) | 5.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621838) |
| base-b-test-4-npu-a3 / run (0) | 6.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621851) |
| base-b-test-16-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621872) |
| base-b-test-2-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621909) |
| base-b-test-4-npu-a3 / run (1) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621946) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129306621996) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129316239442) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129326507581) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42658924559/job/129326507610) |


## [Run #42647673269](https://github.com/sgl-project/sglang/actions/runs/42647673269)
- **分支**: `mani1106/gdn-mis-delimiter-isolation`
- **总耗时**: 16.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42647673269

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42647673269/job/129266693554) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42647673269/job/129266693578) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42647673269/job/129265519971) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42647673269/job/129265519985) |


## [Run #42575746641](https://github.com/sgl-project/sglang/actions/runs/42575746641)
- **分支**: `nixl-odirect-zero-copy`
- **总耗时**: 9.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42575746641

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42575746641/job/129356869775) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42575746641/job/129356869775

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575746641/job/129355558773) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42575746641/job/129355558836) |


## [Run #42558320866](https://github.com/sgl-project/sglang/actions/runs/42558320866)
- **分支**: `k3/dspark-draft-unified-attn`
- **总耗时**: 34.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42558320866

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.7min | 环境问题 | 测试脚本退出码5，setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263645) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263707) |
| base-b-test-4-npu-a3 / run (0) | 8.3min | 代码错误 | NPU dp_attention 测试用例执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263811) |

- **base-b-test-2-npu-a3 / run (0)**: test_npu_mla_fia_hicache_bf16.py 返回exit code 5，表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），导致0/8用例通过。
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263645

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263707

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 在启动 Kimi-VL-A3B-Instruct 服务后运行失败，返回 exit code 1，2 个用例 0 通过，耗时 268s。日志未显示具体 Traceback，需查看该用例详细输出定位是 server 启动失败还是断言失败。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263811

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129743105799) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129743105939) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263472) |
| multimodal-gen-test-1-npu-a3 (1) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263520) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263538) |
| base-b-test-1-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263571) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263703) |
| base-b-test-4-npu-a3 / run (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744263915) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42558320866/job/129744264040) |


---
*Auto-generated by ci_monitor.py*