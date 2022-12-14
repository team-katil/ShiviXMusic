from typing import Dict, List, Union

from ShiviXMusic import BOT_ID, app


def PermissionCheck(mystic):
    async def wrapper(_, message):
        a = await app.get_chat_member(message.chat.id, BOT_ID)
        if a.status != "administrator":
            return await message.reply_text(
                "Β» πΏπ»π΄π°ππ΄ πΆπΈππ΄ πΌπ΄ π±π΄π»πΎπ πΏπ΄ππΌπΈπππΈπΎπ½π :\n\n"
                + "\nβ’ **π³π΄π»π΄ππ΄ πΌπ΄πππ°πΆπ΄π**"
                + "\nβ’ **πΌπ°π½π°πΆπ΄ ππΈπ³π΄πΎ π²π·π°ππ**"
                + "\nβ’ **πΈπ½ππΈππ΄ πππ΄ππ ππΈπ° π»πΈπ½πΊ.**"
            )
        if not a.can_manage_voice_chats:
            await message.reply_text(
                "Β» πΈ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½π ππΎ :"
                + "\n\n**πΌπ°π½π°πΆπ΄ ππΈπ³π΄πΎ π²π·π°ππ.**"
            )
            return
        if not a.can_delete_messages:
            await message.reply_text(
                "Β» πΈ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½π ππΎ :"
                + "\n\n**π³π΄π»π΄ππ΄ πΌπ΄πππ°πΆπ΄π.**"
            )
            return
        if not a.can_invite_users:
            await message.reply_text(
                "Β» πΈ π³πΎπ½'π π·π°ππ΄ πΏπ΄ππΌπΈπππΈπΎπ½π ππΎ :"
                + "\n\n**πΈπ½ππΈππ΄ πππ΄ππ ππΈπ° π»πΈπ½πΊ.**"
            )
            return
        return await mystic(_, message)

    return wrapper
