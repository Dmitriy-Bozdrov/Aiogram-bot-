from aiogram import types, Dispatcher
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram.fsm.state import StatesGroup, State
from keyboards import get_language_keyboard
from config import CSV_URL
import aiohttp
import csv

# Шаги FSM
class StartFSM(StatesGroup):
    language = State()

# Хендлер на /start — только спрашиваем язык
async def start_command(message: types.Message, state: FSMContext):
    await message.answer("👋 Привет! Пожалуйста, выберите язык:", reply_markup=get_language_keyboard())
    await state.set_state(StartFSM.language)

# Хендлер, который срабатывает, когда пользователь выбрал язык
async def set_language(message: types.Message, state: FSMContext):
    language = message.text
    await state.update_data(language=language)

    # Загружаем курсы только здесь!
    rates = await fetch_currency_rates()
    
    user_name = message.from_user.first_name

    # Формируем текст на выбранном языке
    if "Українська" in language:
        reply = (
            f"👋 Вітаю, {user_name}!\n\n"
            "📊 Актуальний курс валют:\n\n"
            " Валюта || Купівля || Продаж \n\n" +
            rates +
            "\n🧾 Використовуйте /crypto або /cash для операцій."
        )
    elif "English" in language:
        reply = (
            f"👋 Hello, {user_name}!\n\n"
            "📊 Current exchange rates:\n\n"
            " Currency || Buy || Sell \n\n" +
            rates +
            "\n🧾 Use /crypto or /cash for other operations."
        )
    else:
        reply = (
            f"👋 Привет, {user_name}!\n\n"
            "📊 Актуальные курсы валют:\n\n"
            " Валюта || Покупка || Продажа \n\n" +
            rates +
            "\n🧾 Используйте /crypto или /cash для других операций."
        )

    await message.answer(reply)
    await state.clear()

# Функция для загрузки курсов
async def fetch_currency_rates():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(CSV_URL) as resp:
                if resp.status == 200:
                    text_data = await resp.text()
                    reader = csv.reader(text_data.splitlines())
                    rows = list(reader)

                    rates = ""
                    for row in rows[1:]:
                        if len(row) >= 3:
                            a, b, c = row[0], row[1], row[2]
                            rates += f"💱 {a}:||         {b}       /   {c}\n"
                    return rates
    except Exception as e:
        print(f"Ошибка при получении курсов валют: {e}")
    return "❌ Ошибка загрузки курсов."

# Регистрация хендлеров
def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
    dp.message.register(set_language, StateFilter(StartFSM.language))
