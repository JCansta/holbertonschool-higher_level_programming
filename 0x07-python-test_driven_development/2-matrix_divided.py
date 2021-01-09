#!/usr/bin/python3
def matrix_divided(matrix, div):
    try:
        if div is 0:
            raise ZeroDivisionError('division by zero')

        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')

        leng = len(matrix[0])
        if not all(len(y) == leng for y in matrix):
            raise TypeError('Each row of the matrix must have the same size')

        for lst in matrix:
            if not all(isinstance(x, (int, float)) for x in lst):
                raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
    except TypeError as e:
        print("TypeError: {}".format(e))
        return None
    except ZeroDivisionError as e:
        print("ZeroDivisionError: {}".format(e))
        return None

    newm = []
    for i in matrix:
        newm.append(list(round(x / div, 2) for x in i))
    return newm
