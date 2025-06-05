# © 2025 @Dypixx.
# Originally developed by @SHARATHITSISME and @ISMARTBOII_UJJWAL
# Modified with additional features and improvements by @Dypixx.
# Huge respect to the original creators ❤️

from pyrogram import Client, filters
from pyrogram.types import *
from configs import *
from pyrogram.errors import *
import asyncio
from Database.userdb import dy

@Client.on_message(filters.command("broadcast") & (filters.private) & filters.user(ADMIN))
async def broadcasting_func(c: Client, m: Message):
    try:
        msg = await m.reply_text("Wait a second!")
        if not m.reply_to_message:
            return await msg.edit("<b>Please reply to a message to broadcast.</b>")
        await msg.edit("Processing ...")
        completed = 0
        failed = 0
        to_copy_msg = m.reply_to_message
        users_list = await dy.get_all_users()
        
        for i, userDoc in enumerate(users_list):
            if i % 20 == 0:
                await msg.edit(f"Total: {i}\nCompleted: {completed}\nFailed: {failed}")
            user_id = userDoc.get("user_id")
            if not user_id:
                continue
            try:
                await to_copy_msg.copy(int(user_id))
                completed += 1
                await asyncio.sleep(0.1)
            except FloodWait as e:
                await asyncio.sleep(e.value)
                try:
                    await to_copy_msg.copy(int(user_id))
                    completed += 1
                except Exception:
                    failed += 1
            except Exception as e:
                print(f"Error in broadcasting to {user_id}: {e}")
                failed += 1
                
        await msg.edit(f"Successfully Broadcasted\nTotal: {len(users_list)}\nCompleted: {completed}\nFailed: {failed}")
    except Exception as e:
        print(f"Error in broadcast: {str(e)}")
        await m.reply_text("An error occurred while broadcasting.")

@Client.on_message(filters.command("ban") & filters.private & filters.user(ADMIN))
async def ban_user_cmd(c: Client, m: Message):
    try:
        command_parts = m.text.split()
        if len(command_parts) < 2:
            await m.reply_text("Usage: /ban user_id")
            return
        user_id = int(command_parts[1])
        reason = " ".join(command_parts[2:]) if len(command_parts) > 2 else None
        try:
            user = await c.get_users(user_id)
        except Exception:
            await m.reply_text("Unable to find user.")
            return
        if await dy.ban_user(user_id, reason):
            ban_message = f"User {user.mention} has been banned."
            if reason:
                ban_message += f"\nReason: {reason}"
            await m.reply_text(ban_message)
        else:
            await m.reply_text("Failed to ban user.")
    except ValueError:
        await m.reply_text("Please provide a valid user ID.")
    except Exception as e:
        await m.reply_text(f"An error occurred: {str(e)}")

@Client.on_message(filters.command("unban") & filters.private & filters.user(ADMIN))
async def unban_user_cmd(c: Client, m: Message):
    try:
        command_parts = m.text.split()
        if len(command_parts) < 2:
            await m.reply_text("Usage: /unban user_id")
            return
        user_id = int(command_parts[1])
        try:
            user = await c.get_users(user_id)
        except Exception:
            await m.reply_text("Unable to find user.")
            return
        if await dy.unban_user(user_id):
            await m.reply_text(f"User {user.mention} has been unbanned.")
        else:
            await m.reply_text("Failed to unban user or user was not banned.")
    except ValueError:
        await m.reply_text("Please provide a valid user ID.")
    except Exception as e:
        await m.reply_text(f"An error occurred: {str(e)}")