#!/usr/bin/python3

"""Lists 10 commits from a given github repo"""
import requests
from sys import argv

if __name__ == "__main__":
    user = argv[2]
    repo = argv[1]
    req = requests.get(f'https://api.github.com/repos/{user}/{repo}/commits')
    try:
        commits = req.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except ValueError:
        pass
