from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import logging
import os, smtplib

load_dotenv('.env')

bot = Bot(token=os.environ.get('token'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_keyboards = [
    InlineKeyboardButton("идентификация", callback_data="идентификация")
]
start_button = InlineKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.callback_query_handler(lambda call: call.data == "идентификация")
async def handle_идентификация_callback(call: types.CallbackQuery):
    await идентификация(call.message)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}", reply_markup=start_button)

@dp.message_handler(commands="идентификация")
async def идентификация(message: types.Message):
    await message.answer("Введите свою электроннную почту: ")


executor.start_polling(dp, skip_updates=True)