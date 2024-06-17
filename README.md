#GeniusDoc

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
   git clone https://github.com/Smitalalai/GeniusDoc.git
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

### Indexing Data into Azure Cognitive Search

1. **Navigate to the `functions/index_data` directory** and deploy the Azure Function:
   
### Create a Search Interface

1. **Navigate to the `webapp/app_service` directory**.
2. **Deploy the Azure Web App**:
 
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
   
3. **Deploy the Azure Web App**:
   
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

