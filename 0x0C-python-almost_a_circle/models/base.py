#!/usr/bin/python3
"""
Base of the model
"""


import json


class Base():
    __nb_objects = 0

    def __init__(self, id=None):
        '''init of the class'''
        self.id = id
        if self.id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''return the string representation of list dictioanries'''
        if not list_dictionaries:
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save the json string representation in a file'''
        new = []
        name = "{}.json".format(cls.__name__)
        if list_objs:
            for i in list_objs:
                new.append(i.to_dictionary())
        new = cls.to_json_string(new)
        with open(name, mode="w", encoding="utf-8") as myFile:
            myFile.write(new)

    @staticmethod
    def from_json_string(json_string):
        '''from json string to list'''
        if not json_string:
            return []
        else:
            return json.loads(json_string)
