import config
from .Clients import app, Ass

failure = "πΌπ°πΊπ΄ ππππ΄ ππΎππ π±πΎπ πΈπ πΈπ½ ππΎππ π»πΎπΆ π²π·π°π½π½π΄π» π°π½π³ πΈπ πΏππΎπΌπΎππ΄π³ π°π π°π½ π°π³πΌπΈπ½ ππΈππ· π΅ππ»π» ππΈπΆπ·ππ !"


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
