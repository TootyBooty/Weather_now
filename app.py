from tkinter import N
from aiogram import executor
from messages import dp
from config import bot, storage

async def on_shutdown(dp):
    bot.close()
    storage.close()

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown)