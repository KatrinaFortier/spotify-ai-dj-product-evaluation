import pandas as pd
from scipy import stats


def summarize_ab_test(sessions):
    ab_summary = (
        sessions
        .groupby("assignment_group")
        .agg(
            users=("user_id", "nunique"),
            sessions=("session_id", "count"),
            avg_session_duration=("duration_min", "mean"),
            session_30min_rate=("continued_30min", "mean"),
            save_rate=("save_rate", "mean"),
            post_search_rate=("post_search_flag", "mean"),
            avg_recommendation_diversity=("recommendation_diversity_score", "mean"),
        )
        .reset_index()
    )

    return ab_summary


def test_session_duration_and_search_behavior(sessions):
    control = sessions[sessions["assignment_group"] == "control_standard_recs"]
    treatment = sessions[sessions["assignment_group"] == "treatment_ai_dj"]

    duration_test = stats.ttest_ind(
        treatment["duration_min"],
        control["duration_min"],
        equal_var=False,
    )

    search_table = pd.crosstab(
        sessions["assignment_group"],
        sessions["post_search_flag"],
    )

    chi2, p_value, dof, expected = stats.chi2_contingency(search_table)

    search_test = {
        "chi2": chi2,
        "p_value": p_value,
        "dof": dof,
    }

    return duration_test, search_test
