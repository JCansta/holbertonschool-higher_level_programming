#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        num = fct(*args)
    except Exception as en:
        print("Exception:", en, file=sys.stderr)
        return None
    return num
