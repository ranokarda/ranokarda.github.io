import os
import requests
from dotenv import load_dotenv
from fastdownload import download_url
from PIL import Image
import pillow_avif
import time

load_dotenv()
Api_Key = os.getenv("GOOG_API_KEY")
cx = "423ccb548d65249dd"
url = "https://www.googleapis.com/customsearch/v1/"

# Dictionnaire : nom du dossier → mot-clé de recherche
bears = {
    "grizzly": "grizzly bear",
    "pizzly": "pizzly bear",
    "teddy": "teddy bear"
}

for folder, query in bears.items():
    os.makedirs(f"images/{folder}", exist_ok=True)
    count = 0
    for start in range(1, 100, 10):
        payload = {
            "key": Api_Key,
            "cx": cx,
            "imgType": "photo",
            "searchType": "image",
            "q": query,
            "num": 10,
            "start": start
        }
        response = requests.get(url, params=payload)
        results = response.json()
        ims = [item["link"] for item in results.get("items", [])]
        if not ims:
            print(f"[{folder}] Plus d'images trouvées ou quota atteint.")
            break
        for i, url_img in enumerate(ims):
            count += 1
            dest = f'images/{folder}/{folder}_{count}.jpg'
            try:
                download_url(url_img, dest)
                im = Image.open(dest)
                im.thumbnail((128, 128))
                print(f"[{folder}] Downloaded and checked: {url_img}")
            except Exception as e:
                print(f"[{folder}] Error with {url_img}: {e}")
        time.sleep(1)
    print(f"[{folder}] {count} images downloaded.\n")
