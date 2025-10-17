# Metadata-repo-

Script to swap repository descriptions using GitHub API.

## Requirements

- Python 3.10 or higher

## Installation

```bash
pip install -e .
```

## Usage

Edit `swap_metadata.py` with your GitHub credentials and repository paths, then run:

```bash
python swap_metadata.py
```

Example configuration:
```python
username = "your_username"
token = "your_personal_access_token"
repo1_path = "owner/repository1"  # Format: owner/repo
repo2_path = "owner/repository2"  # Format: owner/repo
```

## Python 3.10+ Features

This project uses Python 3.10+ syntax features including:
- PEP 604: Union type operator `|` for type hints (e.g., `str | None` instead of `Optional[str]`)
- PEP 585: Built-in generic types (e.g., `dict[str, str]` instead of `Dict[str, str]`)
