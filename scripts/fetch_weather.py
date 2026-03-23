#Purpose: Pull the current weather for Los Angeles, California

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('OPENWEATHER_API_KEY')

#Los Angeles coordinates
LAT = 34.0522
LON = -118.2437

def current_weather():
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        "lat": LAT
        ,"lon": LON
        ,"appID": API_KEY
        ,"units": "imperial"
    }

    response = requests.get(url, params=params)
    data = response.json()
    return data

weather = current_weather()
current_temp = weather['main']['temp']
weather_description = weather['weather'][0]['description']
wind_speed = weather['wind']['speed']
print(current_temp, weather_description,wind_speed)