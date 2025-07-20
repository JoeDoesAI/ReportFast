from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

from app.config import TEMPLATES_DIR, STATIC_DIR
from app.services.news_service import fetch_top_headlines, search_news

app = FastAPI()

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request, q: str = Query(default=None)):
    # if q:
    #     news_articles = search_news(query=q)
    # else:
    news_articles = fetch_top_headlines(country="us")
    return templates.TemplateResponse("base.html", {"request": request, "news": news_articles})
