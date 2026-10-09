import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    designation = Column(String(120), nullable=True)
    company_name = Column(String(150), nullable=True)
    company_website = Column(String(200), nullable=True)
    linkedin_url = Column(String(250), nullable=True)
    telegram_id = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True)
    location = Column(String(100), nullable=True)
    company_size = Column(String(50), nullable=True)
    business_requirement = Column(Text, nullable=True)
    pain_points = Column(Text, nullable=True)

    # Qualification & ICP Fields
    icp_score = Column(Integer, default=0)
    qualification_status = Column(String(50), default="Not Evaluated")  # Qualified, Potential, Not Qualified
    buying_intent = Column(String(50), default="Unknown")                # High, Medium, Low
    lead_summary = Column(Text, nullable=True)
    
    # Workflow Status:
    # New | Contacted | Responded | Qualifying | Qualified | Potential | Not Qualified | Meeting Scheduled | Human Review
    lead_status = Column(String(50), default="New")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    # Relationships
    conversations = relationship("Conversation", back_populates="lead", cascade="all, delete-orphan")
    meetings = relationship("Meeting", back_populates="lead", cascade="all, delete-orphan")


class Conversation(Base):
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id", ondelete="CASCADE"), nullable=False)
    sender = Column(String(50), nullable=False)  # "AI", "Prospect", "User/Human"
    message = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship back to lead
    lead = relationship("Lead", back_populates="conversations")


class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    lead_id = Column(Integer, ForeignKey("leads.id", ondelete="CASCADE"), nullable=False)
    meeting_date = Column(String(50), nullable=False)        # e.g., "2026-10-15"
    meeting_time = Column(String(50), nullable=False)        # e.g., "03:00 PM"
    meeting_type = Column(String(100), default="Discovery Call (30 min)")
    calendar_event_id = Column(String(150), nullable=True)  # Mock ID or Google Calendar Event ID
    status = Column(String(50), default="Scheduled")        # Scheduled, Completed, Cancelled
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    # Relationship back to lead
    lead = relationship("Lead", back_populates="meetings")
