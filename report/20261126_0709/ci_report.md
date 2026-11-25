# NPU CI 执行监控（2026-11-25）
**生成时间**: 2026-11-26 07:09
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-25 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 27

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 350 个 | 失败 37 个 | 成功 Job 平均耗时 17.4min
- **Run 执行情况**: 成功 13 个 | 失败 14 个 | 成功 Run 平均耗时 77.0min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 79.1min | #45392333183 | [job link](https://github.com/sgl-project/sglang/actions/runs/45392333183/job/138440964869) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 69.4min | #45392333183 | [job link](https://github.com/sgl-project/sglang/actions/runs/45392333183/job/138493270073) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 68.2min | #45612628850 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864358) |
| extra-b-test-4-npu-a3 / run (0) | 60.1min | #45612628850 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556103) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 53.3min | #45563325953 | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139044579669) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 52.2min | #45531825472 | [job link](https://github.com/sgl-project/sglang/actions/runs/45531825472/job/139036371323) |
| extra-b-test-2-npu-a3 / run (0) | 51.8min | #45392333183 | [job link](https://github.com/sgl-project/sglang/actions/runs/45392333183/job/138440964546) |
| extra-b-test-2-npu-a3 / run (0) | 45.5min | #45612628850 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556510) |
| extra-b-test-1-npu-a3 / run (0) | 43.2min | #45392333183 | [job link](https://github.com/sgl-project/sglang/actions/runs/45392333183/job/138440965099) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 42.9min | #45592212237 | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139151555717) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 36.1min | #45612628850 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864173) |
| multimodal-gen-test-4-npu-a3 (0) | 30.2min | #45592212237 | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297918) |
| multimodal-gen-test-4-npu-a3 (0) | 27.7min | #45542499978 | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232133) |
| multimodal-gen-test-4-npu-a3 (0) | 27.0min | #45612628850 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555895) |
| multimodal-gen-test-4-npu-a3 (0) | 26.0min | #45564591266 | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101616) |
| multimodal-gen-test-4-npu-a3 (0) | 25.7min | #45583865378 | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038317) |
| multimodal-gen-test-4-npu-a3 (0) | 24.1min | #45523615142 | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823415) |
| multimodal-gen-test-1-npu-a3 (1) | 20.3min | #45560844492 | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373320) |
| multimodal-gen-test-1-npu-a3 (0) | 19.4min | #45560844492 | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373410) |
| extra-b-test-1-npu-a3 / run (1) | 19.2min | #45523615142 | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823847) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| multimodal-gen-test-4-npu-a3 (0) | 20 | 13 | 6 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555895)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297918)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038317)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101616)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232133) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 38 | 32 | 1 | 4 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864173) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 16 | 12 | 2 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139121008436)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139068167268) |
| extra-b-test-1-npu-a3 / run (1) | 24 | 21 | 1 | 1 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823847) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 20 | 17 | 0 | 2 | 1 | - |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 10 | 8 | 1 | 1 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138989887100) |
| multimodal-gen-test-1-npu-a3 (1) | 17 | 15 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373320) |
| multimodal-gen-test-1-npu-a3 (0) | 17 | 15 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373410) |
| extra-b-test-4-npu-a3 / run (0) | 22 | 21 | 0 | 1 | 0 | - |
| extra-b-test-1-npu-a3 / run (0) | 24 | 22 | 0 | 1 | 1 | - |
| extra-b-test-4-npu-a3 / run (1) | 22 | 21 | 0 | 1 | 0 | - |
| extra-b-test-2-npu-a3 / run (1) | 22 | 21 | 0 | 1 | 0 | - |
| extra-b-test-2-npu-a3 / run (0) | 22 | 20 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823729) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `qwen_image_t2i_2npu` | 12 | 5 | 7 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555895)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297918)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038317) |
| `wan2_2_t2v_14b_w8a8_2npu` | 11 | 5 | 6 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555895)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297918)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038317) |
| `minimax_h3_t2va_2npu` | 13 | 11 | 2 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373514)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395466) |
| `npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py` | 5 | 3 | 2 | [extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139121008436)<br>[extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139068167268) |
| `dspark_npu_dispatch.py` | 9 | 8 | 1 | [extra-b-test-1-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823847) |
| `npu_compile_graph_tp2_bf16.py` | 9 | 8 | 1 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823729) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 8 | 7 | 1 | [extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864173) |
| `npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` | 3 | 2 | 1 | [extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138989887100) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #45612628850<br>[#53077 [Fix] gdn: Initialize ReplaySSM verify stages in direct-commit test](https://github.com/sgl-project/sglang/pull/53077) | `main` | 132.9min | 2 | multimodal-gen-test-4-npu-a3 (0), extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45612628850) |
| #45563325953<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 101.6min | 1 | extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45563325953) |
| #45583865378<br>[#50691 [Feat] [NPU] moe: Add MegaMoE fused_op support for prefill and decode](https://github.com/sgl-project/sglang/pull/50691) | `feat/dev_megamoe` | 101.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45583865378) |
| #45564591266<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 95.8min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45564591266) |
| #45576664296<br>[#50205 [Feat] [NPU] deepseek-v4.1: Support Ascend A3 W8A8 inference and DSpark](https://github.com/sgl-project/sglang/pull/50205) | `dsv41-a3-dev-1112` | 95.1min | 1 | extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45576664296) |
| #45542499978<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 91.2min | 2 | multimodal-gen-test-4-npu-a3 (0), extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45542499978) |
| #45592212237<br>[#51069 [Fix] [NPU] multimodal_gen: Fix LLaDA-Image support for NPU backend](https://github.com/sgl-project/sglang/pull/51069) | `llada_image` | 80.3min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45592212237) |
| #45570838802<br>[#46208 [Feat] [NPU] multimodal: support mm_feature_transport=npu_ipc](https://github.com/sgl-project/sglang/pull/46208) | `feat/mm-feature-transport-npu-ipc` | 72.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45570838802) |
| #45521709657<br>[#49502 [Feat] [NPU] dsa: Store the DSA MLA KV cache as INT8 on Ascend A2](https://github.com/sgl-project/sglang/pull/49502) | `feat/npu-dsa-int8-main-kv` | 45.5min | 2 | extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3, extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45521709657) |
| #45560844492<br>[#44056 [Feat] [NPU] diffusion: Support Qwen-Image 2.1 and Turbo on Ascend](https://github.com/sgl-project/sglang/pull/44056) | `qwenimage21` | 40.0min | 2 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45560844492) |
| #45567888699<br>[#38860 [Feat] [NPU] DSpark: Load the GLM-5.2 Speculators draft for static decoding on NPU](https://github.com/sgl-project/sglang/pull/38860) | `feat/glm52-dspark-npu-upstream` | 35.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45567888699) |
| #45523615142<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 28.4min | 3 | multimodal-gen-test-4-npu-a3 (0), extra-b-test-2-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45523615142) |
| #45540562782<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 18.3min | 7 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), extra-b-test-1-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1), extra-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45540562782) |
| #45581752290<br>[#52834 [Perf] [NPU] qsa: Shard prefill Indexer and Sparse Attention across TP](https://github.com/sgl-project/sglang/pull/52834) | `codex/qsa-npu-tp-prefill` | 6.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45581752290) |

