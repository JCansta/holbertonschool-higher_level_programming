#!/usr/bin/python3
def weight_average(my_list=[]):
    mult = 0
    div = 0
    if not my_list:
        return 0
    else:
        for i in my_list:
            mult += i[0] * i[1]
            div += i[1]
    return mult / div
