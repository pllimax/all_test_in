# NPU CI 执行监控（2026-11-24）
**生成时间**: 2026-11-25 07:06
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-24 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 24

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 247 个 | 失败 68 个 | 成功 Job 平均耗时 16.2min
- **Run 执行情况**: 成功 12 个 | 失败 12 个 | 成功 Run 平均耗时 101.3min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 73.6min | #45315933215 | [job link](https://github.com/sgl-project/sglang/actions/runs/45315933215/job/138183627275) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 68.4min | #45315933215 | [job link](https://github.com/sgl-project/sglang/actions/runs/45315933215/job/138211693200) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 56.5min | #45366853403 | [job link](https://github.com/sgl-project/sglang/actions/runs/45366853403/job/138454383876) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 56.3min | #45338516187 | [job link](https://github.com/sgl-project/sglang/actions/runs/45338516187/job/138321098673) |
| extra-b-test-2-npu-a3 / run (0) | 55.4min | #45315933215 | [job link](https://github.com/sgl-project/sglang/actions/runs/45315933215/job/138183627423) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 51.7min | #45381673274 | [job link](https://github.com/sgl-project/sglang/actions/runs/45381673274/job/138417730899) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 43.5min | #45350822358 | [job link](https://github.com/sgl-project/sglang/actions/runs/45350822358/job/138328239515) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 43.1min | #45341985334 | [job link](https://github.com/sgl-project/sglang/actions/runs/45341985334/job/138325455268) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 39.8min | #45397715382 | [job link](https://github.com/sgl-project/sglang/actions/runs/45397715382/job/138490617305) |
| extra-b-test-1-npu-a3 / run (1) | 39.2min | #45315933215 | [job link](https://github.com/sgl-project/sglang/actions/runs/45315933215/job/138183627326) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (1) | 64.2min | #45357302261 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837061) |
| multimodal-gen-test-4-npu-a3 (1) | 63.9min | #45342636530 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457938) |
| extra-b-test-16-npu-a3 / run (0) | 62.2min | #45357302261 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436836998) |
| multimodal-gen-test-4-npu-a3 (0) | 44.6min | #45342636530 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457912) |
| extra-b-test-16-npu-a3 / run (0) | 37.8min | #45323175401 | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903791) |
| multimodal-gen-test-1-npu-a3 (1) | 36.3min | #45342636530 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457825) |
| multimodal-gen-test-4-npu-a3 (0) | 35.6min | #45357302261 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837104) |
| multimodal-gen-test-1-npu-a3 (1) | 31.0min | #45357302261 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837050) |
| multimodal-gen-test-1-npu-a3 (0) | 29.5min | #45342636530 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457843) |
| multimodal-gen-test-1-npu-a3 (0) | 28.8min | #45357302261 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837078) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-b-test-16-npu-a3 / run (0) | 20 | 11 | 2 | 7 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030829)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458033) |
| extra-b-test-2-npu-a3 / run (0) | 23 | 14 | 3 | 6 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45365270238/job/138358097831)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837310)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030864) |
| extra-b-test-1-npu-a3 / run (1) | 21 | 13 | 3 | 5 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837272)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315031384)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458102) |
| extra-b-test-1-npu-a3 / run (0) | 21 | 14 | 1 | 6 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030933) |
| extra-b-test-8-npu-a3 / run (0) | 21 | 14 | 1 | 6 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837149) |
| extra-b-test-2-npu-a3 / run (1) | 23 | 17 | 1 | 4 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030936) |
| extra-b-test-4-npu-a3 / run (0) | 17 | 13 | 2 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838264)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030951) |
| extra-b-test-4-npu-a3 / run (1) | 17 | 14 | 2 | 1 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592910)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838371) |
| multimodal-gen-test-1-npu-a3 (1) | 10 | 7 | 3 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837050)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030585)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457825) |
| multimodal-gen-test-4-npu-a3 (0) | 17 | 14 | 3 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837104)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030636)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457912) |
| multimodal-gen-test-4-npu-a3 (1) | 17 | 14 | 3 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837061)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030689)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457938) |
| multimodal-gen-test-1-npu-a3 (0) | 10 | 7 | 3 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837078)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030522)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457843) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_pd_disaggregation.py` | 5 | 3 | 2 | [extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592910)<br>[extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838371) |
| `npu_speculative_moe_a2a_backend.py` | 3 | 2 | 1 | [extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458033) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 5 | 4 | 1 | [extra-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837149) |
| `npu_dp_attention.py` | 4 | 3 | 1 | [extra-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838264) |
| `ernie_image_t2i_1npu` | 4 | 3 | 1 | [multimodal-gen-test-1-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969678) |
| `npu_hicache_mha.py` | 4 | 3 | 1 | [extra-b-test-1-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458102) |
| `dspark_npu_dispatch.py` | 3 | 2 | 1 | [extra-b-test-1-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837272) |
| `npu_compile_graph_tp2_bf16.py` | 1 | 0 | 1 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837310) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #45342636530<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 71.0min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), extra-b-test-16-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45342636530) |
| #45342902628 | `dsv41-a3-dev-1112` | 68.8min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45342902628) |
| #45357302261<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 65.8min | 9 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), extra-b-test-8-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1), extra-b-test-2-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45357302261) |
| #45390677214<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 44.2min | 2 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3, extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45390677214) |
| #45323175401 | `feat/npu-none-shared-experts-fusion` | 41.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45323175401) |
| #45374533224<br>[#50691 [Feat] [NPU] moe: Add MegaMoE fused_op support for prefill and decode](https://github.com/sgl-project/sglang/pull/50691) | `feat/dev_megamoe` | 36.4min | 1 | extra-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45374533224) |
| #45178679014 | `feat/dev_megamoe` | 32.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45178679014) |
| #45346695574<br>[#38860 [Feat] [NPU] DSpark: Support static mode on GLM 5.2](https://github.com/sgl-project/sglang/pull/38860) | `feat/glm52-dspark-npu-upstream` | 23.2min | 1 | extra-b-test-2-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/45346695574) |
| #45356634455 | `codex/ascend-dsa-verify-request-shard` | 20.9min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45356634455) |
| #45365270238<br>[#52427 [Feat] [NPU] deepseek-v4.1: Capture low-ratio sources and attention in the prefill graph](https://github.com/sgl-project/sglang/pull/52427) | `dsv41-a5-graph` | 15.1min | 1 | extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45365270238) |
| #45354255174<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post14](https://github.com/sgl-project/sglang/pull/51818) | `main` | 9.9min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), extra-b-test-16-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (1), extra-b-test-4-npu-a3 / run (0), extra-b-test-1-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45354255174) |
| #45196912828 | `feat/npu-none-shared-experts-fusion` | 5.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45196912828) |

---


## [Run #45390677214](https://github.com/sgl-project/sglang/actions/runs/45390677214)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 44.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45390677214

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 7.9min | 环境问题 | 自托管 runner 的容器执行失败，jobPod 未就绪，测试未真正运行 | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138449328589) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 14.3min | 环境问题 | 精度测试作业失败，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138449328811) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 日志显示 'Executing the custom container implementation failed' 及 'jobPod must be set - ensure prepareJob completed successfully'，说明 k8s runner 容器/pod 准备阶段失败，测试脚本未执行，属 runner 基础设施问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138449328589

- **extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3**: 日志中段被省略，仅见退出码 5（unittest errors），常见于 setUpClass 时 server 启动失败（host OOM 或进程被 SIGKILL）。需查看省略部分 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138449328811

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138433543975) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138433544441) |
| extra-b-test-16-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759396) |
| extra-b-test-8-npu-a3 / run (0) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759635) |
| extra-b-test-1-npu-a3 / run (0) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759729) |
| extra-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759740) |
| extra-b-test-2-npu-a3 / run (1) | 25.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759817) |
| extra-b-test-1-npu-a3 / run (1) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759900) |
| extra-b-test-4-npu-a3 / run (1) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759957) |
| extra-b-test-4-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138434759973) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45390677214/job/138449328847) |


## [Run #45374533224](https://github.com/sgl-project/sglang/actions/runs/45374533224)
- **分支**: `feat/dev_megamoe`
- **总耗时**: 36.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45374533224

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592725) |
| extra-b-test-4-npu-a3 / run (1) | 8.2min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592910) |
| extra-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592931) |


- **extra-b-test-4-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592910


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138387956255) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138387956352) |
| multimodal-gen-test-1-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592359) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592428) |
| multimodal-gen-test-4-npu-a3 (1) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592585) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592666) |
| extra-b-test-2-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592780) |
| extra-b-test-2-npu-a3 / run (1) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389592841) |
| extra-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389593006) |
| extra-b-test-1-npu-a3 / run (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389593038) |
| extra-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45374533224/job/138389593108) |


## [Run #45365270238](https://github.com/sgl-project/sglang/actions/runs/45365270238)
- **分支**: `dsv41-a5-graph`
- **总耗时**: 15.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45365270238

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 3.8min | 环境问题 | 测试日志文件缺失，未生成 /tmp/test-logs/*.log，作业无产物上传 | [job link](https://github.com/sgl-project/sglang/actions/runs/45365270238/job/138358097831) |

- **extra-b-test-2-npu-a3 / run (0)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未产生日志，可能 server 启动失败或进程被 SIGKILL，导致无输出文件，作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/45365270238/job/138358097831

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45365270238/job/138358098163) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45365270238/job/138358099579) |
| extra-b-test-2-npu-a3 / run (1) | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45365270238/job/138358100247) |


## [Run #45357302261](https://github.com/sgl-project/sglang/actions/runs/45357302261)
- **分支**: `main`
- **总耗时**: 65.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45357302261

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 62.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436836998) |
| multimodal-gen-test-1-npu-a3 (1) | 31.0min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837050) |
| multimodal-gen-test-4-npu-a3 (1) | 64.2min | 环境问题 | multimodal 测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837061) |
| multimodal-gen-test-1-npu-a3 (0) | 28.8min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 工件，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837078) |
| multimodal-gen-test-4-npu-a3 (0) | 35.6min | 环境问题 | 多模态生成测试作业失败，日志显示上传了 diffusion-failures 产物，但未显示具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837104) |
| extra-b-test-8-npu-a3 / run (0) | 12.0min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837149) |
| extra-b-test-1-npu-a3 / run (1) | 17.5min | 环境问题 | 日志被截断，无法看到实际测试失败的错误信息，仅见 artifact 上传和清理阶段正常结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837272) |
| extra-b-test-2-npu-a3 / run (0) | 12.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837310) |
| extra-b-test-4-npu-a3 / run (0) | 15.1min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838264) |
| extra-b-test-4-npu-a3 / run (1) | 14.4min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838371) |


- **multimodal-gen-test-1-npu-a3 (1)**: 日志省略了中间部分，仅见测试后上传 diffusion-failures-npu-1-part1-3.zip 失败产物，退出码 5 提示 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837050

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业上传了 diffusion-failures-npu-2-part1-3.zip 失败工件，说明测试用例执行失败；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看工件中的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837061

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见退出后上传 diffusion-failures-npu-1-part0-3.zip（7505字节）工件，说明用例执行失败并收集了失败产物；结合退出码5，最可能是 setUpClass 时 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837078

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part0-3.zip 产物，推测测试用例执行失败（可能 setUpClass 阶段 server 启动失败或 OOM），需查看省略部分 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837104

- **extra-b-test-8-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837149

- **extra-b-test-1-npu-a3 / run (1)**: 可见日志仅包含 runner 初始化、action 下载、artifact 上传和 post-job 清理，均正常；中间省略部分才含测试执行与失败原因，无法据此判定具体错误，需查看完整日志中 Traceback/RuntimeError 或退出码 5 对应的 setUpClass 失败信息。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837272

- **extra-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_compile_graph_tp2_bf16.py, npu_compile_graph_tp2_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837310

- **extra-b-test-4-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，多为setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838264

- **extra-b-test-4-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838371

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-b-test-2-npu-a3 / run (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436837207) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838510) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436838533) |
| extra-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45357302261/job/138436840115) |


## [Run #45356634455](https://github.com/sgl-project/sglang/actions/runs/45356634455)
- **分支**: `codex/ascend-dsa-verify-request-shard`
- **总耗时**: 20.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45356634455

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332631629) |
| extra-b-test-8-npu-a3 / run (0) | 9.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332631822) |
| extra-b-test-2-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332632008) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332632031) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332632077) |
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332632324) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138331135904) |
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138331136210) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332631553) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45356634455/job/138332631690) |


## [Run #45354255174](https://github.com/sgl-project/sglang/actions/runs/45354255174)
- **分支**: `main`
- **总耗时**: 9.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45354255174

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 2.0min | 环境问题 | 日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因不明确。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030522) |
| multimodal-gen-test-1-npu-a3 (1) | 1.9min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030585) |
| multimodal-gen-test-4-npu-a3 (0) | 2.1min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，实际失败原因被省略。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030636) |
| multimodal-gen-test-4-npu-a3 (1) | 2.1min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030689) |
| extra-b-test-16-npu-a3 / run (0) | 1.9min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030829) |
| extra-b-test-2-npu-a3 / run (0) | 1.8min | 环境问题 | 测试日志文件未生成，用例脚本未产出任何日志，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030864) |
| extra-b-test-1-npu-a3 / run (0) | 1.7min | 环境问题 | 测试日志文件未生成，用例脚本未产出任何日志，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030933) |
| extra-b-test-2-npu-a3 / run (1) | 2.0min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030936) |
| extra-b-test-4-npu-a3 / run (0) | 4.1min | 环境问题 | 测试日志文件未生成，用例脚本退出码5，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030951) |
| extra-b-test-4-npu-a3 / run (1) | 4.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315031070) |
| extra-b-test-8-npu-a3 / run (0) | 6.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315031162) |
| extra-b-test-1-npu-a3 / run (1) | 1.9min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315031384) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，仅见 artifact 路径 diffusion-failures/ 无文件、Node 弃用警告和清理步骤，无 Traceback 或退出码信息，无法定位具体失败原因，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030522

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中未见具体 Traceback，但退出码5表示 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030585

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中间部分被省略，可见部分只有 Node 弃用警告和 'No files were found with the provided path: diffusion-failures/'，无 Traceback/RuntimeError。退出码 5 提示 unittest errors，可能为 setUpClass 中 server 启动失败（如 OOM/SIGKILL），但需完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030636

- **multimodal-gen-test-4-npu-a3 (1)**: 日志被截断，缺少真实错误信息；仅见上传产物路径 diffusion-failures/ 不存在，无 Traceback。需查看完整日志确认是否为 server 启动失败或环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030689

- **extra-b-test-16-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无产物上传；结合退出码 5 的常见原因，可能是 setUpClass 阶段 server 启动失败（如 host OOM 或进程被 SIGKILL），但日志中未见具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030829

- **extra-b-test-2-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 无文件，说明测试脚本未正常执行或提前退出；结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看真实 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030864

- **extra-b-test-1-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无任何 Traceback 或测试输出，说明用例在 setUpClass 启动 sglang server 阶段即失败（可能 host OOM 或进程被 SIGKILL），导致退出码 5 且无日志可上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030933

- **extra-b-test-2-npu-a3 / run (1)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未正常执行或未生成日志，随后直接进入清理阶段，无 Traceback 信息，疑似环境/runner 侧异常导致用例未运行。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030936

- **extra-b-test-4-npu-a3 / run (0)**: 日志显示未找到/tmp/test-logs/*.log，无artifacts上传；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），导致unittest出现errors，属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315030951



- **extra-b-test-1-npu-a3 / run (1)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试脚本未生成日志，结合退出码 5（unittest errors），最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例未正常执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138315031384

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138313815204) |
| extra-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45354255174/job/138313815221) |


## [Run #45346695574](https://github.com/sgl-project/sglang/actions/runs/45346695574)
- **分支**: `feat/glm52-dspark-npu-upstream`
- **总耗时**: 23.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45346695574

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (1) | 0.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691761) |
| extra-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691844) |
| extra-b-test-2-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691851) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691869) |
| extra-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691871) |
| extra-b-test-2-npu-a3 / run (1) | 19.6min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691913) |






- **extra-b-test-2-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691913

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138286574870) |
| extra-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138286574967) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691523) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691606) |
| extra-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691675) |
| extra-b-test-4-npu-a3 / run (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45346695574/job/138287691766) |


## [Run #45342902628](https://github.com/sgl-project/sglang/actions/runs/45342902628)
- **分支**: `dsv41-a3-dev-1112`
- **总耗时**: 68.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45342902628

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 27.9min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138282961752) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，多为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138282961752

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138271148303) |
| extra-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138271148353) |
| multimodal-gen-test-4-npu-a3 (0) | 37.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272401853) |
| multimodal-gen-test-4-npu-a3 (1) | 29.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272401876) |
| multimodal-gen-test-1-npu-a3 (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272401985) |
| multimodal-gen-test-1-npu-a3 (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402126) |
| extra-b-test-4-npu-a3 / run (1) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402171) |
| extra-b-test-2-npu-a3 / run (0) | 25.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402213) |
| extra-b-test-1-npu-a3 / run (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402222) |
| extra-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402271) |
| extra-b-test-2-npu-a3 / run (1) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402272) |
| extra-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402303) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402354) |
| extra-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138272402398) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138282961581) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342902628/job/138282961641) |


## [Run #45342636530](https://github.com/sgl-project/sglang/actions/runs/45342636530)
- **分支**: `main`
- **总耗时**: 71.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45342636530

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 36.3min | 环境问题 | multimodal-gen 测试用例执行失败，退出码 5 表示 unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457825) |
| multimodal-gen-test-1-npu-a3 (0) | 29.5min | 环境问题 | 多模态生成测试用例执行失败，退出码5表明unittest存在errors，疑似setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457843) |
| multimodal-gen-test-4-npu-a3 (0) | 44.6min | 其他 | 多模态生成测试失败，上传了 diffusion-failures 产物，但日志省略了真实错误信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457912) |
| multimodal-gen-test-4-npu-a3 (1) | 63.9min | 环境问题 | 多模态测试用例执行失败，上传了 diffusion-failures 失败产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457938) |
| extra-b-test-16-npu-a3 / run (0) | 19.3min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458033) |
| extra-b-test-1-npu-a3 / run (1) | 12.3min | 环境问题 | 日志中未见明确错误，但作业失败疑似 NPU 环境或 server 启动问题 | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458102) |
| extra-b-test-8-npu-a3 / run (0) | 10.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458141) |
| extra-b-test-1-npu-a3 / run (0) | 7.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458160) |
| extra-b-test-2-npu-a3 / run (0) | 5.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458239) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures 产物，未见具体 Traceback。退出码 5 对应 unittest errors，最常见为 setUpClass 时 server 启动失败（host OOM 或进程被 SIGKILL），需查看省略段真实错误确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457825

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中间省略部分未显示具体Traceback，但作业上传了diffusion-failures-npu-1-part0-2.zip失败产物，退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看省略段真实异常确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457843

- **multimodal-gen-test-4-npu-a3 (0)**: 作业退出码非0，上传了 diffusion-failures-npu-2-part0-2.zip 失败产物，说明测试用例执行失败；但日志中间被省略，未见 Traceback/RuntimeError 等真实错误，无法确定是 setUpClass 启动失败还是用例断言失败，需查看完整日志与产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457912

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业上传了 diffusion-failures-npu-2-part1-2.zip 失败产物，说明多模态生成测试用例运行失败；中间省略部分应含 Traceback/RuntimeError，但可见日志未给出具体错误，需查看失败产物或完整日志确认（可能为 server 启动失败/OOM）。
  链接: https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272457938

- **extra-b-test-16-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458033

- **extra-b-test-1-npu-a3 / run (1)**: 日志仅显示 artifact 上传成功及 Node.js 弃用警告，未包含实际测试失败信息；结合退出码 5 的常见原因，推测为 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看被省略的中间日志确认。
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458102




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138271278213) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138271278234) |
| extra-b-test-2-npu-a3 / run (1) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458140) |
| extra-b-test-4-npu-a3 / run (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458157) |
| extra-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45342636530/job/138272458223) |


## [Run #45323175401](https://github.com/sgl-project/sglang/actions/runs/45323175401)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 41.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45323175401

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903767) |
| extra-b-test-16-npu-a3 / run (0) | 37.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903791) |
| extra-b-test-2-npu-a3 / run (1) | 3.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903832) |
| extra-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903850) |
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903885) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138254903997) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138253717265) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45323175401/job/138253717292) |


## [Run #45196912828](https://github.com/sgl-project/sglang/actions/runs/45196912828)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 5.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45196912828

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138141550355) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138141550395) |
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138141550404) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138141550426) |
| extra-b-test-2-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138141550561) |
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138141550576) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138140255117) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45196912828/job/138140255252) |


## [Run #45178679014](https://github.com/sgl-project/sglang/actions/runs/45178679014)
- **分支**: `feat/dev_megamoe`
- **总耗时**: 32.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45178679014

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969836) |
| extra-b-test-2-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969870) |
| extra-b-test-1-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969888) |
| extra-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969892) |
| extra-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969936) |
| extra-b-test-16-npu-a3 / run (0) | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969952) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138138656553) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138138656588) |
| multimodal-gen-test-4-npu-a3 (0) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969618) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969628) |
| multimodal-gen-test-1-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969678) |
| multimodal-gen-test-4-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45178679014/job/138139969718) |


---
*Auto-generated by ci_monitor.py*