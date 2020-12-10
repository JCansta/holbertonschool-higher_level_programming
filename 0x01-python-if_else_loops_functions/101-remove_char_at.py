#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    for i in range(len(str)):
        if i is not n:
            new += str[i]
    return new
