from fastapi import FastAPI
from app.routes import upload

app = FastAPI(title="AI Resume Reviewer")

app.include_router(upload.router)

@app.get("/")
def root():
    return {"message": "AI Resumr Reviewer"}
