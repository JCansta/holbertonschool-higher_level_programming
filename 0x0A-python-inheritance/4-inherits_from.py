#!/usr/bin/python3
"""
4-inherits_from: heredar
"""


def inherits_from(obj, a_class):
    '''hola'''
    return issubclass(type(obj), a_class) and not type(obj) == a_class
