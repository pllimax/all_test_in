# NPU CI 执行监控（2026-11-16）
**生成时间**: 2026-11-17 07:17
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-16 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 163

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1522 个 | 失败 200 个 | 成功 Job 平均耗时 14.0min
- **Run 执行情况**: 成功 87 个 | 失败 76 个 | 成功 Run 平均耗时 54.2min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-4-npu-a3 / run (0) | 98.8min | #43792255174 | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074907) |
| base-b-test-16-npu-a3 / run (0) | 94.1min | #43799734401 | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675517) |
| base-b-test-4-npu-a3 / run (1) | 92.9min | #43792255174 | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054075059) |
| base-b-test-4-npu-a3 / run (0) | 92.0min | #43722075816 | [job link](https://github.com/sgl-project/sglang/actions/runs/43722075816/job/132836836880) |
| base-b-test-8-npu-a3 / run (0) | 86.5min | #43792255174 | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074916) |
| base-b-test-1-npu-a3 / run (0) | 84.0min | #43722075816 | [job link](https://github.com/sgl-project/sglang/actions/runs/43722075816/job/132836836946) |
| base-b-test-4-npu-a3 / run (1) | 71.9min | #43794593360 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169234) |
| base-b-test-8-npu-a3 / run (0) | 67.1min | #43794593360 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169195) |
| base-b-test-4-npu-a3 / run (0) | 62.3min | #43866183009 | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391901) |
| base-b-test-4-npu-a3 / run (0) | 52.7min | #43738458482 | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245297) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-1-npu-a3 / run (0) | 245.0min | #43783279191 | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046921) |
| base-b-test-16-npu-a3 / run (0) | 185.2min | #43778857464 | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180378) |
| base-b-test-2-npu-a3 / run (0) | 177.6min | #43783279191 | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046809) |
| base-b-test-4-npu-a3 / run (0) | 175.5min | #43783279191 | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046859) |
| base-b-test-2-npu-a3 / run (0) | 146.2min | #43779232427 | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014856931) |
| base-b-test-16-npu-a3 / run (0) | 142.5min | #43779232427 | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014857007) |
| base-b-test-16-npu-a3 / run (0) | 109.5min | #43788623536 | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539775) |
| base-b-test-1-npu-a3 / run (0) | 107.3min | #43788623536 | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539967) |
| base-b-test-16-npu-a3 / run (0) | 89.8min | #43791613655 | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963974) |
| base-b-test-1-npu-a3 / run (0) | 56.4min | #43794210036 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099534) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-4-npu-a3 / run (0) | 121 | 85 | 15 | 12 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202314)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624515)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812728)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000961)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133074601746) |
| base-b-test-16-npu-a3 / run (0) | 105 | 74 | 13 | 5 | 13 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135146)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017045)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402799)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276141)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609693) |
| base-b-test-1-npu-a3 / run (0) | 116 | 89 | 13 | 5 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133309984124)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296392515)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249235)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522482)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892788) |
| base-b-test-2-npu-a3 / run (0) | 124 | 98 | 11 | 3 | 12 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829471)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255577)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249271)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212580320)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892810) |
| base-b-test-4-npu-a3 / run (1) | 121 | 103 | 5 | 7 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255718)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705261)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519210)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636312)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245267) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 61 | 49 | 10 | 0 | 2 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43831160607/job/133180255594)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133119106381)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133083497106)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133078044044)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133084481408) |
| base-b-test-8-npu-a3 / run (0) | 104 | 89 | 4 | 5 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281037)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858477)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864195)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099492) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 108 | 100 | 6 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133286911447)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133285014195)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133215338076)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133214741183)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133215269583) |
| base-a-test-npu | 138 | 137 | 1 | 0 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43775819612/job/133001851396) |
| multimodal-gen-test-1-npu-a3 (1) | 93 | 86 | 1 | 0 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914557768) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_speculative_moe_a2a_backend.py` | 39 | 35 | 4 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135146)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270892)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173899) |
| `npu_pd_disaggregation.py` | 51 | 47 | 4 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255718)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519210)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636312) |
| `npu_dp_attention.py` | 36 | 33 | 3 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202314)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012809623)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629318) |
| `npu_eplb_min_rebalancing_utilization_threshold.py` | 51 | 49 | 2 | [base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281037)<br>[base-b-test-8-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864195) |
| `npu_memory_occupation.py` | 2 | 0 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133309984124)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892788) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 7 | 5 | 2 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133119106381)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133098142211) |
| `wan2_1_t2v_1.3b_1_npu` | 40 | 39 | 1 | [multimodal-gen-test-1-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334793) |
| `npu_hicache_mha.py` | 43 | 42 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673922) |
| `npu_sampling_backend.py` | 39 | 38 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296392515) |
| `npu_eagle3.py` | 39 | 38 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864224) |
| `npu_return_indexer_topk_deepseek_v4.py` | 40 | 39 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829471) |
| `qsa_npu.py` | 2 | 1 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407544) |
| `npu_update_weights_from_tensor.py` | 2 | 1 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892810) |
| `npu_moonlight_16b_a3b_bf16_1p_gsm8k.py` | 12 | 11 | 1 | [base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133215338076) |
| `qwen3.8-flash-next-decode-b2-attn-tp4-cap65536` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407544) |
| `qwen3.8-flash-next-verify-t4-attn-tp8-cap65536` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407544) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43783279191<br>[#33111 [Feat] elastic-ep: Runtime scale-down that retires EP ranks via Mooncake deactivate_ranks](https://github.com/sgl-project/sglang/pull/33111) | `qkang/elastic-ep-mooncake-scale-down` | 249.9min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43783279191) |
| #43778857464<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 191.7min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43778857464) |
| #43779232427<br>[#36088 [Fix] [AMD] distributed: Fix custom AR capture for DSA DP dual graphs](https://github.com/sgl-project/sglang/pull/36088) | `codex/fix-amd-dsa-dense-dp-graph` | 156.0min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43779232427) |
| #43799734401<br>[#43305 [Feat] [NPU] glm5: Support GLM-5.3-Flash on Ascend A3/A5](https://github.com/sgl-project/sglang/pull/43305) | `feat/npu-glm5-flash` | 149.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43799734401) |
| #43792255174 | `feat/qsa-cache-sharding` | 132.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43792255174) |
| #43788623536<br>[#49999 [Feat] [NPU] graph: Compile decode graphs with npugraph_ex and optional static kernels](https://github.com/sgl-project/sglang/pull/49999) | `npu-npugraph-ex-static-kernel` | 127.1min | 3 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43788623536) |
| #43794593360<br>[#45087 [Fix] constrained: bound the compiled-grammar cache by host memory (LRU) to stop RSS growth with per-request schemas](https://github.com/sgl-project/sglang/pull/45087) | `fix/grammar-cache-lru` | 102.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43794593360) |
| #43791613655<br>[#47856 [Fix] [NPU] profiler: :bug: Fix patches and daemon trace parsing](https://github.com/sgl-project/sglang/pull/47856) | `junlin/diffusion-npu-profiler` | 101.3min | 1 | base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43791613655) |
| #43838818540<br>[#50620 [Perf] spec: Fused draft softmax + sample kernel for EAGLE rejection sampling](https://github.com/sgl-project/sglang/pull/50620) | `dark/eagle-fused-draft-sample` | 73.1min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43838818540) |
| #43838644871<br>[#47856 [Fix] [NPU] profiler: :bug: Fix patches and daemon trace parsing](https://github.com/sgl-project/sglang/pull/47856) | `junlin/diffusion-npu-profiler` | 72.1min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43838644871) |
| #43866183009<br>[#46858 [Feat] lfm3: Add text, vision, audio and Omni support](https://github.com/sgl-project/sglang/pull/46858) | `main` | 65.9min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43866183009) |
| #43858783937<br>[#47660 [Feat] [NPU] DSV4.1: Support DeepSeek-V4.1 on Ascend A5](https://github.com/sgl-project/sglang/pull/47660) | `dsv41-a5` | 63.7min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43858783937) |
| #43794210036<br>[#44899 [Fix] disaggregation: Preserve EAGLE/MTP draft KV during CPU retraction](https://github.com/sgl-project/sglang/pull/44899) | `fix/pd-eagle-mtp-cpu-retraction` | 62.2min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43794210036) |
| #43837908042<br>[#43527 [Feat] QSA: Add cache sharding for Qwen3.8 hybrid models](https://github.com/sgl-project/sglang/pull/43527) | `feat/qsa-cache-sharding` | 61.0min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43837908042) |
| #43738458482 | `nvidia-megakernel-binding-offers` | 57.3min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43738458482) |
| #43798212629<br>[#50469 [Perf] hicache: Fence write_back eviction copies on the forward stream instead of blocking the scheduler](https://github.com/sgl-project/sglang/pull/50469) | `hicache-async-write-back-demote` | 54.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43798212629) |
| #43860540579<br>[#44702 [Feat] model-loader: Add model-aware checkpoint shard selection for Qwen MTP](https://github.com/sgl-project/sglang/pull/44702) | `zhy76/mtp-default-shard-selection` | 52.4min | 1 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43860540579) |
| #43810205772<br>[#46210 [Feat] [NVIDIA] megakernels: DSA / MLA binding view, EAGLE draft capture checks, early draft embedding sharing](https://github.com/sgl-project/sglang/pull/46210) | `megakernel-dsa-view-draft-capture` | 50.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43810205772) |
| #43810096726<br>[#43994 [Feat] [XPU] moe: Add FP8 MoE support](https://github.com/sgl-project/sglang/pull/43994) | `ecao/fp8_moe_v2` | 49.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43810096726) |
| #43796932779<br>[#46486 [Perf] [AMD] dsa: Run the GLM-5 decode MLA chain as Gluon kernels on gfx950](https://github.com/sgl-project/sglang/pull/46486) | `feature/amd-glm5-dsa-mla-decode-gfx950` | 48.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43796932779) |
| #43731068586<br>[#47869 [Perf] diffusion: Fuse LTX video VAE normalization and padding](https://github.com/sgl-project/sglang/pull/47869) | `perf/ltx2-vae-gap` | 46.4min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43731068586) |
| #43729962952<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 46.3min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43729962952) |
| #43691440937<br>[#50587 [Feat] dflash: Confidence-scheduled compact verify for DFlash2 on Kimi K3.1](https://github.com/sgl-project/sglang/pull/50587) | `kimi31-dflash2-ragged-verify` | 44.5min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43691440937) |
| #43753468054<br>[#50213 [Feat] scheduler: Keep a reserve of KV and state slots for cached prefixes (--prefill-cache-reserve)](https://github.com/sgl-project/sglang/pull/50213) | `feat/hold-cold-prefill-admission` | 43.3min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43753468054) |
| #43737037780<br>[#42745 [Fix] radix_cache: Cap SWA lock-walk pinning at one window in the Rust TreeCore](https://github.com/sgl-project/sglang/pull/42745) | `fix/swa-window-lock-walk-split` | 42.6min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43737037780) |
| #43775083176<br>[#50146 [Fix] scheduler: Join the prefill delayer all-gather on DP ranks that defer prefill](https://github.com/sgl-project/sglang/pull/50146) | `fix/prefill-delayer-deferring-dp-rank` | 42.0min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43775083176) |
| #43735291168<br>[#50620 [Perf] spec: Fused draft softmax + sample kernel for EAGLE rejection sampling](https://github.com/sgl-project/sglang/pull/50620) | `dark/eagle-fused-draft-sample` | 42.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43735291168) |
| #43804853680<br>[#46210 [Feat] [NVIDIA] megakernels: DSA / MLA binding view, EAGLE draft capture checks, early draft embedding sharing](https://github.com/sgl-project/sglang/pull/46210) | `megakernel-dsa-view-draft-capture` | 41.3min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43804853680) |
| #43793181393<br>[#48118 [Perf] [AMD] gdn: Add an aiter backend for linear-chain target verify](https://github.com/sgl-project/sglang/pull/48118) | `feature/yunkai/gdn-verify-aiter` | 41.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43793181393) |
| #43764100939<br>[#50156 [Perf] [NVIDIA] runtime: Blackwell/Rubin serving optimizations for hybrid GDN + QSA + MoE models](https://github.com/sgl-project/sglang/pull/50156) | `nvidia-runtime-opts-hybrid-gdn-qsa` | 40.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43764100939) |
| #43735781479<br>[#49356 [Feat] xpu: Consolidate simple XPU enablements](https://github.com/sgl-project/sglang/pull/49356) | `xpu/weekly-simple-model-enablement-2026-11-09` | 39.9min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43735781479) |
| #43799666292<br>[#40333 [Feat] [NVIDIA] deepseek-v4.1: Support prefill CP with BCG in PD serving (2/N)](https://github.com/sgl-project/sglang/pull/40333) | `main-v4.1-cp-bcg` | 39.6min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43799666292) |
| #43856047092<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 38.9min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43856047092) |
| #43824992515<br>[#50844 [Perf] [AMD] muse-spark: Faster gfx1250 verify, extend and MoE dispatch](https://github.com/sgl-project/sglang/pull/50844) | `pr/muse-gfx1250` | 37.5min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43824992515) |
| #43872117181<br>[#37570 [Feat] [NPU] Qwen3.8-Flash-Next: Support graph replay, MTP, and Triton kernels](https://github.com/sgl-project/sglang/pull/37570) | `pr-36601` | 35.0min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43872117181) |
| #43841581556<br>[#43360 [Feat] [AMD] fp4: Select the Quark MXFP4 dense GEMM with --fp4-gemm-backend aiter|triton](https://github.com/sgl-project/sglang/pull/43360) | `feat/cli-fp4-gemm-backend-aiter-triton` | 34.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43841581556) |
| #43865775427<br>[#41879 [Perf] [AMD] Qwen3.5/Qwen3.8: Opt-in AITER FlyDSL causal conv1d prefill](https://github.com/sgl-project/sglang/pull/41879) | `pr/gdn-conv-flydsl` | 34.7min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43865775427) |
| #43843591579<br>[#47867 [Feat] [AMD] hicache: Add --hicache-mamba-size-gb to pin the HiCache Mamba host pool size](https://github.com/sgl-project/sglang/pull/47867) | `k3/hicache-mamba-size-gb` | 34.6min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43843591579) |
| #43764842686<br>[#50157 [Feat] [NVIDIA] megakernel-binding: state, pool, prefill-graph and draft-step views for hybrid models](https://github.com/sgl-project/sglang/pull/50157) | `nvidia-megakernel-binding-offers` | 34.2min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43764842686) |
| #43835441113<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 33.9min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43835441113) |
| #43411886427<br>[#50305 ci(npu): run the NPU PR stages on the sglang fed runner labels](https://github.com/sgl-project/sglang/pull/50305) | `ci/npu-fed-labels-only` | 33.9min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43411886427) |
| #43773979054<br>[#44050 [Feat] speculative: Add native UBTree decoding for Ling3](https://github.com/sgl-project/sglang/pull/44050) | `asahi/ubtree` | 33.7min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43773979054) |
| #43840519689<br>[#46858 [Feat] lfm3: Add text, vision, audio and Omni support](https://github.com/sgl-project/sglang/pull/46858) | `lfm3` | 33.3min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43840519689) |
| #43733176480<br>[#44576 [Fix] disaggregation: Release multimodal features when PD prefill finishes a request](https://github.com/sgl-project/sglang/pull/44576) | `pd-prefill-release-mm-features` | 33.3min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43733176480) |
| #43863079771<br>[#49999 [Feat] [NPU] graph: Compile decode graphs with npugraph_ex and optional static kernels](https://github.com/sgl-project/sglang/pull/49999) | `npu-npugraph-ex-static-kernel` | 32.6min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43863079771) |
| #43747523604<br>[#36727 [Diffusion] Preserve mapped component weights during low-memory offload](https://github.com/sgl-project/sglang/pull/36727) | `diffusion-offload-phase01` | 32.1min | 1 | multimodal-gen-test-1-npu-a3 (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43747523604) |
| #43801519578<br>[#43852 [Feat] [NVIDIA] dsv4.1: [2/N] Add SM90 attention for packed FP4 Main KV.](https://github.com/sgl-project/sglang/pull/43852) | `feat/dsv41-packed-main-kv-sm90-attention` | 31.9min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43801519578) |
| #43886228110<br>[#47271 [Feat] Mistral-Large-4: add model support](https://github.com/sgl-project/sglang/pull/47271) | `new-model-support` | 31.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43886228110) |
| #43796865497<br>[#50238 [Feat] [AMD] FLy: Support entropy-gated deferred verification for draft-model speculative decoding](https://github.com/sgl-project/sglang/pull/50238) | `fangyuan/dspark_fly` | 31.1min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43796865497) |
| #43804776385<br>[#50469 [Perf] hicache: Fence write_back eviction copies on the forward stream instead of blocking the scheduler](https://github.com/sgl-project/sglang/pull/50469) | `hicache-async-write-back-demote` | 26.8min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43804776385) |
| #43815338052<br>[#50116 [Fix] mem_cache: Fix explicit HND initialization](https://github.com/sgl-project/sglang/pull/50116) | `fix/mha-kv-pool-hnd-init` | 25.9min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43815338052) |
| #43814553696<br>[#37570 [Feat] [NPU] Qwen3.8-Flash-Next: Support graph replay, MTP, and Triton kernels](https://github.com/sgl-project/sglang/pull/37570) | `pr-36601` | 25.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43814553696) |
| #43815036461 | `feat/npu-glm5-flash` | 25.3min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43815036461) |
| #43854441119<br>[#29949 [Apple Silicon][MPS] Cap memory reporting to Metal's recommended working set](https://github.com/sgl-project/sglang/pull/29949) | `mps-working-set-cap` | 24.9min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43854441119) |
| #43800797825<br>[#42388 [Feat] gdn: Bit-exact tuple replay for linear-chain spec verify](https://github.com/sgl-project/sglang/pull/42388) | `lossless-gdn-tuple-verify` | 24.9min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43800797825) |
| #43870046242<br>[#49289 [Test] [NPU] rl: Add P0 RLHF lifecycle coverage](https://github.com/sgl-project/sglang/pull/49289) | `test/rlhf-test-coverage` | 22.8min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43870046242) |
| #43844853666<br>[#41879 [Perf] [AMD] Qwen3.5/Qwen3.8: Opt-in AITER FlyDSL causal conv1d prefill](https://github.com/sgl-project/sglang/pull/41879) | `pr/gdn-conv-flydsl` | 22.4min | 2 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43844853666) |
| #43777828139<br>[#36088 [Fix] [AMD] distributed: Fix custom AR capture for DSA DP dual graphs](https://github.com/sgl-project/sglang/pull/36088) | `codex/fix-amd-dsa-dense-dp-graph` | 19.6min | 3 | base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43777828139) |
| #43856623124<br>[#43305 [Feat] [NPU] glm5: Support GLM-5.3-Flash on Ascend A3/A5](https://github.com/sgl-project/sglang/pull/43305) | `feat/npu-glm5-flash` | 18.6min | 6 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43856623124) |
| #43741622410 | `wuyaole/fix-prefill-reservation-budget` | 17.9min | 6 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43741622410) |
| #43861787791<br>[#45792 [Feat] [NPU] multimodal: Add JPEG decoding to the shared image loader](https://github.com/sgl-project/sglang/pull/45792) | `feat/npu-jpeg-decode-20261022` | 17.6min | 7 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43861787791) |
| #43837753413<br>[#49289 [Test] [NPU] rl: Add P0 RLHF lifecycle coverage](https://github.com/sgl-project/sglang/pull/49289) | `test/rlhf-test-coverage` | 17.6min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43837753413) |
| #43831160607<br>[#44265 [Feat] [AMD] dsv4: Dispatch Mega-mHC prefill to aiter on gfx950](https://github.com/sgl-project/sglang/pull/44265) | `amd/dsv41-gfx950-mega-mhc-prefill` | 16.8min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43831160607) |
| #43855878452<br>[#49999 [Feat] [NPU] graph: Compile decode graphs with npugraph_ex and optional static kernels](https://github.com/sgl-project/sglang/pull/49999) | `npu-npugraph-ex-static-kernel` | 15.6min | 8 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43855878452) |
| #43824404171<br>[#50671 [Refactor] gateway: Keep sgl-model-gateway as source only and move every user to sgl-router](https://github.com/sgl-project/sglang/pull/50671) | `lsyin/gateway-source-only` | 13.9min | 9 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43824404171) |
| #43813430545<br>[#50844 [Perf] [AMD] muse-spark: Faster gfx1250 verify, extend and MoE dispatch](https://github.com/sgl-project/sglang/pull/50844) | `pr/muse-gfx1250` | 13.4min | 8 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43813430545) |
| #43412247935<br>[#38860 [Feat] [NPU] dspark: Support static mode on GLM 5.2](https://github.com/sgl-project/sglang/pull/38860) | `feat/glm52-dspark-npu-upstream` | 13.1min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43412247935) |
| #43837079639 | `dark/dflash2-fused-select` | 12.6min | 7 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43837079639) |
| #43843890061<br>[#36591 [Fix] hisparse: state-preserving retraction and recovery for DSV4](https://github.com/sgl-project/sglang/pull/36591) | `fix/hisparse-cpu-copy-retraction` | 12.0min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-8-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43843890061) |
| #43837698399<br>[#47876 [Feat] mamba: Support strided destination conv-state pools in the conv-window scatter](https://github.com/sgl-project/sglang/pull/47876) | `xpu-conv-scatter-strided-dst` | 11.2min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43837698399) |
| #43794522920<br>[#43480 [Perf] [AMD] DSV4.1: Fuse wo_b's GEMM with its all-reduce via mori cco on gfx950](https://github.com/sgl-project/sglang/pull/43480) | `xiangch/fused-wo-b-gemm-ar-main` | 10.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43794522920) |
| #43793564223<br>[#48932 [Feat] [Apple] mps: Size the Unlimited-OCR v2 KV pool in document windows and add an opt-in warmup](https://github.com/sgl-project/sglang/pull/48932) | `uocr2-mps-defaults` | 9.8min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43793564223) |
| #43793232884 | `prefill_graph_ascend_ops_on_main` | 9.4min | 9 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43793232884) |
| #43831382634<br>[#50732 [Refactor] gateway: Delete sgl-model-gateway and its leftovers](https://github.com/sgl-project/sglang/pull/50732) | `lsyin/delete-sgl-model-gateway` | 8.8min | 6 | base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43831382634) |
| #43777009435<br>[#36088 [Fix] [AMD] distributed: Fix custom AR capture for DSA DP dual graphs](https://github.com/sgl-project/sglang/pull/36088) | `codex/fix-amd-dsa-dense-dp-graph` | 8.4min | 5 | base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43777009435) |
| #43775819612<br>[#50653 [Fix] inkling2: Ignore the Hub ModelOpt quantization_config stub](https://github.com/sgl-project/sglang/pull/50653) | `inkling-2-small-support` | 5.4min | 1 | base-a-test-npu | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43775819612) |

---


## [Run #43886228110](https://github.com/sgl-project/sglang/actions/runs/43886228110)
- **分支**: `new-model-support`
- **总耗时**: 31.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43886228110

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829471) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829471

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133365260579) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133365260588) |
| multimodal-gen-test-4-npu-a3 (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829074) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829110) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829181) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829233) |
| base-b-test-16-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829290) |
| base-b-test-1-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829376) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829457) |
| base-b-test-4-npu-a3 / run (0) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829492) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133366829676) |
| Analyze failure report / cross-reference failures with recommendations | 0.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43886228110/job/133384611926) |


## [Run #43872117181](https://github.com/sgl-project/sglang/actions/runs/43872117181)
- **分支**: `pr-36601`
- **总耗时**: 35.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43872117181

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 5.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281037) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281037

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133315960081) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133315960197) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317280839) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317280873) |
| multimodal-gen-test-4-npu-a3 (0) | 30.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317280970) |
| base-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281100) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281159) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281166) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281189) |
| base-b-test-16-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281238) |
| multimodal-gen-test-1-npu-a3 (1) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43872117181/job/133317281584) |


## [Run #43870046242](https://github.com/sgl-project/sglang/actions/runs/43870046242)
- **分支**: `test/rlhf-test-coverage`
- **总耗时**: 22.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43870046242

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.5min | 环境问题 | 日志中未见明确错误，但作业以退出码5失败，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133309984124) |

- **base-b-test-1-npu-a3 / run (0)**: 日志末尾仅显示artifact上传成功和清理过程，未包含实际测试错误信息。退出码5表示unittest存在errors，最常见为setUpClass阶段server启动失败（如host OOM、进程被SIGKILL），需查看完整日志中的Traceback确认。
  - 失败用例: npu_memory_occupation.py, npu_memory_occupation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133309984124

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133308749751) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133308749782) |
| base-b-test-2-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43870046242/job/133309984006) |


## [Run #43866183009](https://github.com/sgl-project/sglang/actions/runs/43866183009)
- **分支**: `main`
- **总耗时**: 65.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43866183009

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 8.2min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296392515) |

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，常见于setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  - 失败用例: npu_sampling_backend.py, npu_sampling_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296392515

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133295397670) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391425) |
| multimodal-gen-test-1-npu-a3 (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391503) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391626) |
| multimodal-gen-test-4-npu-a3 (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391716) |
| base-b-test-16-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391743) |
| base-b-test-8-npu-a3 / run (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391861) |
| base-b-test-2-npu-a3 / run (0) | 6.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391868) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391880) |
| base-b-test-4-npu-a3 / run (0) | 62.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43866183009/job/133296391901) |


## [Run #43865775427](https://github.com/sgl-project/sglang/actions/runs/43865775427)
- **分支**: `pr/gdn-conv-flydsl`
- **总耗时**: 34.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43865775427

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202314) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202314

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133294079171) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133294079303) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295201810) |
| multimodal-gen-test-1-npu-a3 (1) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295201856) |
| multimodal-gen-test-4-npu-a3 (0) | 28.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295201873) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295201883) |
| base-b-test-4-npu-a3 / run (1) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202064) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202094) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202133) |
| base-b-test-16-npu-a3 / run (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202144) |
| base-b-test-1-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43865775427/job/133295202168) |


## [Run #43863079771](https://github.com/sgl-project/sglang/actions/runs/43863079771)
- **分支**: `npu-npugraph-ex-static-kernel`
- **总耗时**: 32.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43863079771

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 4.8min | 环境问题 | 作业在 k8s 步骤后异常退出，未进入测试执行阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255577) |
| base-b-test-4-npu-a3 / run (1) | 15.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255718) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 checkout 完成后运行 k8s/index.js 即结束，仅有 Node.js 弃用警告，无测试输出或 Traceback，疑似 runner/容器环境或 k8s 启动环节异常导致作业中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255577

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255718

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133284793384) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133284793786) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255357) |
| multimodal-gen-test-4-npu-a3 (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255427) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255440) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255586) |
| base-b-test-16-npu-a3 / run (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255603) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255624) |
| base-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255643) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43863079771/job/133286255789) |


## [Run #43861787791](https://github.com/sgl-project/sglang/actions/runs/43861787791)
- **分支**: `feat/npu-jpeg-decode-20261022`
- **总耗时**: 17.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43861787791

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 14.5min | 环境问题 | 多模态生成测试作业失败，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249019) |
| multimodal-gen-test-4-npu-a3 (1) | 14.5min | 环境问题 | 多模态生成测试中 diffusion 用例失败，失败产物已上传，但日志省略部分未显示具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249044) |
| multimodal-gen-test-1-npu-a3 (1) | 14.8min | 环境问题 | 日志中未见测试执行细节，仅显示产物上传和清理，无法定位具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249104) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249131) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | 环境问题 | 日志中未见明确错误，作业在 artifact 上传后正常清理，失败原因需查看省略的测试执行段 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249148) |
| base-b-test-1-npu-a3 / run (0) | 3.7min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249235) |
| base-b-test-2-npu-a3 / run (0) | 3.8min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示 artifact 上传和清理成功，无法定位具体错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249271) |
| base-b-test-4-npu-a3 / run (0) | 11.7min | 环境问题 | 日志中未见明确错误，作业实际成功上传了测试日志工件，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249272) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中段被省略，仅见失败产物 diffusion-failures-npu-2-part0-1.zip 上传；退出码 5 提示 unittest 存在 errors，最常见为 setUpClass 时 server 启动失败（host OOM 或进程被 SIGKILL），需查看省略部分 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249019

- **multimodal-gen-test-4-npu-a3 (1)**: 作业在 multimodal-gen-test-4-npu-a3 上运行，上传了 diffusion-failures-npu-2-part1-1.zip 失败产物，说明测试用例执行失败；但省略的日志未包含 Traceback，无法确认是 setUpClass 中 server 启动失败还是其他错误，需查看完整日志与失败产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249044

- **multimodal-gen-test-1-npu-a3 (1)**: 日志被省略，仅含 runner 初始化、artifact 上传（diffusion-failures-npu-1-part1-1.zip）和清理步骤，缺少 unittest 报错 Traceback，无法确认退出码 5 的具体原因，需查看完整日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249104


- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 selected-test-logs artifact 及 post job cleanup，均成功；中间省略部分应含真实失败信息（如 setUpClass 中 server 启动失败、OOM 或 SIGKILL 导致退出码 5）。当前片段无法定位具体错误，建议查看完整日志中的 Traceback/RuntimeError。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249148

- **base-b-test-1-npu-a3 / run (0)**: 日志仅显示artifact上传与清理，缺少Traceback。退出码5表示unittest有errors，最可能是setUpClass中sglang server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249235

- **base-b-test-2-npu-a3 / run (0)**: 提供的日志被省略，只看到 checkout、artifact 上传（321字节）和 post job cleanup，没有 Traceback/RuntimeError 或退出码 5 的上下文。需查看省略部分中 setUpClass 阶段 sglang server 启动日志（如 OOM、SIGKILL）才能确定原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249271

- **base-b-test-4-npu-a3 / run (0)**: 可见日志显示 checkout、下载/上传 artifact 均正常完成，退出码 5 对应的 unittest errors 具体 Traceback 位于省略部分，无法据此判定为用例未收集或性能/精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249272

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133280391708) |
| base-a-test-npu | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133280391771) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281248940) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43861787791/job/133281249186) |


## [Run #43860540579](https://github.com/sgl-project/sglang/actions/runs/43860540579)
- **分支**: `zhy76/mtp-default-shard-selection`
- **总耗时**: 52.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43860540579

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.4min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，疑为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133286911447) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志中间省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看省略部分确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133286911447

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133276131409) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133276131429) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119225) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119226) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119448) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119473) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119510) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119565) |
| base-b-test-4-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119572) |
| base-b-test-1-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133277119720) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133286911221) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43860540579/job/133286911667) |


## [Run #43858783937](https://github.com/sgl-project/sglang/actions/runs/43858783937)
- **分支**: `dsv41-a5`
- **总耗时**: 63.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43858783937

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 1.5min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133285014195) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试日志文件 /tmp/test-logs/*.log 未生成，无 artifact 上传，说明用例在 setUpClass 阶段即失败（server 启动失败，可能 host OOM 或进程被 SIGKILL），导致 unittest errors 退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133285014195

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133271724499) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133271724553) |
| multimodal-gen-test-1-npu-a3 (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869383) |
| multimodal-gen-test-4-npu-a3 (1) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869409) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869434) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869507) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869612) |
| base-b-test-4-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869775) |
| base-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869791) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869843) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869849) |
| base-b-test-16-npu-a3 / run (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133272869963) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 34.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133285014146) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43858783937/job/133285014841) |


## [Run #43856623124](https://github.com/sgl-project/sglang/actions/runs/43856623124)
- **分支**: `feat/npu-glm5-flash`
- **总耗时**: 18.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43856623124

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 4.6min | 环境问题 | multimodal 测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624223) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624281) |
| base-b-test-2-npu-a3 / run (0) | 13.7min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624330) |
| base-b-test-1-npu-a3 / run (0) | 13.7min | 其他 | 日志片段未包含实际测试失败信息，仅显示产物上传与清理成功 | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624351) |
| base-b-test-16-npu-a3 / run (0) | 15.5min | 其他 | 日志被截断，缺少真实错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624392) |
| base-b-test-4-npu-a3 / run (0) | 3.0min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624515) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示作业上传了 diffusion-failures-npu-2-part1-1.zip（423字节），说明测试用例失败并生成失败产物；结合退出码5对应 unittest errors，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略部分的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624223

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产出结果；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624281

- **base-b-test-2-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5对应unittest errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624330

- **base-b-test-1-npu-a3 / run (0)**: 可见日志均为 runner 初始化、下载 action、上传 artifact 和 post job 清理，未出现 Traceback/RuntimeError 或退出码 5 的报错内容，无法定位具体失败原因，需查看被省略的中间测试日志。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624351

- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、下载 action、上传 artifact 和 post job 清理，均正常；中间省略部分才含测试执行与错误，但未提供，无法判断退出码 5 的具体 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624392

- **base-b-test-4-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624515

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133262675563) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133262675574) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624384) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856623124/job/133263624417) |


## [Run #43856047092](https://github.com/sgl-project/sglang/actions/runs/43856047092)
- **分支**: `new-model-support`
- **总耗时**: 38.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43856047092

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 3.4min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858477) |
| base-b-test-2-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858530) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133263171730) |

- **base-b-test-8-npu-a3 / run (0)**: 日志中仅见artifact上传与清理，无Traceback/RuntimeError。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858477



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133260692171) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133260692173) |
| sgl-router-build-aarch64 / Build sgl-router | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133260789000) |
| multimodal-gen-test-4-npu-a3 (0) | 33.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858308) |
| multimodal-gen-test-1-npu-a3 (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858356) |
| multimodal-gen-test-1-npu-a3 (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858382) |
| multimodal-gen-test-4-npu-a3 (1) | 35.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858391) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858469) |
| base-b-test-16-npu-a3 / run (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133261858672) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43856047092/job/133263171801) |


## [Run #43855878452](https://github.com/sgl-project/sglang/actions/runs/43855878452)
- **分支**: `npu-npugraph-ex-static-kernel`
- **总耗时**: 15.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43855878452

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | 环境问题 | multimodal 测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334763) |
| multimodal-gen-test-1-npu-a3 (0) | 12.2min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致用例 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334793) |
| multimodal-gen-test-1-npu-a3 (1) | 12.1min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334867) |
| multimodal-gen-test-4-npu-a3 (0) | 10.9min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334988) |
| base-b-test-2-npu-a3 / run (0) | 12.2min | 环境问题 | 日志中未见明确错误，但用例退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334993) |
| base-b-test-4-npu-a3 / run (0) | 12.3min | 环境问题 | 日志中未见明确错误，但作业以退出码5失败，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335049) |
| base-b-test-1-npu-a3 / run (0) | 11.5min | 环境问题 | 日志中未见明确错误，但作业失败，疑似 NPU 环境或 server 启动异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335077) |
| base-b-test-16-npu-a3 / run (0) | 12.1min | 环境问题 | 日志片段未包含实际测试失败信息，仅显示 artifact 上传与清理成功，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335086) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-2-part1-1.zip 失败工件，说明用例执行报错（退出码5，unittest errors），常见于 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334763

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part0-1.zip 失败产物，未见具体 Traceback。结合退出码 5 与产物命名，推测 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），需查看省略段真实错误确认。
  - 失败用例: wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334793

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part1-1.zip 失败产物，说明用例执行出错（退出码 5 对应 unittest errors），最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL）。需查看省略段 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334867

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行了约10分钟后上传 diffusion-failures-npu-2-part0-1.zip 工件，说明测试用例执行失败并收集了失败产物；结合退出码5的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），但省略的中间日志未直接给出 Traceback，需查看工件确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334988

- **base-b-test-2-npu-a3 / run (0)**: 日志被省略，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看省略段真实异常确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261334993

- **base-b-test-4-npu-a3 / run (0)**: 日志省略了中间部分，仅显示artifact上传和清理成功，未包含实际测试错误。根据退出码5，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志中的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335049

- **base-b-test-1-npu-a3 / run (0)**: 日志被截断，仅见 artifact 上传成功与清理阶段，无 Traceback。结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（host OOM 或进程被 SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335077

- **base-b-test-16-npu-a3 / run (0)**: 可见日志均为 runner 初始化、action 下载、artifact 上传和 post job cleanup，未出现 Traceback/RuntimeError 或退出码 5 的上下文；中间省略部分可能含真实错误，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335086

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133260126567) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133260126660) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335110) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43855878452/job/133261335257) |


## [Run #43854441119](https://github.com/sgl-project/sglang/actions/runs/43854441119)
- **分支**: `mps-working-set-cap`
- **总耗时**: 24.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43854441119

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 2.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522482) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522615) |

- **base-b-test-1-npu-a3 / run (0)**: 日志中段省略，仅见artifact上传与清理，无Traceback。退出码5对应unittest errors，常见于setUpClass时server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522482


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133255187594) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133255187666) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522459) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522524) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522709) |
| base-b-test-16-npu-a3 / run (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522800) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256522827) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43854441119/job/133256523037) |


## [Run #43844853666](https://github.com/sgl-project/sglang/actions/runs/43844853666)
- **分支**: `pr/gdn-conv-flydsl`
- **总耗时**: 22.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43844853666

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 19.2min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 失败产物 | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223514840) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223514970) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515011) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | 环境问题 | 多模态生成测试失败，上传了 diffusion-failures 工件，疑似 server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515045) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515097) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515175) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515193) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业运行了约19分钟后上传了 diffusion-failures-npu-2-part0-1.zip 失败产物，说明测试用例存在失败/错误（退出码5，unittest errors），但省略部分未显示具体 Traceback，无法确定根因，需查看失败产物或完整日志确认是否为 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223514840



- **multimodal-gen-test-4-npu-a3 (1)**: 日志中上传了 diffusion-failures-npu-2-part1-1.zip 工件，说明测试用例执行失败并收集了失败产物；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看工件中的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515045




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133222598165) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133222598280) |
| multimodal-gen-test-1-npu-a3 (1) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223514628) |
| multimodal-gen-test-1-npu-a3 (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223514733) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43844853666/job/133223515116) |


## [Run #43843890061](https://github.com/sgl-project/sglang/actions/runs/43843890061)
- **分支**: `fix/hisparse-cpu-copy-retraction`
- **总耗时**: 12.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43843890061

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 8.0min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647784) |
| base-b-test-4-npu-a3 / run (0) | 6.0min | 环境问题 | 自托管 runner 的 k8s 容器执行失败，临时脚本文件丢失导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647936) |
| base-b-test-1-npu-a3 / run (0) | 6.0min | 其他 | 日志被截断，缺少真实错误信息，无法定位失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647981) |
| base-b-test-2-npu-a3 / run (0) | 6.0min | 环境问题 | 日志被截断，未包含实际测试失败的错误信息，仅见 artifact 上传与清理，无法定位根因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647985) |
| base-b-test-16-npu-a3 / run (0) | 8.3min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220648077) |
| base-b-test-4-npu-a3 / run (1) | 5.2min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220648165) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220648442) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志中间省略，仅见artifact上传成功，未见Traceback。退出码5表示unittest有errors，常见于setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647784

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 execPodStepWithOutput failed，随后 sh 报错无法打开 /__w/_temp/*.sh（No such file），属于自托管 runner 容器执行环境异常，非用例代码或性能精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647936

- **base-b-test-1-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、下载 action、上传 artifact 和清理阶段，中间省略部分包含实际测试执行与错误，但未提供 Traceback/RuntimeError 等关键信息，无法判断是否为 setUpClass 启动失败或退出码 5 的具体来源。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647981

- **base-b-test-2-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、action 下载、artifact 上传和 post job 清理，缺少测试执行阶段的 Traceback/RuntimeError。若退出码为 5，通常为 setUpClass 中 sglang server 启动失败（如 host OOM、SIGKILL），需查看省略段日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647985

- **base-b-test-16-npu-a3 / run (0)**: 日志省略了中间部分，仅显示artifact上传和清理成功，无Traceback。退出码5表明unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看被省略的测试日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220648077

- **base-b-test-4-npu-a3 / run (1)**: 日志中段被省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5表示unittest有errors，常见于setUpClass时server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220648165

- **base-b-test-8-npu-a3 / run (0)**: 日志仅显示artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时sglang server启动失败（如host OOM、进程被SIGKILL），需查看被省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220648442

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133219297470) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133219297489) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843890061/job/133220647760) |


## [Run #43843591579](https://github.com/sgl-project/sglang/actions/runs/43843591579)
- **分支**: `k3/hicache-mamba-size-gb`
- **总耗时**: 34.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43843591579

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 3.2min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812728) |

- **base-b-test-4-npu-a3 / run (0)**: 日志中段被省略，仅见artifact上传与清理，未见Traceback。退出码5表示unittest有errors，通常为setUpClass时server启动失败（如host OOM、进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812728

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133218320658) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133218320909) |
| multimodal-gen-test-1-npu-a3 (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812431) |
| multimodal-gen-test-1-npu-a3 (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812445) |
| multimodal-gen-test-4-npu-a3 (1) | 9.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812507) |
| base-b-test-1-npu-a3 / run (0) | 5.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812572) |
| base-b-test-4-npu-a3 / run (1) | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219812785) |
| base-b-test-2-npu-a3 / run (0) | 7.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219813020) |
| multimodal-gen-test-4-npu-a3 (0) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43843591579/job/133219813259) |


## [Run #43841581556](https://github.com/sgl-project/sglang/actions/runs/43841581556)
- **分支**: `feat/cli-fp4-gemm-backend-aiter-triton`
- **总耗时**: 34.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43841581556

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 2.9min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，常见为setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212580320) |
| base-b-test-4-npu-a3 / run (1) | 1.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133214017376) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133214017564) |

- **base-b-test-2-npu-a3 / run (0)**: 日志仅显示artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass中sglang server启动失败（host OOM/被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212580320



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133211511851) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133211512043) |
| sgl-router-build-aarch64 / Build sgl-router | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133211631667) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579491) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579535) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579585) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579608) |
| base-b-test-16-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579727) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579834) |
| base-b-test-1-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43841581556/job/133212579948) |


## [Run #43840519689](https://github.com/sgl-project/sglang/actions/runs/43840519689)
- **分支**: `lfm3`
- **总耗时**: 33.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43840519689

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000888) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000943) |
| base-b-test-4-npu-a3 / run (0) | 3.1min | 环境问题 | 日志被截断，未见真实错误，但作业以退出码5结束，疑似setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000961) |



- **base-b-test-4-npu-a3 / run (0)**: 日志中间省略，仅见artifact上传成功与清理，无Traceback。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000961

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133207947620) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133207947680) |
| multimodal-gen-test-4-npu-a3 (0) | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000379) |
| multimodal-gen-test-1-npu-a3 (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000446) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000462) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000518) |
| base-b-test-4-npu-a3 / run (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000830) |
| base-b-test-16-npu-a3 / run (0) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000855) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43840519689/job/133209000867) |


## [Run #43838818540](https://github.com/sgl-project/sglang/actions/runs/43838818540)
- **分支**: `dark/eagle-fused-draft-sample`
- **总耗时**: 73.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43838818540

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.0min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示setUpClass阶段server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133215338076) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志中间省略，仅见artifact上传与清理，无Traceback。按背景知识，退出码5多为setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认具体异常。
  - 失败用例: npu_moonlight_16b_a3b_bf16_1p_gsm8k.py, npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133215338076

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133202305236) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133202305327) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133203534774) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133203534828) |
| base-b-test-2-npu-a3 / run (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133203534858) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133203534938) |
| base-b-test-4-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133203535066) |
| base-b-test-4-npu-a3 / run (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133203535134) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133215337786) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838818540/job/133215337796) |


## [Run #43838644871](https://github.com/sgl-project/sglang/actions/runs/43838644871)
- **分支**: `junlin/diffusion-npu-profiler`
- **总耗时**: 72.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43838644871

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.2min | 环境问题 | 日志中未见测试执行错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133214741183) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 可见日志仅显示 runner 初始化、下载 action、上传 429 字节 artifact 及 post job cleanup，无 Traceback/RuntimeError。若退出码为 5，多为 setUpClass 阶段 sglang server 启动失败（如 host OOM、进程被 SIGKILL），需查看省略的测试日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133214741183

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133201720566) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133201720710) |
| multimodal-gen-test-4-npu-a3 (0) | 26.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702229) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702340) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702416) |
| multimodal-gen-test-1-npu-a3 (1) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702418) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702475) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702587) |
| base-b-test-4-npu-a3 / run (1) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702626) |
| base-b-test-16-npu-a3 / run (0) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702636) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702656) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133202702699) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 44.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133214740899) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43838644871/job/133214741026) |


## [Run #43837908042](https://github.com/sgl-project/sglang/actions/runs/43837908042)
- **分支**: `feat/qsa-cache-sharding`
- **总耗时**: 61.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43837908042

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 2.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133215269583) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志中测试阶段以退出码5结束，表示unittest存在errors，最常见原因是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL）。日志省略部分未显示具体Traceback，需查看artifact中的测试日志确认真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133215269583

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133199283023) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133199283041) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490653) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490690) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490722) |
| multimodal-gen-test-1-npu-a3 (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490725) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490807) |
| base-b-test-16-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490810) |
| base-b-test-8-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490858) |
| base-b-test-4-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490863) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200490970) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133200491184) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 27.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133215269606) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837908042/job/133215269671) |


## [Run #43837753413](https://github.com/sgl-project/sglang/actions/runs/43837753413)
- **分支**: `test/rlhf-test-coverage`
- **总耗时**: 17.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43837753413

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 7.4min | 其他 | 日志被截断，缺少实际测试失败的错误信息，无法定位根因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892788) |
| base-b-test-2-npu-a3 / run (0) | 7.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892810) |

- **base-b-test-1-npu-a3 / run (0)**: 可见日志仅为 runner 初始化、action 下载、artifact 上传和清理阶段，中间省略部分才包含测试执行输出。未见 Traceback/RuntimeError 或退出码 5 的具体报错，需查看完整日志中 setUpClass 阶段 server 启动相关错误。
  - 失败用例: npu_memory_occupation.py, npu_memory_occupation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892788

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_update_weights_from_tensor.py, npu_update_weights_from_tensor.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133199892810

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133198775588) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837753413/job/133198775643) |


## [Run #43837698399](https://github.com/sgl-project/sglang/actions/runs/43837698399)
- **分支**: `xpu-conv-scatter-strided-dst`
- **总耗时**: 11.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43837698399

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705176) |
| base-b-test-16-npu-a3 / run (0) | 7.9min | 环境问题 | 日志中未见明确错误，但用例退出码5提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705210) |
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705214) |
| base-b-test-4-npu-a3 / run (1) | 0.5min | 环境问题 | Pod 初始化失败，fs-init 容器异常退出，作业未能启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705261) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705338) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705437) |


- **base-b-test-16-npu-a3 / run (0)**: 日志被截断，仅见artifact上传与清理，无Traceback。退出码5表示unittest有errors，最可能是setUpClass时server启动失败（OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705210


- **base-b-test-4-npu-a3 / run (1)**: Pod 状态为 Failed，fs-init 容器以 exit code 255 终止，导致 job 容器一直处于 PodInitializing，测试脚本未执行。属于自托管 runner 的 Pod 启动/初始化环境问题，需联系 runner 管理员排查 fs-init 失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133199705261



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133198541317) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837698399/job/133198541405) |


## [Run #43837079639](https://github.com/sgl-project/sglang/actions/runs/43837079639)
- **分支**: `dark/dflash2-fused-select`
- **总耗时**: 12.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43837079639

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 8.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673565) |
| multimodal-gen-test-4-npu-a3 (0) | 8.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673598) |
| multimodal-gen-test-1-npu-a3 (1) | 8.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673646) |
| base-b-test-16-npu-a3 / run (0) | 9.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673710) |
| base-b-test-2-npu-a3 / run (0) | 9.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673777) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673814) |
| multimodal-gen-test-4-npu-a3 (1) | 8.8min | 环境问题 | multimodal-gen 测试作业失败，未生成 diffusion-failures 产物，疑似用例执行阶段出错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673853) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673888) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673894) |
| base-b-test-1-npu-a3 / run (0) | 4.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673922) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673565

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示未找到diffusion-failures/目录文件，无artifact上传；结合退出码5，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673598

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673646

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 k8s runner 无法正常启动/运行自定义容器（CANN 镜像），属 runner 环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673710

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码或精度问题；需联系 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673777


- **multimodal-gen-test-4-npu-a3 (1)**: 日志中仅见 'No files were found with the provided path: diffusion-failures/'，说明测试未产出失败样本目录；结合退出码 5 的约定，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），但日志省略段未显示具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673853



- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133197673922

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133196455489) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43837079639/job/133196455526) |


## [Run #43835441113](https://github.com/sgl-project/sglang/actions/runs/43835441113)
- **分支**: `clearing_console_output`
- **总耗时**: 33.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43835441113

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 1.7min | 环境问题 | 自托管 runner 容器环境异常，工作目录 /__w/_temp 不存在导致脚本无法执行 | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892409) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892425) |
| base-b-test-16-npu-a3 / run (0) | 2.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892484) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 sh: cd: can't cd to /__w/_temp，且无法打开临时脚本文件，cp 也找不到 _github_home，属于 runner 容器挂载/工作目录缺失的环境故障，非用例代码问题，需联系 runner 管理员修复。
  链接: https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892409



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133190968961) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133190969006) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892057) |
| multimodal-gen-test-1-npu-a3 (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892088) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892183) |
| multimodal-gen-test-4-npu-a3 (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892288) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892292) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892403) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43835441113/job/133191892420) |


## [Run #43831382634](https://github.com/sgl-project/sglang/actions/runs/43831382634)
- **分支**: `lsyin/delete-sgl-model-gateway`
- **总耗时**: 8.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43831382634

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 5.5min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434409) |
| base-b-test-8-npu-a3 / run (0) | 3.0min | 环境问题 | 作业在 checkout 后执行 k8s 脚本时异常退出，日志未见测试用例执行 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434419) |
| base-b-test-2-npu-a3 / run (0) | 4.8min | 其他 | 日志片段未包含实际测试失败的错误信息，仅显示产物上传和清理过程 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434447) |
| base-b-test-1-npu-a3 / run (0) | 3.0min | 环境问题 | 测试日志文件未生成，用例脚本未产出 /tmp/test-logs/*.log，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434631) |
| base-b-test-4-npu-a3 / run (1) | 1.1min | 环境问题 | 测试日志文件未生成，疑似 sglang server 启动失败导致用例报错 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133180491657) |
| base-b-test-4-npu-a3 / run (0) | 1.0min | 环境问题 | 测试日志文件未生成，用例脚本未产出任何日志，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133180491728) |

- **base-b-test-16-npu-a3 / run (0)**: 日志省略了中间关键部分，仅显示artifact上传和清理成功，无Traceback。退出码5表明unittest有errors，最可能是setUpClass时sglang server启动失败（host OOM/SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434409

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 checkout 完成后运行 /home/runner/k8s/index.js，仅出现 Node.js 弃用警告，随后清理孤儿进程，未进入测试阶段，也无 Traceback，疑似 runner/k8s 环境或脚本执行异常导致作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434419

- **base-b-test-2-npu-a3 / run (0)**: 提供的日志被省略了中间部分，可见内容只有 runner 初始化、下载 action、上传 artifact 和 post job cleanup，没有 Traceback/RuntimeError 等真实错误。退出码 5 提示 unittest 存在 errors（常见为 setUpClass 中 sglang server 启动失败），但需查看被省略的测试执行段日志才能确认具体原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434447

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'No files were found with the provided path: /tmp/test-logs/*.log'，说明测试未产生日志，结合退出码 5（unittest errors），最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），导致用例未执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133178434631

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 /tmp/test-logs/*.log 未找到，无 artifact 上传；结合退出码 5 常见于 setUpClass 阶段 server 启动失败（如 host OOM、进程被 SIGKILL），但日志中未见具体 Traceback，需查看被省略的中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133180491657

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 /tmp/test-logs/*.log 未找到，无任何 Traceback 或测试输出，说明用例在 setUpClass 启动 sglang server 阶段即失败（可能 host OOM 或进程被 SIGKILL），导致退出码 5 且无日志可上传。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133180491728

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133177475267) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133177475313) |
| sgl-router-build-aarch64 / Build sgl-router | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43831382634/job/133177558080) |


## [Run #43831160607](https://github.com/sgl-project/sglang/actions/runs/43831160607)
- **分支**: `amd/dsv41-gfx950-mega-mhc-prefill`
- **总耗时**: 16.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43831160607

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.9min | 环境问题 | 日志被截断，缺少实际测试错误信息，无法定位具体失败原因 | [job link](https://github.com/sgl-project/sglang/actions/runs/43831160607/job/133180255594) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 可见日志仅为 runner 初始化、artifact 上传和清理阶段，未包含测试执行或 Traceback 内容；退出码 5 提示 unittest 存在 errors，可能为 setUpClass 中 sglang server 启动失败，但需完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43831160607/job/133180255594

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43831160607/job/133176773863) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43831160607/job/133176773927) |
| base-b-test-2-npu-a3 / run (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43831160607/job/133177689935) |


## [Run #43824992515](https://github.com/sgl-project/sglang/actions/runs/43824992515)
- **分支**: `pr/muse-gfx1250`
- **总耗时**: 37.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43824992515

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 15.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519210) |

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519210

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133156724422) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133156724429) |
| multimodal-gen-test-1-npu-a3 (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519109) |
| multimodal-gen-test-1-npu-a3 (1) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519120) |
| base-b-test-16-npu-a3 / run (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519139) |
| multimodal-gen-test-4-npu-a3 (0) | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519150) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519157) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519168) |
| base-b-test-1-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519175) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519192) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824992515/job/133157519262) |


## [Run #43824404171](https://github.com/sgl-project/sglang/actions/runs/43824404171)
- **分支**: `lsyin/gateway-source-only`
- **总耗时**: 13.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43824404171

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 10.4min | 环境问题 | 日志中未见明确错误，但作业以退出码5失败，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577669) |
| multimodal-gen-test-4-npu-a3 (0) | 10.8min | 环境问题 | 多模态生成测试用例执行失败，上传了 diffusion-failures 产物，疑似 server 启动失败导致 unittest errors。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577723) |
| multimodal-gen-test-1-npu-a3 (1) | 10.2min | 环境问题 | multimodal-gen 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577733) |
| multimodal-gen-test-4-npu-a3 (1) | 10.2min | 环境问题 | multimodal 测试失败，上传了 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577775) |
| base-b-test-16-npu-a3 / run (0) | 11.0min | 环境问题 | 日志中未见明确错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577890) |
| base-b-test-1-npu-a3 / run (0) | 11.1min | 环境问题 | 日志被截断，无法看到真实错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577914) |
| base-b-test-2-npu-a3 / run (0) | 11.1min | 环境问题 | 日志中未见测试执行失败的具体错误，作业在 artifact 上传后正常清理，失败原因需查看被省略的中间日志。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577999) |
| base-b-test-4-npu-a3 / run (0) | 7.0min | 环境问题 | 日志中未见明确错误，但作业以退出码5结束，提示unittest存在errors，常见于setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133160668082) |
| base-b-test-4-npu-a3 / run (1) | 6.2min | 环境问题 | 日志被截断，未见真实错误，但退出码5提示unittest存在errors，最可能是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL）。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133160668391) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志仅显示artifact上传和清理，无Traceback。退出码5表示unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577669

- **multimodal-gen-test-4-npu-a3 (0)**: 日志中上传了 diffusion-failures-npu-2-part0-2.zip 失败产物，说明用例运行出错；结合退出码 5 与背景知识，最可能是 setUpClass 阶段 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看产物中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577723

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中段被省略，仅见上传 diffusion-failures-npu-1-part1-2.zip 失败产物，退出码 5 提示 unittest errors，最可能是 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看省略段 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577733

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾仅显示上传 diffusion-failures-npu-2-part1-2.zip 产物并清理，未直接给出 Traceback；结合退出码 5 与产物名，推测为 setUpClass 阶段 sglang server 启动失败（如 host OOM/进程被 SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577775

- **base-b-test-16-npu-a3 / run (0)**: 可见日志仅显示 checkout、下载 action、上传 selected-test-logs artifact 及 post job cleanup，均成功；关键失败信息位于省略的中间部分，无法据此判定具体原因，建议查看完整日志中退出码 5 对应的 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577890

- **base-b-test-1-npu-a3 / run (0)**: 日志中段被省略，未见Traceback/RuntimeError等真实错误；仅见artifact上传成功与Node.js弃用警告。退出码5表明unittest有errors，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577914

- **base-b-test-2-npu-a3 / run (0)**: 日志首尾显示 runner 启动、下载 action、上传 selected-test-logs artifact 均成功，Post job cleanup 正常，无 Traceback/RuntimeError。失败点位于省略的中间测试阶段，需查看完整日志确认是否为 setUpClass 阶段 server 启动失败（退出码 5）。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577999

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾仅显示artifact上传成功和清理步骤，未包含实际测试失败Traceback；退出码5表明unittest有errors，最可能是setUpClass中sglang server启动失败（host OOM/SIGKILL），需查看被省略的中间日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133160668082

- **base-b-test-4-npu-a3 / run (1)**: 日志仅显示artifact上传与清理，缺少Traceback。退出码5表示unittest有errors，常见于setUpClass中server启动失败（OOM/SIGKILL），需查看被省略的测试日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133160668391

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133158769492) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133158769558) |
| sgl-router-build-aarch64 / Build sgl-router | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133158834177) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43824404171/job/133159577970) |


## [Run #43815338052](https://github.com/sgl-project/sglang/actions/runs/43815338052)
- **分支**: `fix/mha-kv-pool-hnd-init`
- **总耗时**: 25.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43815338052

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 22.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135146) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135146

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133158226164) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133158226201) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159134892) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135025) |
| base-b-test-8-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135093) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135133) |
| base-b-test-4-npu-a3 / run (1) | 10.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135143) |
| base-b-test-1-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135204) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815338052/job/133159135213) |


## [Run #43815036461](https://github.com/sgl-project/sglang/actions/runs/43815036461)
- **分支**: `feat/npu-glm5-flash`
- **总耗时**: 25.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43815036461

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 5.0min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864195) |
| base-b-test-1-npu-a3 / run (0) | 21.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864224) |

- **base-b-test-8-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_eplb_min_rebalancing_utilization_threshold.py, npu_eplb_min_rebalancing_utilization_threshold.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864195

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_eagle3.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864224

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125260228) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125260277) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864027) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864105) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864109) |
| base-b-test-16-npu-a3 / run (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864138) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864186) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43815036461/job/133125864236) |


## [Run #43814553696](https://github.com/sgl-project/sglang/actions/runs/43814553696)
- **分支**: `pr-36601`
- **总耗时**: 25.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43814553696

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 19.9min | 代码错误 | QSA NPU 算子测试用例 test_qsa_npu.py 执行失败，导致作业退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407544) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/attention/qsa/test_qsa_npu.py 的 passed 为 false（耗时 40 秒），其余用例均通过，最终进程以 exit code 1 结束。失败集中在 QSA attention 算子测试，属于代码或算子实现问题，需查看该用例的 Traceback 定位具体报错。
  - 失败用例: qwen3.8-flash-next-decode-b2-attn-tp4-cap65536, qwen3.8-flash-next-verify-t4-attn-tp8-cap65536, qsa_npu.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407544

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133123663540) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133123663566) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407443) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407476) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407520) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407545) |
| base-b-test-16-npu-a3 / run (0) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407553) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407566) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43814553696/job/133124407644) |


## [Run #43813430545](https://github.com/sgl-project/sglang/actions/runs/43813430545)
- **分支**: `pr/muse-gfx1250`
- **总耗时**: 13.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43813430545

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 9.1min | 环境问题 | diffusion 测试失败，未生成失败产物目录，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889646) |
| multimodal-gen-test-1-npu-a3 (0) | 9.8min | 环境问题 | multimodal 测试未生成 diffusion-failures 目录，疑似用例执行阶段失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889667) |
| multimodal-gen-test-4-npu-a3 (1) | 9.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889694) |
| multimodal-gen-test-1-npu-a3 (1) | 9.0min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889725) |
| base-b-test-16-npu-a3 / run (0) | 10.0min | 环境问题 | Scheduler watchdog 超时，容器执行失败，疑似 host OOM 或进程被 SIGKILL 导致 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889813) |
| base-b-test-2-npu-a3 / run (0) | 10.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889875) |
| base-b-test-1-npu-a3 / run (0) | 10.0min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889887) |
| base-b-test-4-npu-a3 / run (0) | 10.0min | 环境问题 | 自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120890005) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 目录，说明测试未产出失败样本；结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 OOM、SIGKILL），但日志中未出现明确 Traceback，需查看被省略的中间段确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889646

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试脚本未产出失败样本目录；结合退出码 5，可能是 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），但日志省略了真实 Traceback，需查看中间段确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889667

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示未找到diffusion-failures/目录，无产物上传；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889694

- **multimodal-gen-test-1-npu-a3 (1)**: 日志中未见明确 Traceback，但退出码5表示 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 diffusion-failures/ 目录无文件，未上传产物。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889725

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 TP13 EP13 Scheduler watchdog timeout（300s），随后报错“Executing the custom container implementation failed”，模型分片加载虽完成但服务未就绪，属环境/资源类失败，非用例收集问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889813

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 server 已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889875

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于自托管 runner 容器环境异常，并非用例或代码本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889887

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 返回200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120890005

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120111200) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120111351) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120889876) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43813430545/job/133120890025) |


## [Run #43810205772](https://github.com/sgl-project/sglang/actions/runs/43810205772)
- **分支**: `megakernel-dsa-view-draft-capture`
- **总耗时**: 50.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43810205772

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 21.2min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133119106381) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133119106381

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110101123) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110101183) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110857798) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110857863) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110857924) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110857978) |
| multimodal-gen-test-4-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110857980) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110858004) |
| base-b-test-4-npu-a3 / run (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110858016) |
| base-b-test-1-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110858051) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110858066) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133110858074) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133119106327) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810205772/job/133119106372) |


## [Run #43810096726](https://github.com/sgl-project/sglang/actions/runs/43810096726)
- **分支**: `ecao/fp8_moe_v2`
- **总耗时**: 49.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43810096726

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 21.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133118867077) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试请求均返回 200 OK，随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133118867077

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133109780081) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133109780131) |
| multimodal-gen-test-1-npu-a3 (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389758) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389788) |
| multimodal-gen-test-4-npu-a3 (0) | 28.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389862) |
| multimodal-gen-test-4-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389865) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389918) |
| base-b-test-8-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389945) |
| base-b-test-1-npu-a3 / run (0) | 24.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110389982) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110390015) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110390016) |
| base-b-test-4-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133110390034) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133118867061) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43810096726/job/133118867093) |


## [Run #43804853680](https://github.com/sgl-project/sglang/actions/runs/43804853680)
- **分支**: `megakernel-dsa-view-draft-capture`
- **总耗时**: 41.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43804853680

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.4min | 环境问题 | 容器内未安装 sglang 模块，导致测试脚本导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017045) |

- **base-b-test-16-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/环境中未正确安装 sglang 包（可能 pip 安装步骤缺失或失败），进程退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017045

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133093287493) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133093287518) |
| multimodal-gen-test-1-npu-a3 (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094016833) |
| multimodal-gen-test-4-npu-a3 (1) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094016913) |
| multimodal-gen-test-1-npu-a3 (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094016947) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017008) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017041) |
| base-b-test-1-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017049) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017061) |
| base-b-test-4-npu-a3 / run (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017079) |
| multimodal-gen-test-4-npu-a3 (0) | 37.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804853680/job/133094017344) |


## [Run #43804776385](https://github.com/sgl-project/sglang/actions/runs/43804776385)
- **分支**: `hicache-async-write-back-demote`
- **总耗时**: 26.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43804776385

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 6.2min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636312) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 145 秒后 FAILED (errors=1)，2 个用例 0 通过，脚本非零退出导致作业失败；日志未显示具体 Traceback，需查看该用例 setUpClass 阶段 server 启动或断言错误。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636312

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093034415) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093034558) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636091) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636107) |
| base-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636209) |
| base-b-test-2-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636224) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636251) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636292) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43804776385/job/133093636303) |


## [Run #43801519578](https://github.com/sgl-project/sglang/actions/runs/43801519578)
- **分支**: `feat/dsv41-packed-main-kv-sm90-attention`
- **总耗时**: 31.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43801519578

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.5min | 环境问题 | 容器内未安装 sglang 包，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402799) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402891) |

- **base-b-test-16-npu-a3 / run (0)**: run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明测试镜像/环境中缺少 sglang 安装，属于环境配置问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402799


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133094620983) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133094621036) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402705) |
| multimodal-gen-test-4-npu-a3 (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402730) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402809) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402812) |
| base-b-test-8-npu-a3 / run (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402826) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43801519578/job/133095402869) |


## [Run #43800797825](https://github.com/sgl-project/sglang/actions/runs/43800797825)
- **分支**: `lossless-gdn-tuple-verify`
- **总耗时**: 24.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43800797825

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 3.5min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276141) |

- **base-b-test-16-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内未正确安装或未设置 PYTHONPATH，属于环境/安装配置问题，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276141

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133080464627) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133080464713) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081275821) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081275884) |
| base-b-test-4-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276033) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276035) |
| base-b-test-1-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276048) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276123) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43800797825/job/133081276172) |


## [Run #43799734401](https://github.com/sgl-project/sglang/actions/runs/43799734401)
- **分支**: `feat/npu-glm5-flash`
- **总耗时**: 149.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43799734401

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 39.0min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133111636686) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载到76%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器运行时故障，并非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133111636686

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133076887356) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133076887359) |
| multimodal-gen-test-4-npu-a3 (1) | 11.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675397) |
| base-b-test-4-npu-a3 / run (0) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675498) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675506) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675514) |
| base-b-test-16-npu-a3 / run (0) | 94.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675517) |
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675519) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675544) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133077675571) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133111636626) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799734401/job/133111636781) |


## [Run #43799666292](https://github.com/sgl-project/sglang/actions/runs/43799666292)
- **分支**: `main-v4.1-cp-bcg`
- **总耗时**: 39.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43799666292

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 12.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609659) |
| base-b-test-16-npu-a3 / run (0) | 3.3min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609693) |


- **base-b-test-16-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 包未正确安装或 PYTHONPATH 未包含源码目录，属于环境/安装配置问题，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609693

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133076912450) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133076912544) |
| multimodal-gen-test-4-npu-a3 (1) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609483) |
| multimodal-gen-test-1-npu-a3 (1) | 15.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609509) |
| multimodal-gen-test-4-npu-a3 (0) | 29.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609568) |
| multimodal-gen-test-1-npu-a3 (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609583) |
| base-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609598) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609641) |
| base-b-test-1-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609650) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43799666292/job/133077609722) |


## [Run #43798212629](https://github.com/sgl-project/sglang/actions/runs/43798212629)
- **分支**: `hicache-async-write-back-demote`
- **总耗时**: 54.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43798212629

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 3.3min | 环境问题 | 缺少 tqdm 模块导致测试脚本导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133083497106) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 13.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133083497116) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 运行 run_suite.py 时导入 sglang 触发 ModuleNotFoundError: No module named 'tqdm'，依赖未安装完整，测试未执行即退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133083497106


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133071975095) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133071975131) |
| multimodal-gen-test-4-npu-a3 (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072575964) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072575965) |
| base-b-test-2-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072576011) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072576015) |
| base-b-test-16-npu-a3 / run (0) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072576020) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072576085) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072576096) |
| base-b-test-8-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133072576128) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43798212629/job/133083497247) |


## [Run #43796932779](https://github.com/sgl-project/sglang/actions/runs/43796932779)
- **分支**: `feature/amd-glm5-dsa-mla-decode-gfx950`
- **总耗时**: 48.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43796932779

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.0min | 环境问题 | 测试环境缺少 tqdm 模块导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133078044044) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: run_suite.py 导入 sglang 时在 interpreter.py 中 import tqdm 报 ModuleNotFoundError，说明容器镜像或依赖安装步骤未安装 tqdm，测试在用例执行前即失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133078044044

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133067911645) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133067911655) |
| base-b-test-2-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133068627129) |
| base-b-test-16-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133068627170) |
| base-b-test-4-npu-a3 / run (1) | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133068627229) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133068627232) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133078044170) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796932779/job/133078044191) |


## [Run #43796865497](https://github.com/sgl-project/sglang/actions/runs/43796865497)
- **分支**: `fangyuan/dspark_fly`
- **总耗时**: 31.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43796865497

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 20.3min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报 errors=1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133074601746) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_pd_disaggregation.py 运行 147s 后 FAILED (errors=1)，退出码非零，最可能是 setUpClass 阶段 sglang server 启动失败（如 OOM 或进程被 SIGKILL），需查看日志中 Traceback 确认具体异常。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133074601746

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133073745668) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133073745747) |
| base-b-test-1-npu-a3 / run (0) | 6.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133074601729) |
| base-b-test-2-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133074601730) |
| base-b-test-4-npu-a3 / run (1) | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43796865497/job/133074601761) |


## [Run #43795661445](https://github.com/sgl-project/sglang/actions/runs/43795661445)
- **分支**: `cryang/pr/sparsity-pd-disagg-LRU`
- **总耗时**: 7.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43795661445

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 5.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43795661445/job/133064486803) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43795661445/job/133063916388) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43795661445/job/133063916403) |


## [Run #43794593360](https://github.com/sgl-project/sglang/actions/runs/43794593360)
- **分支**: `fix/grammar-cache-lru`
- **总耗时**: 102.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43794593360

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.8min | 环境问题 | 测试环境缺少 tqdm 模块，导致导入 sglang 失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133084481408) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 运行 run_suite.py 时导入 sglang 触发 ModuleNotFoundError: No module named 'tqdm'，说明依赖安装不完整（install_sglang_deps 未装 tqdm），测试在收集阶段即崩溃，退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133084481408

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133060520537) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133060520572) |
| multimodal-gen-test-4-npu-a3 (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061168998) |
| multimodal-gen-test-4-npu-a3 (0) | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169068) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169181) |
| base-b-test-8-npu-a3 / run (0) | 67.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169195) |
| base-b-test-4-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169205) |
| base-b-test-4-npu-a3 / run (1) | 71.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169234) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169257) |
| base-b-test-2-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133061169336) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133084481429) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794593360/job/133084481448) |


## [Run #43794522920](https://github.com/sgl-project/sglang/actions/runs/43794522920)
- **分支**: `xiangch/fused-wo-b-gemm-ar-main`
- **总耗时**: 10.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43794522920

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.0min | 环境问题 | 测试环境缺少 tqdm 模块导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794522920/job/133062744643) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 运行 run_suite.py 时导入 sglang 触发 ModuleNotFoundError: No module named 'tqdm'，说明依赖未正确安装（install_sglang_deps 未生效或镜像缺包），进程退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43794522920/job/133062744643

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794522920/job/133060314319) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794522920/job/133060314341) |
| base-b-test-2-npu-a3 / run (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794522920/job/133061017822) |


## [Run #43794210036](https://github.com/sgl-project/sglang/actions/runs/43794210036)
- **分支**: `fix/pd-eagle-mtp-cpu-retraction`
- **总耗时**: 62.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43794210036

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 10.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099492) |
| base-b-test-1-npu-a3 / run (0) | 56.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099534) |
| base-b-test-16-npu-a3 / run (0) | 4.0min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099587) |
| base-b-test-4-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099618) |
| base-b-test-4-npu-a3 / run (1) | 55.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099620) |



- **base-b-test-16-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内未正确安装或未设置 PYTHONPATH，属环境/依赖配置问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099587



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133059317088) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133059317108) |
| multimodal-gen-test-1-npu-a3 (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099391) |
| multimodal-gen-test-4-npu-a3 (0) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099403) |
| multimodal-gen-test-4-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099449) |
| multimodal-gen-test-1-npu-a3 (1) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099471) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43794210036/job/133060099523) |


## [Run #43793564223](https://github.com/sgl-project/sglang/actions/runs/43793564223)
- **分支**: `uocr2-mps-defaults`
- **总耗时**: 9.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43793564223

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 3.7min | 环境问题 | 测试脚本导入 sglang 模块失败，环境未正确安装或 PYTHONPATH 未配置 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133058213771) |
| base-b-test-1-npu-a3 / run (0) | 3.6min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133058213837) |

- **base-b-test-4-npu-a3 / run (0)**: run_suite.py 第11行 from sglang.test.ci.ci_register 报 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 包未安装或工作目录/PYTHONPATH 未包含源码路径，导致测试无法启动，退出码1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133058213771

- **base-b-test-1-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内 sglang 包未安装或 PYTHONPATH 未包含源码目录，属于环境/依赖配置问题，进程退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133058213837

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133057537903) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133057537997) |
| base-b-test-2-npu-a3 / run (0) | 6.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133058213745) |
| base-b-test-4-npu-a3 / run (1) | 3.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793564223/job/133058213766) |


## [Run #43793232884](https://github.com/sgl-project/sglang/actions/runs/43793232884)
- **分支**: `prefill_graph_ascend_ops_on_main`
- **总耗时**: 9.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43793232884

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 6.5min | 环境问题 | diffusion 测试失败且未生成失败产物，疑似 server 启动失败或进程异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837450) |
| multimodal-gen-test-1-npu-a3 (0) | 6.4min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837455) |
| multimodal-gen-test-4-npu-a3 (1) | 6.3min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837479) |
| base-b-test-8-npu-a3 / run (0) | 6.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837480) |
| multimodal-gen-test-4-npu-a3 (0) | 6.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837482) |
| base-b-test-2-npu-a3 / run (0) | 6.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837569) |
| base-b-test-1-npu-a3 / run (0) | 6.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837584) |
| base-b-test-16-npu-a3 / run (0) | 6.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837590) |
| base-b-test-4-npu-a3 / run (1) | 6.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837601) |
| base-b-test-4-npu-a3 / run (0) | 3.1min | 环境问题 | 容器内未安装 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837661) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试未产出失败样本；结合退出码 5 常见于 setUpClass 阶段 sglang server 启动失败（如 OOM/SIGKILL），但省略段缺少真实 Traceback，需查看中间日志确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837450

- **multimodal-gen-test-1-npu-a3 (0)**: 日志中未见明确 Traceback，但退出码5表示 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM、进程被 SIGKILL）。同时 upload-artifact 未找到 diffusion-failures/ 目录，说明测试未正常产出结果。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837455

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业在约6分钟内结束，无明确Traceback。结合退出码5，最可能是setUpClass中server启动失败（如host OOM或进程被SIGKILL），需查看省略的中间日志确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837479


- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行失败未产出结果；退出码5对应unittest errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837482

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在模型权重加载阶段，属于 runner/容器环境异常，非用例代码错误，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837569

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已正常启动并 ready，随后报错 'Executing the custom container implementation failed'，属于 runner/容器基础设施故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837584

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载过程中报错“Executing the custom container implementation failed”，属于自托管 runner 容器执行环境异常，非用例代码或精度问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837590

- **base-b-test-4-npu-a3 / run (1)**: 日志显示测试请求已成功返回（POST /generate 200 OK），随后报错“Executing the custom container implementation failed”，属于 runner 容器环境/基础设施故障，并非用例断言失败或代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837601

- **base-b-test-4-npu-a3 / run (0)**: 运行 test/run_suite.py 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/环境中未正确安装 sglang 包（或 PYTHONPATH 未包含源码目录），进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056837661

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056288941) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793232884/job/133056288962) |


## [Run #43793181393](https://github.com/sgl-project/sglang/actions/runs/43793181393)
- **分支**: `feature/yunkai/gdn-verify-aiter`
- **总耗时**: 41.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43793181393

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 15.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133098142211) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133098142211

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091816264) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091816331) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091817233) |
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091817717) |
| base-b-test-16-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091817816) |
| base-b-test-2-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091817903) |
| multimodal-gen-test-1-npu-a3 (1) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091818036) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091818149) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091818728) |
| multimodal-gen-test-1-npu-a3 (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091847879) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091859954) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133091860283) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133098142124) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43793181393/job/133098142130) |


## [Run #43792255174](https://github.com/sgl-project/sglang/actions/runs/43792255174)
- **分支**: `feat/qsa-cache-sharding`
- **总耗时**: 132.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43792255174

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.9min | 环境问题 | 测试环境缺少 tqdm 模块导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133086140499) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 运行 run_suite.py 时导入 sglang 触发 ModuleNotFoundError: No module named 'tqdm'，说明容器内 Python 依赖未正确安装，属环境/依赖问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133086140499

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133053262534) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133053262582) |
| multimodal-gen-test-4-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074772) |
| multimodal-gen-test-4-npu-a3 (0) | 27.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074822) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074870) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074886) |
| base-b-test-4-npu-a3 / run (0) | 98.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074907) |
| base-b-test-8-npu-a3 / run (0) | 86.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074916) |
| multimodal-gen-test-1-npu-a3 (0) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074935) |
| base-b-test-2-npu-a3 / run (0) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054074936) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054075019) |
| base-b-test-4-npu-a3 / run (1) | 92.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133054075059) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133086140464) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 26.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43792255174/job/133086140492) |


## [Run #43791613655](https://github.com/sgl-project/sglang/actions/runs/43791613655)
- **分支**: `junlin/diffusion-npu-profiler`
- **总耗时**: 101.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43791613655

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 89.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963974) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示模型分片加载过程中报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，并非用例或代码本身的问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963974

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051229534) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051229632) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963697) |
| multimodal-gen-test-1-npu-a3 (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963726) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963772) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963832) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963906) |
| base-b-test-1-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963908) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963915) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963941) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43791613655/job/133051963943) |


## [Run #43788623536](https://github.com/sgl-project/sglang/actions/runs/43788623536)
- **分支**: `npu-npugraph-ex-static-kernel`
- **总耗时**: 127.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43788623536

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 109.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539775) |
| base-b-test-2-npu-a3 / run (0) | 3.1min | 环境问题 | 容器内未安装 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539817) |
| base-b-test-8-npu-a3 / run (0) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539834) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539957) |
| base-b-test-1-npu-a3 / run (0) | 107.3min | 环境问题 | 作业在 checkout 后执行 k8s 索引脚本时异常退出，未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539967) |
| base-b-test-4-npu-a3 / run (0) | 9.5min | 环境问题 | GitHub Actions 下载 action 时网络超时/503，作业在准备阶段失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539985) |


- **base-b-test-2-npu-a3 / run (0)**: 运行 test/run_suite.py 时抛出 ModuleNotFoundError: No module named 'sglang'，说明镜像/环境中未正确安装 sglang 包（或 PYTHONPATH 未包含源码目录），进程退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539817



- **base-b-test-1-npu-a3 / run (0)**: 日志显示 checkout 完成后运行 /home/runner/k8s/index.js 即结束，仅有 Node 弃用警告，无测试输出或 Traceback，疑似 runner/k8s 环境或脚本执行异常导致作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539967

- **base-b-test-4-npu-a3 / run (0)**: Runner 通过 squid 代理访问 codeload.github.com 下载 actions/checkout、download-artifact 等 action 时多次超时并返回 503 Service Unavailable，重试 3 次后仍失败，作业在准备阶段终止，未进入用例执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539985

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133041904092) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133041904117) |
| multimodal-gen-test-4-npu-a3 (0) | 32.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539709) |
| multimodal-gen-test-1-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539733) |
| multimodal-gen-test-1-npu-a3 (0) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539736) |
| multimodal-gen-test-4-npu-a3 (1) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43788623536/job/133042539750) |


## [Run #43783279191](https://github.com/sgl-project/sglang/actions/runs/43783279191)
- **分支**: `qkang/elastic-ep-mooncake-scale-down`
- **总耗时**: 249.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43783279191

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 177.6min | 环境问题 | 作业在 checkout 阶段被中断，未进入测试执行，疑似 runner 或网络异常导致作业提前终止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046809) |
| base-b-test-4-npu-a3 / run (0) | 175.5min | 环境问题 | 作业在 checkout 后清理阶段异常结束，未进入测试执行，疑似 runner/容器环境异常。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046859) |
| base-b-test-1-npu-a3 / run (0) | 245.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046921) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 checkout 完成后执行 k8s/index.js 时立即出现 Cleaning up orphan processes 并结束，无测试输出与退出码，属 runner/环境侧中断，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046809

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾仅显示 checkout 完成、清理孤儿进程及 Node.js 20 弃用警告，无测试用例执行或 Traceback，作业在准备阶段即终止，属 runner 环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046859


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133025275452) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133025275497) |
| multimodal-gen-test-4-npu-a3 (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046606) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046615) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046631) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046678) |
| base-b-test-16-npu-a3 / run (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046764) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046821) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43783279191/job/133026046879) |


## [Run #43779232427](https://github.com/sgl-project/sglang/actions/runs/43779232427)
- **分支**: `codex/fix-amd-dsa-dense-dp-graph`
- **总耗时**: 156.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43779232427

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 146.2min | 环境问题 | Git 拉取代码时远端返回 503/not our ref，重试后 checkout 成功但作业仍失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014856931) |
| base-b-test-16-npu-a3 / run (0) | 142.5min | 环境问题 | Git 拉取 PR 合并提交时远端返回 not our ref，重试后成功但作业最终失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014857007) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示下载 actions/checkout 时多次 503 Service Unavailable，随后 git fetch 报 'upload-pack: not our ref'，重试约 25 分钟后才成功 checkout；失败源于代码托管/代理服务不稳定，非用例本身问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014856931

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 git fetch 报 'upload-pack: not our ref f9e85b7...'（exit 128），重试后从 git-cdn 镜像拉取成功并完成 checkout；失败源于代码托管/镜像同步的临时不可用（此前还有 503 下载失败），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014857007

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014099392) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014099410) |
| base-b-test-4-npu-a3 / run (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014856957) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014856970) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43779232427/job/133014856996) |


## [Run #43778857464](https://github.com/sgl-project/sglang/actions/runs/43778857464)
- **分支**: `new-model-support`
- **总耗时**: 191.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43778857464

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 185.2min | 环境问题 | Git 拉取 PR 合并提交失败，远端仓库不存在该 ref | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180378) |
| base-b-test-4-npu-a3 / run (0) | 11.0min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012809623) |

- **base-b-test-16-npu-a3 / run (0)**: checkout 阶段多次重试 git fetch 1e57235898ab4aa5350d22983d0d78b4bf740b90，均报 upload-pack: not our ref，exit code 128，导致作业在拉取代码时即失败，未进入测试阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180378

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012809623

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133011372417) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133011372429) |
| sgl-router-build-aarch64 / Build sgl-router | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133011428211) |
| multimodal-gen-test-1-npu-a3 (1) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180227) |
| multimodal-gen-test-1-npu-a3 (0) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180231) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180336) |
| multimodal-gen-test-4-npu-a3 (0) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180376) |
| multimodal-gen-test-4-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180411) |
| base-b-test-2-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180506) |
| base-b-test-1-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012180578) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43778857464/job/133012809619) |


## [Run #43777828139](https://github.com/sgl-project/sglang/actions/runs/43777828139)
- **分支**: `codex/fix-amd-dsa-dense-dp-graph`
- **总耗时**: 19.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43777828139

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 8.7min | 环境问题 | Pod 拉取镜像失败，容器处于 ImagePullBackOff 状态，作业无法启动。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133009143593) |
| base-b-test-2-npu-a3 / run (0) | 14.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133009143612) |
| base-b-test-4-npu-a3 / run (0) | 11.5min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133009143670) |

- **base-b-test-16-npu-a3 / run (0)**: 镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，重试 300 秒后超过宽限期，Pod 一直 Pending。需检查镜像名/标签是否存在、私有仓库 imagePullSecret 凭据、节点到仓库的网络（DNS/防火墙/代理/TLS）。
  链接: https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133009143593



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133008425214) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133008425250) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133009143529) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43777828139/job/133009143611) |


## [Run #43777009435](https://github.com/sgl-project/sglang/actions/runs/43777009435)
- **分支**: `codex/fix-amd-dsa-dense-dp-graph`
- **总耗时**: 8.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43777009435

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 3.8min | 超时 | 作业在下载 action 后等待过久被取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207534) |
| base-b-test-16-npu-a3 / run (0) | 2.0min | 超时 | 作业在下载 action 阶段被取消，疑似超时。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207544) |
| base-b-test-8-npu-a3 / run (0) | 2.8min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动测试容器阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207547) |
| base-b-test-4-npu-a3 / run (0) | 2.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207618) |
| base-b-test-4-npu-a3 / run (1) | 2.4min | 超时 | 作业在下载 action 阶段被取消，疑似超时或外部中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207621) |

- **base-b-test-2-npu-a3 / run (0)**: 日志显示下载 actions/checkout、github-script、download-artifact 后，于 23:58:01 报 'A task was canceled.'，无测试执行或 Traceback，属于作业超时/被取消，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207534

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 Getting action download info 后约90秒出现 A task was canceled，未进入用例执行，无 Traceback，判断为下载 action 超时/取消，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207544

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 k8s 容器启动阶段，测试尚未真正运行，属 runner/容器环境问题，非用例或代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207547

- **base-b-test-4-npu-a3 / run (0)**: 日志显示构建 sglang 及 xatlas 过程中报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境异常，非代码或测试用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207618

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 runner 启动正常，但在 Getting action download info 后约 58 秒出现 'A task was canceled.'，未进入用例执行阶段，无 Traceback 或退出码 5，故非用例失败，属作业被取消/超时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133006207621

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133005587738) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43777009435/job/133005587853) |


## [Run #43775819612](https://github.com/sgl-project/sglang/actions/runs/43775819612)
- **分支**: `inkling-2-small-support`
- **总耗时**: 5.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43775819612

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-a-test-npu | 0.7min | 代码错误 | 测试文件缺少 __main__ 入口导致用例收集失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43775819612/job/133001851396) |

- **base-a-test-npu**: run_suite.py 收集用例时，ci_register.py 检测到 test_unified_mxfp8.py 缺少 `if __name__ == "__main__":` 入口，抛出 ValueError，进程退出码 1。需为该文件补充 unittest.main() 或 pytest.main 入口。
  链接: https://github.com/sgl-project/sglang/actions/runs/43775819612/job/133001851396

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775819612/job/133001851346) |
| sgl-router-build-aarch64 / Build sgl-router | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775819612/job/133001896129) |


## [Run #43775083176](https://github.com/sgl-project/sglang/actions/runs/43775083176)
- **分支**: `fix/prefill-delayer-deferring-dp-rank`
- **总耗时**: 42.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43775083176

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 35.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270892) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270892

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/132999573486) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/132999573501) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270591) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270626) |
| base-b-test-2-npu-a3 / run (0) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270796) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270816) |
| base-b-test-4-npu-a3 / run (1) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270841) |
| base-b-test-4-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270876) |
| base-b-test-1-npu-a3 / run (0) | 33.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43775083176/job/133000270888) |


## [Run #43773979054](https://github.com/sgl-project/sglang/actions/runs/43773979054)
- **分支**: `asahi/ubtree`
- **总耗时**: 33.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43773979054

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 8.9min | 环境问题 | pip 安装 pytest 依赖 packaging 时找不到可用版本，依赖安装失败导致作业退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659365) |
| base-b-test-2-npu-a3 / run (0) | 15.4min | 环境问题 | pip 安装 pytest 依赖 packaging 时找不到可用版本，导致依赖安装失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659394) |
| base-b-test-16-npu-a3 / run (0) | 10.0min | 环境问题 | pip 安装依赖失败，无法找到 packaging 包，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659436) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 pip 报错：Could not find a version that satisfies the requirement packaging (from pytest)，且大量版本因 Requires-Python 不匹配被忽略，最终 No matching distribution found，进程以 exit code 1 结束，属于依赖源/环境配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659365

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 pip 报错：Could not find a version that satisfies the requirement packaging (from pytest)，且大量版本因 Python 版本不匹配被忽略，最终 exit code 1，属依赖源/环境配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659394

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 pip 报错：Could not find a version that satisfies the requirement packaging (from pytest)，No matching distribution found，说明依赖源不可用或网络/代理问题，属环境问题而非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659436

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996019981) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996020035) |
| multimodal-gen-test-1-npu-a3 (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659261) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659273) |
| multimodal-gen-test-4-npu-a3 (0) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659278) |
| multimodal-gen-test-1-npu-a3 (0) | 14.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659295) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659378) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659386) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43773979054/job/132996659511) |


## [Run #43764842686](https://github.com/sgl-project/sglang/actions/runs/43764842686)
- **分支**: `nvidia-megakernel-binding-offers`
- **总耗时**: 34.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43764842686

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 27.6min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173899) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173899

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132967645831) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132967645850) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173787) |
| multimodal-gen-test-1-npu-a3 (1) | 15.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173817) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173819) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173843) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173864) |
| base-b-test-2-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173883) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173919) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173929) |
| base-b-test-1-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764842686/job/132968173951) |


## [Run #43764100939](https://github.com/sgl-project/sglang/actions/runs/43764100939)
- **分支**: `nvidia-runtime-opts-hybrid-gdn-qsa`
- **总耗时**: 40.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43764100939

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 9.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983228) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965339176) |
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965339205) |
| multimodal-gen-test-1-npu-a3 (0) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983048) |
| multimodal-gen-test-1-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983051) |
| multimodal-gen-test-4-npu-a3 (0) | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983089) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983126) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983152) |
| base-b-test-1-npu-a3 / run (0) | 36.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983177) |
| base-b-test-2-npu-a3 / run (0) | 36.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983214) |
| base-b-test-16-npu-a3 / run (0) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983286) |
| base-b-test-4-npu-a3 / run (0) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43764100939/job/132965983405) |


## [Run #43753468054](https://github.com/sgl-project/sglang/actions/runs/43753468054)
- **分支**: `feat/hold-cold-prefill-admission`
- **总耗时**: 43.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43753468054

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 37.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176200) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176200

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132932465623) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132932465708) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176213) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176233) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176254) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176319) |
| base-b-test-4-npu-a3 / run (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176324) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176345) |
| base-b-test-2-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43753468054/job/132933176410) |


## [Run #43747523604](https://github.com/sgl-project/sglang/actions/runs/43747523604)
- **分支**: `diffusion-offload-phase01`
- **总耗时**: 32.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43747523604

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 15.4min | 环境问题 | 自托管 runner 的 k8s 容器执行失败，临时文件丢失导致作业异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914557768) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，随后 runner 报 ENOENT 打开 _runner_file_commands 下 .nfs 临时文件失败，Node 进程崩溃退出码 1，属 runner 环境/文件系统问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914557768

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914102492) |
| multimodal-gen-test-4-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914557451) |
| multimodal-gen-test-4-npu-a3 (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914557510) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43747523604/job/132914557528) |


## [Run #43741622410](https://github.com/sgl-project/sglang/actions/runs/43741622410)
- **分支**: `wuyaole/fix-prefill-reservation-budget`
- **总耗时**: 17.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43741622410

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 14.0min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在安装依赖后异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700886) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700926) |
| base-b-test-1-npu-a3 / run (0) | 10.4min | 环境问题 | 自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700945) |
| base-b-test-4-npu-a3 / run (0) | 11.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700967) |
| base-b-test-2-npu-a3 / run (0) | 12.1min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700972) |
| base-b-test-16-npu-a3 / run (0) | 8.0min | 环境问题 | 自托管 runner 的自定义容器启动失败，作业在运行测试前即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896701095) |

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 sgl-kernel-npu 等 wheel 安装完成后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境/基础设施故障，非用例代码问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700886

- **base-b-test-4-npu-a3 / run (1)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  链接: https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700926

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 Executing the custom container implementation failed，请自托管 runner 管理员排查；此前测试正常推进至第3个用例，非用例本身报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700945

- **base-b-test-4-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700967

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed'，提示联系 self-hosted runner 管理员，属于 runner 容器运行时故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700972

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，容器镜像/运行时异常导致作业无法进入测试阶段，与用例代码无关，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896701095

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132895980352) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132895980426) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700792) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43741622410/job/132896700877) |


## [Run #43738458482](https://github.com/sgl-project/sglang/actions/runs/43738458482)
- **分支**: `nvidia-megakernel-binding-offers`
- **总耗时**: 57.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43738458482

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 32.0min | 环境问题 | pip 安装 triton-ascend 依赖 pandas 时找不到匹配版本，导致构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245267) |

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 pip 解析 triton-ascend 依赖 pandas 时，因 Python 3.12 与 pandas 可用版本 Requires-Python 约束不匹配，报 No matching distribution found，进程退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245267

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132892678315) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132892678392) |
| multimodal-gen-test-4-npu-a3 (0) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245153) |
| multimodal-gen-test-1-npu-a3 (1) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245161) |
| base-b-test-2-npu-a3 / run (0) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245212) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245253) |
| base-b-test-16-npu-a3 / run (0) | 26.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245264) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245270) |
| base-b-test-4-npu-a3 / run (0) | 52.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245297) |
| base-b-test-1-npu-a3 / run (0) | 29.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245400) |
| multimodal-gen-test-4-npu-a3 (1) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43738458482/job/132893245410) |


## [Run #43737037780](https://github.com/sgl-project/sglang/actions/runs/43737037780)
- **分支**: `fix/swa-window-lock-walk-split`
- **总耗时**: 42.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43737037780

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 34.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603080) |
| base-b-test-16-npu-a3 / run (0) | 27.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603090) |
| base-b-test-2-npu-a3 / run (0) | 8.4min | 环境问题 | GitHub Actions 下载 action 超时，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603094) |
| base-b-test-1-npu-a3 / run (0) | 30.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603108) |
| base-b-test-4-npu-a3 / run (0) | 33.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132883243182) |



- **base-b-test-2-npu-a3 / run (0)**: Runner 通过代理访问 codeload.github.com 下载 actions/github-script 时多次超时并返回 503，重试 3 次仍失败，属于网络/代理环境问题，非代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603094



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132881933738) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132881933831) |
| sgl-router-build-aarch64 / Build sgl-router | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132881975844) |
| multimodal-gen-test-4-npu-a3 (0) | 29.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603017) |
| multimodal-gen-test-1-npu-a3 (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603026) |
| multimodal-gen-test-4-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603029) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132882603035) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43737037780/job/132883243232) |


## [Run #43735781479](https://github.com/sgl-project/sglang/actions/runs/43735781479)
- **分支**: `xpu/weekly-simple-model-enablement-2026-11-09`
- **总耗时**: 39.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43735781479

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 27.5min | 环境问题 | pip 安装 triton-ascend 依赖 numpy==1.26.4 时找不到可用版本，导致依赖安装失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769389) |
| base-b-test-1-npu-a3 / run (0) | 30.0min | 环境问题 | pip 从 PyPI 拉取 setuptools 超时，导致依赖安装失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769395) |
| base-b-test-4-npu-a3 / run (0) | 27.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769415) |

- **base-b-test-2-npu-a3 / run (0)**: 安装 triton-ascend==3.2.2 时，其依赖 numpy==1.26.4 在 aarch64/py3.12 源中无匹配版本（from versions: none），pip 报 No matching distribution，进程退出码 1，作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769389

- **base-b-test-1-npu-a3 / run (0)**: 安装 sgl-kernel-npu 后，uv/pip 请求 https://pypi.org/simple/setuptools/ 重试3次仍超时（operation timed out），进程退出码1，作业失败。属网络/代理环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769395


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878114475) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878114497) |
| multimodal-gen-test-1-npu-a3 (1) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769129) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769153) |
| multimodal-gen-test-4-npu-a3 (1) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769187) |
| multimodal-gen-test-4-npu-a3 (0) | 31.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769227) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769374) |
| base-b-test-16-npu-a3 / run (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769388) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735781479/job/132878769401) |


## [Run #43735291168](https://github.com/sgl-project/sglang/actions/runs/43735291168)
- **分支**: `dark/eagle-fused-draft-sample`
- **总耗时**: 42.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43735291168

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 17.9min | 环境问题 | pip 安装 triton-ascend 依赖 decorator==5.1.1 时找不到匹配版本，导致依赖安装失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142916) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 pip 报错 Could not find a version that satisfies the requirement decorator==5.1.1 (from triton-ascend)，No matching distribution found，进程退出码 1，属于依赖源/镜像缺少该包的环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142916

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132876543879) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132876543889) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142683) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142687) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142748) |
| base-b-test-8-npu-a3 / run (0) | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142780) |
| base-b-test-16-npu-a3 / run (0) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142806) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142862) |
| base-b-test-1-npu-a3 / run (0) | 21.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142871) |
| base-b-test-4-npu-a3 / run (1) | 29.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142905) |
| base-b-test-2-npu-a3 / run (0) | 37.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43735291168/job/132877142955) |


## [Run #43733176480](https://github.com/sgl-project/sglang/actions/runs/43733176480)
- **分支**: `pd-prefill-release-mm-features`
- **总耗时**: 33.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43733176480

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 27.9min | 环境问题 | pip 安装 triton-ascend 依赖 numpy==1.26.4 时找不到可用版本，导致依赖安装失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704877) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 ERROR: Could not find a version that satisfies the requirement numpy==1.26.4 (from triton-ascend) (from versions: none)，随后进程以退出码 1 结束。属于依赖源/环境配置问题，非代码或性能回归。
  链接: https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704877

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870046438) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870046472) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704716) |
| multimodal-gen-test-4-npu-a3 (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704753) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704816) |
| base-b-test-16-npu-a3 / run (0) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704843) |
| base-b-test-8-npu-a3 / run (0) | 26.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704845) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704852) |
| base-b-test-1-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43733176480/job/132870704935) |


## [Run #43731068586](https://github.com/sgl-project/sglang/actions/runs/43731068586)
- **分支**: `perf/ltx2-vae-gap`
- **总耗时**: 46.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43731068586

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.1min | 环境问题 | 下载 actions/checkout 动作超时并返回 503，作业在准备阶段失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132873419900) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132873419934) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.6min | 环境问题 | pip 安装 uv 失败，找不到可用版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132873419964) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: Runner 通过代理下载 actions/checkout@v4 时，首次请求 100 秒超时，重试两次均返回 503 Service Unavailable，3 次尝试后放弃，作业未进入测试阶段。
  链接: https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132873419900


- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 在安装依赖阶段执行 pip install uv 时，报错 ERROR: Could not find a version that satisfies the requirement uv (from versions: none)，随后进程以退出码 1 结束，属于依赖源或网络代理导致的环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132873419964

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132863497936) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132863497974) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109598) |
| multimodal-gen-test-1-npu-a3 (1) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109626) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109661) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109663) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109718) |
| base-b-test-2-npu-a3 / run (0) | 26.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109744) |
| base-b-test-16-npu-a3 / run (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109761) |
| base-b-test-1-npu-a3 / run (0) | 28.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109770) |
| base-b-test-4-npu-a3 / run (0) | 29.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109786) |
| base-b-test-4-npu-a3 / run (1) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43731068586/job/132864109849) |


## [Run #43729962952](https://github.com/sgl-project/sglang/actions/runs/43729962952)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 46.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43729962952

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 32.0min | 环境问题 | 安装依赖 memfabric-hybrid==1.3.0 失败，找不到匹配版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838878) |

- **base-b-test-4-npu-a3 / run (0)**: pip 安装 memfabric-hybrid==1.3.0 时提示无可用版本（from versions: none），导致进程退出码 1，作业失败。属于依赖包源缺失或版本不可用的环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838878

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860131870) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860131886) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838513) |
| multimodal-gen-test-4-npu-a3 (0) | 28.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838523) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838546) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838618) |
| base-b-test-2-npu-a3 / run (0) | 30.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838675) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838715) |
| base-b-test-1-npu-a3 / run (0) | 28.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838805) |
| base-b-test-4-npu-a3 / run (1) | 42.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860838924) |
| base-b-test-8-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43729962952/job/132860839201) |


## [Run #43691440937](https://github.com/sgl-project/sglang/actions/runs/43691440937)
- **分支**: `kimi31-dflash2-ragged-verify`
- **总耗时**: 44.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43691440937

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 33.7min | 环境问题 | pip 安装 sglang-router 失败，找不到匹配版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877610184) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 pip 安装依赖时执行 `pip install sglang-router` 报错：Could not find a version that satisfies the requirement sglang-router (from versions: none)，即该包在配置的索引源中不存在，导致安装步骤退出码 1，作业失败。属于依赖/环境配置问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877610184

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877609547) |
| base-b-test-4-npu-a3 / run (1) | 42.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877610049) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877610370) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877610386) |
| multimodal-gen-test-4-npu-a3 (0) | 5.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877610840) |
| base-b-test-1-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877611267) |
| multimodal-gen-test-4-npu-a3 (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877611278) |
| base-b-test-2-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877611369) |
| base-b-test-8-npu-a3 / run (0) | 7.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691440937/job/132877612143) |


## [Run #43412247935](https://github.com/sgl-project/sglang/actions/runs/43412247935)
- **分支**: `feat/glm52-dspark-npu-upstream`
- **总耗时**: 13.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43412247935

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 9.3min | 环境问题 | Pod 拉取镜像失败，容器无法启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43412247935/job/133027090090) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 容器镜像 swr.cn-southwest-2.myhuaweicloud.com/base_image/ascend-ci/cann:9.1.0-a3-ubuntu22.04-py3.12 拉取失败，ImagePullBackOff 超过300秒，Pod 一直 Pending，作业未执行测试即退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/43412247935/job/133027090090

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43412247935/job/133026285188) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43412247935/job/133026285263) |


## [Run #43411886427](https://github.com/sgl-project/sglang/actions/runs/43411886427)
- **分支**: `ci/npu-fed-labels-only`
- **总耗时**: 33.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43411886427

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.0min | 代码错误 | NPU DP attention 测试文件运行失败，23个用例中1个报错，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629318) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629345) |
| base-b-test-4-npu-a3 / run (1) | 11.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629351) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行312秒后 FAILED (errors=1)，2个测试文件0/2通过。日志未显示具体 Traceback，需查看该用例 setUpClass 阶段 server 启动是否失败（如 OOM/SIGKILL）。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629318



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133032805113) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133032805118) |
| multimodal-gen-test-1-npu-a3 (1) | 16.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629245) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629251) |
| multimodal-gen-test-4-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629278) |
| multimodal-gen-test-4-npu-a3 (0) | 30.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629283) |
| base-b-test-1-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629359) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629393) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43411886427/job/133033629447) |


---
*Auto-generated by ci_monitor.py*