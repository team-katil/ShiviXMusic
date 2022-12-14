from ShiviXMusic import app, OWNER_ID
from pyrogram import Client, filters
from pyrogram.types import Message
from ShiviXMusic.Helpers.Database import get_served_chats


@app.on_message(filters.command(["chats", "chatlist", "groups"]) & filters.user(OWNER_ID))
async def list_chats(_, message: Message):
    served_chats = []
    text = "π€― **π»πΈππ πΎπ΅ πΌπππΈπ² π²π·π°ππ πΈπ½ ππ·πΈπ²π· π±πΎπ ππ πΏππ΄ππ΄π½π :**\n\n"
    try:
        chats = await get_served_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"π΄πππΎπ : `{e}`")
        return
    count = 0
    for served_chat in served_chats:
        try:
            title = (await app.get_chat(served_chat)).title
        except Exception:
            title = "β’ πΏππΈππ°ππ΄ π²π·π°π"
        count += 1
        text += f"**β’ {count}. {title}** [`{served_chat}`]\n"
    if not text:
        await message.reply_text("**Β» π½πΎ π²π·π°ππ π΅πΎππ½π³ πΈπ½ π±πΎππ π³π°ππ°π±π°ππ΄.**")  
    else:
        await message.reply_text(text) 

