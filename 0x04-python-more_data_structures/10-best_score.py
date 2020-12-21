#!/usr/bin/python3
def best_score(a_dictionary):
    key_max = max(a_dictionary, key=a_dictionary.get)\
            if a_dictionary is not None else None
    return key_max
