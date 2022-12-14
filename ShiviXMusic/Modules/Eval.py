import os
import re
import subprocess
import sys
import traceback
from inspect import getfullargspec
from io import StringIO
from time import time

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)

from ShiviXMusic import app, SUDO_USERS


__MODULE__ = "π±ππΎπ°π³π²π°ππ"
__HELP__ = """

**π½πΎππ΄ :**
πΎπ½π»π π΅πΎπ πππ³πΎπ΄ππ


/broadcast [πΌπ΄πππ°πΆπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄]
Β» πΌπ΄πππ°πΆπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄.

/broadcast_pin [πΌπ΄πππ°πΆπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆ]
Β» πΌπ΄πππ°πΆπ΄ πΎπ ππ΄πΏπ»π ππΎ π° πΌπ΄πππ°πΆπ΄ π°π½π³ πΏπΈπ½π ππ·π΄ π±ππΎπ°π³π²π°ππ πΌπ΄πππ°πΆπ΄.
"""


async def aexec(code, client, message):
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {a}" for a in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)


async def edit_or_reply(msg: Message, **kwargs):
    func = msg.edit_text if msg.from_user.is_self else msg.reply
    spec = getfullargspec(func.__wrapped__).args
    await func(**{k: v for k, v in kwargs.items() if k in spec})


@app.on_message(
    filters.command("eval")
    & ~filters.forwarded
    & ~filters.via_bot
    & filters.user(SUDO_USERS)
)
async def executor(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**ππ·π°π ππΎπ ππ°π½π½π° π΄ππ΄π²πππ΄ ?**"
        )
    try:
        cmd = message.text.split(" ", maxsplit=1)[1]
    except IndexError:
        return await message.delete()
    t1 = time()
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    redirected_error = sys.stderr = StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(cmd, client, message)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "πππ²π²π΄ππ"
    final_output = f"**πΎπππΏππ**:\n```{evaluation.strip()}```"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="β³",
                        callback_data=f"runtime {t2-t1} Seconds",
                    )
                ]
            ]
        )
        await message.reply_document(
            document=filename,
            caption=f"**πΈπ½πΏππ:**\n`{cmd[0:980]}`\n\n**πΎπππΏππ:**\n`π°πππ°π²π·π΄π³ π³πΎπ²ππΌπ΄π½π`",
            quote=False,
            reply_markup=keyboard,
        )
        await message.delete()
        os.remove(filename)
    else:
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="β³",
                        callback_data=f"runtime {round(t2-t1, 3)} Seconds",
                    ),
                    InlineKeyboardButton(
                        text="π",
                        callback_data=f"forceclose abc|{message.from_user.id}",
                    ),
                ]
            ]
        )
        await edit_or_reply(
            message, text=final_output, reply_markup=keyboard
        )


@app.on_callback_query(filters.regex(r"runtime"))
async def runtime_func_cq(_, cq):
    runtime = cq.data.split(None, 1)[1]
    await cq.answer(runtime, show_alert=True)


@app.on_callback_query(filters.regex("forceclose"))
async def forceclose_command(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    query, user_id = callback_request.split("|")
    if CallbackQuery.from_user.id != int(user_id):
        try:
            return await CallbackQuery.answer(
                "Β» πΈπ ππΈπ»π» π±π΄ π±π΄πππ΄π πΈπ΅ ππΎπ πππ°π πΈπ½ ππΎππ π»πΈπΌπΈπ.", show_alert=True
            )
        except:
            return
    await CallbackQuery.message.delete()
    try:
        await CallbackQuery.answer()
    except:
        return


@app.on_message(
    filters.command("sh")
    & ~filters.forwarded
    & ~filters.via_bot
    & filters.user(SUDO_USERS)
)
async def shellrunner(client, message):
    if len(message.command) < 2:
        return await edit_or_reply(
            message, text="**π΄ππ°πΌπΏπ»π΄ :**\n/sh git pull"
        )
    text = message.text.split(None, 1)[1]
    if "\n" in text:
        code = text.split("\n")
        output = ""
        for x in code:
            shell = re.split(
                """ (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", x
            )
            try:
                process = subprocess.Popen(
                    shell,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except Exception as err:
                print(err)
                await edit_or_reply(
                    message, text=f"**π΄πππΎπ:**\n```{err}```"
                )
            output += f"**{code}**\n"
            output += process.stdout.read()[:-1].decode("utf-8")
            output += "\n"
    else:
        shell = re.split(""" (?=(?:[^'"]|'[^']*'|"[^"]*")*$)""", text)
        for a in range(len(shell)):
            shell[a] = shell[a].replace('"', "")
        try:
            process = subprocess.Popen(
                shell,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except Exception as err:
            print(err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            errors = traceback.format_exception(
                etype=exc_type,
                value=exc_obj,
                tb=exc_tb,
            )
            return await edit_or_reply(
                message, text=f"**π΄πππΎπ:**\n```{''.join(errors)}```"
            )
        output = process.stdout.read()[:-1].decode("utf-8")
    if str(output) == "\n":
        output = None
    if output:
        if len(output) > 4096:
            with open("output.txt", "w+") as file:
                file.write(output)
            await client.send_document(
                message.chat.id,
                "output.txt",
                reply_to_message_id=message.message_id,
                caption="`πΎπππΏππ`",
            )
            return os.remove("output.txt")
        await edit_or_reply(
            message, text=f"**πΎπππΏππ:**\n```{output}```"
        )
    else:
        await edit_or_reply(message, text="**πΎπππΏππ: **\n`π½πΎ πΎπππΏππ`")

