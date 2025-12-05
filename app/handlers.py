from aiogram import Router, types
from aiogram.filters import Command
from aiogram import F

router = Router()

@router.message(Command("start"))
async def start_cmd(msg: types.Message):
    await msg.answer("🚀 Bot ishlayapti! FastAPI + Aiogram 3 + Railway")

@router.message(F.text)
async def echo(msg: types.Message):
    await msg.answer(f"Siz yozdingiz: {msg.text}")
