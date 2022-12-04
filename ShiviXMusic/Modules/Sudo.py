import os
import asyncio
import subprocess

from pyrogram import filters
from pyrogram.types import Message

from ShiviXMusic import BOT_NAME, OWNER_ID, SUDO_USERS, app
from ShiviXMusic.Helpers.Database import (get_active_chats, get_served_chats, remove_active_chat)


__MODULE__ = "𝚂𝚄𝙳𝙾"
__HELP__ = """

/sudolist 
» 𝚂𝙷𝙾𝚆𝚂 𝚃𝙷𝙴 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚂𝚄𝙳𝙾𝙴𝚁𝚂.

**𝙽𝙾𝚃𝙴 :**
𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂.

/restart 
» 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝚂 𝚃𝙷𝙴 𝙱𝙾𝚃 𝙾𝙽 𝚈𝙾𝚄𝚁 𝚂𝙴𝚁𝚅𝙴𝚁.

/update 
» 𝙵𝙴𝚃𝙲𝙷 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝚁𝙴𝙿𝙾.

/clean
» 𝙲𝙻𝙴𝙰𝙽 𝙰𝙻𝙻 𝚃𝙷𝙴 𝚃𝙴𝙼𝙿 𝙳𝙸𝚁𝙴𝙲𝚃𝙾𝚁𝙸𝙴𝚂.
"""


@app.on_message(filters.command(["sudolist", "listsudo", "sudo", "owner"]))
async def sudoers_list(_, message: Message):
    sudoers = SUDO_USERS
    text = "<u>🥀 **𝙾𝚆𝙽𝙴𝚁 :**</u>\n"
    wtf = 0
    for x in OWNER_ID:
        try:
            user = await app.get_users(x)
            user = user.first_name if not user.mention else user.mention
            wtf += 1
        except Exception:
            continue
        text += f"{wtf}➻ {user}\n"
    smex = 0
    for count, user_id in enumerate(sudoers, 1):
        if user_id not in OWNER_ID:
            try:
                user = await app.get_users(user_id)
                user = user.first_name if not user.mention else user.mention
                if smex == 0:
                    smex += 1
                    text += "\n✨<u> **𝚂𝚄𝙳𝙾𝙴𝚁𝚂 :**</u>\n"
                wtf += 1
                text += f"{wtf}➻ {user}\n"
            except Exception:
                continue
    if not text:
        await message.reply_text("**» 𝙽𝙾 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂 𝙵𝙾𝚄𝙽𝙳.**")
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
                f"» {BOT_NAME} 𝙹𝚄𝚂𝚃 𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝙵𝙾𝚁 𝙵𝙴𝚃𝙲𝙷𝙸𝙽𝙶 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙵𝚁𝙾𝙼 𝚃𝙷𝙴 𝚂𝙴𝚁𝚅𝙴𝚁.\n\n𝚂𝙾𝚁𝚁𝚈 𝙵𝙾𝚁 𝚃𝙷𝙴 𝙸𝙽𝙲𝙾𝙽𝚅𝙴𝙽𝙸𝙴𝙽𝙲𝙴.",
            )
            await remove_active_chat(x)
        except Exception:
            pass
    x = await message.reply_text(f"**𝚁𝙴𝚂𝚃𝙰𝚁𝚃𝙸𝙽𝙶 {BOT_NAME}\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...**")
    os.system(f"kill -9 {os.getpid()} && python3 -m ShiviXMusic")



## Update

@app.on_message(filters.command("update") & filters.user(SUDO_USERS))
async def update(_, message):
    m = subprocess.check_output(["git", "pull"]).decode("UTF-8")
    if str(m[0]) != "A":
        x = await message.reply_text("**» 𝙵𝙴𝚃𝙲𝙷𝙸𝙽𝙶 𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙵𝚁𝙾𝙼 𝚁𝙴𝙿𝙾 𝙰𝙽𝙳 𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚁𝙴𝚂𝚃𝙰𝚁𝚃...**")
        return os.system(f"kill -9 {os.getpid()} && python3 -m ShiviXMusic")
    else:
        await message.reply_text(f"**» {BOT_NAME} 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝚄𝙿-𝚃𝙾-𝙳𝙰𝚃𝙴 !**")



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
        await message.reply_text(f"**𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃𝙴𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙸𝙽 {sent} 𝙲𝙷𝙰𝚃𝚂.**")
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/broadcast [𝙼𝙴𝚂𝚂𝙰𝙶𝙴] 𝙾𝚁 [𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴]"
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
    await message.reply_text(f"**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃𝙴𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙸𝙽 {sent} 𝙲𝙷𝙰𝚃𝚂.**")



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
            f"**» 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙸𝙽 {sent} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙿𝙸𝙽𝙽𝙴𝙳 𝙸𝙽 {pin} 𝙲𝙷𝙰𝚃𝚂.**"
        )
        return
    if len(message.command) < 2:
        await message.reply_text(
            "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/broadcast [𝙼𝙴𝚂𝚂𝙰𝙶𝙴] 𝙾𝚁 [𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴]"
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
        f"**» 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃𝙴𝙳 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙸𝙽 {sent} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙿𝙸𝙽𝙽𝙴𝙳 𝙸𝙽 {pin} 𝙲𝙷𝙰𝚃𝚂.**"
    )


# Clean

@app.on_message(filters.command("clean") & filters.user(SUDO_USERS))
async def clean(_, message):
    dir = "ShiviXMusic/Cache"
    ls_dir = os.listdir(dir)
    if ls_dir:
        for dta in os.listdir(dir):
            os.system("rm -rf *.png *.jpg")
        await message.reply_text("**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙻𝙴𝙰𝙽𝙴𝙳 𝙰𝙻𝙻 𝚃𝙴𝙼𝙿𝙾𝚁𝙰𝚁𝚈 𝙳𝙸𝚁𝙴𝙲𝚃𝙾𝚁𝙸𝙴𝚂 !**")
    else:
        await message.reply_text("**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙻𝙴𝙰𝙽𝙴𝙳 𝙰𝙻𝙻 𝚃𝙴𝙼𝙿𝙾𝚁𝙰𝚁𝚈 𝙳𝙸𝚁𝙴𝙲𝚃𝙾𝚁𝙸𝙴𝚂 !**")
