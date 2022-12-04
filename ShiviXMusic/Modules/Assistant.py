import config

from inspect import getfullargspec
from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputTextMessageContent,
                            Message)

from ShiviXMusic import (ASSID, ASSNAME, BOT_ID, BOT_USERNAME, BOT_NAME, SUDO_USERS, app, Ass)
from ShiviXMusic.Helpers.Database import (approve_pmpermit, disapprove_pmpermit,
                            is_pmpermit_approved)


__MODULE__ = "𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃"
__HELP__ = f"""

**𝙽𝙾𝚃𝙴 :**
𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚂𝚄𝙳𝙾𝙴𝚁𝚂

{config.ASS_HANDLER[0]}approve [𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁'𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴] 
» 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝚂 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁 𝚃𝙾 𝙿𝙼 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙰𝙲𝙲𝙾𝚄𝙽𝚃.

{config.ASS_HANDLER[0]}disapprove [𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁'𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴] 
» 𝙳𝙸𝚂𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝚂 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁 𝚃𝙾 𝙿𝙼 𝙾𝙽 𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 .

{config.ASS_HANDLER[0]}pfp [𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾] 
» 𝙲𝙷𝙰𝙽𝙶𝙴𝚂 𝚃𝙷𝙴 𝙿𝙵𝙿 𝙾𝙵 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙰𝙲𝙲𝙾𝚄𝙽𝚃.

{config.ASS_HANDLER[0]}bio [𝚃𝙴𝚇𝚃] 
» 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝚃𝙷𝙴 𝙱𝙸𝙾 𝙾𝙵 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙰𝙲𝙲𝙾𝚄𝙽𝚃.
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
        await message.reply_text("**» 𝚂𝙿𝙰𝙼 𝙳𝙴𝚃𝙴𝙲𝚃𝙴𝙳. 𝙱𝙻𝙾𝙲𝙺𝙸𝙽𝙶 𝚃𝙷𝙸𝚂 𝚄𝚂𝙴𝚁.**")
        await Ass.send_message(
            config.LOGGER_ID,
            f"**𝚂𝙿𝙰𝙼 𝙳𝙴𝚃𝙴𝙲𝚃𝙴𝙳**\n\n» **𝚂𝙿𝙰𝙼𝙼𝙴𝚁 :** {message.from_user.mention}\n» **𝚄𝚂𝙴𝚁 𝙸𝙳:** {message.from_user.id}",
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
            message, text="» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁'𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙰𝙿𝙿𝚁𝙾𝚅𝙴."
        )
    user_id = message.reply_to_message.from_user.id
    if await is_pmpermit_approved(user_id):
        return await eor(message, text="» 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳 𝚃𝙾 𝙿𝙼.")
    await approve_pmpermit(user_id)
    await eor(message, text="» 𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳 𝚃𝙾 𝙿𝙼.")


@Ass.on_message(
    filters.command("disapprove", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def pm_disapprove(_, message):
    if not message.reply_to_message:
        return await eor(
            message, text="» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁'𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙳𝙸𝚂𝙰𝙿𝙿𝚁𝙾𝚅𝙴."
        )
    user_id = message.reply_to_message.from_user.id
    if not await is_pmpermit_approved(user_id):
        await eor(message, text="» 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙳𝙸𝚂𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳 𝚃𝙾 𝙿𝙼.")
        async for m in Ass.iter_history(user_id, limit=5):
            if m.reply_markup:
                try:
                    await m.delete()
                except Exception:
                    pass
        return
    await disapprove_pmpermit(user_id)
    await eor(message, text="» 𝙳𝙸𝚂𝙰𝙿𝙿𝚁𝙾𝚅𝙴𝙳 𝚃𝙾 𝙿𝙼.")

    
@Ass.on_message(
    filters.command("pfp", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_pfp(_, message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await eor(message, text="» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙿𝙷𝙾𝚃𝙾 𝚃𝙾 𝚂𝙴𝚃 𝙸𝚃 𝙰𝚂 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙿𝙵𝙿.")
    photo = await message.reply_to_message.download()
    try: 
        await Ass.set_profile_photo(photo=photo)   
        await eor(message, text="**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝙿𝙵𝙿 𝙾𝙵 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.**")
    except Exception as e:
        await eor(message, text=e)
    
    
@Ass.on_message(
    filters.command("bio", prefixes=config.ASS_HANDLER)
    & filters.user(SUDO_USERS)
    & ~filters.via_bot
)
async def set_bio(_, message):
    if len(message.command) == 1:
        return await eor(message , text="» 𝙶𝙸𝚅𝙴 𝚂𝙾𝙼𝙴 𝚃𝙴𝚇𝚃 𝚃𝙾 𝚂𝙴𝚃 𝙸𝚃 𝙰𝚂 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙸𝙾.")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try: 
            await Ass.update_profile(bio=bio) 
            await eor(message , text="**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙷𝙰𝙽𝙶𝙴𝙳 𝙱𝙸𝙾 𝙾𝙵 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃.**")
        except Exception as e:
            await eor(message , text=e) 
    else:
        return await eor(message , text="» 𝙶𝙸𝚅𝙴 𝚂𝙾𝙼𝙴 𝚃𝙴𝚇𝚃𝙱𝚃𝙾 𝚂𝙴𝚃 𝙸𝚃 𝙰𝚂 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙱𝙸𝙾.")


async def eor(msg: Message, **kwargs):
    func = (
        (msg.edit_text if msg.from_user.is_self else msg.reply)
        if msg.from_user
        else msg.reply
    )
    spec = getfullargspec(func.__wrapped__).args
    return await func(**{k: v for k, v in kwargs.items() if k in spec})
