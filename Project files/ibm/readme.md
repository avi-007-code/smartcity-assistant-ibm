# Sustainable Smartcity Assistant 🌱🏙️

A modular dashboard for interacting with urban sustainability data, powered by an intelligent assistant. The app features real-time KPI visualizations, eco tips search, policy summarization, and feedback collection.

---

## 📁 Project Structure

```
ibm/
│
├── frontend/
│   ├── index.html
│   ├── chat.html
│   ├── upload.html
│   ├── kpi.html
│   ├── tips.html
│   ├── feedback.html
│   └── styles.css
│
└── readme.md
```

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

## Next Steps

The following frontend files will be created:
- `frontend/index.html`
- `frontend/chat.html`
- `frontend/upload.html`
- `frontend/kpi.html`
- `frontend/tips.html`
- `frontend/feedback.html`
- `frontend/styles.css`

Each file will be modular, well-documented, and ready for backend integration.
