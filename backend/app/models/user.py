from sqlalchemy import Column, Integer, String, Boolean, JSON, DateTime, func
from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, default="Assinante")
    created_at = Column(DateTime, server_default=func.now())

    location = Column(String, default="")
    religion = Column(String, nullable=True)
    music_taste = Column(JSON, default=list)

    football_team = Column(String, nullable=True)
    follow_football = Column(Boolean, default=False)
    follow_tennis = Column(Boolean, default=False)
    follow_formula1 = Column(Boolean, default=False)
    follow_esports = Column(Boolean, default=False)

    political_lean = Column(String, default="none")
    follow_brasilia = Column(Boolean, default=False)
    follow_stf = Column(Boolean, default=False)
    follow_economy = Column(Boolean, default=False)

    investor_profile = Column(String, default="conservative")
    follow_crypto = Column(Boolean, default=False)
    follow_stocks = Column(Boolean, default=False)
    follow_macro = Column(Boolean, default=False)
    follow_biotech = Column(Boolean, default=False)
    follow_reits = Column(Boolean, default=False)

    tech_enthusiast = Column(Boolean, default=False)
    pc_gamer = Column(Boolean, default=False)
    follow_ai = Column(Boolean, default=False)
    follow_startups = Column(Boolean, default=False)
    follow_smartphones = Column(Boolean, default=False)

    follows_gta = Column(Boolean, default=False)
    follows_lol = Column(Boolean, default=False)
    follows_fps = Column(Boolean, default=False)
    follows_rpg = Column(Boolean, default=False)

    biohacker = Column(Boolean, default=False)
    follow_longevity = Column(Boolean, default=False)
    follow_nutrition = Column(Boolean, default=False)
    follow_fitness = Column(Boolean, default=False)

    tone_preference = Column(String, default="casual")
    use_emojis = Column(Boolean, default=True)
    use_gifs = Column(Boolean, default=False)
    stoic_quotes = Column(Boolean, default=False)
    language = Column(String, default="pt-BR")

    city = Column(String, nullable=True)
    follow_local_news = Column(Boolean, default=False)
    follow_science = Column(Boolean, default=False)
    follow_environment = Column(Boolean, default=False)
    follow_crime = Column(Boolean, default=False)
    follow_culture = Column(Boolean, default=False)
    follow_streaming = Column(Boolean, default=False)
    follow_movies = Column(Boolean, default=False)
    follow_music_news = Column(Boolean, default=False)
