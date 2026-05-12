def analyze_post_search_categories(searches):
    search_mix = (
        searches
        .groupby(["assignment_group", "search_category"])
        .agg(
            searches=("search_id", "count"),
            avg_specificity=("query_specificity_score", "mean"),
            search_to_play_rate=("search_led_to_play", "mean"),
            search_to_save_rate=("search_led_to_save", "mean"),
        )
        .reset_index()
        .sort_values(["assignment_group", "searches"], ascending=[True, False])
    )

    return search_mix
