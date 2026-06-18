from sqlalchemy import Column, Integer, String, DateTime, Float, func
from app.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    link = Column(String, unique=True, nullable=False)
    source = Column(String, nullable=True)
    summary = Column(String, nullable=True)
    content = Column(String, nullable=True)
    category = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    content_hash = Column(String, nullable=True)
