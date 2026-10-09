# NexusAI: AI-Powered Lead Generation & Outreach Automation

An end-to-end autonomous prototype demonstrating:
**Lead Acquisition → ICP Enrichment & Scoring → AI Qualification → CRM/Database → Personalized Outreach → Conversational AI Agent → Meeting Scheduling → Calendar Booking → CRM Sync**.

---

## 1. Project Overview & Objective

In modern B2B sales pipelines, sales development representatives (SDRs) spend up to 60% of their time manually reviewing unqualified leads, writing repetitive emails, and coordinating meeting schedules.

**NexusAI** automates the entire top-of-funnel workflow:
1. Ingests leads from CSV or sample databases.
2. Applies a **transparent 100-point Ideal Customer Profile (ICP) algorithm**.
3. Employs **LLM-based AI Qualification** returning structured JSON.
4. Generates **hyper-personalized outreach messages** based on the prospect's exact role and pain points.
5. Runs an **interactive, context-aware AI conversational agent** that asks one qualification question at a time and detects buying intent.
6. Handles **Human Escalation** guardrails when human intervention is needed.
7. Offers available calendar slots and automatically books meetings into the database.

---

## 2. Technology Stack & Design Decisions

| Layer | Technology | Rationale |
| :--- | :--- | :--- |
| **Frontend** | React 19 + Vite | Lightweight, sub-second hot reloading, responsive dashboard. |
| **Backend** | Python + FastAPI | High-performance asynchronous API framework with automatic Swagger docs (`/docs`). |
| **Database** | SQLite + SQLAlchemy ORM | Zero-setup, serverless database for easy demonstration; easily swappable with PostgreSQL. |
| **AI / LLM** | Google Gemini API | Advanced reasoning with strict JSON output capabilities; includes deterministic fallback for 100% demo uptime. |
| **Outreach** | Simulated Direct Outreach Channel | Safe, compliant communication interface that avoids unauthorized LinkedIn scraping. |
| **Calendar** | Integrated Calendar Scheduler | Predefined slots with automated event generation and CRM synchronization. |

---

## 3. Architecture & Data Flow

```text
Lead Ingestion (CSV / Samples)
             │
             ▼
100-Point Transparent ICP Scoring
             │
             ▼
AI Qualification Engine (Structured JSON)
             │
             ▼
SQLite CRM (leads.db)
             │
             ▼
Personalized Outreach Copywriter (Name, Company, Pain Point)
             │
             ▼
Communication Channel (Simulated / Telegram Bot API)
             │
             ▼
Context-Aware AI Conversation Agent (1 question at a time)
             │
    ┌────────┴────────┐
    ▼                 ▼
Human Escalation   High Intent Detected
(Status: Review)   (Slot Offered)
                      │
                      ▼
               Meeting Booked & CRM Updated
```

---

## 4. Setup & Installation Instructions

### Prerequisites
- Python 3.10+
- Node.js 18+ and npm

### Backend Setup
```powershell
cd ai-lead-automation/backend
# Create virtual environment (if not already created)
python -m venv venv
.\venv\Scripts\pip.exe install -r requirements.txt

# Start backend server
.\venv\Scripts\python.exe -m uvicorn main:app --reload --port 8000
```
Backend API will be running on: `http://127.0.0.1:8000`  
Swagger Documentation: `http://127.0.0.1:8000/docs`

### Frontend Setup
```powershell
cd ai-lead-automation/frontend
npm.cmd install
npm.cmd run dev
```
Frontend will be running on: `http://localhost:5173`

---

## 5. Environment Variables (`backend/.env`)

```env
PORT=8000
DATABASE_URL=sqlite:///./leads.db
GEMINI_API_KEY=your_gemini_api_key_here
TELEGRAM_BOT_TOKEN=
```
*(Note: If `GEMINI_API_KEY` is omitted, the application runs on its built-in heuristic AI engine so you can demo without API quota limitations!)*

---

## 6. Key REST API Endpoints

- `GET /api/dashboard/stats`: Returns KPI totals (Total Leads, Highly Relevant, Potential, Contacted, Meetings).
- `GET /api/leads`: Lists all leads ordered by ICP score.
- `POST /api/leads/generate-samples`: Seeds 10 realistic B2B test leads.
- `POST /api/leads/upload-csv`: Ingests custom CSV lead files.
- `POST /api/leads/{id}/qualify`: Runs AI qualification service.
- `POST /api/leads/{id}/generate-outreach`: Produces personalized initial and follow-up copy.
- `POST /api/leads/{id}/send-outreach`: Logs message and updates lead status to `Contacted`.
- `POST /api/chat/{lead_id}/message`: Processes prospect/agent messages, generates conversational AI response, and detects intent.
- `POST /api/chat/{lead_id}/escalate`: Triggers human takeover (`Human Review`).
- `GET /api/meetings/slots`: Retrieves available calendar slots.
- `POST /api/meetings`: Confirms meeting and sets lead status to `Meeting Scheduled`.

---

## 7. LinkedIn & Communication Channel Compliance

> **Why LinkedIn scraping is not implemented:**  
> Scraping LinkedIn without official API approval violates LinkedIn's Terms of Service and can result in IP bans or legal notices. This prototype implements a **Simulated Direct Outreach Interface** (or Telegram Bot API), providing an authentic demonstration of AI-driven messaging while remaining 100% compliant and safe.

---

## 8. Future Enhancements (v2)
1. **Multi-Channel Dispatcher**: Add SendGrid for cold email and WhatsApp Business API.
2. **Real-time WebSockets**: Push instant notifications when a prospect replies.
3. **Google Calendar OAuth**: Live two-way calendar sync with Google Meet video links.
4. **CRM Connectors**: Two-way sync with HubSpot and Salesforce.
