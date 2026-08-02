"""
GHOST AI Chatbot - Advanced Telegram Chatbot
Deployed on Railway with Docker
"""

import os
import time
import subprocess
import platform
import random
import asyncio
from datetime import datetime
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pymongo import MongoClient
import requests
import re

# =============================================
# TIME SYNC FIX - Prevents "msg_id too low" error
# =============================================

def sync_time():
    """Synchronize system time to prevent Telegram errors"""
    try:
        print(f"🕐 Current system time: {datetime.now()}")
        system = platform.system()
        
        if system == "Linux":
            print("🐧 Syncing time on Linux...")
            try:
                subprocess.run(["ntpdate", "-u", "pool.ntp.org"], 
                             check=False, capture_output=True, timeout=10)
                print("✅ Time synced with ntpdate")
            except FileNotFoundError:
                try:
                    subprocess.run(["timedatectl", "set-ntp", "true"], 
                                 check=False, capture_output=True)
                    print("✅ Time synced with timedatectl")
                except Exception as e:
                    print(f"⚠️ Time sync failed: {e}")
                    
        elif system == "Windows":
            print("🪟 Syncing time on Windows...")
            subprocess.run(["w32tm", "/resync"], check=False, capture_output=True)
            
        elif system == "Darwin":  # macOS
            print("🍎 Syncing time on macOS...")
            subprocess.run(["sntp", "-sS", "time.apple.com"], check=False)
            
        print(f"🕐 Updated system time: {datetime.now()}")
        return True
        
    except Exception as e:
        print(f"⚠️ Could not sync time: {e}")
        return False

# Sync time before bot starts
sync_time()

# =============================================
# BOT CONFIGURATION
# =============================================

# Get credentials from environment variables
API_ID = int(os.getenv("API_ID", "10248430"))
API_HASH = os.getenv("API_HASH", "42396a6ff14a569b9d59931643897d0d")
BOT_TOKEN = os.getenv("BOT_TOKEN", "8881596731:AAGsPPhUZuB_tOk5C4gqs2q53D34_BQqkhI")
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://tghostingbot008:tghostingbot008@cluster0.pkwi0ib.mongodb.net/?appName=Cluster0")

# Initialize bot
bot = Client(
    "GHOST_AI_Bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =============================================
# DATABASE SETUP
# =============================================

def get_db():
    """Get database connection with retry"""
    max_retries = 5
    for i in range(max_retries):
        try:
            client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=5000)
            client.admin.command('ping')
            print(f"✅ MongoDB connected successfully")
            return client
        except Exception as e:
            print(f"⚠️ MongoDB connection attempt {i+1}/{max_retries} failed: {e}")
            if i < max_retries - 1:
                time.sleep(3)
            else:
                print("❌ Failed to connect to MongoDB after all retries")
                raise
    return None

# Database connections
db_client = get_db()
natasha_db = db_client["NatashaDb"]
natasha_collection = natasha_db["Natasha"]
word_db = db_client["Word"]
word_collection = word_db["WordDb"]

# =============================================
# HELPER FUNCTIONS
# =============================================

async def is_admins(chat_id: int):
    """Get list of admin user IDs in a chat"""
    try:
        admins = []
        async for member in bot.iter_chat_members(chat_id, filter="administrators"):
            admins.append(member.user.id)
        return admins
    except Exception as e:
        print(f"Error getting admins: {e}")
        return []

async def get_random_response(word):
    """Get random response from database for a word"""
    try:
        responses = []
        cursor = word_collection.find({"word": word})
        async for doc in cursor:
            responses.append(doc['text'])
        
        if responses:
            response = random.choice(responses)
            doc = word_collection.find_one({"text": response})
            if doc:
                return response, doc.get('check', 'none')
        return None, None
    except Exception as e:
        print(f"Error getting random response: {e}")
        return None, None

async def send_response(message, response, response_type):
    """Send appropriate response (text or sticker)"""
    try:
        if response_type == "sticker":
            await message.reply_sticker(response)
        else:
            await message.reply_text(response)
    except Exception as e:
        print(f"Error sending response: {e}")
        await message.reply_text("Sorry, I couldn't respond properly. 😅")

# =============================================
# START COMMAND
# =============================================

