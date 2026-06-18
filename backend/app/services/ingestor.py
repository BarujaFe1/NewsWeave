import json
import os
import hashlib
import feedparser
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.article import Article

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
SOURCES_PATH = os.path.join(PROJECT_ROOT, "data", "sources.json")


def load_sources():
    with open(SOURCES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def content_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()[:16]


def fetch_feed(url: str, category: str) -> list[dict]:
    feed = feedparser.parse(url)
    articles = []
    for entry in feed.entries[:50]:
        title = entry.get("title", "")
        link = entry.get("link", "")
        summary = entry.get("summary", "") or entry.get("description", "") or ""
        published = entry.get("published_parsed")
        pub_date = datetime(*published[:6]) if published else datetime.now()
        articles.append({
            "title": title,
            "link": link,
            "summary": summary[:500],
            "category": category,
            "source": feed.feed.get("title", url),
            "published_at": pub_date,
            "content_hash": content_hash(title + summary[:200]),
        })
    return articles


def ingest_all_sources(db: Session) -> int:
    sources = load_sources()
    total = 0
    for category, urls in sources.items():
        for url in urls:
            try:
                articles = fetch_feed(url, category)
                for art in articles:
                    existing = db.query(Article).filter(Article.link == art["link"]).first()
                    if not existing:
                        db.add(Article(**art))
                        total += 1
                db.commit()
            except Exception as e:
                print(f"Erro ao ingerir {url}: {e}")
    return total
