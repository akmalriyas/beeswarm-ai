import os
import discord
from discord.ext import commands
import asyncio
import sys
from honeybee_core import (
    DISCORD_TOKEN, retrieve_context, build_messages, query_llm_api
)

# Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

# Per-channel history
chat_histories = {}

async def send_chunked_message(channel, message_text, reply_to=None):
    """Sends a long message to Discord in chunks to bypass the 2000 character limit."""
    chunk_size = 1900
    chunks = [message_text[i:i+chunk_size] for i in range(0, len(message_text), chunk_size)]
    
    first = True
    for chunk in chunks:
        if first and reply_to:
            await reply_to.reply(chunk, mention_author=False)
            first = False
        else:
            await channel.send(chunk)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name} ({bot.user.id})")
    print("Honey Bee is ready to swarm!")
    await bot.change_presence(activity=discord.Game(name="Bee Swarm Simulator"))

@bot.event
async def on_message(message):
    # Don't respond to self
    if message.author == bot.user:
        return

    print(f"\n--- NEW MESSAGE DETECTED ---")
    print(f"Author: {message.author}")
    print(f"Content: '{message.content}'")

    # Check if we should respond (DM, Mention, or Prefix)
    is_dm = isinstance(message.channel, discord.DMChannel)
    is_mention = bot.user.mentioned_in(message)
    is_command = message.content.startswith("!")

    print(f"Is DM? {is_dm} | Is Mention? {is_mention} | Is Command? {is_command}")

    if is_dm or is_mention or is_command:
        # Clean up the prompt
        content = message.content
        if is_command:
            content = content[1:]
        if is_mention:
            content = content.replace(f'<@{bot.user.id}>', '').replace(f'<@!{bot.user.id}>', '').strip()

        if not content:
            print("Content was empty after cleanup.")
            return

        print(f"Sending this to LLM: '{content}'")

        try:
            async with message.channel.typing():
                print("Querying LLM and ChromaDB...")
                
                # 1. Retrieve Context
                context, sources = await retrieve_context(content, n_results=6)
                
                # 2. Build Messages
                channel_id = message.channel.id
                history = chat_histories.get(channel_id, [])[-8:]
                messages = build_messages(content, context, history, is_discord=True)
                
                # 3. Query LLM
                answer, error = await query_llm_api(messages)
                
                if error:
                    answer = error
                else:
                    # Update History
                    if channel_id not in chat_histories:
                        chat_histories[channel_id] = []
                    
                    if not chat_histories[channel_id] or chat_histories[channel_id][-2].get("content") != content:
                        chat_histories[channel_id].append({"role": "user", "content": content})
                        chat_histories[channel_id].append({"role": "assistant", "content": answer})
                        chat_histories[channel_id] = chat_histories[channel_id][-10:]
                
                print("Successfully got response from LLM!")
        except Exception as e:
            print(f"CRASH during LLM query: {e}")
            # Try once more without typing indicator
            context, sources = await retrieve_context(content, n_results=6)
            messages = build_messages(content, context, chat_histories.get(message.channel.id, [])[-8:], is_discord=True)
            answer, error = await query_llm_api(messages)
            if error:
                answer = error
            
        final_message = answer
        
        if sources:
            source_text = ", ".join(sources).replace(".md", "").replace("_", " ").title()
            final_message += f"\n\n-# *References: {source_text}*"

        print("Attempting to send message back to Discord...")
        
        # Send chunked message instead of cutting it off
        await send_chunked_message(message.channel, final_message, reply_to=message)
        
        print("Message sent successfully!")

    await bot.process_commands(message)

async def console_exit():
    """Allows typing 'exit' in the terminal to stop the bot."""
    loop = asyncio.get_event_loop()
    while True:
        cmd = await loop.run_in_executor(None, sys.stdin.readline)
        if cmd.strip().lower() == 'exit':
            print("Shutting down Honey Bee...")
            await bot.close()
            break

async def main():
    if not DISCORD_TOKEN:
        print("Error: DISCORD_TOKEN not found in .env file!")
        return
        
    # Start the console exit listener and the bot
    async with bot:
        await asyncio.gather(
            bot.start(DISCORD_TOKEN),
            console_exit()
        )

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass # Clean exit on Ctrl+C