from data_processing import load_data, prepare_session_metrics
from ab_test_analysis import summarize_ab_test, test_session_duration_and_search_behavior
from post_search_analysis import analyze_post_search_categories
from retention_modeling import model_retention
from cohort_analysis import compare_listener_cohorts
from signal_detection import detect_post_search_behavior_shifts
from prompt_evaluation import evaluate_prompt_response_quality


def main():
    sessions, searches, retention, discovery, prompts = load_data()
    sessions = prepare_session_metrics(sessions)

    ab_summary = summarize_ab_test(sessions)
    duration_test, search_test = test_session_duration_and_search_behavior(sessions)

    search_mix = analyze_post_search_categories(searches)

    retention_coefficients, retention_auc = model_retention(retention)

    cohort_summary = compare_listener_cohorts(sessions)

    daily_signals, signal_alerts = detect_post_search_behavior_shifts(sessions)

    prompt_eval = evaluate_prompt_response_quality(prompts)

    print("\nA/B summary")
    print(ab_summary)

    print("\nWelch t-test for session duration")
    print(duration_test)

    print("\nChi-square test for post-search behavior")
    print(search_test)

    print("\nPost-interaction search category summary")
    print(search_mix)

    print("\nRetention model coefficients")
    print(retention_coefficients)

    print("\nModel AUC:", retention_auc)

    print("\nCohort analysis")
    print(cohort_summary)

    print("\nSignal detection alerts")
    print(signal_alerts)

    print("\nPrompt-response evaluation")
    print(prompt_eval)


if __name__ == "__main__":
    main()
