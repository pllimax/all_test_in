# NPU CI 执行监控（2026-11-18）
**生成时间**: 2026-11-19 07:04
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-18 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 25

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 237 个 | 失败 24 个 | 成功 Job 平均耗时 15.4min
- **Run 执行情况**: 成功 16 个 | 失败 9 个 | 成功 Run 平均耗时 50.8min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 65.8min | #44302578473 | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575539) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 58.7min | #44182032017 | [job link](https://github.com/sgl-project/sglang/actions/runs/44182032017/job/134405569592) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.1min | #43915838371 | [job link](https://github.com/sgl-project/sglang/actions/runs/43915838371/job/134413406290) |
| multimodal-gen-test-4-npu-a3 (0) | 41.6min | #44010891630 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702075) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 41.4min | #44280612664 | [job link](https://github.com/sgl-project/sglang/actions/runs/44280612664/job/134753762089) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 39.3min | #44262020576 | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134684245419) |
| extra-b-test-2-npu-a3 / run (0) | 39.2min | #44292259275 | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866188) |
| extra-b-test-2-npu-a3 / run (0) | 38.4min | #44230015410 | [job link](https://github.com/sgl-project/sglang/actions/runs/44230015410/job/134679823066) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 37.6min | #44277467354 | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134731178407) |
| base-b-test-2-npu-a3 / run (0) | 37.5min | #44089596697 | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353419) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 63.6min | #44277467354 | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760718) |
| extra-b-test-2-npu-a3 / run (0) | 63.0min | #44302578473 | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575034) |
| extra-b-test-1-npu-a3 / run (0) | 62.9min | #44302578473 | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575149) |
| multimodal-gen-test-1-npu-a3 (1) | 30.3min | #44010891630 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701923) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.1min | #44010891630 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708936878) |
| base-b-test-2-npu-a3 / run (0) | 17.5min | #44040756174 | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718106) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | #44010891630 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701804) |
| extra-b-test-4-npu-a3 / run (1) | 13.3min | #44292259275 | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866132) |
| extra-b-test-16-npu-a3 / run (0) | 11.8min | #44310542336 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998730) |
| multimodal-gen-test-1-npu-a3 (1) | 11.7min | #44310542336 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998362) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-b-test-1-npu-a3 / run (0) | 8 | 6 | 1 | 1 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575149) |
| extra-b-test-4-npu-a3 / run (1) | 8 | 6 | 1 | 1 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866132) |
| multimodal-gen-test-1-npu-a3 (1) | 14 | 12 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701923) |
| multimodal-gen-test-1-npu-a3 (0) | 14 | 12 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701804) |
| multimodal-gen-test-4-npu-a3 (0) | 18 | 16 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760718) |
| extra-b-test-2-npu-a3 / run (0) | 10 | 8 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575034) |
| extra-b-test-16-npu-a3 / run (0) | 8 | 6 | 0 | 1 | 1 | - |
| extra-b-test-8-npu-a3 / run (0) | 8 | 7 | 0 | 1 | 0 | - |
| extra-b-test-4-npu-a3 / run (0) | 8 | 7 | 0 | 1 | 0 | - |
| base-b-test-2-npu-a3 / run (0) | 8 | 7 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718106) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 6 | 4 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708936878) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 5 | 4 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134539226338) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `minimax_h3_t2va_2npu` | 4 | 3 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760718) |
| `npu_speculative_multi_npu.py` | 7 | 6 | 1 | [extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866132) |
| `npu_device_barrier.py` | 5 | 4 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718106) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 3 | 2 | 1 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708936878) |
| `npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` | 2 | 1 | 1 | [base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134539226338) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #44277467354<br>[#51193 [Test] [NPU] refactor: test Laser Attn](https://github.com/sgl-project/sglang/pull/51193) | `test/npu-refactor-without-laser-attn` | 115.2min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44277467354) |
| #44262020576 | `test/npu-refactor-without-laser-attn` | 87.1min | 2 | extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3, extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44262020576) |
| #44302578473<br>[#49066 [Perf] dsv41-flash: Add FP8 DeepGEMM prefill scoring on Hopper](https://github.com/sgl-project/sglang/pull/49066) | `main` | 81.5min | 2 | extra-b-test-2-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44302578473) |
| #44010891630<br>[#44056 [Feat] [NPU] diffusion: Adapt Qwen-Image 2.1 and Turbo on Ascend](https://github.com/sgl-project/sglang/pull/44056) | `qwenimage21` | 53.6min | 3 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44010891630) |
| #44089596697 | `layer_split` | 51.0min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44089596697) |
| #44292259275<br>[#48420 [Feat] [NPU] kimi-k3.1: Add model support and route DSA attention path on Ascend](https://github.com/sgl-project/sglang/pull/48420) | `feat/dsa-routed` | 45.7min | 1 | extra-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44292259275) |
| #44040756174 | `reload-model-mx` | 35.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44040756174) |
| #44081066399<br>[#49790 [Fix] [NPU] qwen3_5_mtp: adapt mtp.fc quantization as ReplicatedLinear](https://github.com/sgl-project/sglang/pull/49790) | `qwen38_quant` | 25.8min | 1 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44081066399) |
| #44310542336<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 15.6min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), extra-b-test-2-npu-a3 / run (0), extra-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/44310542336) |

