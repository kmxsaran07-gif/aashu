import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Bot Configuration
API_ID = os.environ.get("API_ID", "28674463")
API_HASH = os.environ.get("API_HASH", "04e625b25822b3a0f4730a98adedeba2")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8328688592:AAEw0rJzDz_A4o5CL76UQue1DmV0xJ6u4WY")
CHANNEL_ID = os.environ.get("CHANNEL_ID", "@Theprimevault01")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1003488998176"))

# MongoDB Configuration
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://sujalbot:sujalbot@cluster0.mnjoqfu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "wadi")
COLLECTION_NAME = os.environ.get("COLLECTION_NAME", "tests")
ADMIN_ID = os.environ.get("ADMIN_ID", "8327651421")

# Flask Configuration
FLASK_URLS = [
    os.environ.get("PRIMARY_URL", "http://localhost:5000"),
    os.environ.get("SECONDARY_URL", ""),  # Secondary URL from env
    os.environ.get("BACKUP_URL", "")  # Backup URL from env
]

# Remove empty URLs
FLASK_URLS = [url for url in FLASK_URLS if url]

# Feature Flags
USE_FLASK_APP = os.environ.get("USE_FLASK_APP", "True").lower() == "true"
FORCE_DIRECT_SEND = os.environ.get("FORCE_DIRECT_SEND", "False").lower() == "true"

# Messages 
WELCOME_MSG = """
ITsGOLU टेस्ट सीरीज बॉट में आपका स्वागत है। 🎯

मैं किसी भी APPX एप्लिकेशन से टेस्ट सीरीज निकाल सकता हूं।
बस मुझे ऐप का नाम या वेबसाइट URL भेजें।

𝙃𝙤𝙬 𝙩𝙤 𝙪𝙨𝙚:
1. ꜱᴇɴᴅ ᴀᴘᴘ ɴᴀᴍᴇ (ᴇ.ɢ. "parmaracademy")
2. ᴏʀ ꜱᴇɴᴅ ᴡᴇʙꜱɪᴛᴇ ᴜʀʟ / ᴀᴘɪ ᴜʀʟ
3. ꜱᴇʟᴇᴄᴛ ᴛᴇꜱᴛ ꜱᴇʀɪᴇꜱ
4. ɢᴇᴛ ʏᴏᴜʀ ᴛᴇꜱᴛ!
"""

FORCE_SUB_MSG = """
⚠️ कृपया हमारे चैनल से जुड़ें।

इस बॉट का उपयोग करने के लिए आपको हमारे चैनल से जुड़ना होगा।
शामिल होने के लिए नीचे दिए गए बटन पर क्लिक करें।

AFTER JOINING /start AGAIN

""" 























