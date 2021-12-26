from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton


buttonCommands = KeyboardButton('Команды ⌨')
buttonInfo = KeyboardButton('Прочая информация 🗒')

buttonSub = KeyboardButton('Подписаться ✅')
buttonUsnub = KeyboardButton('Отписаться ❎')
buttonFresh = KeyboardButton('Свежие новости 🗞')
buttonAll = KeyboardButton('Все новости 📰')


inline_buttonCode = InlineKeyboardButton(text='Код 💾', url='https://github.com/Meidori/Telegram_Bot')
inline_buttonDocs = InlineKeyboardButton(text='Docs 🖥', url='https://docs.aiogram.dev/en/latest/index.html')


inline_kb_client = InlineKeyboardMarkup(row_width=2)
inline_kb_client.add(inline_buttonCode, inline_buttonDocs)

keyboard_client = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_client.add(buttonInfo, buttonCommands)

keyboard_commands = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_commands.add(buttonSub, buttonUsnub, buttonFresh, buttonAll)




