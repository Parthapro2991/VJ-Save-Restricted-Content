import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21554596"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "4f39dcf27f54338bfe30abc9f42853cf")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://parthapro2991:gZhzNuFOJ3X6Yscz@cluster0.d6hnq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
