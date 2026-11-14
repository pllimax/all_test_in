# NPU CI 执行监控（2026-11-14）
**生成时间**: 2026-11-15 07:11
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-14 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 97

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 812 个 | 失败 132 个 | 成功 Job 平均耗时 14.3min
- **Run 执行情况**: 成功 44 个 | 失败 53 个 | 成功 Run 平均耗时 43.5min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-16-npu-a3 / run (0) | 120.5min | #43466648217 | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029019965) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 55.1min | #43410344250 | [job link](https://github.com/sgl-project/sglang/actions/runs/43410344250/job/132011790594) |
| base-b-test-2-npu-a3 / run (0) | 51.9min | #43593908249 | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833980) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 51.7min | #43394736830 | [job link](https://github.com/sgl-project/sglang/actions/runs/43394736830/job/132008435755) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 50.4min | #43569933067 | [job link](https://github.com/sgl-project/sglang/actions/runs/43569933067/job/132379637082) |
| base-b-test-16-npu-a3 / run (0) | 47.8min | #43480505399 | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743056) |
| base-b-test-16-npu-a3 / run (0) | 45.4min | #43541216378 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308591365) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 43.3min | #43573824823 | [job link](https://github.com/sgl-project/sglang/actions/runs/43573824823/job/132414720789) |
| multimodal-gen-test-4-npu-a3 (0) | 42.0min | #43589942971 | [job link](https://github.com/sgl-project/sglang/actions/runs/43589942971/job/132432922987) |
| multimodal-gen-test-4-npu-a3 (0) | 41.6min | #43452560572 | [job link](https://github.com/sgl-project/sglang/actions/runs/43452560572/job/131992284560) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-2-npu-a3 / run (0) | 79.6min | #43460782953 | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716166) |
| base-b-test-4-npu-a3 / run (0) | 54.5min | #43602552800 | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909048) |
| base-b-test-4-npu-a3 / run (0) | 43.2min | #43605345459 | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485910) |
| base-b-test-4-npu-a3 / run (1) | 35.9min | #43582924642 | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132412480651) |
| multimodal-gen-test-4-npu-a3 (0) | 35.5min | #43454286088 | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762095) |
| base-b-test-16-npu-a3 / run (0) | 32.6min | #43560525596 | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611022) |
| base-b-test-16-npu-a3 / run (0) | 30.8min | #43597487699 | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385686) |
| base-b-test-8-npu-a3 / run (0) | 28.3min | #43477934628 | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643974) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | #43554722276 | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259403) |
| base-b-test-16-npu-a3 / run (0) | 26.9min | #43491316180 | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558542) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-4-npu-a3 / run (0) | 75 | 46 | 19 | 7 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485910)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909048)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833938)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132442116743)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425840796) |
| base-b-test-16-npu-a3 / run (0) | 61 | 40 | 10 | 7 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385686)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150738)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054266)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611022)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548442) |
| base-b-test-4-npu-a3 / run (1) | 75 | 57 | 8 | 6 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548448)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744143)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290150)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193759)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081471) |
| base-b-test-8-npu-a3 / run (0) | 63 | 48 | 10 | 3 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729471)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385733)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150708)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548350)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132336376746) |
| base-b-test-1-npu-a3 / run (0) | 74 | 58 | 4 | 7 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833928)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548339)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193808)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053224804) |
| base-b-test-2-npu-a3 / run (0) | 74 | 58 | 7 | 4 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259475)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548380)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589919)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193731)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838955) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 19 | 13 | 3 | 0 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132439794633)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132338753717)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132098973874) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 36 | 33 | 0 | 2 | 1 | - |
| multimodal-gen-test-4-npu-a3 (1) | 68 | 64 | 1 | 0 | 3 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548114) |
| multimodal-gen-test-1-npu-a3 (1) | 50 | 48 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548142) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_dp_attention.py` | 34 | 21 | 13 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833938)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132442116743)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132412480671) |
| `npu_speculative_moe_a2a_backend.py` | 28 | 25 | 3 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385686)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054266)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611022) |
| `npu_mla_fia_hicache_bf16.py` | 37 | 35 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259475)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548380) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 32 | 30 | 2 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132336376746)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259469) |
| `z_image_t2i_1npu` | 29 | 28 | 1 | [multimodal-gen-test-1-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324847) |
| `qwen_image_t2i_2npu` | 31 | 30 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470908977) |
| `npu_return_indexer_topk_deepseek_v4.py` | 35 | 34 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589919) |
| `npu_return_indexer_topk_glm52.py` | 34 | 33 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360331) |
| `npu_pd_disaggregation.py` | 32 | 31 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744143) |
| `npu_sampling_backend.py` | 32 | 31 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833928) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 1 | 0 | 1 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132338753717) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43466648217<br>[#48648 [Perf] [AMD] Qwen4-Exp/HC: Fuse decode-sized hyper-connection norm and inject into FlyDSL mix](https://github.com/sgl-project/sglang/pull/48648) | `perf/amd-qwen4-fused-hc-decode` | 140.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43466648217) |
| #43460782953<br>[#50294 ci(npu): run PR test suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50294) | `ci/npu-fed-labels` | 85.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43460782953) |
| #43602552800<br>[#47588 [Feat] sail: support DeepGEMM GEMM/MoE backends [4/N]](https://github.com/sgl-project/sglang/pull/47588) | `ywj/upstream_deepgemm_split` | 58.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43602552800) |
| #43593908249<br>[#49121 [Perf] glm: Bound Triton variants on decode replay](https://github.com/sgl-project/sglang/pull/49121) | `main` | 55.0min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43593908249) |
| #43457886200<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels-b2` | 54.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43457886200) |
| #43605345459<br>[#33111 [Feat] elastic-ep: Runtime scale-down that retires EP ranks via Mooncake deactivate_ranks](https://github.com/sgl-project/sglang/pull/33111) | `qkang/elastic-ep-mooncake-scale-down` | 49.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43605345459) |
| #43557226092<br>[#46210 [Feat] [NVIDIA] megakernels: DSA / MLA binding view, EAGLE draft capture checks, early draft embedding sharing](https://github.com/sgl-project/sglang/pull/46210) | `megakernel-dsa-view-draft-capture` | 48.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43557226092) |
| #43493985219<br>[#49717 [Feat] kv-cache: Let platform plugins register KV cache dtypes](https://github.com/sgl-project/sglang/pull/49717) | `kv-cache-dtype-registry` | 45.6min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43493985219) |
| #43480726783 | `rainj-me/rust-apis-11-anthropic` | 44.3min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43480726783) |
| #43582924642<br>[#50176 [CI] disaggregation: Launch sgl-router instead of sgl-model-gateway in the PD tests](https://github.com/sgl-project/sglang/pull/50176) | `lsyin/ci-sgl-router` | 42.6min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43582924642) |
| #43592692830<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 41.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43592692830) |
| #43454286088<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels` | 40.2min | 3 | multimodal-gen-test-4-npu-a3 (0), base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43454286088) |
| #43560525596<br>[#45751 [Feat] moe: Integrate EvenMoE and retire native Waterfill/LPLB](https://github.com/sgl-project/sglang/pull/45751) | `feat/evenmoe-integration` | 39.1min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43560525596) |
| #43580773611<br>[#50389 [Perf] [NVIDIA] diffusion: Read both TP ranks' partial sums in the epilogue kernel (Z-Image, Qwen-Image-2.1)](https://github.com/sgl-project/sglang/pull/50389) | `mick/tp2-peer-partial-epilogue` | 38.5min | 5 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43580773611) |
| #43491316180<br>[#48648 [Perf] [AMD] Qwen4-Exp/HC: Fuse decode-sized hyper-connection norm and inject into FlyDSL mix](https://github.com/sgl-project/sglang/pull/48648) | `perf/amd-qwen4-fused-hc-decode` | 38.1min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43491316180) |
| #43463100952<br>[#49717 [Feat] kv-cache: Let platform plugins register KV cache dtypes](https://github.com/sgl-project/sglang/pull/49717) | `kv-cache-dtype-registry` | 36.3min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43463100952) |
| #43477934628<br>[#49170 [Fix] deepseek-v4.1: Keep active DP decode ranks out of idle tail replay](https://github.com/sgl-project/sglang/pull/49170) | `fix/dsv41-dpa-tail-decode` | 36.2min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43477934628) |
| #43492395149<br>[#46091 [Feat] usage: align prompt and cache accounting across APIs](https://github.com/sgl-project/sglang/pull/46091) | `wuyaole/feat-measured-cache-writes` | 35.5min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43492395149) |
| #43550480134<br>[#45556 [Feat] disagg: Admit the DeepSeek-V4 paged KV layout in the PD decode radix cache](https://github.com/sgl-project/sglang/pull/45556) | `feat/pd-decode-radix-linker-dsv41` | 34.5min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43550480134) |
| #43565168792<br>[#50389 [Perf] [NVIDIA] diffusion: Read both TP ranks' partial sums in the epilogue kernel (Z-Image, Qwen-Image-2.1)](https://github.com/sgl-project/sglang/pull/50389) | `mick/tp2-peer-partial-epilogue` | 34.4min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43565168792) |
| #43544568190<br>[#50122 [Feat] mem_cache: Add an opt-in state-only, cost-based eviction order for Mamba states (--radix-eviction-policy state_cost)](https://github.com/sgl-project/sglang/pull/50122) | `feat/mamba-gds-eviction-option` | 33.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43544568190) |
| #43547463420<br>[#47437 [Perf] [AMD] aiter: Run the DSpark MHA draft on non-causal unified_attention](https://github.com/sgl-project/sglang/pull/47437) | `k3/dspark-draft-unified-attn` | 33.2min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43547463420) |
| #43515190520<br>[#47342 [Feat] [AMD] kda: Add a gfx950 TLX KDA backend](https://github.com/sgl-project/sglang/pull/47342) | `tlx/kda-tlx-backend` | 33.1min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43515190520) |
| #43597487699<br>[#50122 [Feat] mem_cache: Add an opt-in state-only, cost-based eviction order for Mamba states (--radix-eviction-policy state_cost)](https://github.com/sgl-project/sglang/pull/50122) | `feat/mamba-gds-eviction-option` | 33.0min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43597487699) |
| #43467083676<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels-b2` | 32.7min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43467083676) |
| #43520701449<br>[#42254 [Perf] Foundry: adding the adapter of foundry to enable fast CUDA graph save/load](https://github.com/sgl-project/sglang/pull/42254) | `foundry-dep` | 32.6min | 4 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43520701449) |
| #43525876491<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 32.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43525876491) |
| #43549069645<br>[#46410 [Refactor] multimodal: [MM refactor 4/9] Split feature transport and preprocessing placement out of the base processor](https://github.com/sgl-project/sglang/pull/46410) | `rockdu-dev-mm-v2/04-serving-shared` | 31.6min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43549069645) |
| #43470275022<br>[#50347 ci(npu): concurrent NPU PR suite on Ascend CI runner labels [test-only]](https://github.com/sgl-project/sglang/pull/50347) | `ci/npu-fed-labels-b3` | 31.5min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43470275022) |
| #43554722276<br>[#50203 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/50203) | `main` | 31.4min | 3 | multimodal-gen-test-4-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43554722276) |
| #43590676772<br>[#49170 [Fix] deepseek-v4.1: Keep active DP decode ranks out of idle tail replay](https://github.com/sgl-project/sglang/pull/49170) | `fix/dsv41-dpa-tail-decode` | 28.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43590676772) |
| #43395080995<br>[#43852 [Feat] [NVIDIA] dsv4.1: [2/N] Add SM90 attention for packed FP4 Main KV.](https://github.com/sgl-project/sglang/pull/43852) | `feat/dsv41-packed-main-kv-sm90-attention` | 27.4min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43395080995) |
| #43488957950<br>[#43852 [Feat] [NVIDIA] dsv4.1: [2/N] Add SM90 attention for packed FP4 Main KV.](https://github.com/sgl-project/sglang/pull/43852) | `feat/dsv41-packed-main-kv-sm90-attention` | 26.6min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43488957950) |
| #43587376249<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 26.3min | 3 | base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43587376249) |
| #43566187672<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 25.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43566187672) |
| #43458547776<br>[#42745 [Fix] radix_cache: Cap SWA lock-walk pinning at one window in the Rust TreeCore](https://github.com/sgl-project/sglang/pull/42745) | `fix/swa-window-lock-walk-split` | 25.0min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43458547776) |
| #43543828891<br>[#50213 [Feat] scheduler: Keep a reserve of KV and state slots for cached prefixes (--prefill-cache-reserve)](https://github.com/sgl-project/sglang/pull/50213) | `feat/hold-cold-prefill-admission` | 24.8min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43543828891) |
| #43534903019<br>[#50400 [Perf] sampling: Re-derive the top-k flags when a running batch drops rows](https://github.com/sgl-project/sglang/pull/50400) | `oss-sync-6a82a0d84a` | 23.9min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43534903019) |
| #43480930973<br>[#50213 [Feat] scheduler: Keep a reserve of KV and state slots for cached prefixes (--prefill-cache-reserve)](https://github.com/sgl-project/sglang/pull/50213) | `feat/hold-cold-prefill-admission` | 23.6min | 3 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43480930973) |
| #43606755131<br>[#48409 [Feat] scheduler: add fixed-batch bounded LPM policy](https://github.com/sgl-project/sglang/pull/48409) | `codex/bounded-lpm-window` | 23.1min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43606755131) |
| #43577363257 | `kvshard/rocm-aiter-mori` | 23.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43577363257) |
| #43541844206<br>[#50213 [Feat] scheduler: Keep a reserve of KV and state slots for cached prefixes (--prefill-cache-reserve)](https://github.com/sgl-project/sglang/pull/50213) | `feat/hold-cold-prefill-admission` | 22.1min | 4 | base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43541844206) |
| #43558190606<br>[#49328 [Fix] hicache: Report L3 prefetch tokens already cached during the read](https://github.com/sgl-project/sglang/pull/49328) | `shuwen/hicache-host-covered-reason` | 22.0min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43558190606) |
| #43553796590<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 21.5min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43553796590) |
| #43582594190<br>[#48090 [Perf] [AMD] spec: Skip the vocabulary-wide sort in MTP rejection-sampling verify](https://github.com/sgl-project/sglang/pull/48090) | `rocm-sparse-rejection-target-probs` | 21.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43582594190) |
| #43541216378<br>[#50203 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/50203) | `main` | 20.7min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43541216378) |
| #43591113376<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 19.8min | 7 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43591113376) |
| #43551197305 | `kvshard/rocm-aiter-mori` | 19.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43551197305) |
| #43480505399 | `rainj-me/rust-apis-02-pause-and-frontend-state` | 18.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43480505399) |
| #43467523704<br>[#50213 [Feat] scheduler: Keep a reserve of KV and state slots for cached prefixes (--prefill-cache-reserve)](https://github.com/sgl-project/sglang/pull/50213) | `feat/hold-cold-prefill-admission` | 15.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43467523704) |
| #43543574440 | `test/rlhf-test-coverage` | 10.7min | 1 | base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43543574440) |
| #43565653520<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 7.3min | 7 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43565653520) |
| #43565317177<br>[#49896 [Feat] entrypoints: Require --admin-api-key for sensitive admin endpoints](https://github.com/sgl-project/sglang/pull/49896) | `feat/admin-force-endpoints` | 5.8min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43565317177) |

