import numpy as np

def save_ndarray(X, filename="test.npy"):
    np.save(filename, arr = X)

X = np.arange(32, dtype=np.float32).reshape(4, -1)
filename = "test.npy"
print(save_ndarray(X,filename))