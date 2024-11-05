import os
import csv
from typing import Dict, List, Tuple

from metrics import NDCG, mean_average_precision_at_k
from scoring import load_data, rank_documents


EVAL_PATH: str = "eval_data"

K: int = 10


def parse_csv_to_dict(file_path: str) -> Tuple[Dict[str, Dict[str, float]], Dict[str, List[str]]]:
    """Basic parser developed based on skeleton from ChatGPT"""
    query_scores: Dict[str, Dict[str, float]] = {}
    cirrus_ranking: Dict[str, List[str]] = {}
    
    with open(file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert len(rows) == 21, "Must have 1 header and 20 data rows."
        
        # Extract queries from the first row
        queries = [cell for cell in rows[0] if cell.strip()]
        assert len(queries) > 0, "Must have queries to evaluate."
        
        # Initialize a dictionary for each query
        for query in queries:
            query_scores[query] = {}
            cirrus_ranking[query] = []
        
        # Parse ranked documents and their scores
        for row in rows[1:21]:  # Assumes exactly 20 rows for top results
            for i, query in enumerate(queries):
                # Each query has two columns: document and score
                doc_col = i * 2
                score_col = doc_col + 1
                if doc_col < len(row) and score_col < len(row):
                    document = row[doc_col].strip()
                    
                    cirrus_ranking[query].append(document) #!
                    
                    try:
                        score = float(row[score_col].strip())
                    except ValueError:
                        score = 0.0  # Default to 0 if score isn't a valid float
                    if document:
                        query_scores[query][document] = score
    
    return query_scores, cirrus_ranking


def evaluate(
    w_title=0.30, w_body=0.70,
    b_title=0.72, b_body=0.70,
    step_width: float = 0.05,
    step_count: int = 10,
    show_each_step: bool = False
) -> Tuple[float, float]:
    """Function for testing different weight combinations."""
    
    eval_query_data, cirrus_ranking = parse_csv_to_dict("eval_data/Training - Sheet2.csv")
    
    their_scores: Dict[str, List[float]] = {
        query: [eval_query_data[query].get(doc, 0) for doc in cirrus_ranking[query][:K]] for query in eval_query_data.keys()
    }
    their_NDCGs: float = [NDCG(scores) for scores in their_scores.values()]
    their_avg_NDCG: float = sum(their_NDCGs)/len(their_NDCGs)
    their_MAP: float = mean_average_precision_at_k(their_scores.values(), k=K)
    
    print(f"Cirrus Search (Minecraft Wiki) NDCG: `{their_avg_NDCG}`.")
    print(f"Cirrus Search (Minecraft Wiki) MAP:  `{their_MAP}`.")
    
    our_best_NDCG: float = -float("inf")
    our_best_MAP:  float = -float("inf")
    
    for step in range(-step_count, step_count):
        difference = step * step_width
        
        print(f"\nFor difference of {difference}...\n")
        
        our_scores: Dict[str, List[float]] = {
            query: [
                eval_query_data[query].get(doc, 0) 
                for doc, _ in rank_documents(query, w_title=(w_title + difference), w_body=w_body, b_title=b_title, b_body=b_body)[:K]
            ]
            for query in eval_query_data.keys()
        }
        our_NDCGs:    float = [NDCG(scores) for scores in our_scores.values()]
        our_avg_NDCG: float = sum(our_NDCGs)/len(our_NDCGs)
        our_MAP:      float = mean_average_precision_at_k(our_scores.values(), k=K)
        
        print("Varying the difference over `w_title`...")
        print(f"Query Crafter (our tool) NDCG: `{our_avg_NDCG}`.")
        print(f"Query Crafter (our tool) MAP:  `{  our_MAP}`.")
        
        our_scores: Dict[str, List[float]] = {
            query: [
                eval_query_data[query].get(doc, 0) 
                for doc, _ in rank_documents(query, w_title=w_title, w_body=(w_body + difference), b_title=b_title, b_body=b_body)[:K]
            ]
            for query in eval_query_data.keys()
        }
        our_NDCGs:    float = [NDCG(scores) for scores in our_scores.values()]
        our_avg_NDCG: float = sum(our_NDCGs)/len(our_NDCGs)
        our_MAP:      float = mean_average_precision_at_k(our_scores.values(), k=K)
        
        print("Varying the difference over `w_body`...")
        print(f"Query Crafter (our tool) NDCG: `{our_avg_NDCG}`.")
        print(f"Query Crafter (our tool) MAP:  `{  our_MAP}`.")
        
        our_scores: Dict[str, List[float]] = {
            query: [
                eval_query_data[query].get(doc, 0) 
                for doc, _ in rank_documents(query, w_title=w_title, w_body=w_body, b_title=(b_title + difference), b_body=b_body)[:K]
            ]
            for query in eval_query_data.keys()
        }
        our_NDCGs:    float = [NDCG(scores) for scores in our_scores.values()]
        our_avg_NDCG: float = sum(our_NDCGs)/len(our_NDCGs)
        our_MAP:      float = mean_average_precision_at_k(our_scores.values(), k=K)
        
        print("Varying the difference over `b_title`...")
        print(f"Query Crafter (our tool) NDCG: `{our_avg_NDCG}`.")
        print(f"Query Crafter (our tool) MAP:  `{  our_MAP}`.")
        
        our_scores: Dict[str, List[float]] = {
            query: [
                eval_query_data[query].get(doc, 0) 
                for doc, _ in rank_documents(query, w_title=w_title, w_body=w_body, b_title=b_title, b_body=(b_body + difference))[:K]
            ]
            for query in eval_query_data.keys()
        }
        our_NDCGs:    float = [NDCG(scores) for scores in our_scores.values()]
        our_avg_NDCG: float = sum(our_NDCGs)/len(our_NDCGs)
        our_MAP:      float = mean_average_precision_at_k(our_scores.values(), k=K)
        
        print("Varying the difference over `b_body`...")
        print(f"Query Crafter (our tool) NDCG: `{our_avg_NDCG}`.")
        print(f"Query Crafter (our tool) MAP:  `{  our_MAP}`.")
    
    if show_each_step:
        print("\n=== EVALUATION METRICS ===\n")
        
        print("NDCG (averaged across each test query):\n")
        print(f"Cirrus Search (Minecraft Wiki): `{their_avg_NDCG}`.")
        print(f"Query Crafter (our tool):       `{our_avg_NDCG}`.")
        
        print("\n---\n")
        
        print("MAP:\n")
        print(f"Cirrus Search (Minecraft Wiki): `{their_MAP}`.")
        print(f"Query Crafter (our tool):       `{  our_MAP}`.")
        
        print()
    
    return None, None


if __name__ == '__main__':
    load_data()
    
    # query_files: List[str] = os.listdir(EVAL_PATH)
    
    evaluate()