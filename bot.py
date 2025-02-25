import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
from config import TOKEN, CHAT_ID
from strings import COMMANDS
from commands import restart, shutdown, status, check_update, update_code, help_command, get_cpu_temp


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Komutları bağlama
dp.register_message_handler(restart, commands=['restart'])
dp.register_message_handler(shutdown, commands=['shutdown'])
dp.register_message_handler(status, commands=['status'])
dp.register_message_handler(check_update, commands=['check_update'])
dp.register_message_handler(update_code, commands=['update'])
dp.register_message_handler(help_command, commands=['help'])
dp.register_message_handler(get_cpu_temp, commands=['cpu_temp'])

async def on_startup(_):
    await bot.send_message(CHAT_ID, "🚀 Raspberry Pi açıldı ve bot çalışıyor! \n\n" + COMMANDS)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
