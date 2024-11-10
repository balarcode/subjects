################################################
# Title     : Random Process
# Author    : balarcode
# Version   : 1.0
# Date      : 10th November 2024
# File Type : Python Script / Program
# File Test : Verified on Python 3.12.6
# Comments  : Algorithms, concepts and techniques from
#             random processes and probability
#             implemented in Python.
#
# All Rights Reserved.
################################################

import numpy as np

################################################
# Mean of N-Dimensional Random Dataset
################################################
# X is a random data matrix of size = (N, D)
# where, N is the size of the dataset and
# D is the dimensionality of each data point
# NOTE: Uses vectorized implementation.
random = np.random.RandomState(0)
X = random.randn(100, 20) # (N, D)
print(f"N-Dimensional Random Dataset: {X}")
N, D = X.shape
mean = np.zeros((D,))
mean = np.sum(X, axis=0) / N
mean = np.array(mean, dtype=float)
print(f"Mean of the N-Dimensional Random Dataset: {mean}")

################################################
# Covariance of N-Dimensional Random Dataset
################################################
# X is a random data matrix of size = (N, D)
# where, N is the size of the dataset and
# D is the dimensionality of each data point
# NOTE: Uses vectorized implementation.
random = np.random.RandomState(0)
X = random.randn(100, 4) # (N, D)
print(f"N-Dimensional Random Dataset: {X}")
N, D = X.shape
covariance_matrix = np.zeros((D, D))
covariance_matrix = ((X - (np.sum(X, axis=0, keepdims=True) / N)).T @ (X - (np.sum(X, axis=0, keepdims=True) / N))) / N
covariance_matrix = np.array(covariance_matrix, dtype=float)
print("\nCovariance of the N-Dimensional Random Dataset: ")
print(covariance_matrix)
