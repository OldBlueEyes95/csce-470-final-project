import pandas as pd
from typing import List, Dict, Tuple

ALGORITHM: str = [
    "BM25"
][0]

def algorithm_BM25(query: str) -> List[str]:
    pass

def main() -> None:
    query: str = input("Input query here...")
    
    search_results: List[str] = []
    
    match ALGORITHM:
        case "BM25":
            search_results.extend(algorithm_BM25(query))
        case _:
            assert False, "Invalid algorithm selected."
    
    print("Results:\n")
    for result in search_results:
        print(result)

if __name__ == "__main__":
    main()