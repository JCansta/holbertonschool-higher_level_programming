#!/usr/bin/python3
"""3-Square: Square Class"""


class Square:
    '''New Square'''

    def __init__(self, size=0):
        '''attributes of the square'''
        self.size = size

    @property
    def size(self):
        '''define the property of size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''define the value of size'''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        '''area of square: public instance method'''
        return self.__size*self.__size
