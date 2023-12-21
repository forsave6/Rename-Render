# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "25919081")

API_HASH = os.environ.get("API_HASH", "0bc2fdba14b16b44f0d89729ed8d2118")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6670958116:AAGqcbyH4ibtnXgOmzTKwqDhp3ZUfoV-UJk") 

FORCE_SUB = os.environ.get("FORCE_SUB", "vk_botz01") 

             # Don't Remove Credit @VJ_Botz
             # Subscribe YouTube Channel For Amazing Bot @Tech_VJ
             # Ask Doubt on telegram @KingVJ01

DB_NAME = os.environ.get("DB_NAME", "forsave6")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://forsave6:VIREndra123@forsave6.spdf0lo.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1826828317').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