---


## [Run #43606755131](https://github.com/sgl-project/sglang/actions/runs/43606755131)
- **分支**: `codex/bounded-lpm-window`
- **总耗时**: 23.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43606755131

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 13.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729448) |
| base-b-test-8-npu-a3 / run (0) | 9.4min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729471) |
| base-b-test-4-npu-a3 / run (1) | 16.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729476) |
| base-b-test-1-npu-a3 / run (0) | 12.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729492) |
| base-b-test-2-npu-a3 / run (0) | 16.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729493) |
| base-b-test-4-npu-a3 / run (0) | 12.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729674) |





- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例本身已通过（Ran 1 test OK），随后报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729493


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483050285) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483050289) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729354) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43606755131/job/132483729366) |


## [Run #43605345459](https://github.com/sgl-project/sglang/actions/runs/43605345459)
- **分支**: `qkang/elastic-ep-mooncake-scale-down`
- **总耗时**: 49.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43605345459

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 16.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485884) |
| base-b-test-4-npu-a3 / run (0) | 43.2min | 环境问题 | 安装依赖 memfabric-hybrid==1.3.0 失败，找不到匹配版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485910) |
| base-b-test-1-npu-a3 / run (0) | 12.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485924) |
| base-b-test-8-npu-a3 / run (0) | 13.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485962) |


