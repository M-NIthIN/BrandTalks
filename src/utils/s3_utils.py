 
import boto3
from botocore.exceptions import ClientError
from src.utils.config import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_REGION


# Create an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

def upload_to_s3(bucket_name, key, data):
    try:
        if isinstance(data, str):
            data = data.encode('utf-8')
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=data)
        print(f"Successfully uploaded {key} to {bucket_name}.")
    except ClientError as e:
        print(f"Failed to upload {key} to {bucket_name}: {e}")

def download_from_s3(bucket_name, key):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=key)
        data = response['Body'].read()
        print(f"Successfully downloaded {key} from {bucket_name}.")
        return data
    except ClientError as e:
        print(f"Failed to download {key} from {bucket_name}: {e}")
        return None

def file_exists(bucket_name, key):
    try:
        s3_client.head_object(Bucket=bucket_name, Key=key)
        return True
    except ClientError:
        return False

def list_files_in_bucket(bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except ClientError as e:
        print(f"Failed to list files in bucket {bucket_name}: {e}")
        return []
