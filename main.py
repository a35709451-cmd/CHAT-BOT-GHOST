from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
import os
import re

### ============================================> 𝙱𝙾𝚃 𝙼𝙰𝙺𝙸𝙽𝙶 𝚁𝙴𝚀𝚄𝙸𝚁𝙼𝙴𝙽𝚃 <===============================================###

API_ID = 10248430 
API_HASH = "42396a6ff14a569b9d59931643897d0d"
BOT_TOKEN = "5709229627:AAHWn-lp3r3BXK7kRs8_vnmRIQnUMHRV2bU"
MONGO_URL = "mongodb+srv://AyraMusic:Ayra@cluster0.gnakzem.mongodb.net/?retryWrites=true&w=majority"


bot = Client(
    "MrsShayna_Bot" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)


async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in bot.iter_chat_members(
            chat_id, filter="administrators"
        )
    ]

### ============================================> 𝚂𝚃𝙰𝚁𝚃 <===============================================###

@bot.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("👥 sᴜᴘᴘᴏʀᴛ", url="https://t.me/+IdSOWT2mDr9hOTQ1"),
            InlineKeyboardButton("📣 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/+CN0MlYIFGsAyNGI1")
            ],[InlineKeyboardButton(text="💠 owner 💠",
                url="https://t.me/COVIDBABA")]])
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption="""➛ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n───────────────────\nsᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs:\n───────────────────\n
ᴛʜɪꜱ ʙᴏᴛ ᴏʙꜱᴇʀᴠᴇ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴀɴᴅ ꜱᴛᴏʀᴇ ᴀʟʟ ᴛʜᴇ ᴄʜᴀᴛ ɪɴ  ᴅᴀᴛᴀ ᴀɴᴅ  ᴀʟꜱᴏ ɢɪᴠᴇ ʏᴏᴜʀ ʀᴇᴘʟʏ ᴀꜰᴛᴇʀ ᴅᴀᴛᴀ ᴀɴʏʟʏꜱɪꜱ 
ᴀɴʏ ᴋᴇʏ ɪꜱ ɴᴏᴛ ꜱᴇᴛ ᴜᴘ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴛʜɪꜱ ʙᴏᴛ ᴏɴʟʏ ᴏʙꜱᴇʀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴꜱ ᴄᴏʀʀᴇᴄᴛʟʏ ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ᴏɴʟʏ ᴛʜɪɴɢ ᴡʜɪᴄʜ ᴍᴀᴋᴇ ᴛʜɪꜱ ʙᴏᴛ ᴛʜᴇ ʙᴇꜱᴛ ᴀɴᴅ ꜱᴘᴇᴄɪᴀʟ 
ꜰɪʀꜱᴛ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴏᴘᴇɴ ᴛʜᴇ /ᴄʜᴀᴛʙᴏᴛ ᴏɴ ᴀꜰᴛᴇʀ ᴛʜɪꜱ ʏᴏᴜ ᴡɪʟʟ ᴜɴᴅᴇʀꜱᴛᴀɴᴅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢꜱ.\n───────────────────\n""",
                            reply_markup=buttons)
        
    else:
        buttons = [[
            InlineKeyboardButton("➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕", url=f"https://t.me/MissShayna_Bot?startgroup=true")
        ],
        
        [
            InlineKeyboardButton("👥 ᴏғғɪᴄɪᴀʟ ɢʀᴏᴜᴘ", url="https://t.me/+IdSOWT2mDr9hOTQ1"),
            InlineKeyboardButton("📣 ᴏғғɪᴄɪᴀʟ ᴄʜᴀɴɴᴇʟ", url="https://t.me/+CN0MlYIFGsAyNGI1")
        ],
        [
            InlineKeyboardButton("💠 owner 💠", url="https://t.me/COVIDBABA")
        ]]
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption=f"""ʜᴇʟʟᴏ [{message.from_user.first_name}](tg://user?id={message.from_user.id}),
ɪ ᴀᴍ ᴀɴ ᴀᴅᴠᴀɴᴄᴇᴅ ᴀʀᴛɪғɪᴄᴀʟ ᴀɴᴅ ɴᴇxᴛ ʟᴇᴠᴇʟ ɪɴᴛᴇʟʟɪɢᴇɴᴄᴇ ᴄʜᴀᴛ ʙᴏᴛ.
➖➖➖➖➖➖➖➖➖➖➖➖➖
➛ ɪғ ʏᴏᴜ ᴀʀᴇ ғᴇᴇʟɪɴɢ ʟᴏɴᴇʟʏ, ʏᴏᴜ ᴄᴀɴ ᴀʟᴡᴀʏs ᴄᴏᴍᴇ ᴛᴏ ᴍᴇ ᴀɴᴅ ᴄʜᴀᴛ ᴡɪᴛʜ ᴍᴇ
➛ ᴛʀʏ ᴛʜᴇ \help ᴄᴍᴅs. ᴛᴏ ᴋɴᴏᴡ ᴍʏ ᴀʙɪʟɪᴛɪᴇs ××""", reply_markup=InlineKeyboardMarkup(buttons))

