import os
import asyncio

from pyrogram import filters
from pyrogram.types import Message

from ShiviXMusic import BOT_NAME, OWNER_ID, app
from ShiviXMusic.Helpers.Database import add_off, add_on


__MODULE__ = "𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴"
__HELP__ = """

**𝙽𝙾𝚃𝙴 :**
𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁𝚂.


/maintenance on
» ᴇɴᴀʙʟᴇ ᴛʜᴇ ᴍᴀɪɴᴛᴇɴᴀɴᴄᴇ ᴍᴏᴅᴇ ᴏғ ᴛʜᴇ ʙᴏᴛ.

/maintenance off
» 𝙳𝙸𝚂𝙰𝙱𝙻𝙴 𝚃𝙷𝙴 𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴 𝙼𝙾𝙳𝙴 𝙾𝙵 𝚃𝙷𝙴 𝙱𝙾𝚃.
"""


@app.on_message(filters.command("maintenance") & filters.user(OWNER_ID))
async def maintenance(_, message):
    exp = "**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/maintenance [on|off]"
    if len(message.command) != 2:
        return await message.reply_text(exp)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        user_id = 1
        await add_on(user_id)
        await message.reply_text(f"**» {BOT_NAME} 𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴 𝙼𝙾𝙳𝙴 𝙴𝙽𝙰𝙱𝙻𝙴𝙳.**")
    elif state == "off":
        user_id = 1
        await add_off(user_id)
        await message.reply_text(f"**» {BOT_NAME} 𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴 𝙼𝙾𝙳𝙴 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳.**")
    else:
        await message.reply_text(exp)
