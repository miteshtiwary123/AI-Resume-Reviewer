from sqlalchemy.orm import Session
from app import models, schemas

def create_resume_analysis(db: Session, data: schemas.ResumeAnalysisCreate):
    db_obj = models.ResumeAnalysis(
        filename=data.filename,
        s3_url=data.s3_url,
        extracted_text = data.extracted_text,
        job_description = data.job_description,
        missing_keywords = ",".join(data.missing_keywords),
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
