"""Check S3 bucket contents"""
import boto3
"""Script to check the status or existence of an S3 bucket for the Vehicle Insurance Data Pipeline MLops project."""
from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, MODEL_BUCKET_NAME, REGION_NAME

s3 = boto3.client('s3', 
                  aws_access_key_id=AWS_ACCESS_KEY_ID_ENV_KEY,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY_ENV_KEY,
                  region_name=REGION_NAME)

print("=" * 70)
print(f"S3 Bucket: {MODEL_BUCKET_NAME}")
print("=" * 70)

try:
    response = s3.list_objects_v2(Bucket=MODEL_BUCKET_NAME)
    
    if 'Contents' in response:
        for obj in response['Contents']:
            print(f"File: {obj['Key']}")
            print(f"  Size: {obj['Size']/1024/1024:.2f} MB")
            print(f"  Last Modified: {obj['LastModified']}")
            print(f"  ETag: {obj['ETag']}")
            print("-" * 70)
    else:
        print("No objects found in bucket")
except Exception as e:
    print(f"Error: {e}")

print("=" * 70)
