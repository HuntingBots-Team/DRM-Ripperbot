import asyncio
from pyrogram import Client
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")

API_ID = config.getint("API", "ApiID")
API_HASH = config.get("API", "ApiHash")

app = Client("tghrip_userbot", api_id=API_ID, api_hash=API_HASH)

async def upload_file(file_path, target_chat_id):
    async with app:
        await app.send_document(chat_id=target_chat_id, document=file_path)
