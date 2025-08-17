import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ai_analyze_missing_keyword(monkeypatch):
    # Mock AI function
    from app.utils import ai_utils
    async def fake_extract_missing_keywords(resume_text, job_description):
        return ["python", "aws"]
    monkeypatch.setattr(ai_utils, "extract_missing_keywords", fake_extract_missing_keywords)

    payload = {
        "filename": "resume.pdf",
        "s3_url": "https://fake-bucket.s3.amazonaws.com/resume.pdf",
        "extracted_text": "This is a sample resume with FastAPI",
        "job_description": "Looking for Python, AWS, FastAPI developer",
        "missing_keywords": []
    }
    response = client.post("/ai/analyze", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "missing_keywords" in data
    assert "python" in data["missing_keywords"]
    