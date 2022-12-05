from fastapi import APIRouter, Body, Depends,HTTPException,Response
from fastapi import UploadFile
import boto3
import os
from ..auth.auth_handler import decodeJWT
from ..auth.auth_bearer import JWTBearer

files_router = APIRouter()

@files_router.post("/photos/upload", status_code=201, tags=["S3 Service"])
async def add_photo(file: UploadFile):
    print("Create endpoint hit!!")
    print(file.filename)
    print(file.content_type)
    # Upload file to AWS S3
    try:
        s3 = boto3.resource("s3",
        aws_access_key_id=os.environ["AWS_ACCESS_KEY_ID"],
        aws_secret_access_key=os.environ["AWS_SECRET_ACCESS_KEY"]
            )

        S3_BUCKET_NAME = os.environ["S3_BUCKET_NAME"]
        bucket = s3.Bucket(S3_BUCKET_NAME)

        bucket.upload_fileobj(file.file, file.filename, ExtraArgs={"ACL": "public-read"})
        uploaded_file_url = f"https://{S3_BUCKET_NAME}.s3.us-west-1.amazonaws.com/{file.filename}"

    except:
        raise Response(
            status_code=404,
            detail="Something was wrong with the credentials",
            headers={"Error" : "Keys or upload-file"}
        )
    else:
        return {"photo_name": file.filename, "photo_url": uploaded_file_url}