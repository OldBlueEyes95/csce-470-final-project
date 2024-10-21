import pandas as pd
from typing import Tuple

DATA_FOLDER: str = "data/"
DATA_FILE_NAME: str = "tf_matrix"
CANON_TITLE_PATH: str = DATA_FOLDER + "title_" + DATA_FILE_NAME + ".pkl"
CANON_BODY_PATH:  str = DATA_FOLDER + "body_"  + DATA_FILE_NAME + ".pkl"

def store_data(title_frame: pd.DataFrame, body_frame: pd.DataFrame) -> None:
    title_frame.to_pickle(DATA_FOLDER + "title_" + DATA_FILE_NAME + ".pkl")
    body_frame.to_pickle(DATA_FOLDER + "body_" + DATA_FILE_NAME + ".pkl")
    
    print(f"TF vectors saved to data/body_tf_matrix and data/title_tf_matrix.pkl")

def retrieve_data(title_path: str=CANON_TITLE_PATH, body_path: str=CANON_BODY_PATH) -> Tuple[pd.DataFrame, pd.DataFrame]:
    title_frame = pd.read_pickle(title_path)
    body_frame = pd.read_pickle(body_path)
    return title_frame, body_frame