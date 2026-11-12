# NPU CI 执行监控（2026-11-12）
**生成时间**: 2026-11-13 07:18
**统计窗口**: 按 run **完成时间**（北京时间 2026-11-12 00:00 ~ 24:00），排队积压、晚完成的 run 归入其完成日的次日报告
**分析口径**: 成功 run 仅计数（不下载日志），失败 run 逐 job 下载日志并 AI 归因
**分析 Run 数**: 178

---

## 📊 本次执行总结

- **Job 执行情况**: 成功 1736 个 | 失败 125 个 | 成功 Job 平均耗时 15.6min
- **Run 执行情况**: 成功 119 个 | 失败 59 个 | 成功 Run 平均耗时 75.8min

### ✅ 耗时最长的成功 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| base-b-test-4-npu-a3 / run (0) | 71.1min | #43216743679 | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121501) |
| base-b-test-1-npu-a3 / run (0) | 56.0min | #43216743679 | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121851) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 52.6min | #43050091550 | [job link](https://github.com/sgl-project/sglang/actions/runs/43050091550/job/130642155743) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 52.5min | #43131365532 | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130906275476) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 51.7min | #43167158490 | [job link](https://github.com/sgl-project/sglang/actions/runs/43167158490/job/131106140309) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 50.4min | #43176212968 | [job link](https://github.com/sgl-project/sglang/actions/runs/43176212968/job/131060157613) |
| multimodal-gen-test-4-npu-a3 (0) | 49.5min | #43060177173 | [job link](https://github.com/sgl-project/sglang/actions/runs/43060177173/job/130662064694) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 48.8min | #43100836030 | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130879009230) |
| multimodal-gen-test-4-npu-a3 (0) | 48.2min | #43183337988 | [job link](https://github.com/sgl-project/sglang/actions/runs/43183337988/job/131065206465) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 46.9min | #43210641925 | [job link](https://github.com/sgl-project/sglang/actions/runs/43210641925/job/131170451938) |

### ❌ 耗时最长的失败 Job（Top 10）

| Job 名称 | 耗时 | 所属 Run | 链接 |
|----------|------|----------|------|
| multimodal-gen-test-4-npu-a3 (0) | 34.6min | #43204065076 | [job link](https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131135654694) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.5min | #43174413575 | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131047016923) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 30.7min | #43180820011 | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131136953943) |
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | #43148313013 | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309384) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.1min | #43076293355 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130751583982) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 25.1min | #43194371409 | [job link](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870011) |
| base-b-test-1-npu-a3 / run (0) | 24.9min | #42956151253 | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789742476) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.4min | #43152901748 | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130978206594) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 22.8min | #43178336816 | [job link](https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131160203524) |
| base-b-test-2-npu-a3 / run (0) | 22.7min | #43072056952 | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744876) |

---

## 📋 各任务执行统计

| 任务名称 | 执行次数 | 成功 | 执行失败 | 健康检查失败 | 取消 | 失败任务链接 |
|----------|----------|------|---------|-------------|------|-------------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 82 | 64 | 10 | 1 | 7 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131219438535)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870014)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131141069881)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131160203524)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131125387148) |
| base-b-test-1-npu-a3 / run (0) | 121 | 104 | 6 | 3 | 8 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782791)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688938)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562421)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253891) |
| base-b-test-2-npu-a3 / run (0) | 125 | 107 | 6 | 2 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121426)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076924)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333364)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815709)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296613) |
| base-b-test-4-npu-a3 / run (0) | 126 | 114 | 2 | 4 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815694)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043588) |
| base-b-test-4-npu-a3 / run (1) | 127 | 116 | 2 | 3 | 6 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538812)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395427) |
| base-b-test-16-npu-a3 / run (0) | 106 | 94 | 0 | 5 | 7 | - |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 86 | 71 | 5 | 0 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131274102100)<br>[job link 2](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131264647162)<br>[job link 3](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131085017791)<br>[job link 4](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131047016923)<br>[job link 5](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130934959851) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 72 | 64 | 1 | 2 | 5 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870011) |
| base-b-test-8-npu-a3 / run (0) | 105 | 97 | 0 | 2 | 6 | - |
| multimodal-gen-test-4-npu-a3 (0) | 134 | 123 | 1 | 0 | 10 | [job link 1](https://github.com/sgl-project/sglang/actions/runs/43239383335/job/131256622781) |

---

## 📋 各用例失败统计

> 注：成功 run 的日志不下载，用例“成功”数仅统计失败 run 中成功 job 的日志提取结果，实际成功率高于此表数值。

| 用例名称 | 执行次数 | 成功 | 失败 | 失败任务链接 |
|----------|----------|------|------|-------------|
| `npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py` | 9 | 2 | 7 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131219438535)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870014)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131069538877) |
| `npu_glm5_top64_pruned_bf16_8p_gsm8k.py` | 23 | 18 | 5 | [base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131274102100)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131264647162)<br>[base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131085017791) |
| `npu_return_indexer_topk_deepseek_v4.py` | 42 | 39 | 3 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333364)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296613)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427686) |
| `npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py` | 5 | 2 | 3 | [base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131141069881)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131160203524)<br>[base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131125387148) |
| `npu_dp_attention.py` | 45 | 43 | 2 | [base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815694)<br>[base-b-test-4-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043588) |
| `npu_autoround_moe.py` | 44 | 42 | 2 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688938)<br>[base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253891) |
| `npu_mla_fia_hicache_bf16.py` | 46 | 44 | 2 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121426)<br>[base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815709) |
| `minimax_h3_t2va_2npu` | 37 | 36 | 1 | [multimodal-gen-test-4-npu-a3 (0)](https://github.com/sgl-project/sglang/actions/runs/43239383335/job/131256622781) |
| `npu_hicache_mha.py` | 46 | 45 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782791) |
| `npu_autoround_dense.py` | 45 | 44 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562421) |
| `dspark_npu_dispatch.py` | 28 | 27 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789742476) |
| `npu_pd_disaggregation.py` | 47 | 46 | 1 | [base-b-test-4-npu-a3 / run (1)](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538812) |
| `npu_expert_distribution_recorder_mode.py` | 43 | 42 | 1 | [base-b-test-2-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076924) |
| `test_qwen38_packed_prefill_selection` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |
| `qwen3.8-flash-next-decode-b2-attn-tp4-cap65536` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |
| `qwen3.8-flash-next-verify-t4-attn-tp8-cap65536` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |
| `paged` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |
| `fia` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |
| `qsa_npu.py` | 1 | 0 | 1 | [base-b-test-1-npu-a3 / run (0)](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |
| `npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py` | 12 | 11 | 1 | [base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870011) |

---

### ⚠️ 失败的 CI Run

| Run ID | 分支 | 耗时 | 失败任务数 | 失败的任务 | 结论 | 链接 |
|--------|------|------|-----------|-----------|------|------|
| #43180820011<br>[#43852 [Feat] [NVIDIA] dsv4.1: [2/N] Add SM90 attention for packed FP4 Main KV.](https://github.com/sgl-project/sglang/pull/43852) | `feat/dsv41-packed-main-kv-sm90-attention` | 206.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43180820011) |
| #43180173784<br>[#50048 [Feat] [XPU] Qwen3.8-flash-next: Use native QSA, PLE and HyperConnection kernels](https://github.com/sgl-project/sglang/pull/50048) | `xpu-qsa-ple-hc-kernels` | 202.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43180173784) |
| #43178282479<br>[#47588 [Feat] sail: support DeepGEMM GEMM/MoE backends [4/N]](https://github.com/sgl-project/sglang/pull/47588) | `ywj/upstream_deepgemm_split` | 187.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43178282479) |
| #43180074481<br>[#48648 [Perf] [AMD] Qwen4-Exp/HC: Fuse decode-sized hyper-connection norm and inject into FlyDSL mix](https://github.com/sgl-project/sglang/pull/48648) | `perf/amd-qwen4-fused-hc-decode` | 153.9min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43180074481) |
| #43172317142<br>[#48047 [Perf] hicache: optional minimum tokens per write_back allocation-driven eviction](https://github.com/sgl-project/sglang/pull/48047) | `hicache-evict-headroom` | 150.8min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43172317142) |
| #43213808129<br>[#49886 [Feat] mem_cache: Checkpoint hybrid Mamba state only at fork points and request ends](https://github.com/sgl-project/sglang/pull/49886) | `feat/hybrid-cache-checkpoints-level` | 122.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43213808129) |
| #43131365532<br>[#42388 [Feat] gdn: Bit-exact tuple replay for linear-chain spec verify](https://github.com/sgl-project/sglang/pull/42388) | `lossless-gdn-tuple-verify` | 101.3min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43131365532) |
| #43100836030<br>[#49929 [Fix] [AMD] kimi-k3: Skip the CuTe DSL TGV tactic registration on ROCm](https://github.com/sgl-project/sglang/pull/49929) | `ci-fix/kimi-k3-hip-tgv-import` | 100.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43100836030) |
| #43181989882<br>[#49665 [Feat] dflash: Send the draft KV ring over PD disaggregation (Mooncake)](https://github.com/sgl-project/sglang/pull/49665) | `port/dflash-draft-kv-ring-pd` | 98.2min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43181989882) |
| #42988416101<br>[#47856 [Fix] [NPU] profiler: :bug: Fix patches and daemon trace parsing](https://github.com/sgl-project/sglang/pull/47856) | `junlin/diffusion-npu-profiler` | 96.3min | 1 | base-b-test-4-npu-a3 / run (1) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42988416101) |
| #43216743679<br>[#48996 [Perf] [AMD] dsa: Default the DSA KV cache to fp8_e4m3 on gfx950](https://github.com/sgl-project/sglang/pull/48996) | `main` | 94.1min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43216743679) |
| #43076293355<br>[#42388 [Feat] gdn: Bit-exact tuple replay for linear-chain spec verify](https://github.com/sgl-project/sglang/pull/42388) | `lossless-gdn-tuple-verify` | 93.5min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43076293355) |
| #43174413575<br>[#45180 [Feat] diffusion/minimax-h3: Add an online FP8 video VAE decoder](https://github.com/sgl-project/sglang/pull/45180) | `pr/minimax-h3-vae-fp8-decoder` | 93.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43174413575) |
| #43132799295<br>[#39741 [Fix] quantization: Determine Qwen3.5 GDN dense vs. GPTQ init from checkpoint precision and dynamic exclusions (#38854)](https://github.com/sgl-project/sglang/pull/39741) | `fix-qwen35-gdn-gptq-unquant-fallback` | 88.4min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43132799295) |
| #43182723806<br>[#49886 [Feat] mem_cache: Checkpoint hybrid Mamba state only at fork points and request ends](https://github.com/sgl-project/sglang/pull/49886) | `feat/hybrid-cache-checkpoints-level` | 88.2min | 6 | base-b-test-8-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43182723806) |
| #43122467079<br>[#47491 [Fix] [AMD] scheduler: Keep Muse Spark's scheduler GPU work on the forward stream under monokernel](https://github.com/sgl-project/sglang/pull/47491) | `fix/amd-monokernel-forward-stream` | 84.7min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43122467079) |
| #43074885269<br>[#44492 [Feat] [AMD] mori: Run MORI EPv2 dispatch/combine on AsyncLL kernels for TBO](https://github.com/sgl-project/sglang/pull/44492) | `mori_epv2_asyncll_tbo` | 82.7min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43074885269) |
| #43239620467<br>[#49886 [Feat] mem_cache: Checkpoint hybrid Mamba state only at fork points and request ends](https://github.com/sgl-project/sglang/pull/49886) | `feat/hybrid-cache-checkpoints-level` | 78.3min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43239620467) |
| #43140074772<br>[#47876 [Feat] mamba: Support strided destination conv-state pools in the conv-window scatter](https://github.com/sgl-project/sglang/pull/47876) | `xpu-conv-scatter-strided-dst` | 76.2min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43140074772) |
| #43071829299<br>[#49382 [Refactor] custom-ar-v2: Share one symmetric workspace per group](https://github.com/sgl-project/sglang/pull/49382) | `dark/carv2-symm-workspace` | 72.3min | 2 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3, base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43071829299) |
| #43132887909<br>[#49665 [Feat] dflash: Send the draft KV ring over PD disaggregation (Mooncake)](https://github.com/sgl-project/sglang/pull/49665) | `port/dflash-draft-kv-ring` | 69.2min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43132887909) |
| #43152901748<br>[#50034 [Doc] hybrid: Document hybrid cache checkpoint levels](https://github.com/sgl-project/sglang/pull/50034) | `feat/hybrid-cache-checkpoints-level` | 64.4min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43152901748) |
| #43195327213<br>[#49886 [Feat] mem_cache: Checkpoint hybrid Mamba state only at fork points and request ends](https://github.com/sgl-project/sglang/pull/49886) | `feat/hybrid-cache-checkpoints-level` | 59.7min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43195327213) |
| #43239383335<br>[#49353 [Perf] [NPU] MiniMax-H3: optimize RMSNorm and SwiGLU](https://github.com/sgl-project/sglang/pull/49353) | `minimax_npu_rmsnorm_path` | 57.4min | 1 | multimodal-gen-test-4-npu-a3 (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43239383335) |
| #43237210856<br>[#48600 [Feat] [Intel] HiCache: Support unified-memory HiCache on XPU](https://github.com/sgl-project/sglang/pull/48600) | `jeeja/unified_hicache_xpu` | 50.5min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43237210856) |
| #43202075378<br>[#47856 [Fix] [NPU] profiler: :bug: Fix patches and daemon trace parsing](https://github.com/sgl-project/sglang/pull/47856) | `junlin/diffusion-npu-profiler` | 49.3min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43202075378) |
| #43171430795<br>[#50005 [Feat] hisparse: Support Kimi-K3.1 DSA layers on PD decode with DFLASH](https://github.com/sgl-project/sglang/pull/50005) | `port-k31-hisparse` | 47.6min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43171430795) |
| #43171235134<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 46.6min | 2 | base-b-test-4-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43171235134) |
| #43159912245<br>[#50034 [Doc] hybrid: Document hybrid cache checkpoint levels](https://github.com/sgl-project/sglang/pull/50034) | `feat/hybrid-cache-checkpoints-level` | 46.6min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43159912245) |
| #43188224967 | `feat/qsa-cache-sharding` | 45.7min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43188224967) |
| #43207335661<br>[#49886 [Feat] mem_cache: Checkpoint hybrid Mamba state only at fork points and request ends](https://github.com/sgl-project/sglang/pull/49886) | `feat/hybrid-cache-checkpoints-level` | 45.5min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43207335661) |
| #43218629109<br>[#37570 [Feat] [NPU] Qwen3.8-Flash-Next: Support graph replay, MTP, and Triton kernels](https://github.com/sgl-project/sglang/pull/37570) | `pr-36601` | 45.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43218629109) |
| #43059035629<br>[#49665 [Feat] dflash: Send the draft KV ring over PD disaggregation (Mooncake)](https://github.com/sgl-project/sglang/pull/49665) | `port/dflash-draft-kv-ring` | 43.5min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43059035629) |
| #43120984399<br>[#49704 [Perf] [AMD] muse-spark: Prefill and decode optimization](https://github.com/sgl-project/sglang/pull/49704) | `pr/muse-spark-prefill-decode-opt` | 42.0min | 2 | base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3, base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43120984399) |
| #43140832814<br>[#49665 [Feat] dflash: Send the draft KV ring over PD disaggregation (Mooncake)](https://github.com/sgl-project/sglang/pull/49665) | `port/dflash-draft-kv-ring` | 40.6min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43140832814) |
| #43204065076<br>[#49706 [CI] diffusion: run MiniMax-H3-Image T2I and edit in the B200 suite](https://github.com/sgl-project/sglang/pull/49706) | `ci/h3-image-b200-e2e` | 38.0min | 1 | multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43204065076) |
| #43083251976 | `dark/carv2-symm-workspace` | 37.1min | 2 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3, base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43083251976) |
| #43170129057<br>[#47221 [Perf] dsa: Elide shared-layer index-K under HiSparse decode to raise batch size](https://github.com/sgl-project/sglang/pull/47221) | `feature/dsa-index-k-elision-hisparse-decode` | 36.3min | 1 | base-b-test-2-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43170129057) |
| #43063816422<br>[#44329 [Fix] [NPU] diffusion: Clean up warnings](https://github.com/sgl-project/sglang/pull/44329) | `clearing_console_output` | 35.8min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43063816422) |
| #43127916981<br>[#49955 [Feat] [AMD] custom-all-reduce: Add a ring all-reduce and an unrolled 2shot_push on MI450](https://github.com/sgl-project/sglang/pull/49955) | `users/wenkaidu/carv2-2shot-push-gfx1250` | 35.1min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43127916981) |
| #43148313013<br>[#47879 [Refactor] [NPU] dsv4: consume registered sgl-kernel-npu Transformer APIs](https://github.com/sgl-project/sglang/pull/47879) | `refactor/dsv4-cann-transformer-kernels` | 33.6min | 1 | multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43148313013) |
| #43177025846<br>[#44769 [Feat] [Intel] lora: Add intel_xpu LoRA backend](https://github.com/sgl-project/sglang/pull/44769) | `dev/srujan/lora_backend` | 33.0min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43177025846) |
| #43150967318<br>[#50005 [Feat] hisparse: Support Kimi-K3.1 DSA layers on PD decode with DFLASH](https://github.com/sgl-project/sglang/pull/50005) | `port-k31-hisparse` | 31.6min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43150967318) |
| #43194371409<br>[#49790 [NPU] adapt Qwen3.8-27B-w8a8 mtp.fc quantazition](https://github.com/sgl-project/sglang/pull/49790) | `qwen38_quant` | 31.4min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43194371409) |
| #43178336816<br>[#50007 [Fix] qwen-vl: Bound GPU memory of image preprocessing (fixes #49796)](https://github.com/sgl-project/sglang/pull/50007) | `fix/qwen-vl-preprocess-oom` | 27.3min | 1 | base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43178336816) |
| #43072056952<br>[#49686 [Feat] disaggregation: Make the PD top-logprobs metadata width configurable](https://github.com/sgl-project/sglang/pull/49686) | `pd-max-top-logprobs-num` | 26.6min | 2 | base-b-test-1-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43072056952) |
| #43078422719<br>[#49686 [Feat] disaggregation: Make the PD top-logprobs metadata width configurable](https://github.com/sgl-project/sglang/pull/49686) | `pd-max-top-logprobs-num` | 26.4min | 1 | base-b-test-4-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/43078422719) |
| #42956151253<br>[#49189 [Refactor] cleanup: Prune dead code and env vars, fix silent failures found by the code-cleanup skill](https://github.com/sgl-project/sglang/pull/49189) | `bbuf/cleanup-round3` | 25.5min | 1 | base-b-test-1-npu-a3 / run (0) | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42956151253) |
| #43231306849 | `qwen38_quant` | 20.6min | 2 | base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3, base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43231306849) |
| #43179766926<br>[#49665 [Feat] dflash: Send the draft KV ring over PD disaggregation (Mooncake)](https://github.com/sgl-project/sglang/pull/49665) | `port/dflash-draft-kv-ring-pd` | 17.1min | 4 | multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43179766926) |
| #43208319295<br>[#46091 [Feat] usage: align prompt and cache accounting across APIs](https://github.com/sgl-project/sglang/pull/46091) | `wuyaole/feat-measured-cache-writes` | 14.0min | 5 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1), multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43208319295) |
| #43076277606<br>[#49686 [Feat] disaggregation: Make the PD top-logprobs metadata width configurable](https://github.com/sgl-project/sglang/pull/49686) | `pd-max-top-logprobs-num` | 13.8min | 6 | multimodal-gen-test-4-npu-a3 (1), base-b-test-2-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-4-npu-a3 / run (1), base-b-test-1-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43076277606) |
| #42994850535 | `qwen38_quant` | 12.7min | 0 |  | failure | [run link](https://github.com/sgl-project/sglang/actions/runs/42994850535) |
| #42906299425<br>[#45137 [Feat] [NPU] Diffusion: Add HiDream-O1-Image support (DEV, DEV-2604, and FULL TI2I)](https://github.com/sgl-project/sglang/pull/45137) | `hidream` | 11.6min | 4 | multimodal-gen-test-1-npu-a3 (0), multimodal-gen-test-1-npu-a3 (1), multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/42906299425) |
| #43101930886<br>[#46186 [Perf] spec: radix top-k for speculative verify target probabilities](https://github.com/sgl-project/sglang/pull/46186) | `codex/av-3` | 11.0min | 1 | base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43101930886) |
| #43211545023<br>[#50096 [Feat] [NPU] attention: Support FP8 KV for DSA prefill context parallelism](https://github.com/sgl-project/sglang/pull/50096) | `npu-dsa-fp8-pcp` | 9.9min | 4 | multimodal-gen-test-4-npu-a3 (1), base-b-test-1-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-16-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43211545023) |
| #43106567752<br>[#39380 [Feat] xgrammar: Support Lark grammars and bump to 0.2.9](https://github.com/sgl-project/sglang/pull/39380) | `feat/xgrammar-lark-support` | 8.8min | 7 | multimodal-gen-test-4-npu-a3 (1), base-b-test-4-npu-a3 / run (1), base-b-test-16-npu-a3 / run (0), base-b-test-1-npu-a3 / run (0), base-b-test-4-npu-a3 / run (0), base-b-test-8-npu-a3 / run (0), base-b-test-2-npu-a3 / run (0) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43106567752) |
| #43136017491<br>[#49481 [Feat] [NPU] prefill: breakable prefill graph for DSV4 and ascend_ops MoE](https://github.com/sgl-project/sglang/pull/49481) | `prefill_graph_ascend_ops_on_main` | 7.5min | 3 | multimodal-gen-test-4-npu-a3 (0), base-b-test-2-npu-a3 / run (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43136017491) |
| #43133960153<br>[#49675 [Doc] diffusion: Fix feature guides that disagree with the code](https://github.com/sgl-project/sglang/pull/49675) | `doc/diffusion-guides` | 6.3min | 2 | multimodal-gen-test-4-npu-a3 (0), multimodal-gen-test-4-npu-a3 (1) | cancelled | [run link](https://github.com/sgl-project/sglang/actions/runs/43133960153) |

---


## [Run #43242668212](https://github.com/sgl-project/sglang/actions/runs/43242668212)
- **分支**: `pr/gdn-conv-flydsl`
- **总耗时**: 9.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43242668212

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 6.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43242668212/job/131268757600) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 6.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43242668212/job/131268757623) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43242668212/job/131267303204) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43242668212/job/131267303249) |


