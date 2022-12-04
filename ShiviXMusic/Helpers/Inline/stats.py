import config
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


stats_f = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝙶𝙴𝙽𝙴𝚁𝙰𝙻", callback_data=f"bot_stats"
            )
        ],
        [
            InlineKeyboardButton(
                text="𝚂𝚈𝚂𝚃𝙴𝙼", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="𝙼𝙾𝙽𝙶𝙾𝙳𝙱", callback_data=f"mongo_stats"
            )
        ],
        [
            InlineKeyboardButton(
                text="✨ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=config.SUPPORT_CHAT
            ),
                        InlineKeyboardButton(
                text="↻ 𝙲𝙻𝙾𝚂𝙴 ↺", callback_data=f"close"
            )
        ],
    ]
)



stats_b = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="𝙱𝙰𝙲𝙺", callback_data=f"get_back"
            ),
            InlineKeyboardButton(
                text="✨ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=config.SUPPORT_CHAT
            )
        ],
    ]
)

