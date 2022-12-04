import os
import re
import json
import uuid
import time
import psutil
import socket
import logging
import asyncio
import platform

from datetime import datetime
from sys import version as pyver
from pymongo import MongoClient

from pyrogram import Client, filters
from pyrogram import __version__ as pyrover
from pyrogram.types import Message
from ShiviXMusic import (BOT_NAME, SUDO_USERS, app, Ass, StartTime, MONGO_DB_URI)
from ShiviXMusic.Helpers.Database import get_gbans_count, get_served_chats, get_served_users
from ShiviXMusic.Helpers.Inline import stats_f, stats_b
from ShiviXMusic.Modules import ALL_MODULES
from ShiviXMusic.Helpers.Ping import get_readable_time


__MODULE__ = "𝚂𝚃𝙰𝚃𝚂"
__HELP__ = """

/stats
» 𝚂𝙷𝙾𝚆𝚂 𝚃𝙷𝙴 𝚂𝚈𝚂𝚃𝙴𝙼, 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃, 𝙼𝙾𝙽𝙶𝙾 𝙰𝙽𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝚂𝚃𝙰𝚃𝚂 𝙾𝙵 𝚃𝙷𝙴 𝙱𝙾𝚃.
"""


@app.on_message(filters.command(["stats", "gstats"]) & ~filters.edited)
async def gstats(_, message):
    try:
        await message.delete()
    except:
        pass
    hehe = await message.reply_photo(
        photo="ShiviXMusic/Utilities/Stats.jpeg", caption=f"**» 𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...\n\n• 𝙶𝙴𝚃𝚃𝙸𝙽𝙶 {BOT_NAME} 𝚂𝚃𝙰𝚃𝚂...**"
    )
    smex = f"""
**𝙲𝙷𝙾𝙾𝚂𝙴 𝙰𝙽 𝙾𝙿𝚃𝙸𝙾𝙽 𝙵𝙾𝚁 𝙶𝙴𝚃𝚃𝙸𝙽𝙶 {BOT_NAME} 𝙶𝙴𝙽𝙴𝚁𝙰𝙻 𝚂𝚃𝙰𝚃𝚂 𝙾𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚂𝚃𝙰𝚃𝚂 𝙾𝚁 𝙾𝚅𝙴𝚁𝙰𝙻𝙻 𝚂𝚃𝙰𝚃𝚂.**
    """
    await hehe.edit_text(smex, reply_markup=stats_f)
    return


@app.on_callback_query(
    filters.regex(
        pattern=r"^(sys_stats|bot_stats|get_back|mongo_stats|wait_stats)$"
    )
)
async def stats_markup(_, CallbackQuery):
    command = CallbackQuery.matches[0].group(1)
    if command == "sys_stats":
        await CallbackQuery.answer("𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚂...")
        mod = len(ALL_MODULES)
        sc = platform.system()
        arch = platform.machine()
        p_core = psutil.cpu_count(logical=False)
        t_core = psutil.cpu_count(logical=True)
        ram = (
            str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " 𝙶𝙱"
        )
        hdd = psutil.disk_usage("/")
        total = hdd.total / (1024.0 ** 3)
        total = str(total)
        used = hdd.used / (1024.0 ** 3)
        used = str(used)
        free = hdd.free / (1024.0 ** 3)
        free = str(free)
        bot_uptime = int(time.time() - StartTime)
        uptime = f"{get_readable_time((bot_uptime))}"
        smex = f"""
➻ <u>**{BOT_NAME} 𝚂𝚈𝚂𝚃𝙴𝙼 𝚂𝚃𝙰𝚃𝚂 :**</u>

• **𝚄𝙿𝚃𝙸𝙼𝙴 :** {uptime}
• **𝙼𝙾𝙳𝚄𝙻𝙴𝚂 :** {mod}
• **𝙿𝙻𝙰𝚃𝙵𝙾𝚁𝙼 :** {sc}
• **𝙰𝚁𝙲𝙷𝙸𝚃𝙴𝙲𝚃𝚄𝚁𝙴:** {arch}
• **𝙿𝙷𝚈𝚂𝙸𝙲𝙰𝙻 𝙲𝙾𝚁𝙴𝚂 :** {p_core}
• **𝚃𝙾𝚃𝙰𝙻 𝙲𝙾𝚁𝙴𝚂 :** {t_core}
• **𝚁𝙰𝙼 :** {ram}
• **𝙿𝚈𝚃𝙷𝙾𝙽 :** v{pyver.split()[0]}
• **𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼 :** v{pyrover}


➻ <u>**{BOT_NAME} 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 𝚂𝚃𝙰𝚃𝚂 :**</u>

• **𝚃𝙾𝚃𝙰𝙻 :** {total[:4]} 𝙶𝙸𝙱
• **𝚄𝚂𝙴𝙳 :** {used[:4]} 𝙶𝙸𝙱
• **𝙵𝚁𝙴𝙴 :** {free[:4]} 𝙶𝙸𝙱
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "bot_stats":
        await CallbackQuery.answer("𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝙱𝙾𝚃 𝙰𝙽𝙳 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝙶 𝚂𝚃𝙰𝚃𝚂...")
        groups_ub = channels_ub = bots_ub = privates_ub = total_ub = 0
        async for i in Ass.iter_dialogs():
            t = i.chat.type
            total_ub += 1
            if t in ["supergroup", "group"]:
                groups_ub += 1
            elif t == "channel":
                channels_ub += 1
            elif t == "bot":
                bots_ub += 1
            elif t == "private":
                privates_ub += 1

        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        blocked = await get_gbans_count()
        sudoers = len(SUDO_USERS)
        mod = len(ALL_MODULES)
        smex = f"""
