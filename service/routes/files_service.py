from fastapi import APIRouter
from fastapi import UploadFile
from dotenv import dotenv_values
import boto3
import os

files_router = APIRouter()

@files_router.post("/photos/upload", status_code=201)
async def add_photo(file: UploadFile):
    print("Create endpoint hit!!")
    print(file.filename)
    print(file.content_type)
    # Upload file to AWS S3
    s3 = boto3.resource("s3",
    aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
    aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"])
    S3_BUCKET_NAME = os.environ["S3_BUCKET_NAME"]
    bucket = s3.Bucket(S3_BUCKET_NAME)

    bucket.upload_fileobj(file.file, file.filename, ExtraArgs={"ACL": "public-read"})
    uploaded_file_url = f"https://{S3_BUCKET_NAME}.s3.us-west-1.amazonaws.com/{file.filename}"
    print(uploaded_file_url)

    return {"photo_name": file.filename, "photo_url": uploaded_file_url}