# Spotify AI DJ Mock Product Evaluation Dataset

This folder contains synthetic CSV datasets, SQL examples, Python analysis code, and portfolio-ready graphics for a mock product evaluation case study.

## Important Disclaimer

All datasets, metrics, charts, results, and modeled outputs are fully synthetic and created only to demonstrate experimental design, analytical methodology, product evaluation thinking, behavioral analytics workflows, and recommendation-system evaluation. These files do not contain internal Spotify data and do not represent real Spotify reporting.

## Case Study Focus

Research question:
What do listeners search for immediately after exiting conversational recommendation environments like Spotify AI DJ, and what do those post-interaction behaviors reveal about unmet listener intent, recommendation-system gaps, personalization limitations, and emotional mismatch within AI-guided music experiences?

## Synthetic CSV Datasets

1. `user_assignment.csv`
   - User-level randomized assignment table.
   - Includes treatment/control group, listener cohort, market, device, and baseline behavior.

2. `session_listening_behavior.csv`
   - Session-level listening behavior.
   - Includes duration, skips, saves, playlist adds, artist follows, diversity score, override count, and post-session search flag.

3. `post_interaction_search_behavior.csv`
   - Search behavior immediately after recommendation interaction.
   - Includes search category, specificity score, and downstream conversion signals.

4. `prompt_voice_request_logs.csv`
   - Treatment-group prompt and voice request interaction logs.
   - Includes prompt type, success flag, reformulation flag, coherence score, and latency.

5. `retention_outcomes.csv`
   - User-level retention outcomes for day 7, day 14, and day 28.

6. `artist_discovery_outcomes.csv`
   - Artist discovery and conversion signals.
   - Includes new artist exposure, follows, saves, playlist adds, and discovery quality index.

7. `final_model_ready_dataset.csv`
   - Joined analytical table for modeling and feature evaluation.

## Mock Data Pipeline

Raw event logs:
- user assignment
- sessions
- searches
- prompts
- retention
- artist discovery

Cleaning steps:
- standardize event-level identifiers
- join user/session/search/prompt tables
- handle null prompt/search fields
- derive session-level behavioral features

Metric calculations:
- save rate
- skip rate
- artist-follow rate
- post-session search frequency
- 30-minute continuation rate
- recommendation diversity score
- prompt success and reformulation rates

Joined analytical table:
- `final_model_ready_dataset.csv`

Model-ready outputs:
- `analysis_ab_test_summary.csv`
- `analysis_statistical_tests.csv`
- `analysis_retention_model_coefficients.csv`
- `analysis_cohort_summary.csv`
- `analysis_signal_detection_daily.csv`
- `analysis_recommendation_system_evaluation.csv`

## Code

- `code/spotify_ai_dj_mock_sql_examples.sql`
- `code/spotify_ai_dj_mock_python_analysis.py`

## Portfolio Graphics

- `ab_test_results_dashboard.png`
- `post_interaction_search_map.png`
- `retention_curve.png`
- `cohort_comparison_table.png`
- `recommendation_gap_signal_chart.png`
- `feature_health_monitoring_dashboard.png`

Generated on: 2026-05-11
