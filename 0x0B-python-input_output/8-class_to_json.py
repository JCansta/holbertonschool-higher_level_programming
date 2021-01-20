#!/usr/bin/python3
"""
class to json
"""


def class_to_json(obj):
    '''class to json'''
    io = obj.__dict__
    return io
