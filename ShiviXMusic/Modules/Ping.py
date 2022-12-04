import os
import time
import config
from datetime import datetime

import psutil
from pyrogram import filters
from pyrogram.types import Message

from ShiviXMusic.Helpers.Inline import ping_ig
from ShiviXMusic.Helpers.Ping import get_readable_time
from ShiviXMusic import BOT_USERNAME, BOT_NAME, app, StartTime


__MODULE__ = "𝙿𝙸𝙽𝙶"
__HELP__ = """

/ping or /alive
» 𝙲𝙷𝙴𝙲𝙺 𝙸𝙵 𝙱𝙾𝚃 𝙸𝚂 𝙰𝙻𝙸𝚅𝙴 𝙾𝚁 𝙳𝙴𝙰𝙳. [𝙸𝙵 𝙰𝙻𝙸𝚅𝙴 𝚂𝙷𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙷𝙴 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚂 𝙾𝙵 𝚃𝙷𝙴 𝙱𝙾𝚃𝚂 𝚂𝙴𝚁𝚅𝙴𝚁.]
"""


async def ShiviX_ping():
    uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    ShiviX = f"""
✨ 𝚄𝙿𝚃𝙸𝙼𝙴 : {get_readable_time((uptime))}
☁ 𝙲𝙿𝚄 : {cpu}%
❄ 𝚁𝙰𝙼 : {mem}%
💠 𝙳𝙸𝚂𝙺 : {disk}%"""
    return ShiviX

@app.on_message(filters.command(["ping", "alive", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG,
        caption="**» 🔎𝙿𝙸𝙽𝙶𝙸𝙽𝙶🔍🍭...**",
    )
    hehe = await ShiviX_ping()
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await hmm.edit_text(
        f"**» 🔎𝙿𝙾𝙽𝙶🔍 !**\n`☁ {resp}`𝙼𝚂\n\n<b><u>{BOT_NAME} 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚂 :</u></b>{hehe}",
        reply_markup=ping_ig,
    )
