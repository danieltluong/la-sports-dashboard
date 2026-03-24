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
    response.raise_for_status()
    data = response.json()
    return data

weather = current_weather()
current_temp = weather['main']['temp']
weather_description = weather['weather'][0]['description']
wind_speed = weather['wind']['speed']
humidity = weather['main']['humidity']
print(f"""
Temperature: {current_temp} F
Description: {weather_description}
Wind speed: {wind_speed} mph
Humidity: {humidity}%      
""")