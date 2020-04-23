import numpy as np


def change_shape_of_ndarray(X, n_row):
    if n_row == 1:
        return np.array(X).flatten()
    return np.array(X).reshape(n_row, -1)

X = np.ones((32,32), dtype=np.int)
print(change_shape_of_ndarray(X, 1))
print(change_shape_of_ndarray(X, 512))