- **base-b-test-4-npu-a3 / run (0)**: pip 安装 memfabric-hybrid==1.3.0 时提示 from versions: none，无可用发行版，导致进程退出码 1，作业失败。属于依赖包源/环境配置问题，非代码逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485910



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132478809659) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132478809745) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485758) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485773) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485788) |
| multimodal-gen-test-4-npu-a3 (0) | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485790) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485862) |
| base-b-test-16-npu-a3 / run (0) | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43605345459/job/132479485906) |


## [Run #43602552800](https://github.com/sgl-project/sglang/actions/runs/43602552800)
- **分支**: `ywj/upstream_deepgemm_split`
- **总耗时**: 58.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43602552800

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470908999) |
| base-b-test-4-npu-a3 / run (0) | 54.5min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909048) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470359646) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470359650) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470908904) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470908948) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470908977) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470908997) |
| base-b-test-16-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909027) |
| base-b-test-8-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909039) |
| base-b-test-4-npu-a3 / run (1) | 26.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909068) |
| base-b-test-2-npu-a3 / run (0) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602552800/job/132470909081) |


## [Run #43597487699](https://github.com/sgl-project/sglang/actions/runs/43597487699)
- **分支**: `feat/mamba-gds-eviction-option`
- **总耗时**: 33.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43597487699

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 30.8min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385686) |
| base-b-test-8-npu-a3 / run (0) | 11.8min | 环境问题 | pip 安装 triton-ascend 依赖 pandas 时找不到匹配版本，导致依赖安装失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385733) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385686

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 pip 解析 triton-ascend 依赖时，pandas 无可用版本（from versions: none），报 No matching distribution found，进程退出码 1，属依赖源/网络环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385733

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-1-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473385669) |
| base-b-test-4-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473386419) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473386520) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473386535) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387131) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387163) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387198) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387317) |
| base-b-test-2-npu-a3 / run (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387346) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387399) |
| sgl-router-build-aarch64 / Build sgl-router | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43597487699/job/132473387623) |


## [Run #43593908249](https://github.com/sgl-project/sglang/actions/runs/43593908249)
- **分支**: `main`
- **总耗时**: 55.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43593908249

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 18.2min | 代码错误 | NPU采样后端测试用例执行失败，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833928) |
| base-b-test-4-npu-a3 / run (0) | 11.4min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 报 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833938) |

- **base-b-test-1-npu-a3 / run (0)**: test_npu_sampling_backend.py 返回退出码1，13个用例仅1个通过，该测试文件失败导致作业失败；日志未显示具体Traceback，需查看该用例详细输出定位根因。
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833928

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例后 FAILED (errors=1)，退出码 1，导致 0/2 通过。错误多源于 setUpClass 阶段 server 启动失败（如 OOM 或进程被 SIGKILL），需查看日志中 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833938

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444342070) |
| multimodal-gen-test-4-npu-a3 (0) | 29.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833807) |
| multimodal-gen-test-4-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833831) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833849) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833853) |
| base-b-test-8-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833869) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833943) |
| base-b-test-16-npu-a3 / run (0) | 35.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833947) |
| base-b-test-2-npu-a3 / run (0) | 51.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43593908249/job/132444833980) |


## [Run #43592692830](https://github.com/sgl-project/sglang/actions/runs/43592692830)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 41.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43592692830

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.8min | 代码错误 | NPU DP attention 测试用例执行失败，23个测试中1个error导致退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132442116743) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行23个测试出现1个error（FAILED errors=1），耗时369秒后返回退出码1，导致该文件判定失败，整体2个用例0通过。需查看具体Traceback定位是setUpClass中server启动失败还是用例本身异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132442116743

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132440971102) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132440971130) |
| sgl-router-build-aarch64 / Build sgl-router | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441014294) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485229) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485237) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485240) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485244) |
| base-b-test-1-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485280) |
| base-b-test-16-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485309) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485312) |
| base-b-test-2-npu-a3 / run (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132441485808) |
| base-b-test-4-npu-a3 / run (1) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43592692830/job/132442116718) |


## [Run #43591113376](https://github.com/sgl-project/sglang/actions/runs/43591113376)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 19.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43591113376

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465172) |
| multimodal-gen-test-4-npu-a3 (0) | 15.9min | 环境问题 | multimodal 测试作业失败，未生成 diffusion-failures 产物，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465207) |
| multimodal-gen-test-4-npu-a3 (1) | 15.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465213) |
| base-b-test-4-npu-a3 / run (0) | 16.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465254) |
| base-b-test-1-npu-a3 / run (0) | 16.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465255) |
| base-b-test-2-npu-a3 / run (0) | 4.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465284) |
| base-b-test-16-npu-a3 / run (0) | 16.0min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465287) |
| base-b-test-4-npu-a3 / run (1) | 15.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465378) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件可上传，说明测试用例执行失败未产出结果。退出码5表示unittest存在errors，最常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465172

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中 upload-artifact 提示未找到 diffusion-failures/ 目录，说明测试未正常产出失败样本；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志省略段未显示具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465207

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾显示未找到diffusion-failures/目录，无产物上传；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465213

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 server 已正常启动并返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465254

- **base-b-test-1-npu-a3 / run (0)**: 日志显示下载 action 超时重试，随后 apt 更新时出现 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465255


- **base-b-test-16-npu-a3 / run (0)**: 日志显示下载 action 超时重试后，apt 更新阶段报错“Executing the custom container implementation failed”，属 runner 容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465287

- **base-b-test-4-npu-a3 / run (1)**: 日志显示依赖安装正常后出现 'Executing the custom container implementation failed'，属 runner/容器环境问题，非用例代码错误；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465378

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132435925867) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132435925914) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465179) |
| base-b-test-8-npu-a3 / run (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43591113376/job/132436465253) |


## [Run #43590676772](https://github.com/sgl-project/sglang/actions/runs/43590676772)
- **分支**: `fix/dsv41-dpa-tail-decode`
- **总耗时**: 28.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43590676772

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 4.1min | 环境问题 | 依赖包 memfabric-hybrid==1.3.0 在镜像源中找不到，安装失败导致作业退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132439794633) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 pip 安装 memfabric-hybrid==1.3.0 时提示 'from versions: none'，即当前镜像/源无该版本，进程退出码 1，属依赖环境缺失，非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132439794633

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132434632615) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132434632730) |
| base-b-test-2-npu-a3 / run (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132435265072) |
| base-b-test-4-npu-a3 / run (1) | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132435265079) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132435265082) |
| base-b-test-4-npu-a3 / run (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132435265126) |
| base-b-test-16-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43590676772/job/132435265128) |


## [Run #43587376249](https://github.com/sgl-project/sglang/actions/runs/43587376249)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 26.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43587376249

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 16.1min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150708) |
| base-b-test-16-npu-a3 / run (0) | 10.8min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 Rust 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150738) |
| base-b-test-4-npu-a3 / run (0) | 19.8min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425840796) |

- **base-b-test-8-npu-a3 / run (0)**: pip 构建 sglang-router wheel 时，openssl-sys 需要 pkg-config 查找 OpenSSL，但环境中未安装 pkg-config，cargo 编译失败（exit 101），最终 wheel 构建失败、作业退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150708

