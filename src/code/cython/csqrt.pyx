# cython: language_level=3
from math import sqrt
import numpy as np

def csqrt(double[:,:] X):
    cdef int r = X.shape[0]
    cdef int c = X.shape[1]
    cdef double[:, :] Y = np.zeros((r, c))
    cdef int i, j

    for i in range(r):
        for j in range(c):
            Y[i, j] = sqrt(X[i, j])
    return Y  