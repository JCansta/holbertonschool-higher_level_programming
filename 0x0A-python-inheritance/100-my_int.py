#!/usr/bin/python3
"""
100-my_int.py
"""


class MyInt(int):
    '''class int'''

    def __eq__(self, other):
        '''init for eq'''
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        '''init for ne'''
        if int.__eq__(self, other):
            return True
        else:
            return False
