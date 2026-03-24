import requests

def fetch_sports_news():
    articles = []
    
    # Fetch Lakers news
    lakers_url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/news?limit=5&team=lal"
    lakers_response = requests.get(lakers_url)
    lakers_response.raise_for_status()
    lakers_data = lakers_response.json()
    articles.extend(lakers_data.get('articles', []))
    
    # Fetch Rams news
    rams_url = "https://site.api.espn.com/apis/site/v2/sports/football/nfl/news?limit=5&team=lar"
    rams_response = requests.get(rams_url)
    rams_response.raise_for_status()
    rams_data = rams_response.json()
    articles.extend(rams_data.get('articles', []))
    
    return articles
