import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

WELCOME_MESSAGE = (
    "👋 Welcome to TGHRip!\n\n"
    "🔧 Owner: @The_Ghost_Hunter\n"
    "📣 Updates: https://t.me/allhindi_stories\n"
    "💬 Support: https://t.me/TGHLeechSupport2\n\n"
    "This bot allows you to rip DRM and non-DRM protected live streams.\n"
    "Type /help for available commands."
)

HELP_MESSAGE = (
    "📖 TGHRip Help\n\n"
    "Commands:\n"
    "/start - Welcome message\n"
    "/help - Show this help message\n"
    "/rip <url> <key> - Rip DRM or non-DRM protected live streams\n\n"
    "Usage:\n"
    "Send /rip followed by the stream URL and key (if required).\n"
    "Example:\n"
    "/rip https://example.com/stream.mpd abcd1234:key5678\n\n"
    "Supported formats:\n"
    "- DASH (.mpd, DRM or non-DRM)\n"
    "- HLS (.m3u8, non-DRM)\n"
    "\nNote: Ripping DRM-protected content may require a valid key. Only use this bot for authorized content."
)

async def start_pm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start in private chat (PM)."""
    chat_type = update.effective_chat.type
    if chat_type == "private":
        await update.message.reply_text(WELCOME_MESSAGE)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message with usage instructions."""
    await update.message.reply_text(HELP_MESSAGE)

def main():
    from configparser import ConfigParser
    config = ConfigParser()
    config.read("config.ini")
    TOKEN = config.get("TELEGRAM", "Token")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_pm))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
