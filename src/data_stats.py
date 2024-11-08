import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Tuple

from serialize_data import retrieve_tf_data

STATS_FILE: str = "stats/basic_stats.txt"

def main() -> None:
    tf_fields_dict = retrieve_tf_data()
    title_frame = tf_fields_dict["title"]
    body_frame = tf_fields_dict["body"]
    top_terms_histogram(title_frame, body_frame)
    doc_length_chart(body_frame)
    
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


def top_terms_histogram(title_frame: pd.DataFrame, body_frame: pd.DataFrame) -> None:
    title_term_sums = title_frame.sum(axis=0)
    body_term_sums = body_frame.sum(axis=0)
    title_top_5 = title_term_sums.nlargest(5)
    body_top_5 = body_term_sums.nlargest(5)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    ax1.bar(title_top_5.index, title_top_5.values, color='blue')
    ax1.set_title('Top 5 Common Words in Title', fontsize=16)
    ax1.set_xlabel('Words', fontsize=14)
    ax1.set_ylabel('Frequency', fontsize=14)
    ax1.tick_params(axis='both', which='major', labelsize=14)
    
    ax2.bar(body_top_5.index, body_top_5.values, color='green')
    ax2.set_title('Top 5 Common Words in Body', fontsize=16)
    ax2.set_xlabel('Words', fontsize=14)
    ax2.tick_params(axis='both', which='major', labelsize=14)
    
    plt.tight_layout()
    plt.savefig('stats/top_words_histogram.png')


def doc_length_chart(body_frame: pd.DataFrame) -> None:
    body_doc_lengths = body_frame.sum(axis=1)
    median_length = body_doc_lengths.median()
    
    fig, ax = plt.subplots(figsize=(7, 4))
    ax.hist(body_doc_lengths, bins=100, color='green', alpha=0.7)
    
    ax.axvline(median_length, color='red', linestyle='dashed', linewidth=2, label=f'Median: {median_length:.2f}')
    ax.set_title('Document Lengths', fontsize=16)
    ax.set_xlabel('Length', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    
    ax.legend(fontsize=12)
    ax.tick_params(axis='both', which='major', labelsize=14)


if __name__ == "__main__":
    main()