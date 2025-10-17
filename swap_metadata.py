"""Script to swap repository descriptions using GitHub API."""
import requests


def swap_repository_descriptions(
    username: str,
    token: str,
    repo1_url: str,
    repo2_url: str
) -> dict[str, str | None]:
    """
    Swap descriptions between two GitHub repositories.
    
    Args:
        username: GitHub username for authentication
        token: GitHub personal access token
        repo1_url: First repository URL
        repo2_url: Second repository URL
        
    Returns:
        Dictionary with status of the swap operation
    """
    # Retrieve build information for each repository
    repo1_info = requests.get(
        f"https://api.github.com/repos/{repo1_url}",
        auth=(username, token)
    ).json()
    repo2_info = requests.get(
        f"https://api.github.com/repos/{repo2_url}",
        auth=(username, token)
    ).json()
    
    # Swap build information
    repo1_description = repo1_info["description"]
    repo2_description = repo2_info["description"]
    
    repo1_info["description"] = repo2_description
    repo2_info["description"] = repo1_description
    
    # Update build information for each repository
    response1 = requests.patch(
        f"https://api.github.com/repos/{repo1_url}",
        auth=(username, token),
        json=repo1_info
    )
    response2 = requests.patch(
        f"https://api.github.com/repos/{repo2_url}",
        auth=(username, token),
        json=repo2_info
    )
    
    return {
        "repo1_status": "success" if response1.status_code == 200 else "failed",
        "repo2_status": "success" if response2.status_code == 200 else "failed",
        "repo1_new_description": repo2_description,
        "repo2_new_description": repo1_description,
    }


if __name__ == "__main__":
    # GitHub API credentials
    username = "your_username"
    token = "your_token"
    
    # Repository URLs
    repo1_url = "https://github.com/user/repo1.git"
    repo2_url = "https://github.com/user/repo2.git"
    
    result = swap_repository_descriptions(username, token, repo1_url, repo2_url)
    print(f"Swap completed: {result}")
