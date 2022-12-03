from typing import Dict, List, Union

from ShiviXMusic import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "» 𝙿𝙻𝙴𝙰𝚂𝙴 𝙶𝙸𝚅𝙴 𝙼𝙴 𝙱𝙴𝙻𝙾𝚆 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 :\n\n"
                + "\n• **𝙳𝙴𝙻𝙴𝚃𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂**"
                + "\n• **𝙼𝙰𝙽𝙰𝙶𝙴 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂**"
                + "\n• **𝙸𝙽𝚅𝙸𝚃𝙴 𝚄𝚂𝙴𝚁𝚂 𝚅𝙸𝙰 𝙻𝙸𝙽𝙺.**"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "» 𝙸 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 𝚃𝙾 :"
                + "\n\n**𝙼𝙰𝙽𝙰𝙶𝙴 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂.**"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "» 𝙸 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 𝚃𝙾 :"
                + "\n\n**𝙳𝙴𝙻𝙴𝚃𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂.**"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "» 𝙸 𝙳𝙾𝙽'𝚃 𝙷𝙰𝚅𝙴 𝙿𝙴𝚁𝙼𝙸𝚂𝚂𝙸𝙾𝙽𝚂 𝚃𝙾 :"
                + "\n\n**𝙸𝙽𝚅𝙸𝚃𝙴 𝚄𝚂𝙴𝚁𝚂 𝚅𝙸𝙰 𝙻𝙸𝙽𝙺.**"
            )
            return
        return await mystic(_, message)

    return wrapper
