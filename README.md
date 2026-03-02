# GitHub User Activity CLI

A Python command-line tool that fetches and formats recent GitHub activity for a given user using the GitHub public API.

## Features
- Fetches recent GitHub events for any public user
- Groups activity by event type (Push, Pull Request, Issues, etc.)
- Safely handles missing or inconsistent API data
- Outputs a structured `.txt` activity report
- Uses only Python standard library for HTTP and JSON parsing

## Example Usage
```bash
py github-activity.py USERNAME