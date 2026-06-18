"""Popula fontes RSS padrão no banco de dados."""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.app.database import SessionLocal, engine, Base
from backend.app.models.article import Article

SOURCES_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sources.json")


def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    with open(SOURCES_PATH, "r", encoding="utf-8") as f:
        sources = json.load(f)

    print(f"Fontes carregadas: {sum(len(v) for v in sources.values())} feeds em {len(sources)} categorias")
    for cat, urls in sources.items():
        for url in urls:
            print(f"  [{cat}] {url}")

    db.close()
    print("\nPronto para ingerir! Execute POST /api/ingest")


if __name__ == "__main__":
    seed()
