from os import getenv as genv

API_ID = genv("API_ID", "")
API_HASH = genv("API_HASH", "")
BOT_TOKEN = genv("BOT_TOKEN", "")
ADMIN = int(genv("ADMIN", ""))

DATABASE_URL = genv("DATABASE_URL", "")

IS_FSUB = bool(genv("FSUB", True))
AUTH_CHANNELS = list(map(int, genv("AUTH_CHANNEL", "").split()))

CHANNEL_LINK = genv("CHANNEL_LINK", "https://telegram.me/DypixxTech")
REPO_LINK = genv("REPO_LINK", "https://github.com/Dypixx/LinkXpert")


START_TXT = '''<b>{},

🔗 I can convert your links into short links using your API.

📘 Click the Help button below to get more info.

🚀 Let's get started!

<blockquote>⚡ Uᴘᴅᴀᴛᴇs - @DypixxTech</blockquote></b>'''

HELP_TXT = '''<b>🆘 Help Menu

» This bot allows you to convert **any link** into a short URL using your favorite shortener service!

» To set your preferred shortener and API key, use the command below:

» Example: `/set_shortner [site] [api_key]`

» To check your currently connected site and API key using: /info

» Once set, every link you send will be automatically shortened using your selected service.

<blockquote>📌 You can change or update your shortener anytime using the same command..</blockquote></b>'''

ABOUT_TXT = '''<b>╔════❰ {} ❱════❍
║ ┏━━━━━━━━━❥
║ ┣ My Owner ->  <a href='https://telegram.me/Dypixx'>Dypixx</a>
║ ┣ Library -> Pyrogram
║ ┣ Language -> Python
║ ┣ Hosted On -> VPS
║ ┗━━━━━━━━━❥
╚════❰ <a href='https://telegram.me/DypixxTech'>DypixxTech</a> ❱════❍</b>'''
