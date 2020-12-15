#!/usr/bin/python3
def element_at(my_list, idx):
    if idx >= len(my_list) or idx < 0 or not my_list:
        return None
    return my_list[idx]
