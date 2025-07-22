import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Path to your service account JSON key file
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account.json'

# Define your required scopes
SCOPES = ['https://www.googleapis.com/auth/drive.file']

def initialize_gdrive():
    # Check if the credentials file exists
    if not os.path.exists(SERVICE_ACCOUNT_FILE):
        raise FileNotFoundError(f"Service account file not found at {SERVICE_ACCOUNT_FILE}")

    # Load credentials from the JSON key file
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # Build the Drive API client
    drive_service = build('drive', 'v3', credentials=creds)
    return drive_service

def upload_file(file_path, filename):
    drive_service = initialize_gdrive()

    file_metadata = {'name': filename}
    media = MediaFileUpload(file_path, resumable=True)

    # Upload the file
    file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    print(f"File ID: {file.get('id')} uploaded successfully.")

if __name__ == '__main__':
    # Example usage
    file_path = 'path/to/file/to/upload.ext'
    filename = 'uploaded_filename.ext'

    upload_file(file_path, filename)