## [Run #43239620467](https://github.com/sgl-project/sglang/actions/runs/43239620467)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 78.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43239620467

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 8.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131274102100) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131274102100

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131256462272) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131256462317) |
| multimodal-gen-test-4-npu-a3 (0) | 34.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258004526) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258004631) |
| base-b-test-4-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258004808) |
| base-b-test-16-npu-a3 / run (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258004811) |
| base-b-test-1-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258004866) |
| base-b-test-8-npu-a3 / run (0) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258005008) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258005067) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258005127) |
| multimodal-gen-test-4-npu-a3 (1) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258005287) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131258005359) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131274101796) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239620467/job/131274102085) |


## [Run #43239383335](https://github.com/sgl-project/sglang/actions/runs/43239383335)
- **分支**: `minimax_npu_rmsnorm_path`
- **总耗时**: 57.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43239383335

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 13.7min | 环境问题 | 日志中未见明确错误，但上传了 diffusion-failures 工件，推测测试用例失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43239383335/job/131256622781) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，仅见工件上传成功及 Node.js 弃用警告，无 Traceback。结合退出码 5 与 diffusion-failures 工件，推测 setUpClass 阶段 server 启动失败（如 OOM/SIGKILL），需查看完整日志确认。
  - 失败用例: minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu, minimax_h3_t2va_2npu
  链接: https://github.com/sgl-project/sglang/actions/runs/43239383335/job/131256622781

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239383335/job/131255596850) |
| multimodal-gen-test-4-npu-a3 (1) | 6.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43239383335/job/131256622835) |


## [Run #43237210856](https://github.com/sgl-project/sglang/actions/runs/43237210856)
- **分支**: `jeeja/unified_hicache_xpu`
- **总耗时**: 50.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43237210856

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 18.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131264647162) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131264647162

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131247905631) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131247905635) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249338643) |
| multimodal-gen-test-4-npu-a3 (1) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249338842) |
| multimodal-gen-test-4-npu-a3 (0) | 35.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249338977) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339087) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339140) |
| base-b-test-16-npu-a3 / run (0) | 12.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339146) |
| base-b-test-1-npu-a3 / run (0) | 24.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339167) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339279) |
| multimodal-gen-test-1-npu-a3 (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339299) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131249339352) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131264647040) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43237210856/job/131264647243) |


## [Run #43231306849](https://github.com/sgl-project/sglang/actions/runs/43231306849)
- **分支**: `qwen38_quant`
- **总耗时**: 20.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43231306849

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.8min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43231306849/job/131228322984) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 17.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43231306849/job/131228323037) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，非用例本身失败；此前 decode 性能日志正常，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43231306849/job/131228322984

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 的容器运行时故障，并非用例断言失败；此前 server 推理正常，随后容器异常退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/43231306849/job/131228323037

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43231306849/job/131227251941) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43231306849/job/131227251994) |


## [Run #43218629109](https://github.com/sgl-project/sglang/actions/runs/43218629109)
- **分支**: `pr-36601`
- **总耗时**: 45.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43218629109

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 21.8min | 代码错误 | test_qsa_npu.py 用例执行失败导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/attention/qsa/test_qsa_npu.py 的 passed 为 false（耗时16秒），其余用例均通过，该用例失败使进程以退出码1结束，具体报错需查看该用例日志。
  - 失败用例: test_qwen38_packed_prefill_selection, qwen3.8-flash-next-decode-b2-attn-tp4-cap65536, qwen3.8-flash-next-verify-t4-attn-tp8-cap65536, paged, fia
  链接: https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544285

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131184411428) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131184411587) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185543736) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185543778) |
| base-b-test-16-npu-a3 / run (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544010) |
| base-b-test-2-npu-a3 / run (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544048) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544074) |
| base-b-test-4-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544132) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43218629109/job/131185544157) |


## [Run #43216743679](https://github.com/sgl-project/sglang/actions/runs/43216743679)
- **分支**: `main`
- **总耗时**: 94.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43216743679

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 7.7min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121426) |

- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121426

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131178000441) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121148) |
| multimodal-gen-test-4-npu-a3 (0) | 33.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121165) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121380) |
| base-b-test-16-npu-a3 / run (0) | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121455) |
| base-b-test-4-npu-a3 / run (0) | 71.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121501) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121742) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121804) |
| base-b-test-1-npu-a3 / run (0) | 56.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179121851) |
| base-b-test-8-npu-a3 / run (0) | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43216743679/job/131179122152) |


## [Run #43213808129](https://github.com/sgl-project/sglang/actions/runs/43213808129)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 122.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43213808129

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.5min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 执行失败，退出码为 1，3 个用例全部未通过。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131219438535) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: base-c-test-perf-2-npu-a3 套件中，qwen3_6_35b_a3b 的 1p in64k/out1k/prefix90 性能用例运行约 559 秒后返回退出码 1，Test Summary 显示 0/3 passed；日志未给出具体 Traceback，需查看该用例详细输出以定位是性能不达标还是 server 启动异常。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131219438535

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131168123832) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131168123957) |
| multimodal-gen-test-1-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169253726) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169253816) |
| multimodal-gen-test-4-npu-a3 (0) | 32.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169253880) |
| multimodal-gen-test-4-npu-a3 (1) | 26.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169253956) |
| base-b-test-1-npu-a3 / run (0) | 25.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169253965) |
| base-b-test-4-npu-a3 / run (0) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169254082) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169254114) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169254197) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169254559) |
| base-b-test-2-npu-a3 / run (0) | 24.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131169255092) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131186448849) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131186449043) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131186449306) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43213808129/job/131219437724) |


## [Run #43211545023](https://github.com/sgl-project/sglang/actions/runs/43211545023)
- **分支**: `npu-dsa-fp8-pcp`
- **总耗时**: 9.9min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43211545023

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 7.0min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547611) |
| base-b-test-1-npu-a3 / run (0) | 1.0min | 环境问题 | 日志在 checkout 后即结束，未进入测试阶段，疑似 runner 或容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547719) |
| base-b-test-8-npu-a3 / run (0) | 2.5min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在依赖安装阶段中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547727) |
| base-b-test-2-npu-a3 / run (0) | 6.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547840) |
| base-b-test-4-npu-a3 / run (1) | 6.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547855) |
| base-b-test-16-npu-a3 / run (0) | 5.2min | 环境问题 | 自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547861) |
| multimodal-gen-test-4-npu-a3 (0) | 6.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547895) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例未正常产出结果；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547611

- **base-b-test-1-npu-a3 / run (0)**: 日志仅显示代码检出完成，随后执行 k8s 脚本并清理孤儿进程，无任何测试输出或 Traceback，未出现退出码 5 相关用例错误，判断为 runner/容器环境问题而非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547719

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 pip 卸载 numpy/scipy 等包后报错“Executing the custom container implementation failed”，属 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547727



- **base-b-test-16-npu-a3 / run (0)**: 日志显示各 TP 进程刚开始加载权重后即报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131164547861


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131163448210) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43211545023/job/131163448261) |


## [Run #43208319295](https://github.com/sgl-project/sglang/actions/runs/43208319295)
- **分支**: `wuyaole/feat-measured-cache-writes`
- **总耗时**: 14.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43208319295

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 6.8min | 环境问题 | diffusion 测试失败且未生成失败产物，疑似 server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325122) |
| multimodal-gen-test-4-npu-a3 (1) | 6.4min | 环境问题 | 日志中未见测试用例执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业失败原因需结合省略部分确认。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325138) |
| multimodal-gen-test-1-npu-a3 (0) | 6.0min | 环境问题 | multimodal-gen 测试作业失败，未生成 diffusion-failures 产物，疑似 setUpClass 阶段 server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325164) |
| multimodal-gen-test-1-npu-a3 (1) | 4.1min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325199) |
| base-b-test-4-npu-a3 / run (1) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325303) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325309) |
| base-b-test-2-npu-a3 / run (0) | 10.8min | 环境问题 | 自定义容器执行失败，疑似 runner 容器环境异常导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325312) |
| base-b-test-16-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325350) |
| base-b-test-1-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325459) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试用例在 setUpClass 阶段即失败（退出码 5 对应 unittest errors），最可能是 sglang server 启动失败（如 host OOM 或进程被 SIGKILL），需查看中间省略的 Traceback 确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325122

- **multimodal-gen-test-4-npu-a3 (1)**: 日志可见部分无 Traceback/RuntimeError，仅提示 diffusion-failures/ 路径无文件、artifact 未上传；失败点应在被省略的中间日志中，需查看完整日志确认是否为 server 启动失败或退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325138

- **multimodal-gen-test-1-npu-a3 (0)**: 日志被截断，未见真实 Traceback；仅显示 upload-artifact 未找到 diffusion-failures/ 目录，说明测试未正常产出失败样本，结合退出码 5 推断为 setUpClass 中 sglang server 启动失败（如 OOM/SIGKILL），属环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325164

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试未正常产出失败产物；退出码5对应unittest errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325199



- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 sglang server 初始化阶段（Init parallel 完成后），非用例断言失败，属自托管 runner 容器环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325312



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131149285848) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131149285856) |
| base-b-test-8-npu-a3 / run (0) | 8.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43208319295/job/131150325401) |


## [Run #43207335661](https://github.com/sgl-project/sglang/actions/runs/43207335661)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 45.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43207335661

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131162553223) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 10.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131162553272) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 server 已启动成功，随后报错 'Executing the custom container implementation failed'，属于 runner/容器基础设施问题，非用例或代码本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131162553223

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示服务端推理请求均返回 200，随后报错 'Executing the custom container implementation failed'，属于自托管 runner/容器环境故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131162553272

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131145930730) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131145932654) |
| multimodal-gen-test-1-npu-a3 (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162014) |
| multimodal-gen-test-4-npu-a3 (0) | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162164) |
| multimodal-gen-test-1-npu-a3 (1) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162195) |
| multimodal-gen-test-4-npu-a3 (1) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162206) |
| base-b-test-1-npu-a3 / run (0) | 25.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162319) |
| base-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162633) |
| base-b-test-8-npu-a3 / run (0) | 9.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162786) |
| base-b-test-16-npu-a3 / run (0) | 13.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162812) |
| base-b-test-4-npu-a3 / run (0) | 21.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147162838) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131147163045) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43207335661/job/131162553391) |


## [Run #43204065076](https://github.com/sgl-project/sglang/actions/runs/43204065076)
- **分支**: `ci/h3-image-b200-e2e`
- **总耗时**: 38.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43204065076

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 34.6min | 环境问题 | 测试脚本未产生 diffusion-failures 目录，且从 pod 复制 _temp 失败，疑似容器内测试进程异常退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131135654694) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示未找到 diffusion-failures/ 路径，无产物上传，并警告从 pod 复制 _temp 失败；结合退出码 5，可能是 setUpClass 中 sglang server 启动失败（如 OOM/SIGKILL），但日志省略了真实 Traceback，无法确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131135654694

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131134803072) |
| multimodal-gen-test-1-npu-a3 (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131135654750) |
| multimodal-gen-test-1-npu-a3 (1) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131135654752) |
| multimodal-gen-test-4-npu-a3 (1) | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43204065076/job/131135654759) |


