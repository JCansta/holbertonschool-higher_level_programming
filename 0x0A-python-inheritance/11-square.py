#!/usr/bin/python3
"""
11-square: new inehrit
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''new class'''
    def __init__(self, size):
        '''init class'''
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        '''string in return'''
        return ("[Square] {}/{}".format(self.__size, self.__size))
