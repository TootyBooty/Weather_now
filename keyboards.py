from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton

start_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
start_button = KeyboardButton(text='Узнать погоду 🌚 🌝')
start_keyboard.insert(start_button)


City_buttons = [
    KeyboardButton(text='Москва'), KeyboardButton(text='Санкт-Петербург'),
    KeyboardButton(text='Люберцы'), KeyboardButton(text='Орск')
    ]
City_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=2)
for buttons in City_buttons:
    City_keyboard.insert(buttons)


Bye_keyboard = ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
back_button = KeyboardButton(text='Выбрать другой город🏙')
bye_button = KeyboardButton(text='Завершить⛔️')
Bye_keyboard.row(back_button, bye_button)
