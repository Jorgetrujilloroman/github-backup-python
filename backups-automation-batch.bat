::This Windows bash execute the python scripts created to backup github repositories.

@echo off
echo -- Running GitHub Backup Script --
python "%~dp0\github-backup-script.py"
set /p DUMMY=Hit ENTER to exit..