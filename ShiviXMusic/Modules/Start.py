import time
import config
import asyncio
from typing import Dict, List, Union

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, Message)

from ShiviXMusic import ASSID, BOT_NAME, BOT_USERNAME, OWNER_ID, SUDO_USERS, F_OWNER, app
from ShiviXMusic.Helpers.Database import (add_served_chat, add_served_user, is_served_chat, remove_active_chat)
from ShiviXMusic.Cache.permission import PermissionCheck
from ShiviXMusic.Helpers.Inline import start_pannel


welcome_group = 2

__MODULE__ = "πππ°ππ"
__HELP__ = """

/start 
Β» πππ°πππ ππ·π΄ π±πΎπ.

/help 
Β» ππ·πΎππ ππΎπ ππ·π΄ π·π΄π»πΏ πΌπ΄π½π πΎπ΅ ππ·π΄ π±πΎπ.
"""


@app.on_message(filters.new_chat_members, group=welcome_group)
async def welcome(_, message: Message):
    chat_id = message.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    for member in message.new_chat_members:
        try:
            if member.id == ASSID:
                return await remove_active_chat(chat_id)
            if member.id in OWNER_ID:
                return await message.reply_text(
                    f"**Β» ππ·π΄ πΎππ½π΄π πΎπ΅ {BOT_NAME} πΉπππ πΉπΎπΈπ½π΄π³ ππΎππ π²π·π°π.**\n\nβ» πΎππ½π΄π : [{member.mention}] π₯"
                )
            if member.id in SUDO_USERS:
                return await message.reply_text(
                    f"**Β» π° πππ³πΎ πππ΄π πΎπ΅ {BOT_NAME} πΉπππ πΉπΎπΈπ½π΄π³ ππΎππ π²π·π°π.**\n\nβ» πππ³πΎπ΄π : [{member.mention}] π₯"
                )
                return
        except:
            return


@app.on_message(filters.command(["help", "start", f"start@{BOT_USERNAME}"]) & filters.group)
@PermissionCheck
async def gstart(_, message: Message):
    await asyncio.gather(
        message.delete(),
        message.reply_text(
            f"Β» Κα΄Κ,\nππ·πΈπ πΈπ {BOT_NAME}\n π° πΌπππΈπ² πΏπ»π°ππ΄π π±πΎπ π΅πΎπ ππ΄π»π΄πΆππ°πΌ ππΈπ³π΄πΎπ²π·π°ππ.\n\nππ·π°π½πΊπ π΅πΎπ π°π³π³πΈπ½πΆ πΌπ΄ πΈπ½ {message.chat.title}.\n\nπΈπ΅ ππΎπ π·π°ππ΄ π°π½π πππ΄πππΈπΎπ½π π°π±πΎππ πΌπ΄ ππΎπ π²π°π½ π°ππΊ πΈπ πΉπ½ πππΏπΏπΎππ π²π·π°π.",
            reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="π°π³π³ πΌπ΄ π΄π»ππ΄ ππΎπ πΆπ΄π", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π₯ πΎππ½π΄π π₯", user_id=F_OWNER
                ),
                InlineKeyboardButton(
                    text="β π·π΄π»πΏ β", callback_data="ShiviX_help"
                )
            ],
            [
                InlineKeyboardButton(
                    text="β¨ πππΏπΏπΎππ β¨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="π ππΏπ³π°ππ΄ π", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β π²πΎπ³π΄ β", url="https://github.com/team-katil/ShiviXMusic"
                ),
            ],
        ]
     ),
  )
)

