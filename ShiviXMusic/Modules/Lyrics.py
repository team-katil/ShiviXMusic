import re
import os

import lyricsgenius
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from ShiviXMusic import BOT_NAME, app


__MODULE__ = "𝙻𝚈𝚁𝙸𝙲𝚂"
__HELP__ = """

/lyrics [𝙼𝚄𝚂𝙸𝙲 𝙽𝙰𝙼𝙴]
» 𝚂𝙷𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙷𝙴 𝙻𝚈𝚁𝙸𝙲𝚂 𝙾𝙵 𝚃𝙷𝙴 𝚂𝙴𝙰𝚁𝙲𝙷𝙴𝙳 𝚂𝙾𝙽𝙶.
"""


@app.on_message(filters.command(["lyrics", "lyric"]))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**𝙴𝚇𝙰𝙼𝙿𝙻𝙴 :**\n\n/lyrics [𝙼𝚄𝚂𝙸𝙲 𝙽𝙰𝙼𝙴]")
    m = await message.reply_text("**» 𝚂𝙴𝙰𝚁𝙲𝙷𝙸𝙽𝙶 𝙻𝚈𝚁𝙸𝙲𝚂...**")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("**» 𝙻𝚈𝚁𝙸𝙲𝚂 𝙽𝙾𝚃 𝙵𝙾𝚄𝙽𝙳 𝙵𝙾𝚁 𝚃𝙷𝙸𝚂 𝚂𝙾𝙽𝙶.**")
    xxx = f"""
**𝙻𝚈𝚁𝙸𝙲𝚂 𝙿𝙾𝚆𝙴𝚁𝙴𝙳 𝙱𝚈 {BOT_NAME}**

**𝚂𝙴𝙰𝚁𝙲𝙷𝙴𝙳 :-** __{query}__
**𝚃𝙸𝚃𝙻𝙴 :-** __{S.title}__
**𝙰𝚁𝚃𝙸𝚂𝚃 :-** {S.artist}

**𝙻𝚈𝚁𝙸𝙲𝚂 :**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**𝙾𝚄𝚃𝙿𝚄𝚃:**\n\n`𝙻𝚈𝚁𝙸𝙲𝚂`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)

