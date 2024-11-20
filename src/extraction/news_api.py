 
import requests
import json
import sys
import os
from datetime import date, datetime, timedelta
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.utils.s3_utils import upload_to_s3
from src.utils.config import NEWS_API_KEY


# Function to fetch news articles
def fetch_news(brand_name, from_date, to_date, language="en", limit=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": brand_name,
        "from": from_date,
        "to": to_date,
        "pageSize": limit,
        "language": language,
        "apiKey": NEWS_API_KEY
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        #print(json.dumps(data, ensure_ascii=False,indent=4))
        if data.get("status") == "ok":
            articles = data.get("articles", [])
            # Process the articles to maintain consistent structure
            formatted_articles = [
                {
                    "title": article["title"],
                    "description": article.get("description", ""),
                    "content": article.get("content", ""),
                    "url": article["url"],
                    "published_at": article["publishedAt"],
                    "source": article["source"]["name"],
                    "author": article.get("author", "Unknown")
                }
                for article in articles
            ]
            return formatted_articles
        else:
            print("Error:", data.get("message"))
            return []
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return []

def save_news_data_to_s3(brand_name, from_date, to_date):
    articles = fetch_news(brand_name, from_date, to_date)
    
    if articles:
        file_name = f"{brand_name}/news/{date.today()}/raw_data.json"
        upload_to_s3(articles, "car-talks-raw", file_name)
        print(f"Uploaded {len(articles)} articles to S3: {file_name}")
    else:
        print(f"No articles found for {brand_name}.")


if __name__ == "__main__":
    brand_name = "Tesla"
    to_date = datetime.now().strftime('%Y-%m-%d')
    from_date = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')

    print(f"Fetching news for brand: {brand_name}")
    print(f"Date range: {from_date} to {to_date}")

    articles = fetch_news(brand_name, from_date, to_date)

    # if articles:
    #     upload_to_s3(articles, brand_name)
    # else:
    #     print("No articles found.")

    print(type(articles))
    sys.stdout.reconfigure(encoding='utf-8')
    
    with open("sample.json", "w") as outfile:
        json.dump(articles,outfile, ensure_ascii=False,indent=4)

    print(json.dumps(articles, ensure_ascii=False,indent=4))
