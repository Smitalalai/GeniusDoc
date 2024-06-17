import logging
import json
import azure.functions as func
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai

def generate_embedding(text):
    openai.api_key = "db8c6e468a43462fa4b16dca0b341f40"
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def main(inputBlob: func.InputStream) -> None:
    search_endpoint = "https://cwbsearch.search.windows.net"
    admin_key = "Gsk9a4McsoNd7UHsGByHtZ5suy25gtuA0ApAWjDqjIAzSeBP7D6C"
    index_name = "cwb-indexer"

    search_client = SearchClient(endpoint=search_endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

    data = json.loads(inputBlob.read().decode('utf-8'))

    documents = []
    for section, summary in zip(data['sections'], data['summaries']):
        document = {
            "documentName": inputBlob.name,
            "documentLink": f"https://cwbfaq.blob.core.windows.net/pdf-microsoft-faq",
            "sectionText": section,
            "sectionSummary": summary,
            "embedding": generate_embedding(section)
        }
        documents.append(document)

    search_client.upload_documents(documents=documents)
    logging.info(f"Indexed document {inputBlob.name} successfully.")
