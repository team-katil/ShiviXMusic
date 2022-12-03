import config
from ShiviXMusic import BOT_USERNAME, app
from ShiviXMusic.Helpers.Database import is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**» 𝚈𝙾𝚄'𝚁𝙴 𝙰𝙽 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽.\n\n• 𝚁𝙴𝚅𝙴𝚁𝚃 𝙱𝙰𝙲𝙺 𝚃𝙾 𝚄𝚂𝙴𝚁 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝙼𝙴.**"
            )
        if await is_on_off(1):
            if int(message.chat.id) != int(LOGGER_ID):
                return await message.reply_text(
                    f"» {BOT_NAME} 𝙸𝚂 𝚄𝙽𝙳𝙴𝚁 𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴.\n\n𝙸𝙵 𝚈𝙾𝚄 𝚆𝙰𝙽𝙽𝙰 𝙺𝙽𝙾𝙴 𝚃𝙷𝙴 𝚁𝙴𝙰𝚂𝙾𝙽 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙰𝚂𝙺 [ʜᴇʀᴇ]({config.SUPPORT_CHAT}) !",
                    disable_web_page_preview=True,
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**» 𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝙱𝙰𝙽𝙽𝙴𝙳 𝚄𝚂𝙴𝚁 «**\n\n𝙰𝙲𝙲𝙾𝚁𝙳𝙸𝙽𝙶 𝚃𝙾 𝙼𝚈 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝚈𝙾𝚄'𝚁𝙴 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙱𝚈 𝙼𝙷 𝙾𝚆𝙽𝙴𝚁, 𝚂𝙾 𝚈𝙾𝚄 𝙲𝙰𝙽'𝚃 𝚄𝚂𝙴 𝙼𝙴.\n\nᴠɪsɪᴛ : [sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ]({config.SUPPORT_CHAT})",
                 disable_web_page_preview=True,
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOGGER_ID):
                return await CallbackQuery.answer(
                    "» {BOT_NAME} 𝙸𝚂 𝚄𝙽𝙳𝙴𝚁 𝙼𝙰𝙸𝙽𝚃𝙴𝙽𝙰𝙽𝙲𝙴.",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "» 𝙱𝙻𝙾𝙾𝙳𝚈\n\n𝚈𝙾𝚄'𝚁𝙴 𝙶𝙻𝙾𝙱𝙰𝙻𝙻𝚈 𝙱𝙰𝙽𝙽𝙴𝙳 𝙵𝚁𝙾𝙼 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃.", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
