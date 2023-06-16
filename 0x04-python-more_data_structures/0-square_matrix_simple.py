#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
    matrix: A 2 dimensional array.

    Returns:
    A new matrix:
        Same size as matrix
        Each value should be the square of the value of the input
        Initial matrix should not be modified

    Raises:
    ValueError: If matrix is not a 2 dimensional array.
    """

    if not isinstance(matrix, list):
        raise ValueError("matrix must be a list")

    for row in matrix:
        if not isinstance(row, list):
            raise ValueError("matrix must be a list of lists")

    new_matrix = [[value ** 2 for value in row] for row in matrix]

    return new_matrix
