import numpy as np

def n_size_ndarray_creation(n, dtype=np.int):
    X = np.empty((n,n), dtype=np.int)
    for i in range(n):
        X[i,i]=(i+1)**2 - 1
    return X


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        return np.zero(shape, dtype=np.int)
    elif type == 1:
        return np.ones(shape, dtype=np.int)
    else:
        return np.empty(shape, dtype=np.int)


def change_shape_of_ndarray(X, n_row):
    if n_row == 1:
        return np.array(X).flatten()
    return np.array(X).reshape(n_row, -1)

def concat_ndarray(X_1, X_2, chook):
    if len(np.array(X_1).shape) == 1:
        X_1 = np.array(X_1).reshape(1, -1)
    if len(np.array(X_2).shape) == 1:
        X_2 = np.array(X_2).reshape(1, -1)
    try:
        return np.concatenate((X_1,X_2), axis= chook)
    except:
        return False


def normalize_ndarray(X, axis=99, dtype=np.float32):
    if axis == 99:
        return (X-X.mean())/X.std()
    elif axis == 0:
        return (X-X.mean(axis=0))/X.std(axis=0)
    elif axis == 1:
        return (X-X.mean(axis=1).reshape(-1,1))/X.std(axis).reshape(-1,1)
    else:
        return None


def save_ndarray(X, filename="test.npy"):
    np.save(filename, arr = X)


def boolean_index(X, condition):
    return X[eval(str("X")+condition)]


def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X - target_value))]



def get_n_largest_values(X, n):
    a = np.array(X).flatten().tolist()
    a = sorted(a)
    b = []
    for i in range(n):
        b.append(a.pop())
        i+=1
    return np.array(b)
