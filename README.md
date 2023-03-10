# github-backup-python
Python script and batch to make an extra security copy of a public or private GitHub repo.

To make it work you will need to follow the next steps:

1. Install [Python](https://www.python.org/downloads/) on your system.
2. If you want to backup a private repository you will need to [create an access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) to add in the "github-backup-script-v3-token.py" script.

## Scripts

To make the .py scripts work you have to edit them and modify the download_repo() functions setting your backup directory.

-delete-older-backups.py -> This script deletes backups older than 48 hours to save space on the disk. You can change the "cleaning" frequency by changing the second parameter of the function setting the erasing frequency in hours. It is 2 by default.

-github-backup-script.py -> This script saves a GitHub repository locally on the directory that you define on the download_repo() function.

-github-backup-script-branch.py -> Same that the previous but you can decide the branch that is going to be saved.

-github-backup-script-v3-token.py -> You have to introduce in this script an Access Token generated on GitHub as explained before to save private repositories.

## WINDOWS

To make bash files work, you have to edit the .bat bashes by right-clicking them and pressing "Edit". Then you have to replace "USERNAME" your Windows current user. 
When it is done you can run it manually. Do it for the three bashes.

You can manually run the sketches

I made this code work on a Windows system using the Task Scheduler, executing the batch files.

If you are using Windows, you can import the tasks stored in the folder by going to: Task Scheduler -> Actions -> Import Task -> Importing the tasks

You have to change the "Actions Start a Program" route by changing "USERNAME" to your Windows current user. 

By default, the tasks are executed each hour but you can change it by: Double click on the task -> Triggers -> Edit

## LINUX

(Coming soon...)








