import os

from dotenv import load_dotenv

load_dotenv()

BASE_API_URL = "http://127.0.0.1:8000/"

BOT_TOKEN = os.getenv("BOT_TOKEN")
