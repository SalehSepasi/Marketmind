import streamlit as st 
from APIs.coin_name import get_coin_name
from APIs.prices import get_price
from APIs.news import get_news
from APIs.comments import get_comments
from APIs.LLM import generate

st.set_page_config(
    page_title="MarketMind",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("MarketMind")
st.write("Your AI-powered market research assistant")
topic = st.selectbox("Select ", ["Cryptocurrency"])

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
                    response = generate(prompt, price, news, comments)
                    st.subheader("AI Response")
                    st.write(response)

                except Exception as e:
                    st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a prompt.")