## [Run #43202075378](https://github.com/sgl-project/sglang/actions/runs/43202075378)
- **分支**: `junlin/diffusion-npu-profiler`
- **总耗时**: 49.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43202075378

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-16-npu-a3 / run (0) | 6.2min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187621) |
| base-b-test-8-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187746) |
| base-b-test-4-npu-a3 / run (1) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187773) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187825) |
| base-b-test-2-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187919) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187922) |







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131127970347) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131127970654) |
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187554) |
| multimodal-gen-test-4-npu-a3 (1) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187567) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129187583) |
| multimodal-gen-test-4-npu-a3 (0) | 33.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43202075378/job/131129188183) |


## [Run #43196938292](https://github.com/sgl-project/sglang/actions/runs/43196938292)
- **分支**: `port/dflash-draft-kv-ring-pd`
- **总耗时**: 7.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43196938292

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111522656) |
| multimodal-gen-test-4-npu-a3 (1) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111522709) |
| multimodal-gen-test-1-npu-a3 (1) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111522847) |
| base-b-test-2-npu-a3 / run (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111522928) |
| base-b-test-4-npu-a3 / run (1) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111523018) |
| base-b-test-16-npu-a3 / run (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111523033) |
| base-b-test-4-npu-a3 / run (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111523168) |
| base-b-test-1-npu-a3 / run (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111523225) |
| base-b-test-8-npu-a3 / run (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111523228) |
| multimodal-gen-test-1-npu-a3 (0) | 4.6min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131111523715) |











### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131110414850) |
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43196938292/job/131110415285) |


## [Run #43195327213](https://github.com/sgl-project/sglang/actions/runs/43195327213)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 59.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43195327213

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 9.1min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076924) |
| base-b-test-16-npu-a3 / run (0) | 13.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076974) |
| base-b-test-4-npu-a3 / run (0) | 2.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106077015) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_expert_distribution_recorder_mode.py, npu_expert_distribution_recorder_mode.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076924



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131105047900) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131105047973) |
| multimodal-gen-test-4-npu-a3 (0) | 39.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076682) |
| multimodal-gen-test-4-npu-a3 (1) | 26.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076773) |
| multimodal-gen-test-1-npu-a3 (1) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076887) |
| base-b-test-1-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106076901) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106077047) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106077061) |
| multimodal-gen-test-1-npu-a3 (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43195327213/job/131106077206) |


## [Run #43194371409](https://github.com/sgl-project/sglang/actions/runs/43194371409)
- **分支**: `qwen38_quant`
- **总耗时**: 31.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43194371409

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 25.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870011) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 14.3min | 环境问题 | 性能测试用例执行失败，退出码1，疑似服务启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870014) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py, npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870011

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 运行608秒后退出码1，3个用例0通过。日志未显示具体Traceback，需查看用例内部错误确认是否为server启动失败或OOM。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131102870014

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131101619862) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43194371409/job/131101619950) |


## [Run #43189407893](https://github.com/sgl-project/sglang/actions/runs/43189407893)
- **分支**: `layernorm-sp-min-tokens`
- **总耗时**: 6.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43189407893

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860143) |
| multimodal-gen-test-4-npu-a3 (1) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860182) |
| base-b-test-8-npu-a3 / run (0) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860251) |
| base-b-test-2-npu-a3 / run (0) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860253) |
| base-b-test-1-npu-a3 / run (0) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860323) |
| base-b-test-16-npu-a3 / run (0) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860336) |
| base-b-test-4-npu-a3 / run (0) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860360) |
| base-b-test-4-npu-a3 / run (1) | 3.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131085860412) |









### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131084851017) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43189407893/job/131084851031) |


## [Run #43188224967](https://github.com/sgl-project/sglang/actions/runs/43188224967)
- **分支**: `feat/qsa-cache-sharding`
- **总耗时**: 45.7min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43188224967

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业在测试启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131159799664) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 5.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131159799715) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 NPU 进程初始化（HCCL_BUFFSIZE 设置）后，属于 runner/容器环境故障，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131159799664

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，说明容器运行时（k8s runner）无法启动指定镜像，属基础设施/环境问题，非用例代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131159799715

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131140575356) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131140575445) |
| multimodal-gen-test-1-npu-a3 (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621704) |
| multimodal-gen-test-4-npu-a3 (1) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621756) |
| multimodal-gen-test-4-npu-a3 (0) | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621807) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621864) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621908) |
| base-b-test-1-npu-a3 / run (0) | 25.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621986) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141621993) |
| base-b-test-4-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141622025) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141622118) |
| base-b-test-2-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131141622151) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43188224967/job/131159800190) |


## [Run #43182723806](https://github.com/sgl-project/sglang/actions/runs/43182723806)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 88.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43182723806

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-8-npu-a3 / run (0) | 9.3min | 其他 | 日志显示测试全部通过，作业实际未失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538766) |
| base-b-test-4-npu-a3 / run (1) | 8.1min | 代码错误 | NPU PD 分离测试用例执行失败，unittest 报错退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538812) |
| base-b-test-2-npu-a3 / run (0) | 10.9min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538834) |
| base-b-test-4-npu-a3 / run (0) | 12.9min | 环境问题 | 自托管 runner 的容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538900) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538907) |
| base-b-test-1-npu-a3 / run (0) | 12.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538987) |

- **base-b-test-8-npu-a3 / run (0)**: 日志中 Test Summary 为 1/1 passed，用例 test_npu_eplb_min_rebalancing_utilization_threshold.py 成功，耗时321秒，退出码正常，仅存在 Node.js 弃用警告，无失败错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538766

- **base-b-test-4-npu-a3 / run (1)**: test_npu_pd_disaggregation.py 运行 241 秒后 FAILED (errors=1)，2 个用例 0 通过，进程以退出码 1 结束，导致作业失败；具体错误需查看被省略的 Traceback，疑似 setUpClass 阶段 server 启动失败。
  - 失败用例: npu_pd_disaggregation.py, npu_pd_disaggregation.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538812

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型权重加载完成后报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator”，属于 runner 容器环境故障，并非用例或代码本身的问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538834

- **base-b-test-4-npu-a3 / run (0)**: 日志显示测试用例已通过（POST /generate 返回 200），随后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，并非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538900

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 DeepseekV3 权重加载完成后报错“Executing the custom container implementation failed”，属于自托管 runner 容器环境故障，并非用例或代码本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538907

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重分片加载完成后报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538987

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131062586051) |
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131062586178) |
| multimodal-gen-test-1-npu-a3 (0) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538550) |
| multimodal-gen-test-1-npu-a3 (1) | 17.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538603) |
| multimodal-gen-test-4-npu-a3 (1) | 36.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538674) |
| multimodal-gen-test-4-npu-a3 (0) | 32.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43182723806/job/131063538682) |


## [Run #43181989882](https://github.com/sgl-project/sglang/actions/runs/43181989882)
- **分支**: `port/dflash-draft-kv-ring-pd`
- **总耗时**: 98.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43181989882

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 19.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333364) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333364

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131060265226) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131060265549) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333054) |
| multimodal-gen-test-1-npu-a3 (0) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333098) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333172) |
| multimodal-gen-test-4-npu-a3 (0) | 32.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333183) |
| base-b-test-8-npu-a3 / run (0) | 9.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333318) |
| base-b-test-1-npu-a3 / run (0) | 24.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333322) |
| base-b-test-4-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333420) |
| base-b-test-16-npu-a3 / run (0) | 25.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333520) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43181989882/job/131061333592) |


## [Run #43180820011](https://github.com/sgl-project/sglang/actions/runs/43180820011)
- **分支**: `feat/dsv41-packed-main-kv-sm90-attention`
- **总耗时**: 206.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43180820011

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 30.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131136953943) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，非用例代码或性能回归；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131136953943

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131056261855) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131056261982) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057205747) |
| multimodal-gen-test-4-npu-a3 (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057205919) |
| base-b-test-16-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057205984) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057206033) |
| base-b-test-2-npu-a3 / run (0) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057206043) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057206093) |
| base-b-test-1-npu-a3 / run (0) | 23.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057206106) |
| base-b-test-4-npu-a3 / run (0) | 18.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131057206140) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131091630237) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131091630290) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131091630451) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180820011/job/131136953830) |


## [Run #43180173784](https://github.com/sgl-project/sglang/actions/runs/43180173784)
- **分支**: `xpu-qsa-ple-hc-kernels`
- **总耗时**: 202.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43180173784

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 22.4min | 环境问题 | 性能测试用例执行失败，退出码1，疑似服务启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131141069881) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: qwen3_6_27b 性能用例运行1102秒后返回退出码1，3个用例全部失败。日志省略部分未显示具体Traceback，需查看完整日志确认是server启动失败还是性能指标未达标。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131141069881

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131054795074) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131054795097) |
| multimodal-gen-test-1-npu-a3 (1) | 16.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055616874) |
| multimodal-gen-test-4-npu-a3 (0) | 30.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055616875) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055616981) |
| multimodal-gen-test-4-npu-a3 (1) | 19.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055616994) |
| base-b-test-16-npu-a3 / run (0) | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055617034) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055617046) |
| base-b-test-1-npu-a3 / run (0) | 25.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055617095) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055617150) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055617206) |
| base-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131055617329) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131089618738) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 43.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131089618766) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131089618771) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180173784/job/131141070030) |


## [Run #43180074481](https://github.com/sgl-project/sglang/actions/runs/43180074481)
- **分支**: `perf/amd-qwen4-fused-hc-decode`
- **总耗时**: 153.9min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43180074481

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 17.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131085017791) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131085017791

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131053827382) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131053827443) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055058809) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055058943) |
| multimodal-gen-test-4-npu-a3 (0) | 31.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055058973) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055058980) |
| base-b-test-2-npu-a3 / run (0) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055059030) |
| base-b-test-4-npu-a3 / run (1) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055059096) |
| multimodal-gen-test-1-npu-a3 (0) | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055059105) |
| base-b-test-16-npu-a3 / run (0) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055059113) |
| base-b-test-1-npu-a3 / run (0) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055059139) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131055059140) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131085017771) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43180074481/job/131085017799) |


## [Run #43179766926](https://github.com/sgl-project/sglang/actions/runs/43179766926)
- **分支**: `port/dflash-draft-kv-ring-pd`
- **总耗时**: 17.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43179766926

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (1) | 13.4min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861323) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861366) |
| multimodal-gen-test-4-npu-a3 (1) | 13.6min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861368) |
| multimodal-gen-test-4-npu-a3 (0) | 13.6min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861414) |
| base-b-test-1-npu-a3 / run (0) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861606) |
| base-b-test-8-npu-a3 / run (0) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861627) |
| base-b-test-16-npu-a3 / run (0) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861630) |
| base-b-test-4-npu-a3 / run (1) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861635) |
| base-b-test-2-npu-a3 / run (0) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861643) |
| base-b-test-4-npu-a3 / run (0) | 13.8min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861795) |

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示作业以退出码5结束（unittest errors），且未生成 diffusion-failures/ 目录产物，说明用例在 setUpClass 阶段即失败，最可能是 sglang server 启动失败（如 host OOM 或进程被 SIGKILL）。日志中段被省略，未见具体 Traceback，需查看完整日志确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861323

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约13分钟后结束，退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861366

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact；作业约13分钟结束，退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861368

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示作业约13分钟后结束，未上传diffusion-failures/产物，说明测试用例执行阶段出错。退出码5表示unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131053861414







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131052801078) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43179766926/job/131052801562) |


