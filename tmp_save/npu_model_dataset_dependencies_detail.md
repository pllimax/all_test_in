# NPU 测试用例本地模型/数据集依赖汇总

扫描目录: test/registered/npu | 模型: 125 | 数据集: 26

## 一、模型权重 -> 大小 -> 使用测试脚本

### [hf]Qwen3-30B-A3B-Instruct-2507-theo-style-lora — 未公开(内部/私有仓库)
- basic_function/lora/test_npu_experts_shared_outer_lora.py

### AI-ModelScope/Llama-3.1-8B-Instruct — 32.13 GB
- accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_aime25.py
- accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_gsm8k.py
- accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py
- accuracy/glm4_6v_flash/test_npu_glm4_6v_flash_1p_mmmu.py
- accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_aime25.py
- accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_gsm8k.py
- accuracy/glm5_2/test_npu_glm_5_2_w4a8_8p_gpqa.py
- accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms_gpqa.py
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_8p_in3k5_out1k5_50ms_gpqa.py
- accuracy/moonshotai_moonlight_16b_a3b/test_npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in6k_out1k5_bs16_gpqa.py
- accuracy/qwen3_30b_a3b/test_npu_qwen3_30b_w8a8_1p_in3k5_out1k5_50ms_aime25.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_bf16_8p_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa_a2.py
- accuracy/qwen3_5_397b/test_npu_qwen3_5_397b_8p_aime26.py
- accuracy/qwen3_5_397b/test_npu_qwen3_5_397b_8p_gpqa.py
- accuracy/qwen3_5_9b/test_npu_qwen3_5_9b_bf16_1p_gsm8k.py
- accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_1p_gpqa.py
- accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_aime26.py
- accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms_aime26.py
- accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py
- accuracy/qwen3_omni_30b_a3b_thinking/test_npu_qwen3_omni_30b_a3b_thinking_1p_mmmu.py
- accuracy/qwen3_vl_30b_a3b/test_npu_qwen3_vl_30b_a3b_bf16_2p_gsm8k.py
- accuracy/qwen3_vl_30b_a3b_thinking/test_npu_qwen3_vl_30b_a3b_thinking_1p_mmmu.py
- accuracy/qwen3_vl_8b/test_npu_qwen3_vl_8b_bf16_2p_gsm8k.py
- accuracy/qwen3_vl_8b_thinking/test_npu_qwen3_vl_8b_thinking_1p_mmmu.py
- basic_function/Custom_weight_loader/test_npu_weight_loader_drop_cache.py
- basic_function/Custom_weight_loader/test_npu_weight_loader_prefetch.py
- basic_function/EPD/test_npu_epd_disaggregation.py
- basic_function/HTTP/test_npu_nccl_port.py
- basic_function/HiCache/test_npu_hicache.py
- basic_function/HiCache/test_npu_hicache_mha.py
- basic_function/HiCache/test_npu_hicache_mla.py
- basic_function/HiCache/test_npu_hicache_page.py
- basic_function/HiCache/test_npu_hicache_storage_file_backend.py
- basic_function/HiCache/test_npu_hicache_storage_runtime_attach_detach.py
- basic_function/HiCache/test_npu_hicache_variants.py
- basic_function/HiCache/test_npu_hierarchical_cache_mla.py
- basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py
- basic_function/Multi-Modal/test_npu_mm_limit.py
- basic_function/api_related/test_npu_api_related_tool_call.py
- basic_function/api_related/test_npu_default_chat_template_kwargs.py
- basic_function/core/test_npu_hidden_states.py
- basic_function/debug_tensor/test_npu_debug_tensor_dump_output_folder.py
- basic_function/debug_tensor/test_npu_debug_tensor_dumps.py
- basic_function/debug_tensor/test_npu_debug_tensor_input_file.py
- basic_function/dllm/test_npu_llada2_mini.py
- basic_function/kernel_backends/test_npu_hybrid_attention_backend.py
- basic_function/kernel_backends/test_npu_mm_attention_backend.py
- basic_function/kernel_backends/test_npu_sampling_backend.py
- basic_function/kernel_backends/test_npu_swa_radix_cache_kl.py
- basic_function/logging/test_npu_log_level.py
- basic_function/logging/test_npu_metrics_bucket_boundary.py
- basic_function/lora/test_npu_lora_openai_compatible_supplement.py
- basic_function/lora/test_npu_lora_tied_lm_head.py
- basic_function/lora/test_npu_lora_update.py
- basic_function/mambacache/test_npu_mamba_cache.py
- basic_function/mambacache/test_npu_qwen3_next_models.py
- basic_function/mambacache/test_npu_qwen3_next_models_mtp.py
- basic_function/memory_and_scheduling/test_npu_mixed_chunked_prefill.py
- basic_function/memory_and_scheduling/test_npu_no_chunked_prefill.py
- basic_function/memory_and_scheduling/test_npu_prefill_delayer.py
- basic_function/memory_and_scheduling/test_npu_prefill_max_requests.py
- basic_function/memory_and_scheduling/test_npu_request_length_validation.py
- basic_function/memory_and_scheduling/test_npu_scheduler_control.py
- basic_function/model_override/test_npu_model_override_args.py
- basic_function/model_tokenizer/test_npu_model_config_parser.py
- basic_function/model_tokenizer/test_npu_multi_detokenizer.py
- basic_function/model_tokenizer/test_npu_tokenizer_backend.py
- basic_function/msprobe/test_npu_msprobe_dump_config.py
- basic_function/offloading/test_npu_offload_modes.py
- basic_function/optimization_debug/test_npu_compile_graph_tp1_bf16.py
- basic_function/optimization_debug/test_npu_graph_tp1_bf16.py
- basic_function/optimization_debug/test_npu_graph_tp2_bf16.py
- basic_function/optimization_debug/test_npu_piecewise_graph_prefill.py
- basic_function/optimization_debug_options/test_npu_allow_auto_truncate.py
- basic_function/optimization_debug_options/test_npu_attn_tp_gather_fuseep.py
- basic_function/optimization_debug_options/test_npu_cuda_graph_config.py
- basic_function/optimization_debug_options/test_npu_disable_cuda_graph.py
- basic_function/optimization_debug_options/test_npu_disable_cuda_graph_padding.py
- basic_function/optimization_debug_options/test_npu_disable_tokenizer_batch_decode.py
- basic_function/optimization_debug_options/test_npu_embedding_interpolation.py
- basic_function/optimization_debug_options/test_npu_enable_custom_logit_processor.py
- basic_function/optimization_debug_options/test_npu_enable_mixed_chunk.py
- basic_function/optimization_debug_options/test_npu_enable_return_routed_experts.py
- basic_function/optimization_debug_options/test_npu_keep_mm_feature_on_device.py
- basic_function/optimization_debug_options/test_npu_openai_server_hidden_states.py
- basic_function/optimization_debug_options/test_npu_piecewise.py
- basic_function/optimization_debug_options/test_npu_pre_warm_nccl.py
- basic_function/optimization_debug_options/test_npu_torch_compile_debug.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_R1_0528_w4a8_per_channel.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v2.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_480b.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v2.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v3_2_w8a8.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_480b.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_next.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_eplb_min_rebalancing_utilization_threshold.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_init-expert-location.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_moe_runner_backend.py
- basic_function/parameter/test_npu_batch_notify_size.py
- basic_function/parameter/test_npu_custom_sigquit_handler.py
- basic_function/parameter/test_npu_enable_streaming_session.py
- basic_function/parameter/test_npu_fim_completion.py
- basic_function/parameter/test_npu_incremental_streaming_output.py
- basic_function/parameter/test_npu_load_snapshot_publish_interval.py
- basic_function/parameter/test_npu_log_level.py
- basic_function/parameter/test_npu_priority_scheduling.py
- basic_function/parameter/test_npu_retract_decode.py
- basic_function/parameter/test_npu_ssl.py
- basic_function/parameter/test_npu_stream_response_include_usage.py
- basic_function/parameter/test_npu_warmups.py
- basic_function/pd_disaggregation/test_npu_disaggregation_basic.py
- basic_function/pd_disaggregation/test_npu_disaggregation_hybrid_attention.py
- basic_function/prefill_only/test_npu_score_engine.py
- basic_function/quant/test_npu_autoround_dense.py
- basic_function/quant/test_npu_autoround_moe.py
- basic_function/quant/test_npu_gguf.py
- basic_function/quant/test_npu_gguf_moe.py
- basic_function/quant/test_npu_gptq_moe.py
- basic_function/quant/test_npu_w4a4_quantization.py
- basic_function/quantization_and_data_type/test_npu_dtype.py
- basic_function/quantization_and_data_type/test_npu_enable_fp32_lm_head.py
- basic_function/quantization_and_data_type/test_npu_kv_cache_dtype.py
- basic_function/rl/test_npu_moe_rl_routing_capture.py
- basic_function/rl/test_npu_moe_rl_weight_updates_from_disk_and_tensor.py
- basic_function/rl/test_npu_rl_release_memory_occupation.py
- basic_function/runtime_options/test_npu_disaggregation_pp.py
- basic_function/runtime_options/test_npu_pp_single_node.py
- basic_function/runtime_options/test_npu_random_seed.py
- basic_function/runtime_options/test_npu_skip_tokenizer_init.py
- basic_function/runtime_options/test_npu_stream_interval.py
- basic_function/runtime_opts/test_npu_mla_fia_w8a8int8.py
- basic_function/runtime_opts/test_npu_mla_w8a8int8.py
- basic_function/runtime_opts/test_npu_tp1_bf16.py
- basic_function/runtime_opts/test_npu_tp2_bf16.py
- basic_function/runtime_opts/test_npu_tp2_fia_bf16.py
- basic_function/runtime_opts/test_npu_tp4_bf16.py
- basic_function/sessions/test_npu_streaming_session.py
- basic_function/sessions/test_npu_streaming_session_extra.py
- basic_function/sessions/test_npu_streaming_session_swa.py
- basic_function/speculative_inference/test_npu_adaptive_speculative.py
- basic_function/speculative_inference/test_npu_basic_sanity_eagle3.py
- basic_function/speculative_inference/test_npu_eagle3.py
- basic_function/speculative_inference/test_npu_eagle_constrained_decoding.py
- basic_function/speculative_inference/test_npu_eagle_infer_beta_dp_attention.py
- basic_function/speculative_inference/test_npu_spec_eagle.py
- basic_function/speculative_inference/test_npu_spec_eagle_parity.py
- basic_function/speculative_inference/test_npu_spec_eagle_stress.py
- interface/test_npu_matched_stop.py
- llm_models/test_npu_afm_4_5b.py
- llm_models/test_npu_deepseek_v32_indexcache.py
- llm_models/test_npu_deepseek_v3_2_exp_w8a8.py
- llm_models/test_npu_deepseek_v3_2_w8a8.py
- llm_models/test_npu_ernie_4_5_21b_a3b_pt.py
- llm_models/test_npu_gemma_3_4b_it_llm.py
- llm_models/test_npu_gpt_oss_120b_bf16.py
- llm_models/test_npu_kimi_k2_thinking.py
- llm_models/test_npu_ling_lite.py
- llm_models/test_npu_llama4_scount_17b_16e.py
- llm_models/test_npu_mimo_7b_rl.py
- llm_models/test_npu_minimax_m2_bf16.py
- llm_models/test_npu_phi_4_multimodal_llm.py
- llm_models/test_npu_qwen3_0_6b.py
- llm_models/test_npu_qwen3_1_7b_gptq_int8.py
- llm_models/test_npu_qwen3_235b_a22b_w8a8.py
- llm_models/test_npu_qwen3_30b.py
- llm_models/test_npu_qwen3_30b_attn_cp.py
- llm_models/test_npu_qwen3_30b_fuseep.py
- llm_models/test_npu_qwen3_30b_w4a4.py
- llm_models/test_npu_qwen3_32b.py
- llm_models/test_npu_qwen3_8b_communications_quantization.py
- llm_models/test_npu_qwen3_coder_480b_a35b.py
- llm_models/test_npu_qwen3_next_80b.py
- llm_models/test_npu_qwq_32b_w8a8.py
- llm_models/test_npu_trinity_mini.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_prefix90_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1080p_30_out256_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_2p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in128k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in16k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in64k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1080p_30_out256_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in128k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in128k_out1k_prefix90_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in254k_out1k.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_2p_in984k_out1k.py
- rerank_models/test_npu_qwen3_reranker_8b.py
- rerank_models/test_npu_qwen3_vl_reranker_2b.py
- reward_models/test_npu_gemma_2_27b_v0_2.py
- vlm_models/test_npu_encoder_dp.py
- vlm_models/test_npu_gemma_3_4b_it.py
- vlm_models/test_npu_glm_4_5v.py
- vlm_models/test_npu_janus_pro_1b.py
- vlm_models/test_npu_janus_pro_7b.py
- vlm_models/test_npu_kimi_vl_a3b_instruct.py
- vlm_models/test_npu_mimo_vl_7b_rl.py
- vlm_models/test_npu_minicpm_o_2_6.py
- vlm_models/test_npu_mistral_small_3_1_24b_instruct_2503.py
- vlm_models/test_npu_phi4_multimodal_instruct.py
- vlm_models/test_npu_qwen2_5_vl_3b_instruct.py
- vlm_models/test_npu_qwen2_5_vl_72b_instruct.py
- vlm_models/test_npu_qwen3_asr.py
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py
- vlm_models/test_npu_qwen3_vl_235b_a22b_instruct.py
- vlm_models/test_npu_qwen3_vl_30b_a3b_instruct.py
- vlm_models/test_npu_qwen3_vl_4b_instruct.py
- vlm_models/test_npu_qwen3_vl_8b_instruct.py
- vlm_models/test_npu_step3_vl_10b.py
- vlm_models/test_npu_token_id_retokenize_e2e.py
- vlm_models/test_npu_vision_openai_server_a.py
- vlm_models/test_npu_vlm_input_format.py

