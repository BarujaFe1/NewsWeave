import random
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.user import User
from app.models.briefing import Briefing
from app.services.ranker import rank_articles_for_user

STOIC_QUOTES = [
    "A sorte favorece a mente preparada. — Sêneca",
    "Não é o que acontece com você, mas como você reage que importa. — Epicteto",
    "Você tem poder sobre sua mente — não sobre eventos externos. — Marco Aurélio",
    "A felicidade da sua vida depende da qualidade dos seus pensamentos. — Marco Aurélio",
    "O obstáculo é o caminho. — Marco Aurélio",
    "Nós sofremos mais na imaginação do que na realidade. — Sêneca",
    "Comece. A metade de qualquer jornada está em dar o primeiro passo. — Sêneca",
    "A vida não é boa nem má, mas um campo para o bem e o mal. — Sêneca",
]


def build_briefing(db: Session, user: User) -> dict:
    ranked = rank_articles_for_user(db, user)

    top_15 = []
    for i, art in enumerate(ranked[:15]):
        top_15.append({
            "rank": i + 1,
            "title": art["title"],
            "link": art["link"],
            "summary": art["summary"],
            "category": art["category"],
            "source": art["source"],
            "published_at": art["published_at"].isoformat() if art["published_at"] else None,
            "relevance_score": round(art["score"], 1),
        })

    radar = []
    for art in ranked[15:65]:
        radar.append({
            "title": art["title"],
            "link": art["link"],
            "category": art["category"],
        })

    stoic_quote = None
    if user.stoic_quotes:
        stoic_quote = random.choice(STOIC_QUOTES)

    briefing_entry = Briefing(
        user_id=user.id,
        top_articles=top_15,
        radar_bullets=radar,
        stoic_quote=stoic_quote,
    )
    db.add(briefing_entry)
    db.commit()

    return {
        "user_id": user.id,
        "date": datetime.now().isoformat(),
        "greeting": f"Bom dia, {user.name or 'Assinante'}",
        "stoic_quote": stoic_quote,
        "top_15": top_15,
        "radar": radar,
    }