## [Run #43178336816](https://github.com/sgl-project/sglang/actions/runs/43178336816)
- **分支**: `fix/qwen-vl-preprocess-oom`
- **总耗时**: 27.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43178336816

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 22.8min | 其他 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 执行失败，退出码 1 | [job link](https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131160203524) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 该性能用例运行约 1114 秒后返回退出码 1，测试汇总 0/1 通过。日志省略了具体 Traceback，无法确定是性能不达标、server 启动失败还是超时，需查看完整日志中的真实错误。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131160203524

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131159010455) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178336816/job/131159010475) |


## [Run #43178282479](https://github.com/sgl-project/sglang/actions/runs/43178282479)
- **分支**: `ywj/upstream_deepgemm_split`
- **总耗时**: 187.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43178282479

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 21.8min | 其他 | 性能测试用例 test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py 返回退出码 1，3 个用例全部失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131125387148) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本运行约 1068 秒后以 exit code 1 失败，Test Summary 为 0/3 passed，但省略部分未给出具体 Traceback，无法确定是 server 启动失败、性能不达标还是超时，需查看完整日志定位。
  - 失败用例: npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py, npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131125387148

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131047989609) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131047989793) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819189) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819192) |
| multimodal-gen-test-1-npu-a3 (1) | 17.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819238) |
| multimodal-gen-test-4-npu-a3 (0) | 31.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819355) |
| base-b-test-16-npu-a3 / run (0) | 30.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819368) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819437) |
| base-b-test-1-npu-a3 / run (0) | 27.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819523) |
| base-b-test-4-npu-a3 / run (0) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819566) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819618) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131048819672) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131083270833) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 36.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131083270861) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131083270928) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43178282479/job/131125387240) |


## [Run #43177167159](https://github.com/sgl-project/sglang/actions/runs/43177167159)
- **分支**: `port-k31-hisparse`
- **总耗时**: 76.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43177167159

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 28.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131064403468) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 28.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131064403481) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 28.9min | 排队取消 | job 未执行任何步骤（steps=0），排队/等待后随 run 取消 | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131064403548) |




### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131044355372) |
| base-a-test-npu | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131044355410) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059063) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059097) |
| base-b-test-16-npu-a3 / run (0) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059156) |
| base-b-test-4-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059245) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059276) |
| base-b-test-2-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059308) |
| base-b-test-1-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059343) |
| base-b-test-4-npu-a3 / run (1) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177167159/job/131045059381) |


## [Run #43177025846](https://github.com/sgl-project/sglang/actions/runs/43177025846)
- **分支**: `dev/srujan/lora_backend`
- **总耗时**: 33.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43177025846

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 6.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782791) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_hicache_mha.py, npu_hicache_mha.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782791

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131043820785) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131043820804) |
| base-b-test-4-npu-a3 / run (0) | 10.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782739) |
| base-b-test-4-npu-a3 / run (1) | 7.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782785) |
| base-b-test-2-npu-a3 / run (0) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43177025846/job/131044782942) |


## [Run #43174413575](https://github.com/sgl-project/sglang/actions/runs/43174413575)
- **分支**: `pr/minimax-h3-vae-fp8-decoder`
- **总耗时**: 93.0min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43174413575

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 33.5min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131047016923) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131047016923

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131035251851) |
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131035251958) |
| multimodal-gen-test-1-npu-a3 (0) | 14.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036303968) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036303976) |
| multimodal-gen-test-4-npu-a3 (0) | 31.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036303980) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304019) |
| base-b-test-2-npu-a3 / run (0) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304249) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304272) |
| base-b-test-16-npu-a3 / run (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304342) |
| base-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304362) |
| base-b-test-4-npu-a3 / run (1) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304368) |
| base-b-test-1-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131036304502) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131047017012) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43174413575/job/131047017092) |


## [Run #43172317142](https://github.com/sgl-project/sglang/actions/runs/43172317142)
- **分支**: `hicache-evict-headroom`
- **总耗时**: 150.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43172317142

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.2min | 环境问题 | 性能测试用例执行失败，退出码1，疑似服务启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131069538877) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 9.6min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131069539035) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 运行约566秒后返回退出码1，3个用例全部失败。日志未显示具体Traceback，需查看完整日志确认是否为server启动失败或OOM。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131069538877


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131028458290) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131028458606) |
| multimodal-gen-test-1-npu-a3 (0) | 13.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292643) |
| multimodal-gen-test-4-npu-a3 (1) | 20.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292689) |
| multimodal-gen-test-4-npu-a3 (0) | 30.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292690) |
| multimodal-gen-test-1-npu-a3 (1) | 16.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292729) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292799) |
| base-b-test-1-npu-a3 / run (0) | 25.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292802) |
| base-b-test-16-npu-a3 / run (0) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292807) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292834) |
| base-b-test-4-npu-a3 / run (1) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029292856) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131029293045) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 41.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131040184866) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131040184978) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43172317142/job/131040185098) |


## [Run #43171430795](https://github.com/sgl-project/sglang/actions/runs/43171430795)
- **分支**: `port-k31-hisparse`
- **总耗时**: 47.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43171430795

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 14.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131036857169) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 14.2min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131036857187) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试运行中（decode batch 正常输出）后报错 'Executing the custom container implementation failed'，属 runner/容器基础设施故障，非用例本身失败；建议联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131036857169

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示测试请求均返回 200，随后报错 'Executing the custom container implementation failed'，属 runner 容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131036857187

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131025555743) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131025555781) |
| multimodal-gen-test-4-npu-a3 (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338512) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338529) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338571) |
| base-b-test-4-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338601) |
| base-b-test-4-npu-a3 / run (1) | 10.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338629) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338691) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338715) |
| base-b-test-1-npu-a3 / run (0) | 23.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131026338723) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 5.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171430795/job/131036857197) |


## [Run #43171235134](https://github.com/sgl-project/sglang/actions/runs/43171235134)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 46.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43171235134

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 10.1min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815694) |
| base-b-test-16-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815706) |
| base-b-test-2-npu-a3 / run (0) | 6.9min | 环境问题 | sglang server 进程被 SIGKILL(-9)，通常为 host OOM 所致 | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815709) |

- **base-b-test-4-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815694


- **base-b-test-2-npu-a3 / run (0)**: 测试框架/fixture 检测到 server 进程异常终止（rc=-9，用例表现为 exit code 137），用例未真正执行即失败，属于环境/资源问题而非精度回归
  - 失败用例: npu_mla_fia_hicache_bf16.py, npu_mla_fia_hicache_bf16.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815709

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131024925780) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131024925787) |
| multimodal-gen-test-4-npu-a3 (1) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815517) |
| multimodal-gen-test-4-npu-a3 (0) | 42.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815548) |
| multimodal-gen-test-1-npu-a3 (0) | 24.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815621) |
| multimodal-gen-test-1-npu-a3 (1) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815625) |
| base-b-test-4-npu-a3 / run (1) | 11.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815713) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815722) |
| base-b-test-8-npu-a3 / run (0) | 7.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43171235134/job/131025815739) |


## [Run #43170129057](https://github.com/sgl-project/sglang/actions/runs/43170129057)
- **分支**: `feature/dsa-index-k-elision-hisparse-decode`
- **总耗时**: 36.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43170129057

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 18.9min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296613) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296613

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131021366962) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131021367032) |
| multimodal-gen-test-1-npu-a3 (0) | 15.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296389) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296483) |
| multimodal-gen-test-4-npu-a3 (1) | 22.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296534) |
| base-b-test-4-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296618) |
| base-b-test-16-npu-a3 / run (0) | 16.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296634) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296635) |
| base-b-test-1-npu-a3 / run (0) | 27.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296639) |
| multimodal-gen-test-4-npu-a3 (0) | 32.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296680) |
| base-b-test-4-npu-a3 / run (1) | 12.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43170129057/job/131022296691) |


## [Run #43159912245](https://github.com/sgl-project/sglang/actions/runs/43159912245)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 46.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43159912245

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 15.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130999186375) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 15.8min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130999186443) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，服务端推理请求此前均返回 200，说明失败发生在容器运行时层面，而非用例或代码本身，属于 runner 环境问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130999186375

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例断言失败；此前推理仍在正常输出，随后作业被中断。
  链接: https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130999186443

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130988655329) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130988655471) |
| multimodal-gen-test-1-npu-a3 (0) | 15.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424163) |
| multimodal-gen-test-4-npu-a3 (0) | 32.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424195) |
| multimodal-gen-test-1-npu-a3 (1) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424225) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424235) |
| base-b-test-8-npu-a3 / run (0) | 9.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424253) |
| base-b-test-1-npu-a3 / run (0) | 24.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424317) |
| base-b-test-16-npu-a3 / run (0) | 14.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424334) |
| base-b-test-2-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424378) |
| base-b-test-4-npu-a3 / run (0) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424444) |
| base-b-test-4-npu-a3 / run (1) | 14.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130989424460) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43159912245/job/130999186366) |


## [Run #43152901748](https://github.com/sgl-project/sglang/actions/runs/43152901748)
- **分支**: `feat/hybrid-cache-checkpoints-level`
- **总耗时**: 64.4min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43152901748

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 24.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130978206594) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示测试正常进行中（chat/completions 返回 200），随后报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器基础设施故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130978206594

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130966192272) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130966192292) |
| multimodal-gen-test-1-npu-a3 (0) | 13.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111071) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111104) |
| multimodal-gen-test-4-npu-a3 (1) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111106) |
| multimodal-gen-test-4-npu-a3 (0) | 29.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111147) |
| base-b-test-16-npu-a3 / run (0) | 27.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111271) |
| base-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111279) |
| base-b-test-1-npu-a3 / run (0) | 24.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111285) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111302) |
| base-b-test-4-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111318) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130967111404) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130978206553) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43152901748/job/130978206625) |


## [Run #43150967318](https://github.com/sgl-project/sglang/actions/runs/43150967318)
- **分支**: `port-k31-hisparse`
- **总耗时**: 31.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43150967318

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 14.7min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688938) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688938

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130959878208) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130959878238) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688798) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688811) |
| base-b-test-4-npu-a3 / run (1) | 12.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688967) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960688979) |
| base-b-test-16-npu-a3 / run (0) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960689009) |
| base-b-test-2-npu-a3 / run (0) | 22.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960689011) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43150967318/job/130960689061) |


## [Run #43148313013](https://github.com/sgl-project/sglang/actions/runs/43148313013)
- **分支**: `refactor/dsv4-cann-transformer-kernels`
- **总耗时**: 33.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43148313013

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 30.0min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309384) |
| base-b-test-4-npu-a3 / run (1) | 0.7min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309497) |
| base-b-test-16-npu-a3 / run (0) | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309514) |
| base-b-test-2-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309518) |
| base-b-test-4-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309538) |
| base-b-test-8-npu-a3 / run (0) | 0.9min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309541) |
| base-b-test-1-npu-a3 / run (0) | 0.8min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309548) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业约30分钟后结束，退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309384







### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130951430794) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130951430800) |
| multimodal-gen-test-1-npu-a3 (1) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309326) |
| multimodal-gen-test-1-npu-a3 (0) | 15.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309415) |
| multimodal-gen-test-4-npu-a3 (1) | 18.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43148313013/job/130952309487) |


