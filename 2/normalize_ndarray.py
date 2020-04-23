import numpy as np

def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 99:
        return (X-X.mean())/X.std()
    elif axis == 0:
        return (X-X.mean(axis=0))/X.std(axis=0)
    elif axis == 1:
        return (X-X.mean(axis=1).reshape(-1,1))/X.std(axis).reshape(-1,1)
    else:
        return None

X = np.arange(12, dtype = np.float32).reshape(6,2)
print(normalize_ndarray(X))
print(normalize_ndarray(X,1))
print(normalize_ndarray(X,0))