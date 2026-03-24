import pandas as pd
import fetch_lakers

def transform_lakers():
    raw = fetch_lakers.fetch_lakers_games()

    df = raw[['GAME_DATE', 'MATCHUP', 'WL', 'PTS', 'FG_PCT', 'FG3_PCT', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'W', 'L']]

    #Rename to clean readable names
    df = df.rename(columns={
        'GAME_DATE': 'date',
        'MATCHUP': 'matchup',
        'WL': 'result',
        'PTS': 'points',
        'FG_PCT': 'fg_pct',
        'FG3_PCT': 'fg3_pct',
        'REB': 'rebounds',
        'AST': 'assists',
        'STL': 'steals',
        'BLK': 'blocks',
        'TOV': 'turnovers',
        'W': 'wins',
        'L': 'losses'
    })

    #Adding a win loss column bool
    df['win'] = df['result'].apply(lambda x: 1 if x == 'W' else 0)

    df.to_csv('data.lakers_games.csv',index=False)
    print('Saved lakers_games.csv')
    print(df.head())

if __name__ == "__main__":
    transform_lakers()