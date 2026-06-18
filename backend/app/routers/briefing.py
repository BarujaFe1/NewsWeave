from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.services.ranker import rank_articles_for_user
from app.services.generator import build_briefing

router = APIRouter()


@router.get("/briefing/today")
def get_today_briefing(user_id: int = Query(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    briefing = build_briefing(db, user)
    return briefing


@router.get("/briefing/history")
def get_briefing_history(user_id: int = Query(...), db: Session = Depends(get_db)):
    from app.models.briefing import Briefing
    history = (
        db.query(Briefing)
        .filter(Briefing.user_id == user_id)
        .order_by(Briefing.date.desc())
        .limit(10)
        .all()
    )
    return [
        {
            "id": b.id,
            "date": b.date.isoformat() if b.date else None,
            "top_count": len(b.top_articles) if b.top_articles else 0,
        }
        for b in history
    ]
