from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import get_db
from app.models.user import User

router = APIRouter()


class UserProfileSchema(BaseModel):
    location: str = ""
    religion: str | None = None
    music_taste: list[str] = []
    football_team: str | None = None
    follow_football: bool = False
    follow_tennis: bool = False
    follow_formula1: bool = False
    follow_esports: bool = False
    political_lean: str = "none"
    follow_brasilia: bool = False
    follow_stf: bool = False
    follow_economy: bool = False
    investor_profile: str = "conservative"
    follow_crypto: bool = False
    follow_stocks: bool = False
    follow_macro: bool = False
    follow_biotech: bool = False
    follow_reits: bool = False
    tech_enthusiast: bool = False
    pc_gamer: bool = False
    follow_ai: bool = False
    follow_startups: bool = False
    follow_smartphones: bool = False
    follows_gta: bool = False
    follows_lol: bool = False
    follows_fps: bool = False
    follows_rpg: bool = False
    biohacker: bool = False
    follow_longevity: bool = False
    follow_nutrition: bool = False
    follow_fitness: bool = False
    tone_preference: str = "casual"
    use_emojis: bool = True
    use_gifs: bool = False
    stoic_quotes: bool = False
    language: str = "pt-BR"
    city: str | None = None
    follow_local_news: bool = False
    follow_science: bool = False
    follow_environment: bool = False
    follow_crime: bool = False
    follow_culture: bool = False
    follow_streaming: bool = False
    follow_movies: bool = False
    follow_music_news: bool = False


@router.post("/profile")
def create_profile(data: UserProfileSchema, db: Session = Depends(get_db)):
    user = User(**data.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "message": "Perfil criado com sucesso"}


@router.get("/profile/{user_id}")
def get_profile(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user