### ============================================> 𝙷𝙴𝙻𝙿 <===============================================###

@bot.on_message(filters.command(["help"], prefixes=["/", "!"]))
async def help(client, message):
    self = await bot.get_me()
    busername = self.username
    if message.chat.type != "private":
        buttons = InlineKeyboardMarkup(
            [[InlineKeyboardButton(text="ᴄʟɪᴄᴋ ʜᴇʀᴇ",
                url=f"t.me/MissShayna_Bot?start=help_")]])
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption="ᴄᴏɴᴛᴀᴄᴛ ᴍᴇ ɪɴ ᴘᴇʀsᴏɴᴀʟ sᴡᴇᴇᴛʜᴇᴀʀᴛ",
                            reply_markup=buttons)
        
    else: 
        Photo = "https://telegra.ph/file/e81a49fb4985e64da516c.jpg"
        await message.reply_photo(Photo, caption="""➛ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n─────────────────────\nsᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs:\n
ᴛʜɪꜱ ʙᴏᴛ ᴏʙꜱᴇʀᴠᴇ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴀɴᴅ ꜱᴛᴏʀᴇ ᴀʟʟ ᴛʜᴇ ᴄʜᴀᴛ ɪɴ  ᴅᴀᴛᴀ ᴀɴᴅ  ᴀʟꜱᴏ ɢɪᴠᴇ ʏᴏᴜʀ ʀᴇᴘʟʏ ᴀꜰᴛᴇʀ ᴅᴀᴛᴀ ᴀɴʏʟʏꜱɪꜱ 

ᴀɴʏ ᴋᴇʏ ɪꜱ ɴᴏᴛ ꜱᴇᴛ ᴜᴘ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴛʜɪꜱ ʙᴏᴛ ᴏɴʟʏ ᴏʙꜱᴇʀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴꜱ ᴄᴏʀʀᴇᴄᴛʟʏ ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ᴏɴʟʏ ᴛʜɪɴɢ ᴡʜɪᴄʜ ᴍᴀᴋᴇ ᴛʜɪꜱ ʙᴏᴛ ᴛʜᴇ ʙᴇꜱᴛ ᴀɴᴅ ꜱᴘᴇᴄɪᴀʟ 

ꜰɪʀꜱᴛ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴏᴘᴇɴ ᴛʜᴇ /ᴄʜᴀᴛʙᴏᴛ ᴏɴ ᴀꜰᴛᴇʀ ᴛʜɪꜱ ʏᴏᴜ ᴡɪʟʟ ᴜɴᴅᴇʀꜱᴛᴀɴᴅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢꜱ.

─────────────────────\n\n➛ /chatbot on - ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n➛ /chatbot off - ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ""")

### ============================================> 𝙲𝙷𝙰𝚃𝙱𝙾𝚃 𝙾𝙵𝙵 <===============================================###

