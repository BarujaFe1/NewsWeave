from datetime import datetime, timezone, timedelta
from sqlalchemy.orm import Session
from app.models.article import Article
from app.models.user import User
from app.services.deduplicator import deduplicate_articles

KEYWORDS_MAP = {
    "corinthians": ["Corinthians", "Timão", "Mosqueto", "Garro", "Yuri Alberto"],
    "crypto": ["Bitcoin", "Ethereum", "Solana", "altcoin", "memecoin", "degen"],
    "gta": ["GTA VI", "GTA 6", "Grand Theft Auto", "Rockstar"],
    "lol": ["League of Legends", "CBLOL", "LoL"],
    "fps": ["CS2", "Valorant", "Counter-Strike", "Call of Duty"],
    "rpg": ["Elden Ring", "Baldur's Gate", "RPG", "world-building"],
    "ai": ["Inteligência Artificial", "IA", "GPT", "Claude", "Gemini", "machine learning"],
    "biotech": ["BioTech", "GLP-1", "Ozempic", "longevidade", "biohacking"],
    "fii": ["FII", "Fundos Imobiliários", "dividendos"],
    "stf": ["STF", "Supremo", "ministro"],
    "economia": ["fiscal", "câmbio", "BC", "Selic", "inflação", "dólar"],
}


def category_bias(user: User) -> dict[str, int]:
    bias = {}
    if user.follow_football: bias["esportes"] = 30
    if user.follow_stf or user.follow_brasilia: bias["politica"] = 30
    if user.follow_stocks or user.follow_macro: bias["economia"] = 30
    if user.follow_crypto: bias["cryptocurrency"] = 30
    if user.tech_enthusiast or user.follow_ai: bias["tech"] = 30
    if user.follows_gta or user.follows_lol or user.follows_fps: bias["games"] = 30
    if user.follow_longevity or user.biohacker: bias["saude"] = 30
    return bias


def ignore_list(user: User) -> list[str]:
    ignored = []
    if not user.follow_football: ignored.append("esportes")
    if not user.follow_stf: ignored.append("politica")
    if not user.follow_stocks and not user.follow_crypto: ignored.append("economia")
    if not user.tech_enthusiast: ignored.append("tech")
    if not user.follows_gta and not user.follows_lol: ignored.append("games")
    if not user.follow_longevity: ignored.append("saude")
    return ignored


def score_article(article: dict, user: User, bias: dict[str, int], ignore: list[str]) -> float:
    score = 100.0
    cat = (article.get("category") or "").lower()

    if cat in ignore:
        score -= 30

    if cat in bias:
        score += bias[cat]

    title = (article.get("title") or "") + " " + (article.get("summary") or "")
    title_lower = title.lower()

    team = user.football_team
    if team and team.lower() in title_lower:
        score += 20

    for kw_group in KEYWORDS_MAP.values():
        for kw in kw_group:
            if kw.lower() in title_lower:
                score += 15
                break

    published = article.get("published_at")
    if published:
        now = datetime.now(timezone.utc)
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)
        if now - published < timedelta(hours=6):
            score += 10

    return score


def rank_articles_for_user(db: Session, user: User) -> list[dict]:
    articles = db.query(Article).all()
    bias = category_bias(user)
    ignore = ignore_list(user)

    scored = []
    for art in articles:
        art_dict = {
            "id": art.id,
            "title": art.title,
            "link": art.link,
            "summary": art.summary,
            "category": art.category,
            "source": art.source,
            "published_at": art.published_at,
            "content_hash": art.content_hash,
        }
        art_dict["score"] = score_article(art_dict, user, bias, ignore)
        scored.append(art_dict)

    scored.sort(key=lambda x: x["score"], reverse=True)
    return deduplicate_articles(scored)
