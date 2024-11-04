import json
import pandas as pd
from typing import Dict

# Folder for storing data
DATA_FOLDER: str = "data/"

# Define field names dynamically
FIELDS = ["title", "body"]  # Add or remove fields as needed

# Paths data files
TF_FILE_NAME = "tf_matrix"
TF_IDF_FILE_NAME = "tf_idf_matrix"
AVG_LEN_FILE_NAME = "avg_length_dict"

# Helper function to generate file paths for each field and data type
def generate_file_paths(fields: list, data_type: str) -> Dict[str, str]:
    return {field: f"{DATA_FOLDER}{field}_{data_type}.pkl" for field in fields}

# File paths for TF and TF-IDF data
TF_PATHS = generate_file_paths(FIELDS, TF_FILE_NAME)
TF_IDF_PATHS = generate_file_paths(FIELDS, TF_IDF_FILE_NAME)
AVG_LEN_PATH = f"{DATA_FOLDER}{AVG_LEN_FILE_NAME}.json"


# Store TF data
def store_tf_data(tf_data_frames: Dict[str, pd.DataFrame]) -> None:
    for field, df in tf_data_frames.items():
        df.to_pickle(TF_PATHS[field])
        print(f"TF data for '{field}' saved to {TF_PATHS[field]}")


# Store TF-IDF data
def store_tf_idf_data(tf_idf_data_frames: Dict[str, pd.DataFrame]) -> None:
    for field, df in tf_idf_data_frames.items():
        df.to_pickle(TF_IDF_PATHS[field])
        print(f"TF-IDF data for '{field}' saved to {TF_IDF_PATHS[field]}")
        

# Store average lengths as JSON
def store_avg_lengths(avg_lengths_data_frames: Dict[str, float]) -> None:
    with open(AVG_LEN_PATH, "w") as f:
        json.dump(avg_lengths_data_frames, f)
    print(f"Average lengths saved to {AVG_LEN_PATH}")


# Retrieve TF data
def retrieve_tf_data() -> Dict[str, pd.DataFrame]:
    tf_data_frames = {}
    for field, path in TF_PATHS.items():
        tf_data_frames[field] = pd.read_pickle(path)
    return tf_data_frames


# Retrieve TF-IDF data
def retrieve_tf_idf_data() -> Dict[str, pd.DataFrame]:
    tf_idf_data_frames = {}
    for field, path in TF_IDF_PATHS.items():
        tf_idf_data_frames[field] = pd.read_pickle(path)
    return tf_idf_data_frames


# Retrieve average lengths from JSON
def retrieve_avg_lengths() -> Dict[str, float]:
    with open(AVG_LEN_PATH, "r") as f:
        avg_lengths_data_frames = json.load(f)
    print(f"Average lengths loaded from {AVG_LEN_PATH}")
    return avg_lengths_data_frames
