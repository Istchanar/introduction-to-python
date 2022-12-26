import os
from dotenv import load_dotenv


def get_env(var_name: str) -> str:
    try: return os.environ[var_name]
    except KeyError: raise KeyError


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


# Telegram settings
TELEGRAM_LOAD_PATH = 'text_extractor_bot/data/telegram'
TELEGRAM_BOT_TOKEN = get_env('TELEGRAM_BOT_TOKEN')


# Weather settings
OPENWEATHER_API_KEY = get_env('OPENWEATHER_API_KEY')
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/'
WEATHER_REQ_PARAMS = 'cnt=4&units=metric&lang=en'


# YouTube settings
YOUTUBE_LOAD_PATH = 'text_extractor_bot/data/youtube'
