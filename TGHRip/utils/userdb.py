from pyrogram import Client
from utils.mongodb import db
from pyrogram.types import Message


async def AddUser(bot: Client, update: Message):
    if not await db.is_user_exist(update.from_user.id):
           await db.add_user(update.from_user.id)

async def is_user_exist(user_id):
    user = await db.users.find_one({"_id": user_id})
    return user is not None

async def add_user_to_database(user_data):
    await db.users.insert_one(user_data)
