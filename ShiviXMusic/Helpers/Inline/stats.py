import config
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


stats_f = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="πΆπ΄π½π΄ππ°π»", callback_data=f"bot_stats"
            )
        ],
        [
            InlineKeyboardButton(
                text="πππππ΄πΌ", callback_data=f"sys_stats"
            ),
            InlineKeyboardButton(
                text="πΌπΎπ½πΆπΎπ³π±", callback_data=f"mongo_stats"
            )
        ],
        [
            InlineKeyboardButton(
                text="β¨ πππΏπΏπΎππ β¨", url=config.SUPPORT_CHAT
            ),
                        InlineKeyboardButton(
                text="β» π²π»πΎππ΄ βΊ", callback_data=f"close"
            )
        ],
    ]
)



stats_b = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(
                text="π±π°π²πΊ", callback_data=f"get_back"
            ),
            InlineKeyboardButton(
                text="β¨ πππΏπΏπΎππ β¨", url=config.SUPPORT_CHAT
            )
        ],
    ]
)

