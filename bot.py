import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import TOKEN, CHAT_ID
from commands import restart, shutdown, status


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Komutları bağlama
dp.register_message_handler(restart, commands=['restart'])
dp.register_message_handler(shutdown, commands=['shutdown'])
dp.register_message_handler(status, commands=['status'])

async def on_startup(_):
    await bot.send_message(CHAT_ID, "🚀 Raspberry Pi açıldı ve bot çalışıyor!")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
