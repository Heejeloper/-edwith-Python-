import numpy as np

def n_size_ndarray_creation(n, dtype=np.int):
    X = np.empty((n,n), dtype=np.int)
    for i in range(n):
        X[i,i]=(i+1)**2 - 1
    return np.array(X)

print(n_size_ndarray_creation(3, dtype=np.int))
