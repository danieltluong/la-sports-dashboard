import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("NEWS_API_KEY")


#Pull news on Lakers or Rams
def fetch_sports_news():
    url = f"https://newsapi.org/v2/everything?q=Lakers+OR+Rams&language=en&sortBy=publishedAt&pageSize=10&apiKey={API_KEY}"
    
    response = requests.get(url)
    print(response.status_code)
    response.raise_for_status()
    data = response.json()
    return data['articles']

articles = fetch_sports_news()
for article in articles:
    print(article['title'])
    print(article['publishedAt'])
    print()