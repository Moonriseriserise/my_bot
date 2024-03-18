from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f, StateFilter

admin_private_router = Router()


@admin_private_router.message(CommandStart)
async def send_welcome(message: types.Message):

    await message.reply("Привет! Я админ бот.")