## [Run #43140832814](https://github.com/sgl-project/sglang/actions/runs/43140832814)
- **分支**: `port/dflash-draft-kv-ring`
- **总耗时**: 40.6min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43140832814

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-2-npu-a3 / run (0) | 21.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427686) |

- **base-b-test-2-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_return_indexer_topk_deepseek_v4.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427686

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130927390682) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130927390886) |
| multimodal-gen-test-1-npu-a3 (0) | 16.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427392) |
| multimodal-gen-test-4-npu-a3 (0) | 36.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427393) |
| multimodal-gen-test-1-npu-a3 (1) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427433) |
| multimodal-gen-test-4-npu-a3 (1) | 23.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427444) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427560) |
| base-b-test-1-npu-a3 / run (0) | 26.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427585) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427594) |
| base-b-test-16-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427677) |
| base-b-test-4-npu-a3 / run (0) | 20.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140832814/job/130928427701) |


## [Run #43140074772](https://github.com/sgl-project/sglang/actions/runs/43140074772)
- **分支**: `xpu-conv-scatter-strided-dst`
- **总耗时**: 76.2min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43140074772

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 16.3min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130934959851) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_glm5_top64_pruned_bf16_8p_gsm8k.py, npu_glm5_top64_pruned_bf16_8p_gsm8k.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130934959851

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130924835714) |
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130924835736) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130925572563) |
| base-b-test-4-npu-a3 / run (1) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130925572602) |
| base-b-test-4-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130925572609) |
| base-b-test-16-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130925572637) |
| base-b-test-8-npu-a3 / run (0) | 8.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130925572684) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130925572710) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 36.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130934959825) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43140074772/job/130934959910) |


## [Run #43136017491](https://github.com/sgl-project/sglang/actions/runs/43136017491)
- **分支**: `prefill_graph_ascend_ops_on_main`
- **总耗时**: 7.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43136017491

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 3.8min | 环境问题 | 作业在测试阶段失败，日志末尾显示未找到 diffusion-failures/ 目录，无产物上传，疑似测试脚本未正常产出或 setUpClass 阶段 server 启动失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130912493243) |
| base-b-test-2-npu-a3 / run (0) | 3.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动容器阶段即报错退出 | [job link](https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130912493355) |
| multimodal-gen-test-4-npu-a3 (1) | 4.1min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130912493359) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志被截断，未见明确 Traceback；仅见 upload-artifact 报 'No files were found with the provided path: diffusion-failures/'，说明测试未生成失败产物目录，可能 setUpClass 中 sglang server 启动失败（OOM/SIGKILL）导致用例 error 退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130912493243

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在 k8s 容器启动阶段，尚未进入用例执行，属 runner/容器环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130912493355

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示用例执行后退出码5（unittest errors），且未生成 diffusion-failures 目录产物，说明测试在 setUpClass 阶段即失败，常见原因为 host OOM 或 server 进程被 SIGKILL，属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130912493359

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130911606528) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43136017491/job/130911606693) |


## [Run #43133960153](https://github.com/sgl-project/sglang/actions/runs/43133960153)
- **分支**: `doc/diffusion-guides`
- **总耗时**: 6.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43133960153

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (0) | 4.0min | 环境问题 | 作业日志中未见测试执行错误，仅提示未找到 diffusion-failures/ 目录，无法上传产物。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43133960153/job/130918293397) |
| multimodal-gen-test-4-npu-a3 (1) | 3.2min | 环境问题 | 作业日志中未见测试执行错误，仅显示未找到 diffusion-failures/ 目录导致无产物上传，作业本身未报失败原因。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43133960153/job/130918293426) |

- **multimodal-gen-test-4-npu-a3 (0)**: 日志仅显示 'No files were found with the provided path: diffusion-failures/'，说明测试未产生失败产物目录，可能用例未实际运行或提前退出；日志被截断，缺少真实 Traceback，无法确认具体失败原因。
  链接: https://github.com/sgl-project/sglang/actions/runs/43133960153/job/130918293397

- **multimodal-gen-test-4-npu-a3 (1)**: 日志仅含 Node 弃用警告和 artifact 路径缺失提示，无 Traceback/RuntimeError，无法确认用例失败；需查看被省略的中间日志定位真实错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43133960153/job/130918293426

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43133960153/job/130917744451) |


## [Run #43132887909](https://github.com/sgl-project/sglang/actions/runs/43132887909)
- **分支**: `port/dflash-draft-kv-ring`
- **总耗时**: 69.2min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43132887909

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 5.6min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130924882376) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 5.5min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130924882461) |

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例本身代码或性能问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130924882376

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示模型分片加载到12%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，并非用例代码或性能回归问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130924882461

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130901269238) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130901269250) |
| multimodal-gen-test-1-npu-a3 (0) | 15.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040217) |
| multimodal-gen-test-1-npu-a3 (1) | 16.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040314) |
| multimodal-gen-test-4-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040396) |
| multimodal-gen-test-4-npu-a3 (0) | 34.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040403) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040516) |
| base-b-test-16-npu-a3 / run (0) | 13.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040573) |
| base-b-test-4-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040652) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040669) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040710) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130902040819) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 36.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130911087570) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130911087662) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132887909/job/130911087675) |


## [Run #43132799295](https://github.com/sgl-project/sglang/actions/runs/43132799295)
- **分支**: `fix-qwen35-gdn-gptq-unquant-fallback`
- **总耗时**: 88.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43132799295

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.5min | 其他 | 性能测试用例执行失败，退出码1，3个用例全部未通过 | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130931659486) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 运行566秒后返回退出码1，Test Summary 0/3 passed。日志未显示具体Traceback，需查看该用例详细输出定位是server启动失败还是性能指标不达标。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130931659486

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130905558490) |
| base-a-test-npu | 2.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130905558641) |
| multimodal-gen-test-1-npu-a3 (1) | 19.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906596883) |
| multimodal-gen-test-1-npu-a3 (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906596914) |
| multimodal-gen-test-4-npu-a3 (0) | 32.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906596937) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906596961) |
| multimodal-gen-test-4-npu-a3 (1) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906596978) |
| base-b-test-2-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906597008) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906597094) |
| base-b-test-4-npu-a3 / run (1) | 12.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906597104) |
| base-b-test-1-npu-a3 / run (0) | 25.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906597118) |
| base-b-test-16-npu-a3 / run (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130906597206) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130916402904) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130916402938) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 39.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130916402961) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 18.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43132799295/job/130931659348) |


## [Run #43131365532](https://github.com/sgl-project/sglang/actions/runs/43131365532)
- **分支**: `lossless-gdn-tuple-verify`
- **总耗时**: 101.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43131365532

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 22.4min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130925934246) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 22.4min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130925934394) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 'Executing the custom container implementation failed'，属于自托管 runner 容器环境异常，非用例本身失败；此前推理请求均返回 200，服务运行正常。
  链接: https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130925934246

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 perf 测试运行中报错“Executing the custom container implementation failed”，属 runner/容器环境故障，非用例本身失败；需联系自托管 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130925934394

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130896223733) |
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130896223786) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222276) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222371) |
| base-b-test-1-npu-a3 / run (0) | 22.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222539) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222623) |
| base-b-test-4-npu-a3 / run (1) | 13.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222693) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222722) |
| base-b-test-8-npu-a3 / run (0) | 8.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222743) |
| base-b-test-16-npu-a3 / run (0) | 21.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130897222746) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 52.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130906275476) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130906275478) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43131365532/job/130906275519) |


## [Run #43127916981](https://github.com/sgl-project/sglang/actions/runs/43127916981)
- **分支**: `users/wenkaidu/carv2-2shot-push-gfx1250`
- **总耗时**: 35.1min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43127916981

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 9.6min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562421) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_autoround_dense.py, npu_autoround_dense.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562421

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130893554806) |
| base-a-test-npu | 2.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130893554825) |
| multimodal-gen-test-1-npu-a3 (1) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562217) |
| multimodal-gen-test-4-npu-a3 (0) | 31.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562243) |
| multimodal-gen-test-1-npu-a3 (0) | 14.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562268) |
| multimodal-gen-test-4-npu-a3 (1) | 20.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562280) |
| base-b-test-2-npu-a3 / run (0) | 20.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562450) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562482) |
| base-b-test-8-npu-a3 / run (0) | 7.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562542) |
| base-b-test-16-npu-a3 / run (0) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562612) |
| base-b-test-4-npu-a3 / run (0) | 18.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43127916981/job/130894562675) |


## [Run #43122467079](https://github.com/sgl-project/sglang/actions/runs/43122467079)
- **分支**: `fix/amd-monokernel-forward-stream`
- **总耗时**: 84.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43122467079

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.6min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 返回退出码 1，3 个用例全部失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130891918240) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本运行约 575 秒后以 exit code 1 失败，Test Summary 为 0/3 passed，但省略部分未给出具体 Traceback，无法确定是性能回归、server 启动失败还是环境问题，需查看完整日志中的真实错误。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130891918240

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130866290548) |
| base-a-test-npu | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130866290578) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097401) |
| multimodal-gen-test-4-npu-a3 (1) | 11.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097709) |
| base-b-test-2-npu-a3 / run (0) | 22.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097710) |
| base-b-test-1-npu-a3 / run (0) | 22.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097745) |
| base-b-test-4-npu-a3 / run (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097759) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097777) |
| base-b-test-16-npu-a3 / run (0) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097818) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130867097840) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 35.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130877113948) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130877114030) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130877114062) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43122467079/job/130891917913) |


## [Run #43120984399](https://github.com/sgl-project/sglang/actions/runs/43120984399)
- **分支**: `pr/muse-spark-prefill-decode-opt`
- **总耗时**: 42.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43120984399

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 9.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130874092510) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.4min | 环境问题 | TokenizerManager 看门狗超时，容器执行失败，疑似服务进程卡死或被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130874092587) |

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示服务端推理请求均返回 200，随后报错 'Executing the custom container implementation failed'，属于 runner/容器基础设施故障，非用例或代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130874092510

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 TokenizerManager watchdog timeout（300s），随后报错“Executing the custom container implementation failed”，说明 sglang server 在 setUpClass 阶段无响应，可能因 host OOM 或进程被 SIGKILL 导致启动失败，属环境/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130874092587

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130861258258) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130861258390) |
| multimodal-gen-test-4-npu-a3 (1) | 21.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396754) |
| multimodal-gen-test-1-npu-a3 (0) | 15.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396760) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396783) |
| multimodal-gen-test-1-npu-a3 (1) | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396790) |
| base-b-test-16-npu-a3 / run (0) | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396834) |
| base-b-test-4-npu-a3 / run (0) | 19.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396959) |
| base-b-test-4-npu-a3 / run (1) | 14.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862396981) |
| base-b-test-2-npu-a3 / run (0) | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862397005) |
| base-b-test-1-npu-a3 / run (0) | 25.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862397012) |
| base-b-test-8-npu-a3 / run (0) | 8.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130862397218) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43120984399/job/130874092519) |


