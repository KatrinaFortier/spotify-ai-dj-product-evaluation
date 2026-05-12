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
