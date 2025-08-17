from sqlalchemy import Column, Integer, Text, DateTime, func, String
from app.database import Base

class ResumeAnalysis(Base):
    __tablename__ = "resume_analysis"

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    s3_url = Column(String, nullable=False)
    extracted_text = Column(Text, nullable=False)
    job_description = Column(Text, nullable=False)
    missing_keywords = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    