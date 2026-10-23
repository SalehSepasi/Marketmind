from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("LLM7_API_KEY")

client = OpenAI(
        api_key=api_key,
        base_url="https://api.llm7.io/v1",
    )




def generate_crypto_response(prompt: str, prices: str, news: str, comments: str):
    
    response = client.chat.completions.create(
    model="default",
    messages=[
        {
            "role": "system",
            "content": (
                """You are MarketMind, an AI assistant specialized in cryptocurrency market analysis. 
                Analyze crypto prices, market data, and news objectively. 
                Distinguish facts from assumptions, identify risks,
                and never invent data or present uncertain predictions as facts."""
            )
        },
        {
            "role": "user",
            "content": (
                f"User prompt:\n{prompt}\n\n"
                f"Price: {prices}\n\n"
                f"News: {news}\n\n"
                f"Comments: {comments}"
                )
        }
    ],
    
)
    return response.choices[0].message.content






def generate_stock_response(prompt: str, stock_data: str):
    response = client.chat.completions.create(
    model="default",
    messages=[
        {
            "role": "system",
            "content": (
                """You are MarketMind, an AI assistant specialized in Iranian stocks market analysis. 
                Analyze stock prices, market data, and news objectively. 
                Distinguish facts from assumptions, identify risks,
                and never invent data or present uncertain predictions as facts."""
            )
        },
        {
            "role": "user",
            "content": (
                f"User prompt:\n{prompt}\n\n"
                f"Stock data: {stock_data}"
                )
        }
    ]
)
    return response.choices[0].message.content