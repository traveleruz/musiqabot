# Telegram Bot — FastAPI + Aiogram 3 + Railway

## Local setup
1. Create virtualenv and activate it:
   python -m venv venv
   source venv/bin/activate  # linux/mac
   venv\Scripts\activate   # windows

2. Install requirements:
   pip install -r requirements.txt

3. Run locally (you must set WEBHOOK_BASE to a reachable URL, e.g. via ngrok):
   export WEBHOOK_BASE=https://your-ngrok-url
   export WEBHOOK_SECRET=f3b9d8a1c7e24f209d8a3f5e9b1c7d4a
   uvicorn app.main:app --reload

## Railway deploy
1. Push repository to GitHub.
2. Create new Railway project → Deploy from GitHub.
3. In Railway Project Settings → Variables add:
   - WEBHOOK_BASE = https://your-project.up.railway.app
   - WEBHOOK_SECRET = f3b9d8a1c7e24f209d8a3f5e9b1c7d4a
4. Deploy. After successful deploy, Telegram webhook will be set automatically by the app.
5. Test by sending /start to your bot.
