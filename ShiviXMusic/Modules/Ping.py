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


__MODULE__ = "πΏπΈπ½πΆ"
__HELP__ = """

/ping or /alive
Β» π²π·π΄π²πΊ πΈπ΅ π±πΎπ πΈπ π°π»πΈππ΄ πΎπ π³π΄π°π³. [πΈπ΅ π°π»πΈππ΄ ππ·πΎππ ππΎπ ππ·π΄ πππππ΄πΌ πππ°ππ πΎπ΅ ππ·π΄ π±πΎππ ππ΄πππ΄π.]
"""


async def ShiviX_ping():
    uptime = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    ShiviX = f"""
β¨ ππΏππΈπΌπ΄ : {get_readable_time((uptime))}
β π²πΏπ : {cpu}%
β ππ°πΌ : {mem}%
π  π³πΈππΊ : {disk}%"""
    return ShiviX

@app.on_message(filters.command(["ping", "alive", f"ping@{BOT_USERNAME}"]))
async def ping(_, message):
    hmm = await message.reply_photo(
        photo=config.PING_IMG,
        caption="**Β» ππΏπΈπ½πΆπΈπ½πΆππ­...**",
    )
    hehe = await ShiviX_ping()
    start = datetime.now()
    end = datetime.now()
    resp = (end - start).microseconds / 1000
    await hmm.edit_text(
        f"**Β» ππΏπΎπ½πΆπ !**\n`β {resp}`πΌπ\n\n<b><u>{BOT_NAME} πππππ΄πΌ πππ°ππ :</u></b>{hehe}",
        reply_markup=ping_ig,
    )
