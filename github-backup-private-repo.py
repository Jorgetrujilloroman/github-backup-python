import requests
import datetime
import os
import shutil


#It is important to keep your token safe and don't share it with anyone.

def download_repo(repo_url, dest_folder, branch="main", token="Your_Token"):
    # Make a GET request to the GitHub API to download the repository as a zip file
    headers = {"Authorization": f"token {token}"}
    zip_url = f"{repo_url}/archive/{branch}.zip"
    response = requests.get(zip_url, headers=headers, stream=True)

    # If the response status code is not 200, raise an error
    if response.status_code != 200:
        raise ValueError(f"Failed to download repository. Status code: {response.status_code}")

    # Create the destination folder if it does not exist
    os.makedirs(dest_folder, exist_ok=True)

    # Save the contents of the zip file to a local file with the current date in the filename
    now = datetime.datetime.now()
    filename = f"Docs-conetnt-private-backup_{now.strftime('%Y-%m-%d-%H')}_{branch}h.zip"
    filepath = os.path.join(dest_folder, filename)

    with open(filepath, "wb") as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

    # Close the response to free up resources
    response.close()

    print(f"Repository downloaded to {filepath}")
    
#Modify download_repo function with your own parameters.
download_repo("https://github.com/GIT-USERNAME/PRIVATE-REPOSITORY", r"C:\Users\YOUR_USERNAME\Documents\Scripts\Python\github-backup-script\Backups\Private")