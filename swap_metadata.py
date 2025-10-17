"""Script to swap repository descriptions using GitHub API."""
import requests


def swap_repository_descriptions(
    username: str,
    token: str,
    repo1_path: str,
    repo2_path: str
) -> dict[str, str | None]:
    """
    Swap descriptions between two GitHub repositories.
    
    Args:
        username: GitHub username for authentication
        token: GitHub personal access token
        repo1_path: First repository path (format: 'owner/repo')
        repo2_path: Second repository path (format: 'owner/repo')
        
    Returns:
        Dictionary with status of the swap operation
    """
    # Retrieve repository information for each repository
    response1 = requests.get(
        f"https://api.github.com/repos/{repo1_path}",
        auth=(username, token)
    )
    response2 = requests.get(
        f"https://api.github.com/repos/{repo2_path}",
        auth=(username, token)
    )
    
    # Check for errors in retrieving repository information
    if response1.status_code != 200 or response2.status_code != 200:
        return {
            "repo1_status": "failed" if response1.status_code != 200 else "success",
            "repo2_status": "failed" if response2.status_code != 200 else "success",
            "error": f"Failed to retrieve repository information. Status codes: {response1.status_code}, {response2.status_code}",
        }
    
    repo1_info = response1.json()
    repo2_info = response2.json()
    
    # Swap repository descriptions
    repo1_description = repo1_info.get("description")
    repo2_description = repo2_info.get("description")
    
    # Update repository information for each repository
    update1 = requests.patch(
        f"https://api.github.com/repos/{repo1_path}",
        auth=(username, token),
        json={"description": repo2_description}
    )
    update2 = requests.patch(
        f"https://api.github.com/repos/{repo2_path}",
        auth=(username, token),
        json={"description": repo1_description}
    )
    
    return {
        "repo1_status": "success" if update1.status_code == 200 else "failed",
        "repo2_status": "success" if update2.status_code == 200 else "failed",
        "repo1_new_description": repo2_description,
        "repo2_new_description": repo1_description,
    }


if __name__ == "__main__":
    # GitHub API credentials
    username = "your_username"
    token = "your_token"
    
    # Repository paths (format: owner/repo)
    repo1_path = "user/repo1"
    repo2_path = "user/repo2"
    
    result = swap_repository_descriptions(username, token, repo1_path, repo2_path)
    print(f"Swap completed: {result}")
