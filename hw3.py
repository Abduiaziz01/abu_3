from aiogram import Bot, Dispatcher, types, executor
from config import token
from logging import basicConfig, INFO

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

start_keyboards = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("iOS"),
    types.KeyboardButton("UX/UI")
]
start_button = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}", reply_markup=start_button)
    print(message)

@dp.message_handler(text='Backend')
async def backend(message:types.Message):
    await message.answer("""Кто такой разработчик backend? Он ответственен за «внутренние» 
процессы web-продуктов и выбирает системы для хранения, гарантирует максимальный уровень 
производительности при малом объеме сбоев. Бэкэнд разработчик продумывает построение 
логики для реализации разных задумок, «строит» фундамент и опорную систему для проекта — 
от простого сайта для магазина одежды до сложных вычислительных систем и нейронных сетей.
Стоимость: 10000 сом в месяц
Длительность: 5 месяцев""")
    
@dp.message_handler(text='Frontend')
async def frontend(message:types.Message):
    await message.answer("""Хотите стать Frontend разработчиком и зарабатывать 
до 25000 сомов в месяц уже во время обучения? Тогда добро пожаловать в нашу школу 
программирования Geeks! У нас не просто проверенная годами качественная методика, но и 
обучение перспективной, высокооплачиваемой IT профессии, а не просто языку программирования. 
С нами соберете портфолио, научитесь работать в команде и станете востребованным Фронтенд 
веб разработчиком, который сможет выполнять заказы удаленно для разных заказчиков из 
любой точки мира.
Стоимость: 10000 сом в месяц
Длительность: 5 месяцев""")
    
@dp.message_handler(text='Android')
async def android(message:types.Message):
    await message.answer("""Никому не секрет, что Android – это наиболее популярная и 
распространенная мобильная платформа в мире. Плюс в отличие от iOS, она используется на 
самых разнообразных устройствах.
Стоимость: 10000 сом в месяц
Длительность: 7 месяцев""")
    
@dp.message_handler(text='iOS')
async def ios(message:types.Message):
    await message.answer("""У Apple довольно непростые требования, но за счет этого 
получаются качественные приложения, которые нравятся пользователям, поэтому широко 
востребована такая профессия как iOS разработчик.
Стоимость: 10000 сом в месяц
Длительность: 7 месяцев""")
    
@dp.message_handler(text='UX/UI')
async def ux_ui(message:types.Message):
    await message.answer("""Задались вопросом, как стать UX/UI-дизайнером с нуля, 
тогда вы не зря находитесь на нашем сайте, здесь вы можете записаться на курсы 
UX/UI-design, научиться создавать дизайн веб-сайтов и мобильных приложений, освоить 
самый популярный сервис Figma и закреплять обретенные навыки на практике во время обучения.
Стоимость: 10000 сом в месяц
Длительность: 3 месяца""")
    
executor.start_polling(dp)