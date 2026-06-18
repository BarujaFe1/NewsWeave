"""List configured RSS sources.

This script only lists the feeds configured in data/sources.json. It does NOT
seed the database. To populate demo article data, use:

    python scripts/seed_demo.py

Use this utility to verify which categories and feeds will be hit by
`POST /api/ingest`.
"""
import json
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

SOURCES_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "sources.json")


def list_sources():
    with open(SOURCES_PATH, "r", encoding="utf-8") as f:
        sources = json.load(f)

    print(f"Configured sources: {sum(len(v) for v in sources.values())} feeds across {len(sources)} categories\n")
    for cat, urls in sources.items():
        print(f"[{cat}]")
        for url in urls:
            print(f"  - {url}")
        print()

    print("These feeds are fetched by `POST /api/ingest`.")
    print("To populate synthetic demo data instead, run: python scripts/seed_demo.py")


if __name__ == "__main__":
    list_sources()