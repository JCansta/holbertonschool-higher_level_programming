#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    suma = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
             'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        check = 0
        num = roman.get(roman_string[i])
        if num is None:
            return 0
        if i < len(roman_string) - 1:
            check = roman.get(roman_string[i + 1])
        suma += num if num >= check else -num
    return suma
