################################################
# Title     : Random Process
# Author    : balarcode
# Version   : 1.1
# Date      : 10th December 2024
# File Type : Python Script / Program
# File Test : Verified on Python 3.12.6
# Comments  : Algorithms, concepts and techniques from
#             random processes and probability
#             implemented in Python.
#
# All Rights Reserved.
################################################

# %%
import numpy as np
import matplotlib.pyplot as plt

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

# %%
################################################
# Mean Normalization of N-Dimensional Random Dataset
################################################
# X is a random data matrix of size = (N, D)
# where, N is the size of the dataset and
# D is the dimensionality of each data point
# NOTE: Uses vectorized implementation.
random = np.random.RandomState(0)
X = random.randn(100, 4) # (N, D)
#print(f"N-Dimensional Random Dataset: {X}")
N, D = X.shape

mu = np.sum(X, axis=0) / N
max = np.max(X, axis=0)
min = np.min(X, axis=0)
print(f"mu: {mu}, max: {max}, min = {min}")
Xnorm = (X - mu)/(max - min)
#print(f"N-Dimensional Mean Normalized Dataset: {Xnorm}")

# Plot two dimensions from original and mean normalized datasets
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(X[:, 0], X[:, 1], label='original data')
ax.scatter(Xnorm[:, 0], Xnorm[:, 1], label='mean normalized data')
plt.axis('equal')
plt.legend()
ax.set(xlabel='$x_0$', ylabel='$x_1$')
plt.show()

# %%
################################################
# Standardization of N-Dimensional Random Dataset
################################################
# X is a random data matrix of size = (N, D)
# where, N is the size of the dataset and
# D is the dimensionality of each data point
# NOTE: Uses vectorized implementation.
# NOTE: Standardization modifies the dataset to
# have zero mean and unit variance. It is also
# known as Z-score normalization.
random = np.random.RandomState(0)
X = 4 + (2 * random.randn(100, 4)) # (N, D)
#print(f"N-Dimensional Random Dataset: {X}")
N, D = X.shape

mu = np.sum(X, axis=0) / N
sigma = np.sqrt(np.sum((X - mu) ** 2, axis=0) / N)
print(f"mu: {mu}, sigma: {sigma}")
Xnorm = (X - mu)/sigma
#print(f"N-Dimensional Mean Normalized Dataset: {Xnorm}")

# Plot two dimensions from original and mean normalized datasets
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(X[:, 0], X[:, 1], label='original data')
ax.scatter(Xnorm[:, 0], Xnorm[:, 1], label='standardized data')
plt.axis('equal')
plt.legend()
ax.set(xlabel='$x_0$', ylabel='$x_1$')
plt.show()

# %%
