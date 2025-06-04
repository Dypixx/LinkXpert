from pyrogram import Client
from configs import *
from pyrogram.types import *
from pyrogram.errors import *

@Client.on_callback_query()
async def callback(bot: Client, query: CallbackQuery):
    me = await bot.get_me()
    data = query.data
    msg = query.message

    if data == "delete":
        await query.answer("Thank you for closing!", show_alert=True)
        await msg.delete()

    elif data == "help":
        await msg.edit(
            HELP_TXT,
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="start")]])
        )

    elif data == "about":
        await msg.edit(
            ABOUT_TXT.format(me.mention),
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("◀️ Back", callback_data="start")]]),
            disable_web_page_preview=True
        )

    elif data == "start":
        await msg.edit(
            START_TXT.format(query.from_user.mention),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📢 Updates", url=CHANNEL_LINK)],
                [InlineKeyboardButton("❓ Help ", callback_data="help"),
                 InlineKeyboardButton("ℹ️ About", callback_data="about")],
                [InlineKeyboardButton("🛠️ Source", url=REPO_LINK)]
            ])
        )
