from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from datetime import datetime

# ============================
# LEAD SCHEMAS
# ============================
class LeadBase(BaseModel):
    name: str
    designation: Optional[str] = None
    company_name: Optional[str] = None
    company_website: Optional[str] = None
    linkedin_url: Optional[str] = None
    telegram_id: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    company_size: Optional[str] = None
    business_requirement: Optional[str] = None
    pain_points: Optional[str] = None

class LeadCreate(LeadBase):
    pass

class LeadUpdate(BaseModel):
    name: Optional[str] = None
    designation: Optional[str] = None
    company_name: Optional[str] = None
    company_website: Optional[str] = None
    linkedin_url: Optional[str] = None
    telegram_id: Optional[str] = None
    industry: Optional[str] = None
    location: Optional[str] = None
    company_size: Optional[str] = None
    business_requirement: Optional[str] = None
    pain_points: Optional[str] = None
    icp_score: Optional[int] = None
    qualification_status: Optional[str] = None
    buying_intent: Optional[str] = None
    lead_summary: Optional[str] = None
    lead_status: Optional[str] = None

class LeadResponse(LeadBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    icp_score: int = 0
    qualification_status: str
    buying_intent: str
    lead_summary: Optional[str] = None
    lead_status: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


# ============================
# CONVERSATION SCHEMAS
# ============================
class ConversationBase(BaseModel):
    sender: str
    message: str

class ConversationCreate(ConversationBase):
    lead_id: int

class ConversationResponse(ConversationBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    lead_id: int
    timestamp: datetime


# ============================
# MEETING SCHEMAS
# ============================
class MeetingBase(BaseModel):
    meeting_date: str
    meeting_time: str
    meeting_type: Optional[str] = "Discovery Call (30 min)"

class MeetingCreate(MeetingBase):
    lead_id: int

class MeetingResponse(MeetingBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    lead_id: int
    calendar_event_id: Optional[str] = None
    status: str
    created_at: Optional[datetime] = None


# ============================
# ICP CONFIGURATION SCHEMA
# ============================
class ICPConfig(BaseModel):
    target_industry: str = "SaaS"
    target_job_titles: List[str] = ["Founder", "CEO", "Sales Head", "VP Sales", "Co-Founder"]
    target_location: str = "India"
    target_company_size_min: int = 10
    target_company_size_max: int = 200
    target_requirement: str = "Lead generation / sales automation"
    target_pain_point: str = "Too many leads / manual qualification"


# ============================
# AI QUALIFICATION RESULT SCHEMA
# ============================
class AIQualificationResult(BaseModel):
    qualification_status: str  # Qualified, Potential, Not Qualified
    score: int
    buying_intent: str        # High, Medium, Low
    pain_points: List[str]
    requirements: List[str]
    reason: str
    summary: str
    next_action: str
