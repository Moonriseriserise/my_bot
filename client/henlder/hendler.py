from aiogram import types, Router
from aiogram.filters import CommandStart, Command, or_f, StateFilter

client_private_router = Router()


@client_private_router.message(CommandStart)
async def send_welcome(message: types.Message):
    print("Отработал клиент")

    await message.reply("Привет! Я клиент бот.")
