from aiogram import types, Dispatcher
from aiogram.utils.markdown import hunderline, hlink
from bot_creation import client, dispatcher
from buttons import keyboard_client, inline_kb_client, keyboard_commands
import texts
from sq_database import SQ
import json
from sirius_site import check_news_update


db = SQ('database.db')


async def command_start(message: types.Message):
    photo = open('papich.webp', 'rb')
    await client.send_photo(message.from_user.id, photo)
    await client.send_message(message.from_user.id, '''
Привет! Если ты впервые воспользовался ботом, то прочитай "Прочая информация 🗒" и ознакомся с командами по кнопке
"Команды ⌨"    
    ''',
                              reply_markup=keyboard_client)


async def command_commands(message: types.Message):
    await client.send_message(message.from_user.id, texts.commands, reply_markup=types.ReplyKeyboardRemove())
    await client.send_message(message.from_user.id, 'Лучше использовать клавиатуру, а не текстовые команды',
                              reply_markup=keyboard_commands)


async def command_info(message: types.Message):
    await client.send_message(message.from_user.id, texts.info, reply_markup=keyboard_client)
    await message.answer('Ссылки:', reply_markup=inline_kb_client)


async def get_all_news(message: types.Message):
    with open('news_dict.json') as file:
        news_dict = json.load(file)

        for k, v in sorted(news_dict.items()):
            news = f'{hlink(v["article_title"], v["article_url"])}\n'

            await message.answer(news)


async def get_fresh_news(message: types.Message):
    fresh_news = check_news_update()

    if len(fresh_news) >= 1:
        for k, v in sorted(fresh_news.items()):
            news = f'{hlink(v["article_title"], v["article_url"])}\n'

            await message.answer(news)

    else:
        await message.answer('Пока нет свежих новостей...')


async def subscribe(message: types.Message):
    if (not db.subs_exist(message.from_user.id)):
        # если юзера нет в базе, добавляем его
        db.add_subs(message.from_user.id)
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subs(message.from_user.id, True)

    await message.answer("Вы успешно подписались на рассылку!")


async def unsubscribe(message: types.Message):
    if (not db.subs_exist(message.from_user.id)):
        # если юзера нет в базе, добавляем его с неактивной подпиской (запоминаем)
        db.add_subs(message.from_user.id, False)
        await message.answer("Вы итак не подписаны.")
    else:
        # если он уже есть, то просто обновляем ему статус подписки
        db.update_subs(message.from_user.id, False)

        await message.answer("Вы успешно отписаны от рассылки.")


def register_handlers_client(dispatcher: Dispatcher):
    dispatcher.register_message_handler(command_start, commands=['start', 'help'])
    dispatcher.register_message_handler(command_info, lambda message: 'Прочая информация' in message.text)
    dispatcher.register_message_handler(command_commands, lambda message: 'Команды' in message.text)
    dispatcher.register_message_handler(subscribe, lambda message: 'Подписаться' in message.text)
    dispatcher.register_message_handler(unsubscribe, lambda message: 'Отписаться' in message.text)
    dispatcher.register_message_handler(get_all_news, lambda message: 'Все' in message.text)
    dispatcher.register_message_handler(get_fresh_news, lambda message: 'Свежие' in message.text)
