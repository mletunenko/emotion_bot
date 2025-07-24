from aiogram import Bot, Dispatcher
import asyncio
import os

from dotenv import load_dotenv
from handlers.base_commands import router


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
