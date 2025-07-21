from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes
from task_manager import get_task, reset_task

async def send_task_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎞 MP4", callback_data="format_mp4"),
         InlineKeyboardButton("🎥 MKV", callback_data="format_mkv")],
        [InlineKeyboardButton("💾 Save Task", callback_data="save_task"),
         InlineKeyboardButton("❌ Cancel Task", callback_data="cancel_task")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Choose format and save task:", reply_markup=reply_markup)

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_id = query.from_user.id
    task = get_task(user_id)
    await query.answer()

    if query.data.startswith("format_"):
        task.format = query.data.split("_")[1]
        await query.edit_message_text(f"📁 Format set to: {task.format.upper()}")
    elif query.data == "save_task":
        await send_upload_options(update, context)
    elif query.data == "cancel_task":
        reset_task(user_id)
        await query.edit_message_text("❌ Task cancelled.")
    elif query.data.startswith("upload_"):
        task.destination = query.data.split("_")[1]
        await query.edit_message_text(f"✅ Task saved!\nFormat: {task.format.upper()}, Upload: {task.destination.title()}")
        # Now you would trigger the actual rip and upload process

async def send_upload_options(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("☁️ Google Drive", callback_data="upload_gdrive")],
        [InlineKeyboardButton("📤 Telegram", callback_data="upload_telegram")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.edit_message_text("Select upload destination:", reply_markup=reply_markup)  # Inline keyboard logic placeholder
