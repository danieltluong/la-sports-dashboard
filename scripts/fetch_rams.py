import requests
import json

TEAM_ID = 14

#Pull game data for the LA Rams (Team ID #14)
def fetch_rams_games():
    url = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams/{TEAM_ID}/schedule"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data

rams_data = fetch_rams_games()
event = rams_data['events'][0]
competition = event['competitions'][0]
competitors = competition['competitors']
for team in competitors:
    if team['team']['abbreviation'] == 'LAR':
        rams_score = team['score']['displayValue']
        rams_won = team['winner']
    else:
        opp_team = team['team']['abbreviation']
        opp_score = team['score']['displayValue']

result = 'W' if rams_won else 'L'

print(f"""
Latest Game: LAR vs {opp_team}
Result: {result}
Score: {rams_score} - {opp_score}
      """)