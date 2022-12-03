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
            "» 𝙸 𝙳𝙾𝙽'𝚃  𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝙱𝙰𝙽/𝚄𝙽𝙱𝙰𝙽 𝚄𝚂𝙴𝚁𝚂 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝙰𝚃..",
            show_alert=True,
        )
    else:
        try:
            await app.unban_chat_member(
                CallbackQuery.message.chat.id, user_id
            )
        except:
            return await CallbackQuery.answer(
                "» 𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝚃𝙷𝙴 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.",
                show_alert=True,
            )
        return await CallbackQuery.edit_message_text(
            "» 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝚄𝙽𝙱𝙰𝙽𝙽𝙴𝙳, 𝙽𝙾𝚆 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙿𝙻𝙰𝚈 𝚂𝙾𝙽𝙶 𝙰𝙶𝙰𝙸𝙽."
        )

def AssistantAdd(mystic):
    async def wrapper(_, message):
        try:
            b = await app.get_chat_member(message.chat.id, ASSID)
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="• 𝙲𝙻𝙸𝙲𝙺 𝙷𝙴𝚁𝙴 •",
                            callback_data=f"unban_assistant a|{ASSID}",
                        )
                    ],
                ]
            )
            if b.status == "kicked":
                return await message.reply_text(
                    f"» {BOT_NAME} 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝚂 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝙰𝚃.\n\n𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝙳 : `{ASSID}`\n𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{ASSUSERNAME}\n\n𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝚃𝙷𝙴 𝙱𝚄𝚃𝚃𝙾𝙽 𝙶𝙸𝚅𝙴𝙽 𝙱𝙴𝙻𝙾𝚆 𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝚃𝙷𝙴 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.",
                    reply_markup=key,
                )
            elif b.status == "banned":
                return await message.reply_text(
                    f"» {BOT_NAME} 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝚂 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝚂𝚃.\n\n𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝙳 : `{ASSID}`\n𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{ASSUSERNAME}\n\n𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝚃𝙷𝙴 𝙱𝚄𝚃𝚃𝙾𝙽 𝙶𝙸𝚅𝙴𝙽 𝙱𝙴𝙻𝙾𝚆 𝚃𝙾 𝚄𝙽𝙱𝙰𝙽 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.",
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
                        f"» {BOT_NAME} 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝙹𝙾𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝙰𝚃.\n\n**𝚁𝙴𝙰𝚂𝙾𝙽** : {e}"
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
                        f"» {BOT_NAME} 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙹𝙾𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝙰𝚃.\n\n• 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝙳 : `{ASSID}` \n• 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙽𝙰𝙼𝙴 : {ASSNAME}\n• 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : @{ASSUSERNAME}",
                    )
                except UserAlreadyParticipant:
                    pass
                except Exception as e:
                    await message.reply_text(
                        f"» {BOT_NAME} 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝙹𝙾𝙸𝙽 𝚃𝙷𝙸𝚂 𝙲𝙷𝙰𝚃.\n\n**𝚁𝙴𝙰𝚂𝙾𝙽>** : {e}"
                    )
                    return
        return await mystic(_, message)

    return wrapper
