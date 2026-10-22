# 🚀 MarketMind
### AI-Powered Cryptocurrency Market Analysis


MarketMind is an AI-powered cryptocurrency analysis application built with Python. It brings together market prices, cryptocurrency news, and community discussions in one interactive dashboard, allowing users to explore market developments and generate contextual insights with the help of a Large Language Model (LLM).

With a customizable AI prompt, users can guide the analysis toward the questions that matter most to them.

---

## ✨ Features

- 📈 **Cryptocurrency Market Data** — Retrieve current cryptocurrency prices and available market changes.
- 📰 **Crypto News Aggregation** — Collect relevant news to understand recent market developments.
- 💬 **Community Insights** — Retrieve public discussions from CoinMarketCap Community for additional context.
- 🤖 **AI-Powered Analysis** — Combine collected data with custom prompts to generate contextual analysis and summaries.
- 🎯 **Custom AI Prompts** — Guide the model toward specific questions, trends, risks, or market developments.
- 🖥️ **Interactive Dashboard** — Explore cryptocurrencies, submit prompts, and view AI-generated results through Streamlit.
- 🧩 **Modular Architecture** — Keep API integrations, data collection, and AI functionality organized into separate Python modules.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web dashboard |
| Requests | HTTP requests and API communication |
| Beautiful Soup | HTML parsing and web scraping |
| OpenAI-Compatible API | Large language model integration |
| uv | Dependency and environment management |

## 🏗️ Project Structure

```text
Marketmind/
├── src/
│   └── marketmind/
│       ├── __init__.py
│       ├── main.py
│       └── APIs/
│           ├── prices.py
│           └── ...
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
├── LICENSE
└── README.md
```

*Note: This is a simplified overview of the project structure. Additional modules may be present in the repository.*

## ⚡ Getting Started

### Prerequisites

- Python 3.13 or later
- [uv](https://docs.astral.sh/uv/)
- API credentials required by your configured data providers and LLM service

### 1. Clone the Repository

```bash
git clone https://github.com/SalehSepasi/Marketmind.git
cd Marketmind
```

### 2. Install Dependencies

```bash
uv sync
```

This command installs the project's dependencies and prepares the virtual environment.

### 3. Configure API Credentials

Create a `.env` file in the project root and add the credentials required by your implementation.

```env
# Add the environment variables required by your APIs
```

Use the exact variable names expected by your code. Keep your API keys and other secrets private, and never commit them to GitHub.

### 4. Launch MarketMind

```bash
uv run streamlit run src/marketmind/main.py
```

Open the local URL displayed in your terminal to access the dashboard.

## 🔍 How It Works

1. **Choose a Cryptocurrency** — Select the digital asset you want to explore.
2. **Collect Market Information** — Retrieve available price data, relevant news, and public community posts.
3. **Define Your Analysis** — Enter a custom prompt describing what you want the AI to investigate.
4. **Generate Insights** — Send the collected information and your prompt to the configured language model.
5. **Explore the Results** — Review the generated analysis directly in the interactive dashboard.

The results depend on the quality and availability of the collected data, the capabilities of the selected model, and the clarity of your prompt.

## ⚠️ Limitations

- Data availability depends on external APIs, service restrictions, and rate limits.
- Community discussions reflect individual opinions and do not necessarily represent the broader cryptocurrency market.
- AI-generated responses may contain inaccuracies, assumptions, or unsupported conclusions.
- MarketMind does not guarantee the accuracy of its analysis or predict future market movements.

## ⚖️ Disclaimer

MarketMind is an educational and analytical software project. It does not provide financial advice, investment recommendations, or guaranteed predictions. Always verify important information independently and make financial decisions based on your own research.

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