@bot.on_message(
    filters.command("chatbot off", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbotofd(client, message):
    natashadb = MongoClient(MONGO_URL)    
    natasha = natashadb["NatashaDb"]["Natasha"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "sɪʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ.ᴀʙ ᴄʜʟᴀ ᴊᴀᴀ ʙsᴅᴋ ʙɴᴀ ᴅᴜ ᴀᴅᴍɪɴ 😂"
            )
    is_natasha = natasha.find_one({"chat_id": message.chat.id})
    if not is_natasha:
        natasha.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Shayna ᴄʜᴀᴛʙᴏᴛ ᴅɪsᴀʙʟᴇᴅ\n\nᴅᴀʀʟɪɴɢ ᴏғғ ᴋʏᴜ ᴋʀ ʀʜᴇ ʜᴏ ᴍᴜᴊʜᴇ\nᴛʜɪᴋ ʜᴀɪ ʙʏ ᴠᴀɪsᴇ ʙʜɪ ᴛᴜᴍɴᴇ ᴍᴇʀɪ\nʟɪғᴇ ғᴜᴄᴋᴍ ғᴜᴄᴋ ʙɴᴀ ʀᴋʜɪ ʜᴀɪ\nᴀʙ ᴊᴀᴀ ʙsᴅᴋ ᴋ ᴘᴅʜ ᴋʏᴜ ʀʜᴀ ʜᴀɪ 😂")
    if is_natasha:
        await message.reply_text(f"Shayna ᴄʜᴀᴛʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴅɪsᴀʙʟᴇᴅ\n\nᴘʜᴇʟᴇ sᴇ ʜɪ ᴏғғ ʜᴜ ᴀʙ ᴋʏᴀ ɢᴀᴀɴᴅ ᴍᴀʀᴏɢᴇ ᴋʏᴀ\nᴊᴀᴀᴏ ᴀʙ ᴛᴜᴍ ᴍᴜᴊʜsᴇ ʙᴀᴀᴛ ᴋʀᴏ\nᴏʀ ʜᴀᴀɴ ᴇɴɢʟɪsʜ ᴍᴇ ᴜsᴇ ᴋʏᴀ ʙᴏʟᴛᴇ ғᴜ*ᴋ ʏᴏᴜ.")
    
### ============================================> 𝙲𝙷𝙰𝚃𝙱𝙾𝚃 𝙾𝙽 <===============================================###

@bot.on_message(
    filters.command("chatbot on", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatboton(client, message):
    natashadb = MongoClient(MONGO_URL)    
    natasha = natashadb["NatashaDb"]["Natasha"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "sɪʀ ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ.ᴀʙ ᴄʜʟᴀ ᴊᴀᴀ ʙsᴅᴋ ʙɴᴀ ᴅᴜ ᴀᴅᴍɪɴ 😂"
            )
    is_natasha = natasha.find_one({"chat_id": message.chat.id})
    if not is_natasha:           
        await message.reply_text(f"» ᴄʜᴀᴛʙᴏᴛ ɪs ᴀʟʀᴇᴀᴅʏ ᴇɴᴀʙʟᴇᴅ\n\nᴀʀᴇ ᴅᴀʀʟɪɴɢ ᴘʜᴇʟᴇ sᴇ ʜɪ ᴏɴ ʜᴜ\nᴏʀ ʏᴇ ᴄᴍᴅ ᴍᴛ ᴅɪʏᴀ ᴋʀᴏ ʙs ᴇᴋ ᴋɪss ᴅᴇ ᴅɪʏᴀ ᴋʀᴏ 😅👉👈😂")
    if is_natasha:
        natasha.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"✅ | sᴜᴄᴄᴇssғᴜʟʟʏ\nShayna ᴄʜᴀᴛʙᴏᴛ ᴏɴ ᴏғ ᴛʜɪs ɢʀᴏᴜᴘ ɪs sᴇᴛ ᴛᴏ @{message.chat.username}\n ʀᴇǫᴜᴇsᴛᴇᴅ ʙʏ [{message.from_user.first_name}](tg://user?id={message.from_user.id})\nᴘᴏᴡᴇʀᴇᴅ ʙʏ ᴛᴇᴄʜ ǫᴜᴀʀᴅ")
    
## ============================================> 𝙲𝙷𝙰𝚃𝙱𝙾𝚃 <===============================================###

@bot.on_message(
    filters.command("chatbot", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def chatbot(client, message):
        await message.reply_photo("https://telegra.ph/file/e81a49fb4985e64da516c.jpg")
        await message.reply_text(f"""**ʜᴏᴡ ᴛᴏ ᴜsᴇ Shayna:**\n➛ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs:\nᴛʜɪꜱ ʙᴏᴛ ᴏʙꜱᴇʀᴠᴇ ᴀʟʟ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴀɴᴅ ꜱᴛᴏʀᴇ ᴀʟʟ ᴛʜᴇ ᴄʜᴀᴛ ɪɴ  ᴅᴀᴛᴀ ᴀɴᴅ  ᴀʟꜱᴏ ɢɪᴠᴇ ʏᴏᴜʀ ʀᴇᴘʟʏ ᴀꜰᴛᴇʀ ᴅᴀᴛᴀ ᴀɴʏʟʏꜱɪꜱ 

ᴀɴʏ ᴋᴇʏ ɪꜱ ɴᴏᴛ ꜱᴇᴛ ᴜᴘ ɪɴ ᴛʜɪꜱ ʙᴏᴛ ᴛʜɪꜱ ʙᴏᴛ ᴏɴʟʏ ᴏʙꜱᴇʀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ᴄʜᴀᴛ ᴀɴᴅ ʀᴇᴘʟʏ ʏᴏᴜʀ Qᴜᴇꜱᴛɪᴏɴꜱ ᴄᴏʀʀᴇᴄᴛʟʏ ᴛʜɪꜱ ɪꜱ ᴛʜᴇ ᴏɴʟʏ ᴛʜɪɴɢ ᴡʜɪᴄʜ ᴍᴀᴋᴇ ᴛʜɪꜱ ʙᴏᴛ ᴛʜᴇ ʙᴇꜱᴛ ᴀɴᴅ ꜱᴘᴇᴄɪᴀʟ 

ꜰɪʀꜱᴛ ᴀᴅᴅ ᴛʜɪꜱ ʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀɴᴅ ᴏᴘᴇɴ ᴛʜᴇ /ᴄʜᴀᴛʙᴏᴛ ᴏɴ ᴀꜰᴛᴇʀ ᴛʜɪꜱ ʏᴏᴜ ᴡɪʟʟ ᴜɴᴅᴇʀꜱᴛᴀɴᴅ ᴀʟʟ ᴛʜᴇ ᴛʜɪɴɢꜱ.

─────────────────────\n\n➛ /chatbot on - ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ\n➛ /chatbot off - ᴅɪsᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ""")

## ============================================> 𝙱𝙾𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙲𝙾𝙳𝙴 <===============================================###

@bot.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.bot,
)
async def natashaai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})
       if not is_natasha:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})    
       getme = await bot.get_me()
       bot_id = getme.id                             
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_natasha:                   
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})    
               

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.bot,
)
async def natashastickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})
       if not is_natasha:
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       natashadb = MongoClient(MONGO_URL)
       natasha = natashadb["NatashaDb"]["Natasha"] 
       is_natasha = natasha.find_one({"chat_id": message.chat.id})
       getme = await bot.get_me()
       bot_id = getme.id
       if message.reply_to_message.from_user.id == bot_id: 
           if not is_natasha:                    
               await bot.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == bot_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
               


@bot.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.bot,
)
async def natashaprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
       

@bot.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.bot,
)
async def natashaprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await bot.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await bot.get_me()
       bot_id = getme.id       
       if message.reply_to_message.from_user.id == bot_id:                    
           await bot.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
       
bot.run()
