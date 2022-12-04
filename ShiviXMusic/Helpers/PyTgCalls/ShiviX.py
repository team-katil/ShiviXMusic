import os
import time
import asyncio

from config import get_queue
from asyncio import QueueEmpty
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls.types.input_stream import InputAudioStream, InputStream
from pyrogram.types import (CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup, Message)

from ShiviXMusic import BOT_NAME, app, db_mem, Ass
from ShiviXMusic.Helpers.PyTgCalls import Queues
from ShiviXMusic.Helpers.PyTgCalls.Converter import convert
from ShiviXMusic.Helpers.PyTgCalls.Downloader import download
from ShiviXMusic.Helpers.Database import remove_active_chat
from ShiviXMusic.Helpers.Inline import primary_markup
from ShiviXMusic.Helpers.Changers import time_to_seconds
from ShiviXMusic.Helpers.Thumbnails import thumb_init
from ShiviXMusic.Helpers.Ytinfo import get_yt_info_id

pytgcalls = PyTgCalls(Ass)


@pytgcalls.on_kicked()
async def kicked_handler(_, chat_id: int):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


@pytgcalls.on_closed_voice_chat()
async def closed_voice_chat_handler(_, chat_id: int):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


@pytgcalls.on_left()
async def left_handler(_, chat_id: int):
    try:
        Queues.clear(chat_id)
    except QueueEmpty:
        pass
    await remove_active_chat(chat_id)


@pytgcalls.on_stream_end()
async def stream_end_handler(_, update: Update):
    chat_id = update.chat_id
    try:
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await pytgcalls.leave_group_call(chat_id)
        else:
            afk = Queues.get(chat_id)["file"]
            finxx = f"{afk[0]}{afk[1]}{afk[2]}"
            got_queue = get_queue.get(chat_id)
            if got_queue:
                got_queue.pop(0)
            aud = 0
            if str(finxx) != "raw":
                mystic = await app.send_message(
                    chat_id,
                    "**» 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙽𝙴𝚇𝚃 𝚃𝚁𝙰𝙲𝙹 𝙵𝚁𝙾𝙼 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃...**",
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(afk)
                mystic = await mystic.edit(
                    f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n\n0% ■■■■■■■■■■■■ 100%"
                )
                loop = asyncio.get_event_loop()
                downloaded_file = await loop.run_in_executor(
                    None, download, afk, mystic, title
                )
                raw_path = await convert(downloaded_file)
                await pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            raw_path,
                        ),
                    ),
                )
                chat_title = db_mem[afk]["chat_title"]
                user_id = db_mem[afk]["user_id"]
                videoid = afk
                thumb = await thumb_init(videoid)
                buttons = primary_markup(
                    afk, user_id
                )
                await mystic.delete()
                mention = db_mem[afk]["username"]
                finaltext = await app.send_photo(
                    chat_id,
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=(
                        f"<b>➻ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶</b>\n\n**✨ 𝚃𝙸𝚃𝙻𝙴 :** [{title[:40]}](https://www.youtube.com/watch?v={afk}) \n**🥀 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {mention}"
                    ),
                )
                os.remove(thumb)
                videoid = afk
            else:
                videoid = afk
                await pytgcalls.change_stream(
                    chat_id,
                    InputStream(
                        InputAudioStream(
                            afk,
                        ),
                    ),
                )
                title = db_mem[videoid]["title"]
                duration_min = db_mem[videoid]["duration"]
                duration_sec = int(time_to_seconds(duration_min))
                mention = db_mem[videoid]["username"]
                videoid = db_mem[videoid]["videoid"]
                if str(videoid) == "smex1":
                    buttons = buttons = primary_markup(
                        videoid, "283402"
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
                    thumb = f"ShiviXMusic/Cache/{_path_}.jpg"
                    buttons = primary_markup(
                        videoid, "283402"
                    )
                finaltext = await app.send_photo(
                    chat_id,
                    photo=thumb,
                    reply_markup=InlineKeyboardMarkup(buttons),
                    caption=f"<b>➻ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶</b>\n\n**✨ 𝚃𝙸𝚃𝙻𝙴 :** {title[:40]}\n**🥀 𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :** {mention}",
                )
    except Exception as e:
        print(e)


run = pytgcalls.run
