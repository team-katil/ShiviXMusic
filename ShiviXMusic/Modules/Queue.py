import os
import asyncio

from config import get_queue
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery

from ShiviXMusic import app, db_mem
from ShiviXMusic.Helpers.Database import is_active_chat
from ShiviXMusic.Helpers.Inline import primary_markup


__MODULE__ = "πππ΄ππ΄"
__HELP__ = """
 
/queue
Β» ππ·πΎππ ππ·π΄ π»πΈππ πΎπ΅ πππ΄ππ΄π³ πππ°π²πΊπ πΈπ½ ππ·π΄ πππ΄ππ΄.

"""


@app.on_callback_query(filters.regex("pr_go_back_timer"))
async def pr_go_back_timer(_, CallbackQuery):
    await CallbackQuery.answer()
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, user_id = callback_request.split("|")
    if await is_active_chat(CallbackQuery.message.chat.id):
        if db_mem[CallbackQuery.message.chat.id]["videoid"] == videoid:
            dur_left = db_mem[CallbackQuery.message.chat.id]["left"]
            duration_min = db_mem[CallbackQuery.message.chat.id]["total"]
            buttons = primary_markup(videoid, user_id)
            await CallbackQuery.edit_message_reply_markup(reply_markup=InlineKeyboardMarkup(buttons))
   

@app.on_callback_query(filters.regex("timer_checkup_markup"))
async def timer_checkup_markup(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    videoid, user_id = callback_request.split("|")
    if await is_active_chat(CallbackQuery.message.chat.id):
        if db_mem[CallbackQuery.message.chat.id]["videoid"] == videoid:
            dur_left = db_mem[CallbackQuery.message.chat.id]["left"]
            duration_min = db_mem[CallbackQuery.message.chat.id]["total"]
            return await CallbackQuery.answer(
                f"ππ΄πΌπ°πΈπ½πΈπ½πΆ {dur_left} πΎππ πΎπ΅ {duration_min} πΌπΈπ½πππ΄π.",
                show_alert=True,
            )
        return await CallbackQuery.answer(f"π½πΎππ·πΈπ½πΆ πΈπ πΏπ»π°ππΈπ½πΆ...", show_alert=True)
    else:
        return await CallbackQuery.answer(
            f"π½πΎ π°π²ππΈππ΄ ππΈπ³π΄πΎπ²π·π°π π΅πΎππ½π³.", show_alert=True
        )


@app.on_message(filters.command("queue"))
async def activevc(_, message: Message):
    global get_queue
    if await is_active_chat(message.chat.id):
        mystic = await message.reply_text("**Β» πΏπ»π΄π°ππ΄ ππ°πΈπ, πΆπ΄πππΈπ½πΆ πππ΄ππ΄...**")
        dur_left = db_mem[message.chat.id]["left"]
        duration_min = db_mem[message.chat.id]["total"]
        got_queue = get_queue.get(message.chat.id)
        if not got_queue:
            await mystic.edit("**Β» πππ΄ππ΄ π΄πΌπΏππ.**")
        fetched = []
        for get in got_queue:
            fetched.append(get)

        current_playing = fetched[0][0]
        user_name = fetched[0][1]

        msg = "**πππ΄ππ΄π³ π»πΈππ**\n\n"
        msg += "**πΏπ»π°ππΈπ½πΆ :**"
        msg += "\nβ£" + current_playing[:30]
        msg += f"\n   β π±π : {user_name}"
        msg += f"\n   β π³πππ°ππΈπΎ  : ππ΄πΌπ°πΈπ½πΈπ½πΆ `{dur_left}` πΎππ πΎπ΅ `{duration_min}` πΌπΈπ½πππ΄π."
        fetched.pop(0)
        if fetched:
            msg += "\n\n"
            msg += "**π½π΄ππ πΈπ½ πππ΄ππ΄ :**"
            for song in fetched:
                name = song[0][:30]
                usr = song[1]
                dur = song[2]
                msg += f"\nββ {name}"
                msg += f"\n   β  π³πππ°ππΈπΎπ½ : {dur}"
                msg += f"\n   β πππππ΄πππ΄π³ π±π : {usr}\n"
        if len(msg) > 4096:
            await mystic.delete()
            filename = "queue.txt"
            with open(filename, "w+", encoding="utf8") as out_file:
                out_file.write(str(msg.strip()))
            await message.reply_document(
                document=filename,
                caption="**πππ΄ππ΄ π»πΈππ**",
                quote=False,
            )
            os.remove(filename)
        else:
            await mystic.edit(msg)
    else:
        await message.reply_text(f"**Β» πππ΄ππ΄ π΄πΌπΏππ.**")

