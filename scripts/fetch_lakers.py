import requests

def fetch_lakers_games():
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams/13/schedule"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

if __name__ == "__main__":
    data = fetch_lakers_games()
    events = data['events']
    print(f"Total games: {len(events)}")