from typing import *
from math import log2, log10, log

def raw_term_frequency(word: str, document: str, scaled=True) -> int: # TF
    return document.count(word)

def scaled_term_frequency(word: str, document: str, scaled=True) -> float:
    tf = raw_term_frequency(word, document)
    return 1 + log2(tf) if (tf > 0) else 0.0

def inverse_document_frequency(word: str, all_docs: List[str]) -> float: # IDF
    assert all_docs, "Length of `all_docs` must be greater than 0."
    return log2( len(all_docs) / len({d for d in all_docs if d.find(word) != -1}) )

def tf_idf(word: str, document: str, all_docs: List[str]) -> float: # TF-IDF
    return scaled_term_frequency(word, document) * inverse_document_frequency(word, all_docs)

def NDCG(relevances: List[float]) -> float: # Normalized Discounted Cumulative Gain
    DCG:  float = sum([(2**rel - 1)/(log2(i + 1)) for i, rel in enumerate(relevances, start=1)])
    IDCG: float = sum([(2**rel - 1)/(log2(i + 1)) for i, rel in enumerate(sorted(relevances, reverse=True), start=1)])
    return DCG / IDCG if IDCG > 0 else 0

def precision_at_k(relevances: List[float], k: int) -> float:
    assert k >= 1, "`k` must be a natural number."
    is_relevant_up_to_k: List[bool] = [bool(r) for r in relevances[:k]]
    return sum(is_relevant_up_to_k) / k # boolean average over k terms

def average_precision_at_k(relevances: List[float], k: int) -> float:
    precisions_at_k: List[float] = [precision_at_k(relevances, k_i) for k_i, rel in enumerate(relevances[:k], start=1) if rel != 0]
    return sum(precisions_at_k) / len(precisions_at_k) if (len(precisions_at_k) != 0) else 0.0 # skip precision when relevance at position is 0

def mean_average_precision_at_k(query_relevances: List[List[float]], k: int) -> float:
    # average across queries; same as AP@K if only a single query
    average_precisions_at_k: List[float] = [average_precision_at_k(query_rel, k) for query_rel in query_relevances]
    return sum(average_precisions_at_k) / len(average_precisions_at_k) # mean (average)

if __name__ == '__main__':
    rs: List[int] = [1, 0, 2, 3, 0, 0]
    print(NDCG(rs))