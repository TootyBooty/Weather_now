from aiogram.dispatcher.filters.state import StatesGroup, State 

class Weather(StatesGroup):
    Start = State()
    City = State()
    Bye = State()
