from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date
from app.crud.settings_crud import get_last_run_date, update_last_run_date
from app.services.news_service import save_all_news
from app.core.database import SessionLocal

scheduler = BackgroundScheduler()

def scheduled_job():
    db = SessionLocal()
    today = date.today()

    last_run = get_last_run_date(db)
    if last_run == today:
        print("Already fetched News today. Skipping...")
        db.close()
        return

    print("Fetching news automatically...")
    
    categories = ["business", "entertainment", "general", "health", "science", "sports", "technology"]
    save_all_news(categories)

    update_last_run_date(db, today)
    db.close()

def start_scheduler():
    scheduled_job()  
    scheduler.add_job(scheduled_job, "cron", hour=0, minute=0)
    scheduler.start()
    

def stop_scheduler():
    scheduler.shutdown()
    print("Scheduler stopped.")
