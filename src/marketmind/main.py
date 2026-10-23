import streamlit as st 
from APIs.coin_name import get_coin_name
from APIs.prices import get_price
from APIs.news import get_news
from APIs.comments import get_comments
from APIs.LLM import generate_stock_response, generate_crypto_response
from APIs.iran_stocks import get_stock_symbols, get_stock_data

st.set_page_config(
    page_title="MarketMind",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("MarketMind")
st.write("Your AI-powered market research assistant")
topic = st.selectbox("Select ", ["Cryptocurrency","Iranian Stocks"])




if topic == "Iranian Stocks":
    stock_symbol = st.selectbox("Select a stock",get_stock_symbols())
    stock_data = get_stock_data(stock_symbol)

    prompt = st.text_area(
        "Your Prompt",
        placeholder="Enter your prompt here...",
        height=180,
    )

    if st.button("Generate", type="primary", use_container_width=True):
        if prompt.strip():
            with st.spinner("Generating response..."):
                try:
                    response = generate_stock_response(prompt, stock_data)
                    st.subheader("AI Response")
                    st.write(response)
                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")










if topic == "Cryptocurrency":
    coin = st.selectbox("Select a cryptocurrency",get_coin_name())
    price = get_price(coin)
    news = get_news(coin)
    comments = get_comments()
    

    prompt = st.text_area(
        "Your Prompt",
        placeholder="Enter your prompt here...",
        height=180,
    )

    if st.button("Generate", type="primary", use_container_width=True):
        if prompt.strip():
            with st.spinner("Generating response..."):
                try:
                    response = generate_crypto_response(prompt, price, news, comments)
                    st.subheader("AI Response")
                    st.write(response)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")