### AI-ModelScope/Skywork-Reward-Gemma-2-27B-v0.2 — 54.47 GB
- reward_models/test_npu_gemma_2_27b_v0_2.py

### Aswinkv07/qwen3.5-4b-neo4j-text2cypher-lora — 0.19 GB
- basic_function/lora/test_npu_lora_backend.py

### BAAI/bge-reranker-v2-m3 — 2.29 GB
- basic_function/openai_server/test_npu_openai_server.py

### CohereForAI/c4ai-command-r-v01 — 69.97 GB
- basic_function/api_related/test_npu_api_related.py

### DeepSeek-R1-0528-w4a8-per-channel — 未公开(内部/私有仓库)
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_R1_0528_w4a8_per_channel.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_R1_0528_w4a8_per_channel.py
- basic_function/speculative_inference/test_npu_speculative_draft_attention_backend.py

### DeepSeek-V3.2-Exp-W8A8 — 未公开(内部/私有仓库)
- accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_aime25.py
- accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_gsm8k.py
- llm_models/test_npu_deepseek_v3_2_exp_w8a8.py

### Eco-Tech/DeepSeek-V4-Flash-0731-w8a8 — 313.45 GB
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py

### Eco-Tech/DeepSeek-V4-Flash-w8a8-mtp — 300.1 GB
- accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in8k_out1k_50ms.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py

