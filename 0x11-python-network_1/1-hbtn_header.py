#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import urllib.request
from sys import argv
if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        html = response.info()
    print(html['X-Request-Id'])
