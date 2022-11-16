from fastapi import APIRouter
from fastapi import UploadFile
from dotenv import dotenv_values
import boto3

files_router = APIRouter()

config = dotenv_values('./venv/.env.aws')
S3_BUCKET_NAME = config['S3_BUCKET_NAME']
AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']

@files_router.post("/photos/upload", status_code=201)
async def add_photo(file: UploadFile):
    print("Create endpoint hit!!")
    print(file.filename)
    print(file.content_type)
    # Upload file to AWS S3
    s3 = boto3.resource("s3", aws_access_key_id=AWS_ACCESS_KEY_ID,aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    bucket = s3.Bucket(S3_BUCKET_NAME)

    bucket.upload_fileobj(file.file, file.filename, ExtraArgs={"ACL": "public-read"})
    uploaded_file_url = f"https://{S3_BUCKET_NAME}.s3.us-west-1.amazonaws.com/{file.filename}"
    print(uploaded_file_url)

    return {"photo_name": file.filename, "photo_url": uploaded_file_url}