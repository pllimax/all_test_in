# NPU CI 执行监控（2026-11-15）
**生成时间**: 2026-11-16 07:10
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-15 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 92

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 599 个 | 失败 128 个 | 成功 Job 平均耗时 11.9min
- **Run 执行情况**: 成功 36 个 | 失败 56 个 | 成功 Run 平均耗时 16.5min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-4-npu-a3 / run (0) | 87.2min | #43712936550 | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905166) |
| base-b-test-1-npu-a3 / run (0) | 48.2min | #43703826593 | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043149) |
| base-b-test-2-npu-a3 / run (0) | 47.5min | #43712936550 | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905121) |
| base-b-test-4-npu-a3 / run (1) | 47.3min | #43650375358 | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999236) |
| base-b-test-1-npu-a3 / run (0) | 47.2min | #43712936550 | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905152) |
| base-b-test-4-npu-a3 / run (0) | 46.6min | #43713534897 | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979626) |
| base-b-test-4-npu-a3 / run (1) | 44.5min | #43670079359 | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900952) |
| base-b-test-1-npu-a3 / run (0) | 41.1min | #43713534897 | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979643) |
| base-b-test-2-npu-a3 / run (0) | 40.6min | #43713534897 | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979662) |
| base-b-test-8-npu-a3 / run (0) | 37.0min | #43703826593 | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043114) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-16-npu-a3 / run (0) | 171.1min | #43691057907 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293064) |
| base-b-test-4-npu-a3 / run (0) | 151.1min | #43695978100 | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987189) |
| base-b-test-8-npu-a3 / run (0) | 147.7min | #43693961888 | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986667) |
| base-b-test-16-npu-a3 / run (0) | 123.2min | #43695978100 | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987183) |
| base-b-test-1-npu-a3 / run (0) | 113.8min | #43696206407 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069898) |
| base-b-test-2-npu-a3 / run (0) | 105.2min | #43696206407 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069826) |
| base-b-test-4-npu-a3 / run (0) | 91.3min | #43698458050 | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058072) |
| base-b-test-1-npu-a3 / run (0) | 88.6min | #43698458050 | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058086) |
| base-b-test-8-npu-a3 / run (0) | 78.4min | #43675983084 | [job link](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748930616) |
| base-b-test-4-npu-a3 / run (1) | 70.2min | #43691617584 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993777) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-b-test-4-npu-a3 / run (0) | 62 | 34 | 15 | 4 | 9 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663357)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987189)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986726)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132747519600)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493573) |
| base-b-test-16-npu-a3 / run (0) | 47 | 24 | 12 | 7 | 4 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987183)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293064)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082562)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037473)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588092) |
| base-b-test-8-npu-a3 / run (0) | 48 | 31 | 7 | 5 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905170)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519814)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588087)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503916)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748930616) |
| base-b-test-4-npu-a3 / run (1) | 62 | 46 | 7 | 3 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979671)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905185)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841920)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866524)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493536) |
| base-b-test-1-npu-a3 / run (0) | 56 | 40 | 4 | 5 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058086)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069898)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920384)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774508) |
| base-b-test-2-npu-a3 / run (0) | 56 | 45 | 3 | 2 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690381)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069826)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132549157689) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 8 | 5 | 1 | 2 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591513) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 4 | 1 | 2 | 1 | 0 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132793646894)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591491) |
| base-a-test-npu | 80 | 78 | 1 | 0 | 1 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43696996490/job/132759759935) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_dp_attention.py` | 36 | 23 | 13 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663357)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986726)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132747519600) |
| `npu_speculative_moe_a2a_backend.py` | 28 | 24 | 4 | [base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082562)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900913)<br>[base-b-test-16-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405707) |
| `npu_pd_disaggregation.py` | 36 | 34 | 2 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979671)<br>[base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493536) |
| `ernie_image_t2i_1npu` | 25 | 24 | 1 | [multimodal-gen-test-1-npu-a3 (1)](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493507) |
| `wan2_1_t2v_1.3b_1_npu` | 24 | 23 | 1 | [multimodal-gen-test-1-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035563) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 2 | 1 | 1 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132793646894) |
| `[code=1]` | 1 | 0 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493536) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43691057907<br>[#44237 [Fix] embedding: Do not reuse prefixes or split prefills for encoder models](https://github.com/sgl-project/sglang/pull/44237) | `fix/encoder-embedding-prefix-reuse` | 190.1min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43691057907) |
| #43695978100<br>[#46858 [Feat] lfm3: Add text, vision, audio and Omni support](https://github.com/sgl-project/sglang/pull/46858) | `lfm3` | 154.1min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43695978100) |
| #43693961888<br>[#45803 [Fix] parser: Fix reasoning/tool-call grammar handoff and GLM-4.5 argument parsing](https://github.com/sgl-project/sglang/pull/45803) | `feat/ling3-pub-parser` | 152.9min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43693961888) |
| #43696206407<br>[#50522 [Chore] inkling: Bump tml-renderers to 0.4.1](https://github.com/sgl-project/sglang/pull/50522) | `inkling2-port-renderers` | 126.4min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43696206407) |
| #43698458050<br>[#44576 [Fix] disaggregation: Release multimodal features when PD prefill finishes a request](https://github.com/sgl-project/sglang/pull/44576) | `pd-prefill-release-mm-features` | 101.7min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43698458050) |
| #43699054234<br>[#43367 [Feat] [NPU] Diffusion: support Wan2.2-T2V-A14B W4A4F4 DAOS with MXFP4 Attention](https://github.com/sgl-project/sglang/pull/43367) | `F4_support` | 90.7min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43699054234) |
| #43712936550<br>[#50311 [Perf] mem_cache: Cut unified-memory admission host work](https://github.com/sgl-project/sglang/pull/50311) | `main` | 90.5min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43712936550) |
| #43675983084<br>[#49328 [Fix] hicache: Report L3 prefetch tokens already cached during the read](https://github.com/sgl-project/sglang/pull/49328) | `shuwen/hicache-host-covered-reason` | 87.6min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43675983084) |
| #43691617584<br>[#50584 [CI] npu: Launch sgl-router in the NPU multi-node tests and ship it in the NPU image](https://github.com/sgl-project/sglang/pull/50584) | `lsyin/npu-multinode-sgl-router` | 75.1min | 3 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43691617584) |
| #43703826593<br>[#50548 [Perf] scheduler: Retry hybrid SWA admission only after freed capacity can admit a refused request](https://github.com/sgl-project/sglang/pull/50548) | `fix/swa-admission-retry-on-capacity-growth` | 71.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43703826593) |
| #43696996964<br>[#50584 [CI] npu: Launch sgl-router in the NPU multi-node tests and ship it in the NPU image](https://github.com/sgl-project/sglang/pull/50584) | `lsyin/npu-multinode-sgl-router` | 70.6min | 4 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43696996964) |
| #43671680250<br>[#50032 [Perf] scheduler: Cut per-step host work in the batch-1 speculative decode loop](https://github.com/sgl-project/sglang/pull/50032) | `spec-batch1-host-loop` | 69.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43671680250) |
| #43676656385<br>[#50122 [Feat] mem_cache: Add an opt-in state-only, cost-based eviction order for Mamba states (--radix-eviction-policy state_cost)](https://github.com/sgl-project/sglang/pull/50122) | `feat/mamba-gds-eviction-option` | 66.9min | 2 | base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43676656385) |
| #43700682108<br>[#42938 [Feat] [Apple Silicon] MPS execution: Compile Torch-owned decode with MLX and Metal attention](https://github.com/sgl-project/sglang/pull/42938) | `adding-mlx-region-runner` | 58.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43700682108) |
| #43707971541<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 56.5min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43707971541) |
| #43650375358<br>[#49735 [Feat] rust-server: Pause and continue generation, freeze_gc, ping and ready, and the frontend state](https://github.com/sgl-project/sglang/pull/49735) | `rainj-me/rust-apis-02-pause-and-frontend-state` | 52.2min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43650375358) |
| #43692622100 | `inkling2-port-renderers` | 51.2min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43692622100) |
| #43702022037<br>[#42745 [Fix] radix_cache: Cap SWA lock-walk pinning at one window in the Rust TreeCore](https://github.com/sgl-project/sglang/pull/42745) | `fix/swa-window-lock-walk-split` | 50.6min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43702022037) |
| #43669962809<br>[#40893 [Fix] spec: Support a reduced draft vocabulary in rejection sampling](https://github.com/sgl-project/sglang/pull/40893) | `fix/eagle3-rs-reduced-draft-vocab` | 50.2min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43669962809) |
| #43713534897<br>[#50503 [Perf] [AMD] qwen3.5: Route the 512-expert softmax router through aiter topk_gating on gfx942](https://github.com/sgl-project/sglang/pull/50503) | `amd/qwen35-topk-gating-gfx942` | 49.8min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43713534897) |
| #43670079359<br>[#46412 [Refactor] multimodal: [MM refactor 6/9] Serve token-space processors behind --enable-token-space-processor](https://github.com/sgl-project/sglang/pull/46412) | `rockdu-dev-mm-v2/06-sglang-wrapper` | 49.5min | 2 | base-b-test-16-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43670079359) |
| #43676131862<br>[#45488 [Fix] [NVIDIA] kvcache: Gate fused FP8 prefix-valid commit kernel on SM89+](https://github.com/sgl-project/sglang/pull/45488) | `sm86-prefix-valid-gate` | 49.4min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43676131862) |
| #43681790474<br>[#50584 [CI] npu: Launch sgl-router in the NPU multi-node tests and ship it in the NPU image](https://github.com/sgl-project/sglang/pull/50584) | `lsyin/npu-multinode-sgl-router` | 47.9min | 3 | base-b-test-4-npu-a3 / run (1), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43681790474) |
| #43682180915<br>[#43048 [Feat] qwen4-exp: Support GR and PLE sequence parallelism](https://github.com/sgl-project/sglang/pull/43048) | `feat/qwen4-exp-layernorm-sp` | 47.8min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43682180915) |
| #43614554379<br>[#44492 [Feat] [AMD] mori: Run MORI EPv2 dispatch/combine on AsyncLL kernels for TBO](https://github.com/sgl-project/sglang/pull/44492) | `mori_epv2_asyncll_tbo` | 45.1min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43614554379) |
| #43264688614<br>[#50146 [Fix] scheduler: Join the prefill delayer all-gather on DP ranks that defer prefill](https://github.com/sgl-project/sglang/pull/50146) | `fix/prefill-delayer-deferring-dp-rank` | 40.2min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43264688614) |
| #43708356841<br>[#50032 [Perf] scheduler: Cut per-step host work in the batch-1 speculative decode loop](https://github.com/sgl-project/sglang/pull/50032) | `spec-batch1-host-loop` | 39.6min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43708356841) |
| #43675877358<br>[#35647 [Refactor] mem_cache: [11/N] extract KVCache and BaseSWAKVPool into pool/base.py](https://github.com/sgl-project/sglang/pull/35647) | `refactor/mem-cache-pool-base` | 39.0min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43675877358) |
| #43651347487<br>[#33111 [Feat] elastic-ep: Runtime scale-down that retires EP ranks via Mooncake deactivate_ranks](https://github.com/sgl-project/sglang/pull/33111) | `qkang/elastic-ep-mooncake-scale-down` | 38.8min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43651347487) |
| #43640378159 | `rainj-me/rust-apis-02-pause-and-frontend-state` | 37.5min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43640378159) |
| #43691763295<br>[#50576 [Fix] usage: Report reasoning_tokens as 0 when the model does not think](https://github.com/sgl-project/sglang/pull/50576) | `usage-zero-reasoning-tokens` | 37.3min | 2 | base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43691763295) |
| #43628789421<br>[#50122 [Feat] mem_cache: Add an opt-in state-only, cost-based eviction order for Mamba states (--radix-eviction-policy state_cost)](https://github.com/sgl-project/sglang/pull/50122) | `feat/mamba-gds-eviction-option` | 36.6min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43628789421) |
| #43264721540<br>[#50147 [Fix] dp-attention: Deliver an abort behind its request on every DP rank](https://github.com/sgl-project/sglang/pull/50147) | `fix/dp-attention-abort-order` | 34.0min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43264721540) |
| #43660235863<br>[#48409 [Feat] scheduler: add fixed-batch bounded LPM policy](https://github.com/sgl-project/sglang/pull/48409) | `codex/bounded-lpm-window` | 33.3min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43660235863) |
| #43682170289<br>[#50389 [Perf] [NVIDIA] diffusion: Read both TP ranks' partial sums in the epilogue kernel (Z-Image, Qwen-Image-2.1)](https://github.com/sgl-project/sglang/pull/50389) | `mick/tp2-peer-partial-epilogue` | 31.9min | 1 | base-b-test-8-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43682170289) |
| #43677030516<br>[#42103 [Feat] weights: Add native ModelExpress weight transfer backend support](https://github.com/sgl-project/sglang/pull/42103) | `hwoo/delta-recipes-sglang` | 31.7min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43677030516) |
| #43687728145<br>[#46412 [Refactor] multimodal: [MM refactor 6/9] Serve token-space processors behind --enable-token-space-processor](https://github.com/sgl-project/sglang/pull/46412) | `rockdu-dev-mm-v2/06-sglang-wrapper` | 31.6min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43687728145) |
| #43660965189<br>[#50562 [CI] rerun-test: Run NPU single-node test files, with --hw to pick the backend](https://github.com/sgl-project/sglang/pull/50562) | `lsyin/rerun-test-npu-amd` | 31.1min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43660965189) |
| #43194202418<br>[#50049 [Perf] dspark: Fold the static verify epilogue's commits into the accept tail and trim the verify-to-draft glue](https://github.com/sgl-project/sglang/pull/50049) | `dspark-greedy-verify-tail-glue` | 26.1min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43194202418) |
| #43684197278<br>[#50587 [Feat] (draft, do not review yet) dflash: Confidence-scheduled compact verify for DFlash2 on Kimi K3.1](https://github.com/sgl-project/sglang/pull/50587) | `kimi31-dflash2-ragged-verify` | 23.9min | 2 | base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43684197278) |
| #43197020181<br>[#50051 [Perf] scheduler: Send a finished request's last output before its prefix-cache insert and free its prompt ids after the next dispatch](https://github.com/sgl-project/sglang/pull/50051) | `stream-finished-output-before-cache-insert` | 23.7min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43197020181) |
| #43636925061<br>[#50548 [Perf] scheduler: Retry hybrid SWA admission only after freed capacity can admit a refused request](https://github.com/sgl-project/sglang/pull/50548) | `fix/swa-admission-retry-on-capacity-growth` | 23.1min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43636925061) |
| #43687325521<br>[#50587 [Feat] (draft, do not review yet) dflash: Confidence-scheduled compact verify for DFlash2 on Kimi K3.1](https://github.com/sgl-project/sglang/pull/50587) | `kimi31-dflash2-ragged-verify` | 22.8min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43687325521) |
| #43690323117<br>[#45803 [Fix] parser: Fix reasoning/tool-call grammar handoff and GLM-4.5 argument parsing](https://github.com/sgl-project/sglang/pull/45803) | `feat/ling3-pub-parser` | 22.6min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43690323117) |
| #43682036509<br>[#50559 [Refactor] auth: Declare every HTTP route's auth level in one table that the Python and Rust servers both read](https://github.com/sgl-project/sglang/pull/50559) | `lsyin/auth-levels-parity` | 22.4min | 1 | base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43682036509) |
| #43608653616<br>[#48409 [Feat] scheduler: add fixed-batch bounded LPM policy](https://github.com/sgl-project/sglang/pull/48409) | `codex/bounded-lpm-window` | 21.2min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43608653616) |
| #43668796010<br>[#40893 [Fix] spec: Support a reduced draft vocabulary in rejection sampling](https://github.com/sgl-project/sglang/pull/40893) | `fix/eagle3-rs-reduced-draft-vocab` | 20.8min | 3 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43668796010) |
| #43681315776<br>[#50562 [CI] rerun-test: Run NPU single-node test files, with --hw to pick the backend](https://github.com/sgl-project/sglang/pull/50562) | `lsyin/rerun-test-npu-amd` | 20.2min | 8 | multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43681315776) |
| #43628113274<br>[#50544 [Feat] dp-controller: Forward a scheduler's router_l3_layout entry in the startup handshake](https://github.com/sgl-project/sglang/pull/50544) | `oss-sync-a012215732` | 17.9min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43628113274) |
| #43691592070 | `inkling2-port-renderers` | 14.2min | 8 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), base-b-test-16-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43691592070) |
| #43668127214<br>[#40893 [Fix] spec: Support a reduced draft vocabulary in rejection sampling](https://github.com/sgl-project/sglang/pull/40893) | `fix/eagle3-rs-reduced-draft-vocab` | 13.8min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43668127214) |
| #43697766713<br>[#44576 [Fix] disaggregation: Release multimodal features when PD prefill finishes a request](https://github.com/sgl-project/sglang/pull/44576) | `pd-prefill-release-mm-features` | 13.5min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43697766713) |
| #43602678499<br>[#42224 [Perf] [NPU] dsa: Add INT8 LightningIndexer to accelerate indexing on A2/A3](https://github.com/sgl-project/sglang/pull/42224) | `int8_lightening_indexer` | 10.8min | 1 | base-b-test-16-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43602678499) |
| #43682861025<br>[#50562 [CI] rerun-test: Run NPU single-node test files, with --hw to pick the backend](https://github.com/sgl-project/sglang/pull/50562) | `lsyin/rerun-test-npu-amd` | 9.0min | 7 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (0), base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43682861025) |
| #43696996490<br>[#50186 [Feat] inkling2: Support Inkling-2-Small](https://github.com/sgl-project/sglang/pull/50186) | `inkling-2-small-support` | 5.1min | 1 | base-a-test-npu | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43696996490) |
| #43683305183<br>[#50562 [CI] rerun-test: Run NPU single-node test files, with --hw to pick the backend](https://github.com/sgl-project/sglang/pull/50562) | `lsyin/rerun-test-npu-amd` | 5.0min | 1 | base-a-test-npu | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43683305183) |

---


## [Run #43713534897](https://github.com/sgl-project/sglang/actions/runs/43713534897)
- **分支**: `amd/qwen35-topk-gating-gfx942`
- **总耗时**: 49.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43713534897

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 29.0min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报 errors=1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979671) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 205 秒后 FAILED (errors=1)，退出码 1，测试汇总 0/2 通过；日志省略部分未显示具体 Traceback，推测为 setUpClass 阶段 server 启动或初始化异常，需查看完整错误堆栈定位。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979671

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843422794) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843422875) |
| multimodal-gen-test-1-npu-a3 (1) | 15.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979583) |
| multimodal-gen-test-4-npu-a3 (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979589) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979596) |
| base-b-test-4-npu-a3 / run (0) | 46.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979626) |
| multimodal-gen-test-4-npu-a3 (1) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979627) |
| base-b-test-16-npu-a3 / run (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979638) |
| base-b-test-1-npu-a3 / run (0) | 41.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979643) |
| base-b-test-2-npu-a3 / run (0) | 40.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979662) |
| base-b-test-8-npu-a3 / run (0) | 28.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43713534897/job/132843979716) |


## [Run #43712936550](https://github.com/sgl-project/sglang/actions/runs/43712936550)
- **分支**: `main`
- **总耗时**: 90.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43712936550

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 13.6min | 环境问题 | 安装 Rust 工具链时下载超时导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905170) |
| base-b-test-4-npu-a3 / run (1) | 51.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905185) |

- **base-b-test-8-npu-a3 / run (0)**: 脚本检测到无 cargo，通过 rustup 安装 1.92 工具链，下载 channel-rust-1.92.toml 时网络超时（operation timed out），退出码 1。此前下载 action 也出现 503，属网络/代理不稳定。
  链接: https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905170


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808355380) |
| multimodal-gen-test-4-npu-a3 (1) | 20.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808904975) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808904995) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808904998) |
| multimodal-gen-test-1-npu-a3 (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905077) |
| base-b-test-2-npu-a3 / run (0) | 47.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905121) |
| base-b-test-1-npu-a3 / run (0) | 47.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905152) |
| base-b-test-16-npu-a3 / run (0) | 29.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905154) |
| base-b-test-4-npu-a3 / run (0) | 87.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43712936550/job/132808905166) |


## [Run #43708356841](https://github.com/sgl-project/sglang/actions/runs/43708356841)
- **分支**: `spec-batch1-host-loop`
- **总耗时**: 39.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43708356841

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 20.2min | 环境问题 | pip 安装 triton-ascend 依赖 decorator==5.1.1 时找不到匹配版本，依赖安装失败导致作业退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841920) |

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 ERROR: Could not find a version that satisfies the requirement decorator==5.1.1 (from triton-ascend)，No matching distribution found，进程退出码 1。属于依赖源/网络或版本不可用问题，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841920

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794379324) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794379344) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841791) |
| multimodal-gen-test-4-npu-a3 (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841830) |
| multimodal-gen-test-4-npu-a3 (0) | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841843) |
| multimodal-gen-test-1-npu-a3 (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841854) |
| base-b-test-4-npu-a3 / run (0) | 34.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841894) |
| base-b-test-8-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841910) |
| base-b-test-16-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841947) |
| base-b-test-2-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794841964) |
| base-b-test-1-npu-a3 / run (0) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43708356841/job/132794842022) |


## [Run #43707971541](https://github.com/sgl-project/sglang/actions/runs/43707971541)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 56.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43707971541

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 53.3min | 环境问题 | 安装 Rust 时从 rustup 下载脚本被中断，导致 shell 语法错误，作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866524) |

- **base-b-test-4-npu-a3 / run (1)**: curl 下载 https://sh.rustup.rs 时连接中断（transfer closed with 446 bytes remaining），管道传给 sh 的脚本不完整，报 Syntax error: end of file unexpected，退出码 1。属于网络/代理环境问题，非代码或测试用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866524

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793207674) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793207685) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866439) |
| multimodal-gen-test-4-npu-a3 (0) | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866456) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866468) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866486) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866566) |
| base-b-test-16-npu-a3 / run (0) | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866581) |
| base-b-test-1-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866593) |
| base-b-test-8-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866615) |
| base-b-test-2-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43707971541/job/132793866647) |


## [Run #43703826593](https://github.com/sgl-project/sglang/actions/runs/43703826593)
- **分支**: `fix/swa-admission-retry-on-capacity-growth`
- **总耗时**: 71.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43703826593

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132793646894) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132793646894

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132780599664) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132780599682) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781042969) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043071) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043094) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043112) |
| base-b-test-8-npu-a3 / run (0) | 37.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043114) |
| base-b-test-16-npu-a3 / run (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043121) |
| multimodal-gen-test-4-npu-a3 (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043135) |
| base-b-test-1-npu-a3 / run (0) | 48.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132781043149) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132793646893) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43703826593/job/132793646949) |


## [Run #43702022037](https://github.com/sgl-project/sglang/actions/runs/43702022037)
- **分支**: `fix/swa-window-lock-walk-split`
- **总耗时**: 50.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43702022037

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690298) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690311) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690346) |
| base-b-test-2-npu-a3 / run (0) | 7.5min | 环境问题 | 下载 GitHub Action 归档超时并返回 503，导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690381) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132776297233) |
| base-b-test-4-npu-a3 / run (0) | 40.9min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132776297328) |




- **base-b-test-2-npu-a3 / run (0)**: 下载 actions/download-artifact 时两次因 HttpClient 100 秒超时重试，第三次返回 503 Service Unavailable，3 次尝试后失败，属网络/代理环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690381



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775117008) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775117037) |
| sgl-router-build-aarch64 / Build sgl-router | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775160552) |
| multimodal-gen-test-4-npu-a3 (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690256) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43702022037/job/132775690287) |


## [Run #43700682108](https://github.com/sgl-project/sglang/actions/runs/43700682108)
- **分支**: `adding-mlx-region-runner`
- **总耗时**: 58.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43700682108

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 49.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614346) |
| base-b-test-8-npu-a3 / run (0) | 51.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614409) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771023228) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771023275) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614213) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614234) |
| multimodal-gen-test-4-npu-a3 (1) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614261) |
| multimodal-gen-test-1-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614275) |
| base-b-test-16-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614293) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614314) |
| base-b-test-2-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614339) |
| base-b-test-1-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43700682108/job/132771614351) |


## [Run #43699054234](https://github.com/sgl-project/sglang/actions/runs/43699054234)
- **分支**: `F4_support`
- **总耗时**: 90.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43699054234

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 67.5min | 环境问题 | pip 安装 sglang-router 时访问 pypi.org 超时，导致构建依赖失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519814) |

- **base-b-test-8-npu-a3 / run (0)**: 日志显示连接 pypi.org 443 端口 ReadTimeoutError（read timeout=15），随后安装 build 依赖 setuptools>=45 失败，报 No matching distribution found，最终 exit code 1。属于网络/代理环境问题，非代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519814

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766012406) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766012410) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519670) |
| multimodal-gen-test-1-npu-a3 (1) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519673) |
| multimodal-gen-test-4-npu-a3 (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519708) |
| base-b-test-16-npu-a3 / run (0) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519767) |
| multimodal-gen-test-1-npu-a3 (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519775) |
| base-b-test-4-npu-a3 / run (1) | 6.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519872) |
| base-b-test-4-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43699054234/job/132766519879) |


## [Run #43698458050](https://github.com/sgl-project/sglang/actions/runs/43698458050)
- **分支**: `pd-prefill-release-mm-features`
- **总耗时**: 101.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43698458050

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 91.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058072) |
| base-b-test-1-npu-a3 / run (0) | 88.6min | 环境问题 | 编译 sglang-router 时缺少 pkg-config，导致 wheel 构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058086) |


- **base-b-test-1-npu-a3 / run (0)**: 构建 sglang-router 的 Rust 扩展时，openssl-sys 需要 pkg-config 来定位 OpenSSL，但容器内未安装该工具，cargo 编译失败（exit 101），pip 构建 wheel 失败，作业退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058086

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132765479563) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132765479614) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766057989) |
| multimodal-gen-test-4-npu-a3 (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058048) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058069) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058084) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058108) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43698458050/job/132766058156) |


## [Run #43697766713](https://github.com/sgl-project/sglang/actions/runs/43697766713)
- **分支**: `pd-prefill-release-mm-features`
- **总耗时**: 13.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43697766713

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 5.3min | 环境问题 | multimodal 测试未生成 diffusion-failures 目录，疑似用例执行失败或产物缺失 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681224) |
| base-b-test-4-npu-a3 / run (0) | 9.8min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681294) |
| base-b-test-2-npu-a3 / run (0) | 5.5min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681308) |
| base-b-test-8-npu-a3 / run (0) | 6.2min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681312) |
| base-b-test-4-npu-a3 / run (1) | 5.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681316) |
| base-b-test-1-npu-a3 / run (0) | 5.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681337) |
| base-b-test-16-npu-a3 / run (0) | 5.4min | 环境问题 | 自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681346) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 upload-artifact 找不到 diffusion-failures/ 路径，说明测试未产出失败样本目录；结合退出码 5，可能是 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL）导致用例 error，需查看省略段中的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681224


- **base-b-test-2-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 200 OK），随后收到 SIGTERM 优雅退出，紧接着报错“Executing the custom container implementation failed”，属 self-hosted runner 容器实现故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681308


- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，说明 k8s runner 无法启动指定容器镜像，属 runner/容器环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681316

- **base-b-test-1-npu-a3 / run (0)**: 日志显示服务已正常启动并返回 200，随后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681337

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed”，属自托管 runner 容器环境问题；此前仅有 falcon_mamba 导入告警（被忽略），非用例失败根因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681346

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762092367) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762092378) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43697766713/job/132762681194) |


## [Run #43696996964](https://github.com/sgl-project/sglang/actions/runs/43696996964)
- **分支**: `lsyin/npu-multinode-sgl-router`
- **总耗时**: 70.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43696996964

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 59.5min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663321) |
| base-b-test-2-npu-a3 / run (0) | 61.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663341) |
| base-b-test-16-npu-a3 / run (0) | 61.3min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663344) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 报 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663357) |




- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例后 FAILED (errors=1)，退出码 1，导致 0/2 通过；错误发生在 setUpClass 阶段（如 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663357

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761032629) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761032632) |
| multimodal-gen-test-1-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663170) |
| multimodal-gen-test-1-npu-a3 (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663176) |
| multimodal-gen-test-4-npu-a3 (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663234) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663312) |
| base-b-test-4-npu-a3 / run (1) | 12.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663347) |
| multimodal-gen-test-4-npu-a3 (1) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996964/job/132761663377) |


## [Run #43696996490](https://github.com/sgl-project/sglang/actions/runs/43696996490)
- **分支**: `inkling-2-small-support`
- **总耗时**: 5.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43696996490

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-a-test-npu | 0.8min | 代码错误 | 测试文件缺少 __main__ 入口导致用例收集失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996490/job/132759759935) |

- **base-a-test-npu**: run_suite.py 收集用例时，ci_register.py 检测到 test_unified_mxfp8.py 缺少 `if __name__ == "__main__":` 入口，抛出 ValueError，进程退出码 1。需为该文件补充 unittest.main() 或 pytest.main 入口。
  链接: https://github.com/sgl-project/sglang/actions/runs/43696996490/job/132759759935

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996490/job/132759759986) |
| sgl-router-build-aarch64 / Build sgl-router | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696996490/job/132759796101) |


## [Run #43696206407](https://github.com/sgl-project/sglang/actions/runs/43696206407)
- **分支**: `inkling2-port-renderers`
- **总耗时**: 126.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43696206407

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 105.2min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069826) |
| base-b-test-1-npu-a3 / run (0) | 113.8min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069898) |

- **base-b-test-2-npu-a3 / run (0)**: 容器镜像中未安装 pkg-config，openssl-sys 编译时找不到该工具，cargo 构建 sglang-router wheel 失败（exit 101），pip 安装中断，作业退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069826


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132758476795) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132758476796) |
| sgl-router-build-aarch64 / Build sgl-router | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132758521631) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069781) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069793) |
| multimodal-gen-test-4-npu-a3 (0) | 29.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069794) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069803) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069856) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759069875) |
| base-b-test-4-npu-a3 / run (1) | 10.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759625373) |
| base-b-test-4-npu-a3 / run (0) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43696206407/job/132759625396) |


## [Run #43695978100](https://github.com/sgl-project/sglang/actions/runs/43695978100)
- **分支**: `lfm3`
- **总耗时**: 154.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43695978100

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 123.2min | 环境问题 | pip 安装 sglang-router 构建依赖时无法获取 setuptools，导致构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987183) |
| base-b-test-4-npu-a3 / run (0) | 151.1min | 环境问题 | pip 安装 triton-ascend 依赖 psutil==6.0.0 时找不到匹配版本，依赖安装失败导致作业退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987189) |

- **base-b-test-16-npu-a3 / run (0)**: 安装 sglang-router 时 pip 在隔离构建环境中找不到 setuptools>=45（from versions: none），疑似代理/镜像源不可用或网络受限，构建依赖安装失败，进程退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987183

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 ERROR: Could not find a version that satisfies the requirement psutil==6.0.0 (from triton-ascend)，from versions: none，随后进程以 exit code 1 结束。属于依赖源/环境配置问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987189

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756562865) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756562886) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756986976) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987002) |
| base-b-test-8-npu-a3 / run (0) | 7.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987097) |
| base-b-test-2-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987128) |
| base-b-test-1-npu-a3 / run (0) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987150) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43695978100/job/132756987166) |


## [Run #43693961888](https://github.com/sgl-project/sglang/actions/runs/43693961888)
- **分支**: `feat/ling3-pub-parser`
- **总耗时**: 152.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43693961888

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 147.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986667) |
| base-b-test-4-npu-a3 / run (0) | 8.4min | 代码错误 | NPU DP attention 测试用例执行失败，23个测试中1个error，脚本退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986726) |


- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行228秒后 FAILED (errors=1)，2个用例0通过，进程退出码1导致作业失败。需查看该用例 Traceback 确认是 setUpClass 中 server 启动失败还是用例本身断言错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986726

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750410733) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750410785) |
| multimodal-gen-test-4-npu-a3 (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986635) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986655) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986684) |
| base-b-test-1-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986701) |
| base-b-test-4-npu-a3 / run (1) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986715) |
| base-b-test-16-npu-a3 / run (0) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43693961888/job/132750986722) |


## [Run #43692622100](https://github.com/sgl-project/sglang/actions/runs/43692622100)
- **分支**: `inkling2-port-renderers`
- **总耗时**: 51.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43692622100

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 4.2min | 环境问题 | GitHub Actions 下载 action 时网络超时及 503 错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920384) |
| base-b-test-8-npu-a3 / run (0) | 41.2min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920398) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920418) |
| base-b-test-4-npu-a3 / run (0) | 8.8min | 代码错误 | NPU DP attention 测试脚本运行失败，23个用例中1个报错，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132747519600) |

- **base-b-test-1-npu-a3 / run (0)**: Runner 通过代理访问 codeload.github.com 下载 actions/github-script 时多次返回 503 Service Unavailable，重试 3 次后失败，作业在准备阶段即中止，未进入测试执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920384



- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行289秒后 FAILED (errors=1)，脚本返回退出码1，导致该文件判定失败，测试汇总0/2通过。日志未显示具体 Traceback，需查看该用例 setUpClass 阶段 server 启动或断言错误详情。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132747519600

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746424572) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746424603) |
| sgl-router-build-aarch64 / Build sgl-router | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746466861) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920268) |
| multimodal-gen-test-1-npu-a3 (1) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920274) |
| multimodal-gen-test-4-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920280) |
| multimodal-gen-test-1-npu-a3 (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920292) |
| base-b-test-2-npu-a3 / run (0) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132746920343) |
| base-b-test-4-npu-a3 / run (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43692622100/job/132747519598) |


## [Run #43691763295](https://github.com/sgl-project/sglang/actions/runs/43691763295)
- **分支**: `usage-zero-reasoning-tokens`
- **总耗时**: 37.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43691763295

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 24.9min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691763295/job/132744263447) |
| base-b-test-4-npu-a3 / run (0) | 27.8min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691763295/job/132744863397) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691763295/job/132743797296) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691763295/job/132743797339) |
| sgl-router-build-aarch64 / Build sgl-router | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691763295/job/132743840322) |
| base-b-test-4-npu-a3 / run (1) | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691763295/job/132744863369) |


## [Run #43691617584](https://github.com/sgl-project/sglang/actions/runs/43691617584)
- **分支**: `lsyin/npu-multinode-sgl-router`
- **总耗时**: 75.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43691617584

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 62.9min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993719) |
| base-b-test-4-npu-a3 / run (0) | 69.2min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993757) |
| base-b-test-4-npu-a3 / run (1) | 70.2min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993777) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743373981) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743374061) |
| multimodal-gen-test-1-npu-a3 (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993615) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993629) |
| multimodal-gen-test-4-npu-a3 (0) | 30.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993663) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993677) |
| base-b-test-1-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993717) |
| base-b-test-16-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993718) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691617584/job/132743993750) |


## [Run #43691592070](https://github.com/sgl-project/sglang/actions/runs/43691592070)
- **分支**: `inkling2-port-renderers`
- **总耗时**: 14.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43691592070

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 11.2min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719699) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719700) |
| multimodal-gen-test-1-npu-a3 (1) | 11.2min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719702) |
| multimodal-gen-test-4-npu-a3 (0) | 10.7min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719735) |
| base-b-test-16-npu-a3 / run (0) | 7.4min | 环境问题 | 自托管 runner 执行自定义容器失败，torch-npu 安装过程中容器异常退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719764) |
| base-b-test-2-npu-a3 / run (0) | 11.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719784) |
| base-b-test-1-npu-a3 / run (0) | 11.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719802) |
| base-b-test-4-npu-a3 / run (0) | 9.7min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 出现 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719840) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719699

- **multimodal-gen-test-4-npu-a3 (1)**: 日志末尾显示未找到diffusion-failures/目录，无产物上传；结合退出码5，最可能是setUpClass中sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719700

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示用例执行后无 diffusion-failures 产物，退出码5表示 unittest 存在 errors，最常见为 setUpClass 时 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体异常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719702

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719735

- **base-b-test-16-npu-a3 / run (0)**: 日志显示在安装 torch-npu 包时出现 'Executing the custom container implementation failed'，属于自托管 runner 容器环境故障，非用例代码问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719764

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明 k8s runner 无法启动/执行指定容器镜像，属 runner 环境或容器运行时问题，非用例代码失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719784

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例或代码本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719802

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个测试，FAILED (errors=1)，退出码 1，导致 0/2 通过。错误可能发生在 setUpClass 阶段（如 server 启动失败），需查看日志中的 Traceback 确认具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719840

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743289725) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743289829) |
| base-b-test-4-npu-a3 / run (1) | 9.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719871) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691592070/job/132743719958) |


## [Run #43691057907](https://github.com/sgl-project/sglang/actions/runs/43691057907)
- **分支**: `fix/encoder-embedding-prefix-reuse`
- **总耗时**: 190.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43691057907

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 171.1min | 环境问题 | Git 拉取代码超时，作业在 checkout 阶段失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293064) |

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 git fetch 从 git-cdn-service 拉取耗时约31分钟（10:18至10:49），随后 checkout 完成但作业随即清理退出，未进入测试阶段；属基础设施/网络超时，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293064

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132741707491) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132741707500) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742292846) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742292857) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742292866) |
| multimodal-gen-test-4-npu-a3 (0) | 28.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742292881) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293041) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293047) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293063) |
| base-b-test-4-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293109) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43691057907/job/132742293243) |


## [Run #43690323117](https://github.com/sgl-project/sglang/actions/runs/43690323117)
- **分支**: `feat/ling3-pub-parser`
- **总耗时**: 22.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43690323117

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 6.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043897) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043940) |
| base-b-test-1-npu-a3 / run (0) | 6.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043951) |
| base-b-test-4-npu-a3 / run (1) | 6.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043975) |





### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132739509725) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132739509766) |
| multimodal-gen-test-4-npu-a3 (1) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043785) |
| multimodal-gen-test-4-npu-a3 (0) | 4.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043822) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043890) |
| base-b-test-16-npu-a3 / run (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43690323117/job/132740043913) |


## [Run #43687728145](https://github.com/sgl-project/sglang/actions/runs/43687728145)
- **分支**: `rockdu-dev-mm-v2/06-sglang-wrapper`
- **总耗时**: 31.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43687728145

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 27.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082562) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082562

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132731704090) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132731704129) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082420) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082461) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082504) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082511) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082543) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082572) |
| base-b-test-4-npu-a3 / run (0) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687728145/job/132732082605) |


## [Run #43687325521](https://github.com/sgl-project/sglang/actions/runs/43687325521)
- **分支**: `kimi31-dflash2-ragged-verify`
- **总耗时**: 22.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43687325521

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 14.1min | 环境问题 | 依赖下载超时导致作业失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037473) |

- **base-b-test-16-npu-a3 / run (0)**: pip 从 pypi.org 拉取 scipy 等包时多次重试仍超时（operation timed out），退出码 1；同时 actions/checkout 下载曾遇 503，属网络/代理环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037473

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132730497865) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132730497877) |
| multimodal-gen-test-4-npu-a3 (0) | 4.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037400) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037413) |
| base-b-test-1-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037470) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037519) |
| base-b-test-2-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037527) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037548) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43687325521/job/132731037623) |


## [Run #43684197278](https://github.com/sgl-project/sglang/actions/runs/43684197278)
- **分支**: `kimi31-dflash2-ragged-verify`
- **总耗时**: 23.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43684197278

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 13.9min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588087) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588092) |

- **base-b-test-8-npu-a3 / run (0)**: pip 构建 sglang-router wheel 时，openssl-sys 需要 pkg-config 查找 OpenSSL，但环境中未安装 pkg-config，cargo rustc 编译失败（退出码 101），最终 wheel 构建失败、作业退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588087

- **base-b-test-16-npu-a3 / run (0)**: pip 构建 sglang-router wheel 时，openssl-sys 需要 pkg-config 查找 OpenSSL，但环境中未安装 pkg-config，cargo 编译失败（exit 101），最终 wheel 构建失败、作业退出码 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588092

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722134950) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722134980) |
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588078) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588105) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588114) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588116) |
| base-b-test-4-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588186) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43684197278/job/132722588190) |


## [Run #43683305183](https://github.com/sgl-project/sglang/actions/runs/43683305183)
- **分支**: `lsyin/rerun-test-npu-amd`
- **总耗时**: 5.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43683305183

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-a-test-npu | 2.1min | 其他 | 作业在运行第7个测试文件时被外部取消，并非测试失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43683305183/job/132718985461) |

- **base-a-test-npu**: 日志显示前6个测试文件均通过，第7个 test_npu_ascend_dsv4_backend.py 运行中收到 'The operation was canceled'，随后清理退出，无 Traceback 或断言失败，属作业被取消而非用例报错。
  链接: https://github.com/sgl-project/sglang/actions/runs/43683305183/job/132718985461

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43683305183/job/132718985478) |


## [Run #43682861025](https://github.com/sgl-project/sglang/actions/runs/43682861025)
- **分支**: `lsyin/rerun-test-npu-amd`
- **总耗时**: 9.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43682861025

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 0.7min | 环境问题 | 自托管 runner 的 k8s 容器执行失败，jobPod 未创建，作业未能启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634009) |
| multimodal-gen-test-1-npu-a3 (0) | 0.7min | 环境问题 | 自托管 runner 的 k8s 容器执行失败，jobPod 未创建，作业未能启动 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634011) |
| multimodal-gen-test-4-npu-a3 (0) | 0.7min | 环境问题 | 自托管 runner 的 k8s 容器执行失败，jobPod 未就绪导致作业无法运行 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634028) |
| multimodal-gen-test-4-npu-a3 (1) | 5.0min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634076) |
| base-b-test-16-npu-a3 / run (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634120) |
| base-b-test-8-npu-a3 / run (0) | 1.6min | 其他 | 作业在准备阶段被取消，日志无具体错误信息 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634123) |
| base-b-test-4-npu-a3 / run (1) | 1.2min | 环境问题 | 作业在 checkout 后执行 k8s 步骤时异常退出，未见测试用例运行。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634125) |
| base-b-test-2-npu-a3 / run (0) | 1.1min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634136) |
| base-b-test-1-npu-a3 / run (0) | 1.2min | 环境问题 | 作业在 checkout 后执行 k8s 索引脚本时异常退出，未进入测试阶段 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634147) |
| base-b-test-4-npu-a3 / run (0) | 0.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在下载 artifact 后中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634152) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示 custom container implementation failed，且 jobPod must be set，说明 prepareJob 阶段失败，容器/Pod 未成功创建，属于自托管 runner 基础设施问题，非用例本身错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634009

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示 'Executing the custom container implementation failed' 及 'jobPod must be set - ensure prepareJob completed successfully'，说明自托管 runner 的 k8s 插件在准备 Pod 阶段失败，测试脚本未真正执行，属基础设施/环境问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634011

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 'Executing the custom container implementation failed' 和 'jobPod must be set - ensure prepareJob completed successfully'，说明自托管 runner 的 k8s 容器准备阶段失败，pod 未创建成功，测试脚本未真正执行，属 runner 基础设施问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634028



- **base-b-test-8-npu-a3 / run (0)**: 日志仅显示获取 action 下载信息后出现 'The operation was canceled'，未执行到用例脚本，无 Traceback 或退出码，无法判定为用例失败，属作业被外部取消。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634123

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 checkout 完成后运行 /home/runner/k8s/index.js 即结束并清理孤儿进程，无 Traceback 或测试输出，疑似 runner/容器环境或 k8s 步骤异常导致作业提前终止，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634125


- **base-b-test-1-npu-a3 / run (0)**: 日志显示 checkout 完成后运行 /home/runner/k8s/index.js，仅出现 Node.js 弃用警告，随后即清理孤儿进程并结束，无测试输出与 Traceback，疑似 runner 环境/容器启动异常导致作业提前终止。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634147

- **base-b-test-4-npu-a3 / run (0)**: 日志报错 'Executing the custom container implementation failed'，属于 runner 容器环境异常，非用例代码问题；需联系自托管 runner 管理员排查容器启动。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717634152

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717114321) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682861025/job/132717114335) |


## [Run #43682180915](https://github.com/sgl-project/sglang/actions/runs/43682180915)
- **分支**: `feat/qwen4-exp-layernorm-sp`
- **总耗时**: 47.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43682180915

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 2.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132725156576) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718294815) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718294850) |
| multimodal-gen-test-4-npu-a3 (0) | 29.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786692) |
| multimodal-gen-test-4-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786718) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786735) |
| base-b-test-1-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786773) |
| multimodal-gen-test-1-npu-a3 (0) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786781) |
| base-b-test-4-npu-a3 / run (1) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786807) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786818) |
| base-b-test-16-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786825) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786826) |
| base-b-test-2-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132718786856) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132725156542) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682180915/job/132725156569) |


## [Run #43682170289](https://github.com/sgl-project/sglang/actions/runs/43682170289)
- **分支**: `mick/tp2-peer-partial-epilogue`
- **总耗时**: 31.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43682170289

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 10.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503916) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715022679) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715022685) |
| multimodal-gen-test-1-npu-a3 (0) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503838) |
| multimodal-gen-test-1-npu-a3 (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503847) |
| multimodal-gen-test-4-npu-a3 (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503879) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503907) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503920) |
| base-b-test-16-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503935) |
| multimodal-gen-test-4-npu-a3 (1) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503954) |
| base-b-test-4-npu-a3 / run (1) | 28.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503960) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682170289/job/132715503982) |


## [Run #43682036509](https://github.com/sgl-project/sglang/actions/runs/43682036509)
- **分支**: `lsyin/auth-levels-parity`
- **总耗时**: 22.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43682036509

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 16.1min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在下载 artifact 后中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132715589168) |

- **base-b-test-4-npu-a3 / run (1)**: 日志显示下载 sgl-router artifact 后报错 'Executing the custom container implementation failed'，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132715589168

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132714627505) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132714627545) |
| sgl-router-build-aarch64 / Build sgl-router | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132714663645) |
| base-b-test-2-npu-a3 / run (0) | 9.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132715163042) |
| base-b-test-1-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132715163051) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43682036509/job/132715589251) |


## [Run #43681790474](https://github.com/sgl-project/sglang/actions/runs/43681790474)
- **分支**: `lsyin/npu-multinode-sgl-router`
- **总耗时**: 47.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43681790474

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 44.3min | 代码错误 | NPU PD分离测试用例执行失败，返回退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493536) |
| base-b-test-4-npu-a3 / run (0) | 29.3min | 代码错误 | NPU DP attention 测试用例执行失败，23个测试中1个error，脚本退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493573) |
| base-b-test-16-npu-a3 / run (0) | 14.7min | 环境问题 | pip 安装 uv 失败，找不到可用版本，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493585) |

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行112秒后 FAILED (errors=1)，0/2通过，退出码1。日志省略了具体Traceback，需查看setUpClass阶段server启动是否失败（如OOM/SIGKILL）。
  - 失败用例: [code=1], [code=1], npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493536

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行258秒后 FAILED (errors=1)，2个用例0通过，进程退出码1导致作业失败。需查看该用例具体 Traceback 定位是 server 启动失败还是断言错误。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493573

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 pip 升级正常，但随后报错 'Could not find a version that satisfies the requirement uv (from versions: none)'，即包索引中无 uv 可用版本，属依赖源/网络环境问题，非用例代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493585

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132713990014) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132713990104) |
| multimodal-gen-test-4-npu-a3 (1) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493480) |
| multimodal-gen-test-1-npu-a3 (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493503) |
| multimodal-gen-test-1-npu-a3 (1) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493507) |
| multimodal-gen-test-4-npu-a3 (0) | 27.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493510) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493550) |
| base-b-test-8-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493569) |
| base-b-test-2-npu-a3 / run (0) | 34.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681790474/job/132714493601) |


## [Run #43681315776](https://github.com/sgl-project/sglang/actions/runs/43681315776)
- **分支**: `lsyin/rerun-test-npu-amd`
- **总耗时**: 20.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43681315776

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 14.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035556) |
| multimodal-gen-test-4-npu-a3 (0) | 13.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035557) |
| multimodal-gen-test-1-npu-a3 (0) | 14.5min | 环境问题 | 测试脚本退出码5，unittest 出现 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035563) |
| multimodal-gen-test-1-npu-a3 (1) | 14.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035566) |
| base-b-test-2-npu-a3 / run (0) | 13.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035573) |
| base-b-test-8-npu-a3 / run (0) | 13.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035600) |
| base-b-test-4-npu-a3 / run (0) | 14.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035615) |
| base-b-test-16-npu-a3 / run (0) | 6.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035616) |
| base-b-test-4-npu-a3 / run (1) | 15.7min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在下载 artifact 后中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035630) |
| base-b-test-1-npu-a3 / run (0) | 8.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035637) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；结合退出码5，最可能是setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035556

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表示unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035557

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示用例执行后退出码5（unittest errors），且未生成 diffusion-failures 目录产物；结合背景知识，最可能是 setUpClass 中 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认具体错误。
  - 失败用例: wan2_1_t2v_1.3b_1_npu, wan2_1_t2v_1.3b_1_npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035563

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约14分钟后结束。退出码5表明unittest存在errors，最常见为setUpClass时server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035566

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境故障，并非用例代码或精度问题；此前下载 action 时还出现过 503 重试。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035573

- **base-b-test-8-npu-a3 / run (0)**: 日志显示模型加载正常后出现 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035600

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 NPU 推理仍在正常输出（Prefill/Decode batch 持续打印），随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器基础设施异常，非用例断言失败或代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035615


- **base-b-test-4-npu-a3 / run (1)**: 日志显示下载 sgl-router artifact 后报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132713035630


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132712456487) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43681315776/job/132712456496) |


## [Run #43677030516](https://github.com/sgl-project/sglang/actions/runs/43677030516)
- **分支**: `hwoo/delta-recipes-sglang`
- **总耗时**: 31.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43677030516

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 8.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989010) |
| base-b-test-4-npu-a3 / run (0) | 8.1min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 报 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989014) |


- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例后 FAILED (errors=1)，退出码 1，导致 0/2 通过；错误发生在 setUpClass 阶段（如 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989014

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699449120) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699449125) |
| multimodal-gen-test-4-npu-a3 (0) | 28.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699988827) |
| multimodal-gen-test-1-npu-a3 (1) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699988863) |
| multimodal-gen-test-1-npu-a3 (0) | 12.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699988868) |
| multimodal-gen-test-4-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699988882) |
| base-b-test-1-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989005) |
| base-b-test-2-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989029) |
| base-b-test-8-npu-a3 / run (0) | 7.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989032) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43677030516/job/132699989223) |


## [Run #43676656385](https://github.com/sgl-project/sglang/actions/runs/43676656385)
- **分支**: `feat/mamba-gds-eviction-option`
- **总耗时**: 66.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43676656385

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 32.2min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132699475279) |
| base-b-test-4-npu-a3 / run (0) | 58.5min | 代码错误 | NPU DP attention 测试用例执行失败，23个测试中1个error导致退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132699475298) |

- **base-b-test-4-npu-a3 / run (1)**: 日志显示 openssl-sys 编译时找不到 pkg-config 工具，cargo rustc 构建 sglang-router wheel 失败（exit 101），最终 pip 安装失败、作业退出码 1。属于 CI 环境缺少依赖，非代码逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132699475279

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行250秒后 FAILED (errors=1)，2个用例0通过，进程退出码1，作业失败。需查看该用例 Traceback 定位具体错误（可能为 setUpClass 中 server 启动失败）。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132699475298

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698273703) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698273718) |
| sgl-router-build-aarch64 / Build sgl-router | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698315981) |
| multimodal-gen-test-4-npu-a3 (0) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683758) |
| multimodal-gen-test-4-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683765) |
| multimodal-gen-test-1-npu-a3 (1) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683784) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683798) |
| base-b-test-2-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683836) |
| base-b-test-16-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683869) |
| base-b-test-1-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683873) |
| base-b-test-8-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676656385/job/132698683887) |


## [Run #43676131862](https://github.com/sgl-project/sglang/actions/runs/43676131862)
- **分支**: `sm86-prefix-valid-gate`
- **总耗时**: 49.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43676131862

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.6min | 环境问题 | 容器内 aiohttp 版本与 Python 3.12 不兼容，导入时语法错误导致测试失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591491) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 11.2min | 环境问题 | 编译 sglang-router 时缺少 pkg-config，导致 OpenSSL 构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591513) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591532) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 aiohttp/helpers.py 第25行 `ensure_future = asyncio.async` 在 Python 3.12 下报 SyntaxError（asyncio.async 已移除），属镜像内依赖版本过旧的环境问题，非用例本身缺陷。
  链接: https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591491

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 构建 sglang-router wheel 时，openssl-sys 因找不到 pkg-config 工具而编译失败（cargo 退出码 101），pip 安装依赖阶段即中断，测试未执行。
  链接: https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132703591513


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132696688266) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132696688271) |
| base-b-test-2-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200412) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200416) |
| base-b-test-16-npu-a3 / run (0) | 27.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200428) |
| base-b-test-8-npu-a3 / run (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200433) |
| multimodal-gen-test-4-npu-a3 (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200440) |
| base-b-test-1-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200470) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200487) |
| base-b-test-4-npu-a3 / run (1) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43676131862/job/132697200528) |


## [Run #43675983084](https://github.com/sgl-project/sglang/actions/runs/43675983084)
- **分支**: `shuwen/hicache-host-covered-reason`
- **总耗时**: 87.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43675983084

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 78.4min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748930616) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-4-npu-a3 / run (0) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748930969) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748931553) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748931609) |
| base-b-test-4-npu-a3 / run (1) | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675983084/job/132748932903) |


## [Run #43675877358](https://github.com/sgl-project/sglang/actions/runs/43675877358)
- **分支**: `refactor/mem-cache-pool-base`
- **总耗时**: 39.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43675877358

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 35.6min | 环境问题 | 容器内 aiohttp 版本过旧，与 Python 3.12 不兼容导致语法错误 | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389877) |

- **base-b-test-4-npu-a3 / run (0)**: 导入 aiohttp 时 helpers.py 使用 asyncio.async（Python 3.7 已移除），在 Python 3.12 下报 SyntaxError，run_suite.py 启动即失败，退出码 1。属依赖环境版本不匹配，非用例问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389877

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132695889120) |
| Recommend tests from coverage | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132695889160) |
| multimodal-gen-test-1-npu-a3 (0) | 13.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389650) |
| multimodal-gen-test-1-npu-a3 (1) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389665) |
| multimodal-gen-test-4-npu-a3 (0) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389699) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389756) |
| base-b-test-2-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389765) |
| multimodal-gen-test-4-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389785) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389807) |
| base-b-test-16-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389838) |
| base-b-test-1-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43675877358/job/132696389902) |


## [Run #43671680250](https://github.com/sgl-project/sglang/actions/runs/43671680250)
- **分支**: `spec-batch1-host-loop`
- **总耗时**: 69.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43671680250

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132704766077) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697090723) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697090748) |
| multimodal-gen-test-4-npu-a3 (0) | 28.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649464) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649468) |
| multimodal-gen-test-1-npu-a3 (1) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649516) |
| base-b-test-8-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649546) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649551) |
| base-b-test-4-npu-a3 / run (1) | 31.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649589) |
| base-b-test-2-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649593) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649620) |
| base-b-test-1-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649626) |
| base-b-test-16-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132697649659) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132704766085) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43671680250/job/132704766099) |


## [Run #43670079359](https://github.com/sgl-project/sglang/actions/runs/43670079359)
- **分支**: `rockdu-dev-mm-v2/06-sglang-wrapper`
- **总耗时**: 49.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43670079359

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 15.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900895) |
| base-b-test-16-npu-a3 / run (0) | 29.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900913) |
| base-b-test-4-npu-a3 / run (0) | 11.9min | 环境问题 | pip 安装 uv 失败，找不到可用版本，导致作业退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678901038) |


- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900913

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 ERROR: Could not find a version that satisfies the requirement uv (from versions: none)，即 pip 源中无 uv 可用版本，属依赖源/网络环境问题，非用例本身错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678901038

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678345513) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678345655) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900792) |
| multimodal-gen-test-4-npu-a3 (1) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900825) |
| base-b-test-8-npu-a3 / run (0) | 7.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900912) |
| base-b-test-2-npu-a3 / run (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900923) |
| base-b-test-4-npu-a3 / run (1) | 44.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43670079359/job/132678900952) |


## [Run #43669962809](https://github.com/sgl-project/sglang/actions/runs/43669962809)
- **分支**: `fix/eagle3-rs-reduced-draft-vocab`
- **总耗时**: 50.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43669962809

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 5.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43669962809/job/132679271150) |
| base-b-test-1-npu-a3 / run (0) | 39.0min | 环境问题 | Runner 收到关闭信号，作业被取消，未进入实际测试执行。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43669962809/job/132679271207) |


- **base-b-test-1-npu-a3 / run (0)**: 日志显示 runner 在下载 action 信息后约 38 分钟收到 shutdown signal，操作被取消，属于 runner 服务停止或手动取消导致的环境/基础设施问题，非用例失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43669962809/job/132679271207

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43669962809/job/132678818040) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43669962809/job/132678818050) |
| base-b-test-4-npu-a3 / run (1) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43669962809/job/132679271187) |


## [Run #43668796010](https://github.com/sgl-project/sglang/actions/runs/43668796010)
- **分支**: `fix/eagle3-rs-reduced-draft-vocab`
- **总耗时**: 20.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43668796010

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 7.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675855252) |
| base-b-test-4-npu-a3 / run (0) | 7.2min | 环境问题 | 下载 GitHub Action 超时导致作业取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675855287) |
| base-b-test-4-npu-a3 / run (1) | 10.1min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675855303) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，runner 无法启动指定 CANN 镜像容器，测试尚未开始执行，属 CI 基础设施/环境问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675855252

- **base-b-test-4-npu-a3 / run (0)**: 下载 actions/download-artifact 时 HttpClient 超时 100 秒，重试后任务被取消，属网络/代理环境问题，非代码或测试失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675855287


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675261119) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43668796010/job/132675261172) |


## [Run #43668127214](https://github.com/sgl-project/sglang/actions/runs/43668127214)
- **分支**: `fix/eagle3-rs-reduced-draft-vocab`
- **总耗时**: 13.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43668127214

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 5.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43668127214/job/132672710622) |
| base-b-test-4-npu-a3 / run (0) | 9.1min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43668127214/job/132672710700) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示测试用例本身已通过（OK），随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43668127214/job/132672710622


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43668127214/job/132672081709) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43668127214/job/132672081715) |
| base-b-test-4-npu-a3 / run (1) | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43668127214/job/132672710690) |


## [Run #43660965189](https://github.com/sgl-project/sglang/actions/runs/43660965189)
- **分支**: `lsyin/rerun-test-npu-amd`
- **总耗时**: 31.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43660965189

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 12.2min | 环境问题 | pip 安装 aiohttp 构建依赖时无法找到 setuptools>=46.4.0，导致依赖安装失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774508) |
| base-b-test-4-npu-a3 / run (1) | 15.3min | 环境问题 | pip 安装 sglang-router 失败，找不到匹配版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774531) |
| base-b-test-16-npu-a3 / run (0) | 10.6min | 环境问题 | 依赖包 memfabric-hybrid==1.3.0 在镜像源中不存在，导致安装失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774535) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示安装 aiohttp 时构建依赖失败：ERROR: Could not find a version that satisfies the requirement setuptools>=46.4.0 (from versions: none)，即 pip 源不可用或代理/网络问题导致无法获取 setuptools，属于环境/依赖源问题，非代码错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774508

- **base-b-test-4-npu-a3 / run (1)**: 在容器内执行 pip 安装依赖时，报错 ERROR: Could not find a version that satisfies the requirement sglang-router (from versions: none)，即该包在配置的索引源中不可用，导致安装步骤退出码 1，作业失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774531

- **base-b-test-16-npu-a3 / run (0)**: pip 安装 memfabric-hybrid==1.3.0 时提示 No matching distribution found（可用版本为空），进程退出码 1，作业失败。属于镜像/依赖源环境问题，需检查该包是否已发布或源配置是否正确。
  链接: https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774535

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650242133) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650242191) |
| multimodal-gen-test-1-npu-a3 (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774427) |
| multimodal-gen-test-1-npu-a3 (1) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774435) |
| multimodal-gen-test-4-npu-a3 (1) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774455) |
| base-b-test-2-npu-a3 / run (0) | 20.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774467) |
| multimodal-gen-test-4-npu-a3 (0) | 27.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774507) |
| base-b-test-4-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774520) |
| base-b-test-8-npu-a3 / run (0) | 6.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660965189/job/132650774628) |


## [Run #43660235863](https://github.com/sgl-project/sglang/actions/runs/43660235863)
- **分支**: `codex/bounded-lpm-window`
- **总耗时**: 33.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43660235863

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 29.3min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405707) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405707

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132647827523) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132647827551) |
| multimodal-gen-test-4-npu-a3 (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405646) |
| base-b-test-1-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405726) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405758) |
| base-b-test-4-npu-a3 / run (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405780) |
| base-b-test-4-npu-a3 / run (0) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405783) |
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405787) |
| base-b-test-2-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43660235863/job/132648405873) |


## [Run #43651347487](https://github.com/sgl-project/sglang/actions/runs/43651347487)
- **分支**: `qkang/elastic-ep-mooncake-scale-down`
- **总耗时**: 38.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43651347487

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 18.4min | 环境问题 | pip 安装 uv 失败，找不到可用版本 | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676262391) |
| base-b-test-4-npu-a3 / run (1) | 9.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676262874) |

- **base-b-test-16-npu-a3 / run (0)**: 容器内 pip 升级后执行安装 uv 时，报错 Could not find a version that satisfies the requirement uv (from versions: none)，无匹配发行版，导致步骤退出码 1，作业失败。属依赖源/网络环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676262391


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-2-npu-a3 / run (0) | 36.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676262503) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263200) |
| multimodal-gen-test-4-npu-a3 (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263282) |
| multimodal-gen-test-4-npu-a3 (1) | 19.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263301) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263334) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263363) |
| multimodal-gen-test-1-npu-a3 (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263406) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263960) |
| base-b-test-4-npu-a3 / run (0) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676263976) |
| base-b-test-1-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43651347487/job/132676264116) |


## [Run #43650375358](https://github.com/sgl-project/sglang/actions/runs/43650375358)
- **分支**: `rainj-me/rust-apis-02-pause-and-frontend-state`
- **总耗时**: 52.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43650375358

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 36.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999120) |
| base-b-test-4-npu-a3 / run (0) | 39.2min | 代码错误 | test_npu_dp_attention.py 中 1 个用例报错，导致该文件退出码 1，整体 0/2 通过 | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999222) |

- **base-b-test-16-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_speculative_moe_a2a_backend.py, npu_speculative_moe_a2a_backend.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999120

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，test_npu_dp_attention.py 返回 exit code 1，Test Summary 0/2 passed。错误发生在用例执行阶段（可能为 setUpClass 中 server 启动失败），需查看该文件 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999222

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617370269) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617370307) |
| multimodal-gen-test-4-npu-a3 (1) | 12.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999077) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999098) |
| base-b-test-2-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999143) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999168) |
| base-b-test-1-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999186) |
| base-b-test-4-npu-a3 / run (1) | 47.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43650375358/job/132617999236) |


## [Run #43640378159](https://github.com/sgl-project/sglang/actions/runs/43640378159)
- **分支**: `rainj-me/rust-apis-02-pause-and-frontend-state`
- **总耗时**: 37.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43640378159

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 10.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587219874) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132586554502) |
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132586554682) |
| sgl-router-build-aarch64 / Build sgl-router | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132586616478) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587219787) |
| multimodal-gen-test-4-npu-a3 (1) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587219803) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587219883) |
| base-b-test-8-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587219896) |
| base-b-test-1-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587219906) |
| base-b-test-4-npu-a3 / run (0) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587995792) |
| base-b-test-4-npu-a3 / run (1) | 29.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43640378159/job/132587995837) |


## [Run #43636925061](https://github.com/sgl-project/sglang/actions/runs/43636925061)
- **分支**: `fix/swa-admission-retry-on-capacity-growth`
- **总耗时**: 23.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43636925061

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 6.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425947) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132575765372) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132575765381) |
| multimodal-gen-test-4-npu-a3 (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425871) |
| base-b-test-1-npu-a3 / run (0) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425894) |
| base-b-test-4-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425922) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425953) |
| base-b-test-4-npu-a3 / run (1) | 11.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425956) |
| multimodal-gen-test-4-npu-a3 (0) | 4.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576425965) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43636925061/job/132576426022) |


## [Run #43628789421](https://github.com/sgl-project/sglang/actions/runs/43628789421)
- **分支**: `feat/mamba-gds-eviction-option`
- **总耗时**: 36.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43628789421

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 4.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289850) |
| base-b-test-4-npu-a3 / run (0) | 7.7min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 出现 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289913) |


- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例后 FAILED (errors=1)，退出码 1，导致 0/2 通过。错误多因 setUpClass 阶段 sglang server 启动失败（如 OOM 或进程被 SIGKILL），需查看日志中 Traceback 确认具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289913

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132550673055) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132550673076) |
| multimodal-gen-test-1-npu-a3 (1) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289791) |
| multimodal-gen-test-4-npu-a3 (0) | 33.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289798) |
| multimodal-gen-test-1-npu-a3 (0) | 17.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289806) |
| multimodal-gen-test-4-npu-a3 (1) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289812) |
| base-b-test-2-npu-a3 / run (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289864) |
| base-b-test-8-npu-a3 / run (0) | 7.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289869) |
| base-b-test-4-npu-a3 / run (1) | 10.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289885) |
| base-b-test-1-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628789421/job/132551289912) |


## [Run #43628113274](https://github.com/sgl-project/sglang/actions/runs/43628113274)
- **分支**: `oss-sync-a012215732`
- **总耗时**: 17.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43628113274

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 2.2min | 环境问题 | 运行测试脚本时找不到 sglang 模块，导致导入失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132549157689) |

- **base-b-test-2-npu-a3 / run (0)**: test/run_suite.py 导入 sglang.test.ci.ci_register 时抛出 ModuleNotFoundError: No module named 'sglang'，说明容器内未正确安装或未设置 PYTHONPATH，属于环境/依赖配置问题，进程以退出码 1 结束。
  链接: https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132549157689

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132548567782) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132548567786) |
| base-b-test-4-npu-a3 / run (1) | 3.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132549157702) |
| base-b-test-4-npu-a3 / run (0) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43628113274/job/132549157714) |


## [Run #43614554379](https://github.com/sgl-project/sglang/actions/runs/43614554379)
- **分支**: `mori_epv2_asyncll_tbo`
- **总耗时**: 45.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43614554379

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 17.6min | 环境问题 | 编译 sglang-router 时缺少 pkg-config，导致 OpenSSL 构建失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680033237) |
| base-b-test-4-npu-a3 / run (0) | 44.3min | 代码错误 | NPU dp_attention 测试用例执行失败，23个测试中1个error，退出码1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680033973) |

- **base-b-test-8-npu-a3 / run (0)**: 构建 sglang-router 的 Rust 扩展时，openssl-sys 需要 pkg-config 来定位 OpenSSL，但容器内未安装该工具，cargo 编译失败（exit 101），wheel 构建失败，作业退出码为 1。
  链接: https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680033237

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行218秒后 FAILED (errors=1)，2个用例0通过。日志未显示具体Traceback，推测setUpClass阶段server启动异常或测试断言失败，需查看完整错误堆栈定位。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680033973

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034006) |
| multimodal-gen-test-4-npu-a3 (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034059) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034151) |
| base-b-test-1-npu-a3 / run (0) | 22.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034393) |
| base-b-test-16-npu-a3 / run (0) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034550) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034568) |
| base-b-test-2-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680034761) |
| base-b-test-4-npu-a3 / run (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43614554379/job/132680035470) |


## [Run #43608653616](https://github.com/sgl-project/sglang/actions/runs/43608653616)
- **分支**: `codex/bounded-lpm-window`
- **总耗时**: 21.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43608653616

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 9.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337607) |
| base-b-test-1-npu-a3 / run (0) | 4.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337673) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132524693300) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132524693400) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337371) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337415) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337576) |
| base-b-test-4-npu-a3 / run (0) | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337598) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337648) |
| base-b-test-8-npu-a3 / run (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43608653616/job/132525337651) |


## [Run #43602678499](https://github.com/sgl-project/sglang/actions/runs/43602678499)
- **分支**: `int8_lightening_indexer`
- **总耗时**: 10.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43602678499

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 10.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585281561) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585282407) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585283021) |
| multimodal-gen-test-1-npu-a3 (1) | 14.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585283202) |
| base-b-test-1-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585283343) |
| base-b-test-4-npu-a3 / run (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585317930) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585321519) |
| base-b-test-2-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585322877) |
| multimodal-gen-test-4-npu-a3 (1) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585323827) |
| base-b-test-4-npu-a3 / run (0) | 19.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585324042) |
| multimodal-gen-test-1-npu-a3 (0) | 13.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585326036) |
| multimodal-gen-test-4-npu-a3 (0) | 28.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43602678499/job/132585326370) |


## [Run #43264721540](https://github.com/sgl-project/sglang/actions/runs/43264721540)
- **分支**: `fix/dp-attention-abort-order`
- **总耗时**: 34.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43264721540

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 12.2min | 环境问题 | 构建 sglang-router 时缺少 pkg-config，导致 OpenSSL 编译失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395763) |

- **base-b-test-8-npu-a3 / run (0)**: 编译 openssl-sys 需要 pkg-config 但环境中未安装，cargo 构建 sglang-router wheel 失败（exit 101），pip 安装中止，作业退出码 1。属于 CI 环境依赖缺失，非代码逻辑错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395763

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132792756456) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132792756484) |
| multimodal-gen-test-4-npu-a3 (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395677) |
| multimodal-gen-test-4-npu-a3 (0) | 6.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395690) |
| base-b-test-16-npu-a3 / run (0) | 14.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395699) |
| base-b-test-1-npu-a3 / run (0) | 31.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395742) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395773) |
| base-b-test-4-npu-a3 / run (0) | 18.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395784) |
| base-b-test-2-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264721540/job/132793395791) |


## [Run #43264688614](https://github.com/sgl-project/sglang/actions/runs/43264688614)
- **分支**: `fix/prefill-delayer-deferring-dp-rank`
- **总耗时**: 40.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43264688614

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 9.4min | 代码错误 | test_npu_dp_attention.py 中 1 个用例报错，导致该文件退出码 1，测试失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091250) |
| base-b-test-2-npu-a3 / run (0) | 25.3min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091304) |

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，该文件返回 exit code 1，整体 0/2 通过。错误发生在用例执行阶段（可能为 setUpClass 中 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091250


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132775504941) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132775504998) |
| multimodal-gen-test-4-npu-a3 (1) | 12.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091190) |
| multimodal-gen-test-4-npu-a3 (0) | 5.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091204) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091232) |
| base-b-test-16-npu-a3 / run (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091322) |
| base-b-test-8-npu-a3 / run (0) | 7.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091327) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43264688614/job/132776091360) |


## [Run #43197020181](https://github.com/sgl-project/sglang/actions/runs/43197020181)
- **分支**: `stream-finished-output-before-cache-insert`
- **总耗时**: 23.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43197020181

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 13.1min | 代码错误 | NPU DP attention 测试用例执行失败，unittest 出现 1 个 error | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733948) |

- **base-b-test-4-npu-a3 / run (0)**: test_npu_dp_attention.py 运行 23 个用例，242 秒后 FAILED (errors=1)，退出码 1，2 个测试文件 0/2 通过。错误发生在用例执行阶段，需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733948

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697123316) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697123328) |
| multimodal-gen-test-4-npu-a3 (1) | 12.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733905) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733910) |
| base-b-test-16-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733924) |
| base-b-test-2-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733932) |
| base-b-test-8-npu-a3 / run (0) | 7.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733953) |
| base-b-test-1-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733961) |
| base-b-test-4-npu-a3 / run (1) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43197020181/job/132697733971) |


## [Run #43194202418](https://github.com/sgl-project/sglang/actions/runs/43194202418)
- **分支**: `dspark-greedy-verify-tail-glue`
- **总耗时**: 26.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43194202418

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 3.5min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599603) |
| base-b-test-4-npu-a3 / run (0) | 16.4min | 代码错误 | test_npu_dp_attention.py 中 23 个用例有 1 个 error，导致该文件退出码为 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599614) |


- **base-b-test-4-npu-a3 / run (0)**: 日志显示 Ran 23 tests，FAILED (errors=1)，该文件返回 exit code 1，最终 0/2 通过。错误发生在用例执行阶段（可能为 setUpClass 中 server 启动失败），需查看 Traceback 定位具体异常。
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599614

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697066144) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697066175) |
| multimodal-gen-test-4-npu-a3 (0) | 5.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599478) |
| multimodal-gen-test-4-npu-a3 (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599534) |
| base-b-test-2-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599572) |
| base-b-test-4-npu-a3 / run (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599587) |
| base-b-test-1-npu-a3 / run (0) | 19.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599624) |
| base-b-test-16-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194202418/job/132697599656) |


---
*Auto-generated by ci_monitor.py*