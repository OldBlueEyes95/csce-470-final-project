import os
from typing import List
from flask import Flask, request, jsonify
from flask_cors import CORS

# from scoring import rank_documents, load_data
import scoring

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes
scoring.load_data()


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Generate search results based on the query
    results = [
        {'title': doc, 'text': "placeholder", 'link': "foobar"}
        for doc, score in scoring.rank_documents(query)
    ]
    
    # Return the results in JSON format
    return jsonify({'results': results})


@app.route('/api/rank', methods=['POST'])
def get_rankings():
    data = request.get_json()
    query: str | None = data.get('query')
    
    if not query:
        return jsonify({"error": "No query provided"}), 400
    
    # Generate rankings based on the query
    rankings = [doc for doc, score in scoring.rank_documents(query)]
    
    # Return the rankings in JSON format
    return jsonify({"rankings": rankings})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)