- **base-b-test-16-npu-a3 / run (0)**: pip 构建 sglang-router wheel 时，openssl-sys 编译需要 pkg-config 但环境中未安装，cargo 编译失败退出码 101，最终作业以 exit code 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150738

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 cargo 编译 openssl-sys 时找不到 pkg-config 工具，sglang-router wheel 构建失败，退出码 1。属于 CI 环境缺少依赖，非代码逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425840796

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132424766435) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132424766517) |
| sgl-router-build-aarch64 / Build sgl-router | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132424803110) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150656) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150702) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150735) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425150762) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43587376249/job/132425840789) |


## [Run #43582924642](https://github.com/sgl-project/sglang/actions/runs/43582924642)
- **分支**: `lsyin/ci-sgl-router`
- **总耗时**: 42.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43582924642

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 35.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在下载 artifact 后中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132412480651) |
| base-b-test-4-npu-a3 / run (0) | 26.5min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132412480671) |

- **base-b-test-4-npu-a3 / run (1)**: 日志显示下载 sgl-router 产物后约27分钟报错：Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132412480651

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132412480671

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411406850) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411406865) |
| sgl-router-build-aarch64 / Build sgl-router | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411439408) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411927912) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411927919) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411927931) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411927972) |
| base-b-test-8-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411927979) |
| base-b-test-16-npu-a3 / run (0) | 33.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411928009) |
| base-b-test-2-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411928024) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582924642/job/132411928033) |


## [Run #43582594190](https://github.com/sgl-project/sglang/actions/runs/43582594190)
- **分支**: `rocm-sparse-rejection-target-probs`
- **总耗时**: 21.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43582594190

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 6.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43582594190/job/132410842719) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582594190/job/132410401646) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582594190/job/132410401699) |
| base-b-test-1-npu-a3 / run (0) | 6.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582594190/job/132410842678) |
| base-b-test-4-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43582594190/job/132410842745) |


## [Run #43580773611](https://github.com/sgl-project/sglang/actions/runs/43580773611)
- **分支**: `mick/tp2-peer-partial-epilogue`
- **总耗时**: 38.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43580773611

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 6.9min | 环境问题 | Pod 镜像拉取失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548114) |
| multimodal-gen-test-1-npu-a3 (1) | 7.3min | 环境问题 | Pod 镜像拉取失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548142) |
| base-b-test-4-npu-a3 / run (0) | 6.8min | 环境问题 | Pod 镜像拉取失败导致容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548278) |
| base-b-test-1-npu-a3 / run (0) | 6.8min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548339) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548350) |

- **multimodal-gen-test-4-npu-a3 (1)**: 容器 "job" 报 ErrImagePull，持续 300 秒超过宽限期仍未恢复，Pod 处于 Pending。需检查镜像名/tag 是否存在、私有仓库 imagePullSecret 凭据、节点到仓库的网络（DNS/防火墙/代理/TLS）。
  链接: https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548114

- **multimodal-gen-test-1-npu-a3 (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过300秒宽限期，Pod 一直 Pending，作业无法执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548142

- **base-b-test-4-npu-a3 / run (0)**: 容器 job 报 ErrImagePull，超过 300 秒宽限期仍未恢复，Pod 一直 Pending。需检查镜像名/tag 是否存在、私有仓库 imagePullSecret 凭据，以及节点到仓库的网络（DNS、防火墙、代理、TLS）。
  链接: https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548278

- **base-b-test-1-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败超过300秒，Pod 一直 Pending。需检查镜像名/tag 是否存在、私有仓库 imagePullSecret 凭据，以及节点到仓库的网络（DNS/防火墙/代理/TLS）。
  链接: https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548339

- **base-b-test-8-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败（ImagePullBackOff），超过300秒宽限期，Pod 一直 Pending，作业未执行任何测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548350

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132404936908) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132404936990) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548146) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548168) |
| base-b-test-16-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548261) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548282) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43580773611/job/132405548309) |


## [Run #43577363257](https://github.com/sgl-project/sglang/actions/runs/43577363257)
- **分支**: `kvshard/rocm-aiter-mori`
- **总耗时**: 23.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43577363257

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 10.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43577363257/job/132395113901) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43577363257/job/132394536216) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43577363257/job/132394536320) |
| base-b-test-4-npu-a3 / run (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43577363257/job/132395113898) |
| base-b-test-1-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43577363257/job/132395113903) |
| base-b-test-2-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43577363257/job/132395114008) |


## [Run #43566187672](https://github.com/sgl-project/sglang/actions/runs/43566187672)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 25.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43566187672

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 10.7min | 代码错误 | NPU DP attention 测试用例执行失败，23个测试中1个报错，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270333) |
| base-b-test-16-npu-a3 / run (0) | 14.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270339) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行321秒后 FAILED (errors=1)，2个文件中0个通过。日志未显示具体 Traceback，推测为用例内部异常（可能 setUpClass 阶段 server 启动失败），需查看完整错误堆栈定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270333


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132360697159) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132360697160) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270192) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270295) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270305) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270306) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270316) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43566187672/job/132361270332) |


## [Run #43565653520](https://github.com/sgl-project/sglang/actions/runs/43565653520)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 7.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43565653520

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 1.7min | 环境问题 | 测试脚本未生成 diffusion-failures 目录，疑似用例执行失败或 setUpClass 阶段 server 启动异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982198) |
| multimodal-gen-test-4-npu-a3 (0) | 2.1min | 环境问题 | 上传产物路径 diffusion-failures/ 不存在，未找到任何文件 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982229) |
| base-b-test-8-npu-a3 / run (0) | 1.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982251) |
| base-b-test-2-npu-a3 / run (0) | 1.9min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982256) |
| base-b-test-4-npu-a3 / run (1) | 1.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖包阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982275) |
| base-b-test-1-npu-a3 / run (0) | 1.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在安装依赖阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982292) |
| base-b-test-4-npu-a3 / run (0) | 1.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982306) |
| base-b-test-16-npu-a3 / run (0) | 1.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982314) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试用例未产出失败样本目录；结合退出码 5 的常见原因，可能是 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），但日志中未见明确 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982198

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 'No files were found with the provided path: diffusion-failures/. No artifacts will be uploaded.'，说明测试未生成失败产物目录，可能是用例未执行或产物路径配置错误；日志中未见 Traceback/RuntimeError，无法确认 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982229

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 pip 安装依赖后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982251

- **base-b-test-2-npu-a3 / run (0)**: 日志显示解包依赖包后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982256

- **base-b-test-4-npu-a3 / run (1)**: 日志显示在解包 libavcodec58 等 deb 包时出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属于 runner/容器环境故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982275

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 pip 安装 sglang-router 依赖后立即报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，非代码或测试用例问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982292

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 debconf 警告后出现 ##[error]Executing the custom container implementation failed，提示联系自托管 runner 管理员，属 runner/容器环境问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359982306


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359318500) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565653520/job/132359318519) |


## [Run #43565317177](https://github.com/sgl-project/sglang/actions/runs/43565317177)
- **分支**: `feat/admin-force-endpoints`
- **总耗时**: 5.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43565317177

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 1.4min | 环境问题 | multimodal 测试未生成 diffusion-failures 目录，疑似用例执行阶段失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389363) |
| multimodal-gen-test-4-npu-a3 (1) | 1.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389394) |
| base-b-test-8-npu-a3 / run (0) | 2.4min | 环境问题 | 日志在 checkout 后即结束，未进入测试阶段，疑似 runner 或容器环境异常导致作业中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389423) |
| base-b-test-2-npu-a3 / run (0) | 1.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装依赖阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389497) |
| base-b-test-16-npu-a3 / run (0) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在安装 Rust 阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389498) |
| base-b-test-4-npu-a3 / run (0) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389513) |
| base-b-test-1-npu-a3 / run (0) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389516) |
| base-b-test-4-npu-a3 / run (1) | 1.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在环境准备阶段中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389517) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试未产出失败样本目录；结合退出码 5，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389363

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中未见具体Traceback，但退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。另diffusion-failures目录无文件，artifact未上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389394

