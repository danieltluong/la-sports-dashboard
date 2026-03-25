from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams

SEASON = '2025-26'

#Get the ID for Lakers team
def get_lakers_id():
    all_teams = teams.get_teams()
    lakers = [team for team in all_teams if team['full_name'] == 'Los Angeles Lakers']
    return lakers[0]['id']

#Get season's game log
def fetch_lakers_games():
    team_id = get_lakers_id()
    gamelog = teamgamelog.TeamGameLog(team_id=team_id, season=SEASON)
    df = gamelog.get_data_frames()[0]
    return df

if __name__ == "__main__":
    games = fetch_lakers_games()
    latest_game = games.iloc[0]
    latest_matchup = latest_game['MATCHUP']
    latest_result = latest_game['WL']
    latest_score = latest_game['PTS']
    num_wins = latest_game['W']
    num_loss = latest_game['L']