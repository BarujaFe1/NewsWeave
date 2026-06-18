from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, func
from app.database import Base


class Briefing(Base):
    __tablename__ = "briefings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    date = Column(DateTime, server_default=func.now())
    top_articles = Column(JSON, default=list)
    radar_bullets = Column(JSON, default=list)
    stoic_quote = Column(String, nullable=True)
