from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse,JSONResponse

from app.config import TEMPLATES_DIR, STATIC_DIR
from app.services.news_service import fetch_top_headlines, search_news

app = FastAPI()


templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


@app.get("/", response_class=HTMLResponse)
def home(request: Request, q: str = Query(default=None)):
    
    news_articles = fetch_top_headlines(country="us",category="business")
    return templates.TemplateResponse("base.html", {"request": request, "news": news_articles})


@app.get("/api/news")
def get_news(category: str = Query(default="technology")):
    news_articles = fetch_top_headlines(category=category)
    return {"articles": news_articles}