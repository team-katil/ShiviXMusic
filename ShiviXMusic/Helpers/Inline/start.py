import config

from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)
from ShiviXMusic import BOT_USERNAME, F_OWNER


def start_pannel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄ 𝙷𝙴𝙻𝙿 ❄", callback_data="ShiviX_help"
                ),
                InlineKeyboardButton(
                    text="🥀 𝙾𝚆𝙽𝙴𝚁 🥀", user_id=F_OWNER
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
                )
            ],
        ]
        return buttons


def private_panel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="𝙰𝙳𝙳 𝙼𝙴 𝙴𝙻𝚂𝙴 𝚈𝙾𝚄 𝙶𝙴𝚈", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="🥀 𝙾𝚆𝙽𝙴𝙴 🥀", user_id=F_OWNER
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
        return buttons

