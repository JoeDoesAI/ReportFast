import requests
from fastapi import APIRouter
from app.crud.article_crud import get_articles_by_category, search_for_news
from fastapi.responses import JSONResponse
from app.core.database import SessionLocal
from app.services.news_service import search_api_news
from app.crud.article_crud import save_article
from app.services.date_parser import parse_datetime


router = APIRouter(prefix="/news", tags=["News"])




@router.get("/{category}")
def get_news_by_category(category: str):
    db = SessionLocal()
    
    articles = get_articles_by_category(db,category)
    
    return JSONResponse(content=[{
        "news_title": a.news_title,
        "news_url": a.news_url,
        "url_to_image": a.url_to_image,
    } for a in articles])
    

@router.get("/search/{query}")
def search_news(query: str):
    
    db = SessionLocal()
    articles = search_for_news(db,query)
    
    if not articles:
        try:   
            articles = search_api_news(query)
            
            fetched = []

            for article in articles:
                article_data = {
                    "news_title": article.get("title"),
                    "news_description": article.get("description"),
                    "url_to_image": article.get("urlToImage"),
                    "news_url": article.get("url"),
                    "published_at": parse_datetime(article.get("publishedAt")),
                    "news_category": "general"
                }
                
                fetched.append(article_data)
                save_article(db, article_data)
            return JSONResponse(content=fetched, media_type="application/json")
        
        except requests.exceptions.ConnectionError:
            print("Connection error occurred while fetching news.")
        
    return JSONResponse(content=[{
        "news_title": a.news_title,
        "news_url": a.news_url,
        "url_to_image": a.url_to_image 
    } for a in articles])
