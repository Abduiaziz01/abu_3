from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import logging
import os
import smtplib
import random
 

load_dotenv('.env')

bot = Bot(token=os.environ.get('token'))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


user_emails = {}  # Dictionary to store user emails


start_keyboards = [
    InlineKeyboardButton("идентификация", callback_data="идентификация")
]
start_button = InlineKeyboardMarkup(resize_keyboard=True).add(*start_keyboards)

@dp.callback_query_handler(lambda call: call.data == "идентификация")
async def handle_идентификация_callback(call: types.CallbackQuery):
    await идентификация(call.message)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}", reply_markup=start_button)

@dp.message_handler(commands="идентификация")
async def идентификация(message: types.Message):
    user_id = message.from_user.id
    user_emails[user_id] = None  
    await message.answer("Введите свою электронную почту: ")
    
num = random.randint(100000, 999999)
@dp.message_handler(lambda message: user_emails.get(message.from_user.id) is None)
async def handle_email(message: types.Message):
    user_id = message.from_user.id
    user_email = message.text
    user_emails[user_id] = user_email

    
    smtp_server = 'smtp.gmail.com'  
    smtp_port = 587  
    smtp_user = 'abu417494@gmail.com'  
    smtp_password = 'komt nxyf egpe gruz'  

    subject = "Verification Code"
    message_body = f"Your verification code is: {num}"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(smtp_user, user_email, f'Subject: {subject}\n\n{message_body}')
        server.quit()
        await message.answer("Код отправлен на вашу почту. Введите код для идентификации.")
    except Exception as e:
        print(e)
        await message.answer("Произошла ошибка при отправке кода на почту. Попробуйте еще раз.")


@dp.message_handler()
async def handle_verification_code(message: types.Message):
    input_code = int(message.text)

    if input_code == num:
        await message.answer("Вы успешно идентифицировались.")
    else:
        await message.answer("Неправильный ввод. Попробуйте еще раз.")

executor.start_polling(dp, skip_updates=True)
