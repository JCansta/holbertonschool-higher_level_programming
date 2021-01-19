#!/usr/bin/python3
"""
10-square: new inehrit
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''new class'''
    def __init__(self, size):
        '''init class'''
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
