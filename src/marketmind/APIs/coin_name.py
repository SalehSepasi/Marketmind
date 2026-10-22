import requests

url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=100"

def get_coin_name():
    """
    Get the name of all cryptocurrencies
    """
    
    data = requests.get(url).json()

    coins = [coin["name"] for coin in data]
    return coins

if __name__ == "__main__":
    print(get_coin_name())