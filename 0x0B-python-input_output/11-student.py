#!/usr/bin/python3
"""
student class
"""


class Student():
    '''new class student'''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None or not isinstance(attrs, list):
            return self.__dict__
        return ({key: value for key, value in self.__dict__.items()
                if key in attrs})

    def reload_from_json(self, json):
        for key, value in json.items():
            obj = "self."+key+" = value"
            exec(obj)
