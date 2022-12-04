from pyrogram import Client, filters
from pyrogram.types import Message

from ShiviXMusic import app
from ShiviXMusic.Cache.admins import AdminActual
from ShiviXMusic.Helpers.Changers import int_to_alpha
from ShiviXMusic.Helpers.Database import (_get_authusers, delete_authuser, get_authuser,
                            get_authuser_count, get_authuser_names,
                            save_authuser)


__MODULE__ = "𝙰𝚄𝚃𝙷"
__HELP__ = """

**𝙽𝙾𝚃𝙴 :**
• 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁 𝙲𝙰𝙽 𝚂𝙺𝙸𝙿, 𝙿𝙰𝚄𝚂𝙴, 𝚁𝙴𝚂𝚄𝙼𝙴 𝙰𝙽𝙳 𝙴𝙽𝙳 𝚃𝙷𝙴 𝚂𝚃𝚁𝙴𝙰𝙼 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙳𝙼𝙸𝙽 𝚁𝙸𝙶𝙷𝚃𝚂.


/auth [𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁'𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴] 
» 𝙰𝙳𝙳 𝙰 𝚄𝚂𝙴𝚁 𝚃𝙾 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚉𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.

/unauth [𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁'𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴] 
» 𝚁𝙴𝙼𝙾𝚅𝙴𝚂 𝚃𝙷𝙴 𝚄𝚂𝙴𝚁 𝙵𝚁𝙾𝙼 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚉𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃.

/authusers 
» 𝚂𝙷𝙾𝚆𝚂 𝚃𝙷𝙴 𝙻𝙸𝚂𝚃 𝙾𝙵 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙾𝙵 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.
"""


@app.on_message(filters.command("auth") & filters.group)
@AdminActual
async def auth(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝙶𝙸𝚅𝙴 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴/𝙸𝙳.**"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        user_id = message.from_user.id
        token = await int_to_alpha(user.id)
        from_user_name = message.from_user.first_name
        from_user_id = message.from_user.id
        _check = await get_authuser_names(message.chat.id)
        count = 0
        for smex in _check:
            count += 1
        if int(count) == 15:
            return await message.reply_text(
                "**» 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙾𝙽𝙻𝚈 𝙰𝙳𝙳 15 𝚄𝚂𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙶𝚁𝙾𝚄𝙿 𝙰𝚄𝚃𝙷 𝙻𝙸𝚂𝚃.**"
            )
        if token not in _check:
            assis = {
                "auth_user_id": user.id,
                "auth_name": user.first_name,
                "admin_id": from_user_id,
                "admin_name": from_user_name,
            }
            await save_authuser(message.chat.id, token, assis)
            await message.reply_text(
                f"**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙳𝙳𝙴𝙳 {user.first_name} 𝚃𝙾 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.**"
            )
            return
        else:
            await message.reply_text(f"**» {user.first_name} 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙸𝙽 𝙰𝚄𝚃𝙷𝙾𝚁𝚄𝚂𝙴𝙳 𝚄𝚂𝙴𝚁 𝙻𝙸𝚂𝚃.**")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    user_name = message.reply_to_message.from_user.first_name
    token = await int_to_alpha(user_id)
    from_user_name = message.from_user.first_name
    _check = await get_authuser_names(message.chat.id)
    count = 0
    for smex in _check:
        count += 1
    if int(count) == 15:
        return await message.reply_text(
            "**» 𝚈𝙾𝚄 𝙲𝙰𝙽 𝙾𝙽𝙻𝚈 𝙰𝙳𝙳 15 𝚄𝚂𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙶𝚁𝙾𝚄𝙿𝚂 𝙰𝚄𝚃𝙷 𝙻𝙸𝚂𝚃.**"
        )
    if token not in _check:
        assis = {
            "auth_user_id": user_id,
            "auth_name": user_name,
            "admin_id": from_user_id,
            "admin_name": from_user_name,
        }
        await save_authuser(message.chat.id, token, assis)
        await message.reply_text(
            f"**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙰𝙳𝙳𝙴𝙳 {user_name} 𝚃𝙾 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.**"
        )
        return
    else:
        await message.reply_text(f"**» {user_name} 𝙸𝚂 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙸𝙽 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁 𝙻𝙸𝚂𝚃.**")


@app.on_message(filters.command("unauth") & filters.group)
@AdminActual
async def unauth_fe(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**» 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝚄𝚂𝙴𝚁𝚂 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝙶𝙸𝚅𝙴 𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝚁/𝙸𝙳.**"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        token = await int_to_alpha(user.id)
        deleted = await delete_authuser(message.chat.id, token)
        if deleted:
            return await message.reply_text(
                f"**» 𝚁𝙴𝙼𝙾𝚅𝙴𝙳 {user.first_name} 𝙵𝚁𝙾𝙼 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.**"
            )
        else:
            return await message.reply_text("**» 𝙽𝙾𝚃 𝙸𝙽 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃.**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    if deleted:
        return await message.reply_text(
            f"**» 𝚁𝙴𝙼𝙾𝚅𝙴𝙳 {message.reply_to_message.from_user.first_name} 𝙵𝚁𝙾𝙼 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿.**"
        )
    else:
        return await message.reply_text("**» 𝙽𝙾𝚃 𝙸𝙽 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃.**")


@app.on_message(filters.command("authusers") & filters.group)
async def authusers(_, message: Message):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text(
            "**» 𝙽𝙾 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙵𝙾𝚄𝙽𝙳 𝙸𝙽 𝚃𝙷𝙸𝚂 𝙶𝚁𝙾𝚄𝙿𝚂.**"
        )
    else:
        j = 0
        m = await message.reply_text(
            "**» 𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁𝚂 𝙻𝙸𝚂𝚃 𝙵𝚁𝙾𝙼 𝙼𝙾𝙽𝙶𝙾𝙳𝙱...**"
        )
        msg = "**🥀 𝙰𝚄𝚃𝙷𝙾𝚁𝙸𝚂𝙴𝙳 𝚄𝚂𝙴𝚁 𝙻𝙸𝚂𝚃 :**\n\n"
        for note in _playlist:
            _note = await get_authuser(message.chat.id, note)
            user_id = _note["auth_user_id"]
            user_name = _note["auth_name"]
            admin_id = _note["admin_id"]
            admin_name = _note["admin_name"]
            try:
                user = await app.get_users(user_id)
                user = user.first_name
                j += 1
            except Exception:
                continue
            msg += f"{j}➤ {user}[`{user_id}`]\n"
            msg += f"    ┗ 𝙰𝙳𝙳𝙴𝙳 𝙱𝚈 : {admin_name}[`{admin_id}`]\n\n"
        await m.edit_text(msg)