---


## [Run #45612628850](https://github.com/sgl-project/sglang/actions/runs/45612628850)
- **分支**: `main`
- **总耗时**: 132.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45612628850

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.0min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555895) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 36.1min | 环境问题 | 精度测试作业失败，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864173) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行了多模态生成测试并上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例出现失败/错误（退出码5，unittest errors，常见于 setUpClass 阶段 server 启动失败如 OOM/SIGKILL）。日志省略部分未显示具体 Traceback，需查看上传产物确认根因。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555895

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志被截断，未显示真实 Traceback；退出码 5 表明 unittest 存在 errors，最常见为 setUpClass 中 server 启动失败（host OOM 或进程被 SIGKILL），需查看上传的测试日志确认具体异常。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864173

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139200022244) |
| multimodal-gen-test-1-npu-a3 (1) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555735) |
| multimodal-gen-test-1-npu-a3 (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555794) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201555851) |
| extra-b-test-4-npu-a3 / run (0) | 60.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556103) |
| extra-b-test-16-npu-a3 / run (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556160) |
| extra-b-test-8-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556193) |
| extra-b-test-1-npu-a3 / run (1) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556213) |
| extra-b-test-1-npu-a3 / run (0) | 32.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556252) |
| extra-b-test-4-npu-a3 / run (1) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556281) |
| extra-b-test-2-npu-a3 / run (1) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556353) |
| extra-b-test-2-npu-a3 / run (0) | 45.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139201556510) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 68.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864358) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45612628850/job/139235864425) |


