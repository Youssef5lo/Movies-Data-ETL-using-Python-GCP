from google.cloud import storage
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'ServiceKey_GoogleCloud.json'

def create_bucket(bucket_name):
    try:
        client = storage.Client()
        bucket = client.bucket(bucket_name)
        if not bucket.exists():
            bucket.create()
            print(f'Bucket {bucket_name} created.')
        else:
            print(f'Bucket {bucket_name} already exists.')
    except Exception as e:
        print(f"Failed to create or access the bucket: {e}")

if __name__ == "__main__":
    create_bucket('movie_youssef_bucket')
