from fastapi import FastAPI
from app.routes import upload, ai
from app.database import Base, engine

app = FastAPI(title="AI Resume Reviewer")

Base.metadata.create_all(bind=engine)

app.include_router(upload.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "AI Resumr Reviewer"}
