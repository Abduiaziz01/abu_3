from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from dotenv import load_dotenv
from logging import basicConfig, INFO
import os, requests

import sqlite3

conn = sqlite3.connect('user_info.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
               user_id INTEGER PRIMARY KEY,
               first_name TEXT,
               last_name TEXT,
               full_name TEXT
               

)''')

conn.commit()

load_dotenv('.env')

bot = Bot(os.environ.get('token'))
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    full_name = message.from_user.full_name

    cursor.execute(f"INSERT OR REPLACE INTO users VALUES ('{user_id}', '{first_name}', '{last_name}', '{full_name}')")
    await message.answer(f"Привет {message.from_user.full_name}")
    conn.commit()

@dp.message_handler()
async def get_message_url(message:types.Message):
    if 'tiktok.com' in message.text:
        await message.answer(f"{message.text}")
        input_url = message.text.split("?")
        get_id_video = input_url[0].split("/")[5]
        await message.answer(f"ID_video: {get_id_video}")
        video_api = requests.get(f'https://api16-normal-c-useast1a.tiktokv.com/aweme/v1/feed/?aweme_id={get_id_video}').json()
        print(type(video_api))
        video_date = video_api.get("aweme_list")[0]
        author = video_date.get("author").get("nickname")
        await message.answer(f"Author: {author}")
        comment_count = video_date.get("statistics").get("comment_count")
        view_count = video_date.get("statistics").get("play_count")
        like_count = video_date.get("statistics").get("digg_count")
        await message.answer(f"Comment_count: {comment_count}")
        await message.answer(f"View_count: {view_count}")
        await message.answer(f"Like_count: {like_count}")
        video_url = video_api.get("aweme_list")[0].get("video").get("play_addr").get("url_list")[0]
        print(video_url)
        if video_url:
            await message.answer("Скачиваем видео...")
            title_video = video_api.get("aweme_list")[0].get("desc")
            print(title_video)
            try:
                with open(f'video/{title_video}.mp4', 'wb') as video_file:
                    video_file.write(requests.get(video_url).content)
                await message.answer(f"Видео {title_video} успешно скачан XD")
                with open(f'video/{title_video}.mp4', 'rb') as send_video_file:
                    await message.answer_video(send_video_file)
            except Exception as error:
                await message.answer(f"Error: {error}")
    else:
        await message.answer("Неправильная ссылка на видео TikTok")

executor.start_polling(dp, skip_updates=True)