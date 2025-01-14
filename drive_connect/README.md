# Google Drive Integration Script

This script facilitates seamless integration with Google Drive using the Google Drive API. It includes functionalities to:

- Authenticate and connect to Google Drive using a service account.
- Create folders in Google Drive.
- Upload local folders and their structure to Google Drive.
- Upload or update individual files in Google Drive.
- Search for files in Google Drive by name.

## Prerequisites

1. **Google Cloud Project**
   - Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Google Drive API for your project.

2. **Service Account**
   - Create a service account in your Google Cloud project.
   - Download the JSON key file for the service account and save it in the project directory (e.g., `drive_connect/client_secrets.json`). *(Replace `drive_connect/client_secrets.json` with the actual path to your service account JSON file if different.)*
   - Share the desired Google Drive folders with the service account email.

3. **Python Libraries**
   - Install the required Python libraries:
     ```bash
     pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
     ```

## Configuration

- Update the `SERVICE_ACCOUNT_FILE` variable with the path to your service account JSON key file. *(Replace `SERVICE_ACCOUNT_FILE` with the correct path to your key file.)*
- Specify the `google_drive_parent_folder_id` variable with the ID of the Google Drive folder where files and folders will be uploaded. *(Replace `google_drive_parent_folder_id` with the ID of your target Google Drive folder.)*

## Functions

### `connect_to_drive(service_account_file: str)`

Authenticates and connects to Google Drive using a service account.

- **Arguments**:
  - `service_account_file`: Path to the service account JSON key file. *(Ensure the correct file path is provided.)*
- **Returns**: Authenticated Google Drive API client service.

### `create_drive_folder(folder_name: str, parent_folder_id: str, drive_service)`

Creates a folder in Google Drive.

- **Arguments**:
  - `folder_name`: Name of the folder to create.
  - `parent_folder_id`: ID of the parent Google Drive folder. *(Ensure the parent folder ID is correct.)*
  - `drive_service`: Authenticated Google Drive API service.
- **Returns**: ID of the created folder.

### `upload_folder_structure(local_folder_path: str, drive_folder_id: str, drive_service)`

Uploads a local folder structure to Google Drive.

- **Arguments**:
  - `local_folder_path`: Path to the local folder to upload. *(Ensure the correct folder path is provided.)*
  - `drive_folder_id`: ID of the parent Google Drive folder. *(Ensure the parent folder ID is correct.)*
  - `drive_service`: Authenticated Google Drive API service.
- **Returns**: Mapping of local folder paths to Google Drive folder IDs.

### `upload_file_to_drive(file_path: str, file_name: str, folder_id: str, drive_service)`

Uploads a single file to Google Drive.

- **Arguments**:
  - `file_path`: Local path to the file. *(Ensure the correct file path is provided.)*
  - `file_name`: Name of the file in Google Drive.
  - `folder_id`: ID of the Google Drive folder. *(Ensure the parent folder ID is correct.)*
  - `drive_service`: Authenticated Google Drive API service.

### `find_file_in_drive(file_name: str, folder_id: str, drive_service)`

Finds a file by name in a Google Drive folder.

- **Arguments**:
  - `file_name`: Name of the file to search for.
  - `folder_id`: ID of the Google Drive folder. *(Ensure the parent folder ID is correct.)*
  - `drive_service`: Authenticated Google Drive API service.
- **Returns**: ID of the found file, or `None` if not found.

### `upload_or_update_file_to_drive(file_path: str, file_name: str, folder_id: str, drive_service)`

Uploads or updates a file in a Google Drive folder.

- **Arguments**:
  - `file_path`: Local path to the file. *(Ensure the correct file path is provided.)*
  - `file_name`: Name of the file in Google Drive.
  - `folder_id`: ID of the Google Drive folder. *(Ensure the parent folder ID is correct.)*
  - `drive_service`: Authenticated Google Drive API service.

## Usage

1. Ensure that your service account JSON file is in the correct location as specified in `SERVICE_ACCOUNT_FILE`. *(Replace the path if necessary.)*
2. Set the desired parent Google Drive folder ID in `google_drive_parent_folder_id`. *(Replace the ID with your folder ID.)*
3. Use the provided functions in your Python script to interact with Google Drive.

Example:
```python
# Authenticate and connect to Google Drive
drive_service = connect_to_drive(SERVICE_ACCOUNT_FILE)

# Create a folder in Google Drive
folder_id = create_drive_folder("My Folder", drive_service=drive_service)

# Upload a file to the created folder
upload_file_to_drive("local_path/file.txt", "file.txt", folder_id, drive_service)

# Upload an entire folder structure
upload_folder_structure("local_folder", folder_id, drive_service)
```

## Notes

- Ensure that the service account has appropriate permissions for the target Google Drive folders.
- Handle exceptions and errors (e.g., invalid file paths, API errors) as needed for robustness.

## License

This script is provided under the MIT License. Modify and distribute as needed.

