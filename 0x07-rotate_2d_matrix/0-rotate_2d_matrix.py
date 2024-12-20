#!/usr/bin/python3
"""
This module contains a function to rotate a 2D matrix 90 degrees clockwise.
The rotation is performed in-place to optimize space complexity.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise in-place.
    Args:
        matrix (list[list]): The 2D square matrix to rotate
    Returns:
        None. The matrix is edited in-place.
    """
    n = len(matrix)
    
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()