@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start_command(client, message):
    """Handle /start command"""
    try:
        self = await bot.get_me()
        busername = self.username
        
        photo_url = "https://i.ibb.co/ccjT7Wdn/Chat-GPT-Image-Aug-2-2026-02-27-15-PM.png"
        
        if message.chat.type != "private":
            buttons = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("👥 Support", url="https://t.me/+IdSOWT2mDr9hOTQ1"),
                    InlineKeyboardButton("📣 Updates", url="https://t.me/+CN0MlYIFGsAyNGI1")
                ],
                [
                    InlineKeyboardButton("💠 Owner", url="https://t.me/GHOSTRIDERFIRE0")
                ]
            ])
            
            caption = """➛ START THE BOT
───────────────────
SPECIAL FEATURES:
───────────────────

This bot observes all group chats and stores all the chat in data and also gives your reply after data analysis

Any key is not set up in this bot. This bot only observes the group chat and replies to your questions correctly. This is the only thing which makes this bot the best and special

First add this bot in your group and open /chatbot on. After this you will understand all the things.
───────────────────"""
            
            await message.reply_photo(photo_url, caption=caption, reply_markup=buttons)
        else:
            buttons = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("➕ Add Me To Your Group", url=f"https://t.me/GHOST_AI_CHAT_BOT?startgroup=true")
                ],
                [
                    InlineKeyboardButton("👥 Official Group", url="https://t.me/Ghostrider_fire"),
                    InlineKeyboardButton("📣 Official Channel", url="https://t.me/xtrchannel")
                ],
                [
                    InlineKeyboardButton("💠 Owner", url="https://t.me/GHOSTRIDERFIRE0")
                ]
            ])
            
            caption = f"""Hello [{message.from_user.first_name}](tg://user?id={message.from_user.id}),

I am an advanced artificial and next level intelligence chat bot.
➖➖➖➖➖➖➖➖➖➖➖➖➖

➛ If you are feeling lonely, you can always come to me and chat with me
➛ Try /help cmd to know my abilities"""
            
            await message.reply_photo(photo_url, caption=caption, reply_markup=buttons)
            
    except Exception as e:
        print(f"Error in start command: {e}")
        await message.reply_text("An error occurred. Please try again later.")

# =============================================
# HELP COMMAND
# =============================================

@bot.on_message(filters.command(["help"], prefixes=["/", "!"]))
async def help_command(client, message):
    """Handle /help command"""
    try:
        photo_url = "https://i.ibb.co/ccjT7Wdn/Chat-GPT-Image-Aug-2-2026-02-27-15-PM.png"
        
        if message.chat.type != "private":
            buttons = InlineKeyboardMarkup([
                [InlineKeyboardButton("Click Here", url="https://t.me/GHOST_AI_CHAT_BOT?start=help_")]
            ])
            await message.reply_photo(photo_url, caption="Contact me in personal sweetheart", reply_markup=buttons)
        else:
            caption = """➛ START THE BOT
─────────────────────
SPECIAL FEATURES:

This bot observes all group chats and stores all the chat in data and also gives your reply after data analysis

Any key is not set up in this bot. This bot only observes the group chat and replies to your questions correctly. This is the only thing which makes this bot the best and special

First add this bot in your group and open /chatbot on. After this you will understand all the things.

─────────────────────

➛ /chatbot on - Activate chatbot in your group
➛ /chatbot off - Disable chatbot in your group"""
            
            await message.reply_photo(photo_url, caption=caption)
            
    except Exception as e:
        print(f"Error in help command: {e}")
        await message.reply_text("An error occurred. Please try again later.")

# =============================================
# CHATBOT ON/OFF COMMANDS
# =============================================

@bot.on_message(filters.command("chatbot off", prefixes=["/", ".", "?", "-"]) & ~filters.private)
async def chatbot_off(client, message):
    """Turn off chatbot in a group"""
    try:
        if message.from_user:
            user = message.from_user.id
            chat_id = message.chat.id
            
            admins = await is_admins(chat_id)
            if user not in admins:
                await message.reply_text("Sir you are not admin. AB chala jaa bana du admin 😂")
                return
        
        is_chatbot = natasha_collection.find_one({"chat_id": message.chat.id})
        
        if not is_chatbot:
            natasha_collection.insert_one({"chat_id": message.chat.id})
            await message.reply_text("Shayna chatbot disabled\n\nDarling off kyu kr rhe ho mujhe\nThik hai by vaise bhi tumne meri\nLife fuckm fuck bna rkhi hai\nAb jaa BSDK k pdh kyu rha hai 😂")
        else:
            await message.reply_text("Shayna chatbot is already disabled\n\nPhele se hi off hu ab jaaao ab tum mujhse baat kro.")
            
    except Exception as e:
        print(f"Error in chatbot off: {e}")
        await message.reply_text("An error occurred. Please try again later.")

