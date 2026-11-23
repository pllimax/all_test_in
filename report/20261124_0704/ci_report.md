# NPU CI 执行监控（2026-11-23）
**生成时间**: 2026-11-24 07:04
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-23 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 11

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 69 个 | 失败 55 个 | 成功 Job 平均耗时 16.8min
- **Run 执行情况**: 成功 1 个 | 失败 10 个 | 成功 Run 平均耗时 18.1min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 69.7min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133357) |
| extra-b-test-2-npu-a3 / run (0) | 53.4min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133576) |
| extra-b-test-1-npu-a3 / run (0) | 39.3min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133595) |
| extra-b-test-1-npu-a3 / run (1) | 38.0min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133537) |
| extra-b-test-16-npu-a3 / run (0) | 35.4min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133649) |
| extra-b-test-2-npu-a3 / run (1) | 34.1min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133435) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133127) |
| multimodal-gen-test-4-npu-a3 (0) | 32.1min | #45164873284 | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372737) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | #45158850085 | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656344889) |
| extra-b-test-2-npu-a3 / run (1) | 29.7min | #45102416083 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580414094) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 24.5min | #45102416083 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411595) |
| extra-b-test-4-npu-a3 / run (1) | 20.2min | #45102416083 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580412826) |
| multimodal-gen-test-4-npu-a3 (0) | 19.8min | #45091232234 | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386420) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | #45095332878 | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421086) |
| multimodal-gen-test-4-npu-a3 (1) | 18.0min | #45091232234 | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386468) |
| multimodal-gen-test-4-npu-a3 (0) | 17.9min | #45095214643 | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458270) |
| multimodal-gen-test-1-npu-a3 (0) | 16.5min | #45095332878 | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421070) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 11.2min | #45173089722 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751287) |
| extra-b-test-2-npu-a3 / run (0) | 11.2min | #45102416083 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411873) |
| extra-b-test-1-npu-a3 / run (1) | 7.0min | #45102416083 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411811) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-b-test-2-npu-a3 / run (0) | 10 | 1 | 1 | 8 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411873) |
| extra-b-test-2-npu-a3 / run (1) | 10 | 2 | 0 | 8 | 0 | - |
| extra-b-test-1-npu-a3 / run (1) | 9 | 1 | 1 | 7 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411811) |
| extra-b-test-8-npu-a3 / run (0) | 9 | 2 | 0 | 7 | 0 | - |
| extra-b-test-1-npu-a3 / run (0) | 9 | 2 | 0 | 7 | 0 | - |
| extra-b-test-16-npu-a3 / run (0) | 10 | 3 | 0 | 7 | 0 | - |
| multimodal-gen-test-1-npu-a3 (0) | 9 | 8 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421070) |
| multimodal-gen-test-4-npu-a3 (0) | 10 | 7 | 1 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411595) |
| multimodal-gen-test-1-npu-a3 (1) | 9 | 8 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421086) |
| extra-b-test-4-npu-a3 / run (0) | 3 | 2 | 0 | 1 | 0 | - |
| extra-b-test-4-npu-a3 / run (1) | 3 | 2 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580412826) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751287) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `qwen_image_t2i_2npu` | 9 | 6 | 3 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411595)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458270)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386420) |
| `wan2_2_t2v_14b_w8a8_2npu` | 9 | 6 | 3 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411595)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458270)<br>[multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386420) |
| `minimax_h3_t2va_2npu` | 8 | 7 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372737) |
| `npu_pd_disaggregation.py` | 3 | 2 | 1 | [extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580412826) |
| `npu_hicache_mha.py` | 2 | 1 | 1 | [extra-b-test-1-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411811) |
| `npu_device_barrier.py` | 2 | 1 | 1 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411873) |
| `npu_deepseek_v4_flash_w8a8_8p_gpqa.py` | 1 | 0 | 1 | [extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751287) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #45173089722<br>[#52545 [Fix] [NPU] tests: drop pin_memory expandable segments and fix parallel-config mock](https://github.com/sgl-project/sglang/pull/52545) | `main` | 102.0min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45173089722) |
| #45164873284<br>[#50205 [Feat] [NPU] deepseek-v4.1: Support Ascend A3 W8A8 inference and DSpark](https://github.com/sgl-project/sglang/pull/50205) | `dsv41-a3-dev-1112` | 36.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45164873284) |
| #45158850085<br>[#52418 [Refactor] [NPU] laser_attn: use the public sgl_kernel_npu operator entry](https://github.com/sgl-project/sglang/pull/52418) | `refactor/laser_attn_modify` | 35.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45158850085) |
| #45128338666<br>[#50691 [Feat] [NPU] moe: Add MegaMoE fused_op support for prefill and decode](https://github.com/sgl-project/sglang/pull/50691) | `feat/dev_megamoe` | 32.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45128338666) |
| #45095332878<br>[#44056 [Feat] [NPU] diffusion: Support Qwen-Image 2.1 and Turbo on Ascend](https://github.com/sgl-project/sglang/pull/44056) | `qwenimage21` | 32.1min | 2 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45095332878) |
| #45126808339<br>[#50691 [Feat] [NPU] moe: Add MegaMoE fused_op support for prefill and decode](https://github.com/sgl-project/sglang/pull/50691) | `feat/dev_megamoe` | 31.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45126808339) |
| #45102416083<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 25.4min | 4 | multimodal-gen-test-4-npu-a3 (0), extra-b-test-1-npu-a3 / run (1), extra-b-test-2-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45102416083) |
| #45091232234<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 23.7min | 2 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45091232234) |
| #45095214643<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 18.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45095214643) |
| #45108139047<br>[#52066 [Feat] [NPU] kimi-k3.1: Enable prefill context parallelism](https://github.com/sgl-project/sglang/pull/52066) | `kimi-k31-npu-dsa-pd-adapt` | 7.0min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45108139047) |

