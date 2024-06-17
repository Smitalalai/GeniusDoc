from flask import Flask, request, jsonify
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai

app = Flask(__name__)

search_service_endpoint = "https://cwbsearch.search.windows.net"
admin_key = "Gsk9a4McsoNd7UHsGByHtZ5suy25gtuA0ApAWjDqjIAzSeBP7D6C"
index_name = "cwb-indexer"

search_client = SearchClient(endpoint=search_service_endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

def generate_embedding(query):
    openai.api_key = "db8c6e468a43462fa4b16dca0b341f40"
    response = openai.Embedding.create(input=query, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Please provide a query"}), 400

    query_embedding = generate_embedding(query)
    results = search_client.search(embedding=query_embedding, top=5)
    response = [{"documentName": result["documentName"], "documentLink": result["documentLink"], "sectionSummary": result["sectionSummary"], "sectionText": result["sectionText"]} for result in results]
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
