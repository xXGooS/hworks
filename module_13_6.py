from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(asctime)s] [%(levelname)s]: %(message)s", encoding='utf-8')

api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage= MemoryStorage())

kb_reply = ReplyKeyboardMarkup(
    [
        [
        KeyboardButton(text="Рассчитать 🧮"),
        KeyboardButton(text="Информация 🗒️")
        ]
    ],
    resize_keyboard=True
)

kb_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="Рассчитать норму калорий", callback_data="calories"),
        InlineKeyboardButton(text="Формулы расчета ⚙️", callback_data="formulas")
        ]
    ]
)

@dp.message_handler(text = "Рассчитать 🧮")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb_inline)

@dp.callback_query_handler(text="formulas")
async def show_formulas(call):
    await call.message.answer(f"Формула расчёта: \n 10 * 'Вес' + 6.25 * 'Рост' - 5 * 'Возраст' + 5")
    await call.answer()

@dp.message_handler(commands=["start"])
async def start_message(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью,\nНажми на '`Рассчитать 🧮`', чтобы воспроизвести подсчет суточной нормы калорий.", parse_mode="Markdown", reply_markup = kb_reply)

@dp.message_handler()
async def any_message(message):
    await message.answer("Введите команду /start, чтобы начать общение.")

#--------------------Расчет калорий
class CalcCalories(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст:")
    await call.answer()
    await CalcCalories.age.set()


@dp.message_handler(state=CalcCalories.age)
async def set_growth(message, state):
    if isinstance(message.text, int) or isinstance(message.text, float):
        await message.reply("Пожалуйста, введите корректное число.")
        return
    await state.update_data(age=message.text)
    await message.answer("Введите свой рост:")
    await CalcCalories.growth.set()

@dp.message_handler(state=CalcCalories.growth)
async def set_weight(message, state):
    if isinstance(message.text, int) or isinstance(message.text, float):
        await message.reply("Пожалуйста, введите корректное число.")
        return
    await state.update_data(growth=message.text)
    await message.answer("Введите свой вес:")
    await CalcCalories.weight.set()

@dp.message_handler(state=CalcCalories.weight)
async def send_calories(message, state):
    if isinstance(message.text, int) or isinstance(message.text, float):
        await message.reply("Пожалуйста, введите корректное число.")
        return
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5

    await message.answer(f"Ваша норма калорий составляет: {calories}")
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
