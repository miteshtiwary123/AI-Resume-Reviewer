from fastapi import APIRouter, UploadFile, File, HTTPException
from app.utils.file_handler import extract_text_from_pdf, extract_text_from_docx
from app.utils.s3_utils import upload_file_to_s3

router = APIRouter(prefix="/upload", tags=["upload"])

@router.post("/resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf",
                                 "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Invalid filetype. Only PDF and DOCX allowed")

    file_bytes = await file.read()

    # Extract Text
    if file.content_type == "applicationj/pdf":
        extracted_text = extract_text_from_pdf(file_bytes)
    else:
        extracted_text = extract_text_from_docx(file_bytes)

    # Upload to S3
    s3_url = upload_file_to_s3(file_bytes, file.filename, file.content_type)

    return {
        "filename": file.filename,
        "s3_url": s3_url,
        "extracted_text_preview": extracted_text[:500]
    }
