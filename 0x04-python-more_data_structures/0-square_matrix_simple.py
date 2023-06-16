#!/usr/bin/pyhton3

def square_matrix_simple(matrix=[]):
    if not isinstance(matrix, list):
        raise ValueError("matrix must be a list")

    for row in matrix:
        if not isinstance(row, list):
            raise ValueError("matrix must be a list of lists")

    new_matrix = []
    for row in matrix:
        new_row = []
        for value in row:
            new_row.append(value ** 2)
        new_matrix.append(new_row)

    return new_matrix
