from aiogram import Bot, Dispatcher, types
import os

TOKEN = "5092314407:AAGFlgQQbTYhL4cfXli6DpaN-He5jtxeRj0"
# APP_URL = f'https://meidori.herokuapp.com/{TOKEN}'

client = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dispatcher = Dispatcher(client)