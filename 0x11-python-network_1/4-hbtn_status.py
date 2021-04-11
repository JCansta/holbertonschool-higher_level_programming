#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import requests
from sys import argv

if __name__ == "__main__":
    html = requests.get('https://intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
