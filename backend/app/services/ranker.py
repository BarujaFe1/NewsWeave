from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.article import Article
from app.models.user import User
from app.services.deduplicator import deduplicate_articles

# Keywords are now tied to a user preference flag, so the bonus is only
# applied when the user actually opted into that topic. Previously every
# keyword group fired for every user, making the "personalized" ranking
# effectively global.
KEYWORDS_BY_PREF: dict[str, list[str]] = {
    "follow_crypto": ["Bitcoin", "Ethereum", "Solana", "altcoin", "memecoin", "degen"],
    "follows_gta": ["GTA VI", "GTA 6", "Grand Theft Auto", "Rockstar"],
    "follows_lol": ["League of Legends", "CBLOL", "LoL"],
    "follows_fps": ["CS2", "Valorant", "Counter-Strike", "Call of Duty"],
    "follows_rpg": ["Elden Ring", "Baldur's Gate", "RPG", "world-building"],
    "follow_ai": ["Inteligência Artificial", "IA", "GPT", "Claude", "Gemini", "machine learning"],
    "follow_biotech": ["BioTech", "GLP-1", "Ozempic", "longevidade", "biohacking"],
    "follow_reits": ["FII", "Fundos Imobiliários", "dividendos"],
    "follow_stf": ["STF", "Supremo", "ministros"],
    "follow_economy": ["fiscal", "câmbio", "BC", "Selic", "inflação", "dólar"],
}

# Team-specific vocabulary only fires for users who declared that team.
TEAM_KEYWORDS: dict[str, list[str]] = {
    "Corinthians": ["Corinthians", "Timão", "Mosqueto", "Garro", "Yuri Alberto"],
}

# Window used to keep the briefing "daily". If too few articles fall inside
# the window (e.g. first run with a cold feed), we fall back to all articles
# so the demo never renders an empty briefing.
RECENT_WINDOW_HOURS = 48
MIN_RECENT_CANDIDATES = 30


def category_bias(user: User) -> dict[str, int]:
    bias: dict[str, int] = {}
    if user.follow_football or user.follow_tennis or user.follow_formula1 or user.follow_esports:
        bias["esportes"] = 30
    if user.follow_stf or user.follow_brasilia:
        bias["politica"] = 30
    # crypto maps onto the "economia" category (there is no dedicated
    # "cryptocurrency" feed in sources.json), so a crypto-only investor no
    # longer has all economy news suppressed.
    if user.follow_stocks or user.follow_macro or user.follow_crypto or user.follow_economy:
        bias["economia"] = 30
    if user.tech_enthusiast or user.follow_ai:
        bias["tech"] = 30
    if user.follows_gta or user.follows_lol or user.follows_fps or user.follows_rpg:
        bias["games"] = 30
    if user.follow_longevity or user.biohacker:
        bias["saude"] = 30
    return bias


def ignore_list(user: User) -> list[str]:
    ignored: list[str] = []
    if not (user.follow_football or user.follow_tennis or user.follow_formula1 or user.follow_esports):
        ignored.append("esportes")
    if not (user.follow_stf or user.follow_brasilia):
        ignored.append("politica")
    if not (user.follow_stocks or user.follow_macro or user.follow_crypto or user.follow_economy):
        ignored.append("economia")
    if not (user.tech_enthusiast or user.follow_ai):
        ignored.append("tech")
    if not (user.follows_gta or user.follows_lol or user.follows_fps or user.follows_rpg):
        ignored.append("games")
    if not (user.follow_longevity or user.biohacker):
        ignored.append("saude")
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

    # Team substring match + team-specific vocabulary, only for the declared team.
    team = user.football_team
    if team and team.lower() in title_lower:
        score += 20
    if team:
        for kw in TEAM_KEYWORDS.get(team, []):
            if kw.lower() in title_lower:
                score += 15
                break

    # Preference-gated keyword bonuses: only the topics the user opted into.
    for pref, kws in KEYWORDS_BY_PREF.items():
        if not getattr(user, pref, False):
            continue
        for kw in kws:
            if kw.lower() in title_lower:
                score += 15
                break

    published = article.get("published_at")
    if published:
        # feedparser stores naive UTC; compare against naive local now for the demo.
        published_dt = published.replace(tzinfo=None) if published.tzinfo else published
        if datetime.now() - published_dt < timedelta(hours=6):
            score += 10

    return score


def _candidate_articles(db: Session) -> list[Article]:
    """Prefer articles published within the recent window; fall back to all
    when the window is too sparse so the demo never renders an empty briefing."""
    window_start = datetime.now() - timedelta(hours=RECENT_WINDOW_HOURS)
    recent = db.query(Article).filter(Article.published_at >= window_start).all()
    if len(recent) >= MIN_RECENT_CANDIDATES:
        return recent
    return db.query(Article).all()


def rank_articles_for_user(db: Session, user: User) -> list[dict]:
    articles = _candidate_articles(db)
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
