from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from TGHRip.modules.pmtext import Translation 
from config import Config
# Removed add_user_to_database import
from TGHRip.utils.userdb import AddUser  # Keep other functions if needed
from TGHRip.utils.mongodb import db

@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, message):
    # Check if message is from a user
    if not message.from_user:
        return await message.reply_text("I don't know about you sar :(")
    
    # Removed call to add_user_to_database
    
    # Send a message to LOG_CHANNEL
    await bot.send_message(
        Config.LOG_CHANNEL,
        f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started @{Config.BOT_USERNAME} !!"
    )
    
    # Handle force subscribe if needed
    if Config.UPDATES_CHANNEL:
        fsub = await handle_force_subscribe(bot, message)
        if fsub == 400:
            return
    
    # Send welcome message
    await message.reply_text(
        text=Translation.START_TEXT.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
