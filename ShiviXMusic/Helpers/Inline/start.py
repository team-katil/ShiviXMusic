import config

from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)
from ShiviXMusic import BOT_USERNAME, F_OWNER


def start_pannel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β π·π΄π»πΏ β", callback_data="ShiviX_help"
                ),
                InlineKeyboardButton(
                    text="π₯ πΎππ½π΄π π₯", user_id=F_OWNER
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
                )
            ],
        ]
        return buttons


def private_panel():
        buttons = [
            [
                InlineKeyboardButton(
                    text="π°π³π³ πΌπ΄ π΄π»ππ΄ ππΎπ πΆπ΄π", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π₯ πΎππ½π΄π΄ π₯", user_id=F_OWNER
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
        return buttons

