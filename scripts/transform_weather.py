import pandas as pd
from datetime import datetime, timezone
import fetch_weather

def transform_current_weather():
    raw = fetch_weather.current_weather()

    row = {
        "fetched_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
        "city": raw["name"],
        "temp_f": raw["main"]["temp"],
        "feels_like_f": raw["main"]["feels_like"],
        "humidity_pct": raw["main"]["humidity"],
        "wind_mph": raw["wind"]["speed"],
        "condition": raw["weather"][0]["main"],
        "description": raw["weather"][0]["description"],
        "visibility_mi": round(raw["visibility"] / 1609, 1),
        "sunrise": datetime.fromtimestamp(raw["sys"]["sunrise"], tz=timezone.utc).strftime("%H:%M"),
        "sunset": datetime.fromtimestamp(raw["sys"]["sunset"], tz=timezone.utc).strftime("%H:%M"),
    }

    df = pd.DataFrame([row])
    df.to_csv('data/weather_current.csv',index=False)
    print('Dataframe save to weather_current.csv')
    print(df)

transform_current_weather()