---


## [Run #44310542336](https://github.com/sgl-project/sglang/actions/runs/44310542336)
- **分支**: `dsv41-a5`
- **总耗时**: 15.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44310542336

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 11.7min | 环境问题 | 多模态生成测试用例执行失败，退出码5表示unittest存在errors，疑似setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998362) |
| multimodal-gen-test-1-npu-a3 (0) | 11.3min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998398) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败或运行报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998507) |
| multimodal-gen-test-4-npu-a3 (0) | 10.9min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 失败产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998556) |
| extra-b-test-2-npu-a3 / run (0) | 11.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998713) |
| extra-b-test-16-npu-a3 / run (0) | 11.8min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998730) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998742) |
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998744) |
| extra-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998788) |
| extra-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998941) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示上传了diffusion-failures-npu-1-part1-1.zip失败产物，说明测试用例报错。退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看产物中的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998362

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业运行了 multimodal-gen-test-1-npu-a3，最终上传 diffusion-failures-npu-1-part0-1.zip 失败产物，说明测试用例报错（退出码 5 对应 unittest errors），常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志省略段未给出具体 Traceback，需查看上传的失败产物确认根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998398

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part1-1.zip 失败产物，作业以失败结束；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998507

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明多模态生成用例运行出错（退出码5，unittest errors），常见于 setUpClass 阶段 server 启动失败（如 host OOM/进程被 SIGKILL），但省略段未含具体 Traceback，需查看失败产物确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998556

- **extra-b-test-2-npu-a3 / run (0)**: 日志仅显示artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass中sglang server启动失败（如host OOM、进程被SIGKILL），需查看上传的测试日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998713

- **extra-b-test-16-npu-a3 / run (0)**: 日志末尾仅显示artifact上传和清理，未直接给出Traceback；退出码5表示unittest存在errors，最常见为setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看上传的测试日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134824998730





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134823475214) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44310542336/job/134823475355) |


## [Run #44302578473](https://github.com/sgl-project/sglang/actions/runs/44302578473)
- **分支**: `main`
- **总耗时**: 81.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44302578473

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 63.0min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575034) |
| extra-b-test-1-npu-a3 / run (0) | 62.9min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575149) |

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段省略，未见Traceback/RuntimeError。artifact上传成功、清理正常，说明失败发生在测试执行阶段而非基础设施。退出码5对应unittest errors，最可能是setUpClass中server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575034

- **extra-b-test-1-npu-a3 / run (0)**: 日志中段省略，未见Traceback/RuntimeError。退出码5表示unittest有errors，通常为setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL）。需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575149

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134795992936) |
| multimodal-gen-test-1-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797574418) |
| multimodal-gen-test-4-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797574453) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797574456) |
| multimodal-gen-test-1-npu-a3 (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797574516) |
| extra-b-test-8-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797574869) |
| extra-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575123) |
| extra-b-test-16-npu-a3 / run (0) | 36.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575225) |
| extra-b-test-4-npu-a3 / run (0) | 65.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44302578473/job/134797575539) |


## [Run #44292259275](https://github.com/sgl-project/sglang/actions/runs/44292259275)
- **分支**: `feat/dsa-routed`
- **总耗时**: 45.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44292259275

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-4-npu-a3 / run (1) | 13.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866132) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866238) |

- **extra-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_speculative_multi_npu.py, npu_speculative_multi_npu.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866132


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134762341091) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134762341200) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866019) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866056) |
| extra-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866186) |
| extra-b-test-2-npu-a3 / run (0) | 39.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866188) |
| extra-b-test-4-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866274) |
| extra-b-test-1-npu-a3 / run (0) | 29.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44292259275/job/134763866354) |


## [Run #44277467354](https://github.com/sgl-project/sglang/actions/runs/44277467354)
- **分支**: `test/npu-refactor-without-laser-attn`
- **总耗时**: 115.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44277467354

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 63.6min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760718) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约1小时后上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例执行失败；结合退出码5的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志省略部分未显示具体 Traceback，需查看上传的失败产物确认。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760718

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134709614293) |
| extra-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134709614476) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760512) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760547) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760664) |
| extra-b-test-16-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760770) |
| extra-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760959) |
| extra-b-test-1-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710760960) |
| extra-b-test-2-npu-a3 / run (0) | 36.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710761171) |
| extra-b-test-4-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710761202) |
| extra-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134710761246) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134731178298) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 37.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134731178407) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134731180432) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 35.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134751606921) |
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44277467354/job/134751607045) |


