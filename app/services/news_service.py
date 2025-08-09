import requests

from app.services.date_parser import parse_datetime
from app.core.config import NEWS_API_KEY
from apscheduler.schedulers.background import BackgroundScheduler
from app.core.database import SessionLocal
from app.crud.article_crud import save_article

db = SessionLocal()

scheduler = BackgroundScheduler()

BASE_URL = "https://newsapi.org/v2"



def fetch_top_headlines(category: str, country: str = "us", page_size: int = 20):
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

def save_all_news(categories):
    for category in categories:
        articles = fetch_top_headlines(category=category)
        
        for article in articles:
            article_data = {
                "news_title": article.get("title"),
                "news_description": article.get("description"),
                "url_to_image": article.get("urlToImage"),
                "news_url": article.get("url"),
                "published_at": parse_datetime(article.get("publishedAt")),
                "news_category": category
            }
            save_article(db, article_data)
    db.close()

    
def search_api_news(query, page_size=10):
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



