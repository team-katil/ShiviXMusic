import asyncio
import speedtest

from pyrogram import filters
from ShiviXMusic import app, SUDO_USERS


__MODULE__ = "𝚂𝙿𝙴𝙴𝙳𝚃𝙴𝚂𝚃"
__HELP__ = """

/speedtest 
» 𝙲𝙷𝙴𝙲𝙺𝙴𝚁 𝚂𝙴𝚁𝚅𝙴𝚁 𝚂𝙿𝙴𝙴𝙳 𝙰𝙽𝙳 𝙻𝙰𝚃𝙴𝙽𝙲𝚈 𝙰𝙽𝙵 𝙿𝙸𝙽𝙶.

"""


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**⇆ 𝚁𝚄𝙽𝙽𝙸𝙽𝙶 𝙳𝙾𝚆𝙽𝙻𝙾𝙰𝙳 𝚂𝙿𝙴𝙴𝙳𝚃𝙴𝚂𝚃...**")
        test.download()
        m = m.edit("**⇆ 𝚁𝚄𝙽𝙽𝙸𝙽𝙶 𝚄𝙿𝙻𝙾𝙰𝙳 𝚂𝙿𝙴𝙴𝙳𝚃𝙴𝚂𝚃...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**↻ 𝚂𝙷𝙰𝚁𝙸𝙽𝙶 𝚂𝙿𝙴𝙴𝙳𝚃𝙴𝚂𝚃 𝚁𝙴𝚂𝚄𝙻𝚃𝚂...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "sptest", "spt"]) & filters.user(SUDO_USERS))
async def speedtest_function(client, message):
    m = await message.reply_text("**» 𝚁𝚄𝙽𝙽𝙸𝙽𝙶 𝚂𝙾𝙴𝙴𝙳𝚃𝙴𝚂𝚃...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""✯ **𝚂𝙿𝙴𝙴𝙳𝚃𝙴𝚂𝚃 𝚁𝙴𝚂𝚄𝙻𝚃𝚂** ✯
    
<u>**❥͜͡𝙲𝙻𝙸𝙴𝙽𝚃 :**</u>
**» __𝙸𝚂𝙿 :__** {result['client']['isp']}
**» __𝙲𝙾𝚄𝙽𝚃𝚁𝚈 :__** {result['client']['country']}
  
<u>**❥͜͡𝚂𝙴𝚁𝚅𝙴𝚁 :**</u>
**» __𝙽𝙰𝙼𝙴 :__** {result['server']['name']}
**» __𝙲𝙾𝚄𝙽𝚃𝚁𝚈 :__** {result['server']['country']}, {result['server']['cc']}
**» __𝚂𝙿𝙾𝙽𝚂𝙴𝚁 :__** {result['server']['sponsor']}
**» __𝙻𝙰𝚃𝙴𝙽𝙲𝚈 :__** {result['server']['latency']}  
**» __𝙿𝙸𝙽𝙶 :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
