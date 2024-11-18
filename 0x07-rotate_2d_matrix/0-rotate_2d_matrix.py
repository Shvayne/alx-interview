#!/usr/bin/python3
"""This code transposes a matrix by 90 degrees"""

def rotate_2d_matrix(matrix):
  """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.
    The rotation is achieved through two steps:
    1. Transpose the matrix (swap rows and columns)
    2. Reverse each row
  """
  n = len(matrix)

  #Transpose the matix
  for i in range(n):
    for j in range(i, n):
      matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

  for i in range(n):
    matrix[i].reverse()
