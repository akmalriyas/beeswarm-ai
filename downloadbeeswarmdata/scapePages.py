import os
import time
import sys
from curl_cffi import requests
from bs4 import BeautifulSoup
import html2text

# --- 1. Folder Setup ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LIST_DIR = BASE_DIR
RAW_DIR = os.path.join(BASE_DIR, "data", "raw")

os.makedirs(RAW_DIR, exist_ok=True)

# --- 2. Stealth API Gatherer ---
def get_all_wiki_titles():
    print("Connecting to Wiki API via Stealth...")
    api_url = "https://bee-swarm-simulator.fandom.com/api.php"
    params = {
        "action": "query",
        "format": "json",
        "list": "allpages",
        "aplimit": "max"
    }
    
    all_titles = []
    
    try:
        while True:
            # Using impersonate="chrome" here is the key
            response = requests.get(api_url, params=params, impersonate="chrome")
            data = response.json()
            
            pages = data['query']['allpages']
            titles = [p['title'] for p in pages]
            all_titles.extend(titles)
            
            print(f"Collected {len(all_titles)} titles...")
            
            # Check if there are more pages to fetch
            if 'continue' in data:
                params.update(data['continue'])
            else:
                break
        
        # Save the list for your records
        with open(os.path.join(LIST_DIR, "pages.txt"), "w", encoding="utf-8") as f:
            for t in all_titles:
                f.write(t + "\n")
        
        return all_titles
    except Exception as e:
        print(f"API Error: {e}")
        return []

# --- 3. Stealth Content Scraper ---
def scrape_page(title):
    # Skip non-info pages (like Files or Templates)
    if any(prefix in title for prefix in ["File:", "Template:", "Category:", "User:"]):
        return False

    url = f"https://bee-swarm-simulator.fandom.com/wiki/{title.replace(' ', '_')}"
    
    try:
        response = requests.get(url, impersonate="chrome", timeout=15)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find('div', {'class': 'mw-parser-output'})
            
            if content:
                # Strip clutter
                for junk in content(['table', 'div', 'aside', 'script'], class_=['navbox', 'toc', 'wds-tabs']):
                    junk.decompose()
                
                h = html2text.HTML2Text()
                h.body_width = 0
                markdown = h.handle(str(content))
                
                filename = title.replace('/', '_').replace(' ', '_') + ".md"
                with open(os.path.join(RAW_DIR, filename), "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n{markdown}")
                return True
    except Exception as e:
        print(f"Error on {title}: {e}")
    return False

# --- 4. RUN ---
titles = get_all_wiki_titles()

if not titles:
    print("Failed to get titles. Check internet connection.")
    sys.exit()

print(f"Starting download of {len(titles)} potential pages...")
success_count = 0

for i, title in enumerate(titles):
    if scrape_page(title):
        success_count += 1
    
    # Progress bar style print
    if i % 10 == 0:
        print(f"Progress: {i}/{len(titles)} - Successfully saved: {success_count}")
    
    # Tiny sleep to stay under the radar
    time.sleep(0.1)

print(f"\nFINISHED! Total files saved: {success_count}")