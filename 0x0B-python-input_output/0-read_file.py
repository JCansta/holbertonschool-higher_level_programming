#!/usr/bin/python3
"""
read file
"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read())
