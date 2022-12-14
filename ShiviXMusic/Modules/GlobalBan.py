import os
import config
import asyncio

from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from ShiviXMusic import BOT_ID, BOT_NAME, SUDO_USERS, app
from ShiviXMusic.Helpers.Database import (add_gban_user, get_served_chats, is_gbanned_user, remove_gban_user)


__MODULE__ = "πΆ-π±π°π½"
__HELP__ = """

**π½πΎππ΄ :**
πΎπ½π»π π΅πΎπ πππ³πΎπ΄ππ.

/gban [πππ΄ππ½π°πΌπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πππ΄π]
Β» πΆπ»πΎπ±π°π»π»π π±π°π½ π° πππ΄π πΈπ½ π°π»π» ππ·π΄ ππ΄πππ΄π π²π·π°ππ.

/ungban [πππ΄ππ½π°πΌπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πππ΄π]
Β» πΆπ»πΎπ±π°π»π»π ππ½π±π°π½π ππ·π πΆ-π±π°π½π½π΄π³ πππ΄π.
"""


@app.on_message(filters.command("gban") & filters.user(SUDO_USERS))
async def ban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) < 2:
            await message.reply_text("**π΄ππ°πΌπΏπ»π΄ :**\n/gban [πππ΄ππ½π°πΌπ΄/πΈπ³]")
            return
        user = message.text.split(None, 2)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            return await message.reply_text(
                "**Β» ππΎπ π²π°π½'π πΆπ±π°π½ ππΎππππ΄π»π΅ !**"
            )
        elif user.id == BOT_ID:
            await message.reply_text("Β» ππΎπ ππ°π½π πΌπ΄ ππΎ πΆπ±π°π½ πΌπππ΄π»π΅, π½πΎπΎπ±π !")
        elif user.id in SUDO_USERS:
            await message.reply_text("Β» ππΎπ π±π»πΎπΎπ³π, ππΎπ ππ°π½π πΌπ΄ ππΎ πΆπ±π°π½ πΌπ π±π°π±π, πΈ ππΈπ»π» π΅π*πΊ ππΎπ π·π°ππ³ π°π½π³ ππΎπ ππΈπ»π» π½πΎπ π±π΄ π°π±π»π΄ ππΎ π΅π*πΊ π°π½ππΎπ½π΄ π°πΆπ°πΈπ½ !")
        else:
            await add_gban_user(user.id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**πΆπ»πΎπ±π°π»π»π π±π°π½π½πΈπ½πΆ {user.mention}**\n\nπ΄ππΏπ΄π²ππ΄π³ ππΈπΌπ΄ : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.kick_chat_member(sex, user.id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
**πΆ-π±π°π½ πΎπ½ {BOT_NAME}**

**β’ π²π·π°π :** {message.chat.title} [`{message.chat.id}`]
**β’ πππ³πΎπ΄π :** {from_user.mention}
**β’ πππ΄π :** {user.mention}
**β’ πππ΄π πΈπ³:** `{user.id}`
**β’ π±π°π½π½π΄π³ πΈπ½ :** {number_of_chats} π²π·π°ππ"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
        return
    from_user_id = message.from_user.id
    from_user_mention = message.from_user.mention
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id == from_user_id:
        await message.reply_text("Β» ππΎπ π²π°π½'π πΆπ±π°π½ ππΎππππ΄π»π΅ !")
    elif user_id == BOT_ID:
        await message.reply_text("Β» ππΎπ ππ°π½π πΌπ΄ ππΎ πΆπ±π°π½ πΌπππ΄π»π΅, π½πΎπΎπ±π !")
    elif user_id in SUDO_USERS:
        await message.reply_text("Β» ππΎπ π±π»πΎπΎπ³π, ππΎπ ππ°π½π πΌπ΄ ππΎ πΆπ±π°π½ πΌπ π±π°π±π, πΈ ππΈπ»π» π΅π*πΊ ππΎπ π·π°ππ³ π°π½π³ ππΎπ ππΈπ»π» π½πΎπ π±π΄ π°π±π»π΄ ππΎ π΅π*πΊ π°π½ππΎπ½π΄ π°πΆπ°πΈπ½ !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if is_gbanned:
            await message.reply_text("**π°π»ππ΄π°π³π πΆπ±π°π½π½π΄π³ ππ·π°π π²π·ππΌππΈππ°.**")
        else:
            await add_gban_user(user_id)
            served_chats = []
            chats = await get_served_chats()
            for chat in chats:
                served_chats.append(int(chat["chat_id"]))
            m = await message.reply_text(
                f"**πΆπ»πΎπ±π°π»π»π π±π°π½π½πΈπ½πΆ {mention}**\n\nπ΄ππΏπ΄π²ππ΄π³ ππΈπΌπ΄ : {len(served_chats)}"
            )
            number_of_chats = 0
            for sex in served_chats:
                try:
                    await app.kick_chat_member(sex, user_id)
                    number_of_chats += 1
                    await asyncio.sleep(1)
                except FloodWait as e:
                    await asyncio.sleep(int(e.x))
                except Exception:
                    pass
            ban_text = f"""
**πΆ-π±π°π½ πΎπ½ {BOT_NAME}**

**β’ π²π·π°π :** {message.chat.title} [`{message.chat.id}`]
**β’ πππ³πΎπ΄π :** {from_user_mention}
**β’ πππ΄π :** {mention}
**β’ πππ΄π πΈπ³:** `{user_id}`
**β’ π±π°π½π½π΄π³ πΈπ½ :** {number_of_chats} π²π·π°ππ"""
            try:
                await m.delete()
            except Exception:
                pass
            await message.reply_text(
                f"{ban_text}",
                disable_web_page_preview=True,
            )
            return


@app.on_message(filters.command("ungban") & filters.user(SUDO_USERS))
async def unban_globally(_, message):
    if not message.reply_to_message:
        if len(message.command) != 2:
            await message.reply_text(
                "**π΄ππ°πΌπΏπ»π΄ :**\n/ungban [πππ΄ππ½π°πΌπ΄/πΈπ³]"
            )
            return
        user = message.text.split(None, 1)[1]
        if "@" in user:
            user = user.replace("@", "")
        user = await app.get_users(user)
        from_user = message.from_user
        if user.id == from_user.id:
            await message.reply_text("Β» πΈ π°π»ππ΄π°π³π ππΎπ»π³ ππΎπ ππ·π°π ππΎπ π²π°π½'π πΆπ±π°π½ ππΎππππ΄π»π΅ ππΎ π·πΎπ ππ·π΄ π΅π*πΊ ππΎππ'ππ΄ πππΏπΈπ½πΆ ππΎ ππ½πΆπ±π°π½ ππΎππππ΄π»π΅ !")
        elif user.id == BOT_ID:
            await message.reply_text("Β» π±π»πΎπΎπ³π π½πΎπΎπ±, πΈ'πΌ ππ΄π»π»πΈπ½πΆ ππΎπ π³πΎπ½'π π²πΎπΌπ΄ π±π°π²πΊ π°πΆπ°πΈπ½ π΄π»ππ΄ πΈ ππΈπ»π» ππ΄π»π» πΌπ π±π°π±π ππΎ π΅π*πΊ ππΎπ ππΏ !")
        elif user.id in SUDO_USERS:
            await message.reply_text("Β» ππ΄π°π³ ππ·πΈπ πππ°ππ΄πΌπ΄π½π π»π°ππ ππΈπΌπ΄, πΈ'πΌ π½πΎπ πΆπΎπ½π½π° ππ΄π»π» ππΎπ π°πΆπ°πΈπ½-π½-π°πΆπ°πΈπ½ ππ·π°π ππΎπ π²π°π½'π πΆπ±π°π½ πΌπ π±π°π±π !")
        else:
            is_gbanned = await is_gbanned_user(user.id)
            if not is_gbanned:
                await message.reply_text("Β» ππ·πΈπ πππ΄π πΈπ π½πΎπ πΆπ±π°π½π½π΄π³ !")
            else:
                await remove_gban_user(user.id)
                await message.reply_text(f"Β» ππ΄πΌπΎππ΄π³ π΅ππΎπΌ πΆπ±π°π½π½π΄π³ πππ΄ππ π»πΈππ...")
        return
    from_user_id = message.from_user.id
    user_id = message.reply_to_message.from_user.id
    mention = message.reply_to_message.from_user.mention
    if user_id == from_user_id:
        await message.reply_text("Β» πΈ π°π»ππ΄π°π³π ππΎπ»π³ ππΎπ ππ·π°π ππΎπ π²π°π½'π πΆπ±π°π½ ππΎππππ΄π»π΅ ππΎ π·πΎπ π΅π*πΊ ππΎπ'ππ΄ ππππΈπ½πΆ ππΎ ππ½πΆπ±π°π½ ππΎππππ΄π»π΅ !")
    elif user_id == BOT_ID:
        await message.reply_text(
            "Β» π±π»πΎπΎπ³π π½πΎπΎπ±, πΈ'πΌ ππ΄π»π»πΈπ½πΆ ππΎπ π³πΎπ½'π π²πΎπΌπ΄ π±π°π²πΊ π°πΆπ°πΈπ½ π΄π»ππ΄ πΈ ππΈπ»π» ππ΄π»π» πΌπ π±π°π±π ππΎ π΅π*πΊ ππΎπ ππΏ !"
        )
    elif user_id in SUDO_USERS:
        await message.reply_text("Β» ππ΄π°π³ ππ·πΈπ πππ°ππ΄πΌπ΄π½π π»π°ππ ππΈπΌπ΄, πΈ'πΌ π½πΎπ πΆπΎπ½π½π° ππ΄π»π» ππΎπ π°πΆπ°πΈπ½-π½-π°πΆπ°πΈπ½ ππ·π°π ππΎπ π²π°π½'π πΆπ±π°π½ πΌπ π±π°π±π !")
    else:
        is_gbanned = await is_gbanned_user(user_id)
        if not is_gbanned:
            await message.reply_text("Β» ππ·πΈπ πππ΄π πΈπ π½πΎπ πΆπ±π°π½π½π΄π³ !")
        else:
            await remove_gban_user(user_id)
            await message.reply_text(f"Β» ππ΄πΌπΎππ΄π³ π΅ππΎπΌ πΆπ±π°π½π½π΄π³ πππ΄ππ π»πΈππ...")



chat_watcher_group = 5

@app.on_message(group=chat_watcher_group)
async def chat_watcher_func(_, message):
    try:
        userid = message.from_user.id
    except Exception:
        return
    checking = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
    if await is_gbanned_user(userid):
        try:
            await message.chat.kick_member(userid)
        except Exception:
            return
        await message.reply_text(
            f"{checking} πΈπ πΆπ»πΎπ±π°π»π»π π±π°π½π½π΄π³ πΎπ½ {BOT_NAME}\n\n**ππ΄π°ππΎπ½ :** ΚΚα΄α΄α΄ α΄ sα΄α΄Κα΄, Κα΄Ι΄α΄ΙͺΚα΄α΄α΄’, Κα΄Κα΄Ι΄ α΄α΄ Κα΄α΄α΄."
        )
