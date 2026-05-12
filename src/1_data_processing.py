import pandas as pd
import numpy as np

DATA_DIR = "../data"


def load_data(data_dir=DATA_DIR):
    sessions = pd.read_csv(f"{data_dir}/session_listening_behavior.csv")
    searches = pd.read_csv(f"{data_dir}/post_interaction_search_behavior.csv")
    retention = pd.read_csv(f"{data_dir}/retention_outcomes.csv")
    discovery = pd.read_csv(f"{data_dir}/artist_discovery_outcomes.csv")
    prompts = pd.read_csv(f"{data_dir}/prompt_voice_request_logs.csv")

    return sessions, searches, retention, discovery, prompts


def prepare_session_metrics(sessions):
    sessions = sessions.copy()

    sessions["save_rate"] = sessions["saves"] / sessions["tracks_played"].replace(0, np.nan)
    sessions["skip_rate"] = sessions["skips_30s"] / sessions["tracks_played"].replace(0, np.nan)
    sessions["post_search_flag"] = sessions["exited_to_search"].astype(int)

    return sessions