➻ <u>**{BOT_NAME} 𝙶𝙴𝙽𝙴𝚁𝙰𝙻 𝚂𝚃𝙰𝚃𝚂 :**</u>

• **𝙼𝙾𝙳𝚄𝙻𝙴𝚂 :** {mod}
• **𝙶𝙱𝙰𝙽𝙽𝙴𝙳 :** {blocked}
• **𝚂𝚄𝙳𝙾𝙴𝚁𝚂 :** {sudoers}
• **𝙲𝙷𝙰𝚃𝚂 :** {served_chats}
• **𝚄𝚂𝙴𝚁𝚂 :** {served_users}

➻ <u>**{BOT_NAME} 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝙶 𝚂𝚃𝙰𝚃𝚂 :**</u>

• **𝚃𝙾𝚃𝙰𝙻 :** {total_ub}
• **𝙶𝚁𝙾𝚄𝙿𝚂 :** {groups_ub}
• **𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂 :** {channels_ub}
• **𝙱𝙾𝚃𝚂 :** {bots_ub}
• **𝚄𝚂𝙴𝚁𝚂 :** {privates_ub}
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "mongo_stats":
        await CallbackQuery.answer(
            "𝙶𝙴𝚃𝚃𝙸𝙽𝙷 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 𝚂𝚃𝙰𝚃𝚂..."
        )
        try:
            pymongo = MongoClient(MONGO_DB_URI)
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("**𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝙶𝙴𝚃 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 𝚂𝚃𝙰𝚃𝚂...**", reply_markup=stats_b)
        try:
            db = pymongo.ShiviX
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("**𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝙶𝙴𝚃 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 𝚂𝚃𝙰𝚃𝚂...**", reply_markup=stats_b)
        call = db.command("dbstats")
        database = call["db"]
        datasize = call["dataSize"] / 1024
        datasize = str(datasize)
        storage = call["storageSize"] / 1024
        objects = call["objects"]
        collections = call["collections"]
        status = db.command("serverStatus")
        query = status["opcounters"]["query"]
        mver = status["version"]
        mongouptime = status["uptime"] / 86400
        mongouptime = str(mongouptime)
        provider = status["repl"]["tags"]["provider"]
        smex = f"""
➻ <u>**{BOT_NAME} 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 𝚂𝚃𝙰𝚃𝚂 :**</u>

**𝚄𝙿𝚃𝙸𝙼𝙴 :** {mongouptime[:4]} 𝙳𝙰𝚈𝚂
**𝚅𝙴𝚁𝚂𝙸𝙾𝙽 :** {mver}
**𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 :** {database}
**𝙿𝚁𝙾𝚅𝙸𝙳𝙴𝚁 :** {provider}
**𝙳𝙱 𝚂𝙸𝚉𝙴 :** {datasize[:6]} 𝙼𝙱
**𝙳𝙱 𝚂𝚃𝙾𝚁𝙰𝙶𝙴 :** {storage} 𝙼𝙱
**𝙲𝙾𝙻𝙻𝙴𝙲𝚃𝙸𝙾𝙽𝚂 :** {collections}
**𝙺𝙴𝚈𝚂 :** {objects}
**𝚀𝚄𝙴𝚁𝙸𝙴𝚂 :** `{query}`"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "get_back":
        smex = f"**𝙲𝙷𝙾𝙾𝚂𝙴 𝙰𝙽 𝙾𝙿𝚃𝙸𝙾𝙽 𝙵𝙾𝚁 𝙶𝙴𝚃𝚃𝙸𝙽𝙶 {BOT_NAME} 𝙶𝙴𝙽𝙴𝚁𝙰𝙻 𝚂𝚃𝙰𝚃𝚂 𝙾𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚈 𝚂𝚃𝙰𝚃𝚂 𝙾𝚁 𝙾𝚅𝙴𝚁𝙰𝙻𝙻 𝚂𝚃𝙰𝚃𝚂.**"
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_f)
