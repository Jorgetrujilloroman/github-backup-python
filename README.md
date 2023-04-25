# github-backup-python
Python script and Windows/Linux batch to make an extra security copy of a public or private GitHub repository downloading it locally every 2 hours and cleaning old copies to save space on the disk.

To make it work you will need to follow the next steps:

1. Install [Python 3.11.x](https://www.python.org/downloads/) on your system.

2. If you want to backup a private repository you will need to [create an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to add to the **"secrets.ini"** file allowing download private repositories.

3. Download (clone) this repository and save it in a folder of your choice.

## SCRIPT

-To allow the script works you have to open/edit the secrets.ini file and replace the <> parameters setting your Personal Access Token, the GitHub private and public repositories and your backup directories: 

```
[credentials]
token = <Your_Personal_Access_GitHub_Token>

[repositories]
private_repository_url = <GitHub_Private_Repo_URL>
public_repository_url = <GitHub_Public_Repo_URL>

[backup-folders]
private_backup_folder = <Private_Backup_Folder_Full_Path>
public_backup_folder = <Public_Backup_Folder_Full_Path>
```

- If you only need to download a public or a private repository, you can comment/delete the download_repo() functions in the .py script (lines 87 and/or 92):

```
87 - //download_repo(private_repository_url, private_backup_folder, token)

92 - //download_repo(public_repository_url, public_backup_folder, token)
```

## WINDOWS

If you are using Windows, to make the bash file work, you only have to test if the .bat script is working by double-clicking it. If it works properly, a cmd window will be opened and the scripts will start running. 

I made this code works on a Windows system using the Task Scheduler to automatize the process, by executing the batch file periodically.

If you are using Windows, you can import the task named *"GitHub-Backup-Script-Automation.xml"* by going to ```Task Scheduler -> Actions -> Import Task -> Importing the tasks```

While importing the task, you have to change the "Actions Start a Program" route by going to ```Actions -> Edit -> Browse``` and choosing the **"github-backup-script.py"** on the folder where you downloaded it. 

By default, the tasks are executed each hour but you can change it by ```Double click on the task -> Triggers -> Edit```

If you prefer you can **create your own task** by following the next steps:

1. Open Task Scheduler by searching for it in the Start menu.

2. Click on "Create Task" in the "Actions" pane on the right.

3. In the "General" tab, give the task a name and description.

4. In the "Triggers" tab, click "New" to set when the task should run (e.g. daily at a specific time).

5. In the "Actions" tab, click "New" and select "Start a program".

6. Browse to the location of the downloaded "github-backup-script.py" script and select it.

7. In the "Conditions" tab, you can set additional criteria for when the task should run (e.g. only when the computer is plugged in).

8. In the "Settings" tab, you can configure options such as whether the task should run even if the user is not logged in.

9. Click "OK" to save the task.

## LINUX

To make it work on a Linux OS you will need to automate the execution of the Python script by creating a .sh bash and scheduling its execution using [Cron](https://man7.org/linux/man-pages/man8/cron.8.html) 

To do it follow the next steps:

1. Create a new file named *backups-automation-batch.sh* in a directory of your choice.
2. Open the file in a text editor and add the following lines:

```
#!/bin/bash

# Run Python script
/usr/bin/python3 /path/to/script.py
```

Replace /path/to/first/script.py with the path to the Python script downloaded on this repository. 

3. Save the file and exit the text editor.
4. Make the script executable by running the command: ```chmod +x /path/to/backups-automation-batch.sh```
5. You can test the script by running it manually: ```/path/to/backups-automation-batch.sh```

This should execute all three Python scripts in order.

6. Schedule the script to run every hour using cron. Open the crontab file by running the command: ```crontab -e```

Add the following line at the bottom of the file:

```0 * * * * /path/to/backups-automation-batch.sh```

This will run the *backups-automation-batch.sh* file every hour at the start of the hour. Save the file and exit the text editor.

That's it! Your Python scripts should now be executed automatically every hour. You can check the logs in ```/var/log/syslog``` to confirm that the script is being executed.


