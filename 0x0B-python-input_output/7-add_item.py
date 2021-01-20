#!/usr/bin/python3
"""
add item
"""
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    '''add item'''
    myFile = "add_item.json"
    new = []
    sys.argv.pop(0)
    for i in sys.argv:
        new.append(i)

    if os.stat(myFile).st_size == 0:
        save_to_json_file(new, myFile)
    else:
        myObj = load_from_json_file(myFile)
        myObj = myObj + new
        save_to_json_file(myObj, myFile)
