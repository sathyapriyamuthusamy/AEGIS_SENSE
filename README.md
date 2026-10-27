# AegisSense — AI-Powered Intelligent Guidance Platform

**AegisSense is an education-first guidance layer designed to help institutions move from reactive management to proactive, supportive intelligence.** It aims to notice when a learner may need support, suggest a manageable next step, monitor whether guidance helps, and make it easier to involve the right human when needed.

> This repository is a runnable MVP prototype. It uses sample data and rule-based demo guidance, not a trained AI model or a live student information system.

## Product loop

**Sense → Understand → Guide → Monitor → Adapt → Escalate → Follow up**

The goal is not another attendance dashboard or a stream of reminders. AegisSense explores how guidance can adapt when a student is not responding, while keeping interventions respectful and human-centred.

## Current prototype features

- Student overview dashboard with a daily focus checklist.
- Guide AI chat interface with a working FastAPI endpoint and rule-based demo responses.
- Growth page with progress and weekly activity illustration.
- GameVerse page presenting three learning-game concepts: Concept Quest, Memory Garden, and Focus Trail.
- Insights page with a supportive next-step suggestion and clear sample-data notice.
- Responsive layout for desktop, tablet, and mobile.
- FastAPI health check and sample dashboard endpoint.

## Tech stack

- **Frontend:** React, Vite, JavaScript, CSS, Lucide icons
- **Backend:** Python, FastAPI, Pydantic, Uvicorn
- **Data:** In-memory/sample data only in this MVP

## Project structure

```text
AegisSense_Complete/
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── styles.css
│   ├── index.html
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── main.py
│   └── requirements.txt
├── .gitignore
├── README.md
└── TESTING.md
```

## Run locally

### Requirements

- Node.js 20+ recommended
- Python 3.11+ recommended

### 1. Start the backend (Windows PowerShell)

```powershell
cd backend
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

API will run at `http://127.0.0.1:8000` and interactive API docs at `http://127.0.0.1:8000/docs`.

### 2. Start the frontend in a second terminal

```powershell
cd frontend
npm install
npm run dev
```

Open the local address printed by Vite (usually `http://localhost:5173`). The frontend works in demo mode even when the API is not running; starting the API enables the live health status and guidance endpoint.

### Test the API

Open `http://127.0.0.1:8000/api/health` or visit `http://127.0.0.1:8000/docs` and try `POST /api/guidance` with:

```json
{"message":"I feel overwhelmed about my exam"}
```

## Privacy, safety, and limitations

- Do not upload real student records, personal data, passwords, or API keys to this repository.
- The current demo uses sample tasks and simple keyword-based responses; it is **not** a medical or counselling service and does not make real risk predictions.
- Before a real pilot, add authentication, role-based access, consent, data minimisation, secure storage, audit logging, accessibility testing, and human review/escalation workflows.
- The charts and game cards are prototype UI; they do not claim to represent real student analytics or fully implemented games.

## Roadmap

1. Add secure authentication and role-based student/faculty/institution views.
2. Connect approved data sources with explicit consent and access controls.
3. Track whether a guidance intervention helped and adapt follow-up appropriately.
4. Add accessible, functional learning games and offline-first support.
5. Evaluate guidance quality with educators and students before deployment.

## Author

Sathyapriya M · B.Tech CSBS · AegisSense project
