import numpy as np
import pandas as pd
from collections import Counter
from bs4 import BeautifulSoup
import re
from nltk.corpus import stopwords
from typing import Tuple, Set, List

from serialize_data import store_tf_data, store_tf_idf_data

STOP_WORDS: Set[str] = set(stopwords.words('english'))


def tokenize(text: str) -> List:
    tokens = re.findall(r'\b\w+\b', text.lower())
    filtered_tokens = [
        token for token in tokens 
        if token not in STOP_WORDS
        and len(token) > 2
        and not token.isdigit()
        and not re.match(r'^\d+[\w]*$', token)
    ]
    return filtered_tokens


def generate_tf_vectors(xml_file_path: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'lxml')
    
    pages = soup.find_all('page')
    all_body_tf = []
    all_title_tf = []
    page_titles = []
    
    for page in pages:
        title = page.find('title').text
        text = page.find('text').text if page.find('text') else ""
        page_titles.append(title)
        
        title_tokens = tokenize(title)
        body_tokens = tokenize(text)
        title_tf = Counter(title_tokens)
        body_tf = Counter(body_tokens)
        all_title_tf.append(title_tf)
        all_body_tf.append(body_tf)
        
    print(page_titles)
    
    # Make the matrix with all unique terms for column headers.
    unique_title_terms = set()
    for tf_row in all_title_tf:
        unique_title_terms.update(tf_row.keys())
    unique_title_terms = sorted(unique_title_terms)
    
    unique_body_terms = set()
    for tf_row in all_body_tf:
        unique_body_terms.update(tf_row.keys())
    unique_body_terms = sorted(unique_body_terms)
    
    title_tf_matrix = pd.DataFrame(0, index=page_titles, columns=unique_title_terms)
    body_tf_matrix  = pd.DataFrame(0, index=page_titles, columns=unique_body_terms)
    
    # Populate the DataFrames with term frequencies
    for (tf_matrix, tf_rows) in [(title_tf_matrix, all_title_tf), (body_tf_matrix, all_body_tf)]:
        for idx in range(len(tf_rows)):
            curr_title = page_titles[idx]
            tf_row = tf_rows[idx]
            for term, count in tf_row.items():
                tf_matrix.at[curr_title, term] = count
    
    return (title_tf_matrix, body_tf_matrix)


def calculate_tf_idf_matrices(title_tf_matrix: pd.DataFrame, body_tf_matrix: pd.DataFrame) -> Tuple[pd.DataFrame, pd.DataFrame]:
    def calculate_idf(tf_matrix: pd.DataFrame) -> pd.Series:
        N = len(tf_matrix)
        document_frequency = (tf_matrix > 0).sum(axis=0)
        idf = np.log((N + 1) / (document_frequency + 1)) + 1
        return idf

    # Calculate IDF for both title and body terms
    title_idf = calculate_idf(title_tf_matrix)
    body_idf = calculate_idf(body_tf_matrix)

    # Multiply each term's TF by its IDF to get the TF-IDF
    title_tf_idf_matrix = title_tf_matrix * title_idf
    body_tf_idf_matrix = body_tf_matrix * body_idf
    
    print(title_tf_idf_matrix["wolf"].sort_values(ascending=False))
    # print(title_tf_idf_matrix["wolf"]["Wolf"])

    return title_tf_idf_matrix, body_tf_idf_matrix



def main() -> None:
    xml_file_path = "data/pages_export.xml"
    
    title_tf_matrix, body_tf_matrix = generate_tf_vectors(xml_file_path)
    title_tf_idf_matrix, body_tf_idf_matrix = calculate_tf_idf_matrices(title_tf_matrix, body_tf_matrix)
    store_tf_data({"title": title_tf_idf_matrix, "body": body_tf_idf_matrix})
    store_tf_idf_data({"title": title_tf_idf_matrix, "body": body_tf_idf_matrix})


if __name__ == "__main__":
    main()
    