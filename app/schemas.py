from pydantic import BaseModel, field_validator
from typing import List

class ResumeAnalysisCreate(BaseModel):
    filename: str
    s3_url: str
    extracted_text: str
    job_description: str
    missing_keywords: List[str]

    @field_validator("missing_keywords", mode="before")
    def ensure_list(cls, v):
        if isinstance(v, str):  # convert "a,b,c" → ["a", "b", "c"]
            return [kw.strip() for kw in v.split(",") if kw.strip()]
        return v

class ResumeAnalysisResponse(ResumeAnalysisCreate):
    id: int

    class Config:
        from_attributes = True
