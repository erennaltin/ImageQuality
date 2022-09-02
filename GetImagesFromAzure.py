import os
import uuid
from azure.storage.blob import BlobServiceClient

DEST = "<PATH_OF_SOURCE_DIRECTORY>"

connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
# To set connection string
# setx AZURE_STORAGE_CONNECTION_STRING "<yourconnectionstring>"

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container_client = blob_service_client.get_container_client("production")

blob_list = container_client.list_blobs()
dir_list = os.listdir(DEST)

counter = 0
for blob in blob_list:
    counter += 1
    if blob.name in dir_list:
        continue
    print("STARTING TO DOWNLOAD: ", blob.name)
    blob_client = container_client.get_blob_client(blob.name)
    with open(DEST + blob.name, "wb") as my_blob:
        download_stream = blob_client.download_blob()
        my_blob.write(download_stream.readall())
    print(f"FILE CREATED: {counter}")

# To set connection string:
