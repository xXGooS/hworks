from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = " "
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

@dp.message_handler(commands=["start"])
async def start_message(message):
    print("Привет! Я бот помогающий твоему здоровью, а так больше функций не имеется 😁")

@dp.message_handler()
async def any_message(message):
    print("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    dp.start_polling(bot)
