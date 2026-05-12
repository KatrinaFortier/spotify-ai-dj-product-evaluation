def detect_post_search_behavior_shifts(sessions):
    daily = (
        sessions
        .groupby(["assignment_group", "day_index"])
        .agg(
            post_search_rate=("post_search_flag", "mean"),
            override_rate=("recommendation_override_count", "mean"),
            diversity=("recommendation_diversity_score", "mean"),
        )
        .reset_index()
    )

    baseline = daily[
        (daily["assignment_group"] == "treatment_ai_dj")
        & (daily["day_index"] <= 7)
    ]

    baseline_mean = baseline["post_search_rate"].mean()
    baseline_sd = baseline["post_search_rate"].std()

    daily["post_search_zscore_vs_week1_treatment"] = (
        daily["post_search_rate"] - baseline_mean
    ) / baseline_sd

    alerts = daily[
        (daily["assignment_group"] == "treatment_ai_dj")
        & (daily["post_search_zscore_vs_week1_treatment"] > 2)
    ]

    return daily, alerts
