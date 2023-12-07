#!/usr/bin/python3
"""
A Python script that takes your GitHub credentials 
(username and password) and 
uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys
    from sys import argv
    if len(argv) != 3:
        print(f"Usage: {argv[0]} <username> <password>", file=sys.stderr)
        exit(1)

    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(argv[1], argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)

