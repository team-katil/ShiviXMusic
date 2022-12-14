import os
import asyncio
import subprocess

from pyrogram import filters
from pyrogram.types import Message

from ShiviXMusic import BOT_NAME, OWNER_ID, SUDO_USERS, app
from ShiviXMusic.Helpers.Database import (get_active_chats, get_served_chats, remove_active_chat)


__MODULE__ = "πππ³πΎ"
__HELP__ = """

/sudolist 
Β» ππ·πΎππ ππ·π΄ π»πΈππ πΎπ΅ πππ³πΎπ΄ππ.

**π½πΎππ΄ :**
πΎπ½π»π π΅πΎπ πππ³πΎ πππ΄ππ.

/restart 
Β» ππ΄πππ°πππ ππ·π΄ π±πΎπ πΎπ½ ππΎππ ππ΄πππ΄π.

/update 
Β» π΅π΄ππ²π· ππΏπ³π°ππ΄π π΅ππΎπΌ ππ·π΄ ππ΄πΏπΎ.

/clean
Β» π²π»π΄π°π½ π°π»π» ππ·π΄ ππ΄πΌπΏ π³πΈππ΄π²ππΎππΈπ΄π.
"""


@app.on_message(filters.command(["sudolist", "listsudo", "sudo", "owner"]))
async def sudoers_list(_, message: Message):
    sudoers = SUDO_USERS
    text = "<u>π₯ **πΎππ½π΄π :**</u>\n"
    wtf = 0
    for x in OWNER_ID:
        try:
            user = await app.get_users(x)
            user = user.first_name if not user.mention else user.mention
            wtf += 1
        except Exception:
            continue
        text += f"{wtf}β» {user}\n"
    smex = 0
    for count, user_id in enumerate(sudoers, 1):
        if user_id not in OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\nβ¨<u> **πππ³πΎπ΄ππ :**</u>\n"
                wtf += 1
                text += f"{wtf}β» {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("**Β» π½πΎ πππ³πΎ πππ΄ππ π΅πΎππ½π³.**")
    else:
        await message.reply_text(text)



## Restart

@app.on_message(filters.command("restart") & filters.user(OWNER_ID))
async def theme_func(_, message):
    served_chats = []
    try:
        chats = await get_active_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        pass
    for x in served_chats:
        try:
            await app.send_message(
                x,
                f"Β» {BOT_NAME} πΉπππ ππ΄πππ°πππ΄π³ π΅πΎπ π΅π΄ππ²π·πΈπ½πΆ ππΏπ³π°ππ΄π π΅ππΎπΌ ππ·π΄ ππ΄πππ΄π.\n\nππΎπππ π΅πΎπ ππ·π΄ πΈπ½π²πΎπ½ππ΄π½πΈπ΄π½π²π΄.",
            )
            await remove_active_chat(x)
        except Exception:
            pass
    x = await message.reply_text(f"**ππ΄πππ°πππΈπ½πΆ {BOT_NAME}\n\nπΏπ»π΄π°ππ΄ ππ°πΈπ...**")
    os.system(f"kill -9 {os.getpid()} && python3 -m ShiviXMusic")



## Update

@app.on_message(filters.command("update") & filters.user(SUDO_USERS))
async def update(_, message):
    m = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if str(m[0]) != "A":
        x = await message.reply_text("**Β» π΅π΄ππ²π·πΈπ½πΆ ππΏπ³π°ππ΄π π΅ππΎπΌ ππ΄πΏπΎ π°π½π³ ππππΈπ½πΆ ππΎ ππ΄πππ°ππ...**")
        return os.system(f"kill -9 {os.getpid()} && python3 -m ShiviXMusic")
    else:
        await message.reply_text(f"**Β» {BOT_NAME} πΈπ π°π»ππ΄π°π³π ππΏ-ππΎ-π³π°ππ΄ !**")



## Broadcast

@app.on_message(filters.command("broadcast") & filters.user(SUDO_USERS))
async def broadcast(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(f"**πππ²π²π΄πππ΅ππ»π»π π±ππΎπ°π³π²π°πππ΄π³ ππ·π΄ πΌπ΄πππ°πΆπ΄ πΈπ½ {sent} π²π·π°ππ.**")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**π΄ππ°πΌπΏπ»π΄ :**\n/broadcast [πΌπ΄πππ°πΆπ΄] πΎπ [ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**Β» πππ²π²π΄πππ΅ππ»π»π π±ππΎπ°π³π²π°πππ΄π³ ππ·π΄ πΌπ΄πππ°πΆπ΄ πΈπ½ {sent} π²π·π°ππ.**")



@app.on_message(filters.command("broadcast_pin") & filters.user(SUDO_USERS))
async def broadcast_message_pin_silent(_, message):
    if not message.reply_to_message:
        pass
    else:
        x = message.reply_to_message.message_id
        y = message.chat.id
        sent = 0
        pin = 0
        chats = []
        schats = await get_served_chats()
        for chat in schats:
            chats.append(int(chat["chat_id"]))
        for i in chats:
            try:
                m = await app.forward_messages(i, y, x)
                try:
                    await m.pin(disable_notification=True)
                    pin += 1
                except Exception:
                    pass
                await asyncio.sleep(0.3)
                sent += 1
            except Exception:
                pass
        await message.reply_text(
            f"**Β» π±ππΎπ°π³π²π°πππ΄π³ πΌπ΄πππ°πΆπ΄ πΈπ½ {sent} π²π·π°ππ π°π½π³ πΏπΈπ½π½π΄π³ πΈπ½ {pin} π²π·π°ππ.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**π΄ππ°πΌπΏπ»π΄ :**\n/broadcast [πΌπ΄πππ°πΆπ΄] πΎπ [ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄]"
        )
        return
    text = message.text.split(None, 1)[1]
    sent = 0
    pin = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            m = await app.send_message(i, text=text)
            try:
                await m.pin(disable_notification=False)
                pin += 1
            except Exception:
                pass
            await asyncio.sleep(0.3)
            sent += 1
        except Exception:
            pass
    await message.reply_text(
        f"**Β» π±ππΎπ°π³π²π°πππ΄π³ πΌπ΄πππ°πΆπ΄ πΈπ½ {sent} π²π·π°ππ π°π½π³ πΏπΈπ½π½π΄π³ πΈπ½ {pin} π²π·π°ππ.**"
    )


# Clean

@app.on_message(filters.command("clean") & filters.user(SUDO_USERS))
async def clean(_, message):
    dir = "ShiviXMusic/Cache"
    ls_dir = os.listdir(dir)
    if ls_dir:
        for dta in os.listdir(dir):
            os.system("rm -rf *.png *.jpg")
        await message.reply_text("**Β» πππ²π²π΄πππ΅ππ»π»π π²π»π΄π°π½π΄π³ π°π»π» ππ΄πΌπΏπΎππ°ππ π³πΈππ΄π²ππΎππΈπ΄π !**")
    else:
        await message.reply_text("**Β» πππ²π²π΄πππ΅ππ»π»π π²π»π΄π°π½π΄π³ π°π»π» ππ΄πΌπΏπΎππ°ππ π³πΈππ΄π²ππΎππΈπ΄π !**")
