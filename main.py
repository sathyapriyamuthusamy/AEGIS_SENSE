from datetime import date
from typing import Literal
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

app = FastAPI(
    title="AegisSense API",
    description="Demo API for an adaptive, supportive student guidance platform.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "http://localhost:4173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GuidanceRequest(BaseModel):
    message: str = Field(min_length=1, max_length=2000)
    student_context: dict | None = None

class GuidanceResponse(BaseModel):
    reply: str
    category: Literal["study", "wellbeing", "planning", "general"]
    suggested_next_step: str
    is_demo: bool = True

@app.get("/")
def root():
    return {"name": "AegisSense API", "version": "1.0.0", "status": "running", "docs": "/docs"}

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "aegissense-api", "date": date.today().isoformat()}

@app.get("/api/dashboard")
def dashboard():
    return {
        "student": {"display_name": "Sathya Priya", "role": "student"},
        "focus": [
            {"id": 1, "title": "Review Data Structures notes", "detail": "Arrays and linked lists · 20 min", "done": False, "tag": "Study"},
            {"id": 2, "title": "Submit DBMS assignment", "detail": "Due tomorrow · Unit 3", "done": False, "tag": "Deadline"},
            {"id": 3, "title": "Take a 5-minute reset", "detail": "A small break can help you refocus", "done": True, "tag": "Wellbeing"},
        ],
        "notice": "Demo data only. Connect an authorized student information source before real deployment.",
    }

@app.post("/api/guidance", response_model=GuidanceResponse)
def guidance(request: GuidanceRequest):
    text = request.message.lower()
    if any(word in text for word in ("stress", "tired", "overwhelm", "anxious", "sad", "pressure")):
        return GuidanceResponse(
            reply="Let's make this lighter. Pick just one small task for the next 10 minutes, then pause. You don't need to solve everything at once. If things feel difficult to manage, consider talking with someone you trust.",
            category="wellbeing", suggested_next_step="Choose one manageable 10-minute task"
        )
    if any(word in text for word in ("exam", "study", "learn", "subject", "mark", "assignment", "understand")):
        return GuidanceResponse(
            reply="Try a focused 20-minute session: choose one concept, explain it in your own words, then solve one example. What subject should we break down first?",
            category="study", suggested_next_step="Choose one concept and one example"
        )
    if any(word in text for word in ("plan", "time", "schedule", "deadline", "tomorrow")):
        return GuidanceResponse(
            reply="Let's make a flexible plan. Write down what is due first, estimate how long each task may take, and start with one small step. Leave a little breathing room so the plan can adapt.",
            category="planning", suggested_next_step="List the nearest deadline and one first action"
        )
    return GuidanceResponse(
        reply="A useful next step is to choose one specific goal, make it small enough to finish in 15–20 minutes, and check in with yourself afterwards. Would you like help with studying, planning, or getting unstuck?",
        category="general", suggested_next_step="Pick one small goal for the next 15–20 minutes"
    )
