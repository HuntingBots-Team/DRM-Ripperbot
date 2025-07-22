import logging
import os
import subprocess
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
from configparser import ConfigParser
from TGHRip.inline_keyboard import send_task_options, handle_callback
from TGHRip.access_control import is_authorized

config = ConfigParser()
config.read("config.ini")

TOKEN = config.get("TELEGRAM", "Token")
OWNER_ID = int(config.get("TELEGRAM", "OwnerID"))
AUTHORIZED_GROUP = int(config.get("TELEGRAM", "AuthorizedGroupID"))

logging.basicConfig(level=logging.INFO)

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
    savepath = config.get("DOWNLOAD", "SavePath", fallback="downloads/")
    output_file = os.path.join(savepath, filename)

    # DASH (.mpd) links - use web-dl for DRM/non-DRM
    if url.endswith(".mpd"):
        cmd = [
            "python", "webdl.py",
            "--mpd", url,
            "--key", key,
            "--out", output_file
        ]
    # HLS (.m3u8) links - use ffmpeg for non-DRM
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

    await update.message.reply_text(f"Processing your stream. This may take a while...")

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

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rip", rip))
    app.add_handler(CallbackQueryHandler(handle_callback))

    app.run_polling()
