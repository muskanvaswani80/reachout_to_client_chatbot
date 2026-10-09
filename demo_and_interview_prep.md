# Demo Scenario Script & Interview Preparation Guide

---

# PART 1: 5–10 MINUTE DEMO PRESENTATION SCRIPT

Use this exact word-for-word script when recording your assignment video or presenting live.

### Sample Lead for Demo:
- **Name:** John Doe
- **Role:** Founder & CEO
- **Company:** CloudScale AI (50 employees, SaaS, India)
- **Pain Point:** Manual lead qualification & slow follow-up delay

---

### Step-by-Step Narration Script:

#### 1. Introduction (0:00 – 1:00)
> *"Hello everyone! Today I am presenting my project: **AI-Powered Lead Generation & Client Outreach Automation**.*
> 
> *In traditional sales teams, sales reps spend over 50% of their working hours manually sorting leads, writing generic emails, and going back-and-forth trying to book calls. My system automates this entire top-of-funnel funnel from end-to-end: from lead ingestion, ICP scoring, AI qualification, personalized outreach, context-aware chatbot conversation, all the way to calendar meeting scheduling and CRM update.*
> 
> *Let's walk through a live demonstration of the prototype."*

#### 2. Dashboard & ICP Configuration (1:00 – 2:00)
> *"Here is the main dashboard running on React and FastAPI with a local SQLite database. At the top, we have real-time KPI metrics showing Total Ingested Leads, Highly Relevant Leads, Potential Leads, Contacted Leads, and Meetings Booked.*
> 
> *First, let's look at the **Ideal Customer Profile (ICP)**. When I open the ICP configuration, we target B2B SaaS companies in India with 10 to 200 employees, looking for sales automation. Our system uses a transparent 100-point scoring algorithm across industry, title, location, company size, and pain points."*

#### 3. Lead Ingestion & Scoring (2:00 – 3:00)
> *"We can ingest leads by uploading any CSV or clicking **'Generate 10 Sample Leads'**. Notice how the system immediately classifies each lead into categories.*
> 
> *For example, we have David Miller from a Logistics company in the US who gets an ICP score of only 10/100 and is marked **Not Qualified**. On the other hand, our top prospect is **John Doe**, Founder & CEO of CloudScale AI, scoring **95 out of 100**."*

#### 4. Inspecting John & AI Lead Qualification (3:00 – 4:00)
> *(Click "Inspect & Automate" on John Doe)*
> *"Let's open John's profile. Under Tab 1, you can see the transparent point breakdown: 25 points for Industry, 20 for Job Title, 15 for Location, 15 for Company Size, 15 for Business Requirement, and 10 for Pain Point.*
> 
> *Now let's switch to Tab 2: **AI Qualification**. When I click 'Re-run AI Qualification', our AI analyzes John's company profile and requirements. In under a second, it returns a structured JSON evaluation: Status is **Qualified**, Buying Intent is **High**, and it highlights his core pain point: 'Too many inbound leads and manual follow-up delay'."*

#### 5. Personalized Outreach Generation (4:00 – 5:00)
> *(Click Tab 3: Personalized Outreach)*
> *"Now we move to outreach. Rather than sending generic spam, our AI copywriter crafts a hyper-personalized message specifically mentioning John's name, CloudScale AI, the SaaS industry, and his exact challenge with manual follow-up delays. It also drafts a follow-up touch.*
> 
> *I can review and edit this copy, then click **'Approve & Send Initial Outreach'**."*

#### 6. Simulated Communication & Conversational AI (5:00 – 6:30)
> *(System switches to Tab 4: Communication Channel)*
> *"Because unauthorized LinkedIn automation is prohibited by terms of service, we implement a safe, realistic communication channel interface.*
> 
> *Our initial message is delivered. Now let's simulate John replying. Using our preset chip, John replies: **'We handle about 1,000 leads/month'**.*
> 
> *Notice what happens: our AI Agent immediately processes John's volume, maintains conversational context, and asks the next qualification question: 'What is the biggest bottleneck your sales reps experience when qualifying those prospects today?'*
> 
> *John responds: **'Manual follow-up takes 4+ hours daily'**. The AI detects high buying intent and immediately offers available meeting slots: Tuesday at 11 AM or Wednesday at 3 PM.*
> 
> *(Mention Human Escalation guardrail):*
> *Notice also: if a prospect ever says 'I want to speak with a human', the system instantly triggers our Human Escalation guardrail, pauses automation, and flags the lead for human review."*

#### 7. Meeting Scheduling & Calendar Booking (6:30 – 7:30)
> *(Click Tab 5: Meeting Scheduler)*
> *"John selects **Wednesday at 3:00 PM**. When I click **'Book Slot'**, our calendar service reserves the slot, generates a Calendar Event ID (`gcal_...`), logs the confirmation in the chat, and automatically updates John's CRM status to **'Meeting Scheduled'**."*

