import os
import requests
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
import sys

# Configuration
DB_PATH = r"f:\Projects\Python Projects\Training Ai Model\chroma_db"
DATA_DIR = Path(r"f:\Projects\Python Projects\Training Ai Model\data\processed")
LLM_URL = "http://192.168.1.98:1234/v1/chat/completions"

# Persona Constants
AGENT_NAME = "Honey Bee"
CREATOR_NAME = "Akmal Riyas"

# UI Colors (ANSI Escape Codes)
COLOR_USER = "\033[96m"    # Cyan
COLOR_BOT = "\033[93m"     # Yellow
COLOR_SYS = "\033[90m"     # Dark Gray
COLOR_RESET = "\033[0m"    # Reset

# Initialize Chroma
client = chromadb.PersistentClient(path=DB_PATH)
embedding_func = embedding_functions.DefaultEmbeddingFunction()
collection = client.get_or_create_collection(
    name="bee_swarm_wiki",
    embedding_function=embedding_func
)

chat_history = []

def chunk_text(text, chunk_size=800, overlap=150):
    """Splits large text into smaller, searchable chunks with overlap."""
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest_data():
    """Load processed markdown files into ChromaDB with chunking."""
    existing_ids = set(collection.get()['ids'])
    files = list(DATA_DIR.glob("*.md"))
    
    # We only want to process files we haven't seen. 
    # Since we use chunk IDs now (filename_chunk_0), we check if the base filename is in our existing DB
    new_files = [f for f in files if not any(f.name in eid for eid in existing_ids)]
    
    if not new_files:
        return

    print(f"{COLOR_SYS}Bzzz! Indexing {len(new_files)} new nectar drops... Breaking them down for better digestion!{COLOR_RESET}")
    
    documents = []
    metadatas = []
    ids = []
    
    for file_path in new_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Chunk the file so the search actually finds specific facts
            chunks = chunk_text(content)
            for i, chunk in enumerate(chunks):
                documents.append(chunk)
                metadatas.append({"source": file_path.name})
                ids.append(f"{file_path.name}_chunk_{i}")
            
    batch_size = 50
    for i in range(0, len(documents), batch_size):
        collection.add(
            documents=documents[i:i+batch_size],
            metadatas=metadatas[i:i+batch_size],
            ids=ids[i:i+batch_size]
        )

def query_llm(user_query):
    """Retrieve context and generate answer using local LLM with persona."""
    global chat_history
    
    # 1. Bypass search for simple greetings/small talk
    small_talk = ['hey', 'hi', 'hello', 'sup', 'how are you', 'who are you', 'good morning']
    is_small_talk = any(user_query.lower().strip() == phrase for phrase in small_talk)
    
    context = ""
    sources = []
    
    if not is_small_talk:
        # We increased n_results to 5 since chunks are smaller. This gives Gemma more puzzle pieces.
        results = collection.query(
            query_texts=[user_query],
            n_results=5 
        )
        if results['documents'] and results['documents'][0]:
            context = "\n\n".join(results['documents'][0])
            # Get unique sources
            sources = list(set([m['source'] for m in results['metadatas'][0]]))

    # 2. Build Messages
    system_prompt = (
        f"You are {AGENT_NAME}, a friendly, human-like companion for the game Bee Swarm Simulator. "
        f"You were created by {CREATOR_NAME}. "
        "Guidelines:\n"
        "- Speak naturally, like a helpful friend sitting next to the user. Do not sound like a robot.\n"
        "- Be warm, but use bee-related puns sparingly.\n"
        "- NEVER say 'Based on the context', 'According to my knowledge base', or 'I found this in the data'. Just weave facts naturally into your answer.\n"
        "- If the user just says hello, greet them back warmly.\n"
        "- If you do not know the answer, just casually admit you aren't sure right now."
    )
    
    messages = [{"role": "system", "content": system_prompt}]
    
    # Add history
    for msg in chat_history[-10:]:
        messages.append(msg)
        
    # Inject context ONLY if it's not small talk
    if context:
        user_message = f"Relevant game info:\n{context}\n\nUser Question: {user_query}"
    else:
        user_message = user_query
        
    messages.append({"role": "user", "content": user_message})

    payload = {
        "messages": messages,
        "temperature": 0.6,
        "max_tokens": -1,
        "stream": False
    }

    try:
        response = requests.post(LLM_URL, json=payload, timeout=60)
        response.raise_for_status()
        answer = response.json()['choices'][0]['message']['content']
        
        chat_history.append({"role": "user", "content": user_query})
        chat_history.append({"role": "assistant", "content": answer})
        
        return answer, sources
    except Exception as e:
        return f"Whoops, my wings got tangled! (Connection Error: {e})", None

def chat():
    # Clear terminal screen for a clean start (works on Windows & Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{COLOR_BOT}======================================================{COLOR_RESET}")
    print(f"{COLOR_BOT}   Welcome! I am {AGENT_NAME}, created by {CREATOR_NAME}   {COLOR_RESET}")
    print(f"{COLOR_BOT}======================================================{COLOR_RESET}")
    print(f"{COLOR_SYS}Ask me anything about Bee Swarm Simulator! (type 'exit' to leave){COLOR_RESET}\n")
    
    while True:
        try:
            user_input = input(f"{COLOR_USER}You: {COLOR_RESET}").strip()
        except EOFError:
            break
            
        if user_input.lower() in ['exit', 'quit']:
            print(f"\n{COLOR_BOT}{AGENT_NAME}:{COLOR_RESET} Goodbye! Stay sweet! Bzzz!")
            break
        
        if not user_input:
            continue
            
        # Give a quiet thinking indicator
        print(f"{COLOR_SYS}[{AGENT_NAME} is looking through the hive...]{COLOR_RESET}", end="\r")
        
        answer, sources = query_llm(user_input)
        
        # Clear the thinking indicator with spaces
        print(" " * 50, end="\r") 
        
        print(f"{COLOR_BOT}{AGENT_NAME}:{COLOR_RESET} {answer}")
        
        if sources:
            source_list = ", ".join(sources)
            print(f"{COLOR_SYS}[Ref: {source_list}]{COLOR_RESET}")
            
        print(f"{COLOR_SYS}" + "-" * 55 + f"{COLOR_RESET}\n")

if __name__ == "__main__":
    ingest_data()
    if len(sys.argv) > 1 and sys.argv[1] == "--ingest-only":
        print(f"{COLOR_SYS}Ingestion complete.{COLOR_RESET}")
    else:
        chat()