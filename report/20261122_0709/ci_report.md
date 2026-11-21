# NPU CI 执行监控（2026-11-21）
**生成时间**: 2026-11-22 07:03
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-21 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 5

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 49 个 | 失败 6 个 | 成功 Job 平均耗时 17.4min
- **Run 执行情况**: 成功 1 个 | 失败 4 个 | 成功 Run 平均耗时 15.3min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 68.8min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556705) |
| extra-b-test-1-npu-a3 / run (0) | 40.9min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556678) |
| extra-b-test-1-npu-a3 / run (1) | 37.6min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556735) |
| multimodal-gen-test-4-npu-a3 (0) | 36.2min | #44887668307 | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037284) |
| extra-b-test-2-npu-a3 / run (1) | 34.2min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556708) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556601) |
| multimodal-gen-test-4-npu-a3 (1) | 28.2min | #44887668307 | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037309) |
| multimodal-gen-test-4-npu-a3 (1) | 26.4min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556600) |
| multimodal-gen-test-1-npu-a3 (1) | 24.4min | #44887668307 | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037280) |
| extra-b-test-2-npu-a3 / run (1) | 24.1min | #44876487924 | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763064013) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-16-npu-a3 / run (0) | 42.0min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556650) |
| extra-b-test-16-npu-a3 / run (0) | 28.7min | #44876487924 | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063943) |
| extra-b-test-2-npu-a3 / run (0) | 21.8min | #44903052708 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556757) |
| extra-b-test-2-npu-a3 / run (0) | 11.4min | #44876487924 | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063949) |
| extra-b-test-2-npu-a3 / run (0) | 10.6min | #44887668307 | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037395) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 7.5min | #44856205466 | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128672) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-b-test-2-npu-a3 / run (0) | 4 | 1 | 3 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556757)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037395)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063949) |
| extra-b-test-16-npu-a3 / run (0) | 4 | 2 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556650)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063943) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128672) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_device_barrier.py` | 3 | 0 | 3 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556757)<br>[extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037395)<br>[extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063949) |
| `npu_speculative_moe_a2a_backend.py` | 4 | 2 | 2 | [extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556650)<br>[extra-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063943) |
| `npu_deepseek_v4_flash_w8a8_8p_gpqa.py` | 1 | 0 | 1 | [extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128672) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #44903052708<br>[#51256 [Fix] mem_cache: Carry pending request-row resets across static KV storage swaps](https://github.com/sgl-project/sglang/pull/51256) | `main` | 72.6min | 2 | extra-b-test-16-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44903052708) |
| #44856205466<br>[#50975 [Feat] [NPU] moe: Support lplb on npu](https://github.com/sgl-project/sglang/pull/50975) | `lplb` | 63.2min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44856205466) |
| #44887668307<br>[#48874 [Fix] [NPU] mooncake: Pair DSV4 and MLA KV buffers by global layer ID](https://github.com/sgl-project/sglang/pull/48874) | `fix/mooncake-ascend-dsv4-pp-main` | 39.9min | 1 | extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44887668307) |
| #44876487924<br>[#49271 [Feat] [NPU] dcp: Switch MLA and DSA to token sharding](https://github.com/sgl-project/sglang/pull/49271) | `exp/npu-dsa-token-dcp-pd` | 32.9min | 2 | extra-b-test-16-npu-a3 / run (0), extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44876487924) |

---


## [Run #44903052708](https://github.com/sgl-project/sglang/actions/runs/44903052708)
- **分支**: `main`
- **总耗时**: 72.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44903052708

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 42.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556650) |
| extra-b-test-2-npu-a3 / run (0) | 21.8min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556757) |

- **extra-b-test-16-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556650

- **extra-b-test-2-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，多为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看上传的测试日志确认。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556757

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136842879551) |
| multimodal-gen-test-1-npu-a3 (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556597) |
| multimodal-gen-test-4-npu-a3 (1) | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556600) |
| multimodal-gen-test-4-npu-a3 (0) | 34.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556601) |
| multimodal-gen-test-1-npu-a3 (1) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556637) |
| extra-b-test-1-npu-a3 / run (0) | 40.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556678) |
| extra-b-test-4-npu-a3 / run (0) | 68.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556705) |
| extra-b-test-2-npu-a3 / run (1) | 34.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556708) |
| extra-b-test-8-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556713) |
| extra-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556718) |
| extra-b-test-1-npu-a3 / run (1) | 37.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44903052708/job/136843556735) |


## [Run #44887668307](https://github.com/sgl-project/sglang/actions/runs/44887668307)
- **分支**: `fix/mooncake-ascend-dsv4-pp-main`
- **总耗时**: 39.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44887668307

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 10.6min | 环境问题 | 日志被截断，无法看到真实错误，但退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037395) |

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5多为setUpClass启动server失败（OOM/SIGKILL），需查看完整日志确认具体异常。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037395

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136796494006) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136796494059) |
| multimodal-gen-test-1-npu-a3 (1) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037280) |
| multimodal-gen-test-4-npu-a3 (0) | 36.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037284) |
| multimodal-gen-test-1-npu-a3 (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037294) |
| multimodal-gen-test-4-npu-a3 (1) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037309) |
| extra-b-test-16-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037341) |
| extra-b-test-4-npu-a3 / run (1) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037352) |
| extra-b-test-1-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037359) |
| extra-b-test-1-npu-a3 / run (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037363) |
| extra-b-test-4-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037378) |
| extra-b-test-8-npu-a3 / run (0) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037434) |
| extra-b-test-2-npu-a3 / run (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44887668307/job/136797037444) |


## [Run #44876487924](https://github.com/sgl-project/sglang/actions/runs/44876487924)
- **分支**: `exp/npu-dsa-token-dcp-pd`
- **总耗时**: 32.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44876487924

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-16-npu-a3 / run (0) | 28.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063943) |
| extra-b-test-2-npu-a3 / run (0) | 11.4min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063949) |

- **extra-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063943

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略部分确认。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063949

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 3.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136762310206) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136762310231) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063890) |
| extra-b-test-1-npu-a3 / run (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063915) |
| extra-b-test-1-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063945) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063960) |
| extra-b-test-4-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063974) |
| extra-b-test-4-npu-a3 / run (1) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063978) |
| extra-b-test-8-npu-a3 / run (0) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763063982) |
| extra-b-test-2-npu-a3 / run (1) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44876487924/job/136763064013) |


## [Run #44856205466](https://github.com/sgl-project/sglang/actions/runs/44856205466)
- **分支**: `lplb`
- **总耗时**: 63.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44856205466

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 7.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128672) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128672

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699048108) |
| extra-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699048129) |
| extra-b-test-2-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922863) |
| extra-b-test-4-npu-a3 / run (1) | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922870) |
| extra-b-test-1-npu-a3 / run (0) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922881) |
| extra-b-test-2-npu-a3 / run (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922895) |
| extra-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922900) |
| extra-b-test-16-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922906) |
| extra-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922908) |
| extra-b-test-1-npu-a3 / run (1) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136699922918) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128667) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44856205466/job/136711128671) |


---
*Auto-generated by ci_monitor.py*