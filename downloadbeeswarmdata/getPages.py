import requests
import os

output_dir = "../downloadbeeswarmdata"
os.makedirs(output_dir, exist_ok=True)

WIKI_API = "https://bee-swarm-simulator.fandom.com/api.php"

params = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "aplimit": "max" # Pulls 500 pages at a time
}

all_pages = []

while True:
    response = requests.get(WIKI_API, params=params).json()
    pages = response['query']['allpages']
    all_pages.extend([p['title'] for p in pages])
    
    if 'continue' in response:
        params.update(response['continue'])
    else:
        break

with open("pages.txt", "w", encoding="utf-8") as f:
    for page in all_pages:
        f.write(page + "\n")

print(f"Done! Found {len(all_pages)} pages.")