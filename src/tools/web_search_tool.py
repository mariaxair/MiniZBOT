from agno.tools import tool
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # loads SERPAPI_API_KEY from .env

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

@tool
def web_search_tool(query: str) -> str:
    """
    Search the web using SerpAPI and return the top 3 results.
    """
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "engine": "google",
        "api_key": SERPAPI_KEY,
        "num": 3  # number of results
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    # SerpAPI returns results in data["organic_results"]
    results = []
    for item in data.get("organic_results", []):
        title = item.get("title", "")
        snippet = item.get("snippet", "")
        link = item.get("link", "")
        results.append(f"{title}\n{snippet}\n{link}")

    return "\n\n".join(results)
