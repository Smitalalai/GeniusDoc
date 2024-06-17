from flask import Flask, request, jsonify
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai

app = Flask(__name__)

search_service_endpoint = "https://<your-search-service-name>.search.windows.net"
admin_key = "<your-admin-key>"
index_name = "faq-index"

search_client = SearchClient(endpoint=search_service_endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

def generate_embedding(query):
    openai.api_key = "<your-openai-api-key>"
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
