import os
import boto3

# File Paths
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FILE_PATH = os.path.join(DATA_DIR, '2021Icebergs.json')

# AWS Configuration
BUCKET_NAME = "icebergpro-data"
S3_KEY = "2021Icebergs.json"

def upload_to_s3():
    s3 = boto3.client('s3')

    try:
        # Upload file
        s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
        print(f"File '{FILE_PATH}' successfully uploaded to '{BUCKET_NAME}/{S3_KEY}'")
    except Exception as e:
        print(f"Error uploading file: {e}")

if __name__ == "__main__":
    upload_to_s3()
