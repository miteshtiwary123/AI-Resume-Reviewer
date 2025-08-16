import boto3
from app.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION, S3_BUCKET_NAME
from uuid import uuid4

s3_client = boto3.client(
    "s3",
    aws_access_key_id = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name = AWS_REGION
)

def upload_file_to_s3(file_bytes: bytes, filename: str, content_type: str) -> str:
    """ Upload the file to s3 and return the s3 url"""
    unique_filename = f"{uuid4()}-{filename}"
    s3_client.put_object(
        Bucket=S3_BUCKET_NAME,
        Key=unique_filename,
        Body=file_bytes,
        ContentType=content_type
    )
    return f"https://{S3_BUCKET_NAME}.s3.{AWS_REGION}.amazon.com/{unique_filename}"
