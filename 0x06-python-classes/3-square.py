#!/usr/bin/python3
"""3-Square: Square Class"""


class Square:
    '''New Square'''

    def __init__(self, size=0):
        '''attributes of the square'''

        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''area of square: public instance method'''
        return self.__size*self.__size
