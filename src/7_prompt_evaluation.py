def evaluate_prompt_response_quality(prompts):
    prompt_eval = (
        prompts
        .groupby("prompt_type")
        .agg(
            prompt_count=("prompt_id", "count"),
            success_rate=("prompt_success_flag", "mean"),
            reformulation_rate=("prompt_reformulated_flag", "mean"),
            coherence=("prompt_response_coherence_score", "mean"),
            latency_ms=("latency_ms", "mean"),
        )
        .reset_index()
        .sort_values("success_rate")
    )

    return prompt_eval
