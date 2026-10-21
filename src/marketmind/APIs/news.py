import os
import requests
from dotenv import load_dotenv

load_dotenv()
MARKETAUX_API_KEY = os.getenv("MARKETAUX_API_KEY")


def get_news(topic: str, published_after: str | None = None):

    BASE_URL = "https://api.marketaux.com/v1/news/all"
    if not MARKETAUX_API_KEY:
        raise ValueError("MARKETAUX_API_KEY is not configured.")
    params = {
        "api_token": MARKETAUX_API_KEY,
        "search": topic,
        "language": "en",
        "limit": 3,
        "published_after": published_after
    }

    response = requests.get(
        BASE_URL,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    print( process_news(response.json().get("data", []))   )

    


def process_news(articles: list[dict]) -> list[dict]:
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

if __name__ == "__main__":
    get_news("Bitcoin","2026-10-10")