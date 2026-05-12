import pandas as pd
import numpy as np
from scipy import stats
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

DATA_DIR = "../data"

sessions = pd.read_csv(f"{DATA_DIR}/session_listening_behavior.csv")
searches = pd.read_csv(f"{DATA_DIR}/post_interaction_search_behavior.csv")
retention = pd.read_csv(f"{DATA_DIR}/retention_outcomes.csv")
discovery = pd.read_csv(f"{DATA_DIR}/artist_discovery_outcomes.csv")
prompts = pd.read_csv(f"{DATA_DIR}/prompt_voice_request_logs.csv")

sessions["save_rate"] = sessions["saves"] / sessions["tracks_played"].replace(0, np.nan)
sessions["skip_rate"] = sessions["skips_30s"] / sessions["tracks_played"].replace(0, np.nan)
sessions["post_search_flag"] = sessions["exited_to_search"].astype(int)

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

print("\nA/B summary")
print(ab_summary)

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

print("\nWelch t-test for session duration")
print(duration_test)

print("\nChi-square test for post-search behavior")
print({"chi2": chi2, "p_value": p_value})

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

print("\nPost-interaction search category summary")
print(search_mix)

retention["treatment_flag"] = (
    retention["assignment_group"] == "treatment_ai_dj"
).astype(int)

features = [
    "treatment_flag",
    "avg_duration_min",
    "post_search_sessions",
    "total_saves",
    "total_new_artists",
    "avg_diversity",
]

X = retention[features]
y = retention["retained_day_28"]

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

pred = model.predict_proba(X)[:, 1]
auc = roc_auc_score(y, pred)

coef = pd.DataFrame({
    "feature": features,
    "coefficient": model.coef_[0],
})

print("\nRetention model coefficients")
print(coef)
print("\nModel AUC:", auc)

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

print("\nCohort analysis")
print(cohort)

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

print("\nSignal detection alerts")
print(alerts)

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

print("\nPrompt-response evaluation")
print(prompt_eval)
