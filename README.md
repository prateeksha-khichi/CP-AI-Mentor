# CP-AI-Mentor
🧠 Your Personal AI-Powered Competitive Programming Coach — Level Up Smarter, Not Harder.

> Built for aspiring programmers and Codeforces warriors 🔥

AI CP Mentor is an **AI-powered web assistant** that analyzes your Codeforces profile, identifies your weak topics, teaches them via LLMs, quizzes you, and recommends targeted problems, tutorials, and a personalized roadmap. Built using **Streamlit**, **LLMs (OpenAI/Gemini/Mistral)**, **Codeforces API**, and designed to **boost your DSA skills efficiently**.

---

## 🚀 Features

- 🔍 **Auto-analysis of Codeforces handle**
- 📊 **Topic-wise accuracy calculation**
- 📘 **LLM-powered explanations (GPT/Gemini/Mistral)**
- 🧠 **Quiz generator (MCQ + Fill in the Blank)**
- 🧩 **Smart problem recommendations (easy → hard)**
- 🎥 **Tutorial & CP-Algorithms resource linking**
- 🛣️ **Beginner detection & custom roadmap**
- 📥 **User feedback support**
- 📄 **Export to PDF (in-progress)**
- 📂 **Multi-user handle history tracking (in-progress)**
- 🧩 **Chrome Extension for quick analysis (under development)**

---

## 🛠 Tech Stack

| Layer           | Technology                        | Purpose                                                  |
|----------------|------------------------------------|----------------------------------------------------------|
| 🎨 UI           | [Streamlit](https://streamlit.io) | Web frontend to interactively guide the user             |
| 🧠 AI Models    | OpenAI GPT-3.5 / Gemini Pro / Mistral | Generate explanations, quizzes, roadmaps               |
| 📡 APIs         | Codeforces API                     | Fetch real-time user data and problemsets               |
| 📊 Data Analysis| `pandas`, `matplotlib`, `plotly`  | Analyze accuracy and generate topic stats                |
| 💬 Feedback     | CSV or SQLite                      | Store feedback and interaction history                   |
| 🔒 Secrets      | `python-dotenv`                    | Manage API keys securely                                 |
| 🧪 Testing      | Local testing & Streamlit UI       | Simple debugging and user simulation                     |
| 🌐 Extension    | Chrome Extension (HTML + JS)       | Auto-launch assistant directly from CF website (WIP)     |
| 📄 Reporting    | `reportlab` / `pdfkit` *(planned)* | Generate downloadable performance reports                |

---

## 🔗 APIs Used

| API                 | Purpose                                                             |
|---------------------|---------------------------------------------------------------------|
| ✅ **Codeforces API**   | Get user submission history, tags, ratings, and problem metadata  |
| ✅ **OpenAI / Gemini / Mistral** | Generate explanations, quizzes, and learning plans              |
| ✅ **Clause API (via LLM studio)** *(exploration)* | Plug-and-play custom LLM responses *(planned)*           |
| ✅ **YouTube Search Links** | Link relevant DSA tutorials dynamically                        |
| ✅ **CP-Algorithms**     | Link tag-specific theory for better conceptual clarity           |

---

## 📂 Project Structure

```bash
ai-mentor/
│
├── profile/                   # Profile scraper and analyzer
│   ├── main.py
│   ├── tag_accuracy.csv
│   └── user_submissions.csv
│
├── recommender/              # Tag-based problem recommender
│   └── recommender.py
│
├── gpt-helper/               # AI logic and helpers
│   ├── explain.py
│   ├── strategy_gen.py       # LLM-generated roadmap (WIP)
│   └── newbie_helper.py
│
├── app/                      # Streamlit UI
│   └── app.py
│
├── history/                  # Feedback and progress tracker
│   ├── feedback.csv
│   └── db.sqlite3 (optional)
│
└── chrome-extension/         # Under development
    ├── manifest.json
    ├── popup.html
    └── popup.js


🎯 How This Helps Competitive Programmers
User Level	Benefit
✅ Beginners	Detects if you're new and gives a full roadmap with 800–1000 rated problems
✅ Intermediate	Reveals your weak topics and gives concept-wise quizzes + practice
✅ Advanced	Suggests improvement areas and upskills with problemsets and resource
✅ Will be available under /chrome-extension soon.


✨ Future Improvements
📂 Full user dashboard (handle progress, submission logs)

📄 PDF report export

🎯 Custom LLM fine-tuning (Clause Studio / LlamaIndex)

🎖️ CF contest recommender

📈 Leaderboard of improvement


🧑‍💻 Author
Prateeksha Khichi

Codeforeces: @stickydough

LinkedIn: linkedin.com/in/gungunkhichi

Project Status: 🚧 Actively being improved!