### Eco-Tech/GLM-5.1-w4a8 — 420.17 GB
- accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py
- performance/glm5_1/test_npu_glm5_1_w4a8_16p_in3k5_out1k5_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in128k_out1k_20ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in16k_out1k_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_20ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in65k_out1k5_prefix90_25ms.py

### Eco-Tech/Kimi-K2.6-w4a8 — 535.91 GB
- accuracy/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms_aime25.py
- basic_function/optimization_debug_options/test_npu_full_decode_graph_gsm8k.py

### Eco-Tech/MiniMax-M2.5-w8a8-QuaRot — 230.82 GB
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms_gpqa.py
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_8p_in3k5_out1k5_50ms_gpqa.py

### Eco-Tech/Qwen3-30B-A3B-w4a4-LAOS — 31.38 GB
- llm_models/test_npu_qwen3_30b_w4a4.py

### Eco-Tech/Qwen3-32B-w4a4-LAOS — 34.37 GB
- basic_function/quant/test_npu_w4a4_quantization.py

### Eco-Tech/Qwen3.5-35B-A3B-w8a8-mtp — 39.81 GB
- basic_function/Multi-Modal/test_npu_multimodal_quantization_chunked.py
- basic_function/forward/test_npu_enable_quant_communications.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_dispatcher_output_dtype.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_enable_waterfill.py

### Eco-Tech/Qwen3.5-397B-A17B-w4a8-mtp — 235.88 GB
- accuracy/qwen3_5_397b/test_npu_qwen3_5_397b_8p_aime26.py
- accuracy/qwen3_5_397b/test_npu_qwen3_5_397b_8p_gpqa.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_prefix90_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_prefix90_50ms.py

### Eco-Tech/Qwen3.6-27B-w8a8 — 32.15 GB
- accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in128k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in16k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in64k_out1k_50ms.py

### Howeee/DeepSeek-R1-0528-w8a8 — 未公开(内部/私有仓库)
- basic_function/malpo/test_npu_mlapo.py
- basic_function/parallel_strategy/test_npu_bucket_adjust_interval_secs_concurrency.py

### Intel/Qwen3-30B-A3B-Instruct-2507-int4-AutoRound — 16.83 GB
- basic_function/quant/test_npu_autoround_moe.py

### Intel/Qwen3-8B-int4-AutoRound — 6.11 GB
- basic_function/quant/test_npu_autoround_dense.py

### Kimi/Kimi-K2-Thinking — 594.26 GB
- llm_models/test_npu_kimi_k2_thinking.py

### LLM-Research/Llama-2-7B — 13.48 GB
- basic_function/HTTP/test_npu_nccl_port.py

### LLM-Research/Llama-3.2-1B — 4.95 GB
- basic_function/Custom_weight_loader/test_npu_update_weights_from_disk.py
- basic_function/optimization_debug_options/test_npu_enable_profile_cuda_graph.py
- basic_function/rl/test_npu_multi_instance_release_memory_occupation.py
- basic_function/rl/test_npu_rl_release_memory_occupation.py
- basic_function/runtime_options/test_npu_sleep_on_idle.py

### LLM-Research/Llama-3.2-1B-Instruct — 4.95 GB
- basic_function/Custom_weight_loader/test_npu_update_weights_from_disk.py
- basic_function/HTTP/test_npu_skip_warmup.py
- basic_function/HiCache/test_npu_hicache.py
- basic_function/api_related/test_npu_api_related_tool_call.py
- basic_function/core/test_npu_srt_engine.py
- basic_function/debug_tensor/test_npu_debug_tensor_input_file.py
- basic_function/kernel_backends/test_npu_hybrid_attention_backend.py
- basic_function/logging/test_npu_log_level.py
- basic_function/lora/test_npu_lora_basic.py
- basic_function/lora/test_npu_lora_load_from_tensor.py
- basic_function/lora/test_npu_lora_memory_eviction.py
- basic_function/lora/test_npu_lora_openai_compatible.py
- basic_function/lora/test_npu_lora_openai_compatible_supplement.py
- basic_function/lora/test_npu_max_loaded_loras.py
- basic_function/lora/test_npu_wait_threshold.py
- basic_function/memory_and_scheduling/test_npu_abort_on_priority_when_disabled.py
- basic_function/memory_and_scheduling/test_npu_load_snapshot_server.py
- basic_function/memory_and_scheduling/test_npu_priority_scheduling.py
- basic_function/memory_and_scheduling/test_npu_priority_scheduling_preemption_threshold.py
- basic_function/memory_and_scheduling/test_npu_radix_attention.py
- basic_function/memory_and_scheduling/test_npu_schedule_low_priority_values_first.py
- basic_function/model_override/test_npu_model_override_args.py
- basic_function/model_tokenizer/test_npu_model_tokenizer.py
- basic_function/model_tokenizer/test_npu_tokenizer_backend.py
- basic_function/msprobe/test_npu_msprobe_dump_config.py
- basic_function/openai_server/test_npu_openai_server.py
- basic_function/optimization_debug_options/test_npu_allow_auto_truncate.py
- basic_function/optimization_debug_options/test_npu_attn_tp_gather_fuseep.py
- basic_function/optimization_debug_options/test_npu_cuda_graph_config.py
- basic_function/optimization_debug_options/test_npu_disable_cuda_graph.py
- basic_function/optimization_debug_options/test_npu_enable_cudagraph_gc.py
- basic_function/optimization_debug_options/test_npu_no_extra_forked_npu_context.py
- basic_function/optimization_debug_options/test_npu_openai_server_hidden_states.py
- basic_function/optimization_debug_options/test_npu_radix_cache_hit.py
- basic_function/parameter/test_npu_batch_notify_size.py
- basic_function/parameter/test_npu_custom_sigquit_handler.py
- basic_function/parameter/test_npu_enable_streaming_session.py
- basic_function/parameter/test_npu_http2_server.py
- basic_function/parameter/test_npu_incremental_streaming_output.py
- basic_function/parameter/test_npu_load_snapshot_publish_interval.py
- basic_function/parameter/test_npu_log_level.py
- basic_function/parameter/test_npu_original_logprobs.py
- basic_function/parameter/test_npu_priority_scheduling.py
- basic_function/parameter/test_npu_ssl.py
- basic_function/parameter/test_npu_start_profile.py
- basic_function/parameter/test_npu_stream_response_include_usage.py
- basic_function/pd_disaggregation/test_npu_disaggregation_basic.py
- basic_function/prefill_only/test_npu_pooled_hidden_states.py
- basic_function/prefill_only/test_npu_score_api.py
- basic_function/prefill_only/test_npu_score_engine.py
- basic_function/profiling/test_npu_profile_v2.py
- basic_function/quantization_and_data_type/test_npu_dtype.py
- basic_function/quantization_and_data_type/test_npu_kv_cache_dtype.py
- basic_function/rl/test_npu_multi_instance_release_memory_occupation.py
- basic_function/rl/test_npu_rl_pause_resume_basic.py
- basic_function/rl/test_npu_rl_pause_resume_loop.py
- basic_function/rl/test_npu_rl_pause_resume_multi_tokenizer.py
- basic_function/rl/test_npu_rl_pause_resume_multi_turn.py
- basic_function/rl/test_npu_rl_pause_resume_tool_call.py
- basic_function/rl/test_npu_rl_release_memory_occupation.py
- basic_function/runtime_options/test_npu_constrained_json_disable_any_whitespace.py
- basic_function/runtime_options/test_npu_gpu_id.py
- basic_function/runtime_options/test_npu_random_seed.py
- basic_function/runtime_options/test_npu_skip_tokenizer_init.py
- interface/test_npu_anthropic_tool_use.py
- interface/test_npu_api.py
- interface/test_npu_api_abort_request.py
- interface/test_npu_openai_function_calling.py
- interface/test_npu_openai_server_ignore_eos.py
- interface/test_npu_penalty.py