---


## [Run #45173089722](https://github.com/sgl-project/sglang/actions/runs/45173089722)
- **分支**: `main`
- **总耗时**: 102.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45173089722

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 11.2min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751287) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751287

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137687511501) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689132946) |
| multimodal-gen-test-4-npu-a3 (0) | 32.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133127) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133203) |
| extra-b-test-8-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133266) |
| multimodal-gen-test-1-npu-a3 (1) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133276) |
| extra-b-test-4-npu-a3 / run (0) | 69.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133357) |
| extra-b-test-2-npu-a3 / run (1) | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133435) |
| extra-b-test-4-npu-a3 / run (1) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133490) |
| extra-b-test-1-npu-a3 / run (1) | 38.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133537) |
| extra-b-test-2-npu-a3 / run (0) | 53.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133576) |
| extra-b-test-1-npu-a3 / run (0) | 39.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133595) |
| extra-b-test-16-npu-a3 / run (0) | 35.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137689133649) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751345) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45173089722/job/137727751588) |


## [Run #45164873284](https://github.com/sgl-project/sglang/actions/runs/45164873284)
- **分支**: `dsv41-a3-dev-1112`
- **总耗时**: 36.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45164873284

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372952) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372971) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664373093) |
| extra-b-test-2-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664373214) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664373390) |
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664373503) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137662937860) |
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137662937980) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372526) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372728) |
| multimodal-gen-test-4-npu-a3 (0) | 32.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372737) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45164873284/job/137664372772) |


## [Run #45158850085](https://github.com/sgl-project/sglang/actions/runs/45158850085)
- **分支**: `refactor/laser_attn_modify`
- **总耗时**: 35.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45158850085

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656344978) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656345060) |
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656345103) |
| extra-b-test-2-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656345104) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656345181) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656345254) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137654915228) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137654915234) |
| multimodal-gen-test-1-npu-a3 (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656344854) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656344867) |
| multimodal-gen-test-4-npu-a3 (0) | 31.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656344889) |
| multimodal-gen-test-4-npu-a3 (1) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45158850085/job/137656344975) |


## [Run #45128338666](https://github.com/sgl-project/sglang/actions/runs/45128338666)
- **分支**: `feat/dev_megamoe`
- **总耗时**: 32.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45128338666

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142302) |
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142308) |
| extra-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142358) |
| extra-b-test-1-npu-a3 / run (1) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142396) |
| extra-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142417) |
| extra-b-test-2-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142462) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137586865817) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137586865903) |
| multimodal-gen-test-1-npu-a3 (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142062) |
| multimodal-gen-test-4-npu-a3 (1) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142124) |
| multimodal-gen-test-1-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142214) |
| multimodal-gen-test-4-npu-a3 (0) | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45128338666/job/137588142216) |


## [Run #45126808339](https://github.com/sgl-project/sglang/actions/runs/45126808339)
- **分支**: `feat/dev_megamoe`
- **总耗时**: 31.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45126808339

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514184) |
| extra-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514204) |
| extra-b-test-2-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514237) |
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514251) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514319) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514638) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137534468356) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137534468577) |
| multimodal-gen-test-1-npu-a3 (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514074) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514091) |
| multimodal-gen-test-4-npu-a3 (0) | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514118) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514120) |
| extra-b-test-16-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514198) |
| extra-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45126808339/job/137535514225) |


