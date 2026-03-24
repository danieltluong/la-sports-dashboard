import transform_weather
import transform_lakers
import transform_rams
import transform_news

print("Starting ETL pipeline...")
transform_weather.transform_current_weather()
transform_lakers.transform_lakers()
transform_rams.transform_rams()
transform_news.transform_news()
print("\nAll done. CSVs updated in /data")