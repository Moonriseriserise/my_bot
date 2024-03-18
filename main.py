import os
import asyncio

from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, or_f, StateFilter


load_dotenv(find_dotenv())

ALLOW_UPDATE = ["message, edited_message"]


client_bot = Bot(token=os.getenv("CLIENTTOKEN"),)
admin_bot = Bot(token=os.getenv("ADMINTOKEN"),)

dp = Dispatcher()


@dp.message(Command("admin"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я клиент бот.")


@dp.message(Command("admin"))
async def send_welcome(message: types.Message):
    await message.reply("Привет! Я админ бот.")


async def main():

    await dp.start_polling(client_bot, allowed_updates=ALLOW_UPDATE)
    await dp.start_polling(admin_bot, allowed_updates=ALLOW_UPDATE)


asyncio.run(main())
