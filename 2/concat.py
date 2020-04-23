import numpy as np

def concat_ndarray(X_1, X_2, chook):
    if len(np.array(X_1).shape) == 1:
        X_1 = np.array(X_1).reshape(1, -1)
    if len(np.array(X_2).shape) == 1:
        X_2 = np.array(X_2).reshape(1, -1)
    try:
        return np.concatenate((X_1,X_2), axis= chook)
    except:
        return False

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
print(concat_ndarray(a, b, 0))
# array([[1, 2],
#        [3, 4],
#        [5, 6]])
print(concat_ndarray(a, b, 1))
# False
a = np.array([1, 2])
b = np.array([5, 6, 7])
print(concat_ndarray(a, b, 1))
# array([[1, 2, 5, 6, 7]])
print(concat_ndarray(a, b, 0))
#False