@bot.on_message(filters.command("chatbot on", prefixes=["/", ".", "?", "-"]) & ~filters.private)
async def chatbot_on(client, message):
    """Turn on chatbot in a group"""
    try:
        if message.from_user:
            user = message.from_user.id
            chat_id = message.chat.id
            
            admins = await is_admins(chat_id)
            if user not in admins:
                await message.reply_text("Sir you are not admin. AB chala jaa bana du admin 😂")
                return
        
        is_chatbot = natasha_collection.find_one({"chat_id": message.chat.id})
        
        if not is_chatbot:
            await message.reply_text("» Chatbot is already enabled\n\nAre darling phele se hi hu\nOr ye cmd mt diya kro 😅👉👈😂")
        else:
            natasha_collection.delete_one({"chat_id": message.chat.id})
            await message.reply_text(f"""✅ | Successfully
Shayna chatbot on of this group is set to @{message.chat.username}
Requested by [{message.from_user.first_name}](tg://user?id={message.from_user.id})
Powered by Tech Guard""")
            
    except Exception as e:
        print(f"Error in chatbot on: {e}")
        await message.reply_text("An error occurred. Please try again later.")

# =============================================
# CHATBOT INFO COMMAND
# =============================================

@bot.on_message(filters.command("chatbot", prefixes=["/", ".", "?", "-"]) & ~filters.private)
async def chatbot_info(client, message):
    """Show chatbot information"""
    try:
        photo_url = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(photo_url)
        
        caption = """**How to use Shayna:**
➛ Special Features:
This bot observes all group chats and stores all the chat in data and also gives your reply after data analysis

Any key is not set up in this bot. This bot only observes the group chat and replies to your questions correctly. This is the only thing which makes this bot the best and special

First add this bot in your group and open /chatbot on. After this you will understand all the things.

─────────────────────

➛ /chatbot on - Activate chatbot in your group
➛ /chatbot off - Disable chatbot in your group"""
        
        await message.reply_text(caption)
        
    except Exception as e:
        print(f"Error in chatbot info: {e}")
        await message.reply_text("An error occurred. Please try again later.")

# =============================================
# MESSAGE HANDLERS
# =============================================

@bot.on_message(
    (filters.text | filters.sticker) & ~filters.private & ~filters.bot,
)
async def handle_group_messages(client: Client, message: Message):
    """Handle messages in groups"""
    try:
        # Check if chatbot is disabled in this group
        is_chatbot = natasha_collection.find_one({"chat_id": message.chat.id})
        if is_chatbot:
            return
        
        # For messages without reply
        if not message.reply_to_message:
            await bot.send_chat_action(message.chat.id, "typing")
            
            # Handle text messages
            if message.text:
                response, response_type = await get_random_response(message.text)
                if response:
                    await send_response(message, response, response_type)
            
            # Handle sticker messages
            elif message.sticker:
                response, response_type = await get_random_response(message.sticker.file_unique_id)
                if response:
                    await send_response(message, response, response_type)
        
        # For replies to messages
        elif message.reply_to_message:
            getme = await bot.get_me()
            bot_id = getme.id
            
            # If replying to bot's message
            if message.reply_to_message.from_user.id == bot_id:
                is_chatbot = natasha_collection.find_one({"chat_id": message.chat.id})
                if is_chatbot:
                    return
                
                await bot.send_chat_action(message.chat.id, "typing")
                
                # Handle text reply
                if message.text:
                    response, response_type = await get_random_response(message.text)
                    if response:
                        await send_response(message, response, response_type)
                
                # Handle sticker reply
                elif message.sticker:
                    response, response_type = await get_random_response(message.sticker.file_unique_id)
                    if response:
                        await send_response(message, response, response_type)
            
            # If replying to someone else's message - learn from it
            elif message.reply_to_message.from_user.id != bot_id:
                # Learn text response
                if message.text and message.reply_to_message.text:
                    exists = word_collection.find_one({
                        "word": message.reply_to_message.text,
                        "text": message.text
                    })
                    if not exists:
                        word_collection.insert_one({
                            "word": message.reply_to_message.text,
                            "text": message.text,
                            "check": "none"
                        })
                
                # Learn sticker response to text
                elif message.sticker and message.reply_to_message.text:
                    exists = word_collection.find_one({
                        "word": message.reply_to_message.text,
                        "id": message.sticker.file_unique_id
                    })
                    if not exists:
                        word_collection.insert_one({
                            "word": message.reply_to_message.text,
                            "text": message.sticker.file_id,
                            "check": "sticker",
                            "id": message.sticker.file_unique_id
                        })
                
                # Learn text response to sticker
                elif message.text and message.reply_to_message.sticker:
                    exists = word_collection.find_one({
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.text
                    })
                    if not exists:
                        word_collection.insert_one({
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.text,
                            "check": "text"
                        })
                
                # Learn sticker response to sticker
                elif message.sticker and message.reply_to_message.sticker:
                    exists = word_collection.find_one({
                        "word": message.reply_to_message.sticker.file_unique_id,
                        "text": message.sticker.file_id
                    })
                    if not exists:
                        word_collection.insert_one({
                            "word": message.reply_to_message.sticker.file_unique_id,
                            "text": message.sticker.file_id,
                            "check": "none"
                        })
                    
    except Exception as e:
        print(f"Error in group message handler: {e}")

