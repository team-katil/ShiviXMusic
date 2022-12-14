import asyncio
from os import path

from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardMarkup, Voice
from youtube_search import YoutubeSearch

from ShiviXMusic import (BOT_USERNAME, DURATION_LIMIT_SEC, DURATION_LIMIT,
                   BOT_NAME, app, db_mem)
from ShiviXMusic.Helpers.Url import get_url
from ShiviXMusic.Cache.checker import checker
from ShiviXMusic.Cache.assistant import AssistantAdd
from ShiviXMusic.Cache.permission import PermissionCheck
from ShiviXMusic.Helpers.Thumbnails import thumb_init
from ShiviXMusic.Helpers.PyTgCalls.Converter import convert
from ShiviXMusic.Helpers.PyTgCalls.Downloader import download
from ShiviXMusic.Helpers.Database import add_served_user, add_served_chat
from ShiviXMusic.Helpers.Changers import seconds_to_min, time_to_seconds
from ShiviXMusic.Helpers.Stream import start_stream, start_stream_audio
from ShiviXMusic.Helpers.Ytinfo import (get_yt_info_id, get_yt_info_query, get_yt_info_query_slider)


loop = asyncio.get_event_loop()


@app.on_message(
    filters.command(["play", f"play@{BOT_USERNAME}"]) & filters.group
)
@checker
@PermissionCheck
@AssistantAdd
async def play(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    await add_served_chat(message.chat.id)
    if message.chat.id not in db_mem:
        db_mem[message.chat.id] = {}
    if message.sender_chat:
        return await message.reply_text(
            "**Β» ππΎπ'ππ΄ π°π½ π°π½πΎπ½ππΌπΎππ π°π³πΌπΈπ½.\n\nππ΄ππ΄ππ π±π°π²πΊ ππΎ πππ΄π π°π²π²πΎππ½π π΅πΎπ πππΈπ½πΆ πΌπ΄.**"
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text(
            "**β» πΏππΎπ²π΄πππΈπ½πΆ...\n\nπΏπ»π΄π°ππ΄ ππ°πΈπ...**"
        )

        if audio.file_size > 314572800:
            return await mystic.edit_text(
                "**Β» π°ππ³πΈπΎ π΅πΈπ»π΄ ππΈππ΄ ππΎππ»π³ π±π΄ π»π΄ππ ππ·π°π½ 300πΌπ±.**"
            )
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT_SEC:
            return await mystic.edit_text(
                f"**Β» {BOT_NAME} π³πΎπ΄ππ½'π π°π»π»πΎπ ππΎπ½πΏπ»π°π πππ°π²πΊπ π»πΎπ½πΆπ΄π ππ·π°π½ {DURATION_LIMIT_MIN} πΌπΈπ½πππ΄π.**"
            )
        file_name = (
            audio.file_unique_id
            + "."
            + (
                (audio.file_name.split(".")[-1])
                if (not isinstance(audio, Voice))
                else "ogg"
            )
        )
        file_name = path.join(path.realpath("downloads"), file_name)
        file = await convert(
            (await message.reply_to_message.download(file_name))
            if (not path.isfile(file_name))
            else file_name,
        )
        return await start_stream_audio(
            message,
            file,
            "smex1",
            "Given Audio Via Telegram",
            duration_min,
            duration_sec,
            mystic,
        )
    elif url:
        mystic = await message.reply_text("**β» ππ΄π°ππ²π·πΈπ½π·...\n\nπΏπ»π΄π°ππ΄ ππ°πΈπ...**")
        if not message.reply_to_message:
            query = message.text.split(None, 1)[1]
        else:
            query = message.reply_to_message.text
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
        if duration_sec > DURATION_LIMIT_SEC:
            return await message.reply_text(
                f"**Β» {BOT_NAME} π³πΎπ΄ππ½'π π°π»π»πΎπ ππΎπ½πΏπ»π°π πππ°π²πΊπ π»πΎπ½πΆπ΄π ππ·π°π½ {DURATION_LIMIT_MIN} πΌπΈπ½πππ΄π.**"
            )
        downloaded_file = await loop.run_in_executor(
            None, download, videoid, mystic, title
        )
        raw_path = await convert(downloaded_file)
        thumb = await thumb_init(videoid)
        await mystic.delete()
    else:
        if len(message.command) < 2:
            await message.reply_photo(
                photo="ShiviXMusic/Utilities/Play.jpeg",
                caption=(
                    "**β» ππ·πΈπ πΈπ π½πΎπ ππ·π΄ π²πΎπππ΄π²π π΅πΎππΌπ°ππ΄ ππΎ πΏπ»π°π.**\n\n**π΄ππ°πΌπΏπ»π΄ :** /play [ππΎπ½πΆ π½π°πΌπ΄ πΎπ ππΎππππ±π΄ π»πΈπ½πΊ πΎπ ππ΄πΏπ»π ππΎ π° π°ππ³πΈπΎ]"
                ),
            )
            return
        mystic = await message.reply_text("**β» ππ΄π°ππ²π·πΈπ½πΆ...\n\nπΏπ»π΄π°ππ΄ ππ°πΈπ...**")
        query = message.text.split(None, 1)[1]
        (
            title,
            duration_min,
            duration_sec,
            thumb,
            videoid,
        ) = get_yt_info_query(query)
        await mystic.delete()
    title, duration_min, duration_sec, thumbnail = get_yt_info_id(videoid)
    if duration_sec > DURATION_LIMIT_SEC:
        return await message.reply_text(
            f"**Β» {BOT_NAME} π³πΎπ΄ππ½'π π°π»π»πΎπ ππΎπ½πΏπ»π°π πππ°π²πΊπ π»πΎπ½πΆπ΄π ππ·π°π½ {DURATION_LIMIT_MIN} πΌπΈπ½πππ΄π.**"
        )
    mystic = await message.reply_text(
        f"**{BOT_NAME} π³πΎππ½π»πΎπ°π³π΄π**\n\n**ππΈππ»π΄ :** {title}\n\n0% β β β β β β β β β β β β  100%"
    )
    downloaded_file = await loop.run_in_executor(
        None, download, videoid, mystic, title
    )
    chat_id = message.chat.id
    user_id = message.from_user.id
    raw_path = await convert(downloaded_file)
    thumb = await thumb_init(videoid)
    if chat_id not in db_mem:
        db_mem[chat_id] = {}
    await start_stream(
        message,
        raw_path,
        videoid,
        thumb,
        title,
        duration_min,
        duration_sec,
        mystic,
    )
