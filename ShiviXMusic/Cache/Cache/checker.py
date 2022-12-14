import config
from ShiviXMusic import BOT_USERNAME, app
from ShiviXMusic.Helpers.Database import is_gbanned_user, is_on_off


def checker(mystic):
    async def wrapper(_, message):
        if message.sender_chat:
            return await message.reply_text(
                "**Β» ππΎπ'ππ΄ π°π½ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½.\n\nβ’ ππ΄ππ΄ππ π±π°π²πΊ ππΎ πππ΄π π°π²π²πΎππ½π π΅πΎπ πππΈπ½πΆ πΌπ΄.**"
            )
        if await is_on_off(1):
            if int(message.chat.id) != int(LOGGER_ID):
                return await message.reply_text(
                    f"Β» {BOT_NAME} πΈπ ππ½π³π΄π πΌπ°πΈπ½ππ΄π½π°π½π²π΄.\n\nπΈπ΅ ππΎπ ππ°π½π½π° πΊπ½πΎπ΄ ππ·π΄ ππ΄π°ππΎπ½ ππΎπ π²π°π½ π°ππΊ [Κα΄Κα΄]({config.SUPPORT_CHAT}) !",
                    disable_web_page_preview=True,
                )
        if await is_gbanned_user(message.from_user.id):
            return await message.reply_text(
                f"**Β» πΆπ»πΎπ±π°π»π»π π±π°π½π½π΄π³ πππ΄π Β«**\n\nπ°π²π²πΎππ³πΈπ½πΆ ππΎ πΌπ π³π°ππ°π±π°ππ΄ ππΎπ'ππ΄ πΆπ±π°π½π½π΄π³ π±π πΌπ· πΎππ½π΄π, ππΎ ππΎπ π²π°π½'π πππ΄ πΌπ΄.\n\nα΄ ΙͺsΙͺα΄ : [sα΄α΄©α΄©α΄Κα΄ α΄Κα΄α΄]({config.SUPPORT_CHAT})",
                 disable_web_page_preview=True,
            )
        return await mystic(_, message)

    return wrapper


def checkerCB(mystic):
    async def wrapper(_, CallbackQuery):
        if await is_on_off(1):
            if int(CallbackQuery.message.chat.id) != int(LOGGER_ID):
                return await CallbackQuery.answer(
                    "Β» {BOT_NAME} πΈπ ππ½π³π΄π πΌπ°πΈπ½ππ΄π½π°π½π²π΄.",
                    show_alert=True,
                )
        if await is_gbanned_user(CallbackQuery.from_user.id):
            return await CallbackQuery.answer(
                "Β» π±π»πΎπΎπ³π\n\nππΎπ'ππ΄ πΆπ»πΎπ±π°π»π»π π±π°π½π½π΄π³ π΅ππΎπΌ ππ·πΈπ π±πΎπ.", show_alert=True
            )
        return await mystic(_, CallbackQuery)

    return wrapper
