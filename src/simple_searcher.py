import urllib
import scoring


def run_engine() -> None:
    """
    handles user queries in a loop.
    """
    
    n: int = 10
    assert n > 1, "`n` must be an integer greater than 1."
    scoring.load_data()
    
    print("Welcome to this Document Ranking System Demo")
    print("Type your query below, or type 'q' to quit.\n")
    
    while True:
        query = input("Enter your query: ").lower()
        if query in ['exit', 'q', 'quit']:
            print("Exiting the system. Goodbye!")
            break
        
        ranked_docs = scoring.rank_documents(query)[:10]
        
        if ranked_docs:
            print("\nRanked Document IDs:")
            print(f"{'Score':<10}{'Document ID':<60}  {'URL':<60}")
            print("-" * 132)
            for doc_id, score in ranked_docs:
                url = f"https://minecraft.wiki/w/{urllib.parse.quote(doc_id, safe=':/')}"
                print(f"{score:<10.4f}{doc_id:<60}  {url:<60}")
        else:
            print("No documents found for the given query.")
        
        print("\n---\n")


if __name__ == "__main__":
    run_engine()
