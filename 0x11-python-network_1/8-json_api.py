#!/usr/bin/python3
"""
will get the type, conten and utf check of a url
"""
import requests
from sys import argv

if __name__ == "__main__":

    value = "" if len(argv) == 1 else argv[1]

    r = requests.post("http://0.0.0.0:5000/search_user", data=value)
    try:
        string = r.json()
        if string == {}:
            print("No result")
        else:
            print("[{}] {}".format(string.get("id"), string.get("name")))
    except ValueError:
        print("Not a valid JSON")
