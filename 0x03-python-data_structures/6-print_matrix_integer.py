#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """this function read values in interger an print it"""
    if matrix:
        for s in matrix:
            i = 0
            for v in s:
                print("{:d}".format(v), end=" " if i < len(s) - 1 else "")
                i = i + 1
            print("")
