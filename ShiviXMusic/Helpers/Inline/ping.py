import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="πππΏπΏπΎππ",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="ππΏπ³π°ππ΄",
                    url=config.SUPPORT_CHANNEL
                )
            ]
        ]
    )