- **base-b-test-8-npu-a3 / run (0)**: 日志仅显示代码检出完成及 k8s 脚本启动，随后出现 Node.js 弃用警告和清理孤儿进程，无任何测试执行或 Traceback，作业在测试前终止，属环境/基础设施问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389423

- **base-b-test-2-npu-a3 / run (0)**: 日志显示在 apt 安装 python3.10 等依赖后报错 'Executing the custom container implementation failed'，属于 runner/容器环境问题，非用例代码错误，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389497

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题；随后作业进入清理阶段，未执行到测试。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389498

- **base-b-test-4-npu-a3 / run (0)**: 日志显示安装依赖后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，非用例代码失败，需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389513

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 apt 解包 libpython3.10-stdlib 时出现 find: '/usr/lib/python3': No such file or directory，随后报错 'Executing the custom container implementation failed'，属于 runner/容器环境异常，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389516

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 apt 安装依赖后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，非用例或代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132358389517

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132357884810) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565317177/job/132357884821) |


## [Run #43565168792](https://github.com/sgl-project/sglang/actions/runs/43565168792)
- **分支**: `mick/tp2-peer-partial-epilogue`
- **总耗时**: 34.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43565168792

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 26.4min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054266) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054266

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132357404138) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132357404158) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054216) |
| multimodal-gen-test-1-npu-a3 (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054226) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054239) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054254) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054280) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054288) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054295) |
| base-b-test-4-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054310) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43565168792/job/132358054315) |


## [Run #43560525596](https://github.com/sgl-project/sglang/actions/runs/43560525596)
- **分支**: `feat/evenmoe-integration`
- **总耗时**: 39.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43560525596

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 32.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611022) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611022

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343065993) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343066116) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343610888) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343610889) |
| multimodal-gen-test-4-npu-a3 (0) | 27.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343610894) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343610905) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343610979) |
| base-b-test-4-npu-a3 / run (1) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611009) |
| base-b-test-4-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611011) |
| base-b-test-8-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611033) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43560525596/job/132343611052) |


## [Run #43558190606](https://github.com/sgl-project/sglang/actions/runs/43558190606)
- **分支**: `shuwen/hicache-host-covered-reason`
- **总耗时**: 22.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43558190606

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 10.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132336376746) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132336376746

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132335816763) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132335816808) |
| base-b-test-4-npu-a3 / run (1) | 5.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132336376708) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43558190606/job/132336376753) |


## [Run #43557876060](https://github.com/sgl-project/sglang/actions/runs/43557876060)
- **分支**: `main`
- **总耗时**: 6.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43557876060

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132403471970) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402679199) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402679604) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402768842) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402769049) |
| multimodal-gen-test-4-npu-a3 (0) | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402772141) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402772918) |
| base-b-test-1-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402808550) |
| base-b-test-16-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402813656) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402824180) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402825564) |
| base-b-test-4-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402825721) |
| base-b-test-8-npu-a3 / run (0) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132402826008) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132403409464) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557876060/job/132403409844) |


## [Run #43557226092](https://github.com/sgl-project/sglang/actions/runs/43557226092)
- **分支**: `megakernel-dsa-view-draft-capture`
- **总耗时**: 48.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43557226092

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 17.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132338753717) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132338753723) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132338753717


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132332808427) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132332808519) |
| multimodal-gen-test-1-npu-a3 (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462160) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462227) |
| multimodal-gen-test-1-npu-a3 (1) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462275) |
| multimodal-gen-test-4-npu-a3 (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462297) |
| base-b-test-1-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462330) |
| base-b-test-8-npu-a3 / run (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462371) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462385) |
| base-b-test-16-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462388) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462435) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132333462448) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43557226092/job/132338753815) |


## [Run #43554722276](https://github.com/sgl-project/sglang/actions/runs/43554722276)
- **分支**: `main`
- **总耗时**: 31.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43554722276

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259403) |
| base-b-test-8-npu-a3 / run (0) | 9.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259469) |
| base-b-test-2-npu-a3 / run (0) | 7.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259475) |
| base-b-test-16-npu-a3 / run (0) | 14.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259501) |
| base-b-test-4-npu-a3 / run (0) | 13.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259562) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示用例以退出码5结束（unittest errors），且未生成 diffusion-failures 目录产物；结合背景知识，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259403

- **base-b-test-8-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259469

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259475



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132326642600) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132326642631) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259402) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259408) |
| multimodal-gen-test-4-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259462) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259548) |
| base-b-test-1-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43554722276/job/132327259614) |


## [Run #43553796590](https://github.com/sgl-project/sglang/actions/runs/43553796590)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 21.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43553796590

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 7.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548380) |
| base-b-test-1-npu-a3 / run (0) | 8.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548406) |
| base-b-test-4-npu-a3 / run (0) | 6.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548418) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | 环境问题 | 容器内 aiohttp 版本过旧，与 Python 3.12 不兼容导致语法错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548442) |
| base-b-test-4-npu-a3 / run (1) | 18.3min | 环境问题 | 容器内 aiohttp 版本过旧，与 Python 3.12 不兼容导致语法错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548448) |

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548380



- **base-b-test-16-npu-a3 / run (0)**: 导入 aiohttp 时 helpers.py 中 asyncio.async 在 Python 3.12 已移除，触发 SyntaxError，run_suite.py 无法启动，进程退出码 1。属镜像依赖版本不匹配的环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548442

- **base-b-test-4-npu-a3 / run (1)**: aiohttp/helpers.py 使用 asyncio.async（Python 3.7 已移除），在 Python 3.12 下报 SyntaxError，导入 sglang 失败，测试脚本无法启动。需升级镜像中 aiohttp 版本。
  链接: https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548448

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322074296) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322074300) |
| base-b-test-8-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43553796590/job/132322548455) |


## [Run #43551197305](https://github.com/sgl-project/sglang/actions/runs/43551197305)
- **分支**: `kvshard/rocm-aiter-mori`
- **总耗时**: 19.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43551197305

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 7.2min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132314408597) |

- **base-b-test-4-npu-a3 / run (0)**: pip 安装 sglang-router 时，cargo 编译 openssl-sys 因找不到 pkg-config 工具而失败（exit 101），wheel 构建失败，作业退出码 1。属于 CI 镜像缺少构建依赖的环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132314408597

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132313899794) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132313899892) |
| base-b-test-2-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132314408569) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132314408607) |
| base-b-test-1-npu-a3 / run (0) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43551197305/job/132314408616) |


## [Run #43550480134](https://github.com/sgl-project/sglang/actions/runs/43550480134)
- **分支**: `feat/pd-decode-radix-linker-dsv41`
- **总耗时**: 34.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43550480134

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 7.8min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 出现 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374537) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例后 FAILED (errors=1)，退出码 1，2 个测试文件 0/2 通过。日志未显示具体 Traceback，推测 setUpClass 阶段 server 启动异常，需查看完整错误定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374537

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132311663745) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132311663751) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374425) |
| base-b-test-8-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374509) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374517) |
| base-b-test-16-npu-a3 / run (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374531) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374556) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374570) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43550480134/job/132312374639) |


## [Run #43549069645](https://github.com/sgl-project/sglang/actions/runs/43549069645)
- **分支**: `rockdu-dev-mm-v2/04-serving-shared`
- **总耗时**: 31.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43549069645

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 4.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324982) |
| base-b-test-4-npu-a3 / run (0) | 8.4min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 出现 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308325033) |


- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例后 FAILED (errors=1)，退出码 1，2 个测试文件 0/2 通过。错误发生在 setUpClass 阶段（如 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308325033

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132307619200) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132307619239) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324844) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324847) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324872) |
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324889) |
| base-b-test-2-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324921) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324946) |
| base-b-test-8-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308324953) |
| base-b-test-1-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43549069645/job/132308325150) |


