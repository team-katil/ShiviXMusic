import asyncio
import speedtest

from pyrogram import filters
from ShiviXMusic import app, SUDO_USERS


__MODULE__ = "ππΏπ΄π΄π³ππ΄ππ"
__HELP__ = """

/speedtest 
Β» π²π·π΄π²πΊπ΄π ππ΄πππ΄π ππΏπ΄π΄π³ π°π½π³ π»π°ππ΄π½π²π π°π½π΅ πΏπΈπ½πΆ.

"""


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("**β πππ½π½πΈπ½πΆ π³πΎππ½π»πΎπ°π³ ππΏπ΄π΄π³ππ΄ππ...**")
        test.download()
        m = m.edit("**β πππ½π½πΈπ½πΆ ππΏπ»πΎπ°π³ ππΏπ΄π΄π³ππ΄ππ...**")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("**β» ππ·π°ππΈπ½πΆ ππΏπ΄π΄π³ππ΄ππ ππ΄πππ»ππ...**")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(["speedtest", "sptest", "spt"]) & filters.user(SUDO_USERS))
async def speedtest_function(client, message):
    m = await message.reply_text("**Β» πππ½π½πΈπ½πΆ ππΎπ΄π΄π³ππ΄ππ...**")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""β― **ππΏπ΄π΄π³ππ΄ππ ππ΄πππ»ππ** β―
    
<u>**β₯ΝΝ‘π²π»πΈπ΄π½π :**</u>
**Β» __πΈππΏ :__** {result['client']['isp']}
**Β» __π²πΎππ½πππ :__** {result['client']['country']}
  
<u>**β₯ΝΝ‘ππ΄πππ΄π :**</u>
**Β» __π½π°πΌπ΄ :__** {result['server']['name']}
**Β» __π²πΎππ½πππ :__** {result['server']['country']}, {result['server']['cc']}
**Β» __ππΏπΎπ½ππ΄π :__** {result['server']['sponsor']}
**Β» __π»π°ππ΄π½π²π :__** {result['server']['latency']}  
**Β» __πΏπΈπ½πΆ :__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["share"], 
        caption=output
    )
    await m.delete()
