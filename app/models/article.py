from sqlalchemy import Column, Integer, String, Text, DateTime
from app.core.database import Base
from datetime import datetime



class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    url = Column(String, unique=True, nullable=False)
    url_to_image = Column(String, nullable=True)
    published_at = Column(DateTime)
    source = Column(String, nullable=True)
    category = Column(String, nullable=True)
