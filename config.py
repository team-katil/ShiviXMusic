from os import getenv
from dotenv import load_dotenv

load_dotenv()

get_queue = {}


API_ID = int(getenv("API_ID", "11660229")) 
API_HASH = getenv("API_HASH", "b89dc605daa9a5e957559402cc19856b")
ASS_HANDLER = list(getenv("ASS_HANDLER", ".").split())
BOT_TOKEN = getenv("BOT_TOKEN", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "500"))
LOGGER_ID = int(getenv("LOGGER_ID", "-1001750682671"))
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "5301800943").split()))
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1c309582720212c9af07a.jpg")
START_IMG = getenv("START_IMG","https://telegra.ph/file/1949364cf73fb7223f6fb.jpg")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/katilsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/katil_bots")
STRING_SESSION = getenv("STRING_SESSION", "")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5301800943").split()))
GIT_TOKEN = getenv("GIT_TOKEN", "")
