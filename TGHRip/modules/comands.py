from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton 
from pyrogram import Client, filters
from asyncio import TimeoutError
from pyrogram.errors import MessageNotModified
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery, ForceReply
from TGHRip.modules.pmtext import Translation 
from config import config
from pyrogram import Client, filters 


COMMANDS_TEXT = """
📖 <b>TGHRip Commands</b>

<b>General Commands:</b>
/start - Show the welcome message
/help - Show this help message
/about - Show information about the bot

<b>Ripping Commands:</b>
/rip <url> <key> - Rip DRM or non-DRM protected live streams

<b>Usage Example:</b>
/rip https://example.com/stream.mpd abcd1234:key5678

<b>Supported Formats:</b>
- DASH (.mpd, DRM or non-DRM)
- HLS (.m3u8, non-DRM)

<b>Notes:</b>
- Ripping DRM-protected content may require a valid key.
- Only use this bot for authorized content.
"""

COMMANDS_BUTTONS = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("🏡 Home", callback_data="home")],
        [
            InlineKeyboardButton("❔ Help", callback_data="help"),
            InlineKeyboardButton("👨‍🚒 About", callback_data="about")
        ],
        [InlineKeyboardButton("⛔️ Close", callback_data="close")]
    ]
)



@Client.on_message(filters.command(["start"]) & filters.private)
async def start(bot, update):
    if not update.from_user:
        return await update.reply_text("I don't know about you sar :(")
    await add_user_to_database(bot, update)
    await bot.send_message(
        Config.LOG_CHANNEL,
           f"#NEW_USER: \n\nNew User [{update.from_user.first_name}](tg://user?id={update.from_user.id}) started @{Config.BOT_USERNAME} !!"
    )
    
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, update)
      if fsub == 400:
        return
    await update.reply_text(
        text=Translation.START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=Translation.START_BUTTONS
    )
