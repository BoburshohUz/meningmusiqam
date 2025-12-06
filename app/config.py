import os

BOT_TOKEN = "8420723410:AAGZp6cfo1HIp6ygL8oJqSxAm_VR2E6QSGo"

WEBHOOK_BASE = "https://web-production-9f4e7.up.railway.app"

WEBHOOK_PATH = f"/webhook/{BOT_TOKEN}"
WEBHOOK_URL = WEBHOOK_BASE + WEBHOOK_PATH

PORT = int(os.getenv("PORT", 8000))
