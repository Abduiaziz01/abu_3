from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardButton
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from logging import basicConfig, INFO
import os, requests 

load_dotenv('.env')

bot = Bot(os.environ.get('Token'))
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_keyboards = [
    InlineKeyboardButton("USD/KGS"),
    InlineKeyboardButton("EUR/KGS"),
    InlineKeyboardButton("RUB/KGS"),
    InlineKeyboardButton("KZT/KGS")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"""Привет {message.from_user.full_name}!
Я бот для обмена валюты""", reply_markup=start_button)
    url = 'https://www.nbkr.kg/index.jsp?lang=RUS'

    response = requests.get(url=url)
    print(response)
    soup = BeautifulSoup(response.text, 'lxml')
    all_currencies = soup.find_all('td', class_='excurr')
    print(all_currencies)
    all_changes = soup.find_all('td', class_='exrate')
    print(all_changes)

@dp.message_handler(text='USD/KGS')
async def change1(message:types.Message):
    await message.answer("100 - 8932")

@dp.message_handler(text='EUR/KGS')
async def change2(message:types.Message):
    await message.answer("100 - 9411")

@dp.message_handler(text='RUB/KGS')
async def change3(message:types.Message):
    await message.answer("100 - 92")

@dp.message_handler(text='KZT/KGS')
async def change4(message:types.Message):
    await message.answer("100 - 19")

executor.start_polling(dp, skip_updates=True)