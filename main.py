import telebot
from telebot import types
import random
from list1 import list1
from list2 import list2
import os
from flask import Flask, request

BOT_TOKEN = os.environ['TOKEN']
APP_URL = f'https://vitaljaheroku.herokuapp.com/{BOT_TOKEN}'
client = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)


@client.message_handler(commands=['start'])     # Команда /start
def start(message):                             # Функция меню бота
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_info = types.KeyboardButton('Информация о боте 🤖')
    item_commands = types.KeyboardButton('Команды ⌨')
    item_games = types.KeyboardButton('Игры 🎮')

    markup.add(item_info, item_commands, item_games)

    sticker = open('papich.webp', 'rb')
    # сообщение которое выводится при первом вызове меню (команда /start)
    client.send_sticker(message.chat.id, sticker)
    client.send_message(message.chat.id, 'Здравсвуйте, {0.first_name}!'.format(message.from_user), reply_markup=markup)


# работа всего бота
@client.message_handler(content_types=['text'])
def get_message(message):
    if message.chat.type == 'private':       # проверяем, что мы в ЛС, а не в канале

        if message.text == 'Информация о боте 🤖':
            client.send_message(message.chat.id, '''
@Meidori_bot – это простой игровой Телеграм бот, 
написанный на языке программирования Python, для проекта на Сириус.

Код можно просмотреть здесь: https://github.com/Meidori/Telegram_Bot
                            ''')

        elif message.text == 'Команды ⌨':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_list1 = types.KeyboardButton('1/2 страница команд 🗒')
            item_list2 = types.KeyboardButton('2/2 страница команд 🗒')
            item_back = types.KeyboardButton('Назад ⬅')

            markup.add(item_list1, item_list2, item_back)

            client.send_message(message.chat.id, 'Вы в меню: Команды ⌨',
                                reply_markup=markup)

        elif message.text == 'Игры 🎮':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_roll = types.KeyboardButton('Случайное число от 1 до 100 🎰')
            item_dice = types.KeyboardButton('Сыграть в кости 🎲')
            item_back = types.KeyboardButton('Назад ⬅')

            markup.add(item_roll, item_dice, item_back)

            client.send_message(message.chat.id, 'Вы в меню: Игры 🎮',
                                reply_markup=markup)

        elif message.text == 'Назад ⬅':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item_info = types.KeyboardButton('Информация о боте 🤖')
            item_commands = types.KeyboardButton('Команды ⌨')
            item_games = types.KeyboardButton('Игры 🎮')

            markup.add(item_info, item_commands, item_games)

            client.send_message(message.chat.id, 'Главное Меню 🗒',
                                reply_markup=markup)

        elif message.text == 'Случайное число от 1 до 100 🎰':
            client.send_message(message.chat.id, 'Случайное число(1-100): ' + str(random.randint(1, 100)))

        elif message.text == 'Сыграть в кости 🎲':
            client.send_message(message.chat.id, 'Вам выпало: ' + str(random.randint(1, 6)) + ' ' + str(random.randint(1, 6)))

        elif message.text == '1/2 страница команд 🗒':
            client.send_message(message.chat.id, list1)
        elif message.text == '2/2 страница команд 🗒':
            client.send_message(message.chat.id, list2)


@server.route('/' + BOT_TOKEN, methods=['POST'])
def get_message():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    client.process_new_updates([update])
    return '!', 200


@server.route('/')
def webhook():
    client.remove_webhook()
    client.set_webhook(url=APP_URL)
    return '!', 200


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
