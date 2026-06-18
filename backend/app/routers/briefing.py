from datetime import datetime, timezone
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.briefing import Briefing
from app.services.generator import build_briefing, shape_briefing_response

router = APIRouter()


@router.get("/briefing/today")
def get_today_briefing(user_id: int = Query(...), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    # Idempotency: if a briefing already exists for today (UTC calendar date),
    # reuse it instead of creating a new one on every call.
    latest = (
        db.query(Briefing)
        .filter(Briefing.user_id == user_id)
        .order_by(Briefing.date.desc())
        .first()
    )
    today_utc = datetime.now(timezone.utc).date()
    if latest and latest.date:
        latest_date = latest.date
        if latest_date.tzinfo is None:
            latest_date = latest_date.replace(tzinfo=timezone.utc)
        if latest_date.date() == today_utc:
            return shape_briefing_response(latest, user)

    return build_briefing(db, user)


@router.get("/briefing/history")
def get_briefing_history(user_id: int = Query(...), db: Session = Depends(get_db)):
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
