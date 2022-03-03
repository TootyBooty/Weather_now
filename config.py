from dotenv import load_dotenv
import os
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import logging

load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
WEATHER_API = os.getenv('WEATHER_API')

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(format=u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s',
                    level=logging.INFO,
                    )
