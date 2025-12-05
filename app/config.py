import os

# Bot token (you provided)
BOT_TOKEN = "8420723410:AAGZp6cfo1HIp6ygL8oJqSxAm_VR2E6QSGo"

# Railway domain must be provided in .env or Railway variables
WEBHOOK_BASE = os.getenv("WEBHOOK_BASE")

# Secure webhook secret (generated)
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "f3b9d8a1c7e24f209d8a3f5e9b1c7d4a")

# PORT provided by Railway at runtime
PORT = int(os.getenv("PORT", 8000))

if not WEBHOOK_BASE:
    raise RuntimeError("WEBHOOK_BASE .env yoki Railway Variables ichida ko‘rsatilmagan!")

WEBHOOK_PATH = f"/webhook/{WEBHOOK_SECRET}"
WEBHOOK_URL = WEBHOOK_BASE.rstrip("/") + WEBHOOK_PATH
