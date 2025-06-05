# © 2025 @Dypixx.
# Originally developed by @SHARATHITSISME and @ISMARTBOII_UJJWAL
# Modified with additional features and improvements by @Dypixx
# Huge respect to the original creators ❤️

from bot import bot
from pyrogram import idle

async def start():
    await bot.start()

bot.loop.create_task(start())
idle()