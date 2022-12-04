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


__MODULE__ = "𝙰𝙳𝙼𝙸𝙽𝚂"
__HELP__ = """


/pause
» 𝙿𝙰𝚄𝚂𝙴 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚃𝚁𝙴𝙰𝙼.

/resume
» 𝚁𝙴𝚂𝚄𝙼𝙴𝙳 𝚃𝙷𝙴 𝙿𝙰𝚄𝚂𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼.

/skip ᴏʀ /next
» 𝚂𝙺𝙸𝙿 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚃𝚁𝙴𝙰𝙼.

/end ᴏʀ /stop
» 𝙴𝙽𝙳 𝚃𝙷𝙴 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝚂𝚃𝚁𝙴𝙰𝙼.

/queue
» 𝚂𝙷𝙾𝚆𝚂 𝚃𝙷𝙴 𝙻𝙸𝚂𝚃 𝙾𝙵 𝚀𝚄𝙴𝚄𝙴𝙳 𝚃𝚁𝙰𝙲𝙺𝚂.

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
        return await message.reply_text("**𝚆𝚃𝙵😡 !**")
    if not await is_active_chat(message.chat.id):
        return await message.reply_text("**» 𝙳𝙸𝙳 𝚈𝙾𝚄 𝚁𝙴𝙼𝙴𝙼𝙱𝙴𝚁 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄'𝚅𝙴 𝙿𝙻𝙰𝚈𝙴𝙳 𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 ?**")
    chat_id = message.chat.id
    if message.command[0][1] == "a":
        if not await is_music_playing(message.chat.id):
            return await message.reply_text("**» 𝚂𝚃𝚁𝙴𝙰𝙼 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙿𝙰𝚄𝚂𝙴𝙳.**")
        await music_off(chat_id)
        await ShiviX.pytgcalls.pause_stream(chat_id)
        await message.reply_text(
            f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝙿𝙰𝚄𝚂𝙴𝙳** ☁️\n│ \n└𝙱𝚈 : {message.from_user.first_name} 🥀",
            reply_markup=audio_markup,
        )
    if message.command[0][1] == "e":
        if await is_music_playing(message.chat.id):
            return await message.reply_text("**» 𝙳𝙸𝙳 𝚈𝙾𝚄 𝚁𝙴𝙼𝙴𝙼𝙱𝙴𝚁 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄'𝚅𝙴 𝙿𝙰𝚄𝚂𝙴𝙳 𝚂𝙾𝙼𝙴𝚃𝙷𝙸𝙽𝙶 ?**")
        await music_on(chat_id)
        await ShiviX.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(
            f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝚁𝙴𝚂𝚄𝙼𝙴𝙳** ✨\n│ \n└𝙱𝚈 : {message.from_user.first_name} 🥀",
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
            f"➻ **𝚂𝚃𝚁𝙴𝙰𝙽 𝙴𝙽𝙳𝙴𝙳/𝚂𝚃𝙾𝙿𝙿𝙴𝙳** ❄\n│ \n└𝙱𝚈 : {message.from_user.first_name} 🥀",
            reply_markup=close_key,
        )
    if message.command[0][1] == "k" or message.command[0][2] == "x":
        Queues.task_done(chat_id)
        if Queues.is_empty(chat_id):
            await remove_active_chat(chat_id)
            await message.reply_text(
                f"➻ **𝚂𝚃𝚁𝙴𝙰𝙼 𝚂𝙺𝙸𝙿𝙿𝙴𝙳** 🥺\n│ \n└𝙱𝚈 : {message.from_user.first_name} 🥀\n\n» 𝙽𝙾 𝙼𝙾𝚁𝙴 𝚀𝚄𝙴𝚄𝙴𝙳 𝚃𝚁𝙰𝙲𝙺𝚂 𝙸𝙽 {message.chat.title}, **𝙻𝙴𝙰𝚅𝙸𝙽𝙶 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃.**",
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
                    f"**» 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙸𝙽𝙶 𝙽𝙴𝚇𝚃 𝚃𝚁𝙰𝙲𝙺 𝙵𝚁𝙾𝙼 𝙿𝙻𝙰𝚈𝙻𝙸𝚂𝚃...**"
                )
                (
                    title,
                    duration_min,
                    duration_sec,
                    thumbnail,
                ) = get_yt_info_id(videoid)
                await mystic.edit(
                    f"**» {BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n\n0% ▓▓▓▓▓▓▓▓▓▓▓▓ 100%"
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
                        f"<b>➻ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙶</b>\n\n<b>✨ 𝚃𝙸𝚃𝙻𝙴 :</b> [{title[:40]}](https://www.youtube.com/watch?v={videoid})\n☁ <b>𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 :</b> {duration_min} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂\n🥀 <b>𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :</b> {mention}"
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
                    caption=f"<b>➻ 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚂𝚃𝚁𝙴𝙰𝙼𝙸𝙽𝙷</b>\n\n<b>✨ 𝚃𝙸𝚃𝙻𝙴 :</b> {title[:40]}\n☁ <b>𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 :</b> {duration_min} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂\n🥀 <b>𝚁𝙴𝚀𝚄𝙴𝚂𝚃𝙴𝙳 𝙱𝚈 :</b> {mention}",
                )
