from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from app.config import BOT_TOKEN, WEBHOOK_URL, WEBHOOK_PATH
from app.handlers import router

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
dp.include_router(router)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await bot.set_webhook(WEBHOOK_URL)
    print("Webhook o‘rnatildi:", WEBHOOK_URL)

@app.on_event("shutdown")
async def shutdown():
    await bot.delete_webhook()
    await bot.session.close()

@app.post(WEBHOOK_PATH)
async def telegram_webhook(request: Request):
    update = Update(**await request.json())
    await dp.feed_update(update)
    return {"ok": True}

@app.get("/")
async def root():
    return {"status": "running", "webhook": WEBHOOK_URL}
