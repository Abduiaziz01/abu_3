from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Привет, как дела?")

@dp.message_handler(commands='help')
async def get_help(message:types.Message):
    await message.answer("Вам нужна помощь?")

@dp.message_handler(text='Привет')
async def hello(message:types.Message):
    await message.answer("Привет!")

@dp.message_handler(text='test')
async def test_bot(message:types.Message):
    await message.answer("Тест бота")
    await message.reply("Ответ на сообщение")
    await message.answer_photo("https://akket.com/wp-content/uploads/2022/03/Takogo-eshhe-nikto-ne-delal.-Tesla-nachala-massovo-shtrafovat-vladeltsev-avtomobilei-na-20-ot-stoimosti-mashiny-2.jpg")
    with open('python.jpg', 'rb') as photo:
        await message.answer_photo(photo)
    await message.answer_location(40.51931772662277, 72.80301182274856)
    await message.answer_dice()


@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял, введите /help")

executor.start_polling(dp)