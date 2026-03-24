import pandas as pd
import fetch_rams



def transform_rams():
    raw = fetch_rams.fetch_rams_games()

    rows = []
    for event in raw['events']:
        competition = event['competitions'][0]
        competitors = competition['competitors']

        status = competition['status']['type']['shortDetail']
        completed = competition['status']['type']['completed']

        rams = None
        opponent = None
        for team in competitors:
            if team['team']['abbreviation'] == 'LAR':
                rams = team
            else:
                opponent = team
        
        row = {
            'date': event['date'][:10],
            'matchup': event['shortName'],
            'status': status,
            'completed': completed,
            'rams_score': rams['score']['displayValue'] if completed else None,
            'opp_score': opponent['score']['displayValue'] if completed else None,
            'opp_team': opponent['team']['abbreviation'],
            'result': 'W' if completed and rams.get('winner') else 'L' if completed else None,
            'win': 1 if completed and rams.get('winner') else 0 if completed else None,
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv('data/rams_games.csv',index=False)
    print("Saved rams_games.csv")
    print(df.head())

if __name__ == "__main__":
    transform_rams()

