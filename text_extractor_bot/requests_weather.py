import requests
from aiogram.types import Location


import settings as s


class WeatherException(BaseException):
    pass


def forecast(url: str) -> str:
    response = get_response(url)
    celsius_mark = '\u2103'
    new_row = '\n'
    main_data = response['main']
    wind_data = response['wind']
    twelve_hour_forecast = (f"🌡 Temperature: {main_data['temp']} {celsius_mark}{new_row}"
                            f"😶‍🌫️ Feels like: {main_data['feels_like']} {celsius_mark}{new_row}"
                            f"✨ Pressure:   {round(int(main_data['pressure'])/1.333, 1)} mmhg{new_row}"
                            f"☁ Humidity:   {main_data['humidity']} %{new_row}"
                            f"🌊 Wind:       {wind_data['speed']} ms{new_row}")
    return twelve_hour_forecast


def get_response(url: str):
    response = requests.get(url)
    if (response.status_code != 200):
        raise WeatherException()
    return response.json()['list'][3]


def get_city_url(city: str) -> str:
    return f'{s.WEATHER_API_URL}forecast?q={city}&appid={s.OPENWEATHER_API_KEY}&{s.WEATHER_REQ_PARAMS}'


def get_location_url(location: Location) -> str:
    return f'{s.WEATHER_API_URL}forecast?lat={location.latitude}&lon={location.longitude}&appid={s.OPENWEATHER_API_KEY}&{s.WEATHER_REQ_PARAMS}'
