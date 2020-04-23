import numpy as np
def boolean_index(X, condition):
    return X[eval(str("X")+condition)]


X = np.arange(32, dtype=np.float32).reshape(4, -1)
print(boolean_index(X, "== 3"))
X = np.arange(32, dtype=np.float32)
print(boolean_index(X, "> 6"))

