import os
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from ShiviXMusic import app, Ass, BOT_NAME, SUDO_USERS
from ShiviXMusic.Helpers.Database import get_active_chats


__MODULE__ = "𝚃𝙾𝙾𝙻𝚂"
__HELP__ = """

**𝙽𝙾𝚃𝙴 :**
𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚂𝚄𝙳𝙾𝙴𝚁𝚂


/joinassistant [𝙲𝙷𝙰𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 𝙸𝙳]
» 𝙾𝚁𝙳𝙴𝚁 𝚃𝙷𝙴 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚃𝙾 𝙹𝙾𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃.

/leaveassistant [𝙲𝙷𝙰𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 𝙸𝙳]
» 𝙾𝚁𝙳𝙴𝚁 𝚃𝙷𝙴 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚃𝙾 𝙻𝙴𝙰𝚅𝙴 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃.

/leavebot [𝙲𝙷𝙰𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 𝙸𝙳]
» 𝙾𝚁𝙳𝙴𝚁 𝚃𝙷𝙴 𝙱𝙾𝚃 𝚃𝙾 𝙻𝙴𝙰𝚅𝙴 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃.
"""


@app.on_message(filters.command(["activevc", "activevoice"]) & filters.user(SUDO_USERS))
async def activevc(_, message: Message):
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"**𝙴𝚁𝚁𝙾𝚁 :** {e}")
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙶𝚁𝙾𝚄𝙿"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += (
                f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n\n"
            )
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n\n"
        j += 1
    if not text:
        await message.reply_text(f"**» 𝙽𝙾 𝙰𝙲𝚃𝙸𝚅𝙴 𝚅𝙸𝙳𝙴𝙾𝙲𝙷𝙰𝚃𝚂 𝙾𝙽 {BOT_NAME} 𝚂𝙴𝚁𝚅𝙴𝚁𝚂.**")
    else:
        await message.reply_text(
            f"**» 𝙰𝙲𝚃𝙸𝚅𝙴 𝚅𝙸𝙳𝙴𝙾𝙲𝙷𝙰𝚃𝚂 𝙾𝙽 {BOT_NAME} 𝚂𝙴𝚁𝚅𝙴𝚁 :**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["joinassistant", "join", "ass", "assistant"]) & filters.user(SUDO_USERS))
async def assjoin(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/joinassistant [𝙲𝙷𝙰𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 𝙸𝙳]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await Ass.join_chat(chat)
    except Exception as e:
        await message.reply_text(f"𝙵𝙰𝙸𝙻𝙴𝙳.\n\n**𝚁𝙴𝙰𝚂𝙾𝙽 :** {e}")
        return
    await message.reply_text("**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽𝙴𝙳 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃.**")


@app.on_message(filters.command(["leavebot", "leave"]) & filters.user(SUDO_USERS))
async def botl(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/leavebot [𝙲𝙷𝙰𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 𝙸𝙳]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await app.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"𝙵𝙰𝙸𝙻𝙴𝙳\n**𝚁𝙴𝙰𝚂𝙾𝙽 :** {e}")
        print(e)
        return
    await message.reply_text("**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙻𝙴𝙵𝚃 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃.**")


@app.on_message(filters.command(["leaveassistant", "assleave", "userbotleave", "leaveass"]) & filters.user(SUDO_USERS))
async def assleave(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/assleave [𝙲𝙷𝙰𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝙲𝙷𝙰𝚃 𝙸𝙳]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await Ass.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"𝙵𝙰𝙸𝙻𝙴𝙳\n**𝚁𝙴𝙰𝚂𝙾𝙽 :** {e}")
        return
    await message.reply_text("**» 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙻𝙴𝙵𝚃 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝚃.**")
