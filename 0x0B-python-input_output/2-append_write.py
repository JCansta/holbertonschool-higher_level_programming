#!/usr/bin/python3
"""
append write
"""


def append_write(filename="", text=""):
    '''append a string to new file'''
    with open(filename, mode="a", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
