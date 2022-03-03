import requests
from config import WEATHER_API

def weather_now(city):
    params = {
        'q':f'{city}',
        'appid':f'{WEATHER_API}',
        'lang':'ru',
        'units':'metric'
    }
    try:
        r = requests.get(url='https://api.openweathermap.org/data/2.5/weather', params=params).json()
        sky = r.get('weather')[0].get('description')
        temp = round(r.get('main').get('temp'), 1)
        feels_like = round(r.get('main').get('feels_like'), 1)
        wind = round(r.get('wind').get('speed'), 1)
        text = f'В городе {city} сейчас {sky}!\nТемпература воздуха {temp}℃\nОщущается как {feels_like}℃\nСкорость ветра {wind}💨'
    except:
        text = 'Похоже такого города не существует😅\nПроверь, не допущена ли ошибка.'
    return text