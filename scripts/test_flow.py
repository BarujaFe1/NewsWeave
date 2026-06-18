"""Test the full NewsWeave flow."""
import requests
import sys
import os

os.environ["PYTHONIOENCODING"] = "utf-8"

BASE = "http://127.0.0.1:8001"

# 1. Test health
r = requests.get(f"{BASE}/api/health")
assert r.status_code == 200, f"Health check failed: {r.text}"
print("[OK] Health check")

# 2. Create profile
profile = {
    "location": "Sao Carlos",
    "follow_football": True,
    "football_team": "Corinthians",
    "tech_enthusiast": True,
    "follow_ai": True,
    "follow_stocks": True,
    "follow_crypto": True,
    "follow_longevity": True,
    "tone_preference": "casual",
    "use_emojis": True,
    "stoic_quotes": True,
    "language": "pt-BR",
}
r = requests.post(f"{BASE}/api/profile", json=profile)
assert r.status_code == 200, f"Profile creation failed: {r.text}"
user_id = r.json()["id"]
print(f"[OK] Profile created: ID {user_id}")

# 3. Get profile
r = requests.get(f"{BASE}/api/profile/{user_id}")
assert r.status_code == 200
print(f"[OK] Profile retrieved: {r.json()['location']}")

# 4. Ingest RSS
print("  [..] Ingesting RSS feeds (may take a while)...")
r = requests.post(f"{BASE}/api/ingest")
if r.status_code != 200:
    print(f"  [ER] Ingest error: {r.text[:200]}")
    sys.exit(1)
data = r.json()
print(f"[OK] Ingest complete: {data['articles']} articles")

# 5. Get briefing
r = requests.get(f"{BASE}/api/briefing/today?user_id={user_id}")
assert r.status_code == 200, f"Briefing failed: {r.text}"
briefing = r.json()
print(f"[OK] Briefing generated!")
print(f"  Greeting: {briefing['greeting']}")
print(f"  Top 15: {len(briefing['top_15'])} articles")
print(f"  Radar: {len(briefing['radar'])} bullets")

if briefing["top_15"]:
    for art in briefing["top_15"][:3]:
        print(f"    #{art['rank']} [{art['category']}] {art['title'][:60]}...")

if briefing.get("stoic_quote"):
    print(f"  Stoic quote: {briefing['stoic_quote'][:60]}...")

# 6. Briefing history
r = requests.get(f"{BASE}/api/briefing/history?user_id={user_id}")
assert r.status_code == 200
history = r.json()
print(f"[OK] Briefing history: {len(history)} entries")

print("\n[PASS] ALL TESTS PASSED!")
