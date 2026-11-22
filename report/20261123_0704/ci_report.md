# NPU CI 执行监控（2026-11-22）
**生成时间**: 2026-11-23 07:03
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-22 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 6

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 56 个 | 失败 9 个 | 成功 Job 平均耗时 16.7min
- **Run 执行情况**: 成功 1 个 | 失败 5 个 | 成功 Run 平均耗时 14.9min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-4-npu-a3 / run (0) | 69.8min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556284) |
| extra-b-test-16-npu-a3 / run (0) | 47.5min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556240) |
| multimodal-gen-test-4-npu-a3 (0) | 40.0min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556196) |
| extra-b-test-1-npu-a3 / run (0) | 39.6min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556351) |
| extra-b-test-1-npu-a3 / run (1) | 39.4min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556223) |
| extra-b-test-2-npu-a3 / run (1) | 36.4min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556275) |
| multimodal-gen-test-4-npu-a3 (1) | 33.3min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556183) |
| extra-b-test-2-npu-a3 / run (1) | 28.4min | #44989468468 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757673) |
| multimodal-gen-test-1-npu-a3 (1) | 28.3min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556146) |
| multimodal-gen-test-1-npu-a3 (0) | 26.8min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556199) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| extra-b-test-2-npu-a3 / run (0) | 24.8min | #45021365349 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556255) |
| multimodal-gen-test-4-npu-a3 (0) | 21.7min | #44989468468 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757539) |
| extra-b-test-4-npu-a3 / run (1) | 20.6min | #44989468468 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757695) |
| extra-b-test-2-npu-a3 / run (0) | 15.9min | #45007451074 | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816951) |
| extra-b-test-4-npu-a3 / run (1) | 14.8min | #44938890891 | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040731) |
| extra-b-test-2-npu-a3 / run (0) | 12.8min | #44989468468 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757620) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 12.3min | #44982779994 | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563898) |
| extra-b-test-2-npu-a3 / run (0) | 10.7min | #44938890891 | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040737) |
| extra-b-test-1-npu-a3 / run (1) | 9.2min | #44989468468 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757742) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| extra-b-test-2-npu-a3 / run (0) | 5 | 1 | 4 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556255)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816951)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757620)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040737) |
| extra-b-test-4-npu-a3 / run (1) | 5 | 3 | 2 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757695)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040731) |
| multimodal-gen-test-4-npu-a3 (0) | 4 | 3 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757539) |
| extra-b-test-1-npu-a3 / run (1) | 5 | 4 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757742) |
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 1 | 0 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563898) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_device_barrier.py` | 3 | 0 | 3 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556255)<br>[extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757620)<br>[extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040737) |
| `npu_pd_disaggregation.py` | 3 | 1 | 2 | [extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757695)<br>[extra-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040731) |
| `qwen_image_t2i_2npu` | 2 | 1 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757539) |
| `wan2_2_t2v_14b_w8a8_2npu` | 2 | 1 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757539) |
| `npu_hicache_mha.py` | 3 | 2 | 1 | [extra-b-test-1-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757742) |
| `npu_return_indexer_topk_glm52.py` | 5 | 4 | 1 | [extra-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816951) |
| `npu_deepseek_v4_flash_w8a8_8p_gpqa.py` | 1 | 0 | 1 | [extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563898) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #45021365349<br>[#52277 [Fix] sampling: Draw filler seeds per request with a secure RNG](https://github.com/sgl-project/sglang/pull/52277) | `main` | 73.5min | 1 | extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45021365349) |
| #44982779994 | `feat/npu-none-shared-experts-fusion` | 44.8min | 1 | extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44982779994) |
| #44989468468<br>[#51818 [CI] [NPU] docker: Bump CANN to 9.2.0 and NPU kernel to 2026.11.0.post12](https://github.com/sgl-project/sglang/pull/51818) | `main` | 32.0min | 4 | multimodal-gen-test-4-npu-a3 (0), extra-b-test-2-npu-a3 / run (0), extra-b-test-4-npu-a3 / run (1), extra-b-test-1-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44989468468) |
| #45007451074<br>[#49341 [Feat] NPU: support shared-expert fusion across MoE A2A backends](https://github.com/sgl-project/sglang/pull/49341) | `feat/npu-none-shared-experts-fusion` | 26.0min | 1 | extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/45007451074) |
| #44938890891<br>[#51069 [Fix] [NPU] multimodal_gen: Fix LLaDA-Image support for NPU backend](https://github.com/sgl-project/sglang/pull/51069) | `llada_image` | 24.4min | 2 | extra-b-test-4-npu-a3 / run (1), extra-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/44938890891) |

---


## [Run #45021365349](https://github.com/sgl-project/sglang/actions/runs/45021365349)
- **分支**: `main`
- **总耗时**: 73.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45021365349

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 24.8min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556255) |

- **extra-b-test-2-npu-a3 / run (0)**: 日志仅显示 runner 初始化、下载 action、上传 artifact 和清理阶段，中间省略部分未包含 Traceback/RuntimeError 等真实错误；退出码 5 提示 unittest 存在 errors，可能为 setUpClass 中 sglang server 启动失败，但需完整日志确认。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556255

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137204880426) |
| multimodal-gen-test-1-npu-a3 (1) | 28.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556146) |
| multimodal-gen-test-4-npu-a3 (1) | 33.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556183) |
| multimodal-gen-test-4-npu-a3 (0) | 40.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556196) |
| multimodal-gen-test-1-npu-a3 (0) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556199) |
| extra-b-test-1-npu-a3 / run (1) | 39.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556223) |
| extra-b-test-8-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556230) |
| extra-b-test-16-npu-a3 / run (0) | 47.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556240) |
| extra-b-test-2-npu-a3 / run (1) | 36.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556275) |
| extra-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556277) |
| extra-b-test-4-npu-a3 / run (0) | 69.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556284) |
| extra-b-test-1-npu-a3 / run (0) | 39.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45021365349/job/137205556351) |


## [Run #45007451074](https://github.com/sgl-project/sglang/actions/runs/45007451074)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 26.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/45007451074

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-2-npu-a3 / run (0) | 15.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816951) |

- **extra-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_glm52.py, npu_return_indexer_topk_glm52.py
  链接: https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816951

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162201693) |
| extra-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162201723) |
| extra-b-test-2-npu-a3 / run (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816928) |
| extra-b-test-8-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816933) |
| extra-b-test-1-npu-a3 / run (1) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816992) |
| extra-b-test-16-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816994) |
| extra-b-test-1-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162816996) |
| extra-b-test-4-npu-a3 / run (1) | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162817017) |
| extra-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/45007451074/job/137162817088) |


## [Run #44989468468](https://github.com/sgl-project/sglang/actions/runs/44989468468)
- **分支**: `main`
- **总耗时**: 32.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44989468468

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 21.7min | 其他 | 日志被截断，未见真实错误，仅显示上传了 diffusion-failures 产物，无法确定失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757539) |
| extra-b-test-2-npu-a3 / run (0) | 12.8min | 环境问题 | 日志中未见明确错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的测试执行段 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757620) |
| extra-b-test-4-npu-a3 / run (1) | 20.6min | 其他 | 日志被截断，未见真实错误，无法确定失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757695) |
| extra-b-test-1-npu-a3 / run (1) | 9.2min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757742) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，可见部分只有 runner 初始化、artifact 上传和清理，没有 Traceback/RuntimeError 等真实错误信息。产物名 diffusion-failures-npu-2-part0-1 提示多模态生成测试有失败，但具体原因需查看完整日志或该产物。
  - 失败用例: qwen_image_t2i_2npu, qwen_image_t2i_2npu, wan2_2_t2v_14b_w8a8_2npu, wan2_2_t2v_14b_w8a8_2npu, qwen_image_t2i_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757539

- **extra-b-test-2-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 selected-test-logs artifact 及 post job cleanup，均成功；失败发生在被省略的中间测试执行部分，需查看完整日志中的 Traceback/RuntimeError 才能定位，当前信息不足以判定为代码或精度问题。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757620

- **extra-b-test-4-npu-a3 / run (1)**: 日志中间省略，仅见产物上传成功与 Node.js 弃用警告，无 Traceback/RuntimeError 或退出码信息，需查看完整日志中 setUpClass 阶段错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757695

- **extra-b-test-1-npu-a3 / run (1)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757742

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107242603) |
| extra-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107242651) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757527) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757588) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757599) |
| extra-b-test-16-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757623) |
| extra-b-test-2-npu-a3 / run (1) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757673) |
| extra-b-test-8-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757738) |
| extra-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757824) |
| extra-b-test-1-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44989468468/job/137107757858) |


## [Run #44982779994](https://github.com/sgl-project/sglang/actions/runs/44982779994)
- **分支**: `feat/npu-none-shared-experts-fusion`
- **总耗时**: 44.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44982779994

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3 | 12.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563898) |

- **extra-c-acc-test-16-npu-a3 / extra-c-acc-test-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_deepseek_v4_flash_w8a8_8p_gpqa.py, npu_deepseek_v4_flash_w8a8_8p_gpqa.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563898

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137086810816) |
| extra-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137086810833) |
| extra-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212717) |
| extra-b-test-8-npu-a3 / run (0) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212748) |
| extra-b-test-4-npu-a3 / run (1) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212812) |
| extra-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212815) |
| extra-b-test-2-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212825) |
| extra-b-test-1-npu-a3 / run (1) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212849) |
| extra-b-test-2-npu-a3 / run (1) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212869) |
| extra-b-test-1-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137087212876) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563829) |
| extra-c-acc-test-2-npu-a3 / extra-c-acc-test-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44982779994/job/137092563942) |


## [Run #44938890891](https://github.com/sgl-project/sglang/actions/runs/44938890891)
- **分支**: `llada_image`
- **总耗时**: 24.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/44938890891

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| extra-b-test-4-npu-a3 / run (1) | 14.8min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040731) |
| extra-b-test-2-npu-a3 / run (0) | 10.7min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040737) |

- **extra-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040731

- **extra-b-test-2-npu-a3 / run (0)**: 日志中段省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看上传的测试日志artifact确认。
  - 失败用例: npu_device_barrier.py, npu_device_barrier.py
  链接: https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040737

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136959238730) |
| extra-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136959238817) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040562) |
| extra-b-test-16-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040573) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040581) |
| extra-b-test-1-npu-a3 / run (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040614) |
| extra-b-test-2-npu-a3 / run (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040648) |
| extra-b-test-1-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040653) |
| extra-b-test-8-npu-a3 / run (0) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040684) |
| extra-b-test-4-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/44938890891/job/136960040739) |


---
*Auto-generated by ci_monitor.py*