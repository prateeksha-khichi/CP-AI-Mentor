import os
import requests
from dotenv import load_dotenv

# Load API Key from .env
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

# Model options: 'mistralai/mixtral-8x7b', 'meta-llama/llama-3-70b-instruct', 'anthropic/claude-3-opus'
MODEL = "meta-llama/llama-3-70b-instruct"


def get_openrouter_response(prompt):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful competitive programming mentor."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {e}\n\nFull response: {response.text}"

def generate_explanation_and_quiz(topic):
    prompt = f"""
Explain the topic '{topic}' in simple terms for a beginner in competitive programming.
Then generate:
1. One multiple choice question (MCQ)
2. One fill-in-the-blank question

Format:
### Explanation:
...

### Quiz:
1. MCQ: ...
   a) ...
   b) ...
   c) ...
   d) ...
   Answer: [...]

2. Fill in the blank:
"..."
Answer: [...]
"""
    return get_openrouter_response(prompt)

# ======= Test Script ========
if __name__ == "__main__":
    weak_topics = ["trees", "dp", "bitmasks"]
    for topic in weak_topics:
        print(f"\n🧠 Topic: {topic.upper()}")
        result = generate_explanation_and_quiz(topic)
        print(result)
        print("=" * 80)
