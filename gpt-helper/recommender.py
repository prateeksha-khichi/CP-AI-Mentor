import requests
import random

def fetch_codeforces_problems():
    url = "https://codeforces.com/api/problemset.problems"
    try:
        res = requests.get(url)
        data = res.json()
        if data["status"] != "OK":
            return []
        problems = data["result"]["problems"]
        return problems
    except Exception as e:
        print("❌ Error fetching problems:", e)
        return []

def recommend_problems(tag, count=2):
    problems = fetch_codeforces_problems()
    tagged = [p for p in problems if "tags" in p and tag.lower() in map(str.lower, p["tags"])]
    
    if not tagged:
        return []

    chosen = random.sample(tagged, min(count, len(tagged)))
    result = []
    for prob in chosen:
        name = prob.get("name", "Unknown Problem")
        contestId = prob.get("contestId", "0")
        index = prob.get("index", "A")
        url = f"https://codeforces.com/problemset/problem/{contestId}/{index}"
        result.append({
            "name": name,
            "url": url
        })
    return result
