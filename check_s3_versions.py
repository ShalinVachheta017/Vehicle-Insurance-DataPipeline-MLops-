"""Check S3 bucket object versions"""
import boto3
from src.constants import AWS_ACCESS_KEY_ID_ENV_KEY, AWS_SECRET_ACCESS_KEY_ENV_KEY, MODEL_BUCKET_NAME, REGION_NAME

s3 = boto3.client('s3', 
                  aws_access_key_id=AWS_ACCESS_KEY_ID_ENV_KEY,
                  aws_secret_access_key=AWS_SECRET_ACCESS_KEY_ENV_KEY,
                  region_name=REGION_NAME)

print("=" * 70)
print(f"S3 Bucket: {MODEL_BUCKET_NAME}")
print("Object Versions for: model.pkl")
print("=" * 70)

try:
    response = s3.list_object_versions(Bucket=MODEL_BUCKET_NAME, Prefix='model.pkl')
    
    if 'Versions' in response:
        print(f"\nTotal Versions: {len(response['Versions'])}\n")
        for i, version in enumerate(response['Versions'], 1):
            print(f"Version {i}:")
            print(f"  Version ID: {version['VersionId']}")
            print(f"  Size: {version['Size']/1024/1024:.2f} MB")
            print(f"  Last Modified: {version['LastModified']}")
            print(f"  Is Latest: {version['IsLatest']}")
            print(f"  ETag: {version['ETag']}")
            print("-" * 70)
    else:
        print("No versions found (versioning may have just been enabled)")
        
    if 'DeleteMarkers' in response:
        print(f"\nDelete Markers: {len(response['DeleteMarkers'])}")
        
except Exception as e:
    print(f"Error: {e}")

print("=" * 70)
