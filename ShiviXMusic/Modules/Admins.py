import os
import random
import asyncio

from pyrogram import filters
from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, KeyboardButton, Message)
from config import get_queue
from asyncio import QueueEmpty
from pytgcalls import StreamType
from pytgcalls.types.input_stream import InputAudioStream, InputStream

from ShiviXMusic import BOT_NAME, app, db_mem
from ShiviXMusic.Cache.admins import AdminRightsCheck
from ShiviXMusic.Cache.checker import checker, checkerCB
from ShiviXMusic.Helpers.Ytinfo import get_yt_info_id
from ShiviXMusic.Helpers.Thumbnails import thumb_init
from ShiviXMusic.Helpers.Changers import time_to_seconds
from ShiviXMusic.Helpers.PyTgCalls import Queues, ShiviX
from ShiviXMusic.Helpers.PyTgCalls.Converter import convert
from ShiviXMusic.Helpers.PyTgCalls.Downloader import download
from ShiviXMusic.Helpers.Inline import primary_markup, close_key, audio_markup
from ShiviXMusic.Helpers.Database import (is_active_chat, is_music_playing, music_off,
                            music_on, remove_active_chat)


loop = asyncio.get_event_loop()


__MODULE__ = "π°π³πΌπΈπ½π"
__HELP__ = """


/pause
Β» πΏπ°πππ΄ ππ·π΄ π²ππππ΄π½π ππππ΄π°πΌ.

/resume
Β» ππ΄πππΌπ΄π³ ππ·π΄ πΏπ°πππ΄π³ ππππ΄π°πΌ.

/skip α΄Κ /next
Β» ππΊπΈπΏ ππ·π΄ π²ππππ΄π½π ππππ΄π°πΌ.

/end α΄Κ /stop
Β» π΄π½π³ ππ·π΄ π²ππππ΄π½π ππππ΄π°πΌ.

/queue
Β» ππ·πΎππ ππ·π΄ π»πΈππ πΎπ΅ πππ΄ππ΄π³ πππ°π²πΊπ.

"""


@app.on_message(
    filters.command(["pause", "skip", "next", "resume", "stop", "end"])
    & filters.group
)
@AdminRightsCheck
@checker
async def admins(_, message: Message):
    global get_queue
    if not len(message.command) == 1:
        return await message.reply_text("**πππ΅π‘ !**")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("**Β» π³πΈπ³ ππΎπ ππ΄πΌπ΄πΌπ±π΄π ππ·π°π ππΎπ'ππ΄ πΏπ»π°ππ΄π³ ππΎπΌπ΄ππ·πΈπ½πΆ ?**")
    chat_id = message.chat.id
    if message.command[0][1] == "a":
        if not await is_music_playing(message.chat.id):
            return await message.reply_text("**Β» ππππ΄π°πΌ π°π»ππ΄π°π³π πΏπ°πππ΄π³.**")
        await music_off(chat_id)
        await ShiviX.pytgcalls.pause_stream(chat_id)
        await message.reply_text(
            f"β» **ππππ΄π°πΌ πΏπ°πππ΄π³** βοΈ\nβ \nβπ±π : {message.from_user.first_name} π₯",
            reply_markup=audio_markup,
        )
    if message.command[0][1] == "e":
        if await is_music_playing(message.chat.id):
            return await message.reply_text("**Β» π³πΈπ³ ππΎπ ππ΄πΌπ΄πΌπ±π΄π ππ·π°π ππΎπ'ππ΄ πΏπ°πππ΄π³ ππΎπΌπ΄ππ·πΈπ½πΆ ?**")
        await music_on(chat_id)
        await ShiviX.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(
            f"β» **ππππ΄π°πΌ ππ΄πππΌπ΄π³** β¨\nβ \nβπ±π : {message.from_user.first_name} π₯",
            reply_markup=audio_markup,
        )
    if message.command[0][1] == "t" or message.command[0][1] == "n":
        try:
            Queues.clear(message.chat.id)
        except QueueEmpty:
            pass
        await remove_active_chat(chat_id)
        await ShiviX.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(
            f"β» **ππππ΄π°π½ π΄π½π³π΄π³/πππΎπΏπΏπ΄π³** β\nβ \nβπ±π : {message.from_user.first_name} π₯",
            reply_markup=close_key,
        )
    if message.command[0][1] == "k" or message.command[0][2] == "x":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await message.reply_text(
                f"β» **ππππ΄π°πΌ ππΊπΈπΏπΏπ΄π³** π₯Ί\nβ \nβπ±π : {message.from_user.first_name} π₯\n\nΒ» π½πΎ πΌπΎππ΄ πππ΄ππ΄π³ πππ°π²πΊπ πΈπ½ {message.chat.title}, **π»π΄π°ππΈπ½πΆ ππΈπ³π΄πΎ π²π·π°π.**",
                reply_markup=close_key,
            )
            await ShiviX.pytgcalls.leave_group_call(message.chat.id)
            return
        else:
            videoid = Queues.get(chat_id)["file"]
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            finxx = f"{videoid[0]}{videoid[1]}{videoid[2]}"
            aud = 0
            if str(finxx) != "raw":
                mystic = await message.reply_text(
                    f"**Β» π³πΎππ½π»πΎπ°π³πΈπ½πΆ π½π΄ππ πππ°π²πΊ π΅ππΎπΌ πΏπ»π°ππ»πΈππ...**"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**Β» {BOT_NAME} π³πΎππ½π»πΎπ°π³π΄π**\n\n**ππΈππ»π΄ :** {title}\n\n0% ββββββββββββ 100%"
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
                chat_title = message.chat.title
                thumb = await thumb_init(videoid)
                buttons = primary_markup(
                    videoid, message.from_user.id
                )
                await mystic.delete()
                mention = db_mem[videoid]["username"]
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>β» πππ°πππ΄π³ ππππ΄π°πΌπΈπ½πΆ</b>\n\n<b>β¨ ππΈππ»π΄ :</b> [{title[:40]}](https://www.youtube.com/watch?v={videoid})\nβ <b>π³πππ°ππΈπΎπ½ :</b> {duration_min} πΌπΈπ½πππ΄π\nπ₯ <b>ππ΄πππ΄πππ΄π³ π±π :</b> {mention}"
                    ),
                )
                os.remove(thumb)
            else:
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
                    buttons = buttons = primary_markup(
                        videoid,
                        message.from_user.id,
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
                    thumb = f"ShiviXMusic/Cache/{_path_}.png"
                    buttons = primary_markup(
                        videoid,
                        message.from_user.id,
                    )
                final_output = await message.reply_photo(
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>β» πππ°πππ΄π³ ππππ΄π°πΌπΈπ½π·</b>\n\n<b>β¨ ππΈππ»π΄ :</b> {title[:40]}\nβ <b>π³πππ°ππΈπΎπ½ :</b> {duration_min} πΌπΈπ½πππ΄π\nπ₯ <b>ππ΄πππ΄πππ΄π³ π±π :</b> {mention}",
                )
