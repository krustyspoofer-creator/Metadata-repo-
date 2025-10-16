# Metadata-repo-
import requests

# GitHub API credentials
username = "your_username"
token = "your_token"

# Repository URLs
repo1_url = "https://github.com/user/repo1.git"
repo2_url = "https://github.com/user/repo2.git"

# Retrieve build information for each repository
repo1_info = requests.get(f"https://api.github.com/repos/{repo1_url}", auth=(username, token)).json()
repo2_info = requests.get(f"https://api.github.com/repos/{repo2_url}", auth=(username, token)).json()

# Swap build information
repo1_info["description"] = repo2_info["description"]
repo2_info["description"] = repo1_info["description"]

# Update build information for each repository
requests.patch(f"https://api.github.com/repos/{repo1_url}", auth=(username, token), json=repo1_info)
requests.patch(f"https://api.github.com/repos/{repo2_url}", auth=(username, token), json=repo2_info)
