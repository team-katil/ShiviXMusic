import re
import os

import lyricsgenius
from pyrogram import filters
from pyrogram.types import Message
from youtubesearchpython import VideosSearch

from ShiviXMusic import BOT_NAME, app


__MODULE__ = "π»πππΈπ²π"
__HELP__ = """

/lyrics [πΌπππΈπ² π½π°πΌπ΄]
Β» ππ·πΎππ ππΎπ ππ·π΄ π»πππΈπ²π πΎπ΅ ππ·π΄ ππ΄π°ππ²π·π΄π³ ππΎπ½πΆ.
"""


@app.on_message(filters.command(["lyrics", "lyric"]))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**π΄ππ°πΌπΏπ»π΄ :**\n\n/lyrics [πΌπππΈπ² π½π°πΌπ΄]")
    m = await message.reply_text("**Β» ππ΄π°ππ²π·πΈπ½πΆ π»πππΈπ²π...**")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("**Β» π»πππΈπ²π π½πΎπ π΅πΎππ½π³ π΅πΎπ ππ·πΈπ ππΎπ½πΆ.**")
    xxx = f"""
**π»πππΈπ²π πΏπΎππ΄ππ΄π³ π±π {BOT_NAME}**

**ππ΄π°ππ²π·π΄π³ :-** __{query}__
**ππΈππ»π΄ :-** __{S.title}__
**π°πππΈππ :-** {S.artist}

**π»πππΈπ²π :**

{S.lyrics}"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**πΎπππΏππ:**\n\n`π»πππΈπ²π`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)

