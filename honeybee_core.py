import os
import aiohttp
import asyncio
import chromadb
from chromadb.utils import embedding_functions
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASE_DIR = Path(__file__).parent
DB_PATH = str(BASE_DIR / "chroma_db")
DATA_DIR = BASE_DIR / "data" / "processed"
LLM_URL = os.getenv("LLM_URL", "http://192.168.1.98:1234/v1/chat/completions")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


AGENT_NAME = "Honey Bee"        
CREATOR_NAME = "Akmal Riyas"

# UI Colors (ANSI Escape Codes) - For Terminal
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

async def retrieve_context(user_query, n_results=6):
    """Retrieve context from ChromaDB based on the user query."""
    small_talk = ['hey', 'hi', 'hello', 'sup', 'how are you', 'who are you', 'good morning']
    is_small_talk = any(user_query.lower().strip() == phrase for phrase in small_talk)
    
    if is_small_talk:
        return "", []

    # Run query synchronously in thread to avoid blocking asyncio loop
    results = await asyncio.to_thread(
        collection.query,
        query_texts=[user_query],
        n_results=n_results
    )
    
    context = ""
    sources = []
    
    if results['documents'] and results['documents'][0]:
        context = "\n\n".join(results['documents'][0])
        sources = list(set([m['source'].split('_chunk')[0] for m in results['metadatas'][0]]))
        
    return context, sources

def build_messages(user_query, context, history, is_discord=False):
    """Builds the message prompt for the LLM based on environment."""
    
    if is_discord:
        system_prompt = (
            f"You are {AGENT_NAME}, a friendly, human-like companion for the game Bee Swarm Simulator. "
            f"You were created by {CREATOR_NAME}. "
            "CRITICAL DISCORD GUIDELINES:\n"
            "- Speak naturally, like a helpful friend on Discord. Do NOT sound like an AI.\n"
            "- Use standard Discord markdown naturally (e.g., **bold** for item names).\n"
            "- NEVER say 'Based on the context', 'According to my data', or 'I am an AI'.\n"
            "- If you don't know the answer, admit it casually and briefly."
        )
    else:
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
        
    if context:
        system_prompt += f"\n\nCURRENT DATABASE KNOWLEDGE FOR THIS QUESTION:\n{context}"

    messages = [{"role": "system", "content": system_prompt}]
    
    for msg in history:
        messages.append(msg)
        
    messages.append({"role": "user", "content": user_query})
    
    return messages

async def query_llm_api(messages, temperature=0.65, max_tokens=1500):
    """Asynchronously calls the LLM API."""
    payload = {
        "messages": messages,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(LLM_URL, json=payload, timeout=120) as response:
                if response.status == 200:
                    data = await response.json()
                    answer = data['choices'][0]['message']['content'].strip()
                    return answer, None
                else:
                    return None, f"Bzzz... My wings are tired! (Error {response.status})"
        except Exception as e:
            return None, f"Connection Error: {e}"
