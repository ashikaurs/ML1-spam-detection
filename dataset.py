import urllib.request
import zipfile
import os

url = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"

os.makedirs("data", exist_ok=True)

zip_path = "data/dataset.zip"

print("Downloading dataset...")

urllib.request.urlretrieve(url, zip_path)

print("Download complete.")

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall("data")

print("Dataset extracted.")

os.remove(zip_path)

print("Done!")