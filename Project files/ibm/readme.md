# Sustainable Smartcity Assistant 🌱🏙️

A modular dashboard for interacting with urban sustainability data, powered by an intelligent assistant. The app features real-time KPI visualizations, eco tips search, policy summarization, and feedback collection.

---

🚀 Features
🔍 Policy Summarization — Upload policies (.txt or .csv) and get concise summaries.

🔥 KPI Monitoring — View real-time city KPIs like air quality, water usage, and energy.

💬 Sustainability Chat — Ask AI about eco-friendly practices, policies, and city stats.

🌿 Eco-Friendly Tips — Get tips by searching with relevant keywords.

🗣️ Citizen Feedback — Submit feedback categorized by issue or suggestion.

🧠 Anomaly Detection — Identify anomalies in uploaded datasets.

---

🧠 AI Model
✅ Model Used: ibm-granite/granite-3.3-2b-instruct via Hugging Face API.

---
## 🖥️ Frontend Overview

- Pure HTML5 + CSS3 (no JS frameworks)
- Responsive, accessible, and modular design
- Connects to FastAPI backend endpoints for all features

---

## 🚦 Running the Application

1. **Backend**: Start FastAPI server (`uvicorn backend.main:app --reload`)
        command : cd D:\ibm\backend
                  uvicorn main:app --reload
2. **Frontend**: Serve `frontend/` statically (`python -m http.server 8080`)
        command : cd D:\ibm\frontend
                  python -m http.server 8080
3. **Open**: `http://localhost:8080/index.html` in your browser

---
