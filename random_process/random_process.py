################################################
# Title     : Random Process
# Author    : balarcode
# Version   : 1.2
# Date      : 11th December 2024
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
from scipy.stats import norm

################################################
# Function Definitions
################################################
def norm_plot(ax, data):
    scale = (np.max(data) - np.min(data)) * 0.2
    x = np.linspace(np.min(data)-scale, np.max(data)+scale, 50)
    _,bins, _ = ax.hist(data, x, color="xkcd:azure")

    mu = np.mean(data)
    sigma = np.std(data)
    dist = norm.pdf(bins, loc=mu, scale=sigma)

    axr = ax.twinx()
    axr.plot(bins, dist, color="orange", lw=2)
    axr.set_ylim(bottom=0)
    axr.axis('off')

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
ax.scatter(Xnorm[:, 0], Xnorm[:, 1], label='mean normalized data', color="orange")
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
#print(f"N-Dimensional Standardized Dataset: {Xnorm}")

# Plot first two features from original and standardized datasets as a scatter plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.scatter(X[:, 0], X[:, 1], label='original data')
ax.scatter(Xnorm[:, 0], Xnorm[:, 1], label='standardized data', color="orange")
plt.axis('equal')
plt.legend()
ax.set(xlabel='$x_0$', ylabel='$x_1$')
plt.show()

# Plot all features from original and standardized datasets (i.e. per dimension)
fig, ax = plt.subplots(1, 4, figsize=(12, 3))
for i in range(len(ax)):
    ax[i].scatter(range(len(X[:, i])), X[:, i], label='original data')
    ax[i].set_xlabel('$x$'+str(i))
for i in range(len(ax)):
    ax[i].scatter(range(len(Xnorm[:, i])), Xnorm[:, i], label='standardized data', color="orange")
    ax[i].set_xlabel('$x$'+str(i))
fig.suptitle("Features of original & standardized data (per dimension)")
ax[0].set_ylabel("output")
plt.legend()
plt.show()

# Plot distribution of features from original and standardized datasets (i.e. per dimension)
fig, ax = plt.subplots(1, 4, figsize=(12, 3))
for i in range(len(ax)):
    norm_plot(ax[i], X[:,i], )
    ax[i].set_xlabel('$x$'+str(i))
ax[0].set_ylabel("count")
fig.suptitle("Distribution of features of original data (per dimension)")
plt.show()
fig, ax = plt.subplots(1, 4, figsize=(12, 3))
for i in range(len(ax)):
    norm_plot(ax[i], Xnorm[:,i], )
    ax[i].set_xlabel('$x$'+str(i))
ax[0].set_ylabel("count")
fig.suptitle("Distribution of features of standardized data (per dimension)")
plt.show()

# %%
