#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import urllib.request
import urllib.parse
import urllib.error
from sys import argv

if __name__ == "__main__":

    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode("ascii")
        print(html)
    except urllib.error.HTTPError as e:
        print("Error Code: {}".format(e))
