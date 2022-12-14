from typing import Dict, List, Union

from pyrogram import filters
from pyrogram.errors import UserAlreadyParticipant, UserNotParticipant
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from ShiviXMusic import (ASSID, ASSMENTION, ASSNAME, ASSUSERNAME, BOT_ID, BOT_NAME, app, Ass)



@app.on_callback_query(filters.regex("unban_assistant"))
async def unban_assistant_(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    a = await app.get_chat_member(CallbackQuery.message.chat.id, BOT_ID)
    if not a.can_restrict_members:
        return await CallbackQuery.answer(
            "Β» πΈ π³πΎπ½'π  π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½ ππΎ π±π°π½/ππ½π±π°π½ πππ΄ππ πΈπ½ ππ·πΈπ π²π·π°π..",
            show_alert=True,
        )
    else:
        try:
            await app.unban_chat_member(
                CallbackQuery.message.chat.id, user_id
            )
        except:
            return await CallbackQuery.answer(
                "Β» π΅π°πΈπ»π΄π³ ππΎ ππ½π±π°π½ ππ·π΄ π°πππΈπππ°π½π.",
                show_alert=True,
            )
        return await CallbackQuery.edit_message_text(
            "Β» π°πππΈπππ°π½π πππ²π²π΄πππ΅ππ»π»π ππ½π±π°π½π½π΄π³, π½πΎπ ππΎπ π²π°π½ πΏπ»π°π ππΎπ½πΆ π°πΆπ°πΈπ½."
        )

def AssistantAdd(mystic):
    async def wrapper(_, message):
        try:
            b = await app.get_chat_member(message.chat.id, ASSID)
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="β’ π²π»πΈπ²πΊ π·π΄ππ΄ β’",
                            callback_data=f"unban_assistant a|{ASSID}",
                        )
                    ],
                ]
            )
            if b.status == "kicked":
                return await message.reply_text(
                    f"Β» {BOT_NAME} π°πππΈπππ°π½π πΈπ π±π°π½π½π΄π³ πΈπ½ ππ·πΈπ π²π·π°π.\n\nπ°πππΈπππ°π½π πΈπ³ : `{ASSID}`\nπ°πππΈπππ°π½π πππ΄ππ½π°πΌπ΄ : @{ASSUSERNAME}\n\nπ²π»πΈπ²πΊ πΎπ½ ππ·π΄ π±ππππΎπ½ πΆπΈππ΄π½ π±π΄π»πΎπ ππΎ ππ½π±π°π½ ππ·π΄ π°πππΈπππ°π½π.",
                    reply_markup=key,
                )
            elif b.status == "banned":
                return await message.reply_text(
                    f"Β» {BOT_NAME} π°πππΈπππ°π½π πΈπ π±π°π½π½π΄π³ πΈπ½ ππ·πΈπ π²π·ππ.\n\nπ°πππΈπππ°π½π πΈπ³ : `{ASSID}`\nπ°πππΈπππ°π½π πππ΄ππ½π°πΌπ΄ : @{ASSUSERNAME}\n\nπ²π»πΈπ²πΊ πΎπ½ ππ·π΄ π±ππππΎπ½ πΆπΈππ΄π½ π±π΄π»πΎπ ππΎ ππ½π±π°π½ π°πππΈπππ°π½π.",
                    reply_markup=key,
                )
        except UserNotParticipant:
            if message.chat.username:
                try:
                    await Ass.join_chat(message.chat.username)
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"Β» {BOT_NAME} π°πππΈπππ°π½π π΅π°πΈπ»π΄π³ ππΎ πΉπΎπΈπ½ ππ·πΈπ π²π·π°π.\n\n**ππ΄π°ππΎπ½** : {e}"
                    )
                    return
            else:
                try:
                    invitelink = await app.export_chat_invite_link(
                        message.chat.id
                    )
                    if invitelink.startswith("https://t.me/+"):
                        invitelink = invitelink.replace(
                            "https://t.me/+", "https://t.me/joinchat/"
                        )
                    await Ass.join_chat(invitelink)
                    await message.reply(
                        f"Β» {BOT_NAME} π°πππΈπππ°π½π πππ²π²π΄πππ΅ππ»π»π πΉπΎπΈπ½ ππ·πΈπ π²π·π°π.\n\nβ’ π°πππΈπππ°π½π πΈπ³ : `{ASSID}` \nβ’ π°πππΈπππ°π½π π½π°πΌπ΄ : {ASSNAME}\nβ’ π°πππΈπππ°π½π πππ΄ππ½π°πΌπ΄ : @{ASSUSERNAME}",
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"Β» {BOT_NAME} π°πππΈπππ°π½π π΅π°πΈπ»π΄π³ ππΎ πΉπΎπΈπ½ ππ·πΈπ π²π·π°π.\n\n**ππ΄π°ππΎπ½>** : {e}"
                    )
                    return
        return await mystic(_, message)

    return wrapper
