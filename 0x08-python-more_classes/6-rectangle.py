#!/usr/bin/python3
'''2-rectangle: new classes'''


class Rectangle():
    '''new rectangle'''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        '''create new object'''
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        '''calculate the area of the rectangle object'''
        return self.__width*self.__height

    def perimeter(self):
        '''calculate the perimeter of the rectangle'''
        if self.__width is 0 or self.__height is 0:
            return 0
        return (self.__width*2)+(self.__height*2)

    def __str__(self):
        '''str function'''
        new = ""
        if self.__height is 0 or self.__width is 0:
            return new
        for i in range(self.__height):
            new += ("#"*self.__width)
            if i < self.__height-1:
                new += "\n"
        return new

    def __repr__(self):
        '''repr function'''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''delete an object'''
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
