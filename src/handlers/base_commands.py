from aiogram import F, Router

from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет! Я базовый aiogram-бот.")
    await message.reply("Как дела")


@router.message(Command("help"))
async def start_handler(message: Message):
    await message.answer("Вы нажали на кнопку помощи")
