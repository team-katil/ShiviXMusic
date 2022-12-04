import os
import asyncio

from config import get_queue
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, CallbackQuery

from ShiviXMusic import app, db_mem
from ShiviXMusic.Helpers.Database import is_active_chat
from ShiviXMusic.Helpers.Inline import primary_markup


__MODULE__ = "𝚀𝚄𝙴𝚄𝙴"
__HELP__ = """
 
/queue
» 𝚂𝙷𝙾𝚆𝚂 𝚃𝙷𝙴 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚀𝚄𝙴𝚄𝙴𝙳 𝚃𝚁𝙰𝙲𝙺𝚂 𝙸𝙽 𝚃𝙷𝙴 𝚀𝚄𝙴𝚄𝙴.

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
                f"𝚁𝙴𝙼𝙰𝙸𝙽𝙸𝙽𝙶 {dur_left} 𝙾𝚄𝚃 𝙾𝙵 {duration_min} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂.",
                show_alert=True,
            )
        return await CallbackQuery.answer(f"𝙽𝙾𝚃𝙷𝙸𝙽𝙶 𝙸𝚂 𝙿𝙻𝙰𝚈𝙸𝙽𝙶...", show_alert=True)
    else:
        return await CallbackQuery.answer(
            f"𝙽𝙾 𝙰𝙲𝚃𝙸𝚅𝙴 𝚅𝙸𝙳𝙴𝙾𝙲𝙷𝙰𝚃 𝙵𝙾𝚄𝙽𝙳.", show_alert=True
        )


@app.on_message(filters.command("queue"))
async def activevc(_, message: Message):
    global get_queue
    if await is_active_chat(message.chat.id):
        mystic = await message.reply_text("**» 𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃, 𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝚀𝚄𝙴𝚄𝙴...**")
        dur_left = db_mem[message.chat.id]["left"]
        duration_min = db_mem[message.chat.id]["total"]
        got_queue = get_queue.get(message.chat.id)
        if not got_queue:
            await mystic.edit("**» 𝚀𝚄𝙴𝚄𝙴 𝙴𝙼𝙿𝚃𝚈.**")
        fetched = []
        for get in got_queue:
            fetched.append(get)

        current_playing = fetched[0][0]
        user_name = fetched[0][1]

        msg = "**𝚀𝚄𝙴𝚄𝙴𝙳 𝙻𝙸𝚂𝚃**\n\n"
        msg += "**𝙿𝙻𝙰𝚈𝙸𝙽𝙶 :**"
        msg += "\n‣" + current_playing[:30]
        msg += f"\n   ╚ 𝙱𝚈 : {user_name}"
        msg += f"\n   ╚ 𝙳𝚄𝚁𝙰𝚃𝙸𝙾  : 𝚁𝙴𝙼𝙰𝙸𝙽𝙸𝙽𝙶 `{dur_left}` 𝙾𝚄𝚃 𝙾𝙵 `{duration_min}` 𝙼𝙸𝙽𝚄𝚃𝙴𝚂."
        fetched.pop(0)
        if fetched:
            msg += "\n\n"
            msg += "**𝙽𝙴𝚇𝚃 𝙸𝙽 𝚀𝚄𝙴𝚄𝙴 :**"
            for song in fetched:
                name = song[0][:30]
                usr = song[1]
                dur = song[2]
                msg += f"\n❚❚ {name}"
                msg += f"\n   ╠ 𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 : {dur}"
                msg += f"\n   ╚ 𝚁𝚁𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 : {usr}\n"
        if len(msg) > 4096:
            await mystic.delete()
            filename = "queue.txt"
            with open(filename, "w+", encoding="utf8") as out_file:
                out_file.write(str(msg.strip()))
            await message.reply_document(
                document=filename,
                caption="**𝚀𝚄𝙴𝚄𝙴 𝙻𝙸𝚂𝚃**",
                quote=False,
            )
            os.remove(filename)
        else:
            await mystic.edit(msg)
    else:
        await message.reply_text(f"**» 𝚀𝚄𝙴𝚄𝙴 𝙴𝙼𝙿𝚃𝚈.**")

