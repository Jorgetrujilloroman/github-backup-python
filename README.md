# github-backup-python
Python script and batch to make an extra security copy of a public or private GitHub repository.

To make it work you will need to follow the next steps:

1. Install [Python](https://www.python.org/downloads/) on your system.
2. If you want to backup a private repository you will need to [create an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to add in the "github-backup-private-repo.py" script.

## SCRIPTS

To make the .py scripts work you have to edit them and modify the **download_repo()** functions setting your GitHub repository and your backup directory.

-**delete-older-backups.py** -> This script deletes backups older than 48 hours to save space on the disk. You can change the "cleaning" frequency by changing the second parameter of the function setting the erasing frequency in hours. It is 48h by default.

-**github-backup-public-repo.py** -> This script saves a public GitHub repository locally on the directory that you define on the download_repo() function. You can also change the branch to backup changing the third parameter on the same function.

-**github-backup-private-repo.py** -> This script saves a private GitHub repository locally on the directory that you define on the download_repo() function. You need to introduce in the function an Access Token previously generated on GitHub as explained before to save private repositories.

## WINDOWS

To make the bash file work, you have to edit the .bat bash file named **"backups-automation-batch.bat"** by right-clicking them and pressing "Edit". Then you have to replace "USERNAME" your Windows current user in the three python commands. 

You can test if the bat script is working by double-clicking it. If it works properly, a cmd window will be opened and the scripts will start running. 

I made this code work on a Windows system using the Task Scheduler to automatize the process, by executing the batch file periodically.

If you are using Windows, you can import the task named *"GitHub-Backup-Script-Automation.xml"* by going to ```Task Scheduler -> Actions -> Import Task -> Importing the tasks```

You have to change the "Actions Start a Program" route by changing "USERNAME" to your Windows current user. 

By default, the tasks are executed each hour but you can change it by ```Double click on the task -> Triggers -> Edit```

## LINUX

To make it work on a Linux OS you will need to automatice the execution of the python scripts by creating a .sh bash and schedule its execution using [Cron](https://man7.org/linux/man-pages/man8/cron.8.html) 

To do it follow the next steps:

1. Create a new file named *backups-automation-batch.sh* in a directory of your choice.
2. Open the file in a text editor and add the following lines:

```
#!/bin/bash

# Run first Python script
/usr/bin/python3 /path/to/first/script.py

# Run second Python script
/usr/bin/python3 /path/to/second/script.py

# Run third Python script
/usr/bin/python3 /path/to/third/script.py
```

Replace /path/to/first/script.py, /path/to/second/script.py, and /path/to/third/script.py with the paths to the Python scripts downloaded on this repository. 

3. Save the file and exit the text editor.
4. Make the script executable by running the command: ```chmod +x /path/to/backups-automation-batch.sh```
5. You can test the script by running it manually: ```/path/to/backups-automation-batch.sh```

This should execute all three Python scripts in order.

6. Schedule the script to run every hour using cron. Open the crontab file by running the command: ```crontab -e```

Add the following line at the bottom of the file:

```0 * * * * /path/to/backups-automation-batch.sh```

This will run the *backups-automation-batch.sh* file every hour at the start of the hour. Save the file and exit the text editor.

That's it! Your Python scripts should now be executed automatically every hour. You can check the logs in ```/var/log/syslog``` to confirm that the script is being executed.


