from fastapi import APIRouter
from app.crud.article_crud import get_articles_by_category, search_for_news
from fastapi.responses import JSONResponse
from app.core.database import SessionLocal

router = APIRouter(prefix="/news", tags=["News"])

@router.get("/{category}")
def get_news_by_category(category: str):
    db = SessionLocal()
    
    articles = get_articles_by_category(db,category)
    
    return JSONResponse(content=[{
        "title": a.title,
        "url": a.url,
        "image": a.url_to_image
    } for a in articles])
    

@router.get("/search/{query}")
def search_news(query: str):
    
    db = SessionLocal()
    articles = search_for_news(db,query)
    
    return JSONResponse(content=[{
        "title": a.title,
        "url": a.url,
        "image": a.url_to_image
    } for a in articles])