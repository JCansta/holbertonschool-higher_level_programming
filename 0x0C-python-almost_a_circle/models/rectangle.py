#!/usr/bin/python3
"""
rectangle class
"""


from models.base import Base


class Rectangle(Base):
    '''new rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''init class'''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        '''str function'''
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                                                       self.__x,
                                                       self.__y,
                                                       self.__width,
                                                       self.__height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate('y', value)
        self.__y = value

    @classmethod
    def __validate(cls, name, value):
        '''validate the values of the attributes'''
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if name is 'width' or name is 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(name))
        if name is 'x' or name is 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(name))

    def area(self):
        '''area of the rectangle is calculated'''
        return self.__height * self.__width

    def display(self):
        '''prints the rectangle with #'''
        print("\n"*self.__y, end="")
        for i in range(self.__height):
            print(" "*self.__x, end="")
            print('#'*self.__width)

    def update(self, *args, **kwargs):
        '''update data'''
        var = ["id", "width", "height", "x", "y"]
        if args:
            for key, item in zip(var, args):
                setattr(self, key, item)
        else:
            for key, item in kwargs.items():
                if key in var:
                    setattr(self, key, item)

    def to_dictionary(self):
        '''return a dictionary representation of the class'''
        dic = {}
        keys = ['x', 'y', 'id', 'height', 'width']
        for k in keys:
            dic[k] = getattr(self, k)
        return dic