## [Run #43106567752](https://github.com/sgl-project/sglang/actions/runs/43106567752)
- **分支**: `feat/xgrammar-lark-support`
- **总耗时**: 8.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43106567752

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 5.7min | 环境问题 | 测试脚本退出码5，unittest 存在 errors，疑似 setUpClass 阶段 sglang server 启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477199) |
| base-b-test-4-npu-a3 / run (1) | 4.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477280) |
| base-b-test-16-npu-a3 / run (0) | 5.8min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477321) |
| base-b-test-1-npu-a3 / run (0) | 5.7min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477393) |
| base-b-test-4-npu-a3 / run (0) | 4.3min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在启动阶段即中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477468) |
| base-b-test-8-npu-a3 / run (0) | 4.7min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在容器启动阶段即报错终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477475) |
| base-b-test-2-npu-a3 / run (0) | 5.3min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477559) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示 diffusion-failures/ 目录无文件，未上传 artifact；作业以退出码5结束，符合 unittest errors（如 setUpClass 中 server 启动失败、host OOM 或进程被 SIGKILL）的特征，需查看中间省略的 Traceback 确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477199

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境故障，非用例代码问题；此前 server 已正常初始化，随后容器执行异常退出。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477280

- **base-b-test-16-npu-a3 / run (0)**: 日志末尾报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner 容器环境异常，并非用例代码或精度问题；NPU 进程启动后作业即被中止。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477321

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到75%时出现“Executing the custom container implementation failed”，属于 runner 容器环境异常，并非用例断言失败；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477393

- **base-b-test-4-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，容器启动失败，未进入用例执行阶段，属 runner/容器环境问题，非代码或精度问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477468

- **base-b-test-8-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，发生在容器镜像启动阶段，非用例代码问题，需联系 runner 管理员排查容器运行时/镜像拉取。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477475

- **base-b-test-2-npu-a3 / run (0)**: 日志显示模型分片加载到70%时出现 'Executing the custom container implementation failed'，属于 runner/容器环境故障，非用例代码问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477559

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130811518873) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130811518935) |
| multimodal-gen-test-4-npu-a3 (0) | 4.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43106567752/job/130812477044) |


## [Run #43101930886](https://github.com/sgl-project/sglang/actions/runs/43101930886)
- **分支**: `codex/av-3`
- **总耗时**: 11.0min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43101930886

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 7.2min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在加载模型分片过程中中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43101930886/job/130796947181) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示模型分片加载到47%时出现“Executing the custom container implementation failed”，属于自托管 runner/容器环境异常，非用例断言失败；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43101930886/job/130796947181

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43101930886/job/130795551264) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43101930886/job/130795551378) |


## [Run #43100836030](https://github.com/sgl-project/sglang/actions/runs/43100836030)
- **分支**: `ci-fix/kimi-k3-hip-tgv-import`
- **总耗时**: 100.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43100836030

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.6min | 其他 | 性能测试用例 test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py 返回退出码 1，3 个用例全部失败。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130898978896) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示该性能测试脚本运行约 586 秒后以 exit code 1 失败，Test Summary 为 0/3 passed，但省略部分未给出具体 Traceback，无法确定是精度/性能阈值不达标还是 server 启动异常，需查看完整日志定位。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130898978896

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130867748192) |
| base-a-test-npu | 2.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130867748248) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868839895) |
| multimodal-gen-test-4-npu-a3 (1) | 11.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868839968) |
| base-b-test-2-npu-a3 / run (0) | 23.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868840089) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868840103) |
| base-b-test-16-npu-a3 / run (0) | 19.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868840136) |
| base-b-test-1-npu-a3 / run (0) | 23.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868840140) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868840157) |
| base-b-test-4-npu-a3 / run (0) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130868840227) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 48.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130879009230) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130879009246) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 27.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130879009248) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 23.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43100836030/job/130898978855) |


## [Run #43083251976](https://github.com/sgl-project/sglang/actions/runs/43083251976)
- **分支**: `dark/carv2-symm-workspace`
- **总耗时**: 37.1min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43083251976

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 10.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130755182530) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 10.4min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130755182963) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志显示 evalscope 子进程刚启动后即报错“Executing the custom container implementation failed”，属于 runner/容器环境故障，非用例本身失败，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130755182530

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境故障，非用例代码或精度问题；此前服务请求均返回 200 OK。
  链接: https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130755182963

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130741324927) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130741325043) |
| multimodal-gen-test-1-npu-a3 (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361216) |
| multimodal-gen-test-1-npu-a3 (1) | 16.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361273) |
| multimodal-gen-test-4-npu-a3 (0) | 28.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361320) |
| multimodal-gen-test-4-npu-a3 (1) | 18.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361551) |
| base-b-test-16-npu-a3 / run (0) | 12.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361716) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361764) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361780) |
| base-b-test-2-npu-a3 / run (0) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361901) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742361944) |
| base-b-test-4-npu-a3 / run (0) | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130742362132) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43083251976/job/130755182484) |


## [Run #43078422719](https://github.com/sgl-project/sglang/actions/runs/43078422719)
- **分支**: `pd-max-top-logprobs-num`
- **总耗时**: 26.4min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43078422719

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (0) | 11.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043588) |

- **base-b-test-4-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_dp_attention.py, npu_dp_attention.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043588

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130724742162) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130724742174) |
| multimodal-gen-test-4-npu-a3 (0) | 5.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043425) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043521) |
| multimodal-gen-test-4-npu-a3 (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043552) |
| base-b-test-1-npu-a3 / run (0) | 23.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043564) |
| base-b-test-4-npu-a3 / run (1) | 11.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043568) |
| base-b-test-2-npu-a3 / run (0) | 20.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043598) |
| base-b-test-8-npu-a3 / run (0) | 8.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43078422719/job/130726043875) |


## [Run #43076293355](https://github.com/sgl-project/sglang/actions/runs/43076293355)
- **分支**: `lossless-gdn-tuple-verify`
- **总耗时**: 93.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43076293355

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 29.1min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业中止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130751583982) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码或性能回归问题，需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130751583982

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130717112507) |
| Recommend tests from coverage | 1.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130717112529) |
| multimodal-gen-test-4-npu-a3 (0) | 5.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718459710) |
| base-b-test-4-npu-a3 / run (0) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718459751) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718459758) |
| base-b-test-4-npu-a3 / run (1) | 10.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718459905) |
| base-b-test-1-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718459998) |
| base-b-test-2-npu-a3 / run (0) | 22.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718460109) |
| base-b-test-8-npu-a3 / run (0) | 8.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718460182) |
| base-b-test-16-npu-a3 / run (0) | 15.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130718460785) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 36.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130731607195) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130731607278) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130731607492) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076293355/job/130751583956) |


## [Run #43076277606](https://github.com/sgl-project/sglang/actions/runs/43076277606)
- **分支**: `pd-max-top-logprobs-num`
- **总耗时**: 13.8min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43076277606

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-4-npu-a3 (1) | 10.5min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256110) |
| base-b-test-2-npu-a3 / run (0) | 10.6min | 环境问题 | 自托管 runner 的自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256162) |
| base-b-test-4-npu-a3 / run (0) | 10.2min | 环境问题 | 自托管 runner 的容器执行失败，作业在模型分片加载中途被中断。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256196) |
| base-b-test-4-npu-a3 / run (1) | 10.4min | 环境问题 | 自托管 runner 执行自定义容器失败，作业在测试启动阶段被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256217) |
| base-b-test-1-npu-a3 / run (0) | 10.1min | 环境问题 | 自托管 runner 的容器执行失败，导致作业中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256267) |
| base-b-test-16-npu-a3 / run (0) | 10.6min | 环境问题 | Scheduler watchdog 超时，容器执行失败，疑似 host 资源不足导致 server 启动异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256271) |

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures/目录无文件，未上传artifact，说明测试用例执行异常。退出码5表示unittest存在errors，最常见为setUpClass阶段server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256110

- **base-b-test-2-npu-a3 / run (0)**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境故障，非用例代码问题；此前 sglang 初始化正常，无 Traceback。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256162

- **base-b-test-4-npu-a3 / run (0)**: 日志显示模型分片加载到43%时出现“Executing the custom container implementation failed”，属于 runner/容器环境异常，并非用例断言失败；需联系 runner 管理员排查容器运行时。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256196

- **base-b-test-4-npu-a3 / run (1)**: 日志末尾报错“Executing the custom container implementation failed”，属 runner/容器环境异常，非用例断言失败；此前仅有 torch_npu 警告，未见 Traceback 或退出码 5。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256217

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型权重加载到 0% 时出现“Executing the custom container implementation failed”，这是 runner 容器层面的错误，并非用例或代码问题，需联系 runner 管理员排查容器环境。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256267

- **base-b-test-16-npu-a3 / run (0)**: 日志显示 Scheduler watchdog timeout (soft=True)，随后报错 custom container implementation failed，多个 TP 进程权重加载耗时约 300s，疑似 host OOM 或进程被 SIGKILL 导致 server 启动失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256271

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130717244964) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130717245141) |
| multimodal-gen-test-4-npu-a3 (0) | 5.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256087) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43076277606/job/130718256186) |


## [Run #43074885269](https://github.com/sgl-project/sglang/actions/runs/43074885269)
- **分支**: `mori_epv2_asyncll_tbo`
- **总耗时**: 82.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43074885269

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 13.2min | 环境问题 | 性能测试用例执行失败，退出码1，疑似服务启动或运行异常 | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130856936272) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: base-c-test-perf-2-npu-a3 套件中 qwen3_6_35b_a3b 的 1p_in64k_out1k_prefix90_50ms 性能用例运行559秒后退出码1，3个用例全部失败；日志未显示具体 Traceback，需查看用例内部错误确认是否为 server 启动失败或 OOM。
  - 失败用例: npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py, npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130856936272

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-2-npu-a3 / run (0) | 21.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826944877) |
| base-a-test-npu | 2.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826946615) |
| base-b-test-1-npu-a3 / run (0) | 22.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826946982) |
| base-b-test-8-npu-a3 / run (0) | 8.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826947522) |
| base-b-test-4-npu-a3 / run (1) | 14.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826947973) |
| multimodal-gen-test-4-npu-a3 (1) | 11.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826948218) |
| base-b-test-16-npu-a3 / run (0) | 13.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826948292) |
| multimodal-gen-test-4-npu-a3 (0) | 4.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826948424) |
| base-b-test-4-npu-a3 / run (0) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130826948473) |
| Recommend tests from coverage | 1.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130827003317) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 17.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130838392870) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 40.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130838392912) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130838393009) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 17.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43074885269/job/130856936371) |


## [Run #43072056952](https://github.com/sgl-project/sglang/actions/runs/43072056952)
- **分支**: `pd-max-top-logprobs-num`
- **总耗时**: 26.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43072056952

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 22.4min | 环境问题 | 自定义容器执行失败，作业在加载模型权重过程中被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744800) |
| base-b-test-2-npu-a3 / run (0) | 22.7min | 环境问题 | 自定义容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744876) |

- **base-b-test-1-npu-a3 / run (0)**: 日志显示模型分片加载至60%时出现“Executing the custom container implementation failed”，属于自托管 runner 容器环境异常，非用例代码错误，需联系 runner 管理员排查容器/资源问题。
  链接: https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744800