## [Run #43547463420](https://github.com/sgl-project/sglang/actions/runs/43547463420)
- **分支**: `k3/dspark-draft-unified-attn`
- **总耗时**: 33.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43547463420

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 6.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744066) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744143) |


- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 143 秒后 FAILED (errors=1)，2 个用例 0 通过，进程退出码 1，导致作业失败；具体错误需查看被省略的 Traceback。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744143

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302131560) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302131567) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302743948) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302743960) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302743998) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744028) |
| base-b-test-16-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744034) |
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744053) |
| base-b-test-8-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744060) |
| base-b-test-1-npu-a3 / run (0) | 27.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43547463420/job/132302744290) |


## [Run #43544568190](https://github.com/sgl-project/sglang/actions/runs/43544568190)
- **分支**: `feat/mamba-gds-eviction-option`
- **总耗时**: 33.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43544568190

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 10.6min | 代码错误 | test_npu_dp_attention.py 中 23 个用例有 1 个 error，导致该文件退出码 1，整体 0/2 通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501085) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，该文件返回 exit code 1，测试汇总 0/2 passed。错误发生在用例执行阶段（可能为 setUpClass 中 server 启动失败），需查看具体 Traceback 定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501085

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340011644) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340011679) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501000) |
| multimodal-gen-test-4-npu-a3 (0) | 28.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501010) |
| multimodal-gen-test-4-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501029) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501033) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501082) |
| base-b-test-2-npu-a3 / run (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501091) |
| base-b-test-16-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501111) |
| base-b-test-8-npu-a3 / run (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501117) |
| base-b-test-1-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43544568190/job/132340501179) |


## [Run #43543828891](https://github.com/sgl-project/sglang/actions/runs/43543828891)
- **分支**: `feat/hold-cold-prefill-admission`
- **总耗时**: 24.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43543828891

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.1min | 代码错误 | test_npu_dp_attention.py 中 23 个用例有 1 个 error，导致该文件退出码 1，整体 0/2 通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398871) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示该测试文件 Ran 23 tests，FAILED (errors=1)，退出码 1，属于 unittest 用例执行报错（可能为 setUpClass 阶段 server 启动失败），非超时或环境问题。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398871

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132339897007) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132339897019) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398746) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398785) |
| base-b-test-4-npu-a3 / run (1) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398821) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398851) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398869) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398888) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543828891/job/132340398914) |


## [Run #43543574440](https://github.com/sgl-project/sglang/actions/runs/43543574440)
- **分支**: `test/rlhf-test-coverage`
- **总耗时**: 10.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43543574440

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 7.1min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43543574440/job/132290281687) |
| base-b-test-1-npu-a3 / run (0) | 2.7min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43543574440/job/132290281706) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543574440/job/132289590037) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43543574440/job/132289590077) |


## [Run #43541844206](https://github.com/sgl-project/sglang/actions/runs/43541844206)
- **分支**: `feat/hold-cold-prefill-admission`
- **总耗时**: 22.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43541844206

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 17.6min | 环境问题 | 自托管 runner 执行自定义容器失败，作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633200) |
| base-b-test-2-npu-a3 / run (0) | 15.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633203) |
| base-b-test-4-npu-a3 / run (0) | 10.8min | 代码错误 | test_npu_dp_attention.py 中 23 个用例有 1 个 error，导致该文件退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633236) |
| base-b-test-1-npu-a3 / run (0) | 15.0min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633303) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示在加载模型分片约82%时出现“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例代码问题，需联系自托管 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633200

- **base-b-test-2-npu-a3 / run (0)**: 日志显示服务初始化后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境故障，并非用例或代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633203

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，该文件返回 exit code 1，最终 0/2 通过。错误发生在用例执行阶段（可能为 setUpClass 中 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633236

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 容器运行时故障，并非用例或代码本身的问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633303

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284087821) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284087850) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633130) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633194) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633199) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541844206/job/132284633241) |


## [Run #43541216378](https://github.com/sgl-project/sglang/actions/runs/43541216378)
- **分支**: `main`
- **总耗时**: 20.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43541216378

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 20.2min | 代码错误 | test_npu_return_indexer_topk_deepseek_v4.py 用例执行失败，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589919) |
| base-b-test-4-npu-a3 / run (0) | 12.3min | 代码错误 | test_npu_dp_attention.py 中 23 个用例有 1 个 error，导致该文件退出码 1，测试失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589986) |

- **base-b-test-2-npu-a3 / run (0)**: TIMINGS 显示 test/registered/npu/rl/indexer_replay/test_npu_return_indexer_topk_deepseek_v4.py 的 passed 为 false（耗时 162s），其余用例均通过，最终进程以 exit code 1 结束。日志省略了该用例的具体 Traceback，需查看该文件日志确认是 setUpClass 启动失败还是断言错误。
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589919

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，该文件返回 exit code 1，Test Summary 0/2 passed。错误发生在用例执行阶段（可能为 setUpClass 中 server 启动失败），需查看具体 Traceback 定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589986

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-1-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308589940) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308590458) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308590738) |
| base-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308590795) |
| multimodal-gen-test-4-npu-a3 (1) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308590825) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308590828) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308591197) |
| base-b-test-16-npu-a3 / run (0) | 45.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308591365) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308591651) |
| multimodal-gen-test-1-npu-a3 (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43541216378/job/132308591701) |


## [Run #43534903019](https://github.com/sgl-project/sglang/actions/runs/43534903019)
- **分支**: `oss-sync-6a82a0d84a`
- **总耗时**: 23.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43534903019

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 4.0min | 环境问题 | 编译 sglang-router 时缺少 pkg-config，导致 OpenSSL 构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290150) |

- **base-b-test-4-npu-a3 / run (1)**: 构建 sglang-router 的 Rust 扩展时，openssl-sys 需要 pkg-config 来定位 OpenSSL，但容器内未安装该工具，cargo 编译失败（exit 101），wheel 构建失败，作业退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290150

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132261564456) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132261564473) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262289962) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262289991) |
| base-b-test-4-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290092) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290109) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290191) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290219) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43534903019/job/132262290290) |


## [Run #43525876491](https://github.com/sgl-project/sglang/actions/runs/43525876491)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 32.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43525876491

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669664) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132231577527) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132231577561) |
| multimodal-gen-test-4-npu-a3 (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669373) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669377) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669392) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669460) |
| base-b-test-1-npu-a3 / run (0) | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669669) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669727) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669734) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669778) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43525876491/job/132232669809) |


## [Run #43520701449](https://github.com/sgl-project/sglang/actions/runs/43520701449)
- **分支**: `foundry-dep`
- **总耗时**: 32.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43520701449

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 3.2min | 环境问题 | pip 安装 sglang-router 构建依赖时无法获取 setuptools>=45，导致构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193731) |
| base-b-test-4-npu-a3 / run (1) | 2.2min | 环境问题 | pip 安装 uv 失败，找不到可用版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193759) |
| base-b-test-1-npu-a3 / run (0) | 5.2min | 环境问题 | 安装 Rust 工具链时下载超时导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193808) |
| base-b-test-16-npu-a3 / run (0) | 3.2min | 环境问题 | pip 安装 sglang-router 时访问 pypi.org 超时，导致构建依赖失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193867) |

- **base-b-test-2-npu-a3 / run (0)**: 容器内 pip 安装 sglang-router 时，构建依赖 setuptools>=45 无法从索引获取（versions: none），疑似代理/镜像源不可达或索引配置问题，属环境依赖下载失败，非代码逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193731

- **base-b-test-4-npu-a3 / run (1)**: 容器内 pip 升级后执行安装 uv 时，报错 Could not find a version that satisfies the requirement uv (from versions: none)，无匹配发行版，导致步骤退出码 1，作业失败。属依赖源/网络环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193759

- **base-b-test-1-npu-a3 / run (0)**: 脚本检测到未安装 cargo，通过 rustup 安装 1.92 工具链，下载 channel-rust-1.92.toml 时网络超时（operation timed out），退出码 1，属网络/环境问题，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193808