## [Run #45108139047](https://github.com/sgl-project/sglang/actions/runs/45108139047)
- **分支**: `kimi-k31-npu-dsa-pd-adapt`
- **总耗时**: 7.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45108139047

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (1) | 1.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45108139047/job/137520949495) |
| extra-b-test-2-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45108139047/job/137520949542) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45108139047/job/137520949576) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45108139047/job/137519940673) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45108139047/job/137519940771) |


## [Run #45102416083](https://github.com/sgl-project/sglang/actions/runs/45102416083)
- **分支**: `main`
- **总耗时**: 25.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45102416083

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 24.5min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 失败产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411595) |
| extra-b-test-1-npu-a3 / run (1) | 7.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411811) |
| extra-b-test-2-npu-a3 / run (0) | 11.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411873) |
| extra-b-test-4-npu-a3 / run (1) | 20.2min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580412826) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-6.zip 失败产物，说明多模态生成测试存在失败用例；日志省略部分未显示具体 Traceback，无法进一步定位，需查看该 artifact 中的错误详情。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411595

- **extra-b-test-1-npu-a3 / run (1)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411811

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段被省略，未见具体Traceback；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。需查看省略部分确认真实异常。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580411873

- **extra-b-test-4-npu-a3 / run (1)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580412826

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-b-test-8-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580412990) |
| extra-b-test-1-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580413192) |
| extra-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580413243) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580413479) |
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580413651) |
| multimodal-gen-test-4-npu-a3 (1) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580413768) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580414018) |
| extra-b-test-2-npu-a3 / run (1) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580414094) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580414154) |
| extra-b-test-4-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45102416083/job/137580414465) |


## [Run #45095332878](https://github.com/sgl-project/sglang/actions/runs/45095332878)
- **分支**: `qwenimage21`
- **总耗时**: 32.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45095332878

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 16.5min | 其他 | 日志被截断，缺少实际测试错误信息，仅见产物上传成功 | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421070) |
| extra-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421082) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 失败产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421086) |
| extra-b-test-2-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421156) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421180) |
| extra-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421192) |
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421233) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421257) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中间省略，未显示 Traceback/RuntimeError 等真实错误；末尾仅显示上传 diffusion-failures 产物并清理，无法定位失败根因，需查看完整日志确认退出码 5 的具体报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421070


- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示作业上传了 diffusion-failures-npu-1-part1-2.zip 失败产物，说明多模态生成用例运行出错；中间省略部分应含 Traceback，但可见信息不足以定位具体异常，推测为 NPU 环境或 server 启动问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421086






### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137521351248) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137521351264) |
| multimodal-gen-test-4-npu-a3 (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421119) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095332878/job/137522421123) |


## [Run #45095214643](https://github.com/sgl-project/sglang/actions/runs/45095214643)
- **分支**: `main`
- **总耗时**: 18.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45095214643

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458202) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458225) |
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458237) |
| extra-b-test-2-npu-a3 / run (1) | 4.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458244) |
| multimodal-gen-test-4-npu-a3 (0) | 17.9min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458270) |
| extra-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458272) |
| extra-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458273) |





- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行了 multimodal-gen-test-4-npu-a3，最终上传 diffusion-failures-npu-2-part0-3.zip 失败产物，说明测试用例出现 errors（退出码 5），常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志省略部分未显示具体 Traceback，需查看上传的失败产物确认根因。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458270



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452458726) |
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452459304) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452459329) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452459352) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45095214643/job/137452459680) |


## [Run #45091232234](https://github.com/sgl-project/sglang/actions/runs/45091232234)
- **分支**: `main`
- **总耗时**: 23.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45091232234

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 19.8min | 环境问题 | 多模态生成测试用例执行失败，退出码5表示unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386420) |
| multimodal-gen-test-4-npu-a3 (1) | 18.0min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386468) |
| extra-b-test-8-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386517) |
| extra-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386535) |
| extra-b-test-2-npu-a3 / run (1) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386550) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386562) |
| extra-b-test-1-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386598) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386611) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中间省略部分应包含真实错误（Traceback/RuntimeError），但可见部分仅显示测试失败后上传了diffusion-failures-npu-2-part0-2.zip失败产物，最终作业失败。需查看省略日志确认server启动失败原因（如host OOM、进程被SIGKILL）。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386420

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，未见具体 Traceback；作业退出前上传了 diffusion-failures-npu-2-part1-2.zip 失败产物，结合退出码 5 推断为 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），属环境问题，需查看产物中真实错误确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386468







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137427457095) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137427457163) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386456) |
| multimodal-gen-test-1-npu-a3 (1) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45091232234/job/137428386525) |


---
*Auto-generated by ci_monitor.py*