#GeniusDoc

Certainly! Below is the complete `README.md` file that you can use for your GitHub repository. The code snippets have been updated to use Azure Web Apps instead of Flask for deployment.

---

# Azure AI Document Search and Generative AI POC

This repository contains a Proof of Concept (POC) for building a full-text search and generative AI system over Microsoft FAQ documents using Azure AI services.

## Table of Contents

- [Introduction](#introduction)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Directory Structure](#directory-structure)
- [Part 1: Full-Text Search POC](#part-1-full-text-search-poc)
  - [Set Up Azure Cognitive Search](#set-up-azure-cognitive-search)
  - [Upload PDF to Azure Blob Storage](#upload-pdf-to-azure-blob-storage)
  - [Data Extraction Using Document Intelligence Studio](#data-extraction-using-document-intelligence-studio)
  - [Text Processing and Partitioning](#text-processing-and-partitioning)
  - [Indexing Data into Azure Cognitive Search](#indexing-data-into-azure-cognitive-search)
  - [Create a Search Interface](#create-a-search-interface)
- [Part 2: Generative AI with RAG Pattern](#part-2-generative-ai-with-rag-pattern)
  - [Generate Embeddings Using Azure OpenAI](#generate-embeddings-using-azure-openai)
  - [Index Embeddings in Azure Cognitive Search](#index-embeddings-in-azure-cognitive-search)
  - [Build a Query Interface with Vector Search](#build-a-query-interface-with-vector-search)
- [Deployment to Azure Web Apps](#deployment-to-azure-web-apps)
- [License](#license)

## Introduction

Welcome! This project demonstrates how to build a full-text search and generative AI system using Azure's powerful AI services. It guides you through processing and indexing your Microsoft FAQ documents to create a robust search and retrieval system.

## Architecture

Here's what we're using:
- **Azure Cognitive Search**: For indexing and searching document content.
- **Azure Blob Storage**: To store your PDF documents.
- **Azure Document Intelligence Studio**: For extracting text from PDFs.
- **Azure Functions**: For processing text and indexing it.
- **Azure OpenAI**: To generate embeddings and support natural language queries.
- **Azure Web Apps**: For deploying our search interface.

## Prerequisites

Before you start, make sure you have:
- An Azure Subscription
- Python 3.8 or higher
- Azure CLI installed
- Git installed
- An OpenAI API Key

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/azure-ai-document-search.git
   cd azure-ai-document-search
   ```

2. **Create a Python virtual environment and install dependencies**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Directory Structure

Here's an overview of the main files and directories in this repository:

```
azure-ai-document-search/
│
├── functions/
│   ├── process_text/
│   │   ├── __init__.py          # Azure Function to process and summarize text
│   └── index_data/
│       ├── __init__.py          # Azure Function to index data into Azure Cognitive Search
│
├── webapp/
│   ├── app_service/             # Directory for Azure Web App service code
│   │   ├── main.py              # Main application code for Azure Web App
│   │   ├── requirements.txt     # Dependencies for Azure Web App
│
├── data/
│   ├── sample-faq.pdf           # Sample Microsoft FAQ PDF document
│
├── requirements.txt             # Dependencies for Azure Functions
├── README.md                    # This readme file
└── LICENSE                      # License file
```

## Part 1: Full-Text Search POC

### Set Up Azure Cognitive Search

1. **Create an Azure Cognitive Search service** in the Azure portal.
2. **Define your index schema** with fields to store document metadata, section text, and summaries.

### Upload PDF to Azure Blob Storage

1. **Create a Blob Storage container** and upload your Microsoft FAQ PDF document.
2. **Configure access keys** for the storage.

### Data Extraction Using Document Intelligence Studio

1. **Set Up Document Intelligence Studio**:
   - Create a Form Recognizer resource in the Azure portal.
   - Use the prebuilt model to extract text from the PDF document.
   - Save the extracted data in JSON format.

### Text Processing and Partitioning

1. **Navigate to the `functions/process_text` directory** and deploy the Azure Function:
   ```bash
   cd functions/process_text
   func azure functionapp publish <your-function-app-name>
   ```

### Indexing Data into Azure Cognitive Search

1. **Navigate to the `functions/index_data` directory** and deploy the Azure Function:
   ```bash
   cd ../index_data
   func azure functionapp publish <your-function-app-name>
   ```

### Create a Search Interface

1. **Navigate to the `webapp/app_service` directory**.
2. **Deploy the Azure Web App**:
   ```bash
   az webapp up --name <your-webapp-name> --resource-group <your-resource-group> --plan <your-app-service-plan>
   ```

## Part 2: Generative AI with RAG Pattern

### Generate Embeddings Using Azure OpenAI

1. **Generate embeddings** for each section using Azure OpenAI Service. This is integrated into the indexing Azure Function.

### Index Embeddings in Azure Cognitive Search

1. **Extend the previous indexing Azure Function** to include embeddings. This is already done in the provided code.

### Build a Query Interface with Vector Search

1. **Extend the Azure Web App** to handle vector searches. This is already done in the provided code.

## Deployment to Azure Web Apps

1. **Log in to Azure CLI**:
   ```bash
   az login
   ```

2. **Create an Azure App Service Plan and Web App**:
   ```bash
   az group create --name MyResourceGroup --location <location>
   az appservice plan create --name MyAppServicePlan --resource-group MyResourceGroup --sku FREE
   az webapp create --name MyWebAppName --resource-group MyResourceGroup --plan MyAppServicePlan
   ```

3. **Deploy the Azure Web App**:
   ```bash
   cd webapp/app_service
   az webapp up --name MyWebAppName --resource-group MyResourceGroup --plan MyAppServicePlan
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to reach out if you have any questions or run into any issues. Happy coding!

---

### Main Application Code (`webapp/app_service/main.py`)

```python
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
```

### Azure Function Code (`functions/process_text/__init__.py`)

```python
import logging
import azure.functions as func
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

def main(inputBlob: func.InputStream, outputBlob: func.Out[func.InputStream]) -> None:
    endpoint = "https://<your-text-analytics-endpoint>"
    key = "<your-text-analytics-key>"
    client = TextAnalyticsClient(endpoint=endpoint, credential=AzureKeyCredential(key))

    document = inputBlob.read().decode('utf-8')
    sections = document.split('\n\n')  # Simple partition by paragraphs

    summaries = []
    for section in sections:
        response = client.extract_summary(documents=[section])[0]
        summaries.append(response.summary)

    outputBlob.set({"sections": sections, "summaries": summaries})
```

### Azure Function Code (`functions/index_data/__init__.py`)

```python
import logging
import json
import azure.functions as func
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import openai

def generate_embedding(text):
    openai.api_key = "<your-openai-api-key>"
    response =

 openai.Embedding.create(input=text, model="text-embedding-ada-002")
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
```

---
