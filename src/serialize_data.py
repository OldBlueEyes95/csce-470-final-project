import pandas as pd
from typing import Dict

# Folder for storing data
DATA_FOLDER: str = "data/"

# Define field names dynamically
FIELDS = ["title", "body"]  # Add or remove fields as needed

# Paths for TF and TF-IDF data files
TF_FILE_NAME = "tf_matrix"
TF_IDF_FILE_NAME = "tf_idf_matrix"

# Helper function to generate file paths for each field and data type
def generate_file_paths(fields: list, data_type: str) -> Dict[str, str]:
    return {field: f"{DATA_FOLDER}{field}_{data_type}.pkl" for field in fields}

# File paths for TF and TF-IDF data
TF_PATHS = generate_file_paths(FIELDS, TF_FILE_NAME)
TF_IDF_PATHS = generate_file_paths(FIELDS, TF_IDF_FILE_NAME)

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

