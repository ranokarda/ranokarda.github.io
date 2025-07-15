from dotenv import load_dotenv
import os
import requests
from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex, SimpleField, SearchableField
)
from fastdownload import download_url
from PIL import Image

load_dotenv()

# Azure settings
SERVICE_NAME = os.getenv("BING_API_KEY")
ENDPOINT = f"https://{SERVICE_NAME}.search.windows.net"
API_KEY = os.getenv("AZURE_SEARCH_API_KEY")
INDEX_NAME = os.getenv("AZURE_SEARCH_INDEX")
credential = AzureKeyCredential(API_KEY)

# 1. Create the index (run only ONCE)
index_client = SearchIndexClient(endpoint=ENDPOINT, credential=credential)
fields = [
    SimpleField(name="id", type="Edm.String", key=True),
    SearchableField(name="caption", type="Edm.String"),
    SimpleField(name="url", type="Edm.String", retrievable=True)
]
index = SearchIndex(name=INDEX_NAME, fields=fields)
index_client.create_or_update_index(index)

# 2. Upload documents (valid images) into the index
search_client = SearchClient(endpoint=ENDPOINT, index_name=INDEX_NAME, credential=credential)
documents = [
    {"id": "1", "caption": "Grizzly bear standing in river", "url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb"},
    {"id": "2", "caption": "Grizzly bear in the wild", "url": "https://images.unsplash.com/photo-1464983953574-0892a716854b"},
]

resp = search_client.upload_documents(documents)
print("Upload successful:", resp)

# 3. Search in the index
results = search_client.search(search_text="grizzly bear")
print("Results found:")
urls = []
for r in results:
    print(f"- {r['id']}: {r['caption']} → {r['url']}")
    urls.append(r['url'])

# 4. Download and display the first actually accessible image
def safe_download(url, dest):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        resp = requests.head(url, timeout=10, headers=headers, allow_redirects=True)
        if resp.status_code != 200:
            print(f"Image not found ({resp.status_code}): {url}")
            return False
        # fastdownload doesn't use headers, so fallback to requests.get if needed
        try:
            download_url(url, dest)
        except Exception:
            img_data = requests.get(url, headers=headers).content
            with open(dest, "wb") as f:
                f.write(img_data)
        return True
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

found = False
for url in urls:
    if safe_download(url, "image_downloaded.jpg"):
        img = Image.open("image_downloaded.jpg")
        img.thumbnail((128, 128))
        img.show()
        print(f"Displayed image: {url}")
        found = True
        break

if not found:
    print("No valid image could be downloaded.")
