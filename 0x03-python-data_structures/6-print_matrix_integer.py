#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    clen = len(matrix[0])-1
    for fila in matrix:
        for j in fila:
            print("{:d}".format(j), end="" if j == fila[clen] else " ")
        print()
