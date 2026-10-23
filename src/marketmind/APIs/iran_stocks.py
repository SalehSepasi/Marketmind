import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
API_KEY = os.getenv("IRAN_STOCKS_API_KEY")




def get_stock_data(symbol):
    url = "https://api.brsapi.ir/Tsetmc/Symbol.php"

    params = {
        "key": API_KEY,
        "l18": symbol
    }

    response = requests.get(
        url,
        params=params,
        timeout=15
    )
    response.raise_for_status()

    return simplify_stock_data(response.json())





def simplify_stock_data(data):
    return {
        "symbol": data.get("l18"),
        "company": data.get("l30"),
        "date": data.get("date_update"),
        "time": data.get("time"),
        "status": data.get("state"),
        "last_price": data.get("pl"),
        "closing_price": data.get("pc"),
        "change_percent": data.get("plp"),
        "daily_low": data.get("pmin"),
        "daily_high": data.get("pmax"),
        "volume": data.get("tvol"),
        "trade_count": data.get("tno"),
        "eps": data.get("eps"),
        "pe": data.get("pe"),
    }


@st.cache_data(ttl=3600)
def get_stock_symbols():
    url = "https://api.brsapi.ir/Tsetmc/AllSymbols.php"

    params = {
        "key": API_KEY,
        "type": 1
    }

    response = requests.get(
        url, params=params, timeout=15
    )
    response.raise_for_status()
    data = response.json()

    data = response.json()

    symbols = [stock["l18"] for stock in data if stock.get("l18")]

    return symbols
"""
    # استخراج فهرست نمادها
    if isinstance(data, dict):
        data = data.get("data", data.get("symbols", []))

    return [
        stock for stock in data
        if isinstance(stock, dict) and stock.get("l18")
    ]"""



if __name__ == "__main__":
    #data = get_stock_data("خودرو")
    print(get_stock_symbols())
    #print(data)