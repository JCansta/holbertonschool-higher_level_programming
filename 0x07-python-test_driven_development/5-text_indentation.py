#!/usr/bin/python3
def text_indentation(text):
    """text_indentation"""
    if text is None:
        return
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        print(i, end="")
        if ord(i) in [46, 58, 63]:
            print("\n")
