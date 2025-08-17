from fastapi import FastAPI
from app.routes import upload, ai
from app.database import Base, engine
from app.middleware.rate_limiter import limiter, rate_limit_exception_handler
from slowapi.middleware import SlowAPIMiddleware

app = FastAPI(title="AI Resume Reviewer")

Base.metadata.create_all(bind=engine)

#Middleware for rate limiting
app.state.limiter = limiter
app.add_exception_handler(429, rate_limit_exception_handler)
app.add_middleware(SlowAPIMiddleware)

app.include_router(upload.router)
app.include_router(ai.router)

@app.get("/")
def root():
    return {"message": "AI Resumr Reviewer"}