@bot.on_message(
    (filters.text | filters.sticker) & filters.private & ~filters.bot,
)
async def handle_private_messages(client: Client, message: Message):
    """Handle private messages"""
    try:
        await bot.send_chat_action(message.chat.id, "typing")
        
        # For messages without reply
        if not message.reply_to_message:
            # Handle text
            if message.text:
                response, response_type = await get_random_response(message.text)
                if response:
                    await send_response(message, response, response_type)
            
            # Handle sticker
            elif message.sticker:
                response, response_type = await get_random_response(message.sticker.file_unique_id)
                if response:
                    await send_response(message, response, response_type)
        
        # For replies to bot's messages
        elif message.reply_to_message:
            getme = await bot.get_me()
            bot_id = getme.id
            
            if message.reply_to_message.from_user.id == bot_id:
                # Handle text reply
                if message.text:
                    response, response_type = await get_random_response(message.text)
                    if response:
                        await send_response(message, response, response_type)
                
                # Handle sticker reply
                elif message.sticker:
                    response, response_type = await get_random_response(message.sticker.file_unique_id)
                    if response:
                        await send_response(message, response, response_type)
                    
    except Exception as e:
        print(f"Error in private message handler: {e}")
        await message.reply_text("An error occurred. Please try again later.")

# =============================================
# HEALTH CHECK
# =============================================

@bot.on_message(filters.command(["ping", "health"], prefixes=["/", "!"]))
async def health_check(client, message):
    """Health check endpoint"""
    try:
        start_time = time.time()
        await message.reply_chat_action("typing")
        
        # Check MongoDB connection
        try:
            db_client.admin.command('ping')
            db_status = "✅ Connected"
        except:
            db_status = "❌ Disconnected"
        
        response = f"""**Bot Status**
━━━━━━━━━━━━━━━━
🤖 Bot: ✅ Running
💾 Database: {db_status}
🕐 Uptime: {time.time() - start_time:.2f}s
━━━━━━━━━━━━━━━━
Power by Tech Guard"""
        
        await message.reply_text(response)
        
    except Exception as e:
        print(f"Error in health check: {e}")
        await message.reply_text("⚠️ Bot is running but some features may be degraded.")

# =============================================
# BOT STARTUP
# =============================================

if __name__ == "__main__":
    print("=" * 50)
    print("🤖 Starting GHOST AI Chatbot")
    print("=" * 50)
    print(f"🔹 Bot Token: {BOT_TOKEN[:10]}...")
    print(f"🔹 API ID: {API_ID}")
    print(f"🔹 MongoDB: {MONGO_URL[:30]}...")
    print("=" * 50)
    print("🔄 Initializing bot...")
    
    try:
        bot.run()
    except Exception as e:
        print(f"❌ Bot crashed: {e}")
        print("🔄 Attempting to restart in 5 seconds...")
        time.sleep(5)
        # Railway will handle restart
        try:
            bot.run()
        except Exception as e2:
            print(f"❌ Bot failed to restart: {e2}")
            raise
