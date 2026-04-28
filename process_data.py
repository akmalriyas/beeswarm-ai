import os
import json
import requests
import re
from pathlib import Path

# Configuration
RAW_DATA_DIR = Path(r"f:\Projects\Python Projects\Training Ai Model\downloadbeeswarmdata\data\raw")
PROCESSED_DATA_DIR = Path(r"f:\Projects\Python Projects\Training Ai Model\data\processed")
CHECKPOINT_FILE = Path(r"f:\Projects\Python Projects\Training Ai Model\data\processing_checkpoint.json")
LLM_URL = "http://192.168.1.98:1234/v1/chat/completions"

# Ensure directories exist
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

def load_checkpoint():
    if CHECKPOINT_FILE.exists():
        with open(CHECKPOINT_FILE, 'r') as f:
            return json.load(f)
    return {"processed_files": []}

def save_checkpoint(processed_files):
    with open(CHECKPOINT_FILE, 'w') as f:
        json.dump({"processed_files": processed_files}, f)

def clean_with_llm(content, filename):
    system_prompt = (
        "You are an expert data cleaner and Bee Swarm Simulator game historian. "
        "Your task is to refine raw wiki markdown data into high-quality training data."
    )
    
    user_prompt = f"""
Input File: {filename}
Raw Content:
---
{content}
---

Your Task:
1. CLEAN BLOAT: Remove navigation links, Fandom UI elements, and repetitive global location/shop lists at the bottom.
2. QUALITY: Fix grammar, improve flow, and ensure the content is clear and professional.
3. RETAIN INFO: Keep all factual information (stats, mobs, items, costs, trivia, mechanics).
4. RENAME: Suggest a simple, descriptive lowercase snake_case filename for this topic (e.g. 'brave_bee_gate', 'royal_jelly').

Output Format (STRICT):
FILENAME: <suggested_filename_without_extension>
CONTENT:
<cleaned_markdown_content>
"""

    payload = {
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3,
        "max_tokens": -1,
        "stream": False
    }

    try:
        response = requests.post(LLM_URL, json=payload, timeout=200)
        response.raise_for_status()
        text = response.json()['choices'][0]['message']['content']
        
        # Parse the output
        name_match = re.search(r"FILENAME:\s*(.*)", text)
        content_match = re.search(r"CONTENT:\s*(.*)", text, re.DOTALL)
        
        if name_match and content_match:
            new_name = name_match.group(1).strip()
            new_content = content_match.group(1).strip()
            return new_name, new_content
        else:
            print(f"Warning: Could not parse LLM output for {filename}. Using raw parsing.")
            return None, None
    except Exception as e:
        print(f"Error processing {filename}: {e}")
        return None, None

def main(limit=None):
    checkpoint = load_checkpoint()
    processed_files = checkpoint["processed_files"]
    
    raw_files = [f for f in RAW_DATA_DIR.glob("*.md") if f.name not in processed_files]
    
    if limit:
        raw_files = raw_files[:limit]
        print(f"Processing a limited batch of {len(raw_files)} files...")
    else:
        print(f"Starting processing of {len(raw_files)} files...")

    for i, file_path in enumerate(raw_files):
        print(f"[{i+1}/{len(raw_files)}] Processing {file_path.name}...")
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_name, new_content = clean_with_llm(content, file_path.name)
        
        if new_name and new_content:
            # Ensure the filename is safe
            new_name = re.sub(r'[^\w\-_\.]', '_', new_name)
            if not new_name.endswith(".md"):
                new_name += ".md"
            
            output_path = PROCESSED_DATA_DIR / new_name
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            processed_files.append(file_path.name)
            save_checkpoint(processed_files)
            print(f"  Successfully saved as {new_name}")
        else:
            print(f"  Failed to process {file_path.name}")

if __name__ == "__main__":
    import sys
    batch_limit = int(sys.argv[1]) if len(sys.argv) > 1 else None
    main(limit=batch_limit)
