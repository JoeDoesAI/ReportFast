from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from contextlib import asynccontextmanager


from app.models.article import Article
from app.core.database import SessionLocal
from app.routers.news import router
from app.core.config import TEMPLATES_DIR, STATIC_DIR
from app.core.database import Base, engine
from app.core.scheduler import start_scheduler, stop_scheduler


Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    start_scheduler()
    yield
    stop_scheduler()

app = FastAPI(lifespan=lifespan)

app.include_router(router)

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    db = SessionLocal()

    try:
        articles = db.query(Article).order_by(Article.published_at.desc()).limit(20).all()
    finally:
        db.close()

    return templates.TemplateResponse(
        "base.html",
        {"request": request, "articles": articles}
    )

