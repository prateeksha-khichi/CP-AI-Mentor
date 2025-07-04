import sys
import os
import datetime

# Add parent (gpt-helper/) to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Add recommender folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "recommender")))

from explain import generate_explanation_and_quiz
from recommender import recommend_problems

import streamlit as st
import subprocess
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Streamlit UI
st.set_page_config(page_title="AI CP Mentor", layout="wide")
st.title("🤖 AI CP Mentor - Personalized Codeforces Assistant")

st.markdown("🚀 Enter your Codeforces handle to get:")
st.markdown("""
- 🧠 Weak topic detection  
- 📘 GPT-based explanations & quizzes  
- 🎯 Practice problems (live from Codeforces)  
- 🧭 Learning roadmap  
""")

handle = st.text_input("🎯 Enter Codeforces Handle")

# ✅ Log user handle
def log_usage(handle):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user_history.csv", "a", encoding="utf-8") as f:
        f.write(f"{handle},{timestamp}\n")

if handle:
    log_usage(handle)

if st.button("Analyze"):
    if not handle:
        st.warning("Please enter a valid Codeforces handle.")
    else:
        with st.spinner("🔍 Fetching submission data and analyzing weak areas..."):
            # ✅ Run the main.py file from profile folder
            subprocess.run(["python", "../../profile/main.py", handle])

        # ✅ Correct: get the absolute path to tag_accuracy.csv
        tag_file = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "profile", "tag_accuracy.csv"))

        if not os.path.exists(tag_file):
            st.error("❌ Could not find tag_accuracy.csv. Something went wrong.")
        else:
            df = pd.read_csv(tag_file)
            weak_tags = df[df["accuracy (%)"] < 30]["tag"].tolist()

            if not weak_tags:
                st.success("🎉 You're doing great! No weak tags found.")
            else:
                st.success(f"🧠 Found {len(weak_tags)} weak topics!")
                st.subheader("📚 Topics Needing Improvement")

                for tag in weak_tags[:5]:  # Limit to 5 topics
                    with st.expander(f"📘 {tag.upper()} - Explanation, Quiz, Practice"):
                        explanation = generate_explanation_and_quiz(tag)
                        st.markdown(explanation)

                        st.markdown("### 🧩 Practice Problems:")
                        problems = recommend_problems(tag)
                        if problems:
                            for prob in problems:
                                st.markdown(f"- [{prob['name']}]({prob['url']})")
                        else:
                            st.info("No problems found for this tag.")

                        st.markdown("### 🧭 Learning Roadmap:")
                        st.markdown(f"""
- ✅ Read [CP-Algorithms](https://cp-algorithms.com/) article on **{tag}**
- 🎥 Watch [YouTube Tutorials on {tag}](https://www.youtube.com/results?search_query=codeforces+{tag})
- 🧠 Practice 5 more problems on [Codeforces Tags](https://codeforces.com/problemset?tags={tag})
""")

# ✅ Feedback form (below analysis)
st.subheader("💬 Give Feedback")

feedback = st.text_area("✍️ What did you like or want improved?")

if st.button("Submit Feedback"):
    with open("feedback.csv", "a", encoding="utf-8") as f:
        f.write(f"{handle},{feedback}\n")
    st.success("✅ Thanks for your feedback!")

st.markdown("---")
st.caption("Built with ❤️ by your AI Mentor")
