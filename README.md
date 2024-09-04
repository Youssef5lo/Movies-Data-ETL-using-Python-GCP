# Movies-Data-ETL-using-Python-GCP

## Overview

This project involves creating an ETL (Extract, Transform, Load) pipeline for movie rating data using Python and Google Cloud Platform (GCP). The ETL process includes:

1. **Downloading Movie Data**: Retrieves movie data from a public dataset.
2. **Processing Data**: Transforms the data into a CSV format.
3. **Creating a Cloud Storage Bucket**: Sets up a Google Cloud Storage bucket to store the data.
4. **Uploading Data**: Uploads the processed data to the Cloud Storage bucket.

## Prerequisites

- Python 3.6 or higher
- Google Cloud SDK
- Access to Google Cloud Platform (with billing enabled)

## Setup

### 1. Clone the Repository

```bash
(https://github.com/Youssef5lo/Movies-Data-ETL-using-Python-GCP.git)
```
### 2. Create and Activate a Virtual Environment
```bash
python -m venv newenv
source newenv/bin/activate  # On Windows: newenv\Scripts\activate
```
### 3. Install Dependencies
```bash
Copy code
pip install -r requirements.txt
```
### 4. Google Cloud Setup
Enable APIs: Ensure that the Cloud Storage and Cloud Storage JSON API are enabled in your GCP project.
Create a Service Account: Follow the steps to create a service account and download the JSON key file. Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of this file.
### 5. Configure the Scripts
create_bucket.py: Update the bucket_name with your desired unique bucket name.
process_data.py: Ensure that the path to the ml-100k directory is correct.
load_data.py: Update the bucket_name, source_file_name, and destination_blob_name as needed.
### 6. Run the ETL Process
Make download_data.sh Executable (if using Linux or macOS):

```bash
Copy code
chmod +x download_data.sh
```
## Execute the ETL Process:

```bash
Copy code
python movies_etl.py
```
## Project Files
create_bucket.py: Creates a new Google Cloud Storage bucket.
process_data.py: Processes raw movie data into CSV format.
load_data.py: Uploads processed CSV files to Google Cloud Storage.
movies_etl.py: Orchestrates the ETL process.
download_data.sh: Downloads and unzips the movie data (for Unix-like systems).
## Troubleshooting
ModuleNotFoundError: Ensure that all required Python packages are installed.
Permission Issues: Verify that your service account has the appropriate permissions in GCP.
FileNotFoundError: Check that all file paths are correct and files are in the expected locations.
## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
For questions or feedback, please contact [youssefmagdy2504@gmail.com].
