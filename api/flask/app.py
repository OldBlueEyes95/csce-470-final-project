import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS

# from scoring import rank_documents, load_data
import scoring

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes
scoring.load_data()

logging.basicConfig(level=logging.DEBUG)  # logging

@app.route('/search', methods=['GET'])
def search():
    try:
        # Retrieve query parameter
        query = request.args.get('q')
        
        if not query:
            return jsonify({"error": "No query provided"}), 400
        
        # Process the query and generate search results
        results = [
            {'title': doc, 'text': f"`{doc}`", 'link': f"https://minecraft.wiki/w/{doc}"}
            for doc, score in scoring.rank_documents(query)
        ]
        
        if not results:
            return jsonify({"error": "No results found for the given query"}), 404
        
        # Return the results in JSON format
        return jsonify({'results': results})
    
    except Exception as e:
        # Log unexpected errors
        logging.error(f"Unexpected error occurred: {e}", exc_info=True)
        return jsonify({"error": "Internal server error"}), 500


@app.route('/api/base_url', methods=['GET'])
def get_base_url():
    vercel_url = os.environ.get('VERCEL_URL')
    if vercel_url:
        # If we're in Vercel, return the full backend URL
        return jsonify({"base_url": f"https://{vercel_url}"})
    else:
        # Fallback for local development
        return jsonify({"base_url": "http://localhost:5000"})
