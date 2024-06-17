import logging
import json
import azure.functions as func
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai

def generate_embedding(text):
    openai.api_key = "<your-openai-api-key>"
    response = openai.Embedding.create(input=text, model="text-embedding-ada-002")
    return response['data'][0]['embedding']

def main(inputBlob: func.InputStream) -> None:
    search_endpoint = "https://<your-search-service-name>.search.windows.net"
    admin_key = "<your-admin-key>"
    index_name = "faq-index"

    search_client = SearchClient(endpoint=search_endpoint, index_name=index_name, credential=AzureKeyCredential(admin_key))

    data = json.loads(inputBlob.read().decode('utf-8'))

    documents = []
    for section, summary in zip(data['sections'], data['summaries']):
        document = {
            "documentName": inputBlob.name,
            "documentLink": f"https://<your-storage-account>.blob.core.windows.net/faq-documents/{inputBlob.name}",
            "sectionText": section,
            "sectionSummary": summary,
            "embedding": generate_embedding(section)
        }
        documents.append(document)

    search_client.upload_documents(documents=documents)
    logging.info(f"Indexed document {inputBlob.name} successfully.")
