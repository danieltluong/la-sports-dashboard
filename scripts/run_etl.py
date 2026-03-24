import fetch_weather
import fetch_lakers
import fetch_rams
import fetch_news

print("Running ETL pipeline...")
fetch_weather.run()
fetch_lakers.run()
fetch_rams.run()
fetch_news.run()
print("Done.")