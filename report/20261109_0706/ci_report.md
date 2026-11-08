# NPU CI 执行监控（2026-11-08）
**生成时间**: 2026-11-09 07:06
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-08 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 58

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 547 个 | 失败 100 个 | 成功 Job 平均耗时 15.2min
- **Run 执行情况**: 成功 38 个 | 失败 20 个 | 成功 Run 平均耗时 68.6min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 78.2min | #42479417988 | [job link](https://github.com/sgl-project/sglang/actions/runs/42479417988/job/128743860570) |
| base-b-test-4-npu-a3 / run (0) | 63.6min | #42479417988 | [job link](https://github.com/sgl-project/sglang/actions/runs/42479417988/job/128728496798) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 54.9min | #42422254087 | [job link](https://github.com/sgl-project/sglang/actions/runs/42422254087/job/128558843652) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 54.2min | #42455053609 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455053609/job/128657217733) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 53.2min | #42435493775 | [job link](https://github.com/sgl-project/sglang/actions/runs/42435493775/job/128599093500) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 50.9min | #42437342616 | [job link](https://github.com/sgl-project/sglang/actions/runs/42437342616/job/128623873310) |
| base-b-test-2-npu-a3 / run (0) | 45.4min | #42479417988 | [job link](https://github.com/sgl-project/sglang/actions/runs/42479417988/job/128728496673) |
| base-b-test-16-npu-a3 / run (0) | 44.9min | #42479417988 | [job link](https://github.com/sgl-project/sglang/actions/runs/42479417988/job/128728496626) |
| multimodal-gen-test-4-npu-a3 (0) | 44.8min | #42459173751 | [job link](https://github.com/sgl-project/sglang/actions/runs/42459173751/job/128665072581) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 43.5min | #42447380316 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447380316/job/128634283468) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 38.4min | #42092516394 | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946117) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 35.2min | #42456818131 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128662788610) |
| multimodal-gen-test-4-npu-a3 (0) | 18.4min | #42447492283 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880431) |
| base-b-test-1-npu-a3 / run (0) | 18.2min | #42447492283 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880530) |
| base-b-test-4-npu-a3 / run (1) | 18.2min | #42438403292 | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759792) |
| multimodal-gen-test-4-npu-a3 (0) | 18.1min | #42448838864 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058108) |
| base-b-test-1-npu-a3 / run (0) | 18.1min | #42448838864 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058182) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | #42447492283 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880465) |
| multimodal-gen-test-4-npu-a3 (1) | 18.0min | #42448838864 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058101) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | #42447492283 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880406) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-4-npu-a3 / run (1) | 50 | 40 | 2 | 1 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767932)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759792) |
| base-b-test-16-npu-a3 / run (0) | 40 | 32 | 0 | 2 | 6 | - |
| base-b-test-2-npu-a3 / run (0) | 46 | 32 | 1 | 1 | 12 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264550) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 50 | 47 | 0 | 2 | 1 | - |
| base-b-test-4-npu-a3 / run (0) | 50 | 37 | 0 | 1 | 12 | - |
| base-b-test-8-npu-a3 / run (0) | 40 | 35 | 0 | 1 | 4 | - |
| base-b-test-1-npu-a3 / run (0) | 45 | 33 | 0 | 1 | 11 | - |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28 | 25 | 0 | 1 | 2 | - |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_pd_disaggregation.py` | 11 | 9 | 2 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767932)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759792) |
| `npu_expert_distribution_recorder_mode.py` | 6 | 5 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264550) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #42456818131<br>[#49018 [Test] scheduler: Check that a request exits and sends its final output at most once](https://github.com/sgl-project/sglang/pull/49018) | `lsyin/sched-pr28` | 61.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42456818131) |
| #42092516394 | `dspark-int8-markov-walk` | 41.8min | 3 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42092516394) |
| #42438403292<br>[#45314 [Refactor] [AMD] kimi-k3: Rename two ROCm K3 env vars and read them through Envs](https://github.com/sgl-project/sglang/pull/45314) | `k3-aiter-opt-envs` | 41.5min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42438403292) |
| #42408606337<br>[#39845 [Feat] hicache: opt-in exclusive L2->L3 tiering, dedup cache-mode L3 writes through the existence cache](https://github.com/sgl-project/sglang/pull/39845) | `pr/c-standalone` | 37.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42408606337) |
| #42450267820<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 33.4min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42450267820) |
| #42490322856<br>[#44017 [Feat] [XPU] GDN: support speculative decoding](https://github.com/sgl-project/sglang/pull/44017) | `gdn-spec-decode-xpu` | 30.7min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42490322856) |
| #42469498573<br>[#49151 [Fix] scheduler: Finish rejected requests and offloaded releases through the request retirer](https://github.com/sgl-project/sglang/pull/49151) | `lsyin/retirer-bypass` | 26.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42469498573) |
| #42454982207<br>[#49019 [Refactor] scheduler: Commit a step's result only on the rows of requests still in the batch](https://github.com/sgl-project/sglang/pull/49019) | `lsyin/sched-pr29` | 22.5min | 3 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42454982207) |
| #42448838864<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 21.7min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42448838864) |
| #42447492283<br>[#48431 [Feat] hicache: Share request-end Mamba backups](https://github.com/sgl-project/sglang/pull/48431) | `feat/hicache-mamba-request-end` | 21.4min | 6 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42447492283) |
| #42456064704<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 19.8min | 7 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42456064704) |
| #42462840074<br>[#49144 [Refactor] scheduler: Move the pause state into PauseState](https://github.com/sgl-project/sglang/pull/49144) | `lsyin/sched-pr30` | 17.9min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42462840074) |
| #42409016910 | `fix/load-snapshot-idle-publish-floor` | 14.6min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42409016910) |
| #42453813450<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 14.1min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42453813450) |
| #42454758433<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 11.9min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42454758433) |
| #42460336253<br>[#48741 [Feat] kimi-k3.1: PD disaggregation under decode context parallelism](https://github.com/sgl-project/sglang/pull/48741) | `kpham/k31-dcp-pd-hicache` | 11.0min | 1 | base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42460336253) |
| #42455553298<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 8.1min | 10 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42455553298) |
| #42457335209<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 6.4min | 10 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42457335209) |
| #42410203754 | `fix/load-snapshot-idle-publish-floor` | 6.1min | 8 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42410203754) |
| #42457737741<br>[#46694 [Perf] [AMD] minimax: decode indexer CP for DSpark verify on the NVFP4 index cache](https://github.com/sgl-project/sglang/pull/46694) | `m31-amd/indexer-cp` | 5.1min | 8 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42457737741) |

---


## [Run #42490322856](https://github.com/sgl-project/sglang/actions/runs/42490322856)
- **分支**: `gdn-spec-decode-xpu`
- **总耗时**: 30.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42490322856

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 15.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767932) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767932

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761145808) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761145820) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767862) |
| multimodal-gen-test-4-npu-a3 (1) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767880) |
| base-b-test-16-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767921) |
| base-b-test-4-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767948) |
| base-b-test-8-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767954) |
| base-b-test-1-npu-a3 / run (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767965) |
| base-b-test-2-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42490322856/job/128761767969) |


## [Run #42469498573](https://github.com/sgl-project/sglang/actions/runs/42469498573)
- **分支**: `lsyin/retirer-bypass`
- **总耗时**: 26.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42469498573

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128702400937) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128702400966) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128702400983) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128696835886) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128696835905) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469736) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469797) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469803) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469825) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469827) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469844) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469878) |
| base-b-test-4-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42469498573/job/128697469935) |


## [Run #42462840074](https://github.com/sgl-project/sglang/actions/runs/42462840074)
- **分支**: `lsyin/sched-pr30`
- **总耗时**: 17.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42462840074

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 14.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339039) |
| base-b-test-1-npu-a3 / run (0) | 14.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339068) |
| base-b-test-4-npu-a3 / run (0) | 14.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339086) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例本身已通过（OK），但在开始第3个用例时出现“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339039

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 Capturing batches 进度到 92% 后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339068

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Prefill 正常进行后突然报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码或性能问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339086

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128675807922) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128675807992) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676338980) |
| base-b-test-16-npu-a3 / run (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339031) |
| multimodal-gen-test-4-npu-a3 (1) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339043) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339069) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42462840074/job/128676339104) |


## [Run #42460336253](https://github.com/sgl-project/sglang/actions/runs/42460336253)
- **分支**: `kpham/k31-dcp-pd-hicache`
- **总耗时**: 11.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42460336253

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 7.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42460336253/job/128668587882) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 HiCache 预取正常后报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42460336253/job/128668587882

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42460336253/job/128668135511) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42460336253/job/128668135582) |
| base-b-test-4-npu-a3 / run (1) | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42460336253/job/128668587934) |


## [Run #42457737741](https://github.com/sgl-project/sglang/actions/runs/42457737741)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 5.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42457737741

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 0.6min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，jobPod 未设置导致作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935879) |
| multimodal-gen-test-1-npu-a3 (0) | 1.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935887) |
| multimodal-gen-test-4-npu-a3 (1) | 1.3min | 环境问题 | 日志被截断，未见真实错误，但作业在 checkout 后即清理退出，疑似 runner/环境异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935924) |
| base-b-test-2-npu-a3 / run (0) | 1.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935937) |
| multimodal-gen-test-4-npu-a3 (0) | 0.8min | 其他 | 日志中未见测试执行或真实错误，仅显示未找到 diffusion-failures 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935944) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935953) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935962) |
| base-b-test-4-npu-a3 / run (0) | 1.1min | 环境问题 | 日志在 checkout 后即结束，未进入测试阶段，疑似 runner 或容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935992) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 其他 | 日志在 checkout 后即结束，未显示实际测试执行或错误信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660936110) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 'Executing the custom container implementation failed' 及 'jobPod must be set - ensure prepareJob completed successfully'，属于 runner 基础设施/容器环境问题，非用例代码或精度问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935879

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见具体Traceback，但退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。另diffusion-failures目录无文件，artifact上传为空。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935887

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅显示 checkout 完成及 Node 弃用警告，随后清理孤儿进程结束，无测试执行或 Traceback。若退出码为 5，多为 setUpClass 中 sglang server 启动失败（如 host OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935924

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 apt 更新后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，容器未能启动，测试未实际执行，属 runner/容器环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935937

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和清理，没有 unittest 输出或 Traceback；唯一异常是 'No files were found with the provided path: diffusion-failures/'，说明测试可能未运行或未生成失败产物，需查看完整日志确认退出码 5 的真实原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935944

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 k8s 容器启动步骤，未进入任何测试用例，属 runner/容器环境故障，非代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935953


- **base-b-test-4-npu-a3 / run (0)**: 日志仅显示代码检出完成及 Node.js 弃用警告，随后出现 Cleaning up orphan processes，无任何测试执行或错误堆栈，未出现退出码 5 相关用例失败信息，判断为 runner/容器环境异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660935992

- **base-b-test-4-npu-a3 / run (1)**: 日志仅包含 runner 初始化、下载 action、git checkout 等步骤，随后出现 Node.js 弃用警告和清理孤儿进程，未见测试脚本运行、退出码或 Traceback，无法判定具体失败原因，需查看后续日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660936110

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660422516) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42457737741/job/128660422575) |


## [Run #42457335209](https://github.com/sgl-project/sglang/actions/runs/42457335209)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 6.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42457335209

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 2.7min | 环境问题 | 日志中未见测试用例的实际错误输出，仅显示未找到 diffusion-failures/ 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687261) |
| multimodal-gen-test-4-npu-a3 (0) | 2.5min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures 目录，作业提前结束 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687264) |
| multimodal-gen-test-4-npu-a3 (1) | 2.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687307) |
| multimodal-gen-test-1-npu-a3 (1) | 2.4min | 环境问题 | diffusion 测试失败且未生成 diffusion-failures 目录，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687327) |
| base-b-test-1-npu-a3 / run (0) | 2.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687328) |
| base-b-test-8-npu-a3 / run (0) | 2.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687333) |
| base-b-test-2-npu-a3 / run (0) | 1.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687371) |
| base-b-test-4-npu-a3 / run (0) | 2.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687389) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687412) |
| base-b-test-16-npu-a3 / run (0) | 2.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687420) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，缺少关键 Traceback。可见部分仅有 Node.js 弃用警告和 'No files were found with the provided path: diffusion-failures/'，说明测试产物目录未生成，推测测试在 setUpClass 阶段失败（如 server 启动失败），但日志中无真实错误信息，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687261

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和 artifact 上传提示“No files were found with the provided path: diffusion-failures/”，没有测试脚本输出或 Traceback，无法确认具体失败点，疑似测试未实际运行或产物目录缺失。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687264

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中无diffusion-failures产物，说明用例未正常执行；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687307

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 路径，说明测试未产出失败样本目录；结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略段中的 Traceback/RuntimeError 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687327

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 pip 安装 triton-ascend 等依赖后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687328

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 pip 安装 triton-ascend 等依赖后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687333

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 pip 安装 sglang-router 依赖时出现 ##[error]Executing the custom container implementation failed，属 runner/容器环境故障，非用例代码问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687371

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 pip 卸载 numpy/scipy 等包后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687389

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 安装 triton-ascend 等依赖过程中报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687412

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 pip 安装依赖过程中报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659687420

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659196403) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42457335209/job/128659196409) |


## [Run #42456818131](https://github.com/sgl-project/sglang/actions/runs/42456818131)
- **分支**: `lsyin/sched-pr28`
- **总耗时**: 61.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42456818131

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 35.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128662788610) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明是 runner 侧容器运行环境异常，而非用例本身的精度或代码问题；此前推理请求均正常返回 200。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128662788610

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128657572449) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128657572576) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042480) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042494) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042554) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042582) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042616) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042629) |
| base-b-test-1-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042630) |
| base-b-test-2-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128658042711) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128662788634) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456818131/job/128662788736) |


## [Run #42456064704](https://github.com/sgl-project/sglang/actions/runs/42456064704)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 19.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42456064704

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 16.1min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830860) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830878) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830886) |
| multimodal-gen-test-4-npu-a3 (1) | 15.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830941) |
| base-b-test-2-npu-a3 / run (0) | 15.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830942) |
| base-b-test-1-npu-a3 / run (0) | 15.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830969) |
| base-b-test-4-npu-a3 / run (0) | 16.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830973) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 diffusion-failures/ 目录无文件可上传，说明测试用例执行阶段出错；结合退出码5，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例 error 而非正常失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830860

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产生输出。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830878

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830886

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830941

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境异常，并非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830942

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载刚开始（0/1 shard）即报错“Executing the custom container implementation failed”，属于自托管 runner 容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830969

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明是 runner 容器环境/基础设施问题，而非用例代码或精度问题；此前 server 已正常启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830973

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655352474) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655352562) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830967) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655830980) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42456064704/job/128655831137) |


## [Run #42455553298](https://github.com/sgl-project/sglang/actions/runs/42455553298)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 8.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42455553298

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 4.3min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328189) |
| multimodal-gen-test-1-npu-a3 (0) | 4.2min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328208) |
| multimodal-gen-test-4-npu-a3 (0) | 4.2min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328259) |
| base-b-test-16-npu-a3 / run (0) | 4.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在测试启动阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328272) |
| multimodal-gen-test-4-npu-a3 (1) | 4.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328276) |
| base-b-test-8-npu-a3 / run (0) | 3.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328282) |
| base-b-test-2-npu-a3 / run (0) | 3.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328331) |
| base-b-test-1-npu-a3 / run (0) | 3.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328352) |
| base-b-test-4-npu-a3 / run (1) | 4.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328357) |
| base-b-test-4-npu-a3 / run (0) | 4.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328388) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示用例退出码5（FAILED errors=N），常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）；且未找到 diffusion-failures/ 目录，无产物上传。需查看中间省略的 Traceback 确认真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328189

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见具体 Traceback，但退出码5表明 unittest 有 errors，常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传 artifact。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328208

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业提前结束，未见具体Traceback。结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328259

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码或精度问题；测试脚本刚启动即被中断，未产生真实用例错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328272

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业提前结束。退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328276

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 k8s 容器启动环节，测试尚未真正运行，属 runner/容器环境问题，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328282

- **base-b-test-2-npu-a3 / run (0)**: 日志显示容器镜像拉取与 CANN 安装均成功，但随后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 侧容器执行环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328331

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在开始运行 test_npu_hicache_mha.py 之后、无任何用例输出，属 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328352

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，测试脚本刚启动即中断，属 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328357

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在容器启动/初始化阶段（PATH、TRITON_CACHE_DIR 打印后），未进入用例执行，属 runner/容器环境问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128654328388

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128653825496) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42455553298/job/128653825504) |


## [Run #42454982207](https://github.com/sgl-project/sglang/actions/runs/42454982207)
- **分支**: `lsyin/sched-pr29`
- **总耗时**: 22.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42454982207

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 17.5min | 环境问题 | 自托管 runner 执行自定义容器失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778007) |
| base-b-test-2-npu-a3 / run (0) | 17.3min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778028) |
| base-b-test-1-npu-a3 / run (0) | 17.7min | 环境问题 | 自托管 runner 容器执行失败，测试进程被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778036) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778007

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，并非用例代码或精度问题；测试进行到第5个用例时容器执行失败，作业随即终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778028

- **base-b-test-1-npu-a3 / run (0)**: 日志显示执行自定义容器实现失败（Executing the custom container implementation failed），发生在 test_npu_tp1_bf16 的 gsm8k 用例运行期间，属 runner/容器环境异常，非用例断言失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778036

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652277105) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652277220) |
| base-b-test-4-npu-a3 / run (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778012) |
| multimodal-gen-test-4-npu-a3 (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778024) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778047) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778065) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454982207/job/128652778102) |


## [Run #42454758433](https://github.com/sgl-project/sglang/actions/runs/42454758433)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 11.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42454758433

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 8.3min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858215) |
| multimodal-gen-test-1-npu-a3 (1) | 8.1min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858244) |
| multimodal-gen-test-4-npu-a3 (1) | 8.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858262) |
| multimodal-gen-test-4-npu-a3 (0) | 8.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858275) |
| base-b-test-4-npu-a3 / run (1) | 8.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在模型分片加载过程中被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858373) |
| base-b-test-16-npu-a3 / run (0) | 8.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858402) |
| base-b-test-2-npu-a3 / run (0) | 8.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858439) |
| base-b-test-1-npu-a3 / run (0) | 8.0min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858533) |
| base-b-test-4-npu-a3 / run (0) | 8.2min | 环境问题 | 自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858740) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产出结果；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858215

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858244

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858262

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业以退出码5结束（unittest errors），且未生成 diffusion-failures/ 目录产物。中间省略部分应含 Traceback/RuntimeError，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看完整日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858275

- **base-b-test-4-npu-a3 / run (1)**: 日志显示模型分片加载到 10/17 时出现“Executing the custom container implementation failed”，属于 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858373

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 k8s 容器启动/执行环节异常，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858402

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题；server 启动后随即报错退出，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858439

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属 self-hosted runner 容器实现故障，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858533

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 health_generate 返回 503，随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858740

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651440836) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651440898) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42454758433/job/128651858374) |


## [Run #42453813450](https://github.com/sgl-project/sglang/actions/runs/42453813450)
- **分支**: `m31-amd/indexer-cp`
- **总耗时**: 14.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42453813450

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063693) |
| base-b-test-1-npu-a3 / run (0) | 10.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063777) |
| base-b-test-2-npu-a3 / run (0) | 10.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063790) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | 环境问题 | 自定义容器执行失败，疑似 NPU 通信/存储服务异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063868) |
| base-b-test-4-npu-a3 / run (0) | 9.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063874) |
| base-b-test-16-npu-a3 / run (0) | 10.6min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063927) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业约10分钟后结束，diffusion-failures目录无文件，未上传artifact。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063693

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境故障，并非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063777

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题；此前 server 请求均返回 200，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063790

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，并伴随 AccTcpStore/SMEM 链路断开（link broken）及服务关闭，属于 runner 容器或 NPU 环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063868

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题；此前 tokenizer 已正常初始化，随后容器执行报错退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063874

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 DeepseekV3 权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063927

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128648521937) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128648522011) |
| multimodal-gen-test-4-npu-a3 (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063713) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42453813450/job/128649063864) |


## [Run #42450267820](https://github.com/sgl-project/sglang/actions/runs/42450267820)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 33.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42450267820

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 10.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264550) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264550

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128637889928) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128637889990) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264434) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264471) |
| multimodal-gen-test-4-npu-a3 (0) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264472) |
| base-b-test-16-npu-a3 / run (0) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264506) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264526) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264561) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264582) |
| base-b-test-1-npu-a3 / run (0) | 25.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264598) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42450267820/job/128638264611) |


## [Run #42448838864](https://github.com/sgl-project/sglang/actions/runs/42448838864)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 21.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42448838864

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058091) |
| multimodal-gen-test-4-npu-a3 (1) | 18.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058101) |
| multimodal-gen-test-4-npu-a3 (0) | 18.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058108) |
| base-b-test-2-npu-a3 / run (0) | 17.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058138) |
| base-b-test-1-npu-a3 / run (0) | 18.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058182) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | 环境问题 | 自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058222) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058091

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058101

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约17分钟结束，退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058108

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在执行第5个测试用例期间，属于 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058138

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在 test_npu_tp1_bf16 的 test_a_gsm8k 执行期间，属于 runner/容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058182

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 dp_attention 用例耗时824秒后，在启动 w4a4 量化用例时出现 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例代码本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058222

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128633607884) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128633607940) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058118) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058160) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058221) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42448838864/job/128634058224) |


## [Run #42447492283](https://github.com/sgl-project/sglang/actions/runs/42447492283)
- **分支**: `feat/hicache-mamba-request-end`
- **总耗时**: 21.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42447492283

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | 环境问题 | diffusion 测试失败且未生成失败产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880406) |
| multimodal-gen-test-4-npu-a3 (0) | 18.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880431) |
| multimodal-gen-test-4-npu-a3 (1) | 17.9min | 环境问题 | 作业日志被截断，未显示真实错误，但上传产物路径 diffusion-failures/ 不存在，说明测试脚本未生成失败产物，疑似 setUpClass 阶段 server 启动失败导致用例 error。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880451) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880465) |
| base-b-test-1-npu-a3 / run (0) | 18.2min | 环境问题 | 自定义容器执行失败，作业在模型权重加载完成后被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880530) |
| base-b-test-2-npu-a3 / run (0) | 18.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880651) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试用例未正常产出失败文件；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880406

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行约18分钟后失败，退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM、进程被SIGKILL）。日志中未找到diffusion-failures目录，无产物上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880431

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中仅见 'No files were found with the provided path: diffusion-failures/'，无 Traceback 可见；结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM/SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880451

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示作业运行约18分钟后结束，diffusion-failures/ 目录无文件，未上传产物。退出码5表明 unittest 有 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880465

- **base-b-test-1-npu-a3 / run (0)**: 日志显示权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 容器执行异常，非用例断言失败，需联系 runner 管理员排查容器/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880530

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 NPU 内存分配警告后立即报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880651

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629469939) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629470023) |
| base-b-test-4-npu-a3 / run (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880507) |
| base-b-test-4-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880519) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880605) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42447492283/job/128629880670) |


## [Run #42438403292](https://github.com/sgl-project/sglang/actions/runs/42438403292)
- **分支**: `k3-aiter-opt-envs`
- **总耗时**: 41.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42438403292

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 18.2min | 环境问题 | PD分离测试用例返回退出码5，setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759792) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行843秒后返回exit code 5，表明unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看日志中Traceback确认具体错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759792

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602259128) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602259172) |
| multimodal-gen-test-1-npu-a3 (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759712) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759724) |
| base-b-test-16-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759743) |
| base-b-test-8-npu-a3 / run (0) | 9.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759755) |
| base-b-test-1-npu-a3 / run (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759768) |
| multimodal-gen-test-4-npu-a3 (0) | 38.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759784) |
| multimodal-gen-test-1-npu-a3 (1) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759810) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759833) |
| base-b-test-4-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42438403292/job/128602759856) |


## [Run #42410203754](https://github.com/sgl-project/sglang/actions/runs/42410203754)
- **分支**: `fix/load-snapshot-idle-publish-floor`
- **总耗时**: 6.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42410203754

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 3.1min | 环境问题 | 上传产物时未找到 diffusion-failures 目录，测试脚本可能未生成失败产物或提前退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499108) |
| base-b-test-4-npu-a3 / run (0) | 2.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499211) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在解包依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499218) |
| multimodal-gen-test-4-npu-a3 (0) | 2.8min | 环境问题 | 日志中未见测试用例执行，仅显示未找到 diffusion-failures/ 目录，作业提前结束。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499221) |
| base-b-test-1-npu-a3 / run (0) | 3.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499223) |
| base-b-test-4-npu-a3 / run (1) | 1.0min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499264) |
| base-b-test-2-npu-a3 / run (0) | 1.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装 Rust 工具链时中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499288) |
| base-b-test-8-npu-a3 / run (0) | 2.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在安装依赖阶段被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499293) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未产出该目录，结合退出码5推测 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），导致用例 error 且无失败产物可上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499108

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 torch-npu 安装后立即报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境故障，并非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499211

- **base-b-test-16-npu-a3 / run (0)**: 日志显示解包 deb 包时出现 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499218

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，可见部分只有 runner 初始化、action 下载和清理，未出现 Traceback 或退出码 5 的用例错误；upload-artifact 提示 diffusion-failures/ 无文件，说明测试产物未生成，疑似环境或前置步骤异常导致用例未真正运行。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499221

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 SHA256 校验通过后立即报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 侧容器执行环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499223

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 apt 下载依赖过程中报错 'Executing the custom container implementation failed'，属于 runner/容器环境问题，非用例代码失败，需联系自托管 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499264

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 rustup 下载组件后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499288

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 pip 安装 sglang-router 等包后立即报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128550499293

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128549953871) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42410203754/job/128549953924) |


## [Run #42409016910](https://github.com/sgl-project/sglang/actions/runs/42409016910)
- **分支**: `fix/load-snapshot-idle-publish-floor`
- **总耗时**: 14.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42409016910

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564204) |
| base-b-test-16-npu-a3 / run (0) | 11.2min | 环境问题 | 自定义容器执行失败，作业在启动阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564284) |
| base-b-test-1-npu-a3 / run (0) | 10.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564307) |
| base-b-test-2-npu-a3 / run (0) | 11.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在加载模型分片时中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564351) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564392) |
| base-b-test-4-npu-a3 / run (0) | 9.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564474) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中未见用例收集失败，退出码5表示 unittest 有 errors，常见于 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。日志还显示 diffusion-failures/ 目录无文件，未上传产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564204

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器启动/执行环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564284

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到25%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器运行时故障，并非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564307

- **base-b-test-2-npu-a3 / run (0)**: 日志显示“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，发生在多线程加载模型分片约62%时，属于 runner/容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564351

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；此前 Gloo 仅连到 0 个 peer rank 属正常初始化输出。
  链接: https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564392

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 tokenizer 初始化后立即报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564474

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128512977810) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128512977888) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564149) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42409016910/job/128513564395) |


## [Run #42408606337](https://github.com/sgl-project/sglang/actions/runs/42408606337)
- **分支**: `pr/c-standalone`
- **总耗时**: 37.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42408606337

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308277) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308296) |
| base-b-test-4-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308304) |
| base-b-test-2-npu-a3 / run (0) | 0.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308317) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308351) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308444) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128511724134) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128511724165) |
| multimodal-gen-test-1-npu-a3 (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308224) |
| multimodal-gen-test-4-npu-a3 (1) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308252) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308270) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42408606337/job/128512308298) |


## [Run #42092516394](https://github.com/sgl-project/sglang/actions/runs/42092516394)
- **分支**: `dspark-int8-markov-walk`
- **总耗时**: 41.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42092516394

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 38.4min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946117) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128568412483) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 14.4min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128568412568) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest出现errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946117

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例或代码本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128568412483

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非用例断言失败；此前 server 请求均返回 200，未见精度或代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128568412568

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562428566) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562428583) |
| multimodal-gen-test-1-npu-a3 (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946091) |
| multimodal-gen-test-4-npu-a3 (1) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946103) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946181) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946183) |
| multimodal-gen-test-1-npu-a3 (1) | 27.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946254) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946297) |
| base-b-test-4-npu-a3 / run (1) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946307) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946322) |
| base-b-test-16-npu-a3 / run (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128562946347) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42092516394/job/128568412558) |


---
*Auto-generated by ci_monitor.py*