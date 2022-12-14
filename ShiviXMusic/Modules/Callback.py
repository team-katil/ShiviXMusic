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
            "Β» π³πΈπ³ ππΎπ ππ΄πΌπ΄πΌπ±π΄π ππ·π°π ππΎπ'ππ΄ πΏπ»π°ππ΄π³ ππΎπΌπ΄ππ·πΈπ½πΆ ?", show_alert=True
        )
    chat_id = CallbackQuery.message.chat.id
    if command == "pausecb":
        if not await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "Β» ππππ΄π°πΌ π°π»ππ΄π°π³π πΏπ°πππ΄π³.", show_alert=True
            )
        await music_off(chat_id)
        await ShiviX.pytgcalls.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(
            f"β» **ππππ΄π°πΌ πΏπ°πππ΄π³** βοΈ\nβ \nβπ±π : {CallbackQuery.from_user.first_name} π₯",
            reply_markup=audio_markup,
        )
        await CallbackQuery.answer("Β» ππππ΄π°πΌ πΏπ°πππ΄π³.")
    if command == "resumecb":
        if await is_music_playing(chat_id):
            return await CallbackQuery.answer(
                "Β» π³πΈπ³ ππΎπ ππ΄πΌπ΄πΌπ±π΄π ππ·π°π ππΎπ'ππ΄ πΏπ°πππ΄π³ ππ·π΄ ππππ΄π°πΌ ?", show_alert=True
            )
        await music_on(chat_id)
        await ShiviX.pytgcalls.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(
            f"β» **ππππ΄π°πΌ ππ΄πππΌπ΄π³** β¨\nβ \nβπ±π : {CallbackQuery.from_user.first_name} π₯",
            reply_markup=audio_markup,
        )
        await CallbackQuery.answer("Β» ππππ΄π°πΌ ππ΄πππΌπ΄π³.")
    if command == "stopcb":
        try:
            Queues.clear(chat_id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await ShiviX.pytgcalls.leave_group_call(chat_id)
        await CallbackQuery.message.reply_text(
            f"β» **ππππ΄π°πΌ π΄π½π³π΄π³/πππΎπΏπ΄π³** β\nβ \nβπ±π : {CallbackQuery.from_user.first_name} π₯",
            reply_markup=close_key,
        )
        await CallbackQuery.message.delete()
        await CallbackQuery.answer("Β» ππππ΄π°πΌ π΄π½π³π΄π³.")
    if command == "skipcb":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await CallbackQuery.message.reply_text(
                f"β» **ππππ΄π°πΌ ππΊπΈπΏπΏπ΄π³** π₯Ί\nβ \nβπ±π : {CallbackQuery.from_user.first_name} π₯\n\nΒ» π½πΎ πΌπΎππ΄ πππ΄ππ΄π³ πππ°π²πΊπ΄π³ πΈπ½ {CallbackQuery.message.chat.title}, **π»π΄π°ππΈπ½πΆ ππΈπ³π΄πΎ π²π·π°π.**",
              reply_markup=close_key,
            )
            await ShiviX.pytgcalls.leave_group_call(chat_id)
            await CallbackQuery.message.delete()
            await CallbackQuery.answer(
                "Β» ππΊπΈπΏπΏπ΄π³, π½πΎ πΌπΎππ΄ πππ°π²πΊ πΈπ½ πππ΄ππ΄."
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
                    "ππππ΄π°πΌ ππΊπΈπΏπΏπ΄π³..."
                )
                mystic = await CallbackQuery.message.reply_text(
                    f"**π³πΎππ½π»πΎπ°π³πΈπ½πΆ π½π΄ππ πππ°π²πΊ π΅ππΎπΌ πΏπ»π°ππ»πΈππ...\n\nππππ΄π°πΌ ππΊπΈπΏπΏπ΄π³ π±π  {CallbackQuery.from_user.mention} !**π₯"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**{BOT_NAME} π³πΎππ½π»πΎπ°π³π΄π**\n\n**ππΈππ»π΄ :** {title[:40]}\n\n0% β β β β β β β β β β β β  100%"
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
                        f"<b>β» πππ°πππ΄π³ ππππ΄π°πΌπΈπ½πΆ</b>\n\n<b>β¨ α΄Ιͺα΄Κα΄ :</b> [{title[:40]}](https://www.youtube.com/watch?v={videoid})\nβ <b>π³πππ°ππΈπΎπ½ :</b> {duration_min} πΌπΈπ½πππ΄π³\nπ₯ <b>ππ΄πππ΄πππ΄π³ π±π :</b> {mention}"
                    ),
                )
                os.remove(thumb)

            else:
                await CallbackQuery.message.delete()
                await CallbackQuery.answer("ππππ΄π°πΌ ππΊπΈπΏπΏπ΄π³...")
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
                    caption=f"<b>β» πππ°πππ΄π³ ππππ΄π°πΌπΈπ½πΆ</b>\n\n<b>β¨ ππΈππ»π΄ :</b> {title[:40]}\nβ <b>π³πππ°ππΈπΎπ½ :</b> {duration_min} πΌπΈπ½πππ΄π\nπ₯ <b>ππ΄πππ΄πππ΄π³ π±π :</b> {mention}",
                )


@app.on_callback_query(filters.regex("close"))
async def closed(_, query: CallbackQuery):
    await query.message.delete()
    await query.answer()