- **base-b-test-16-npu-a3 / run (0)**: 日志显示连接 pypi.org 读取超时（read timeout=15），随后安装 setuptools>=45 时找不到可用版本，sglang-router 构建依赖安装失败，进程退出码 1。属于网络/代理环境问题，非代码缺陷。
  链接: https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193867

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132214117473) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132214117530) |
| multimodal-gen-test-4-npu-a3 (0) | 29.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193630) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193638) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193704) |
| multimodal-gen-test-4-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193717) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193856) |
| base-b-test-4-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43520701449/job/132215193891) |


## [Run #43515190520](https://github.com/sgl-project/sglang/actions/runs/43515190520)
- **分支**: `tlx/kda-tlx-backend`
- **总耗时**: 33.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43515190520

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.8min | 代码错误 | test_npu_dp_attention.py 中 23 个用例有 1 个 error，导致该文件退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513278) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513702) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，该文件返回 exit code 1，最终 0/2 通过。错误发生在用例执行阶段（可能是 setUpClass 中 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513278

- **base-b-test-16-npu-a3 / run (0)**: cargo 编译 openssl-sys 需要 pkg-config 工具，但容器镜像中未安装，导致 sglang-router wheel 构建失败，pip 安装报错退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513702

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132195450327) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132195450411) |
| multimodal-gen-test-1-npu-a3 (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196512961) |
| multimodal-gen-test-1-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513051) |
| multimodal-gen-test-4-npu-a3 (0) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513075) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513157) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513162) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513217) |
| base-b-test-1-npu-a3 / run (0) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513264) |
| base-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43515190520/job/132196513537) |


## [Run #43493985219](https://github.com/sgl-project/sglang/actions/runs/43493985219)
- **分支**: `kv-cache-dtype-registry`
- **总耗时**: 45.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43493985219

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 19.6min | 环境问题 | 容器内 aiohttp 版本过旧，与 Python 3.12 不兼容导致语法错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593573) |

- **base-b-test-16-npu-a3 / run (0)**: aiohttp/helpers.py 第25行使用 asyncio.async，该语法在 Python 3.12 已非法，导入 sglang 时即报 SyntaxError，测试脚本无法启动。需升级/固定 aiohttp 版本。
  链接: https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593573

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132122383111) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132122383114) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593280) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593297) |
| multimodal-gen-test-4-npu-a3 (0) | 24.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593346) |
| base-b-test-1-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593391) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593402) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593472) |
| base-b-test-2-npu-a3 / run (0) | 40.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593578) |
| base-b-test-4-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593690) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43493985219/job/132123593767) |


## [Run #43492395149](https://github.com/sgl-project/sglang/actions/runs/43492395149)
- **分支**: `wuyaole/feat-measured-cache-writes`
- **总耗时**: 35.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43492395149

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 10.0min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081471) |
| base-b-test-8-npu-a3 / run (0) | 10.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081525) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081530) |
| base-b-test-1-npu-a3 / run (0) | 9.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081707) |

- **base-b-test-4-npu-a3 / run (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 300 秒后超过宽限期，Pod 一直处于 Pending。需检查镜像名/标签是否存在、私有仓库的 imagePullSecret 凭据，以及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081471




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132116922366) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132116922370) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081167) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081170) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081219) |
| multimodal-gen-test-4-npu-a3 (0) | 30.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081376) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081451) |
| base-b-test-2-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43492395149/job/132118081562) |


## [Run #43491316180](https://github.com/sgl-project/sglang/actions/runs/43491316180)
- **分支**: `perf/amd-qwen4-fused-hc-decode`
- **总耗时**: 38.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43491316180

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 26.9min | 环境问题 | 网络连接中断导致 pip 下载 fastapi 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558542) |
| base-b-test-4-npu-a3 / run (1) | 8.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558804) |

- **base-b-test-16-npu-a3 / run (0)**: 下载 fastapi-0.75.1 时连接反复中断，重试6次仍收到0字节，pip 报 incomplete-download 错误，进程退出码1。属网络/代理环境问题，非代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558542


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132113183366) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132113183732) |
| multimodal-gen-test-4-npu-a3 (0) | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558071) |
| multimodal-gen-test-1-npu-a3 (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558286) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558302) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558446) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558471) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558571) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558622) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43491316180/job/132114558785) |


## [Run #43488957950](https://github.com/sgl-project/sglang/actions/runs/43488957950)
- **分支**: `feat/dsv41-packed-main-kv-sm90-attention`
- **总耗时**: 26.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43488957950

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 17.8min | 代码错误 | NPU DP attention 测试用例执行失败，23个测试中1个报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194502) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行345秒后 FAILED (errors=1)，退出码1，2个测试文件0/2通过。错误发生在测试执行阶段，可能为 setUpClass 中 server 启动失败或用例断言异常，需查看具体 Traceback 定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194502

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132298396495) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132298396533) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194354) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194393) |
| base-b-test-2-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194411) |
| base-b-test-8-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194464) |
| base-b-test-16-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194510) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194524) |
| base-b-test-4-npu-a3 / run (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43488957950/job/132299194551) |


## [Run #43480930973](https://github.com/sgl-project/sglang/actions/runs/43480930973)
- **分支**: `feat/hold-cold-prefill-admission`
- **总耗时**: 23.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43480930973

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 10.3min | 环境问题 | pip 安装 uv 失败，找不到可用版本，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457451) |
| base-b-test-4-npu-a3 / run (0) | 12.1min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457584) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | 环境问题 | K8s Pod 拉取镜像失败，容器进入 ImagePullBackOff 状态 | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457696) |

- **base-b-test-16-npu-a3 / run (0)**: 容器内 pip 升级到 26.3 后执行安装 uv，报错 Could not find a version that satisfies the requirement uv (from versions: none)，无匹配发行版，疑似代理/镜像源不可达或索引配置问题，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457451

- **base-b-test-4-npu-a3 / run (0)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败并重试超过 300 秒，Pod 一直 Pending，导致作业在启动阶段即失败，与测试代码无关。
  链接: https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457584

- **base-b-test-4-npu-a3 / run (1)**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 300 秒后超过宽限期，Pod 一直处于 Pending，作业无法启动。需检查镜像名/tag、私有仓库凭据及节点到仓库的网络连通性。
  链接: https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457696

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132116057099) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132116057114) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457226) |
| multimodal-gen-test-4-npu-a3 (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457236) |
| base-b-test-1-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457472) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457637) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480930973/job/132117457673) |


## [Run #43480726783](https://github.com/sgl-project/sglang/actions/runs/43480726783)
- **分支**: `rainj-me/rust-apis-11-anthropic`
- **总耗时**: 44.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43480726783

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132077884560) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | 环境问题 | pip 安装 uv 失败，找不到可用版本，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132077884668) |


- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 升级后执行安装 uv 时报错：Could not find a version that satisfies the requirement uv (from versions: none)，随后进程以退出码 1 结束，属于依赖源/网络环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132077884668

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132076480528) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132076480572) |
| base-b-test-1-npu-a3 / run (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132077884480) |
| base-b-test-4-npu-a3 / run (0) | 39.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480726783/job/132077884580) |


## [Run #43480505399](https://github.com/sgl-project/sglang/actions/runs/43480505399)
- **分支**: `rainj-me/rust-apis-02-pause-and-frontend-state`
- **总耗时**: 18.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43480505399

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229741204) |

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229741204

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-4-npu-a3 / run (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229741162) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229742557) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743032) |
| base-b-test-16-npu-a3 / run (0) | 47.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743056) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743514) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743521) |
| base-b-test-2-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743860) |
| base-b-test-1-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229743914) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43480505399/job/132229744012) |


## [Run #43477934628](https://github.com/sgl-project/sglang/actions/runs/43477934628)
- **分支**: `fix/dsv41-dpa-tail-decode`
- **总耗时**: 36.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43477934628

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 28.3min | 环境问题 | 下载依赖包时代理返回503，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643974) |

