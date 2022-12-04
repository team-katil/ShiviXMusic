from ShiviXMusic import app
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


help_panel = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙰𝙳𝙼𝙸𝙽𝚂",
                    callback_data="help_callback ADMIN",
                ),
                InlineKeyboardButton(
                    text="𝙰𝚄𝚃𝙷",
                    callback_data="help_callback AUTH",
                ),
                InlineKeyboardButton(
                    text="𝙿𝙻𝙰𝚈",
                    callback_data="help_callback PLAY",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝙾𝚆𝙽𝙴𝚁",
                    callback_data="help_callback OWNER",
                ),
                InlineKeyboardButton(
                    text="𝚂𝚄𝙳𝙾",
                    callback_data="help_callback SUDO",
                ),
                InlineKeyboardButton(
                    text="𝚃𝙾𝙾𝙻𝚂",
                    callback_data="help_callback TOOLS",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="𝙱𝙰𝙲𝙺",
                    callback_data=f"ShiviX_home",
                ),
                InlineKeyboardButton(
                    text="𝙲𝙻𝙾𝚂𝙴",
                    callback_data=f"close"
                ),
            ]
        ]
    )


help_markup = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙱𝙰𝙲𝙺",
                    callback_data=f"ShiviX_help",
                ),
                InlineKeyboarutton(
                    text="𝙲𝙻𝙾𝚂𝙴",
                    callback_data=f"close"
                )
            ]
        ]
    )
