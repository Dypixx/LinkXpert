# © 2025 @Dypixx.
# Originally developed by @SHARATHITSISME and @ISMARTBOII_UJJWAL
# Modified with additional features and improvements by @Dypixx.
# Huge respect to the original creators ❤️

from pyrogram import Client, filters
from pyrogram.types import *
from configs import *
from pyrogram.errors import *
from Database.shortdb import db
from Database.userdb import dy
from .utils import save_data, short_link, get_fsub
from pyrogram.errors import *

@Client.on_message(filters.command('start') & filters.private)
async def start_handler(c, m):
    try:
        if await dy.is_user_banned(m.from_user.id):
            await m.reply("**🚫 You are banned from using this bot**",
                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support", user_id=int(ADMIN))]]))
            return
        if await dy.get_user(m.from_user.id) is None:
            await dy.addUser(m.from_user.id, m.from_user.first_name)
            await db.add(m.from_user.id)
        await m.reply_text(
            START_TXT.format(m.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Updates", url=CHANNEL_LINK)],
                [InlineKeyboardButton("❓ Help ", callback_data="help"),
                 InlineKeyboardButton("ℹ️ About", callback_data="about")],
                [InlineKeyboardButton("🛠️ Source", url=REPO_LINK)]])
        )
    except Exception as u:
        await m.reply(f"{str(u)}")

@Client.on_message(filters.command('set_shortner') & filters.private)
async def save_shortlink(c, m):
    if await dy.is_user_banned(m.from_user.id):
            await m.reply("**🚫 You are banned from using this bot**",
                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support", user_id=int(ADMIN))]]))
            return
    if IS_FSUB and not await get_fsub(c, m):return
    if len(m.command) < 3:
        await m.reply_text(
            "**❌ Please provide both the Shortener URL and API key along with the command.\n\nExample: `/set_shortner example.com your_api_key`\n\n>⚡ Updates: @DypixxTech**",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔓 Close", callback_data="delete")]]))
        return    
    usr = m.from_user
    elg = await save_data((m.command[1].replace("/", "").replace("https:", "").replace("http:", "")), m.command[2], uid=usr.id)
    if elg:
        await m.reply_text(f"**✅ Shortener has been set successfully!\n\nShortener URL - {await db.get_value('shortner', uid=usr.id)}\nShortener API - {await db.get_value('api', uid=usr.id)}\n\n>⚡ Updates - @DypixxTech**",
                           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔓 Close", callback_data="delete")]]))
    else:       
        await m.reply_text(f"**⚠️ Error:\n\nYour Shortlink API or URL is invalid, please check again!**",
                           reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔓 Close", callback_data="delete")]]))    
    

@Client.on_message(filters.command('info') & filters.private)
async def showinfo(c, m):
    if await dy.is_user_banned(m.from_user.id):
            await m.reply("**🚫 You are banned from using this bot**",
                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support", user_id=int(ADMIN))]]))
            return
    usr = m.from_user
    site = await db.get_value('shortner', uid=usr.id)
    api = await db.get_value('api', uid=usr.id)
    await m.reply_text(f"**🔐 Your Information\n\n👤 User: {usr.mention}\n🆔 User ID: `{usr.id}`\n\n🌐 Connected Site: `{site}`\n🔗 Connected API: `{api}`\n\n>⚡ Uᴘᴅᴀᴛᴇs - @DypixxTech**",
                       reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔓 Close", callback_data="delete")]]))


@Client.on_message(filters.text & filters.private)
async def shorten_link(_, m):
    if await dy.is_user_banned(m.from_user.id):
            await m.reply("**🚫 You are banned from using this bot**",
                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Support", user_id=int(ADMIN))]]))
            return
    if IS_FSUB and not await get_fsub(_, m):return
    txt = m.text
    if txt.startswith("/"):return
    if not ("http://" in txt or "https://" in txt):
        await m.reply_text("Please send a valid link to shorten.")
        return
    usr = m.from_user
    try:
        short = await short_link(link=txt, uid=usr.id)
        msg = f"**✨ 𝐘𝐨𝐮𝐫 𝐒𝐡𝐨𝐫𝐭 𝐋𝐢𝐧𝐤 𝐢𝐬 𝐑𝐞𝐚𝐝𝐲!\n\n🔗 𝗟𝗶𝗻𝗸: <code>{short}</code>\n\n>📢 Stay updated: @DypixxTech**"
        await m.reply_text(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔓 Close", callback_data="delete")]]))
    except Exception as e:
        await m.reply_text(f"Error shortening link: {e}")