### LLM-Research/Meta-Llama-3-8B-Instruct — 32.13 GB
- basic_function/speculative_inference/test_npu_speculative_token_map.py

### LLM-Research/Meta-Llama-3.1-8B-Instruct — 32.13 GB
- basic_function/model_tokenizer/test_npu_multi_tokenizer.py

### Qwen/Eagle3-Qwen3-8B-zh — 未公开(内部/私有仓库)
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in6k_out1k5_bs16_gpqa.py

### Qwen/Qwen2-VL-2B-Instruct — 4.43 GB
- basic_function/model_loading/test_npu_external_models.py
- vlm_models/test_npu_vision_openai_server_a.py

### Qwen/Qwen2.5-7B-Instruct — 15.24 GB
- basic_function/HiCache/test_npu_hicache_mha.py
- basic_function/optimization_debug/test_npu_compile_graph_tp1_bf16.py
- basic_function/optimization_debug/test_npu_graph_tp1_bf16.py
- basic_function/optimization_debug/test_npu_graph_tp2_bf16.py
- basic_function/optimization_debug/test_npu_piecewise_graph_prefill.py
- basic_function/optimization_debug_options/test_npu_cuda_graph_bs.py
- basic_function/runtime_opts/test_npu_tp1_bf16.py
- basic_function/runtime_opts/test_npu_tp2_bf16.py
- basic_function/runtime_opts/test_npu_tp2_fia_bf16.py

### Qwen/Qwen2.5-VL-3B-Instruct — 7.52 GB
- basic_function/runtime_options/test_npu_skip_tokenizer_init.py
- vlm_models/test_npu_qwen2_5_vl_3b_instruct.py
- vlm_models/test_npu_token_id_retokenize_e2e.py
- vlm_models/test_npu_vlm_input_format.py

### Qwen/Qwen2.5-VL-72B-Instruct — 146.83 GB
- vlm_models/test_npu_encoder_dp.py
- vlm_models/test_npu_qwen2_5_vl_72b_instruct.py

### Qwen/Qwen3-0.6B — 1.52 GB
- basic_function/api_related/test_npu_default_chat_template_kwargs.py
- basic_function/api_related/test_npu_e2e_constrained_reasoning.py
- basic_function/api_related/test_npu_strip_thinking.py
- basic_function/core/test_npu_engine_child_pids.py
- basic_function/core/test_npu_hidden_states.py
- basic_function/core/test_npu_srt_endpoint.py
- basic_function/input_embedding/test_npu_input_embeds_chunked.py
- basic_function/kernel_backends/test_npu_json_mode.py
- basic_function/logging/test_npu_crash_dump.py
- basic_function/logging/test_npu_request_logger.py
- basic_function/logging/test_npu_scheduler_status_logger.py
- basic_function/logging/test_npu_tracing.py
- basic_function/logging/test_npu_tracing_disaggregation.py
- basic_function/memory_and_scheduling/test_npu_data_parallelism.py
- basic_function/memory_and_scheduling/test_npu_prefill_delayer.py
- basic_function/memory_and_scheduling/test_npu_prefill_delayer_buckets.py
- basic_function/memory_and_scheduling/test_npu_prefill_delayer_max_delay.py
- basic_function/memory_and_scheduling/test_npu_request_length_validation.py
- basic_function/memory_and_scheduling/test_npu_request_queue_validation.py
- basic_function/optimization_debug_options/test_npu_delete_ckpt_after_loading.py
- basic_function/optimization_debug_options/test_npu_disable_tokenizer_batch_decode.py
- basic_function/optimization_debug_options/test_npu_enable_mixed_chunk.py
- basic_function/optimization_debug_options/test_npu_enable_tokenizer_batch_encode.py
- basic_function/optimization_debug_options/test_npu_numa_node.py
- basic_function/optimization_debug_options/test_npu_pre_warm_nccl.py
- basic_function/optimization_debug_options/test_npu_scheduler_recv_interval.py
- basic_function/optimization_debug_options/test_npu_torch_compile_moe.py
- basic_function/parallel_strategy/test_npu_prefill_policy_bucket_balance.py
- basic_function/parameter/test_npu_input_embeddings.py
- basic_function/prefill_only/test_npu_pooled_hidden_states.py
- basic_function/prefill_only/test_npu_score_engine.py
- basic_function/rl/test_npu_weight_checker_e2e.py
- basic_function/runtime_options/test_npu_constrained_json_whitespace_pattern.py
- basic_function/runtime_options/test_npu_soft_watchdog.py
- basic_function/runtime_options/test_npu_stream_interval.py
- basic_function/runtime_options/test_npu_watchdog.py
- interface/test_npu_anthropic_server.py
- interface/test_npu_http2_server.py
- interface/test_npu_openai_server_ebnf.py
- llm_models/test_npu_qwen3_0_6b.py

### Qwen/Qwen3-1.7B-GPTQ-Int8 — 2.08 GB
- llm_models/test_npu_qwen3_1_7b_gptq_int8.py

### Qwen/Qwen3-30B-A3B — 61.08 GB
- basic_function/api_related/test_npu_sampling_default.py
- basic_function/export_metrics/test_npu_export_metrics.py
- basic_function/pd_disaggregation/test_npu_pd_disaggregation_optimistic.py
- basic_function/rl/test_npu_rl_release_memory_occupation.py
- basic_function/speculative_inference/test_npu_eagle_dp_attention.py
- interface/test_npu_enable_thinking.py
- llm_models/test_npu_qwen3_30b_attn_cp.py

### Qwen/Qwen3-30B-A3B-GGUF/Qwen3-30B-A3B-Q4_K_M.gguf — 18.56 GB
- basic_function/quant/test_npu_gguf_moe.py

### Qwen/Qwen3-30B-A3B-GPTQ-Int4 — 16.95 GB
- basic_function/quant/test_npu_gptq_moe.py

### Qwen/Qwen3-30B-A3B-Instruct-2507 — 61.08 GB
- basic_function/lora/test_npu_experts_shared_outer_lora.py
- basic_function/parallel_strategy/data_parallelism/test_npu_load_balance_method_pd_disaggregation.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_ep_dispatch_algorithm.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_expert_distribution_recorder_mode.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_init-expert-location.py
- basic_function/rl/test_npu_rl_release_memory_occupation.py
- llm_models/test_npu_qwen3_30b.py

### Qwen/Qwen3-30B-A3B-w8a8 — 未公开(内部/私有仓库)
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_30b_a3b_w8a8.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_30b_a3b_w8a8.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_eplb_min_rebalancing_utilization_threshold.py
- llm_models/test_npu_qwen3_30b_fuseep.py
- test_npu_memory_consumption.py

### Qwen/Qwen3-32B — 65.54 GB
- accuracy/qwen3_32b/test_npu_qwen3_32b_bf16_8p_gpqa.py
- basic_function/Custom_weight_loader/test_npu_prefetch_checkpoints_multi_npu.py
- basic_function/HiCache/test_npu_disaggregation_hicache.py
- basic_function/HiCache/test_npu_enable_offload_kvcache_cached_tokens.py
- basic_function/HiCache/test_npu_hicache_io_backend.py
- basic_function/HiCache/test_npu_hierarchical_cache_ttft_mha.py
- basic_function/api_related/test_npu_api_related_tool_call.py
- basic_function/debug_tensor/test_npu_debug_tensor_dump_output_folder.py
- basic_function/debug_tensor/test_npu_debug_tensor_dumps.py
- basic_function/dp_attn/test_npu_dp_attention.py
- basic_function/forward/test_npu_forward_hooks.py
- basic_function/ha/test_npu_pd_disaggregation_ha_mixed_worker_failover.py
- basic_function/ha/test_npu_router_ha_mixed_worker_failover.py
- basic_function/memory_and_scheduling/test_npu_schedule_conservativeness.py
- basic_function/offloading/test_npu_cpu_offload_gb.py
- basic_function/optimization_debug_options/test_npu_enable_custom_logit_processor.py
- basic_function/parameter/test_npu_dynamic_batch_tokenizer_params.py
- basic_function/pd_disaggregation/test_npu_pd_disaggregation.py
- basic_function/quantization_and_data_type/test_npu_enable_fp32_lm_head.py
- llm_models/test_npu_qwen3_32b.py