## [Run #45592212237](https://github.com/sgl-project/sglang/actions/runs/45592212237)
- **分支**: `llada_image`
- **总耗时**: 80.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45592212237

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.2min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297918) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139175209913) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中作业退出并上传 diffusion-failures-npu-2-part0-2.zip 失败产物，说明测试用例执行出错（退出码 5，unittest errors），常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），属环境/资源问题。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297918


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139134025869) |
| extra-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139134026120) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297615) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297625) |
| multimodal-gen-test-4-npu-a3 (1) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297665) |
| extra-b-test-16-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297817) |
| extra-b-test-2-npu-a3 / run (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297847) |
| extra-b-test-1-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297904) |
| extra-b-test-1-npu-a3 / run (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297911) |
| extra-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297956) |
| extra-b-test-8-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135297961) |
| extra-b-test-4-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135298024) |
| extra-b-test-2-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139135298060) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139151555710) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 42.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139151555717) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 35.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45592212237/job/139151555737) |


## [Run #45583865378](https://github.com/sgl-project/sglang/actions/runs/45583865378)
- **分支**: `feat/dev_megamoe`
- **总耗时**: 101.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45583865378

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 25.7min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038317) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见测试结束后上传 diffusion-failures-npu-2-part0-2.zip 失败产物，作业以非零退出。结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）导致用例 error，需查看省略段中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038317

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139102773980) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139102773986) |
| multimodal-gen-test-1-npu-a3 (1) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038172) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038248) |
| extra-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038457) |
| extra-b-test-16-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038520) |
| extra-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038534) |
| extra-b-test-8-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038546) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038576) |
| extra-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038589) |
| extra-b-test-2-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038609) |
| extra-b-test-1-npu-a3 / run (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038664) |
| extra-b-test-2-npu-a3 / run (1) | 26.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139104038794) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 35.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139122289582) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 37.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139122290048) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139122290051) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45583865378/job/139144064419) |


## [Run #45581752290](https://github.com/sgl-project/sglang/actions/runs/45581752290)
- **分支**: `codex/qsa-npu-tp-prefill`
- **总耗时**: 6.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45581752290

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45581752290/job/139108006299) |
| extra-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45581752290/job/139108006376) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45581752290/job/139106337223) |
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45581752290/job/139106337459) |


## [Run #45576664296](https://github.com/sgl-project/sglang/actions/runs/45576664296)
- **分支**: `dsv41-a3-dev-1112`
- **总耗时**: 95.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45576664296

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 12.8min | 环境问题 | 日志中未见明确错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的测试阶段日志 | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139121008436) |

- **extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3**: 可见日志仅显示 artifact 上传成功及 post job cleanup，无 Traceback/RuntimeError。退出码 5 提示 unittest 存在 errors，可能为 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），但具体错误在被省略的中间日志中，需查看 selected-test-logs artifact 确认。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139121008436

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139083479630) |
| extra-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139083479715) |
| multimodal-gen-test-1-npu-a3 (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073667) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073740) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073746) |
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073834) |
| extra-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073920) |
| extra-b-test-4-npu-a3 / run (0) | 29.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073940) |
| extra-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073960) |
| extra-b-test-16-npu-a3 / run (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073963) |
| extra-b-test-2-npu-a3 / run (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085073998) |
| extra-b-test-2-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085074028) |
| extra-b-test-1-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085074036) |
| extra-b-test-1-npu-a3 / run (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139085074204) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139100258516) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 35.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139100258537) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139100258643) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45576664296/job/139121008275) |


## [Run #45570838802](https://github.com/sgl-project/sglang/actions/runs/45570838802)
- **分支**: `feat/mm-feature-transport-npu-ipc`
- **总耗时**: 72.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45570838802

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 1.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139089974092) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139089974125) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139058174948) |
| extra-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139058174970) |
| multimodal-gen-test-4-npu-a3 (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043773) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043774) |
| multimodal-gen-test-4-npu-a3 (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043783) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043838) |
| extra-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043938) |
| extra-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043969) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059043977) |
| extra-b-test-2-npu-a3 / run (1) | 30.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059044013) |
| extra-b-test-4-npu-a3 / run (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059044030) |
| extra-b-test-1-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059044038) |
| extra-b-test-16-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059044174) |
| extra-b-test-1-npu-a3 / run (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139059044206) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139073611978) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139073612013) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45570838802/job/139073612167) |


## [Run #45567888699](https://github.com/sgl-project/sglang/actions/runs/45567888699)
- **分支**: `feat/glm52-dspark-npu-upstream`
- **总耗时**: 35.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45567888699

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139094429819) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139094429894) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139094429920) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139079297472) |
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139079297592) |
| multimodal-gen-test-1-npu-a3 (1) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400606) |
| multimodal-gen-test-4-npu-a3 (0) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400648) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400667) |
| extra-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400707) |
| extra-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400716) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400735) |
| extra-b-test-1-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400748) |
| extra-b-test-1-npu-a3 / run (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400758) |
| extra-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400780) |
| extra-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400784) |
| extra-b-test-2-npu-a3 / run (1) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400796) |
| extra-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45567888699/job/139080400958) |


