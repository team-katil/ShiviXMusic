import os
import asyncio
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery
from asyncio import QueueEmpty
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from config import get_queue
from ShiviXMusic.Cache.checker import checkerCB
from ShiviXMusic.Cache.admins import AdminRightsCheck, AdminRightsCheckCB
from ShiviXMusic.Helpers.Thumbnails import thumb_init
from ShiviXMusic.Helpers.Ytinfo import get_yt_info_id
from ShiviXMusic.Helpers.PyTgCalls import Queues, ShiviX
from ShiviXMusic.Helpers.Changers import time_to_seconds
from ShiviXMusic.Helpers.PyTgCalls.Converter import convert
from ShiviXMusic.Helpers.PyTgCalls.Downloader import download
from ShiviXMusic import BOT_USERNAME, BOT_NAME, app, db_mem
from ShiviXMusic.Helpers.Inline import (audio_markup, primary_markup, close_key)
from ShiviXMusic.Helpers.Database import (add_active_chat, is_active_chat, remove_active_chat, is_music_playing, music_off, music_on)


loop = asyncio.get_event_loop()


@app.on_callback_query(
    filters.regex(pattern=r"^(pausecb|skipcb|stopcb|resumecb)$")
)
@AdminRightsCheckCB
@checkerCB
async def admin_risghts(_, CallbackQuery):
    global get_queue
    command = CallbackQuery.matches[0].group(1)
    if not await is_active_chat(CallbackQuery.message.chat.id):
        return await CallbackQuery.answer(
            "» 𝙳𝙸𝙳 𝚈𝙾𝚄 𝚁𝙴𝙼𝙴𝙼𝙱𝙴𝚁 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄'𝚅𝙴 𝙿𝙻𝙰𝚈𝙴𝙳 𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 ?", show_alert=True
        )
    chat_id = CallbackQuery.message.chat.id
    if command == "pausecb":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "» 𝚂𝚃𝚁𝙴𝙰𝙼 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙿𝙰𝚄𝚂𝙴𝙳.", show_alert=True
            )
        await music_off(chat_id)
        await ShiviX.pytgcalls.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝙿𝙰𝚄𝚂𝙴𝙳** ☁️\n│ \n└𝙱𝚈 : {CallbackQuery.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
        await CallbackQuery.answer("» 𝚂𝚃𝚁𝙴𝙰𝙼 𝙿𝙰𝚄𝚂𝙴𝙳.")
    if command == "resumecb":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "» 𝙳𝙸𝙳 𝚈𝙾𝚄 𝚁𝙴𝙼𝙴𝙼𝙱𝙴𝚁 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄'𝚅𝙴 𝙿𝙰𝚄𝚂𝙴𝙳 𝚃𝙷𝙴 𝚂𝚃𝚁𝙴𝙰𝙼 ?", show_alert=True
            )
        await music_on(chat_id)
        await ShiviX.pytgcalls.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝚁𝙴𝚂𝚄𝙼𝙴𝙳** ✨\n│ \n└𝙱𝚈 : {CallbackQuery.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
        await CallbackQuery.answer("» 𝚂𝚃𝚁𝙴𝙰𝙼 𝚁𝙴𝚂𝚄𝙼𝙴𝙳.")
    if command == "stopcb":
        try:
            Queues.clear(chat_id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await ShiviX.pytgcalls.leave_group_call(chat_id)
        await CallbackQuery.message.reply_text(
            f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝙴𝙽𝙳𝙴𝙳/𝚂𝚃𝙾𝙿𝙴𝙳** ❄\n│ \n└𝙱𝚈 : {CallbackQuery.from_user.first_name} 🥀",
            reply_markup=close_key,
        )
        await CallbackQuery.message.delete()
        await CallbackQuery.answer("» 𝚂𝚃𝚁𝙴𝙰𝙼 𝙴𝙽𝙳𝙴𝙳.")
    if command == "skipcb":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await CallbackQuery.message.reply_text(
                f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝙺𝙸𝙿𝙿𝙴𝙳** 🥺\n│ \n└𝙱𝚈 : {CallbackQuery.from_user.first_name} 🥀\n\n» 𝙽𝙾 𝙼𝙾𝚁𝙴 𝚀𝚄𝙴𝚄𝙴𝙳 𝚃𝚁𝙰𝙲𝙺𝙴𝙳 𝙸𝙽 {CallbackQuery.message.chat.title}, **𝙻𝙴𝙰𝚅𝙸𝙽𝙶 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃.**",
              reply_markup=close_key,
            )
            await ShiviX.pytgcalls.leave_group_call(chat_id)
            await CallbackQuery.message.delete()
            await CallbackQuery.answer(
                "» 𝚂𝙺𝙸𝙿𝙿𝙴𝙳, 𝙽𝙾 𝙼𝙾𝚁𝙴 𝚃𝚁𝙰𝙲𝙺 𝙸𝙽 𝚀𝚄𝙴𝚄𝙴."
            )
            return
        else:
            videoid = Queues.get(chat_id)["file"]
            got_queue = get_queue.get(CallbackQuery.message.chat.id)
            if got_queue:
                got_queue.pop(0)
            finxx = f"{videoid[0]}{videoid[1]}{videoid[2]}"
            aud = 0
            if str(finxx) != "raw":
                await CallbackQuery.message.delete()
                await CallbackQuery.answer(
                    "𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝙺𝙸𝙿𝙿𝙴𝙳..."
                )
                mystic = await CallbackQuery.message.reply_text(
                    f"**𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙽𝙴𝚂𝚃 𝚃𝚁𝙰𝙲𝙺 𝙵𝚁𝙾𝙼 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃...\n\n𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝙺𝙸𝙿𝙿𝙴𝙳 𝙱𝚈  {CallbackQuery.from_user.mention} !**🥀"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**{BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title[:40]}\n\n0% ■■■■■■■■■■■■ 100%"
                )
                downloaded_file = await loop.run_in_executor(
                    None, download, videoid, mystic, title
                )
                raw_path = await convert(downloaded_file)
                await ShiviX.pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            raw_path,
                        ),
                    ),
                )
                chat_title = CallbackQuery.message.chat.title
                thumb = await thumb_init(videoid)
                buttons = primary_markup(
                    videoid,
                    CallbackQuery.from_user.id
                )
                await mystic.delete()
                mention = db_mem[videoid]["username"]
                final_output = await CallbackQuery.message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>➻ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶</b>\n\n<b>✨ ᴛɪᴛʟᴇ :</b> [{title[:40]}](https://www.youtube.com/watch?v={videoid})\n☁ <b>𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 :</b> {duration_min} 𝙼𝙸𝙽𝚄𝚃𝙴𝙳\n🥀 <b>𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :</b> {mention}"
                    ),
                )
                os.remove(thumb)

            else:
                await CallbackQuery.message.delete()
                await CallbackQuery.answer("𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝙺𝙸𝙿𝙿𝙴𝙳...")
                await ShiviX.pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            videoid,
                        ),
                    ),
                )
                afk = videoid
                title = db_mem[videoid]["title"]
                duration_min = db_mem[videoid]["duration"]
                duration_sec = int(time_to_seconds(duration_min))
                mention = db_mem[videoid]["username"]
                videoid = db_mem[videoid]["videoid"]
                if str(videoid) == "smex1":
                    buttons = primary_markup(
                        videoid,
                        CallbackQuery.from_user.id,
                    )
                    thumb = "ShiviXMusic/Utilities/Audio.jpeg"
                    aud = 1
                else:
                    _path_ = _path_ = (
                        (str(afk))
                        .replace("_", "", 1)
                        .replace("/", "", 1)
                        .replace(".", "", 1)
                    )
                    thumb = f"ShiviXMusic/Cache/{_path_}final.png"
                    buttons = primary_markup(
                        videoid,
                        CallbackQuery.from_user.id,
                    )
                final_output = await CallbackQuery.message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>➻ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶</b>\n\n<b>✨ 𝚃𝙸𝚃𝙻𝙴 :</b> {title[:40]}\n☁ <b>𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 :</b> {duration_min} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂\n🥀 <b>𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :</b> {mention}",
                )


@app.on_callback_query(filters.regex("close"))
async def closed(_, query: CallbackQuery):
    await query.message.delete()
    await query.answer()

