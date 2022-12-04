from ShiviXMusic import app, OWNER_ID
from pyrogram import Client, filters
from pyrogram.types import Message
from ShiviXMusic.Helpers.Database import get_served_chats


@app.on_message(filters.command(["chats", "chatlist", "groups"]) & filters.user(OWNER_ID))
async def list_chats(_, message: Message):
    served_chats = []
    text = "🤯 **𝙻𝙸𝚂𝚃 𝙾𝙵 𝙼𝚄𝚂𝙸𝙲 𝙲𝙷𝙰𝚃𝚂 𝙸𝙽 𝚆𝙷𝙸𝙲𝙷 𝙱𝙾𝚃 𝚄𝚂 𝙿𝚁𝙴𝚂𝙴𝙽𝚃 :**\n\n"
    try:
        chats = await get_served_chats()
        for chat in chats:
            served_chats.append(int(chat["chat_id"]))
    except Exception as e:
        await message.reply_text(f"𝙴𝚁𝚁𝙾𝚁 : `{e}`")
        return
    count = 0
    for served_chat in served_chats:
        try:
            title = (await app.get_chat(served_chat)).title
        except Exception:
            title = "• 𝙿𝚁𝙸𝚅𝙰𝚃𝙴 𝙲𝙷𝙰𝚃"
        count += 1
        text += f"**• {count}. {title}** [`{served_chat}`]\n"
    if not text:
        await message.reply_text("**» 𝙽𝙾 𝙲𝙷𝙰𝚃𝚂 𝙵𝙾𝚄𝙽𝙳 𝙸𝙽 𝙱𝙾𝚃𝚂 𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴.**")  
    else:
        await message.reply_text(text) 