## [Run #45564591266](https://github.com/sgl-project/sglang/actions/runs/45564591266)
- **分支**: `main`
- **总耗时**: 95.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45564591266

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 26.0min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101616) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约26分钟后上传 diffusion-failures-npu-2-part0-2.zip 失败产物，说明测试用例出现 errors（退出码5），常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志中段被省略，未见具体 Traceback，需查看产物与完整日志确认根因。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101616

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139036996822) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139036996830) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101600) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101643) |
| extra-b-test-2-npu-a3 / run (1) | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101701) |
| extra-b-test-1-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101704) |
| extra-b-test-8-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101705) |
| extra-b-test-1-npu-a3 / run (1) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101726) |
| extra-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101764) |
| extra-b-test-4-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101790) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101792) |
| extra-b-test-2-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101800) |
| extra-b-test-16-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139038101803) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 36.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139049675519) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139049675544) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139049675560) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139067065319) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45564591266/job/139067065320) |


## [Run #45563325953](https://github.com/sgl-project/sglang/actions/runs/45563325953)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 101.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45563325953

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 14.7min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139068167268) |

- **extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3**: 可见部分仅为 runner 初始化、下载 action、上传 artifact 和清理阶段，均正常；中间省略段可能含真实错误（如退出码5、setUpClass 启动失败），但未提供，无法判断。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139068167268

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033043003) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033043014) |
| extra-b-test-4-npu-a3 / run (1) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908707) |
| extra-b-test-2-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908772) |
| extra-b-test-16-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908798) |
| extra-b-test-4-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908800) |
| extra-b-test-1-npu-a3 / run (0) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908831) |
| extra-b-test-2-npu-a3 / run (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908863) |
| extra-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908871) |
| extra-b-test-1-npu-a3 / run (1) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139033908922) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139044579626) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139044579635) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 53.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139044579669) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45563325953/job/139068166914) |


## [Run #45560844492](https://github.com/sgl-project/sglang/actions/runs/45560844492)
- **分支**: `qwenimage21`
- **总耗时**: 40.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45560844492

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 20.3min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373320) |
| multimodal-gen-test-1-npu-a3 (0) | 19.4min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束且上传了diffusion-failures产物，推测setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373410) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139091348607) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139091348763) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139091348768) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，未见具体 Traceback；作业退出码 5 表示 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（host OOM 或进程被 SIGKILL）。已上传 diffusion-failures-npu-1-part1-2.zip 工件，需查看该工件确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373320

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest存在errors，常见于setUpClass时sglang server启动失败（如host OOM/进程被SIGKILL）。需查看省略段与diffusion-failures-npu-1-part0-2.zip确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373410




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139074750515) |
| extra-a-test-npu | 3.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139074750577) |
| multimodal-gen-test-4-npu-a3 (1) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373323) |
| multimodal-gen-test-4-npu-a3 (0) | 35.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373514) |
| extra-b-test-1-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373556) |
| extra-b-test-4-npu-a3 / run (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373595) |
| extra-b-test-4-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373599) |
| extra-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373655) |
| extra-b-test-16-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373691) |
| extra-b-test-1-npu-a3 / run (1) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373702) |
| extra-b-test-2-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373855) |
| extra-b-test-2-npu-a3 / run (1) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45560844492/job/139076373914) |


## [Run #45542499978](https://github.com/sgl-project/sglang/actions/runs/45542499978)
- **分支**: `main`
- **总耗时**: 91.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45542499978

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.7min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232133) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 5.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138989887100) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约27分钟后上传 diffusion-failures-npu-2-part0-2.zip 失败产物，退出码5对应 unittest errors，常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看产物中的 Traceback 确认具体错误。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232133

- **extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py, npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138989887100

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138965317175) |
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138965317181) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232114) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232142) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232211) |
| extra-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232254) |
| extra-b-test-2-npu-a3 / run (1) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232261) |
| extra-b-test-4-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232262) |
| extra-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232272) |
| extra-b-test-1-npu-a3 / run (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232279) |
| extra-b-test-2-npu-a3 / run (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232281) |
| extra-b-test-8-npu-a3 / run (0) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232294) |
| extra-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138966232309) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138978837891) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138978837927) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138978837959) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45542499978/job/138989887044) |


