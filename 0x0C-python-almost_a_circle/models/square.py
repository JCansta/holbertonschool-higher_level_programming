#!/usr/bin/python3
"""
square class
"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    '''new square class'''

    def __init__(self, size, x=0, y=0, id=None):
        '''init for square'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''str method'''
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update data'''
        var = ["id", "size", "x", "y"]
        if args:
            for key, item in zip(var, args):
                setattr(self, key, item)
        else:
            for key, item in kwargs.items():
                if key in var:
                    setattr(self, key, item)

    def to_dictionary(self):
        '''dicitonary representation of the class'''
        dic = {}
        keys = ['id', 'x', 'size', 'y']
        for k in keys:
            dic[k] = getattr(self, k)
        return dic
