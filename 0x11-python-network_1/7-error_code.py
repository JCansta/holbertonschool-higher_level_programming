#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import requests
from sys import argv

if __name__ == "__main__":
    r = requests.get(argv[1])

    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
