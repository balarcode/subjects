################################################
# Title     : Linear Algebra
# Author    : balarcode
# Version   : 1.1
# Date      : 30th October 2024
# File Type : Python Script / Program
# File Test : Verified on Python 3.12.6
# Comments  : Algorithms, concepts and techniques from linear algebra implemented in Python.
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

################################################
# Change of Basis
################################################
b0_x = np.array([1, 0])
b0_y = np.array([0, 1])
r0 = 2 * b0_x + 2 * b0_y # Vector in a space spanned by basis vectors b0_x and b0_y
print("\nVector in old basis vector space: ")
print(r0)

# New basis
b1_x = np.array([3, 1])
b1_y = np.array([-1, 3])
r1_00 = (r0 @ b1_x) / (np.linalg.norm(b1_x) * np.linalg.norm(b1_x)) * b1_x
r1_01 = (r0 @ b1_y) / (np.linalg.norm(b1_y) * np.linalg.norm(b1_y)) * b1_y
r1 = r1_00 + r1_01
print("\nVector in new basis vector space: ")
print(r1)