- **base-b-test-2-npu-a3 / run (0)**: 日志显示 'Executing the custom container implementation failed'，发生在第5个用例启动后约11秒，属于自托管 runner 容器环境异常，非用例代码或精度问题，需联系 runner 管理员排查。
  链接: https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744876

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130702475405) |
| base-a-test-npu | 2.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130702475420) |
| multimodal-gen-test-4-npu-a3 (0) | 6.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703743994) |
| multimodal-gen-test-4-npu-a3 (1) | 13.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744182) |
| base-b-test-4-npu-a3 / run (1) | 10.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744339) |
| base-b-test-4-npu-a3 / run (0) | 20.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744564) |
| base-b-test-8-npu-a3 / run (0) | 10.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744821) |
| base-b-test-16-npu-a3 / run (0) | 13.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43072056952/job/130703744928) |


## [Run #43071829299](https://github.com/sgl-project/sglang/actions/runs/43071829299)
- **分支**: `dark/carv2-symm-workspace`
- **总耗时**: 72.3min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43071829299

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 3.0min | 环境问题 | 自托管 runner 执行自定义容器实现失败，作业在容器启动阶段即报错退出。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130739209440) |
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 3.0min | 环境问题 | 自托管 runner 的自定义容器实现执行失败，作业在容器启动阶段即中止。 | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130739209477) |

- **base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3**: 日志显示 CANN 自定义算子安装成功后，报错“Executing the custom container implementation failed. Please contact your self hosted runner administrator.”，属于 runner/容器环境问题，非用例代码或性能回归。
  链接: https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130739209440

- **base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3**: 日志显示 CANN 自定义算子安装成功后，报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner/容器环境问题，非用例代码或性能回归。
  链接: https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130739209477

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130701715326) |
| base-a-test-npu | 2.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130701715420) |
| multimodal-gen-test-1-npu-a3 (1) | 22.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864206) |
| multimodal-gen-test-4-npu-a3 (1) | 23.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864253) |
| multimodal-gen-test-1-npu-a3 (0) | 19.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864320) |
| base-b-test-1-npu-a3 / run (0) | 24.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864328) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864406) |
| base-b-test-2-npu-a3 / run (0) | 27.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864514) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864589) |
| base-b-test-8-npu-a3 / run (0) | 10.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864604) |
| base-b-test-4-npu-a3 / run (0) | 17.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702864928) |
| multimodal-gen-test-4-npu-a3 (0) | 35.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130702865201) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 18.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130718343610) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 4.3min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130718343653) |
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 37.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43071829299/job/130718343713) |


## [Run #43063816422](https://github.com/sgl-project/sglang/actions/runs/43063816422)
- **分支**: `clearing_console_output`
- **总耗时**: 35.8min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43063816422

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 15.4min | 环境问题 | 宿主机内存不足，host 内存分配失败，server 崩溃/被杀 | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253891) |

- **base-b-test-1-npu-a3 / run (0)**: 日志命中 host 内存分配失败（'Malloc pin memory failed' 或 'rtsMallocHost ... out of memory'）：server 各 TP/EP 调度器因 host OOM 同时异常退出，随后被 SIGKILL（exit -9/137）。常见于同一作业内多个用例连跑、前一用例资源未完全释放，需检查 runner 内存水位与用例间清理
  - 失败用例: npu_autoround_moe.py, npu_autoround_moe.py
  链接: https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253891

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130673571484) |
| base-a-test-npu | 2.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130673572047) |
| multimodal-gen-test-1-npu-a3 (0) | 16.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253194) |
| multimodal-gen-test-1-npu-a3 (1) | 17.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253256) |
| multimodal-gen-test-4-npu-a3 (0) | 31.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253257) |
| multimodal-gen-test-4-npu-a3 (1) | 21.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253332) |
| base-b-test-2-npu-a3 / run (0) | 21.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253565) |
| base-b-test-4-npu-a3 / run (0) | 18.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253626) |
| base-b-test-8-npu-a3 / run (0) | 8.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253635) |
| base-b-test-16-npu-a3 / run (0) | 16.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253642) |
| base-b-test-4-npu-a3 / run (1) | 11.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43063816422/job/130675253678) |


## [Run #43059035629](https://github.com/sgl-project/sglang/actions/runs/43059035629)
- **分支**: `port/dflash-draft-kv-ring`
- **总耗时**: 43.5min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/43059035629

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3 | 15.5min | 环境问题 | 自托管 runner 的自定义容器执行失败，导致作业异常终止 | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130672123470) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 15.5min | 环境问题 | 自托管 runner 的容器执行失败，作业被中断 | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130672123536) |

- **base-c-test-acc-16-npu-a3 / base-c-test-acc-16-npu-a3**: 日志末尾报错 'Executing the custom container implementation failed. Please contact your self hosted runner administrator.'，属于 runner 容器环境故障，非用例代码或精度问题；此前 chat/completions 请求均返回 200。
  链接: https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130672123470

- **base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3**: 日志显示服务端请求正常返回 200，随后报错 'Executing the custom container implementation failed'，属于自托管 runner 容器运行时故障，非用例本身失败。
  链接: https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130672123536

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130656497469) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130656497632) |
| multimodal-gen-test-4-npu-a3 (0) | 33.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562177) |
| multimodal-gen-test-4-npu-a3 (1) | 22.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562257) |
| multimodal-gen-test-1-npu-a3 (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562437) |
| base-b-test-16-npu-a3 / run (0) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562505) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562529) |
| base-b-test-1-npu-a3 / run (0) | 24.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562544) |
| multimodal-gen-test-1-npu-a3 (1) | 20.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562557) |
| base-b-test-2-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562581) |
| base-b-test-4-npu-a3 / run (0) | 19.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657562599) |
| base-b-test-4-npu-a3 / run (1) | 11.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130657563034) |
| base-c-test-acc-2-npu-a3 / base-c-test-acc-2-npu-a3 | 3.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/43059035629/job/130672123494) |


## [Run #42994850535](https://github.com/sgl-project/sglang/actions/runs/42994850535)
- **分支**: `qwen38_quant`
- **总耗时**: 12.7min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42994850535

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-c-test-perf-16-npu-a3 / base-c-test-perf-16-npu-a3 | 1.1min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42994850535/job/131015186826) |
| base-c-test-perf-2-npu-a3 / base-c-test-perf-2-npu-a3 | 1.0min | 健康检查失败 | check-pr-test-health 步骤失败（fast-fail 级联） | [job link](https://github.com/sgl-project/sglang/actions/runs/42994850535/job/131015186849) |



### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994850535/job/131014338266) |
| base-a-test-npu | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42994850535/job/131014338267) |


## [Run #42988416101](https://github.com/sgl-project/sglang/actions/runs/42988416101)
- **分支**: `junlin/diffusion-npu-profiler`
- **总耗时**: 96.3min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42988416101

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-4-npu-a3 / run (1) | 10.0min | 日志下载失败 | 日志下载 HTTP 404 | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395427) |


### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-a-test-npu | 2.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131058291895) |
| Recommend tests from coverage | 1.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131058292016) |
| multimodal-gen-test-1-npu-a3 (1) | 18.0min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395164) |
| multimodal-gen-test-1-npu-a3 (0) | 16.4min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395174) |
| multimodal-gen-test-4-npu-a3 (1) | 21.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395257) |
| multimodal-gen-test-4-npu-a3 (0) | 32.9min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395284) |
| base-b-test-2-npu-a3 / run (0) | 24.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395345) |
| base-b-test-1-npu-a3 / run (0) | 23.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395351) |
| base-b-test-4-npu-a3 / run (0) | 21.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395434) |
| base-b-test-8-npu-a3 / run (0) | 8.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395456) |
| base-b-test-16-npu-a3 / run (0) | 27.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42988416101/job/131059395539) |


## [Run #42956151253](https://github.com/sgl-project/sglang/actions/runs/42956151253)
- **分支**: `bbuf/cleanup-round3`
- **总耗时**: 25.5min | **结论**: failure
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42956151253

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| base-b-test-1-npu-a3 / run (0) | 24.9min | 代码错误 | test_dspark_npu_dispatch.py 用例执行失败，导致作业退出码为1 | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789742476) |

- **base-b-test-1-npu-a3 / run (0)**: TIMINGS 显示 test/registered/kernels/ops/speculative/test_dspark_npu_dispatch.py 的 passed 为 false（耗时47秒），其余用例均通过，最终进程以退出码1结束。日志未给出具体 Traceback，需查看该用例详细输出定位失败原因。
  - 失败用例: dspark_npu_dispatch.py
  链接: https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789742476

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| base-b-test-2-npu-a3 / run (0) | 25.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789911213) |
| base-b-test-8-npu-a3 / run (0) | 8.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789961360) |
| base-b-test-4-npu-a3 / run (0) | 20.6min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130789986865) |
| multimodal-gen-test-4-npu-a3 (0) | 33.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790046341) |
| base-b-test-4-npu-a3 / run (1) | 15.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790225001) |
| base-b-test-16-npu-a3 / run (0) | 11.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790343901) |
| multimodal-gen-test-4-npu-a3 (1) | 21.1min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790370781) |
| base-a-test-npu | 1.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790399875) |
| multimodal-gen-test-1-npu-a3 (0) | 17.5min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790464124) |
| multimodal-gen-test-1-npu-a3 (1) | 19.8min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790543788) |
| Recommend tests from coverage | 2.2min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42956151253/job/130790587537) |


## [Run #42906299425](https://github.com/sgl-project/sglang/actions/runs/42906299425)
- **分支**: `hidream`
- **总耗时**: 11.6min | **结论**: cancelled
- **workflow 链接**: https://github.com/sgl-project/sglang/actions/runs/42906299425

### ⚠️ 失败/超时任务

| 任务 | 耗时 | 分类 | AI 分析 | 链接 |
|------|------|------|---------|------|
| multimodal-gen-test-1-npu-a3 (0) | 8.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592153) |
| multimodal-gen-test-1-npu-a3 (1) | 8.8min | 环境问题 | 测试脚本退出码5，unittest存在errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592177) |
| multimodal-gen-test-4-npu-a3 (0) | 8.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592206) |
| multimodal-gen-test-4-npu-a3 (1) | 8.9min | 环境问题 | 测试脚本退出码5，unittest出现errors，疑似setUpClass阶段sglang server启动失败 | [job link](https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592268) |

- **multimodal-gen-test-1-npu-a3 (0)**: 日志显示diffusion-failures目录无文件，未上传artifact；作业以退出码5结束，表明unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592153

- **multimodal-gen-test-1-npu-a3 (1)**: 日志显示diffusion-failures目录无文件，未上传artifact；退出码5表明unittest有errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592177

- **multimodal-gen-test-4-npu-a3 (0)**: 日志末尾显示未找到diffusion-failures/目录，无产物上传；退出码5表明unittest存在errors，最常见为setUpClass时sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略部分的Traceback确认。
  链接: https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592206

- **multimodal-gen-test-4-npu-a3 (1)**: 日志显示diffusion-failures目录无文件可上传，说明测试用例执行异常。退出码5表示unittest存在errors，最常见原因是setUpClass阶段sglang server启动失败（如host OOM或进程被SIGKILL），需查看中间省略的Traceback确认具体错误。
  链接: https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130739592268

### 正常任务

| 任务 | 耗时 | 结果 | 链接 |
|------|------|------|------|
| Recommend tests from coverage | 1.7min | success | [job link](https://github.com/sgl-project/sglang/actions/runs/42906299425/job/130738644416) |


---
*Auto-generated by ci_monitor.py*