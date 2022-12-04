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


__MODULE__ = "𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃"
__HELP__ = """

**𝙽𝙾𝚃𝙴 :**
𝙾𝙽𝙻𝚈 𝙵𝙾𝚁 𝚂𝚄𝙳𝙾𝙴𝚁𝚂


/broadcast [𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴]
» 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴.

/broadcast_pin [𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶]
» 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙾𝚁 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙰𝙽𝙳 𝙿𝙸𝙽𝚂 𝚃𝙷𝙴 𝙱𝚁𝙾𝙰𝙳𝙲𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴.
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
            message, text="**𝚆𝙷𝙰𝚃 𝚈𝙾𝚄 𝚆𝙰𝙽𝙽𝙰 𝙴𝚇𝙴𝙲𝚄𝚃𝙴 ?**"
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
        evaluation = "𝚂𝚄𝙲𝙲𝙴𝚂𝚂"
    final_output = f"**𝙾𝚄𝚃𝙿𝚄𝚃**:\n```{evaluation.strip()}```"
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(evaluation.strip()))
        t2 = time()
        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="⏳",
                        callback_data=f"runtime {t2-t1} Seconds",
                    )
                ]
            ]
        )
        await message.reply_document(
            document=filename,
            caption=f"**𝙸𝙽𝙿𝚄𝚃:**\n`{cmd[0:980]}`\n\n**𝙾𝚄𝚃𝙿𝚄𝚃:**\n`𝙰𝚃𝚃𝙰𝙲𝙷𝙴𝙳 𝙳𝙾𝙲𝚄𝙼𝙴𝙽𝚃`",
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
                        text="⏳",
                        callback_data=f"runtime {round(t2-t1, 3)} Seconds",
                    ),
                    InlineKeyboardButton(
                        text="🗑",
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
                "» 𝙸𝚃 𝚆𝙸𝙻𝙻 𝙱𝙴 𝙱𝙴𝚃𝚃𝙴𝚁 𝙸𝙵 𝚈𝙾𝚄 𝚂𝚃𝙰𝚈 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙻𝙸𝙼𝙸𝚃.", show_alert=True
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
            message, text="**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n/sh git pull"
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
                    message, text=f"**𝙴𝚁𝚁𝙾𝚁:**\n```{err}```"
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
                message, text=f"**𝙴𝚁𝚁𝙾𝚁:**\n```{''.join(errors)}```"
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
                caption="`𝙾𝚄𝚃𝙿𝚄𝚃`",
            )
            return os.remove("output.txt")
        await edit_or_reply(
            message, text=f"**𝙾𝚄𝚃𝙿𝚄𝚃:**\n```{output}```"
        )
    else:
        await edit_or_reply(message, text="**𝙾𝚄𝚃𝙿𝚄𝚃: **\n`𝙽𝙾 𝙾𝚄𝚃𝙿𝚄𝚃`")

