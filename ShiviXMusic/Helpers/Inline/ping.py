import config
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


ping_ig = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝚂𝚄𝙿𝙿𝙾𝚁𝚃",
                    url=config.SUPPORT_CHAT,
                ),
                InlineKeyboardButton(
                    text="𝚄𝙿𝙳𝙰𝚃𝙴",
                    url=config.SUPPORT_CHANNEL
                )
            ]
        ]
    )
