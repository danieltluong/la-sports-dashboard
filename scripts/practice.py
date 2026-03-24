import pandas as pd

data = [
    {"name": "LeBron", "points": 28, "team": "LAL"},
    {"name": "AD",     "points": 22, "team": "LAL"},
    {"name": "Austin", "points": 15, "team": "LAL"},
]

df = pd.DataFrame(data)
print(df)
print()

small_df = df[['name','points']]
print(small_df)
print()

df = df.rename(columns={'name':'player_name','points':'pts'})
print(df)
print()

df.to_csv('data/practice.csv',index=False)
print('saved!')