### Qwen/Qwen3-4B-GGUF/Qwen3-4B-Q4_K_M.gguf — 2.5 GB
- basic_function/model_tokenizer/test_npu_model_tokenizer.py
- basic_function/quant/test_npu_gguf.py

### Qwen/Qwen3-8B — 16.4 GB
- basic_function/Custom_weight_loader/test_npu_weight_loader_drop_cache.py
- basic_function/Custom_weight_loader/test_npu_weight_loader_prefetch.py
- basic_function/HiCache/test_npu_enable_offload_kvcache.py
- basic_function/HiCache/test_npu_hicache_variants.py
- basic_function/HiCache/test_npu_hierarchical_cache.py
- basic_function/HiCache/test_npu_hierarchical_cache_mutually_exclusive.py
- basic_function/HiCache/test_npu_radix_cache.py
- basic_function/bench_fn/test_npu_bench_serving_functionality.py
- basic_function/kernel_backends/test_npu_constrained_decoding.py
- basic_function/optimization_debug_options/test_npu_torch_compile_debug.py
- basic_function/sessions/test_npu_session_control.py
- basic_function/sessions/test_npu_streaming_session.py
- basic_function/sessions/test_npu_streaming_session_extra.py
- basic_function/speculative_inference/test_npu_adaptive_speculative.py
- basic_function/speculative_inference/test_npu_basic_sanity.py
- basic_function/speculative_inference/test_npu_basic_sanity_eagle3.py
- basic_function/speculative_inference/test_npu_constrained_decoding_spec_reasoning.py
- basic_function/speculative_inference/test_npu_dflash_speculative.py
- basic_function/speculative_inference/test_npu_eagle3.py
- basic_function/speculative_inference/test_npu_eagle_infer_beta_dp_attention.py
- basic_function/speculative_inference/test_npu_skip_dp_mlp_sync.py
- interface/test_npu_large_max_new_tokens.py
- llm_models/test_npu_qwen3_8b_communications_quantization.py

### Qwen/Qwen3-8B-W8A8 — 未公开(内部/私有仓库)
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in6k_out1k5_bs16_gpqa.py

### Qwen/Qwen3-8B_eagle3 — 未公开(内部/私有仓库)
- basic_function/HiCache/test_npu_hicache_variants.py
- basic_function/sessions/test_npu_streaming_session.py
- basic_function/sessions/test_npu_streaming_session_extra.py
- basic_function/speculative_inference/test_npu_adaptive_speculative.py
- basic_function/speculative_inference/test_npu_basic_sanity_eagle3.py
- basic_function/speculative_inference/test_npu_constrained_decoding_spec_reasoning.py
- basic_function/speculative_inference/test_npu_eagle3.py
- basic_function/speculative_inference/test_npu_eagle_infer_beta_dp_attention.py
- basic_function/speculative_inference/test_npu_skip_dp_mlp_sync.py

### Qwen/Qwen3-ASR-0.6B — 1.88 GB
- basic_function/api_related/test_npu_api_related_asr_max.py

### Qwen/Qwen3-ASR-1.7B — 4.7 GB
- vlm_models/test_npu_qwen3_asr.py

### Qwen/Qwen3-Embedding-8B — 15.15 GB
- embedding_models/test_npu_qwen3_embedding_8b.py

### Qwen/Qwen3-Next-80B-A3B-Instruct — 162.68 GB
- accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_next.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_next.py
- basic_function/pd_disaggregation/test_npu_disaggregation_hybrid_attention.py
- llm_models/test_npu_qwen3_next_80b.py

### Qwen/Qwen3-Omni-30B-A3B-Instruct — 70.53 GB
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py

### Qwen/Qwen3-Omni-30B-A3B-Thinking — 63.45 GB
- accuracy/qwen3_omni_30b_a3b_thinking/test_npu_qwen3_omni_30b_a3b_thinking_1p_mmmu.py

### Qwen/Qwen3-Reranker-8B — 16.39 GB
- rerank_models/test_npu_qwen3_reranker_8b.py

### Qwen/Qwen3-VL-235B-A22B-Instruct — 471.35 GB
- vlm_models/test_npu_qwen3_vl_235b_a22b_instruct.py

### Qwen/Qwen3-VL-30B-A3B-Instruct — 62.15 GB
- accuracy/qwen3_vl_30b_a3b/test_npu_qwen3_vl_30b_a3b_bf16_2p_gsm8k.py
- basic_function/EPD/test_npu_adaptive_dispatch_to_encoder.py
- basic_function/EPD/test_npu_disaggregated_vlm.py
- vlm_models/test_npu_qwen3_vl_30b_a3b_instruct.py
- vlm_models/test_npu_vision_openai_server_a.py

### Qwen/Qwen3-VL-30B-A3B-Thinking — 62.15 GB
- accuracy/qwen3_vl_30b_a3b_thinking/test_npu_qwen3_vl_30b_a3b_thinking_1p_mmmu.py

### Qwen/Qwen3-VL-4B-Instruct — 8.89 GB
- basic_function/EPD/test_npu_epd_disaggregation.py
- basic_function/Multi-Modal/test_npu_multimodal_basic.py
- basic_function/Multi-Modal/test_npu_multimodal_dp_attention.py
- basic_function/Multi-Modal/test_npu_multimodal_offload.py
- basic_function/Multi-Modal/test_npu_multimodal_parallelism.py
- basic_function/Multi-Modal/test_npu_multimodal_tool_call.py
- basic_function/optimization_debug_options/test_npu_embedding_interpolation.py
- interface/test_npu_api_encode.py
- vlm_models/test_npu_qwen3_vl_4b_instruct.py

### Qwen/Qwen3-VL-8B-Instruct — 17.55 GB
- accuracy/qwen3_vl_8b/test_npu_qwen3_vl_8b_bf16_2p_gsm8k.py
- basic_function/EPD/test_npu_epd_dynamic_register.py
- basic_function/Multi-Modal/test_npu_mm_limit.py
- basic_function/Multi-Modal/test_npu_multimodal_spec_overlap.py
- basic_function/model_tokenizer/test_npu_model_tokenizer_multimodal.py
- basic_function/prefix_mm_cache/test_npu_prefix_mm_cache.py
- vlm_models/test_npu_qwen3_vl_8b_instruct.py
- vlm_models/test_npu_vision_openai_server_a.py

### Qwen/Qwen3-VL-8B-Instruct-Eagle3 — 未公开(内部/私有仓库)
- basic_function/Multi-Modal/test_npu_multimodal_spec_overlap.py

### Qwen/Qwen3-VL-8B-Thinking — 17.55 GB
- accuracy/qwen3_vl_8b_thinking/test_npu_qwen3_vl_8b_thinking_1p_mmmu.py
- basic_function/pp/test_npu_pp_single_node_extra.py

### Qwen/Qwen3-VL-Reranker-2B — 4.27 GB
- rerank_models/test_npu_qwen3_vl_reranker_2b.py

