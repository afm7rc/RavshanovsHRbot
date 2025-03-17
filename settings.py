import os
from dotenv import load_dotenv

# .env faylini yuklash
load_dotenv()

# Bot token va MySQL sozlamalari
BOT_TOKEN = os.getenv("BOT_TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")