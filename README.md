# GitHub User Activity CLI

A Python command-line tool that fetches and formats a GitHub user's recent public activity using the GitHub Events API.  
The tool groups events by type and generates a structured activity report as a `.txt` file.

---

## Features

- Fetches recent public GitHub events for any user
- Groups activity by event type (Push, Pull Requests, Issues, Reviews, etc.)
- Safely handles nested JSON fields to prevent runtime crashes
- Generates a structured `<username>.txt` activity report
- Gracefully handles invalid usernames and API errors
- Built using only Python standard library modules

---

## How It Works

1. Sends an HTTP request to GitHub's public events endpoint.
2. Parses the JSON response.
3. Safely extracts nested fields using defensive JSON access.
4. Groups events by type.
5. Writes a structured text report.

---

## Installation

No external dependencies required.

Requirements:
- Python 3.9+

---

## Usage

```bash
python github-activity.py <username>