import pandas as pd
from typing import Tuple

from serialize_data import retrieve_data

def main() -> None:
    title_frame, body_frame = retrieve_data()
    
    print(title_frame.dtypes, body_frame.dtypes, sep='\n\n\n')
    

if __name__ == "__main__":
    main()