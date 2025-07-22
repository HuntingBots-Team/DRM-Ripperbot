from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

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
