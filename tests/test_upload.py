import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_invalid_file():
    response = client.post(
        "/upload/resume",
        files={"file": ("test.txt", b"hello world", "text/plain")}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid file type. Only PDF and DOCX allowed."
    