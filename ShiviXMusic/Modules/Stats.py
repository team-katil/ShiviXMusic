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


__MODULE__ = "πππ°ππ"
__HELP__ = """

/stats
Β» ππ·πΎππ ππ·π΄ πππππ΄πΌ, π°πππΈπππ°π½π, πΌπΎπ½πΆπΎ π°π½π³ πππΎππ°πΆπ΄ πππ°ππ πΎπ΅ ππ·π΄ π±πΎπ.
"""


@app.on_message(filters.command(["stats", "gstats"]) & ~filters.edited)
async def gstats(_, message):
    try:
        await message.delete()
    except:
        pass
    hehe = await message.reply_photo(
        photo="ShiviXMusic/Utilities/Stats.jpeg", caption=f"**Β» πΏπ»π΄π°ππ΄ ππ°πΈπ...\n\nβ’ πΆπ΄πππΈπ½πΆ {BOT_NAME} πππ°ππ...**"
    )
    smex = f"""
**π²π·πΎπΎππ΄ π°π½ πΎπΏππΈπΎπ½ π΅πΎπ πΆπ΄πππΈπ½πΆ {BOT_NAME} πΆπ΄π½π΄ππ°π» πππ°ππ πΎπ π°πππΈπππ°π½π πππ°ππ πΎπ πΎππ΄ππ°π»π» πππ°ππ.**
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
        await CallbackQuery.answer("πΆπ΄πππΈπ½πΆ πππππ΄πΌ πππ°ππ...")
        mod = len(ALL_MODULES)
        sc = platform.system()
        arch = platform.machine()
        p_core = psutil.cpu_count(logical=False)
        t_core = psutil.cpu_count(logical=True)
        ram = (
            str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " πΆπ±"
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
β» <u>**{BOT_NAME} πππππ΄πΌ πππ°ππ :**</u>

β’ **ππΏππΈπΌπ΄ :** {uptime}
β’ **πΌπΎπ³ππ»π΄π :** {mod}
β’ **πΏπ»π°ππ΅πΎππΌ :** {sc}
β’ **π°ππ²π·πΈππ΄π²ππππ΄:** {arch}
β’ **πΏπ·πππΈπ²π°π» π²πΎππ΄π :** {p_core}
β’ **ππΎππ°π» π²πΎππ΄π :** {t_core}
β’ **ππ°πΌ :** {ram}
β’ **πΏπππ·πΎπ½ :** v{pyver.split()[0]}
β’ **πΏπππΎπΆππ°πΌ :** v{pyrover}


β» <u>**{BOT_NAME} πππΎππ°πΆπ΄ πππ°ππ :**</u>

β’ **ππΎππ°π» :** {total[:4]} πΆπΈπ±
β’ **πππ΄π³ :** {used[:4]} πΆπΈπ±
β’ **π΅ππ΄π΄ :** {free[:4]} πΆπΈπ±
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "bot_stats":
        await CallbackQuery.answer("πΆπ΄πππΈπ½πΆ π±πΎπ π°π½π³ π°πππΈπππ°π½πΆ πππ°ππ...")
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
β» <u>**{BOT_NAME} πΆπ΄π½π΄ππ°π» πππ°ππ :**</u>

β’ **πΌπΎπ³ππ»π΄π :** {mod}
β’ **πΆπ±π°π½π½π΄π³ :** {blocked}
β’ **πππ³πΎπ΄ππ :** {sudoers}
β’ **π²π·π°ππ :** {served_chats}
β’ **πππ΄ππ :** {served_users}

β» <u>**{BOT_NAME} π°πππΈπππ°π½πΆ πππ°ππ :**</u>

β’ **ππΎππ°π» :** {total_ub}
β’ **πΆππΎππΏπ :** {groups_ub}
β’ **π²π·π°π½π½π΄π»π :** {channels_ub}
β’ **π±πΎππ :** {bots_ub}
β’ **πππ΄ππ :** {privates_ub}
"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "mongo_stats":
        await CallbackQuery.answer(
            "πΆπ΄πππΈπ½π· πΌπΎπ½πΆπΎπ³π± πππ°ππ..."
        )
        try:
            pymongo = MongoClient(MONGO_DB_URI)
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("**π΅π°πΈπ»π΄π³ ππΎ πΆπ΄π πΌπΎπ½πΆπΎπ³π± πππ°ππ...**", reply_markup=stats_b)
        try:
            db = pymongo.ShiviX
        except Exception as e:
            print(e)
            return await CallbackQuery.edit_message_text("**π΅π°πΈπ»π΄π³ ππΎ πΆπ΄π πΌπΎπ½πΆπΎπ³π± πππ°ππ...**", reply_markup=stats_b)
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
β» <u>**{BOT_NAME} πΌπΎπ½πΆπΎπ³π± πππ°ππ :**</u>

**ππΏππΈπΌπ΄ :** {mongouptime[:4]} π³π°ππ
**ππ΄πππΈπΎπ½ :** {mver}
**π³π°ππ°π±π°ππ΄ :** {database}
**πΏππΎππΈπ³π΄π :** {provider}
**π³π± ππΈππ΄ :** {datasize[:6]} πΌπ±
**π³π± πππΎππ°πΆπ΄ :** {storage} πΌπ±
**π²πΎπ»π»π΄π²ππΈπΎπ½π :** {collections}
**πΊπ΄ππ :** {objects}
**πππ΄ππΈπ΄π :** `{query}`"""
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_b)
    if command == "get_back":
        smex = f"**π²π·πΎπΎππ΄ π°π½ πΎπΏππΈπΎπ½ π΅πΎπ πΆπ΄πππΈπ½πΆ {BOT_NAME} πΆπ΄π½π΄ππ°π» πππ°ππ πΎπ π°πππΈπππ°π½π πππ°ππ πΎπ πΎππ΄ππ°π»π» πππ°ππ.**"
        await CallbackQuery.edit_message_text(smex, reply_markup=stats_f)
