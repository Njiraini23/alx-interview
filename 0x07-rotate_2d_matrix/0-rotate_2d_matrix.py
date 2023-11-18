#!/usr/bin/python3
"""A function that rotates a 2D matrix"""


def rotate_2d_matrix(matrix):
    '''
    rotates a 2d matrix in 90 degrees clockwise
    parameters:
        matrix [list of lists of integers]:
            matrix to rotatehas a 2 dimensions and cannit
            be empty
    '''
    # save the original matrix
    N = len(matrix)

    # build the rotated matrix
    matrix_copy = []
    copy_row = 0
    for column in range(N):
        for row in range((N - 1), -1, -1):
            if column == 0:
                matrix_copy.append([])
            matrix_copy[copy_row].append(matrix[row][column])
        copy_row += 1

    # copy the contents of a matrix
    for row in range(N):
        for column in range(N):
            matrix[row][column] = matrix_copy[row][column]
