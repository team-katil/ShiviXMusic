import config

from inspect import getfullargspec
from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputTextMessageContent,
                            Message)

from ShiviXMusic import (ASSID, ASSNAME, BOT_ID, BOT_USERNAME, BOT_NAME, SUDO_USERS, app, Ass)
from ShiviXMusic.Helpers.Database import (approve_pmpermit, disapprove_pmpermit,
                            is_pmpermit_approved)


__MODULE__ = "π°πππΈπππ°π½π"
__HELP__ = f"""

**π½πΎππ΄ :**
πΎπ½π»π π΅πΎπ πππ³πΎπ΄ππ

{config.ASS_HANDLER[0]}approve [ππ΄πΏπ»π ππΎ π° πππ΄π'π πΌπ΄πππ°πΆπ΄] 
Β» π°πΏπΏππΎππ΄π ππ·π΄ πππ΄π ππΎ πΏπΌ πΎπ½ ππΎππ π°πππΈπππ°π½π π°π²π²πΎππ½π.

{config.ASS_HANDLER[0]}disapprove [ππ΄πΏπ»π ππΎ π° πππ΄π'π πΌπ΄πππ°πΆπ΄] 
Β» π³πΈππ°πΏπΏππΎππ΄π ππ·π΄ πππ΄π ππΎ πΏπΌ πΎπ½ ππΎππ π°πππΈπππ°π½π .

{config.ASS_HANDLER[0]}pfp [ππ΄πΏπ»π ππΎ π° πΏπ·πΎππΎ] 
Β» π²π·π°π½πΆπ΄π ππ·π΄ πΏπ΅πΏ πΎπ΅ π°πππΈπππ°π½π π°π²π²πΎππ½π.

{config.ASS_HANDLER[0]}bio [ππ΄ππ] 
Β» π²π·π°π½πΆπ΄π³ ππ·π΄ π±πΈπΎ πΎπ΅ π°πππΈπππ°π½π π°π²π²πΎππ½π.
"""

flood = {}


@Ass.on_message(
    filters.private
    & filters.incoming
    & ~filters.service
    & ~filters.edited
    & ~filters.me
    & ~filters.bot
    & ~filters.via_bot
    & ~filters.user(SUDO_USERS)
)
async def awaiting_message(_, message):
    user_id = message.from_user.id
    if await is_pmpermit_approved(user_id):
        return
    async for m in Ass.iter_history(user_id, limit=5):
        if m.reply_markup:
            await m.delete()
    if str(user_id) in flood:
        flood[str(user_id)] += 1
    else:
        flood[str(user_id)] = 1
    if flood[str(user_id)] > 9:
        await message.reply_text("**Β» ππΏπ°πΌ π³π΄ππ΄π²ππ΄π³. π±π»πΎπ²πΊπΈπ½πΆ ππ·πΈπ πππ΄π.**")
        await Ass.send_message(
            config.LOGGER_ID,
            f"**ππΏπ°πΌ π³π΄ππ΄π²ππ΄π³**\n\nΒ» **ππΏπ°πΌπΌπ΄π :** {message.from_user.mention}\nΒ» **πππ΄π πΈπ³:** {message.from_user.id}",
        )
        return await Ass.block_user(user_id)


@Ass.on_message(
    filters.command("approve", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def pm_approve(_, message):
    if not message.reply_to_message:
        return await eor(
            message, text="Β» ππ΄πΏπ»π ππΎ π° πππ΄π'π πΌπ΄πππ°πΆπ΄ ππΎ π°πΏπΏππΎππ΄."
        )
    user_id = message.reply_to_message.from_user.id
    if await is_pmpermit_approved(user_id):
        return await eor(message, text="Β» π°π»ππ΄π°π³π π°πΏπΏππΎππ΄π³ ππΎ πΏπΌ.")
    await approve_pmpermit(user_id)
    await eor(message, text="Β» π°πΏπΏππΎππ΄π³ ππΎ πΏπΌ.")


@Ass.on_message(
    filters.command("disapprove", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def pm_disapprove(_, message):
    if not message.reply_to_message:
        return await eor(
            message, text="Β» ππ΄πΏπ»π ππΎ π° πππ΄π'π πΌπ΄πππ°πΆπ΄ ππΎ π³πΈππ°πΏπΏππΎππ΄."
        )
    user_id = message.reply_to_message.from_user.id
    if not await is_pmpermit_approved(user_id):
        await eor(message, text="Β» π°π»ππ΄π°π³π π³πΈππ°πΏπΏππΎππ΄π³ ππΎ πΏπΌ.")
        async for m in Ass.iter_history(user_id, limit=5):
            if m.reply_markup:
                try:
                    await m.delete()
                except Exception:
                    pass
        return
    await disapprove_pmpermit(user_id)
    await eor(message, text="Β» π³πΈππ°πΏπΏππΎππ΄π³ ππΎ πΏπΌ.")

    
@Ass.on_message(
    filters.command("pfp", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_pfp(_, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="Β» ππ΄πΏπ»π ππΎ π° πΏπ·πΎππΎ ππΎ ππ΄π πΈπ π°π π°πππΈπππ°π½π πΏπ΅πΏ.")
    photo = await message.reply_to_message.download()
    try: 
        await Ass.set_profile_photo(photo=photo)   
        await eor(message, text="**Β» πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ πΏπ΅πΏ πΎπ΅ π°πππΈπππ°π½π.**")
    except Exception as e:
        await eor(message, text=e)
    
    
@Ass.on_message(
    filters.command("bio", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_bio(_, message):
    if len(message.command) == 1:
        return await eor(message , text="Β» πΆπΈππ΄ ππΎπΌπ΄ ππ΄ππ ππΎ ππ΄π πΈπ π°π π°πππΈπππ°π½π π±πΈπΎ.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try: 
            await Ass.update_profile(bio=bio) 
            await eor(message , text="**Β» πππ²π²π΄πππ΅ππ»π»π π²π·π°π½πΆπ΄π³ π±πΈπΎ πΎπ΅ π°πππΈπππ°π½π.**")
        except Exception as e:
            await eor(message , text=e) 
    else:
        return await eor(message , text="Β» πΆπΈππ΄ ππΎπΌπ΄ ππ΄πππ±ππΎ ππ΄π πΈπ π°π π°πππΈπππ°π½π π±πΈπΎ.")


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
