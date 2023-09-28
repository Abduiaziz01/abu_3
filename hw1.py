from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет! Я загадал число от 1 до 3 угадайте")

@dp.message_handler(text=['1', '2', '3'])
async def rand(message:types.Message):
    user =  message.text
    bot = random.choice(['1', '2', '3'])
    if user == bot:
        await message.answer("Правильно вы отгадали")
        await message.answer_photo("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    elif user != bot:
        await message.answer("Неправильно вы не отгадали")
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

executor.start_polling(dp)