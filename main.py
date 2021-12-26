from aiogram import executor
from bot_creation import dispatcher
from handlers import client


async def on_startup(_):
    print('Online')


client.register_handlers_client(dispatcher)


executor.start_polling(dispatcher, skip_updates=True, on_startup=on_startup)