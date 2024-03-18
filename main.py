import os
import asyncio

from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, or_f, StateFilter


load_dotenv(find_dotenv())

ALLOW_UPDATE = ["message, edited_message"]


client_bot = Bot(token=os.getenv("CLIENTTOKEN"),)
admin_bot = Bot(token=os.getenv("ADMINTOKEN"),)

client_dp = Dispatcher()  # КЛИЕНТ
admin_dp = Dispatcher()  # АДМИН


@client_dp.message(Command("start"))
async def send_welcome(message: types.Message):
    print("Отработал клиент")

    await message.reply("Привет! Я клиент бот.")


@admin_dp.message(Command("start"))
async def send_welcome(message: types.Message):
    print("Отработал админ")

    await message.reply("Привет! Я админ бот.")


async def client():
    await client_bot.delete_webhook(drop_pending_updates=True)
    await client_dp.start_polling(client_bot, allowed_updates=ALLOW_UPDATE)
    #   await admin_dp.start_polling(admin_bot, allowed_updates=ALLOW_UPDATE)


async def admin():
    await admin_bot.delete_webhook(drop_pending_updates=True)
    await admin_dp.start_polling(admin_bot, allowed_updates=ALLOW_UPDATE)


async def main():
    task_client = asyncio.create_task(client())
    task_admin = asyncio.create_task(admin())

    await asyncio.gather(task_client, task_admin)


asyncio.run(main())