- **base-b-test-8-npu-a3 / run (0)**: 从gh-proxy下载custom-ops压缩包时连接中断，重试后squid代理返回503 Service Unavailable，进程退出码1，属网络/代理环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643974

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132078342176) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132078342492) |
| base-b-test-2-npu-a3 / run (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643693) |
| base-b-test-4-npu-a3 / run (1) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643705) |
| base-b-test-16-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643759) |
| base-b-test-4-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43477934628/job/132079643792) |


## [Run #43470275022](https://github.com/sgl-project/sglang/actions/runs/43470275022)
- **分支**: `ci/npu-fed-labels-b3`
- **总耗时**: 31.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43470275022

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 10.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838955) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132040183726) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132040183884) |
| multimodal-gen-test-4-npu-a3 (0) | 27.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041837903) |
| multimodal-gen-test-4-npu-a3 (1) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041837955) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838069) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838113) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838815) |
| base-b-test-4-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838884) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041838913) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041839021) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43470275022/job/132041839509) |


## [Run #43467523704](https://github.com/sgl-project/sglang/actions/runs/43467523704)
- **分支**: `feat/hold-cold-prefill-admission`
- **总耗时**: 15.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43467523704

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049813546) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049813690) |
| base-b-test-8-npu-a3 / run (0) | 9.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049813830) |
| base-b-test-4-npu-a3 / run (1) | 8.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049814004) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049814095) |






### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132048502199) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132048502310) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049813396) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049813479) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467523704/job/132049813923) |


## [Run #43467083676](https://github.com/sgl-project/sglang/actions/runs/43467083676)
- **分支**: `ci/npu-fed-labels-b2`
- **总耗时**: 32.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43467083676

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 8.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629849) |
| base-b-test-1-npu-a3 / run (0) | 8.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629906) |
| base-b-test-8-npu-a3 / run (0) | 2.5min | 环境问题 | 容器内未安装 sglang 包，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030630151) |



- **base-b-test-8-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明测试镜像/环境中缺少 sglang 安装（未执行 pip install -e . 或 PYTHONPATH 未设置），进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030630151

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132029353642) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132029353718) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629623) |
| multimodal-gen-test-4-npu-a3 (0) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629701) |
| multimodal-gen-test-4-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629748) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629787) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030629944) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030630022) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43467083676/job/132030630112) |


## [Run #43466648217](https://github.com/sgl-project/sglang/actions/runs/43466648217)
- **分支**: `perf/amd-qwen4-fused-hc-decode`
- **总耗时**: 140.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43466648217

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132098973867) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 13.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132098973874) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132027778708) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132027778826) |
| multimodal-gen-test-1-npu-a3 (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029019773) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029019891) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029019931) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029019939) |
| base-b-test-16-npu-a3 / run (0) | 120.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029019965) |
| base-b-test-8-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029020019) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029020142) |
| base-b-test-4-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029020158) |
| base-b-test-2-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029020199) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132029020223) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43466648217/job/132098973968) |


## [Run #43463100952](https://github.com/sgl-project/sglang/actions/runs/43463100952)
- **分支**: `kv-cache-dtype-registry`
- **总耗时**: 36.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43463100952

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 6.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141415) |
| base-b-test-16-npu-a3 / run (0) | 10.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141546) |
| base-b-test-8-npu-a3 / run (0) | 2.4min | 环境问题 | 容器内未安装 sglang 模块，导致测试脚本导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141834) |



- **base-b-test-8-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/环境中未正确安装 sglang 包（或 PYTHONPATH 未包含源码目录），进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141834

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132033479361) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132033480398) |
| multimodal-gen-test-4-npu-a3 (0) | 32.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141137) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141174) |
| multimodal-gen-test-4-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141217) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141274) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141346) |
| base-b-test-4-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141431) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43463100952/job/132035141531) |


## [Run #43460782953](https://github.com/sgl-project/sglang/actions/runs/43460782953)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 85.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43460782953

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 79.6min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716166) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 3.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132007872731) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132007872892) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009715649) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009715670) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009715687) |
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009715692) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716019) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716116) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716173) |
| base-b-test-1-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716344) |
| base-b-test-16-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43460782953/job/132009716520) |


## [Run #43458547776](https://github.com/sgl-project/sglang/actions/runs/43458547776)
- **分支**: `fix/swa-window-lock-walk-split`
- **总耗时**: 25.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43458547776

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 4.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360120) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360331) |


- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_glm52.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360331

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/131999291430) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/131999291460) |
| multimodal-gen-test-4-npu-a3 (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000359749) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000359851) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000359905) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360183) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360307) |
| base-b-test-4-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43458547776/job/132000360409) |


## [Run #43457886200](https://github.com/sgl-project/sglang/actions/runs/43457886200)
- **分支**: `ci/npu-fed-labels-b2`
- **总耗时**: 54.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43457886200

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 20.6min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/132013443371) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，发生在 decode 正常运行时，属 runner/容器基础设施故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43457886200/job/132013443371

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131997468378) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131997468406) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998926987) |
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927238) |
| base-b-test-1-npu-a3 / run (0) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927266) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927299) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927414) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927466) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927468) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927475) |
| base-b-test-16-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927476) |
| multimodal-gen-test-1-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/131998927615) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/132013443217) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43457886200/job/132013443304) |


## [Run #43454286088](https://github.com/sgl-project/sglang/actions/runs/43454286088)
- **分支**: `ci/npu-fed-labels`
- **总耗时**: 40.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43454286088

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 35.5min | 环境问题 | multimodal-gen 测试作业失败，未生成 diffusion-failures 产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762095) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/132000739093) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 10.9min | 环境问题 | 依赖安装失败：pip 找不到 decorator==5.1.1 的可用版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/132000739201) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中 upload-artifact 提示未找到 diffusion-failures/ 文件，说明测试未产出失败样本；结合退出码 5 的常见原因，推测 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762095

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载到57%时出现“Executing the custom container implementation failed”，属于自托管 runner 的容器运行时故障，并非用例断言失败或代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43454286088/job/132000739093

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 安装 triton-ascend 依赖时，pip 报错 Could not find a version that satisfies the requirement decorator==5.1.1（from versions: none），无匹配发行版，进程退出码 1，属依赖源/镜像环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43454286088/job/132000739201

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131984373795) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131984373805) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762038) |
| multimodal-gen-test-1-npu-a3 (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762069) |
| multimodal-gen-test-4-npu-a3 (1) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762092) |
| base-b-test-2-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762209) |
| base-b-test-16-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762372) |
| base-b-test-4-npu-a3 / run (1) | 9.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762383) |
| base-b-test-4-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762398) |
| base-b-test-1-npu-a3 / run (0) | 25.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762500) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/131985762868) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43454286088/job/132000739252) |


## [Run #43395080995](https://github.com/sgl-project/sglang/actions/runs/43395080995)
- **分支**: `feat/dsv41-packed-main-kv-sm90-attention`
- **总耗时**: 27.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43395080995

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 14.8min | 环境问题 | pip 安装 triton-ascend 依赖时找不到 scipy==1.13.1 的可用版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053224804) |
| base-b-test-2-npu-a3 / run (0) | 10.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053225022) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | 环境问题 | pip 安装依赖失败，无法找到 pytest==8.3.2 版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053225683) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 pip 报错：Could not find a version that satisfies the requirement scipy==1.13.1 (from triton-ascend)，No matching distribution found，进程退出码 1。属于依赖包在 aarch64/Python3.12 环境下不可用或镜像源缺失，非代码逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053224804


- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 解析 triton-ascend 依赖时，报错 Could not find a version that satisfies the requirement pytest==8.3.2，且无匹配发行版，导致安装失败、进程退出码 1。属于依赖源/环境问题，非用例本身错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053225683

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132051969452) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132051971385) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053224577) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053224653) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053224798) |
| base-b-test-4-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053225137) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43395080995/job/132053225320) |


---
*Auto-generated by ci_monitor.py*