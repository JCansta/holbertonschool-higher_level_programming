#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = "https://api.github.com/repos/{}/{}/commits".format(
        argv[1], argv[2]
    )
    r = requests.get(r)
    commits = r.json()
    for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