#### 8. Final CRM Verification & Architecture (7:30 – 8:30)
> *(Close modal and show dashboard table)*
> *"Closing the drawer, we see our CRM table is updated in real-time. John Doe's status is now 'Meeting Scheduled', and our Meetings KPI badge has incremented.*
> 
> *To summarize the architecture: Ingestion → Transparent ICP Scoring → AI Qualification → CRM Database → Personalized Outreach → Conversational AI Agent → Calendar Engine → CRM Sync.*
> 
> *Thank you! I am ready to answer any technical questions."*

---

# PART 2: 17 INTERVIEW QUESTIONS & PUNCHY ANSWERS

### 1. What problem does this project solve?
> *"It eliminates the manual repetitive work done by B2B sales development reps (SDRs)—specifically manual lead triage, generic cold outreach, back-and-forth qualification chat, and meeting coordination—reducing lead response time from hours to seconds."*

### 2. Why did you choose this technology stack?
> *"FastAPI offers high-speed asynchronous request handling and automatic OpenAPI documentation. React with Vite provides an instantaneous, responsive user interface. SQLite with SQLAlchemy ORM allows frictionless local demonstration while remaining easily swappable with PostgreSQL in production. Google Gemini offers structured JSON output capabilities."*

### 3. How does lead scoring work?
> *"We use a transparent 100-point deterministic matrix: Industry (25 pts), Job Title (20 pts), Location (15 pts), Company Size 10–200 (15 pts), Business Requirement (15 pts), and Pain Point urgency (10 pts). Scores 80+ are Highly Relevant, 60–79 are Potential, and below 60 are Not Qualified."*

### 4. How does the AI qualify leads?
> *"The AI receives the prospect's profile, ICP requirements, and conversation history, returning a strictly constrained JSON schema specifying qualification status, buying intent (High/Medium/Low), extracted pain points, and recommended next steps."*

### 5. How does the chatbot maintain context?
> *"All messages between the prospect and AI are persisted in the SQLite `conversations` table linked by `lead_id`. On every inbound message, the agent retrieves the chronological dialogue history before generating the response."*

### 6. How do you detect buying intent?
> *"Through a combination of keyword and intent signals in the dialogue: mentions of high monthly lead volumes (>500 leads), specific operational pain points, explicit timeline or budget inquiries, and willingness to review demo slots."*

### 7. How do you prevent repetitive questions?
> *"The conversation engine tracks question stages based on message history length and key extracted entities (volume already asked vs. bottleneck already asked), advancing sequentially rather than looping."*

### 8. How does human escalation work?
> *"If the prospect expresses hostility, requests a human agent ('speak with someone', 'real person'), or asks questions outside the qualification scope, the lead status changes to 'Human Review', automated outreach is halted, and an alert banner is displayed."*

### 9. How is LinkedIn integration handled?
> *"We built a simulated direct messaging channel. This provides the exact conversational experience without violating third-party platform policies."*

### 10. Why didn't you scrape LinkedIn?
> *"Automated scraping or unauthorized bot automation on LinkedIn violates Section 8.2 of LinkedIn's Terms of Service and can cause IP blacklisting and account bans. Production systems should use official LinkedIn Marketing APIs or verified CRM integrations like HubSpot."*

### 11. How does meeting scheduling work?
> *"The system exposes predefined available calendar slots. When a qualified prospect chooses a slot, the system creates a meeting record, generates a calendar event ID, notifies the chat history, and transitions the lead status to 'Meeting Scheduled'."*

### 12. How is data stored?
> *"In a relational SQLite database (`leads.db`) managed through SQLAlchemy ORM, comprising `leads`, `conversations`, and `meetings` tables with cascading foreign keys."*

### 13. What APIs are used?
> *"Google Gemini REST API for LLM generation, FastAPI REST endpoints for lead management and conversation orchestration, and calendar booking APIs."*

### 14. How would you scale this system?
> *"Replace SQLite with PostgreSQL, deploy FastAPI behind an ASGI server with Kubernetes horizontal pod autoscaling, use Celery/Redis for background message queuing, and add WebSockets for real-time bi-directional chat."*

### 15. What security measures would be required in production?
> *"JWT-based authentication (OAuth2), rate limiting via Redis, input sanitization against prompt injection attacks, encryption at rest for PII data, and HTTPS enforcement."*

### 16. What are the limitations of this prototype?
> *"It currently uses simulated outreach rather than live live email/LinkedIn webhooks, and uses predefined calendar slots rather than live Google Calendar OAuth refresh tokens."*

### 17. What would you improve in version 2?
> *"Integrate SendGrid and WhatsApp Business API, add live Google Meet/Zoom link creation via Google Calendar OAuth, and build a two-way sync connector with Salesforce/HubSpot."*
