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

__MODULE__ = "𝚂𝚃𝙰𝚁𝚃"
__HELP__ = """

/start 
» 𝚂𝚃𝙰𝚁𝚃𝚂 𝚃𝙷𝙴 𝙱𝙾𝚃.

/help 
» 𝚂𝙷𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙷𝙴 𝙷𝙴𝙻𝙿 𝙼𝙴𝙽𝚄 𝙾𝙵 𝚃𝙷𝙴 𝙱𝙾𝚃.
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
                    f"**» 𝚃𝙷𝙴 𝙾𝚆𝙽𝙴𝚁 𝙾𝙵 {BOT_NAME} 𝙹𝚄𝚂𝚃 𝙹𝙾𝙸𝙽𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃.**\n\n➻ 𝙾𝚆𝙽𝙴𝚁 : [{member.mention}] 🥀"
                )
            if member.id in SUDO_USERS:
                return await message.reply_text(
                    f"**» 𝙰 𝚂𝚄𝙳𝙾 𝚄𝚂𝙴𝚁 𝙾𝙵 {BOT_NAME} 𝙹𝚄𝚂𝚃 𝙹𝙾𝙸𝙽𝙴𝙳 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃.**\n\n➻ 𝚂𝚄𝙳𝙾𝙴𝚁 : [{member.mention}] 🥀"
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
            f"» ʜᴇʏ,\n𝚃𝙷𝙸𝚂 𝙸𝚂 {BOT_NAME}\n 𝙰 𝙼𝚄𝚂𝙸𝙲 𝙿𝙻𝙰𝚈𝙴𝚁 𝙱𝙾𝚃 𝙵𝙾𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚅𝙸𝙳𝙴𝙾𝙲𝙷𝙰𝚃𝚂.\n\n𝚃𝙷𝙰𝙽𝙺𝚂 𝙵𝙾𝚁 𝙰𝙳𝙳𝙸𝙽𝙶 𝙼𝙴 𝙸𝙽 {message.chat.title}.\n\n𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝚀𝚄𝙴𝚂𝚃𝙸𝙾𝙽𝚂 𝙰𝙱𝙾𝚄𝚃 𝙼𝙴 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙰𝚂𝙺 𝙸𝚃 𝙹𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙲𝙷𝙰𝚃.",
            reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙰𝙳𝙳 𝙼𝙴 𝙴𝙻𝚂𝙴 𝚈𝙾𝚄 𝙶𝙴𝚈", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥀 𝙾𝚆𝙽𝙴𝚁 🥀", user_id=F_OWNER
                ),
                InlineKeyboardButton(
                    text="❄ 𝙷𝙴𝙻𝙿 ❄", callback_data="ShiviX_help"
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💘 𝚄𝙿𝙳𝙰𝚃𝙴 💘", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☁ 𝙲𝙾𝙳𝙴 ☁", url="https://github.com/team-katil/ShiviXMusic"
                ),
            ],
        ]
     ),
  )
)

