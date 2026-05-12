def compare_listener_cohorts(sessions):
    cohort = (
        sessions
        .groupby(["assignment_group", "listener_cohort"])
        .agg(
            sessions=("session_id", "count"),
            avg_duration=("duration_min", "mean"),
            post_search_rate=("post_search_flag", "mean"),
            avg_override=("recommendation_override_count", "mean"),
            diversity=("recommendation_diversity_score", "mean"),
            save_rate=("save_rate", "mean"),
        )
        .reset_index()
    )

    return cohort
