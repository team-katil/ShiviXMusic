from ShiviXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_panel = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="π°π³πΌπΈπ½π",
                    callback_data="help_callback ADMIN",
                ),
                InlineKeyboardButton(
                    text="π°πππ·",
                    callback_data="help_callback AUTH",
                ),
                InlineKeyboardButton(
                    text="πΏπ»π°π",
                    callback_data="help_callback PLAY",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="πΎππ½π΄π",
                    callback_data="help_callback OWNER",
                ),
                InlineKeyboardButton(
                    text="πππ³πΎ",
                    callback_data="help_callback SUDO",
                ),
                InlineKeyboardButton(
                    text="ππΎπΎπ»π",
                    callback_data="help_callback TOOLS",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="π±π°π²πΊ",
                    callback_data=f"ShiviX_home",
                ),
                InlineKeyboardButton(
                    text="π²π»πΎππ΄",
                    callback_data=f"close"
                ),
            ]
        ]
    )


help_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="π±π°π²πΊ",
                    callback_data=f"ShiviX_help",
                ),
                InlineKeyboarutton(
                    text="π²π»πΎππ΄",
                    callback_data=f"close"
                )
            ]
        ]
    )
