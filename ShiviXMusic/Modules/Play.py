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
            "**» 𝚈𝙾𝚄'𝚁𝙴 𝙰𝙽 𝙰𝙽𝙾𝙽𝚈𝙼𝙾𝚄𝚂 𝙰𝙳𝙼𝙸𝙽.\n\n𝚁𝙴𝚅𝙴𝚁𝚃 𝙱𝙰𝙲𝙺 𝚃𝙾 𝚄𝚂𝙴𝚁 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙵𝙾𝚁 𝚄𝚂𝙸𝙽𝙶 𝙼𝙴.**"
        )
    audio = (
        (message.reply_to_message.audio or message.reply_to_message.voice)
        if message.reply_to_message
        else None
    )
    url = get_url(message)
    if audio:
        mystic = await message.reply_text(
            "**↻ 𝙿𝚁𝙾𝙲𝙴𝚂𝚂𝙸𝙽𝙶...\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...**"
        )

        if audio.file_size > 314572800:
            return await mystic.edit_text(
                "**» 𝙰𝚄𝙳𝙸𝙾 𝙵𝙸𝙻𝙴 𝚂𝙸𝚉𝙴 𝚂𝙾𝚄𝙻𝙳 𝙱𝙴 𝙻𝙴𝚂𝚂 𝚃𝙷𝙰𝙽 300𝙼𝙱.**"
            )
        duration_min = seconds_to_min(audio.duration)
        duration_sec = audio.duration
        if (audio.duration) > DURATION_LIMIT_SEC:
            return await mystic.edit_text(
                f"**» {BOT_NAME} 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙰𝙻𝙻𝙾𝚆 𝚃𝙾𝙽𝙿𝙻𝙰𝚈 𝚃𝚁𝙰𝙲𝙺𝚂 𝙻𝙾𝙽𝙶𝙴𝚁 𝚃𝙷𝙰𝙽 {DURATION_LIMIT_MIN} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂.**"
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
        mystic = await message.reply_text("**↻ 𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙷...\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...**")
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
                f"**» {BOT_NAME} 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙰𝙻𝙻𝙾𝚆 𝚃𝙾𝙽𝙿𝙻𝙰𝚈 𝚃𝚁𝙰𝙲𝙺𝚂 𝙻𝙾𝙽𝙶𝙴𝚁 𝚃𝙷𝙰𝙽 {DURATION_LIMIT_MIN} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂.**"
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
                    "**➻ 𝚃𝙷𝙸𝚂 𝙸𝚂 𝙽𝙾𝚃 𝚃𝙷𝙴 𝙲𝙾𝚁𝚁𝙴𝙲𝚃 𝙵𝙾𝚁𝙼𝙰𝚃𝙴 𝚃𝙾 𝙿𝙻𝙰𝚈.**\n\n**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :** /play [𝚂𝙾𝙽𝙶 𝙽𝙰𝙼𝙴 𝙾𝚁 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙻𝙸𝙽𝙺 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙰𝚄𝙳𝙸𝙾]"
                ),
            )
            return
        mystic = await message.reply_text("**↻ 𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...**")
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
            f"**» {BOT_NAME} 𝙳𝙾𝙴𝚂𝙽'𝚃 𝙰𝙻𝙻𝙾𝚆 𝚃𝙾𝙽𝙿𝙻𝙰𝚈 𝚃𝚁𝙰𝙲𝙺𝚂 𝙻𝙾𝙽𝙶𝙴𝚁 𝚃𝙷𝙰𝙽 {DURATION_LIMIT_MIN} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂.**"
        )
    mystic = await message.reply_text(
        f"**{BOT_NAME} 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳𝙴𝚁**\n\n**𝚃𝙸𝚃𝙻𝙴 :** {title}\n\n0% ■■■■■■■■■■■■ 100%"
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
