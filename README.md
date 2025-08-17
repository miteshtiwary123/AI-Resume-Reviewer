# AI Resume Reviewer API

An API to upload resumes (PDF/DOCX), extract text, analyze against job descriptions using AI, and suggest missing keywords.

---

## 🚀 Features
- Upload resumes (PDF, DOCX)
- Extract text with **PyMuPDF** & **docx2txt**
- Store files in **AWS S3**
- Analyze resumes with **OpenAI GPT / HuggingFace**
- Extract missing keywords from job description
- Store results in **PostgreSQL**
- API rate limiting
- Async AI processing
- Automated tests

---

## 📦 Installation
```bash
git clone https://github.com/miteshtiwary123/ai_resume_reviewer.git
cd ai_resume_reviewer
pip install -r requirements.txt
```
Set environment variables in .env:
```env
AWS_ACCESS_KEY_ID=xxxx
AWS_SECRET_ACCESS_KEY=xxxx
AWS_REGION=ap-south-1
S3_BUCKET_NAME=ai-resume-bucket
OPENAI_API_KEY=sk-xxxx
DATABASE_URL=postgresql://postgres:password@localhost:5432/ai_resume
```
## ▶️ Run Locally
```bash
uvicorn app.main:app --reload
```
Visit docs: http://127.0.0.1:8000/docs

## 📌 API Endpoints
### 1. Upload Resume
`POST /upload/resume`

* Request: multipart file (**PDF** or **DOCX**)

* Response:
```json
{
  "filename": "resume.pdf",
  "s3_url": "https://bucket.s3.aws.com/resume.pdf",
  "extracted_text_preview": "Extracted resume text..."
}
```
### 2. Analyze Resume
`POST /ai/analyze`
* Request:
```json
{
  "filename": "resume.pdf",
  "s3_url": "https://bucket.s3.aws.com/resume.pdf",
  "extracted_text": "Candidate has FastAPI experience",
  "job_description": "We need Python, AWS, FastAPI developer",
  "missing_keywords": []
}
```
* Response:
```json
{
  "id": 1,
  "filename": "resume.pdf",
  "s3_url": "https://bucket.s3.aws.com/resume.pdf",
  "extracted_text": "Candidate has FastAPI experience",
  "job_description": "We need Python, AWS, FastAPI developer",
  "missing_keywords": ["Python", "AWS"]
}
```
## 🧪 Run Tests
```bash
pytest -v
```
### 📜 License
MIT License