import os
import config
import asyncio

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from ShiviXMusic import BOT_ID, BOT_NAME, SUDO_USERS, app
from ShiviXMusic.Helpers.Database import (add_gban_user, get_served_chats, is_gbanned_user, remove_gban_user)


__MODULE__ = "𝙶-𝙱𝙰𝙽"
__HELP__ = """

**𝙽𝙾𝚃𝙴 :**
𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚂𝚄𝙳𝙾𝙴𝚁𝚂.

/gban [𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁]
» 𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙸𝙽 𝙰𝙻𝙻 𝚃𝙷𝙴 𝚂𝙴𝚁𝚅𝙴𝚁 𝙲𝙷𝙰𝚃𝚂.

/ungban [𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁]
» 𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝚄𝙽𝙱𝙰𝙽𝚂 𝚃𝙷𝚁 𝙶-𝙱𝙰𝙽𝙽𝙴𝙳 𝚄𝚂𝙴𝚁.
"""


@app.on_message(filters.command("gban") & filters.user(SUDO_USERS))
async def ban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/gban [𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴/𝙸𝙳]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            return await message.reply_text(
                "**» 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙶𝙱𝙰𝙽 𝚈𝙾𝚄𝚁𝚂𝙴𝙻𝙵 !**"
            )
        elif user.id == BOT_ID:
            await message.reply_text("» 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙼𝙴 𝚃𝙾 𝙶𝙱𝙰𝙽 𝙼𝚈𝚂𝙴𝙻𝙵, 𝙽𝙾𝙾𝙱𝚂 !")
        elif user.id in SUDO_USERS:
            await message.reply_text("» 𝚈𝙾𝚄 𝙱𝙻𝙾𝙾𝙳𝚈, 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙼𝙴 𝚃𝙾 𝙶𝙱𝙰𝙽 𝙼𝚈 𝙱𝙰𝙱𝚈, 𝙸 𝚆𝙸𝙻𝙻 𝙵𝚄*𝙺 𝚈𝙾𝚄 𝙷𝙰𝚁𝙳 𝙰𝙽𝙳 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙱𝙴 𝙰𝙱𝙻𝙴 𝚃𝙾 𝙵𝚄*𝙺 𝙰𝙽𝚈𝙾𝙽𝙴 𝙰𝙶𝙰𝙸𝙽 !")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝙱𝙰𝙽𝙽𝙸𝙽𝙶 {user.mention}**\n\n𝙴𝚇𝙿𝙴𝙲𝚃𝙴𝙳 𝚃𝙸𝙼𝙴 : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.kick_chat_member(sex, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
**𝙶-𝙱𝙰𝙽 𝙾𝙽 {BOT_NAME}**

**• 𝙲𝙷𝙰𝚃 :** {message.chat.title} [`{message.chat.id}`]
**• 𝚂𝚄𝙳𝙾𝙴𝚁 :** {from_user.mention}
**• 𝚄𝚂𝙴𝚁 :** {user.mention}
**• 𝚄𝚂𝙴𝚁 𝙸𝙳:** `{user.id}`
**• 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽 :** {number_of_chats} 𝙲𝙷𝙰𝚃𝚂"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id == from_user_id:
        await message.reply_text("» 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙶𝙱𝙰𝙽 𝚈𝙾𝚄𝚁𝚂𝙴𝙻𝙵 !")
    elif user_id == BOT_ID:
        await message.reply_text("» 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙼𝙴 𝚃𝙾 𝙶𝙱𝙰𝙽 𝙼𝚈𝚂𝙴𝙻𝙵, 𝙽𝙾𝙾𝙱𝚂 !")
    elif user_id in SUDO_USERS:
        await message.reply_text("» 𝚈𝙾𝚄 𝙱𝙻𝙾𝙾𝙳𝚈, 𝚈𝙾𝚄 𝚆𝙰𝙽𝚃 𝙼𝙴 𝚃𝙾 𝙶𝙱𝙰𝙽 𝙼𝚈 𝙱𝙰𝙱𝚈, 𝙸 𝚆𝙸𝙻𝙻 𝙵𝚄*𝙺 𝚈𝙾𝚄 𝙷𝙰𝚁𝙳 𝙰𝙽𝙳 𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙱𝙴 𝙰𝙱𝙻𝙴 𝚃𝙾 𝙵𝚄*𝙺 𝙰𝙽𝚈𝙾𝙽𝙴 𝙰𝙶𝙰𝙸𝙽 !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("**𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝚃𝙷𝙰𝚃 𝙲𝙷𝚄𝙼𝚃𝙸𝚈𝙰.**")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝙱𝙰𝙽𝙽𝙸𝙽𝙶 {mention}**\n\n𝙴𝚇𝙿𝙴𝙲𝚃𝙴𝙳 𝚃𝙸𝙼𝙴 : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.kick_chat_member(sex, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
**𝙶-𝙱𝙰𝙽 𝙾𝙽 {BOT_NAME}**

**• 𝙲𝙷𝙰𝚃 :** {message.chat.title} [`{message.chat.id}`]
**• 𝚂𝚄𝙳𝙾𝙴𝚁 :** {from_user_mention}
**• 𝚄𝚂𝙴𝚁 :** {mention}
**• 𝚄𝚂𝙴𝚁 𝙸𝙳:** `{user_id}`
**• 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽 :** {number_of_chats} 𝙲𝙷𝙰𝚃𝚂"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@app.on_message(filters.command("ungban") & filters.user(SUDO_USERS))
async def unban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/ungban [𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴/𝙸𝙳]"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            await message.reply_text("» 𝙸 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝚃𝙾𝙻𝙳 𝚈𝙾𝚄 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙶𝙱𝙰𝙽 𝚈𝙾𝚄𝚁𝚂𝙴𝙻𝙵 𝚂𝙾 𝙷𝙾𝚆 𝚃𝙷𝙴 𝙵𝚄*𝙺 𝚈𝙾𝚄𝚁'𝚁𝙴 𝚃𝚈𝙿𝙸𝙽𝙶 𝚃𝙾 𝚄𝙽𝙶𝙱𝙰𝙽 𝚈𝙾𝚄𝚁𝚂𝙴𝙻𝙵 !")
        elif user.id == BOT_ID:
            await message.reply_text("» 𝙱𝙻𝙾𝙾𝙳𝚈 𝙽𝙾𝙾𝙱, 𝙸'𝙼 𝚃𝙴𝙻𝙻𝙸𝙽𝙶 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙲𝙾𝙼𝙴 𝙱𝙰𝙲𝙺 𝙰𝙶𝙰𝙸𝙽 𝙴𝙻𝚂𝙴 𝙸 𝚆𝙸𝙻𝙻 𝚃𝙴𝙻𝙻 𝙼𝚈 𝙱𝙰𝙱𝚈 𝚃𝙾 𝙵𝚄*𝙺 𝚈𝙾𝚄 𝚄𝙿 !")
        elif user.id in SUDO_USERS:
            await message.reply_text("» 𝚁𝙴𝙰𝙳 𝚃𝙷𝙸𝚂 𝚂𝚃𝙰𝚃𝙴𝙼𝙴𝙽𝚃 𝙻𝙰𝚂𝚃 𝚃𝙸𝙼𝙴, 𝙸'𝙼 𝙽𝙾𝚃 𝙶𝙾𝙽𝙽𝙰 𝚃𝙴𝙻𝙻 𝚈𝙾𝚄 𝙰𝙶𝙰𝙸𝙽-𝙽-𝙰𝙶𝙰𝙸𝙽 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙶𝙱𝙰𝙽 𝙼𝚈 𝙱𝙰𝙱𝚈 !")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("» 𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙽𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 !")
            else:
                await remove_gban_user(user.id)
                await message.reply_text(f"» 𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃...")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id == from_user_id:
        await message.reply_text("» 𝙸 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝚃𝙾𝙻𝙳 𝚈𝙾𝚄 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙶𝙱𝙰𝙽 𝚈𝙾𝚄𝚁𝚂𝙴𝙻𝙵 𝚂𝙾 𝙷𝙾𝚆 𝙵𝚄*𝙺 𝚈𝙾𝚄'𝚁𝙴 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚄𝙽𝙶𝙱𝙰𝙽 𝚈𝙾𝚄𝚁𝚂𝙴𝙻𝙵 !")
    elif user_id == BOT_ID:
        await message.reply_text(
            "» 𝙱𝙻𝙾𝙾𝙳𝚈 𝙽𝙾𝙾𝙱, 𝙸'𝙼 𝚃𝙴𝙻𝙻𝙸𝙽𝙶 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙲𝙾𝙼𝙴 𝙱𝙰𝙲𝙺 𝙰𝙶𝙰𝙸𝙽 𝙴𝙻𝚂𝙴 𝙸 𝚆𝙸𝙻𝙻 𝚃𝙴𝙻𝙻 𝙼𝚈 𝙱𝙰𝙱𝚈 𝚃𝙾 𝙵𝚄*𝙺 𝚈𝙾𝚄 𝚄𝙿 !"
        )
    elif user_id in SUDO_USERS:
        await message.reply_text("» 𝚁𝙴𝙰𝙳 𝚃𝙷𝙸𝚂 𝚂𝚃𝙰𝚃𝙴𝙼𝙴𝙽𝚃 𝙻𝙰𝚂𝚃 𝚃𝙸𝙼𝙴, 𝙸'𝙼 𝙽𝙾𝚃 𝙶𝙾𝙽𝙽𝙰 𝚃𝙴𝙻𝙻 𝚈𝙾𝚄 𝙰𝙶𝙰𝙸𝙽-𝙽-𝙰𝙶𝙰𝙸𝙽 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝙶𝙱𝙰𝙽 𝙼𝚈 𝙱𝙰𝙱𝚈 !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("» 𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁 𝙸𝚂 𝙽𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 !")
        else:
            await remove_gban_user(user_id)
            await message.reply_text(f"» 𝚁𝙴𝙼𝙾𝚅𝙴𝙳 𝙵𝚁𝙾𝙼 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃...")



chat_watcher_group = 5

@app.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.kick_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"{checking} 𝙸𝚂 𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝙱𝙰𝙽𝙽𝙴𝙳 𝙾𝙽 {BOT_NAME}\n\n**𝚁𝙴𝙰𝚂𝙾𝙽 :** ʙʜᴀᴅᴠᴀ sᴀᴀʟᴀ, ʀᴀɴᴅɪʙᴀᴀᴢ, ʙᴇʜᴇɴ ᴋᴀ ʟᴏᴅᴀ."
        )
