import os
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from dotenv import load_dotenv

import models
import schemas
from database import engine, get_db, Base
from routes import leads, chat, meetings
from services.lead_service import DEFAULT_ICP

load_dotenv()

# Automatically ensure all tables exist in SQLite
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-Powered Lead Generation & Outreach Automation",
    description="End-to-end prototype for Lead Qualification, Personalized Outreach, Conversation Handling, and Scheduling",
    version="1.0.0"
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(leads.router)
app.include_router(chat.router)
app.include_router(meetings.router)

# In-memory ICP Config state (defaults to Phase 3 criteria)
current_icp_config = dict(DEFAULT_ICP)

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "AI Lead Automation API is running!",
        "version": "1.0.0",
        "docs_url": "/docs"
    }

@app.get("/api/health")
def health_check(db: Session = Depends(get_db)):
    lead_count = db.query(models.Lead).count()
    meeting_count = db.query(models.Meeting).count()
    return {
        "status": "healthy",
        "database": "sqlite (leads.db)",
        "tables_created": True,
        "lead_count": lead_count,
        "meeting_count": meeting_count,
        "ai_service": "ready"
    }

@app.get("/api/dashboard/stats")
def get_dashboard_stats(db: Session = Depends(get_db)):
    all_leads = db.query(models.Lead).all()
    total = len(all_leads)
    highly_relevant = sum(1 for l in all_leads if l.icp_score >= 80)
    potential = sum(1 for l in all_leads if 60 <= l.icp_score < 80)
    not_qualified = sum(1 for l in all_leads if l.icp_score < 60)
    contacted = sum(1 for l in all_leads if l.lead_status in ["Contacted", "Responded", "Qualifying", "Qualified", "Meeting Scheduled"])
    meetings_scheduled = sum(1 for l in all_leads if l.lead_status == "Meeting Scheduled")
    human_review = sum(1 for l in all_leads if l.lead_status == "Human Review")

    return {
        "total_leads": total,
        "highly_relevant": highly_relevant,
        "potential": potential,
        "not_qualified": not_qualified,
        "contacted": contacted,
        "meetings_scheduled": meetings_scheduled,
        "human_review": human_review
    }

@app.get("/api/icp-config")
def get_icp_config():
    return current_icp_config

@app.post("/api/icp-config")
def update_icp_config(config: dict):
    global current_icp_config
    current_icp_config.update(config)
    return {"message": "ICP Configuration updated successfully", "icp": current_icp_config}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
