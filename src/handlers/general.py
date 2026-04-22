from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from src.services.user import UserService
from src.database import get_session

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    async with get_session() as session:
        user_service = UserService(session=session)

        user, is_new = await user_service.register_user(message.from_user.id)

    if is_new:
        await message.answer(
            f"👋 Привет, <b>{message.from_user.first_name}</b>!\n"
            "Рад видеть тебя впервые — добро пожаловать 🎉"
        )
    else:
        await message.answer(
            f"С возвращением, <b>{message.from_user.first_name}</b>! 👀\n"
            "Давно не виделись — проходи скорее 🚀"
        )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("<b>Доступные команды:</b>\n/start — начать\n/help — помощь")
