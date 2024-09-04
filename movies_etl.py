from create_bucket import create_bucket
from process_data import process_data
from load_data import upload_blob
import os
import subprocess

def download_data():
    # Run the batch script
    subprocess.run(['download_data.bat'], check=True)

if __name__ == "__main__":
    create_bucket('movie_youssef_bucket')
    download_data()  # Run the batch script to download and extract data
    process_data('ml-100k', 'ratings.csv')
    upload_blob('movie_youssef_bucket', 'ratings.csv', 'first_project/ratings.csv')
