from pyrogram import Client
from TGHRip.utils.mongodb import db
from pyrogram.types import Message

async def AddUser(bot: Client, message: Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    is_bot = message.from_user.is_bot
    joined_at = message.date

    # Check if user exists
    if not await db.is_user_exist(user_id):
        # Add user with detailed info
        await db.add_user({
            "_id": user_id,
            "first_name": first_name,
            "username": username,
            "is_bot": is_bot,
            "joined_at": joined_at
        })