### Qwen/Qwen3-a3B_eagle3 — 未公开(内部/私有仓库)
- accuracy/qwen3_30b_a3b/test_npu_qwen3_30b_w8a8_1p_in3k5_out1k5_50ms_aime25.py
- basic_function/speculative_inference/test_npu_eagle_dp_attention.py

### Qwen/Qwen3.5-27B — 55.59 GB
- basic_function/api_related/test_npu_api_related_tool_call.py

### Qwen/Qwen3.5-35B-A3B — 71.93 GB
- basic_function/Multi-Modal/test_npu_multimodal_moe_eplb.py
- basic_function/Multi-Modal/test_npu_multimodal_moe_gdn.py
- basic_function/Multi-Modal/test_npu_multimodal_moe_multistream.py
- basic_function/Multi-Modal/test_npu_multimodal_reasoning_parser.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_dispatcher_output_dtype.py

### Qwen/Qwen3.5-4B — 9.34 GB
- basic_function/lora/test_npu_lora_backend.py
- basic_function/lora/test_npu_lora_tied_lm_head.py

### Qwen/Qwen3.5-9B — 19.33 GB
- accuracy/qwen3_5_9b/test_npu_qwen3_5_9b_bf16_1p_gsm8k.py
- basic_function/Multi-Modal/test_npu_multimodal_chat_completions.py
- basic_function/Multi-Modal/test_npu_multimodal_dp_attention.py
- basic_function/Multi-Modal/test_npu_multimodal_gdn_attention.py
- basic_function/Multi-Modal/test_npu_multimodal_parallelism.py
- basic_function/Multi-Modal/test_npu_multimodal_pd_disaggregation.py
- basic_function/Multi-Modal/test_npu_multimodal_spec_decoding.py
- basic_function/rl/test_npu_rl_release_memory_occupation.py

### Qwen/Qwen3.6-27B — 55.59 GB
- accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_1p_gpqa.py
- basic_function/lora/test_npu_lora_qwen3_6_27b_logprob_diff.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1080p_30_out256_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_2p_in64k_out1k_prefix90_50ms.py

### Qwen/Qwen3.6-35B-A3B — 71.93 GB
- accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_aime26.py
- accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms_aime26.py
- basic_function/optimization_debug_options/test_npu_attn_tp_gather_fuseep.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1080p_30_out256_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in128k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in128k_out1k_prefix90_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in254k_out1k.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_2p_in984k_out1k.py

### Qwen/gte-Qwen2-1.5B-instruct — 7.12 GB
- basic_function/core/test_npu_srt_engine.py

### Qwen3-Coder-480B-A35B-Instruct-w8a8-QuaRot — 未公开(内部/私有仓库)
- basic_function/api_related/test_npu_api_related_tool_call.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_480b.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_480b.py
- llm_models/test_npu_qwen3_coder_480b_a35b.py

### XiaomiMiMo/MiMo-7B-RL — 15.68 GB
- llm_models/test_npu_mimo_7b_rl.py

### XiaomiMiMo/MiMo-VL-7B-RL — 16.62 GB
- vlm_models/test_npu_mimo_vl_7b_rl.py

### YZY/Qwen3-8B — 未公开(内部/私有仓库)
- basic_function/checkpoint_decryption/test_npu_decrypted_draft_config_file.py

### YZY/Qwen3-8B_eagle3 — 未公开(内部/私有仓库)
- basic_function/checkpoint_decryption/test_npu_decrypted_draft_config_file.py

### ZhipuAI/GLM-4.5V — 215.45 GB
- vlm_models/test_npu_glm_4_5v.py

### ZhipuAI/GLM-4.6V-Flash — 20.61 GB
- accuracy/glm4_6v_flash/test_npu_glm4_6v_flash_1p_mmmu.py

### ZhipuAI/GLM-4.7-Flash — 62.47 GB
- accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_aime25.py
- accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_gsm8k.py

### Zjcxy-SmartAI/Eagle3-Qwen3-32B-zh — 1.57 GB
- accuracy/qwen3_32b/test_npu_qwen3_32b_bf16_8p_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa_a2.py
- basic_function/speculative_inference/test_npu_speculative_attention_mode.py
- basic_function/speculative_inference/test_npu_speculative_multi_npu.py
- basic_function/speculative_inference/test_npu_speculative_token_map.py

### aleoyang/Qwen3-32B-w8a8-MindIE — 42.77 GB
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa_a2.py
- basic_function/speculative_inference/test_npu_speculative_attention_mode.py
- basic_function/speculative_inference/test_npu_speculative_multi_npu.py
- basic_function/speculative_inference/test_npu_speculative_token_map.py

### algoprog/fact-generation-llama-3.1-8b-instruct-lora — 0.39 GB
- basic_function/lora/test_npu_lora_update.py

### arcee-ai/AFM-4.5B-Base — 9.26 GB
- llm_models/test_npu_afm_4_5b.py

### arcee-ai/Trinity-Mini — 52.27 GB
- llm_models/test_npu_trinity_mini.py

### baidu/ERNIE-4.5-21B-A3B-PT — 43.92 GB
- llm_models/test_npu_ernie_4_5_21b_a3b_pt.py

### codelion/Llama-3.2-1B-Instruct-tool-calling-lora — 0.18 GB
- basic_function/lora/test_npu_lora_basic.py
- basic_function/lora/test_npu_lora_load_from_tensor.py
- basic_function/lora/test_npu_lora_memory_eviction.py
- basic_function/lora/test_npu_lora_openai_compatible.py
- basic_function/lora/test_npu_lora_openai_compatible_supplement.py
- basic_function/lora/test_npu_max_loaded_loras.py
- basic_function/lora/test_npu_wait_threshold.py

### cyankiwi/MiniMax-M2-BF16 — 457.51 GB
- llm_models/test_npu_minimax_m2_bf16.py

### deepseek-ai/DeepSeek-Coder-V2-Lite-Instruct — 31.42 GB
- basic_function/memory_and_scheduling/test_npu_prefill_delayer.py
- basic_function/offloading/test_npu_offload_group_size.py
- basic_function/offloading/test_npu_offload_modes.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_moe_dense_tp_size.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_moe_runner_backend.py
- basic_function/runtime_options/test_npu_pp_single_node.py

### deepseek-ai/DeepSeek-R1-Distill-Qwen-7B — 15.24 GB
- basic_function/api_related/test_npu_reasoning_content.py

### deepseek-ai/Janus-Pro-1B — 4.18 GB
- vlm_models/test_npu_janus_pro_1b.py

### deepseek-ai/Janus-Pro-7B — 14.85 GB
- vlm_models/test_npu_janus_pro_7b.py

### deepseek-ai/deepseek-coder-1.3b-base — 2.69 GB
- basic_function/parameter/test_npu_fim_completion.py

### eigen-ai-labs/gpt-oss-120b-bf16 — 未公开(内部/私有仓库)
- basic_function/kernel_backends/test_npu_swa_radix_cache_kl.py
- basic_function/sessions/test_npu_streaming_session_swa.py
- llm_models/test_npu_gpt_oss_120b_bf16.py

### google/gemma-3-4b-it — 8.64 GB
- basic_function/kernel_backends/test_npu_mm_attention_backend.py
- llm_models/test_npu_gemma_3_4b_it_llm.py
- vlm_models/test_npu_gemma_3_4b_it.py
- vlm_models/test_npu_vlm_input_format.py

### google/gemma-4-31B-it — 62.58 GB
- vlm_models/test_npu_vision_openai_server_a.py

### hot_map/pd_prefill_0720.pt — 未公开(内部/私有仓库)
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in8k_out1k_50ms.py

### hotdogs/qwen3.6-27b-cybersecurity-lora — 1.32 GB
- basic_function/lora/test_npu_lora_qwen3_6_27b_logprob_diff.py

### iic/gte_Qwen2-1.5B-instruct — 7.11 GB
- basic_function/model_tokenizer/test_npu_openai_embedding.py

