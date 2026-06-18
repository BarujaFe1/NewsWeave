import Levenshtein


def is_duplicate(title1: str, title2: str, threshold: float = 0.85) -> bool:
    if not title1 or not title2:
        return False
    distance = Levenshtein.ratio(title1.lower(), title2.lower())
    return distance > threshold


def deduplicate_articles(articles: list[dict]) -> list[dict]:
    seen = []
    result = []
    for art in articles:
        title = art.get("title", "")
        dup = False
        for s in seen:
            if is_duplicate(title, s):
                dup = True
                break
        if not dup:
            seen.append(title)
            result.append(art)
    return result
