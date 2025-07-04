import os

# Get absolute path to this script's folder
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


import requests
import pandas as pd
import sys
from collections import defaultdict

def fetch_submissions(handle):
    url = f"https://codeforces.com/api/user.status?handle={handle}&from=1&count=10000"
    res = requests.get(url)
    data = res.json()
    
    if data["status"] != "OK":
        raise Exception("Error fetching submission data")
    
    submissions = data["result"]
    problems = []
    seen = set()
    
    for sub in submissions:
        prob = sub.get("problem", {})
        key = f"{prob.get('contestId')}-{prob.get('index')}"
        
        if key in seen:
            continue
        seen.add(key)
        
        problems.append({
            "name": prob.get("name", ""),
            "contestId": prob.get("contestId", ""),
            "index": prob.get("index", ""),
            "tags": ";".join(prob.get("tags", [])),
            "verdict": sub.get("verdict", ""),
            "url": f"https://codeforces.com/problemset/problem/{prob.get('contestId')}/{prob.get('index')}"
        })
    
    return problems

def calculate_tag_accuracy(problems):
    tag_stats = defaultdict(lambda: {"solved": 0, "total": 0})
    
    for prob in problems:
        tags = prob["tags"].split(";")
        solved = prob["verdict"] == "OK"
        
        for tag in tags:
            if tag.strip() == "":
                continue
            tag_stats[tag]["total"] += 1
            if solved:
                tag_stats[tag]["solved"] += 1
    
    rows = []
    for tag, stats in tag_stats.items():
        total = stats["total"]
        solved = stats["solved"]
        accuracy = round((solved / total) * 100, 2) if total > 0 else 0
        rows.append({
            "tag": tag,
            "solved": solved,
            "total": total,
            "accuracy (%)": accuracy
        })
    
    return pd.DataFrame(rows).sort_values(by="accuracy (%)")

def main():
    if len(sys.argv) < 2:
        print("❌ Usage: python main.py <codeforces_handle>")
        return
    
    handle = sys.argv[1]
    print(f"🔍 Analyzing profile for: {handle}")
    
    try:
        problems = fetch_submissions(handle)
        df = pd.DataFrame(problems)
        df.to_csv(os.path.join(BASE_DIR, "user_submissions.csv"), index=False)
        print("✅ Submission data saved to user_submissions.csv")
        
        tag_df = calculate_tag_accuracy(problems)
        tag_df.to_csv(os.path.join(BASE_DIR, "tag_accuracy.csv"), index=False)
        print("✅ Tag accuracy stats saved to tag_accuracy.csv")
    
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    main()
