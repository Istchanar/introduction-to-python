import random
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.dispatcher.filters import Command
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType


import settings as st
import requests_weather as rw
import requests_youtube as yt
from bot_states import BotStates
from u_interface import inline_menu

storage = MemoryStorage()
bot = Bot( token = st.TELEGRAM_BOT_TOKEN)
dp = Dispatcher(bot, storage = storage)


@dp.message_handler(Command('start', ignore_case = True))
async def start_command(message: Message) -> None:
    await message.answer('Hi!👋 \nChoose an action:', reply_markup = inline_menu)


# Weather block
@dp.callback_query_handler(lambda callback: callback.data == 'weather', state = None)
async def callback_weather(callback_q: CallbackQuery) -> None:
    await BotStates.weather.set()
    await bot.answer_callback_query(callback_q.id)
    await bot.send_message(callback_q.from_user.id, 'Send the city name or your location:')


@dp.message_handler(content_types = [ContentType.TEXT, ContentType.LOCATION], state = BotStates.weather)
async def get_wether(message: Message, state: FSMContext) -> None:
    try:
        if(message.content_type == ContentType.LOCATION):
            weather = rw.forecast(rw.get_location_url(message.location))
        else: 
            weather = rw.forecast(rw.get_city_url(message.text))
        await state.finish()
    except rw.WeatherException:
        await message.answer("Sorry, I didn't understand you 🙃.\nMaybe, the service is unavailable or bad request data (city, location).")
        return
    await message.answer(weather)


# Youtube block
@dp.callback_query_handler(lambda callback: callback.data == 'youtube', state = None)
async def callback_youtube(callback_q: CallbackQuery):
    await bot.answer_callback_query(callback_q.id)
    await bot.send_message(callback_q.from_user.id, "Send me the url, I'll see what I can do meaning.")
    await BotStates.youtube.set()


@dp.message_handler(state = BotStates.youtube)
async def download(message: Message, state: FSMContext):
    try:
        with open(f'{st.YOUTUBE_LOAD_PATH}/{yt.dowload_audio(message.text)}', 'rb') as audio:
            await bot.send_audio(message.chat.id, audio)
    except:
        await message.answer('I have a problem with your... case. Maybe the file is too big or network problems 😵‍💫')
        return
    await message.answer('Task completed 🥷')
    await state.finish()


# Save files block
@dp.callback_query_handler(lambda callback: callback.data == 'save_file', state = None)
async def callback_save_data(callback_q: CallbackQuery):
    await bot.answer_callback_query(callback_q.id)
    await bot.send_message(callback_q.from_user.id, "Send me document with file forman in caption (png, txt, mp3), I'll save it.")
    await BotStates.save_file.set()

@dp.message_handler(content_types = ContentType.DOCUMENT, state = BotStates.save_file)
async def save_data(message: Message, state: FSMContext) -> None:
    try:
        await message.document.download(destination_file = f'{st.TELEGRAM_LOAD_PATH}/{message.document.file_name}')
    except:
        await message.answer('I have problem with saving, try later.')
        return
    await message.answer('Document saved in local folder.')
    await state.finish()


@dp.message_handler(Command('cancel', ignore_case = True))
async def close_command(message: Message, state: FSMContext) -> None:
    c_state = await state.get_state
    if c_state is None: return
    await state.finish()
    await message.answer('Goodbye! 🛸', reply_markup = ReplyKeyboardRemove())


@dp.message_handler(Command('menu', ignore_case = True))
async def help_command(message: Message, state: FSMContext) -> None:
    await state.finish()
    await message.answer("I'm glad to help! 👋 \nChoose an action:", reply_markup=inline_menu)


@dp.message_handler()
async def echo_message(message: Message) -> None:
    await bot.send_message(message.from_user.id, message.text)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(message: Message) -> None:
    random_text = ["I don't understand what you mean 🎃", "Try /help command", "I can't do it"]
    await message.reply(random.choice(random_text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)
