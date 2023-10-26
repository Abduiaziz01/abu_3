import random
import smtplib,logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ParseMode
from aiogram.utils import executor
# Ваши данные
API_TOKEN = '6673882703:AAHCCnyynPWcRL7tyIiE2e_9r73E1QWehy4'
EMAIL_FROM = 'abu417494@gmail.com'
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_USERNAME = 'abu417494@gmail.com'    
SMTP_PASSWORD = 'komt nxyf egpe gruz'
DB_FILE = 'bot.db'
logging.basicConfig(level=logging.INFO)


# Генерация 6-значного кода
def generate_verification_code():
    return str(random.randint(100000, 999999))

# Функция для отправки кода по электронной почте
def send_verification_code(email, code):
    subject = "Код верификации"
    body = f"Ваш код верификации: {code}"
    message = f"Subject: {subject}\n\n{body}"

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    server.sendmail(EMAIL_FROM, email, message)
    server.quit()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Определение состояний беседы
class States(StatesGroup):
    EMAIL = State()
    VERIFY = State()

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    user = message.from_user
    await message.reply(f"Привет, {user.first_name}! Для начала идентификации, введите свою почту.")
    await States.EMAIL.set()

# Обработка ввода почты
@dp.message_handler(state=States.EMAIL)
async def process_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        verification_code = generate_verification_code()
        data['code'] = verification_code
        send_verification_code(data['email'], verification_code)
        await message.reply("На вашу почту отправлен 6-значный код верификации. Введите код:")
        await States.VERIFY.set()

# Обработка ввода кода верификации
@dp.message_handler(lambda message: message.text.isdigit(), state=States.VERIFY)
async def process_verification_code(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        user_code = message.text

        if user_code == data['code']:
            await message.reply("Вы успешно идентифицировались!")
        else:
            await message.reply("Неправильный ввод. Попробуйте еще раз.")

    # Очищаем данные в состоянии
    await state.finish()

executor.start_polling(dp, skip_updates=True)