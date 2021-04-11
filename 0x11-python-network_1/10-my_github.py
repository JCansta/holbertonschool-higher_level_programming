#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import requests
from sys import argv

if __name__ == "__main__":
    auth = requests.auth.HTTPBasicAuth(argv[1], argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
