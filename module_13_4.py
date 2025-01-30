from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(text = "Calories")
async def set_age(message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if isinstance(message.text, int) or isinstance(message.text, float):
        await message.reply("Пожалуйста, введите корректное число.")
        return
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if isinstance(message.text, int) or isinstance(message.text, float):
        await message.reply("Пожалуйста, введите корректное число.")
        return
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if isinstance(message.text, int) or isinstance(message.text, float):
        await message.reply("Пожалуйста, введите корректное число.")
        return
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5

    await message.answer(f"Ваша норма калорий составляет: {calories}")
    await state.finish()

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью,\nНапиши '`Calories`', чтобы воспроизвести подсчет суточной нормы калорий.", parse_mode="Markdown")

@dp.message_handler()
async def any_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == '__main__':
    try:
        async def start():
            await dp.start_polling(bot)
        asyncio.run(start())
    except KeyboardInterrupt:
        print('Бот прекратил свою работу.')
