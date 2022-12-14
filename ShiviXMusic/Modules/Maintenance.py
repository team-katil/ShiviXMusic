import os
import asyncio

from pyrogram import filters
from pyrogram.types import Message

from ShiviXMusic import BOT_NAME, OWNER_ID, app
from ShiviXMusic.Helpers.Database import add_off, add_on


__MODULE__ = "๐ผ๐ฐ๐ธ๐ฝ๐๐ด๐ฝ๐ฐ๐ฝ๐ฒ๐ด"
__HELP__ = """

**๐ฝ๐พ๐๐ด :**
๐พ๐ฝ๐ป๐ ๐ต๐พ๐ ๐๐๐ณ๐พ ๐๐๐ด๐๐.


/maintenance on
ยป แดษดแดสสแด แดสแด แดแดษชษดแดแดษดแดษดแดแด แดแดแดแด แดา แดสแด สแดแด.

/maintenance off
ยป ๐ณ๐ธ๐๐ฐ๐ฑ๐ป๐ด ๐๐ท๐ด ๐ผ๐ฐ๐ธ๐ฝ๐๐ด๐ฝ๐ฐ๐ฝ๐ฒ๐ด ๐ผ๐พ๐ณ๐ด ๐พ๐ต ๐๐ท๐ด ๐ฑ๐พ๐.
"""


@app.on_message(filters.command("maintenance") & filters.user(OWNER_ID))
async def maintenance(_, message):
    exp = "**๐ด๐๐ฐ๐ผ๐ฟ๐ป๐ด :**\n/maintenance [on|off]"
    if len(message.command) != 2:
        return await message.reply_text(exp)
    chat_id = message.chat.id
    state = message.text.split(None, 1)[1].strip()
    state = state.lower()
    if state == "on":
        user_id = 1
        await add_on(user_id)
        await message.reply_text(f"**ยป {BOT_NAME} ๐ผ๐ฐ๐ธ๐ฝ๐๐ด๐ฝ๐ฐ๐ฝ๐ฒ๐ด ๐ผ๐พ๐ณ๐ด ๐ด๐ฝ๐ฐ๐ฑ๐ป๐ด๐ณ.**")
    elif state == "off":
        user_id = 1
        await add_off(user_id)
        await message.reply_text(f"**ยป {BOT_NAME} ๐ผ๐ฐ๐ธ๐ฝ๐๐ด๐ฝ๐ฐ๐ฝ๐ฒ๐ด ๐ผ๐พ๐ณ๐ด ๐ณ๐ธ๐๐ฐ๐ฑ๐ป๐ด๐ณ.**")
    else:
        await message.reply_text(exp)
