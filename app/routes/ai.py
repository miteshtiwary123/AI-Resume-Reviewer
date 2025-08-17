from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ResumeAnalysisCreate, ResumeAnalysisResponse
from app.crud import create_resume_analysis
from app.utils.ai_utils import extract_missing_keywords

router = APIRouter(prefix="/ai", tags=["AI"])

@router.post("/analyze", response_model=ResumeAnalysisResponse)
def analyze_resume(data: ResumeAnalysisCreate, db: Session =Depends(get_db)):
    try:
        missing_keywords = extract_missing_keywords(
            resume_text=data.extracted_text,
            job_description=data.job_description
        )

        # Ensure it's always a list of strings
        if isinstance(missing_keywords, str):
            missing_keywords = [kw.strip() for kw in missing_keywords.split(",") if kw.strip()]
            
        data.missing_keywords = missing_keywords
        result = create_resume_analysis(db, data)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
