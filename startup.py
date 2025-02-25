import asyncio
from aiogram import Bot
from config import TOKEN, CHAT_ID, COMMANDS

async def send_startup_message():
    bot = Bot(token=TOKEN)
    await bot.send_message(CHAT_ID, "🚀 Raspberry Pi açıldı!\n\n" + COMMANDS)
    await bot.session.close()

if __name__ == "__main__":
    asyncio.run(send_startup_message())
