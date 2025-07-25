import os
import subprocess
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from pyrogram import Client
from TGHRip.inline_keyboard import handle_callback
from TGHRip.access_control import is_authorized
from config import Config

# Read config values
TOKEN = Config.BOT_TOKEN
OWNER_ID = Config.OWNER_ID
AUTHORIZED_GROUP = Config.LOG_CHANNEL


logging.basicConfig(level=logging.INFO)

# Telegram command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if chat_id < 0 and chat_id != AUTHORIZED_GROUP:
        return

    if not is_authorized(user_id, chat_id):
        await update.message.reply_text("You are not authorized to use this bot.")
        return

    await update.message.reply_text("👋 Welcome to TGHRip!\nSend /rip <url> <key> to start ripping.")

async def rip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    chat_id = update.effective_chat.id

    if chat_id < 0 and chat_id != AUTHORIZED_GROUP:
        return

    if not is_authorized(user_id, chat_id):
        await update.message.reply_text("⛔ Not authorized.")
        return

    if len(context.args) < 2:
        await update.message.reply_text("Usage: /rip <url> <decryption_key>")
        return

    url, key = context.args[0], context.args[1]
    filename = "output.mp4"
    savepath = Config.DOWNLOAD_LOCATION
    output_file = os.path.join(savepath, filename)

    # Determine command based on link type
    if url.endswith(".mpd"):
        cmd = [
            "python3", "webdl.py",
            "--mpd", url,
            "--key", key,
            "--out", output_file
        ]
    elif url.endswith(".m3u8"):
        cmd = [
            "ffmpeg",
            "-y",
            "-i", url,
            "-c", "copy",
            output_file
        ]
    else:
        await update.message.reply_text("Unsupported link type. Only .mpd and .m3u8 are supported.")
        return

    await update.message.reply_text("Processing your stream. This may take a while...")

    try:
        subprocess.run(cmd, check=True)
        if os.path.exists(output_file):
            with open(output_file, "rb") as f:
                await update.message.reply_document(f)
            os.remove(output_file)
        else:
            await update.message.reply_text("Ripping failed: output file not found.")
    except Exception as e:
        await update.message.reply_text(f"Error while ripping: {str(e)}")

async def main():
    # Initialize Telegram application
    application = ApplicationBuilder().token(TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("rip", rip))
    application.add_handler(CallbackQueryHandler(handle_callback))

    if __name__ == "__main__":
        if not os.path.isdir(Config.DOWNLOAD_LOCATION):
            os.makedirs(Config.DOWNLOAD_LOCATION)
        plugins = dict(root="TGHRip")
        client = Client(
            "@urltofile00bot",
            bot_token=Config.BOT_TOKEN,
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            upload_boost=True,
            sleep_threshold=300,
            plugins=plugins
        )
        print("🎊 I AM ALIVE 🎊  • Support @TGHLeechSupport")
        client.run()
