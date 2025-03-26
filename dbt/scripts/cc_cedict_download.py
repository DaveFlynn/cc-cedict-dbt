# scripts/download_cc_cedict.py

import os
import requests
import zipfile
from io import BytesIO

CEDICT_URL = "https://www.mdbg.net/chinese/export/cedict/cedict_1_0_ts_utf-8_mdbg.zip"
DEST_FOLDER = "./data"
EXTRACTED_FILENAME = "cedict_ts.u8"
FINAL_FILENAME = "cc-cedict.txt"

def download_and_extract():
    print(f"Downloading CC-CEDICT from {CEDICT_URL}...")
    response = requests.get(CEDICT_URL)
    response.raise_for_status()

    print("Extracting zip file...")
    with zipfile.ZipFile(BytesIO(response.content)) as zip_ref:
        if not os.path.exists(DEST_FOLDER):
            os.makedirs(DEST_FOLDER)
        zip_ref.extract(EXTRACTED_FILENAME, DEST_FOLDER)

    # Rename to a consistent name
    os.rename(
        os.path.join(DEST_FOLDER, EXTRACTED_FILENAME),
        os.path.join(DEST_FOLDER, FINAL_FILENAME)
    )
    print(f"Saved to {os.path.join(DEST_FOLDER, FINAL_FILENAME)}")

if __name__ == "__main__":
    download_and_extract()