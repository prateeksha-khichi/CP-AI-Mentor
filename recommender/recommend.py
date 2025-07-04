import requests
import pandas as pd

# === CONFIG ===
HANDLE = "stickydough"
WEAK_TAGS = ["trees", "dp"]
RATING_RANGE = (800, 1400)

# === Load user submissions ===
user_df = pd.read_csv(r"C:\Users\gungu\OneDrive\Desktop\ai-mentor\profile\user_submissions.csv")
solved_problems = set(user_df[user_df["solved"] == True]["problem_id"].values)

# === Fetch full problemset ===
print("Fetching problemset...")
response = requests.get("https://codeforces.com/api/problemset.problems")
all_problems = response.json()["result"]["problems"]

recommended = []

for prob in all_problems:
    tags = prob.get("tags", [])
    rating = prob.get("rating", None)
    contestId = prob.get("contestId", None)
    index = prob.get("index", None)
    name = prob.get("name", "")
    
    if not contestId or not index or not rating:
        continue

    problem_id = f"{contestId}-{index}"
    
    if problem_id in solved_problems:
        continue  # already solved

    # Check rating range
    if not (RATING_RANGE[0] <= rating <= RATING_RANGE[1]):
        continue

    # Check if any weak tag is present
    if any(tag in tags for tag in WEAK_TAGS):
        url = f"https://codeforces.com/problemset/problem/{contestId}/{index}"
        recommended.append({
            "name": name,
            "contestId": contestId,
            "index": index,
            "rating": rating,
            "tags": ", ".join(tags),
            "url": url
        })

# === Save recommended problems ===
df = pd.DataFrame(recommended).sort_values(by="rating")
df.to_csv("recommended_problems.csv", index=False)

print(f"✅ {len(df)} problems recommended and saved to recommended_problems.csv")
