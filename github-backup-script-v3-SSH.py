import os
import subprocess

# Set the repository details
username = 'your-github-username'
repository = 'your-repo-name'
branch = 'main'
local_path = '/path/to/local/directory'

# Set the SSH URL for the repository
repo_url = f'git@github.com:{username}/{repository}.git'

# Set the path to the SSH key file
ssh_key_path = '/path/to/ssh/key'

# Clone the repository using SSH authentication
subprocess.run(f'git clone -b {branch} {repo_url} {local_path}', shell=True, check=True, env={'GIT_SSH_COMMAND': f'ssh -i {ssh_key_path}'})

print(f"Repository {repository} downloaded successfully.")