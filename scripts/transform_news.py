import pandas as pd
import fetch_news

def transform_news():
    raw = fetch_news.fetch_sports_news()

    rows = []
    for article in raw:
        row = {
            'published_at': article.get('published', '')[:10],
            'headline': article.get('headline', ''),
            'description': article.get('description', ''),
            'url': article.get('links', {}).get('web', {}).get('href', ''),
            'source': 'ESPN',
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    df.to_csv("data/news.csv", index=False)
    print("Saved news.csv")
    print(df[['published_at', 'headline']].head(10))

if __name__ == "__main__":
    transform_news()