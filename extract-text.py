from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

# Replace with your Form Recognizer endpoint and key
endpoint = "https://<your-form-recognizer-endpoint>.cognitiveservices.azure.com/"
key = "<your-form-recognizer-key>"

# Initialize DocumentAnalysisClient
document_analysis_client = DocumentAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

# Path to the local PDF file
pdf_path = "path/to/your/faq.pdf"

# Open the PDF file and analyze it
with open(pdf_path, "rb") as pdf_file:
    poller = document_analysis_client.begin_analyze_document(
        model_id="prebuilt-document",
        document=pdf_file
    )
    result = poller.result()

# Extract and print text from the document
for page in result.pages:
    print(f"Page {page.page_number}")
    for line in page.lines:
        print(line.content)

# Optionally, save the extracted text to a file
extracted_text = ""
for page in result.pages:
    for line in page.lines:
        extracted_text += line.content + "\n"

with open("extracted_text.txt", "w") as text_file:
    text_file.write(extracted_text)

print("Text extraction complete. Check the 'extracted_text.txt' file.")
