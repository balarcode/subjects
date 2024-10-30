################################################
# Title     : Linear Algebra
# Author    : balarcode
# Version   : 1.0
# Date      : 29th October 2024
# File Type : Python Script / Program
# File Test : Verified on Python 3.12.6
# Comments  : Concepts and techniques from linear algebra implemented in Python.
#
# All Rights Reserved.
################################################

import numpy as np
#import matplotlib.pyplot as plt

################################################
# Row and Column Vectors
################################################
s_col = [[1],
         [2],
         [3],
         [4],
         [5]]

s_row = [6, 7, 8, 9, 0]

s_col_vector = np.array(s_col) # Column vector
s_row_vector = np.array(s_row) # Row vector

print("\nColumn vector in numpy -- np.array(list): ")
print(s_col_vector)

print("\nRow vector in numpy -- np.array(list): ")
print(s_row_vector)

print("\nTransposing a vector in numpy -- np.array([vector]).T: ")
print(np.array([s_row_vector]).T)

################################################
# Dot Product of Vectors
################################################
s = [1, 2, 3, 4, 5]
r = [1, 2, 3, 4, 5]
s_vector = np.array(s) # Row vector
r_vector = np.array(r) # Row vector

# Note that the result will be a scalar
print("\nDot product of vectors, s and r using Python operator -- s @ r: ")
print(s_vector @ r_vector)

print("\nDot product of vectors, s and r in numpy -- np.dot(s, r): ")
print(np.dot(s_vector, r_vector))

################################################
# Element-wise Multiplication of Vectors
################################################
s = [1, 2, 3, 4, 5]
r = [1, 2, 3, 4, 5]
s_vector = np.array(s) # Row vector
r_vector = np.array(r) # Row vector

# Note that the result will still be a vector
print("\nElement-wise multiplication of vectors, s and r -- s * r: ")
print(s_vector * r_vector)

################################################
# Scalar Projection
################################################
x = np.array([2, 2])
y = np.array([4, 0])
theta = np.arccos((x @ y) / (np.linalg.norm(x) * np.linalg.norm(y)))
theta_degrees = theta * (180 / np.pi)
print("\nAngle between the two vectors in degrees: ")
print(theta_degrees)

scalar_proj_x_over_y = (x @ y) / np.linalg.norm(y)
print("\nScalar projection of vector x over vector y: ")
print(scalar_proj_x_over_y)

################################################
# Vector Projection
################################################
vector_proj_x_over_y = (x @ y) / (np.linalg.norm(y) * np.linalg.norm(y)) * y
print("\nVector projection of vector x over vector y: ")
print(vector_proj_x_over_y)
