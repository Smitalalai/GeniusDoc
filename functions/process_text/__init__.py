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

