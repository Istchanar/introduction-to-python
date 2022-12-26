from aiogram.types import \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

close = KeyboardButton('/close')
youtube = InlineKeyboardButton('Audio from YTube', callback_data='youtube')
weather = InlineKeyboardButton('Сheck weather', callback_data='weather')
save_file = InlineKeyboardButton('Save file', callback_data='save_file')
open_gh = InlineKeyboardButton('Look source code', url='https://github.com/Istchanar/introduction-to-python')

reply_menu = ReplyKeyboardMarkup(
    resize_keyboard=True, one_time_keyboard=True).add(close)
inline_menu = InlineKeyboardMarkup().add(weather, youtube, save_file, open_gh)
