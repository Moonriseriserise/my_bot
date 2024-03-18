import os
import asyncio

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, or_f, StateFilter

from admin.hendler.hendler import admin_private_router
from client.henlder.hendler import client_private_router

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


ALLOW_UPDATE = ["message, edited_message"]


client_bot = Bot(token=os.getenv("CLIENTTOKEN"),)
admin_bot = Bot(token=os.getenv("ADMINTOKEN"),)

client_dp = Dispatcher()  # КЛИЕНТ
admin_dp = Dispatcher()  # АДМИН

client_dp.include_router(client_private_router)
admin_dp.include_router(admin_private_router)


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
