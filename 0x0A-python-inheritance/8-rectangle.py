#!/usr/bin/python3
"""
8-rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''new inherit class'''
    def __init__(self, width, height):
        '''init method'''
        if super().integer_validator('width', width):
            self.__width = width
        if super().integer_validator('height', height):
            self.__height = height
