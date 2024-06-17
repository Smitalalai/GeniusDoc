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
- **Flask**: A web framework for building our search interface.

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

#directory-structure
azure-ai-document-search/
│
├── functions/
│   ├── process_text/
│   │   ├── __init__.py          # Azure Function to process and summarize text
│   └── index_data/
│       ├── __init__.py          # Azure Function to index data into Azure Cognitive Search
│
├── webapp/
│   ├── app.py                   # Flask web application for search interface
│   ├── requirements.txt         # Dependencies for Flask application
│
├── data/
│   ├── sample-faq.pdf           # Sample Microsoft FAQ PDF document
│
├── requirements.txt             # Dependencies for Azure Functions
├── README.md                    # This readme file
└── LICENSE                      # License file

