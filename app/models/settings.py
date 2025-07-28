from sqlalchemy import Column, Integer, String, Text, Date
from app.core.database import Base
from datetime import datetime




class AppSetting(Base):
    __tablename__ = "app_settings"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    value = Column(String)
    last_run_date = Column(Date, nullable=True)