### inclusionAI/LLaDA2.0-mini — 32.52 GB
- basic_function/dllm/test_npu_llada2_mini.py

### inclusionAI/Ling-lite — 33.61 GB
- llm_models/test_npu_ling_lite.py

### lightseekorg/kimi-k2.6-eagle3 — 6.36 GB
- accuracy/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms_aime25.py

### lmms-lab/llava-onevision-qwen2-7b-ov — 16.07 GB
- vlm_models/test_npu_vision_openai_server_a.py

### lmsys/sglang-EAGLE-LLaMA3-Instruct-8B — 1.55 GB
- basic_function/speculative_inference/test_npu_speculative_token_map.py

### meta-llama/Llama-4-Scout-17B-16E-Instruct — 217.32 GB
- llm_models/test_npu_llama4_scount_17b_16e.py

### microsoft/Phi-4-multimodal-instruct — 12.88 GB
- basic_function/optimization_debug_options/test_npu_keep_mm_feature_on_device.py
- llm_models/test_npu_phi_4_multimodal_llm.py
- vlm_models/test_npu_phi4_multimodal_instruct.py

### mistralai/Mistral-7B-Instruct-v0.2 — 29.49 GB
- basic_function/model_tokenizer/test_npu_model_config_parser.py

### mistralai/Mistral-Small-3.1-24B-Instruct-2503 — 96.08 GB
- vlm_models/test_npu_mistral_small_3_1_24b_instruct_2503.py

### moonshotai/Kimi-VL-A3B-Instruct — 32.82 GB
- basic_function/dp_attn/test_npu_dp_attention.py
- vlm_models/test_npu_kimi_vl_a3b_instruct.py
- vlm_models/test_npu_vision_openai_server_a.py
- vlm_models/test_npu_vlm_input_format.py

### moonshotai/Moonlight-16B-A3B-Instruct — 31.93 GB
- accuracy/moonshotai_moonlight_16b_a3b/test_npu_moonlight_16b_a3b_bf16_1p_gsm8k.py

### nvidia/llama-3.1-nemoguard-8b-topic-control — 0.08 GB
- basic_function/lora/test_npu_lora_update.py

### openai/whisper-large-v3 — 24.7 GB
- basic_function/openai_server/test_npu_serving_transcription.py

### openbmb/MiniCPM-V-2_6 — 16.21 GB
- vlm_models/test_npu_vision_openai_server_a.py

### openbmb/MiniCPM-o-2_6 — 17.43 GB
- basic_function/parameter/test_npu_warmups.py
- vlm_models/test_npu_minicpm_o_2_6.py
- vlm_models/test_npu_vision_openai_server_a.py

### pbevan11/llama-3.1-8b-ocr-correction — 0.34 GB
- basic_function/lora/test_npu_lora_update.py

### philschmid/code-llama-3-1-8b-text-to-sql-lora — 4.79 GB
- basic_function/lora/test_npu_lora_update.py

### rednote-hilab/dots.ocr — 6.09 GB
- vlm_models/test_npu_dots_ocr.py

### sgl-npu/MiniMax-M2.5-eagel-model-0318 — 2.68 GB
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms_gpqa.py
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_8p_in3k5_out1k5_50ms_gpqa.py

### sglang-EAGLE3-LLaMA3.1-Instruct-8B — 未公开(内部/私有仓库)
- basic_function/optimization_debug_options/test_npu_openai_server_hidden_states.py
- basic_function/pd_disaggregation/test_npu_disaggregation_basic.py
- basic_function/speculative_inference/test_npu_eagle_constrained_decoding.py
- basic_function/speculative_inference/test_npu_spec_eagle.py
- basic_function/speculative_inference/test_npu_spec_eagle_parity.py
- basic_function/speculative_inference/test_npu_spec_eagle_stress.py

### stepfun-ai/Step3-VL-10B — 20.36 GB
- vlm_models/test_npu_step3_vl_10b.py

### suayptalha/FastLlama-3.2-LoRA — 0.06 GB
- basic_function/lora/test_npu_lora_basic.py
- basic_function/lora/test_npu_lora_memory_eviction.py
- basic_function/lora/test_npu_lora_openai_compatible_supplement.py
- basic_function/lora/test_npu_wait_threshold.py

### vllm-ascend/DeepSeek-R1-0528-W8A8 — 701.69 GB
- basic_function/HiCache/test_npu_hierarchical_cache_mla.py
- basic_function/parallel_strategy/data_parallelism/test_npu_load_balance_method.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep.py
- basic_function/speculative_inference/test_npu_speculative_moe_a2a_backend.py

### vllm-ascend/DeepSeek-V2-Lite-W8A8 — 17.22 GB
- basic_function/HiCache/test_npu_hicache_mla.py
- basic_function/dp_attn/test_npu_dp_attention.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v2.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v2.py
- basic_function/runtime_opts/test_npu_mla_fia_w8a8int8.py
- basic_function/runtime_opts/test_npu_mla_w8a8int8.py

### vllm-ascend/DeepSeek-V3.2-W8A8 — 694.47 GB
- basic_function/cp/test_npu_cp_vs_nocp_ttft.py
- basic_function/optimization_debug_options/test_npu_enable_return_routed_experts.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_deepseek_v3_2_w8a8.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_deepseek_v3_2_w8a8.py
- llm_models/test_npu_deepseek_v32_indexcache.py
- llm_models/test_npu_deepseek_v3_2_w8a8.py

### vllm-ascend/QWQ-32B-W8A8 — 43.44 GB
- llm_models/test_npu_qwq_32b_w8a8.py

### vllm-ascend/Qwen3-235B-A22B-W8A8 — 236.8 GB
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_auto_qwen3_235b_a22b_w8a8.py
- basic_function/parallel_strategy/expert_parallelism/test_npu_deepep_low_latency_qwen3_235b_a22b_w8a8.py
- llm_models/test_npu_qwen3_235b_a22b_w8a8.py

### vllm-ascend/Qwen3-30B-A3B-W8A8 — 31.29 GB
- accuracy/qwen3_30b_a3b/test_npu_qwen3_30b_w8a8_1p_in3k5_out1k5_50ms_aime25.py

### vllm-ascend/Qwen3-Next-80B-A3B-Instruct-W8A8 — 84.9 GB
- accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py

### yzgjhdxf/GLM-5-top64-pruned-gsm8k — 420.41 GB
- accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py

### z-lab/Qwen3-8B-DFlash-b16 — 2.1 GB
- basic_function/speculative_inference/test_npu_dflash_speculative.py

## 二、数据集 -> 使用测试脚本

### [ds]audios/bird.mp3
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py

### [ds]audios/trump.mp3
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py

### [ds]gsm8k_deepseekv4/cache0_32000/formal_run1_64_32000_cache0.json
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py

### [ds]gsm8k_deepseekv4/cache0_8000/formal_run1_160_8000_cache0.json
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py

### [ds]images/023.jpg
- rerank_models/test_npu_qwen3_vl_reranker_2b.py

### [ds]images/1x1.png
- basic_function/pp/test_npu_pp_single_node_extra.py

### [ds]images/example_image.png
- basic_function/dp_attn/test_npu_dp_attention.py
- basic_function/runtime_options/test_npu_skip_tokenizer_init.py

### [ds]images/invoice_with_barcode_logo.jpeg
- basic_function/prefix_mm_cache/test_npu_prefix_mm_cache.py
- vlm_models/test_npu_dots_ocr.py

### [ds]images/logo.png
- basic_function/Multi-Modal/test_npu_mm_limit.py
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py

### [ds]images/man.png
- basic_function/Multi-Modal/test_npu_mm_limit.py
- basic_function/optimization_debug_options/test_npu_embedding_interpolation.py
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py

