import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

SCOPES = ["https://www.googleapis.com/auth/drive"]

creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

try:
    service = build("drive", "v3", credentials=creds)

    response = (
        service.files()
        .list(
            q="name='cat-1-backup' and mimeType='application/vnd.google-apps.folder'",
            spaces="drive",
        )
        .execute()
    )

    if not response["files"]:
        file_metadata = {
            "name": "cat-1-backup",
            "mimeType": "application/vnd.google-apps.folder",
        }
        file = service.files().create(body=file_metadata, fields="id").execute()
        folder_id = file.get("id")
    else:
        folder_id = response["files"][0]["id"]

    # Define a function to upload files and subdirectories recursively
    def upload_directory(folder_id, folder_path):
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):
                # If it's a subdirectory, create a folder in Google Drive and upload its contents
                subfolder_metadata = {
                    "name": item,
                    "parents": [folder_id],
                    "mimeType": "application/vnd.google-apps.folder",
                }
                subfolder = (
                    service.files()
                    .create(body=subfolder_metadata, fields="id")
                    .execute()
                )
                subfolder_id = subfolder.get("id")
                upload_directory(subfolder_id, item_path)
            elif os.path.isfile(item_path):
                # If it's a file, upload it to the current folder in Google Drive
                file_metadata = {"name": item, "parents": [folder_id]}
                media = MediaFileUpload(item_path)
                upload_file = (
                    service.files()
                    .create(body=file_metadata, media_body=media, fields="id")
                    .execute()
                )
                print("Backed up file:", item)

    # Upload the entire "outputs" folder and its contents recursively
    upload_directory(folder_id, "outputs")

except HttpError as e:
    print("Error: " + str(e))