## [Run #44262020576](https://github.com/sgl-project/sglang/actions/runs/44262020576)
- **分支**: `test/npu-refactor-without-laser-attn`
- **总耗时**: 87.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44262020576

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3 | 8.2min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，多为setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134704583274) |
| extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3 | 8.8min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134704583442) |

- **extra-c-perf-test-16-npu-a3 / extra-c-perf-test-16-npu-a3**: 日志中间省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（host OOM或进程被SIGKILL），需查看被省略的测试日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134704583274

- **extra-c-perf-test-2-npu-a3 / extra-c-perf-test-2-npu-a3**: 日志中间省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5多为setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134704583442

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134666082115) |
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134666082289) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268520) |
| multimodal-gen-test-4-npu-a3 (0) | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268590) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268608) |
| multimodal-gen-test-4-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268638) |
| extra-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268649) |
| extra-b-test-16-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268744) |
| extra-b-test-2-npu-a3 / run (0) | 35.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268753) |
| extra-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268786) |
| extra-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268813) |
| extra-b-test-1-npu-a3 / run (0) | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134667268884) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134684245357) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 39.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134684245419) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44262020576/job/134684245858) |


## [Run #44089596697](https://github.com/sgl-project/sglang/actions/runs/44089596697)
- **分支**: `layer_split`
- **总耗时**: 51.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44089596697

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.2min | 其他 | 日志片段未包含实际测试失败信息，仅显示产物上传与清理成功 | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134535767840) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.2min | 环境问题 | 精度测试作业失败，日志中段被省略，无法看到真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134535767926) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 可见日志为作业初始化与收尾阶段，测试执行部分被省略，未出现 Traceback/RuntimeError 或退出码 5 等错误，无法定位失败原因，需查看被省略的中间日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134535767840

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志仅显示artifact上传成功和清理阶段，关键测试执行段被省略，未见Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134535767926

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134517334637) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134517334649) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353107) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353125) |
| base-b-test-8-npu-a3 / run (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353361) |
| base-b-test-4-npu-a3 / run (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353389) |
| base-b-test-16-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353390) |
| base-b-test-1-npu-a3 / run (0) | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353392) |
| base-b-test-2-npu-a3 / run (0) | 37.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353419) |
| base-b-test-4-npu-a3 / run (0) | 24.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134518353449) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44089596697/job/134535767896) |


## [Run #44081066399](https://github.com/sgl-project/sglang/actions/runs/44081066399)
- **分支**: `qwen38_quant`
- **总耗时**: 25.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44081066399

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 8.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134539226338) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py, npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134539226338

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134538097286) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134538097324) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44081066399/job/134539226454) |


## [Run #44040756174](https://github.com/sgl-project/sglang/actions/runs/44040756174)
- **分支**: `reload-model-mx`
- **总耗时**: 35.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44040756174

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 17.5min | 其他 | 日志被截断，缺少真实错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718106) |

- **base-b-test-2-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、action 下载、artifact 上传和 post job 清理，均正常结束；中间省略部分才含测试执行与错误，但未提供，无法判断退出码 5 的具体 Traceback。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718106

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134858056259) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134858056375) |
| multimodal-gen-test-4-npu-a3 (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718038) |
| base-b-test-1-npu-a3 / run (0) | 31.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718387) |
| base-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859718885) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859719111) |
| base-b-test-4-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859720713) |
| base-b-test-4-npu-a3 / run (1) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859722420) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44040756174/job/134859724607) |


## [Run #44010891630](https://github.com/sgl-project/sglang/actions/runs/44010891630)
- **分支**: `qwenimage21`
- **总耗时**: 53.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44010891630

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 失败产物，疑似 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701804) |
| multimodal-gen-test-1-npu-a3 (1) | 30.3min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 NPU 上 server 启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701923) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708936878) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，未见具体 Traceback；但作业上传了 diffusion-failures-npu-1-part0-2.zip 失败产物，说明用例运行出错（退出码 5 对应 unittest errors），最常见为 setUpClass 时 server 启动失败（如 host OOM/进程被 SIGKILL）。需查看省略段确认真实异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701804

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part1-2.zip 失败产物，说明测试用例执行失败；结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），属环境/资源类问题，需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696701923

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708936878

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134695566576) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134695566609) |
| multimodal-gen-test-4-npu-a3 (1) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702036) |
| multimodal-gen-test-4-npu-a3 (0) | 41.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702075) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702176) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702185) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702210) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702340) |
| base-b-test-16-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702354) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134696702422) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708936614) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44010891630/job/134708937643) |


---
*Auto-generated by ci_monitor.py*