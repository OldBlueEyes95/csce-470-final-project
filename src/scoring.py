from typing import List, Tuple
import numpy as np
import pandas as pd
from index import tokenize
# from collections import Counter

from serialize_data import retrieve_tf_data, retrieve_tf_idf_data, retrieve_avg_lengths, FIELDS


field_tf_frames:   dict[str, pd.DataFrame]
field_avg_lengths: dict[str, float]
document_titles:   list[str]


k1:                  float = 1.0
pageRankLambda:      float = 0.9
pageRankLambdaPrime: float = 2.0


def calculate_idf_for_term(term: str, tf_matrix: pd.DataFrame) -> float:
    N = len(tf_matrix)
    document_frequency: float = (tf_matrix[term] > 0).sum() if (term in tf_matrix.columns) else 0 # term not known
    
    idf = np.log((N + 1) / (document_frequency + 1)) + 1
    return idf


def score_document(
    query_terms: List[str], 
    document_id: str,
    w_title=0.30, w_body=0.70,
    b_title=0.72, b_body=0.70
) -> float:
    """
    Score a document for relevance to the query using BM25.
    :param query_terms: List of terms in the query.
    :param document_id: ID of the document to score.
    :return: BM25 score for the document.
    """
    
    weight_w = {'title': w_title, 'body': w_body}
    weight_b = {'title': b_title, 'body': b_body}
    
    score: float = 0.0
    for t in query_terms:
        idf: float = calculate_idf_for_term(t, field_tf_frames['body'])
        term_score: float = 0.0
        
        for f in FIELDS:
            tf_frame = field_tf_frames[f]
            f_avg_len = field_avg_lengths[f]
            tf = tf_frame.at[document_id, t] if t in tf_frame.columns else 0
            doc_length_f = tf_frame.loc[document_id].sum()
            field_score = weight_w[f] * (tf * (k1 + 1)) / (tf + k1 * (1 - weight_b[f] + weight_b[f] * (doc_length_f / f_avg_len)))
            term_score += field_score
        
        score += idf * term_score
    
    return score


def rank_documents(
    query: str,
    w_title=0.30, w_body=0.70,
    b_title=0.72, b_body=0.70
) -> List[Tuple[str, float]]:
    """
    Rank all documents based on their relevance to the query.
    
    :param query: The search query as a string.
    :return: A list of tuples where each tuple contains a document ID and its score,
             sorted by score in descending order.
    """
    query_terms = tokenize(query)
    
    # score for each document
    document_scores = [
        (
            doc_id, 
            score_document(query_terms, doc_id, w_title=w_title, w_body=w_body, b_title=b_title, b_body=b_body)
        )
        for doc_id in document_titles
    ]
    
    # descending order sort
    return sorted(document_scores, key=lambda x: x[1], reverse=True)


def load_data() -> None:
    global field_tf_frames
    global field_avg_lengths
    global document_titles
    
    field_tf_frames   = retrieve_tf_data()
    field_avg_lengths = retrieve_avg_lengths()
    document_titles   = list(field_tf_frames['title'].index)


def main() -> None:
    load_data()
    
    n: int = 5
    assert n > 1, "`n` must be an integer greater than 1."
    
    query: str = "wolf"
    
    print(f"top {n} from query '{query}':")
    print(rank_documents(query)[:n])


if __name__ == "__main__":
    main()
