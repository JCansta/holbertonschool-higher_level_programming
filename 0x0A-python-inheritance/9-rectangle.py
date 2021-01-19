#!/usr/bin/python3
"""
9-rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''new inherit class'''
    def __init__(self, width, height):
        '''init method'''
        super().integer_validator('width', width)
        super().integer_validator('height', height)
        self.__width = width
        self.__height = height

    def area(self):
        '''area  method'''
        return self.__width * self.__height

    def __str__(self):
        '''string method'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
