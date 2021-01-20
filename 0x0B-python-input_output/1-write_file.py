#!/usr/bin/python3
"""
write a file
"""


def write_file(filename="", text=""):
    '''write a file'''
    with open(filename, mode="w", encoding="utf-8") as myFile:
        myFile.write(text)
    return len(text)
