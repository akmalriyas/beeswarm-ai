import os
import sys
import asyncio
from honeybee_core import (
    AGENT_NAME, CREATOR_NAME, COLOR_BOT, COLOR_USER, COLOR_SYS, COLOR_RESET,
    ingest_data, retrieve_context, build_messages, query_llm_api
)

chat_history = []

async def async_chat():
    # Clear terminal screen for a clean start (works on Windows & Mac/Linux)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(f"{COLOR_BOT}================================================================{COLOR_RESET}")
    print(f"{COLOR_BOT}           Welcome to Bee Swarm Simulator AI                    {COLOR_RESET}")
    print(f"{COLOR_BOT}================================================================{COLOR_RESET}")
    print(f"{COLOR_SYS}Ask me anything about Bee Swarm Simulator! (type 'exit' to leave){COLOR_RESET}\n")
    
    global chat_history

    while True:
        try:
            user_input = input(f"{COLOR_USER}You: {COLOR_RESET}").strip()
        except EOFError:
            break
            
        if user_input.lower() in ['exit', 'quit']:
            print(f"\n{COLOR_BOT}{AGENT_NAME}:{COLOR_RESET} Goodbye!")
            break
        
        if not user_input:
            continue
            
        # Give a quiet thinking indicator
        print(f"{COLOR_SYS}[{AGENT_NAME} is thinking...]{COLOR_RESET}", end="\r")
        
        # 1. Retrieve Context
        context, sources = await retrieve_context(user_input, n_results=6)
        
        # 2. Build Messages
        messages = build_messages(user_input, context, chat_history[-10:], is_discord=False)
        
        # 3. Query LLM
        answer, error = await query_llm_api(messages)
        
        # Clear the thinking indicator with spaces
        print(" " * 50, end="\r") 
        
        if error:
            print(f"{COLOR_BOT}{AGENT_NAME}:{COLOR_RESET} {error}")
            print(f"{COLOR_SYS}" + "-" * 55 + f"{COLOR_RESET}\n")
            continue
            
        # Anti-Loop Check: Don't save the exact same question twice in a row
        if not chat_history or chat_history[-2].get("content") != user_input:
            chat_history.append({"role": "user", "content": user_input})
            chat_history.append({"role": "assistant", "content": answer})
        
        print(f"{COLOR_BOT}{AGENT_NAME}:{COLOR_RESET} {answer}")
        
        if sources:
            source_list = ", ".join(sources).replace(".md", "").replace("_", " ").title()
            print(f"{COLOR_SYS}[Ref: {source_list}]{COLOR_RESET}")
            
        print(f"{COLOR_SYS}" + "-" * 55 + f"{COLOR_RESET}\n")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--ingest-only":
        ingest_data()
        print(f"{COLOR_SYS}Ingestion complete.{COLOR_RESET}")
    else:
        # We can run ingestion silently at start, or just rely on it being pre-ingested
        ingest_data()
        asyncio.run(async_chat())