import numpy as np

def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        return np.zero(shape, dtype=np.int)
    elif type == 1:
        return np.ones(shape, dtype=np.int)
    else:
        return np.empty(shape, dtype=np.int)


print(zero_or_one_or_empty_ndarray(shape=(2,2), type=1))
print(zero_or_one_or_empty_ndarray(shape=(3,3), type=99))