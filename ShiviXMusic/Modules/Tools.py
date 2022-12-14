import os
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from ShiviXMusic import app, Ass, BOT_NAME, SUDO_USERS
from ShiviXMusic.Helpers.Database import get_active_chats


__MODULE__ = "ππΎπΎπ»π"
__HELP__ = """

**π½πΎππ΄ :**
πΎπ½π»π π΅πΎπ πππ³πΎπ΄ππ


/joinassistant [π²π·π°π πππ΄ππ½π°πΌπ΄ πΎπ π²π·π°π πΈπ³]
Β» πΎππ³π΄π ππ·π΄ π°πππΈπππ°π½π ππΎ πΉπΎπΈπ½ ππ·π°π π²π·π°π.

/leaveassistant [π²π·π°π πππ΄ππ½π°πΌπ΄ πΎπ π²π·π°π πΈπ³]
Β» πΎππ³π΄π ππ·π΄ π°πππΈπππ°π½π ππΎ π»π΄π°ππ΄ ππ·π°π π²π·π°π.

/leavebot [π²π·π°π πππ΄ππ½π°πΌπ΄ πΎπ π²π·π°π πΈπ³]
Β» πΎππ³π΄π ππ·π΄ π±πΎπ ππΎ π»π΄π°ππ΄ ππ·π°π π²π·π°π.
"""


@app.on_message(filters.command(["activevc", "activevoice"]) & filters.user(SUDO_USERS))
async def activevc(_, message: Message):
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"**π΄πππΎπ :** {e}")
    text = ""
    j = 0
    for x in served_chats:
        try:
            title = (await app.get_chat(x)).title
        except Exception:
            title = "πΏππΈππ°ππ΄ πΆππΎππΏ"
        if (await app.get_chat(x)).username:
            user = (await app.get_chat(x)).username
            text += (
                f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})[`{x}`]\n\n"
            )
        else:
            text += f"<b>{j + 1}. {title}</b> [`{x}`]\n\n"
        j += 1
    if not text:
        await message.reply_text(f"**Β» π½πΎ π°π²ππΈππ΄ ππΈπ³π΄πΎπ²π·π°ππ πΎπ½ {BOT_NAME} ππ΄πππ΄ππ.**")
    else:
        await message.reply_text(
            f"**Β» π°π²ππΈππ΄ ππΈπ³π΄πΎπ²π·π°ππ πΎπ½ {BOT_NAME} ππ΄πππ΄π :**\n\n{text}",
            disable_web_page_preview=True,
        )


@app.on_message(filters.command(["joinassistant", "join", "ass", "assistant"]) & filters.user(SUDO_USERS))
async def assjoin(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**π΄ππ°πΌπΏπ»π΄ :**\n/joinassistant [π²π·π°π πππ΄ππ½π°πΌπ΄ πΎπ π²π·π°π πΈπ³]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await Ass.join_chat(chat)
    except Exception as e:
        await message.reply_text(f"π΅π°πΈπ»π΄π³.\n\n**ππ΄π°ππΎπ½ :** {e}")
        return
    await message.reply_text("**Β» πππ²π²π΄πππ΅ππ»π»π πΉπΎπΈπ½π΄π³ ππ·π°π π²π·π°π.**")


@app.on_message(filters.command(["leavebot", "leave"]) & filters.user(SUDO_USERS))
async def botl(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**π΄ππ°πΌπΏπ»π΄ :**\n/leavebot [π²π·π°π πππ΄ππ½π°πΌπ΄ πΎπ π²π·π°π πΈπ³]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await app.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"π΅π°πΈπ»π΄π³\n**ππ΄π°ππΎπ½ :** {e}")
        print(e)
        return
    await message.reply_text("**Β» πππ²π²π΄πππ΅ππ»π»π π»π΄π΅π ππ·π°π π²π·π°π.**")


@app.on_message(filters.command(["leaveassistant", "assleave", "userbotleave", "leaveass"]) & filters.user(SUDO_USERS))
async def assleave(_, message):
    if len(message.command) != 2:
        await message.reply_text(
            "**π΄ππ°πΌπΏπ»π΄ :**\n/assleave [π²π·π°π πππ΄ππ½π°πΌπ΄ πΎπ π²π·π°π πΈπ³]"
        )
        return
    chat = message.text.split(None, 2)[1]
    try:
        await Ass.leave_chat(chat)
    except Exception as e:
        await message.reply_text(f"π΅π°πΈπ»π΄π³\n**ππ΄π°ππΎπ½ :** {e}")
        return
    await message.reply_text("**Β» π°πππΈπππ°π½π πππ²π²π΄πππ΅ππ»π»π π»π΄π΅π ππ·π°π π²π·π°π.**")
