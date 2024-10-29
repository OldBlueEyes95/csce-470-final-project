import pandas as pd
from typing import List, Tuple

from serialize_data import retrieve_data

STATS_FILE: str = "stats/basic_stats.txt"

def main() -> None:
    title_frame, body_frame = retrieve_data()
    
    number_of_files = len(title_frame.axes[0])
    
    print(number_of_files)
    
    title_common_words: List[str, float] = [
        (field, title_frame[field].sum())
        for field in title_frame.columns
    ]
    title_common_words.sort(key=(lambda x: x[-1]))
    
    
    body_common_words: List[str, float] = [
        (field, body_frame[field].sum())
        for field in body_frame.columns
    ]
    body_common_words.sort(key=(lambda x: x[-1]))
    
    
    # print(title_frame.dtypes, body_frame.dtypes, sep='\n\n\n')
    with open(STATS_FILE, mode='w+', encoding='utf8') as stats_file:
        # for field in title_frame.columns:
            # stats_file.write(f"`{field}`: `{title_frame[field].mean()}`.\n")
        stats_file.write("==== TITLE WORD COUNTS ====\n")
        
        for word, average in title_common_words:
            stats_file.write(f"`{word}`: `{average}`.\n")
        
        stats_file.write("\n\n\n==== BODY WORD COUNTS ====\n")
        
        for word, average in body_common_words:
            stats_file.write(f"`{word}`: `{average}`.\n")

if __name__ == "__main__":
    main()