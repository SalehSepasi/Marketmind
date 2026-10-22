import os
import requests
from datetime import date, timedelta
from dotenv import load_dotenv

load_dotenv()
MARKETAUX_API_KEY = os.getenv("MARKETAUX_API_KEY")


def get_news(topic: str):

    BASE_URL = "https://api.marketaux.com/v1/news/all"
    if not MARKETAUX_API_KEY:
        raise ValueError("MARKETAUX_API_KEY is not configured.")

    params = {
        "api_token": MARKETAUX_API_KEY,
        "search": topic,
        "language": "en",
        "limit": 3,
        "published_after": time_filter()
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    return process_news(response.json().get("data", []))  

    


def process_news(articles: list[dict]):
    """Extract useful fields from raw news articles."""

    processed_articles = []

    for article in articles:
        processed_article = {
            "title": article.get("title"),
            "description": article.get("description"),
            "published_at": article.get("published_at"),
            "source": article.get("source"),
            "url": article.get("url"),
        }

        processed_articles.append(processed_article)

    return processed_articles

def time_filter():
    today = date.today()
    seven_days_ago = today - timedelta(days=7)
    return seven_days_ago

if __name__ == "__main__":
    get_news("Bitcoin",time_filter())