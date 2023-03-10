import os
import datetime

def delete_old_files(folder_path, hours_del):
    # Get the current time
    now = datetime.datetime.now()

    # Calculate the time threshold for deleting files
    threshold = now - datetime.timedelta(hours=hours_del)

    # Loop over all files in the folder
    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)

        # Check if the file is a zip file and is older than the threshold
        if filename.endswith(".zip") and os.path.getmtime(filepath) < threshold.timestamp():
            # Delete the file
            os.remove(filepath)
            print(f"Deleted old file: {filename}")

# Change the second parameter on the next functions to modify the erasin frequency. Defalut: 48h

delete_old_files(r"C:\Users\YOUR_USERNAME\Documents\Scripts\Python\github-backup-script\Backups\Private", 48)
delete_old_files(r"C:\Users\YOUR_USERNAME\Documents\Scripts\Python\github-backup-script\Backups\Public", 48)