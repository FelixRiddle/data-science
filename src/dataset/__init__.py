import re
import gdown
import os


def extract_file_id(url: str):
    """Extracts file_id from a Google Drive URL."""
    # Regex looks for the pattern between /d/ and /
    match = re.search(r"/d/([a-zA-Z0-9_-]+)", url)
    if match:
        return match.group(1)
    return None


def download_dataset(file_id: str, filename: str):
    """Download dataset from Google Drive"""
    # Google Drive download URL template
    url = f"https://drive.google.com/uc?id={file_id}"

    # Optional: Ensure the 'data/raw' directory exists (standard DS practice)
    output_path = os.path.join("data", "raw", filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    print(f"Downloading {filename}...")

    # gdown handles the authentication tokens and large file cookies automatically
    gdown.download(url, output_path, quiet=False)

    print(f"Dataset saved to: {output_path}")


def download_dataset_from_url(url: str):
    # Extract the ID from the link using Regex
    file_id = extract_file_id(url)
    if not file_id:
        print("Error: Invalid Google Drive URL.")
        return

    # Direct download URL for gdown
    download_url = f"https://drive.google.com/uc?id={file_id}"

    print(f"Connecting to Google Drive (ID: {file_id})...")

    # download() returns the path of the downloaded file
    downloaded_path = gdown.download(download_url, None, quiet=False)

    print(f"Successfully downloaded: {downloaded_path}")
