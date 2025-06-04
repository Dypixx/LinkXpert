from os import getenv as genv

API_ID = genv("API_ID", "27339145")
API_HASH = genv("API_HASH", "e620f86919c34496729285dd2a6d35e6")
BOT_TOKEN = genv("BOT_TOKEN", "7784529867:AAG9-hYNVY_g1bH28yCOxX_uavCNiehBXd8")
ADMIN = int(genv("ADMIN", "1782834874"))

BASE_URL = genv("BASE_URL", "api.gplinks.com")
DATABASE_URL = genv("DATABASE_URL", "mongodb+srv://starcinebot:mkooaa@werdeveloper.vxfam.mongodb.net/?retryWrites=true&w=majority&appName=werdeveloper")

IS_FSUB = bool(genv("FSUB", True))
AUTH_CHANNELS = list(map(int, genv("AUTH_CHANNEL", "-1002421861644").split()))

CHANNEL_LINK = genv("CHANNEL_LINK", "https://telegram.me/DypixxTech")
REPO_LINK = genv("REPO_LINK", "https://telegram.me/DypixxTech")


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
