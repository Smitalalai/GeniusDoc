from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

connection_string = "DefaultEndpointsProtocol=https;AccountName=cwbfaq;AccountKey=lo0AizbsXbjZWMVj368VWvr+fbCyrmaB9//PkHb3e9Wg4sEF9Co1k8hjeXrpcpKvnyuXKkipi8aH+AStm+SmKQ==;EndpointSuffix=core.windows.net"

blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "pdf-microsoft-faq"

try:
    container_client = blob_service_client.create_container(container_name)
except Exception as e:
    print(f"Container already exists. Error: {e}")

# Path to the local PDF file
local_file_path = ""C:\Users\smita\OneDrive\Desktop\cwb\FAQ\Azure AI Services.pdf""
blob_name = os. path.basename(local_file_path)

blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

# Upload the file
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)

print(f"{blob_name} uploaded to container {container_name}.")
