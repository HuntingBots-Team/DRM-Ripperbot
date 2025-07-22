import asyncio
from pyrogram import Client
from config import Config

API_ID = Config.API_ID
API_HASH = Config.API_HASH
SESSION_NAME = Config.SESSION_NAME if hasattr(Config, "SESSION_NAME") else "tghrip_userbot"

app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

async def upload_file(file_path, target_chat_id):
    async with app:
        await app.send_document(chat_id=target_chat_id, document=file_path)
