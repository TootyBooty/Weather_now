import asyncio
from config import dp
from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards import start_keyboard, City_keyboard, Bye_keyboard
from aiogram.dispatcher import FSMContext
from states import Weather
from getweather import weather_now

@dp.message_handler(Command(['start', 'help']), state=None)
async def help_commands(message:Message):
    await message.answer(text='Привет!\nЯ бот, который поможет тебе узнать погоду ☀️', reply_markup=start_keyboard)
    await Weather.Start.set()


@dp.message_handler(state=Weather.Start)
async def City(message:Message, state:FSMContext):
    await message.answer(text='Выбери город из списка, или введи название вручную', reply_markup=City_keyboard)
    await Weather.City.set()


@dp.message_handler(state=Weather.City)
async def get_answer(message:Message, state:FSMContext):
    city = message.text
    await message.answer(text=weather_now(city), reply_markup=Bye_keyboard)
    await Weather.Bye.set()
    

@dp.message_handler(state=Weather.Bye)
async def goodbye(message:Message, state:FSMContext):
    if message.text == 'Выбрать другой город🏙':
        await Weather.City.set()
        await message.answer(text='Какой город вас интересует?', reply_markup=City_keyboard)
    else:
        await message.answer(text='Всего хорошего 👋\nЕсли снова захочешь узнать погоду, нажми сюда --> /start')
        await state.finish()


@dp.message_handler(state=None)
async def echo(message:Message):
    await message.answer(text="Извини, я не знаю что тебе на это ответить 🥺\nПопробуй написать /start")
