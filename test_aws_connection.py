"""
Quick test to verify AWS credentials are loaded correctly
"""
# test_aws_connection.py
"""
Script to test AWS connection for the Vehicle Insurance Data Pipeline MLops project.
"""
from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, MODEL_BUCKET_NAME, REGION_NAME

print("=" * 60)
print("AWS Configuration Check")
print("=" * 60)

if AWS_ACCESS_KEY_ID_ENV_KEY:
    print(f"✅ AWS_ACCESS_KEY_ID: {AWS_ACCESS_KEY_ID_ENV_KEY[:10]}...{AWS_ACCESS_KEY_ID_ENV_KEY[-4:]}")
else:
    print("❌ AWS_ACCESS_KEY_ID: NOT FOUND")

if AWS_SECRET_ACCESS_KEY_ENV_KEY:
    print(f"✅ AWS_SECRET_ACCESS_KEY: {AWS_SECRET_ACCESS_KEY_ENV_KEY[:10]}...***")
else:
    print("❌ AWS_SECRET_ACCESS_KEY: NOT FOUND")

print(f"✅ REGION_NAME: {REGION_NAME}")
print(f"✅ BUCKET_NAME: {MODEL_BUCKET_NAME}")

print("=" * 60)

if AWS_ACCESS_KEY_ID_ENV_KEY and AWS_SECRET_ACCESS_KEY_ENV_KEY:
    print("✅ All credentials loaded successfully!")
    print("=" * 60)
    
    # Test S3 connection
    try:
        import boto3
        s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID_ENV_KEY,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY_ENV_KEY,
            region_name=REGION_NAME
        )
        
        # Try to access the bucket
        response = s3_client.head_bucket(Bucket=MODEL_BUCKET_NAME)
        print(f"✅ Successfully connected to S3 bucket: {MODEL_BUCKET_NAME}")
        print("✅ You can now run: python demo.py")
    except Exception as e:
        print(f"⚠️  Bucket access test: {str(e)}")
        print("If you see AccessDenied, wait a bit - AWS may still be processing the new credentials.")
else:
    print("❌ Credentials missing! Check your .env file")

print("=" * 60)
