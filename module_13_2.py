from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

api = "token"
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью, а так больше функций не имеется 😁')

@dp.message()
async def start_message(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    try:
        async def start():
            await dp.start_polling(bot)
        asyncio.run(start())
    except KeyboardInterrupt:
        print('Бот прекратил свою работу.')