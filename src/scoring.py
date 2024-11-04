from typing import List, Tuple
import numpy as np
import pandas as pd
from index import tokenize
from collections import Counter

from serialize_data import retrieve_tf_data, retrieve_tf_idf_data, retrieve_avg_lengths, FIELDS


field_tf_frames: dict[str, pd.DataFrame]
field_avg_lengths: dict[str, float]
document_titles: list[str]

w = {
    'title': .3,
    'body': .7
}

b = {
    'title': 0.72,
    'body': 0.7
}

k1 = 1.0
pageRankLambda = .9
pageRankLambdaPrime = 2.0


def calculate_idf_for_term(term: str, tf_matrix: pd.DataFrame) -> float:
    N = len(tf_matrix)
    if term in tf_matrix.columns:
        document_frequency = (tf_matrix[term] > 0).sum()
    else:
        document_frequency = 0  # term not known
    
    idf = np.log((N + 1) / (document_frequency + 1)) + 1
    return idf


    
def score_document(query_terms: List[str], document_id: str) -> float:
    """
    Score a document for relevance to the query using BM25.
    :param query_terms: List of terms in the query.
    :param document_id: ID of the document to score.
    :return: BM25 score for the document.
    """
    score = 0.0
    for t in query_terms:
        idf = calculate_idf_for_term(t, field_tf_frames['body'])
        term_score = 0.0

        for f in FIELDS:
            tf_frame = field_tf_frames[f]
            f_avg_len = field_avg_lengths[f]
            tf = tf_frame.at[document_id, t] if t in tf_frame.columns else 0
            doc_length_f = tf_frame.loc[document_id].sum()
            field_score = w[f] * (tf * (k1 + 1)) / (tf + k1 * (1 - b[f] + b[f] * (doc_length_f / f_avg_len)))
            term_score += field_score

        score += idf * term_score
    
    return score
        


def rank_documents(query: str) -> List[Tuple[str, float]]:
    """
    Rank all documents based on their relevance to the query.
    
    :param query: The search query as a string.
    :return: A list of tuples where each tuple contains a document ID and its score,
             sorted by score in descending order.
    """
    query_terms = tokenize(query)
    document_scores = []

    # score for each document
    for doc_id in document_titles:
        score = score_document(query_terms, doc_id)
        document_scores.append((doc_id, score))

    # descending order sort
    ranked_documents = sorted(document_scores, key=lambda x: x[1], reverse=True)

    return ranked_documents


def load_data():
    global field_tf_frames
    global field_avg_lengths
    global document_titles
    field_tf_frames = retrieve_tf_data()
    field_avg_lengths = retrieve_avg_lengths()
    document_titles = list(field_tf_frames['title'].index)


def main():
    load_data()
    print('top five from query "wolf":')
    print(rank_documents('wolf')[:5])
    

if __name__ == "__main__":
    main()
