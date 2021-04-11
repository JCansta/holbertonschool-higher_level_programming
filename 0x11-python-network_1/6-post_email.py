#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    values = {"email": argv[2]}

    r = requests.post(url, data=values)
    print(r.text)
