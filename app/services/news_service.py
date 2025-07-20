import requests
from app.config import NEWS_API_KEY

BASE_URL = "https://newsapi.org/v2"

def fetch_top_headlines(country="us", category="technology", page_size=10):
    url = f"{BASE_URL}/top-headlines"
    params = {
        "country": country,
        "category": category,
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise error if request fails
    data = response.json()
    return data.get("articles", [])



def search_news(query, page_size=10):
    url = f"{BASE_URL}/everything"
    params = {
        "q": query,
        "pageSize": page_size,
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data.get("articles", [])