### [ds]images/man_ironing_on_back_of_suv.png
- vlm_models/test_npu_vision_openai_server_a.py
- vlm_models/test_npu_vlm_input_format.py

### [ds]images/sgl_logo.png
- vlm_models/test_npu_vlm_input_format.py

### [ds]openslr/librispeech_asr
- vlm_models/test_npu_qwen3_asr.py

### [ds]video/audios_Trump_WEF_2018_10s.mp3
- basic_function/openai_server/test_npu_serving_transcription.py

### [ds]video/jobs.mp4
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py

### [ds]wav/asr_en.wav
- basic_function/api_related/test_npu_api_related_asr_max.py

### aisbench-type:gsm8k
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in8k_out1k_50ms.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_16p_in3k5_out1k5_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in128k_out1k_20ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in16k_out1k_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_20ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in128k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in16k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in254k_out1k.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_2p_in984k_out1k.py

### aisbench-type:mm-custom-gen
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1080p_30_out256_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1080p_30_out256_50ms.py

### aisbench:generated-shared-prefix
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in65k_out1k5_prefix90_25ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_prefix90_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_2p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in128k_out1k_prefix90_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms.py

### aisbench:image
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_1p_in1080p_30_out256_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1024x1024_30_out1024_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in1080p_30_out256_50ms.py

### aisbench:random
- basic_function/cp/test_npu_cp_vs_nocp_ttft.py
- basic_function/parallel_strategy/test_npu_bucket_adjust_interval_secs_concurrency.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_1p1d_16p_in8k_out1k_50ms.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in32k_out1k_50ms.py
- performance/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_in8k_out1k_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_16p_in3k5_out1k5_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in128k_out1k_20ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in16k_out1k_50ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_20ms.py
- performance/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms.py
- performance/glm5_2/test_npu_glm_5_2_w4a8_2p1d_32p_in128k_out1k_prefix90_20ms.py
- performance/glm5_2/test_npu_glm_5_2_w4a8_2p1d_32p_in64k_out1k_prefix90_20ms.py
- performance/glm5_2/test_npu_glm_5_2_w4a8_3p1d_32p_in16k_out1k_50ms.py
- performance/glm5_2/test_npu_glm_5_2_w4a8_4p1d_48p_in128k_out1k_prefix90_50ms.py
- performance/glm5_2/test_npu_glm_5_2_w4a8_4p1d_48p_in64k_out1k_prefix90_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in128k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in16k_out1k_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in3k5_out1k5_50ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_20ms.py
- performance/qwen3_5_397b/test_npu_qwen3_5_397b_w4a8_8p_in64k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in64k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in128k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in16k_out1k_50ms.py
- performance/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_2p_in64k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in128k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in254k_out1k.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in3k5_out1k5_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_50ms.py
- performance/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_2p_in984k_out1k.py

### evalscope:aime25
- accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_aime25.py
- accuracy/kimi_k2_6/test_npu_kimi_k2_6_w4a8_16p_in64k_out1k_100ms_aime25.py
- accuracy/qwen3_30b_a3b/test_npu_qwen3_30b_w8a8_1p_in3k5_out1k5_50ms_aime25.py
- accuracy/qwen3_next_80b_a3b_instruct/test_npu_qwen3_next_80b_w8a8_2p_in6k_out1k5_bs16_aime25.py

### evalscope:aime26
- accuracy/glm5_1/test_npu_glm5_1_w4a8_1p1d_32p_in64k_out1k_50ms_aime26.py
- accuracy/qwen3_5_397b/test_npu_qwen3_5_397b_8p_aime26.py
- accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_aime26.py
- accuracy/qwen3_6_35b_a3b/test_npu_qwen3_6_35b_a3b_1p_in64k_out1k_prefix90_50ms_aime26.py

### evalscope:gpqa_diamond
- accuracy/deepseek_v4_flash/test_npu_deepseek_v4_flash_w8a8_8p_gpqa.py
- accuracy/glm5_2/test_npu_glm_5_2_w4a8_8p_gpqa.py
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_4p_in64k_out1k_prefix90_50ms_gpqa.py
- accuracy/minimax_m2_5/test_npu_minimax_m2_5_w8a8_8p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3-8b/test_npu_qwen3_8b_w8a8_1p_in6k_out1k5_bs16_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_bf16_8p_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa.py
- accuracy/qwen3_32b/test_npu_qwen3_32b_w8a8_2p_in3k5_out1k5_50ms_gpqa_a2.py
- accuracy/qwen3_5_397b/test_npu_qwen3_5_397b_8p_gpqa.py
- accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_1p_gpqa.py
- accuracy/qwen3_6_27b/test_npu_qwen3_6_27b_w8a8_1p_in3k5_out1k5_50ms_gpqa.py

### evalscope:gsm8k
- accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_aime25.py
- accuracy/deepseek_v3_2/test_npu_deepseek_v3_2_8p_gsm8k.py
- accuracy/glm4_7_flash/test_npu_glm4_7_flash_1p_gsm8k.py
- accuracy/glm5_top64_pruned/test_npu_glm5_top64_pruned_bf16_8p_gsm8k.py
- accuracy/moonshotai_moonlight_16b_a3b/test_npu_moonlight_16b_a3b_bf16_1p_gsm8k.py
- accuracy/qwen3_5_9b/test_npu_qwen3_5_9b_bf16_1p_gsm8k.py
- accuracy/qwen3_vl_30b_a3b/test_npu_qwen3_vl_30b_a3b_bf16_2p_gsm8k.py
- accuracy/qwen3_vl_8b/test_npu_qwen3_vl_8b_bf16_2p_gsm8k.py

### evalscope:mmmu
- accuracy/glm4_6v_flash/test_npu_glm4_6v_flash_1p_mmmu.py
- accuracy/qwen3_omni_30b_a3b_thinking/test_npu_qwen3_omni_30b_a3b_thinking_1p_mmmu.py
- accuracy/qwen3_vl_30b_a3b_thinking/test_npu_qwen3_vl_30b_a3b_thinking_1p_mmmu.py
- accuracy/qwen3_vl_8b_thinking/test_npu_qwen3_vl_8b_thinking_1p_mmmu.py

## 三、其他仓库ID/特殊引用（运行时从 HF/ModelScope 拉取或特殊用途）

### Qwen/Qwen2-0.5B-Instruct
- basic_function/runtime_options/test_npu_download_dir.py

### RedHatAI/Qwen2.5-0.5B-Instruct-quantized.w8a8
- basic_function/quant/test_npu_w8a8_quantization.py

### default
- basic_function/Multi-Modal/test_npu_multimodal_basic.py
- basic_function/Multi-Modal/test_npu_multimodal_chat_completions.py
- basic_function/Multi-Modal/test_npu_multimodal_dp_attention.py
- basic_function/Multi-Modal/test_npu_multimodal_reasoning_parser.py
- basic_function/Multi-Modal/test_npu_multimodal_tool_call.py
- basic_function/dp_attn/test_npu_dp_attention.py
- basic_function/optimization_debug_options/test_npu_embedding_interpolation.py
- vlm_models/test_npu_qwen3_asr.py
- vlm_models/test_npu_qwen3_omni_30b_a3b_instruct.py
- vlm_models/test_npu_vision_openai_server_a.py

### dots_ocr
- vlm_models/test_npu_dots_ocr.py

### dummy
- basic_function/pd_disaggregation/test_npu_disaggregation_basic.py

### meta-llama/Llama-3.1-8B-Instruct
- basic_function/openai_server/test_npu_openai_server.py

### qwen3-asr
- basic_function/api_related/test_npu_api_related_asr_max.py

### whisper
- basic_function/openai_server/test_npu_serving_transcription.py
