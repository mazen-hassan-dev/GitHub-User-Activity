import requests
import json
import os

def safe_get(data, *keys, default=None):
    for key in keys:
        if isinstance(data, dict):
            data = data.get(key)
        else:
            return default
        if data is None:
            return default
    return data

def getUserActivity(username):

    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:

        all_events = response.json()

        event_types = {
            "PushEvent" : [],
            "PullRequestEvent" : [],
            "PullRequestReviewEvent" : [],
            "PullRequestReviewCommentEvent" : [],
            "IssuesEvent" : [],
            "IssueCommentEvent" : [],
            "WatchEvent" : [],
            "CreateEvent" : [],
            "Other" : []
        }
        
        for event in all_events:

            if event['type'] == "PushEvent":
                repoName = event['repo']['name']
                repoID = event['repo']['id']
                commitCount = safe_get(event, 'payload', 'size', default=0)
                event_types["PushEvent"].append(f"Pushed ({commitCount}) commits to '{repoName}'. ID: ({repoID})")
            
            elif event['type'] == "PullRequestEvent":
                pull_num = safe_get(event, 'payload', 'pull_request', 'number', default=0)
                event_types["PullRequestEvent"].append(f"Created pull request {pull_num}).")
            
            elif event['type'] == "PullRequestReviewEvent":
                pull_num = safe_get(event, 'payload', 'pull_request', 'number', default=0)
                event_types["PullRequestReviewEvent"].append(f"Reviewed pull request: ({pull_num}).")

            elif event['type'] == "PullRequestReviewCommentEvent":
                pull_num = safe_get(event, 'payload', 'pull_request', 'number', default=0)
                event_types["PullRequestReviewCommentEvent"].append(f"Commented on pull request: ({pull_num}).")

            elif event['type'] == "IssuesEvent":
                issue_num = safe_get(event, 'payload', 'issue', 'number', default=0)
                event_types["IssuesEvent"].append(f"Created issue: {issue_num}.")

            elif event['type'] == "IssueCommentEvent":
                pull_num = safe_get(event, 'payload', 'pull_request', 'number', default=0)
                event_types["IssueCommentEvent"].append(f"Commented on issue: ({issue_num}).")

            elif event['type'] == "WatchEvent":
                repoName = event['repo']['name']
                event_types["WatchEvent"].append(f"Starred repository: {repoName}.")

            elif event['type'] == "CreateEvent":
                repoName = event['repo']['name']
                repoID = event['repo']['id']
                event_types["CreateEvent"].append(f"Created repository: {repoName}. ID: ({repoID})")

            else:
                event_types["Other"].append(f"{username} did the following {event['type']} to the repository {event['repo']['name']}")
    
        
        USER_FILE = f"{username}.txt"

        with open(USER_FILE, "w") as f:
            f.write(f"{username}\n")
            f.write("*" * len(username) + "\n\n")

            for header, items in event_types.items():
                f.write(f"\n{header}:\n")
                f.write("*" * len(header) + "\n")
                for item in items:
                    f.write(f"-- {item}\n")
    
    else:
        print(f"Error fetching user activity for: {username}. | Error Code: {response.status_code}")

    
