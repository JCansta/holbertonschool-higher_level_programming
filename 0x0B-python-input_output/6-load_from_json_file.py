#!/usr/bin/python3
"""
load from json file
"""


import json


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="utf-8") as myFile:
        io = myFile.read()
    return json.loads(io)
