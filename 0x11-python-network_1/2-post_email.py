#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}

    data = urllib.parse.urlencode(values).encode("ascii")

    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
