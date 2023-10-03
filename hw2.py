from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_keyboards = [
    types.KeyboardButton("О нас"),
    types.KeyboardButton("Объекты"),
    types.KeyboardButton("Контакты")
]
start_buttons = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}", reply_markup=start_buttons)

@dp.message_handler(text='О нас')
async def about(message:types.Message):
    await message.answer("""СТРОИТЕЛЬНАЯ КОМПАНИЯ

ОсОО «Визион Групп»
Мы - развивающаяся компания, которая предлагает своим клиентам широкий выбор квартир в 
объектах расположенных во всех наиболее привлекательных районах городов Ош и Джалал-Абад. 
У нас максимально выгодные условия, гибкий (индивидуальный) подход при реализации жилой и 
коммерческой недвижимости. Мы занимаем лидирующие позиции по количеству объектов по югу 
Кыргызстана. Наша миссия: Мы обеспечиваем население удобным жильем для всей семьи, 
проявляя лояльность и индивидуальный подход и обеспечивая высокий уровень обслуживания. 
Мы обеспечиваем бизнес подходящим коммерческим помещением, используя современные решения и 
опыт профессионалов своего дела.""")

object_keyboards = [
    types.KeyboardButton("Завершенные объекты"),
    types.KeyboardButton("Строящиеся объекты"),
    types.KeyboardButton("Главная")
]
object_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*object_keyboards)

@dp.message_handler(text='Объекты')
async def objects(message:types.Message):
    await message.answer("Выбирите объекты:", reply_markup=object_button)

@dp.message_handler(text='Завершенные объекты')
async def object1(message:types.Message):
    await message.answer("""ЖК «Малина-Лайф», ЖК «Томирис», 
ЖК «Черемушки», ЖК «Фрунзе»""")

@dp.message_handler(text='Строящиеся объекты')
async def object2(message:types.Message):
    await message.answer("""ЖК «ВИЗИОН РЕЗИДЕНС», ЖК «ВИЗИОН СПУТНИК», 
ЖК «ВИЗИОН ЛАЙФ-ПАРК», ЖК «ВИЗИОН ВИКТОРИЯ», 
ЖК «ВИЗИОН КОМФОРТ», ЖК «МАЛИНА ЛАЙФ 2»""")
    
@dp.message_handler(text='Главная')
async def home(message:types.Message):
    await start(message)
    
@dp.message_handler(text='Контакты')
async def contact(message:types.Message):
    await message.answer("""Контакты
contact@vg-stroy.com
+996 709 620088
+996 772 620088
+996 550 620088""")

executor.start_polling(dp)