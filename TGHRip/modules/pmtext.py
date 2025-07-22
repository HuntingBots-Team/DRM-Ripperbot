from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
👋 Welcome to TGHRip!

🔧 Owner: @The_Ghost_Hunter
📣 Updates: https://t.me/allhindi_stories
💬 Support: https://t.me/TGHLeechSupport2

This bot allows you to rip DRM and non-DRM protected live streams.
Type /help for available commands.

<b>Note:</b>
- Only use this bot for authorized content.
- Abuse or misuse may result in a ban.
"""

    HELP_MESSAGE = """
📖 TGHRip Help

<b>Commands:</b>
/start - Show the welcome message
/help - Show this help message
/rip <url> <key> - Rip DRM or non-DRM protected live streams

<b>Usage:</b>
Send /rip followed by the stream URL and key (if required).
Example:
/rip https://example.com/stream.mpd abcd1234:key5678

<b>Supported formats:</b>
- DASH (.mpd, DRM or non-DRM)
- HLS (.m3u8, non-DRM)

<b>Note:</b> Ripping DRM-protected content may require a valid key. Only use this bot for authorized content.
"""
