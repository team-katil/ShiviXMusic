from pyrogram import Client, filters
from pyrogram.types import Message

from ShiviXMusic import app
from ShiviXMusic.Cache.admins import AdminActual
from ShiviXMusic.Helpers.Changers import int_to_alpha
from ShiviXMusic.Helpers.Database import (_get_authusers, delete_authuser, get_authuser,
                            get_authuser_count, get_authuser_names,
                            save_authuser)


__MODULE__ = "π°πππ·"
__HELP__ = """

**π½πΎππ΄ :**
β’ π°πππ·πΎππΈππ΄π³ πππ΄π π²π°π½ ππΊπΈπΏ, πΏπ°πππ΄, ππ΄πππΌπ΄ π°π½π³ π΄π½π³ ππ·π΄ ππππ΄π°πΌ ππΈππ·πΎππ π°π³πΌπΈπ½ ππΈπΆπ·ππ.


/auth [πππ΄ππ½π°πΌπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πππ΄π'π πΌπ΄πππ°πΆπ΄] 
Β» π°π³π³ π° πππ΄π ππΎ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ πΎπ΅ ππ·π΄ πΆππΎππΏ.

/unauth [πππ΄ππ½π°πΌπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πππ΄π'π πΌπ΄πππ°πΆπ΄] 
Β» ππ΄πΌπΎππ΄π ππ·π΄ πππ΄π π΅ππΎπΌ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ.

/authusers 
Β» ππ·πΎππ ππ·π΄ π»πΈππ πΎπ΅ π°πππ·πΎππΈππ΄π³ πππ΄ππ πΎπ΅ ππ·π΄ πΆππΎππΏ.
"""


@app.on_message(filters.command("auth") & filters.group)
@AdminActual
async def auth(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**Β» ππ΄πΏπ»π ππΎ π° πππ΄ππ πΌπ΄πππ°πΆπ΄ πΎπ πΆπΈππ΄ πππ΄ππ½π°πΌπ΄/πΈπ³.**"
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
                "**Β» ππΎπ π²π°π½ πΎπ½π»π π°π³π³ 15 πππ΄ππ πΈπ½ π° πΆππΎππΏ π°πππ· π»πΈππ.**"
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
                f"**Β» πππ²π²π΄πππ΅ππ»π»π π°π³π³π΄π³ {user.first_name} ππΎ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ πΎπ΅ ππ·π΄ πΆππΎππΏ.**"
            )
            return
        else:
            await message.reply_text(f"**Β» {user.first_name} πΈπ π°π»ππ΄π°π³π πΈπ½ π°πππ·πΎππππ΄π³ πππ΄π π»πΈππ.**")
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
            "**Β» ππΎπ π²π°π½ πΎπ½π»π π°π³π³ 15 πππ΄ππ πΈπ½ π° πΆππΎππΏπ π°πππ· π»πΈππ.**"
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
            f"**Β» πππ²π²π΄πππ΅ππ»π»π π°π³π³π΄π³ {user_name} ππΎ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ πΎπ΅ ππ·π΄ πΆππΎππΏ.**"
        )
        return
    else:
        await message.reply_text(f"**Β» {user_name} πΈπ π°π»ππ΄π°π³π πΈπ½ π°πππ·πΎππΈππ΄π³ πππ΄π π»πΈππ.**")


@app.on_message(filters.command("unauth") & filters.group)
@AdminActual
async def unauth_fe(_, message: Message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**Β» ππ΄πΏπ»π ππΎ π° πππ΄ππ πΌπ΄πππ°πΆπ΄ πΎπ πΆπΈππ΄ πππ΄ππ½π°πΌπ/πΈπ³.**"
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
                f"**Β» ππ΄πΌπΎππ΄π³ {user.first_name} π΅ππΎπΌ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ πΎπ΅ ππ·π΄ πΆππΎππΏ.**"
            )
        else:
            return await message.reply_text("**Β» π½πΎπ πΈπ½ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ.**")
    user_id = message.reply_to_message.from_user.id
    token = await int_to_alpha(user_id)
    deleted = await delete_authuser(message.chat.id, token)
    if deleted:
        return await message.reply_text(
            f"**Β» ππ΄πΌπΎππ΄π³ {message.reply_to_message.from_user.first_name} π΅ππΎπΌ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ πΎπ΅ ππ·π΄ πΆππΎππΏ.**"
        )
    else:
        return await message.reply_text("**Β» π½πΎπ πΈπ½ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ.**")


@app.on_message(filters.command("authusers") & filters.group)
async def authusers(_, message: Message):
    _playlist = await get_authuser_names(message.chat.id)
    if not _playlist:
        return await message.reply_text(
            "**Β» π½πΎ π°πππ·πΎππΈππ΄π³ πππ΄ππ π΅πΎππ½π³ πΈπ½ ππ·πΈπ πΆππΎππΏπ.**"
        )
    else:
        j = 0
        m = await message.reply_text(
            "**Β» πΆπ΄πππΈπ½πΆ π°πππ·πΎππΈππ΄π³ πππ΄ππ π»πΈππ π΅ππΎπΌ πΌπΎπ½πΆπΎπ³π±...**"
        )
        msg = "**π₯ π°πππ·πΎππΈππ΄π³ πππ΄π π»πΈππ :**\n\n"
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
            msg += f"{j}β€ {user}[`{user_id}`]\n"
            msg += f"    β π°π³π³π΄π³ π±π : {admin_name}[`{admin_id}`]\n\n"
        await m.edit_text(msg)
