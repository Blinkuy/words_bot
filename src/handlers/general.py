from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, <b>{message.from_user.first_name}</b>!\n")


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("<b>Доступные команды:</b>\n/start — начать\n/help — помощь")
