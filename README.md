# Metadata-repo-

Script to swap repository descriptions using GitHub API.

## Requirements

- Python 3.10 or higher

## Installation

```bash
pip install -e .
```

## Usage

Edit `swap_metadata.py` with your GitHub credentials and repository URLs, then run:

```bash
python swap_metadata.py
```

## Python 3.10+ Features

This project uses Python 3.10+ syntax features including:
- PEP 604: Union type operator `|` for type hints (e.g., `str | None` instead of `Optional[str]`)
- PEP 585: Built-in generic types (e.g., `dict[str, str]` instead of `Dict[str, str]`)
