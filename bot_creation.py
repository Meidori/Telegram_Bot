from aiogram import Bot, Dispatcher, types
import os

TOKEN = ""
# APP_URL = f'https://meidori.herokuapp.com/{TOKEN}'

client = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(client)