## [Run #45540562782](https://github.com/sgl-project/sglang/actions/runs/45540562782)
- **分支**: `main`
- **总耗时**: 18.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45540562782

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 12.9min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 工件，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651901) |
| multimodal-gen-test-4-npu-a3 (0) | 13.5min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651925) |
| multimodal-gen-test-1-npu-a3 (1) | 13.3min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651953) |
| multimodal-gen-test-4-npu-a3 (1) | 14.2min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651986) |
| extra-b-test-1-npu-a3 / run (0) | 14.2min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652120) |
| extra-b-test-1-npu-a3 / run (1) | 14.0min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652161) |
| extra-b-test-2-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652171) |
| extra-b-test-2-npu-a3 / run (0) | 13.7min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652203) |
| extra-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138960534090) |
| extra-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138960534157) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，未见具体 Traceback；但作业上传了 diffusion-failures-npu-1-part0-2.zip 失败工件，且用例退出码 5 通常对应 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651901

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中上传了 diffusion-failures-npu-2-part0-2.zip 失败产物，说明多模态生成用例执行出错；结合退出码 5 与背景知识，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看产物中的 Traceback 确认。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651925

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part1-2.zip 产物，说明测试用例执行失败并收集了失败信息；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651953

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part1-2.zip 失败产物，说明用例执行出错（退出码 5，unittest errors），最常见为 setUpClass 时 sglang server 启动失败（host OOM/进程被 SIGKILL）。需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959651986

- **extra-b-test-1-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest errors，多因setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652120

- **extra-b-test-1-npu-a3 / run (1)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652161


- **extra-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652203



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138958613906) |
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138958613971) |
| sgl-router-build-aarch64 / Build sgl-router | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138958690182) |
| extra-b-test-16-npu-a3 / run (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652033) |
| extra-b-test-8-npu-a3 / run (0) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45540562782/job/138959652106) |


## [Run #45523615142](https://github.com/sgl-project/sglang/actions/runs/45523615142)
- **分支**: `main`
- **总耗时**: 28.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45523615142

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 24.1min | 环境问题 | 日志被截断，无法看到真实错误，但作业退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823415) |
| extra-b-test-2-npu-a3 / run (0) | 12.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823729) |
| extra-b-test-1-npu-a3 / run (1) | 19.2min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823847) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示artifact上传与清理，中间省略部分含真实Traceback。退出码5对应unittest errors，常见于setUpClass中server启动失败（OOM/SIGKILL），需查看省略段确认具体异常。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823415

- **extra-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_compile_graph_tp2_bf16.py, npu_compile_graph_tp2_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823729

- **extra-b-test-1-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922823847

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922822409) |
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922822740) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922825050) |
| multimodal-gen-test-4-npu-a3 (1) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922825076) |
| multimodal-gen-test-1-npu-a3 (1) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922825470) |
| extra-b-test-16-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922825513) |
| extra-b-test-2-npu-a3 / run (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922826147) |
| extra-b-test-8-npu-a3 / run (0) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922826518) |
| extra-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922826523) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922826565) |
| extra-b-test-4-npu-a3 / run (1) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45523615142/job/138922826860) |


## [Run #45521709657](https://github.com/sgl-project/sglang/actions/runs/45521709657)
- **分支**: `feat/npu-dsa-int8-main-kv`
- **总耗时**: 45.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45521709657

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 14.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138923979277) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 14.9min | 环境问题 | 日志中未见明确错误，但作业失败，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138923979315) |

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志中段被省略，未见具体Traceback；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看artifact中测试日志确认真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138923979277

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 日志被截断，仅见 artifact 上传成功与清理阶段，无 Traceback/RuntimeError。按退出码 5 推断为 unittest errors，最常见是 setUpClass 时 sglang server 启动失败（host OOM 或进程被 SIGKILL），需查看被省略的测试日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138923979315

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138912359049) |
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138912359190) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395423) |
| multimodal-gen-test-1-npu-a3 (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395452) |
| multimodal-gen-test-4-npu-a3 (0) | 35.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395466) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395472) |
| extra-b-test-1-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395547) |
| extra-b-test-4-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395554) |
| extra-b-test-1-npu-a3 / run (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395575) |
| extra-b-test-4-npu-a3 / run (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395624) |
| extra-b-test-16-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395625) |
| extra-b-test-2-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395689) |
| extra-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395701) |
| extra-b-test-2-npu-a3 / run (1) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138913395841) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45521709657/job/138923979321) |


---
*Auto-generated by ci_monitor.py*