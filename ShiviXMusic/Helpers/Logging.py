import config
from .Clients import app, Ass

failure = "𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚈𝙾𝚄𝚁 𝙱𝙾𝚃 𝙸𝚂 𝙸𝙽 𝚈𝙾𝚄𝚁 𝙻𝙾𝙶 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙰𝙽𝙳 𝙸𝚂 𝙿𝚁𝙾𝙼𝙾𝚃𝙴𝙳 𝙰𝚂 𝙰𝙽 𝙰𝙳𝙼𝙸𝙽 𝚆𝙸𝚃𝙷 𝙵𝚄𝙻𝙻 𝚁𝙸𝙶𝙷𝚃𝚂 !"


async def startup_msg(_message_):
    try:
        ShiviXwtf = await app.send_message(
            config.LOGGER_ID, f"{_message_}"
        )
        return ShiviXwtf
    except:
        print(failure)
        return


async def startup_edit(_message_id, _message_):
    try:
        ShiviXwtf = await app.edit_message_text(
            config.LOGGER_ID, _message_id.message_id, f"{_message_}"
        )
        return ShiviXwtf
    except:
        ShiviXwtf = await startup_send_new(_message_)
        return ShiviXwtf


async def startup_del(_message_id):
    try:
        await app.delete_messages(config.LOGGER_ID, _message_id.message_id)
        return bool(1)
    except:
        pass
