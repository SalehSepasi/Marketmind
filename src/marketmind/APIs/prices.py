import os
import requests
from dotenv import load_dotenv

load_dotenv()
COINGECKO_API_KEY = os.getenv("COINGECKO_API_KEY")
BASE_URL = "https://api.coingecko.com/api/v3/simple/price"


def get_price(coin_name: str, currency: str = "usd"):
    """Get the latest available price of a cryptocurrency."""

    if not COINGECKO_API_KEY:
        raise ValueError(
            "COINGECKO_API_KEY is not configured in .env"
        )

    params = {
        "ids": coin_name,
        "vs_currencies": currency,
        "include_24hr_change": "true",
        "include_last_updated_at": "true",
    }

    headers = {
        "x-cg-demo-api-key": COINGECKO_API_KEY,
    }

    response = requests.get(
        BASE_URL,
        params=params,
        headers=headers,
        timeout=20,
    )
    response.raise_for_status()

    data = response.json()



    return data


if __name__ == "__main__":
    print(get_price("Bitcoin"))