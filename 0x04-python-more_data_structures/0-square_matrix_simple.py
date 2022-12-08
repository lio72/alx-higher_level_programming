#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ return matrix with squart value and matrix"""
    new_matrix = [[n**2 for n in m ] for m in matrix]
    return new_matrix
