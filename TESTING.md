# Testing checklist

## Frontend
- [ ] `npm install` completes inside `frontend/`.
- [ ] `npm run dev` opens the dashboard.
- [ ] Sidebar navigation opens Overview, Guide AI, My Growth, GameVerse, and Insights.
- [ ] Daily focus items can be checked and unchecked.
- [ ] Guide AI accepts a message and returns a response (with backend running or fallback demo response).
- [ ] Mobile menu works at narrow viewport widths.
- [ ] `npm run build` completes without errors.

## Backend
- [ ] Install packages from `backend/requirements.txt` in a virtual environment.
- [ ] `python -m uvicorn main:app --reload` starts the API.
- [ ] `GET /api/health` returns `status: ok`.
- [ ] `GET /api/dashboard` returns sample dashboard data.
- [ ] `POST /api/guidance` returns a response for a non-empty message.

## Before any real deployment
- [ ] Replace sample data with an approved, secured data source.
- [ ] Add authentication, authorisation, consent, retention rules, and audit logs.
- [ ] Review privacy, accessibility, security, and human escalation with qualified stakeholders.
