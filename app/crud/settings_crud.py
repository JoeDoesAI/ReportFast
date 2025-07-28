from sqlalchemy.orm import Session
from app.models.settings import AppSetting
from datetime import date

def get_last_run_date(db: Session) -> date | None:
    setting = db.query(AppSetting).filter(AppSetting.key == "last_run_date").first()
    return setting.last_run_date if setting else None

def update_last_run_date(db: Session, new_date: date):
    setting = db.query(AppSetting).filter(AppSetting.key == "last_run_date").first()
    if setting:
        setting.last_run_date = new_date
    else:
        setting = AppSetting(key="last_run_date", last_run_date=new_date)
        db.add(setting)
    db.commit()
    db.refresh(setting)
    return setting


