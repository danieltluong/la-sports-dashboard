import pandas as pd
import fetch_lakers

def transform_lakers():
    raw = fetch_lakers.fetch_lakers_games()

    rows = []
    for event in raw['events']:
        competition = event['competitions'][0]
        status = competition['status']['type']['shortDetail']
        completed = competition['status']['type']['completed']

        lakers = None
        opponent = None
        for team in competition['competitors']:
            if team['team']['abbreviation'] == 'LAL':
                lakers = team
            else:
                opponent = team

        # Get season record from the record array
        record = lakers['record'][0]['displayValue'] if completed else None
        wins = record.split('-')[0] if record else None
        losses = record.split('-')[1] if record else None

        row = {
            'date': event['date'][:10],
            'matchup': event['shortName'],
            'status': status,
            'completed': completed,
            'lakers_score': lakers['score']['displayValue'] if completed else None,
            'opp_score': opponent['score']['displayValue'] if completed else None,
            'opp_team': opponent['team']['abbreviation'],
            'result': 'W' if completed and lakers.get('winner') else 'L' if completed else None,
            'win': 1 if completed and lakers.get('winner') else 0 if completed else None,
            'wins': wins,
            'losses': losses,
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv("data/lakers_games.csv", index=False)
    print("Saved lakers_games.csv")
    print(df[df['completed'] == True].head())

if __name__ == "__main__":
    transform_lakers()