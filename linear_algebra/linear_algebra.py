################################################
# Title     : Linear Algebra
# Author    : balarcode
# Version   : 1.3
# Date      : 14th November 2024
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

################################################
# Cauchy-Schwarz Inequality
################################################
s = np.array([1, 2, 3, 4, 5])
r = np.array([5, 4, 3, 2, 1])
# NOTE: || s || = <s, s> ^ (1/2) is the 2-norm of vector, s which is also an induced norm.
print("\nCauchy-Schwarz Inequality: <s, r> <= || s || || r || i.e. {} <= {} * {}".format((s @ r), np.linalg.norm(s), np.linalg.norm(r)))

################################################
# Weighted Inner Product
################################################
x1 = np.array([1, 1])
x2 = np.array([2, 1])
print("\nTwo vectors, x1 and x2 are made orthogonal with a weighted inner product.")
print("Inner product of vectors, x1 and x2: {}".format(x1 @ x2))
W = np.array([[2, -2],
              [-2, 2]])
print("Weight Matrix, W: ")
print(W)
print("Weighted inner product of vectors, x1 and x2: {}".format((x1 @ W @ x2)))
print("W is a positive definite matrix when used with vector, x2 i.e. weighted norm of x2 is greater than 0: {}".format(x2 @ W @ x2))

################################################
# Angle between Vectors
################################################
# Uses a non-standard inner product where-in the
# matrix A defines the inner product
def find_angle(A, x, y):
    """Compute the angle"""
    inner_prod = x.T @ A @ y
    norm_x = np.sqrt(x.T @ A @ x)
    norm_y = np.sqrt(y.T @ A @ y)
    cos_w = inner_prod/(norm_x*norm_y)
    angle = np.arccos(cos_w)
    return np.round(angle, 2) # Round up to 2 decimal places

A = np.array([[1, 0, 0],[0, 2, -1],[0, -1, 3]])
x = np.array([1, 1, 1])
y = np.array([2, -1, 0])
angle = find_angle(A, x, y)
print("\nAngle between two vectors, x1 and x2 using a non-standard inner product: {} radians".format(angle))
