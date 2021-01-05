#!/usr/bin/python3
"""3-Square: Square Class"""


class Square:
    '''New Square'''

    def __init__(self, size=0, position=(0, 0)):
        '''attributes of the square'''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        '''define thr property of position'''
        return self.__position

    @position.setter
    def position(self, value):
        '''define the value of position'''
        if type(value) is not tuple or len(value) is not 2 or min(value) < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''area of square: public instance method'''
        return self.__size*self.__size

    def my_print(self):
        '''print the square with #'''
        number = self.__size
        tup = self.__position
        if tup[1] > 0:
            print("\n"*(tup[1]-1))
        for i in range(number):
            print(" "*tup[0], end="")
            print("#"*number)
        if number is 0:
            print("")
