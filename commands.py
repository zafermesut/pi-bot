import os
from aiogram import types
from config import CHAT_ID

async def restart(message: types.Message):
    if message.from_user.id == CHAT_ID:
        await message.answer("📢 Cihaz yeniden başlatılıyor...")
        os.system("sudo reboot")

async def shutdown(message: types.Message):
    if message.from_user.id == CHAT_ID:
        await message.answer("⚠ Cihaz kapanıyor...")
        os.system("sudo shutdown now")

async def status(message: types.Message):
    await message.answer("✅ Raspberry Pi aktif ve çalışıyor!")
