import shutil
import requests
import os
import zipfile # for unzipping archives
print("Downloading and unzipping archives...")
def download_file(url):
    local_filename = os.path.expanduser("~") + "/" + url.split('/')[-1]
    with requests.get(url, stream=True) as r:
        with open(local_filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

    return local_filename
file = download_file("https://github.com/Tyler887/typoqsuat/archive/refs/heads/ghpages.zip"
with zipfile.ZipFile(file) ,"r") as zip_ref:
    zip_ref.extractall(os.path.expanduser("~") + "/Typoqsuat")

print("Deleting archives...")
os.unlink(file)
print("done :)")
