import numpy as np

def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X - target_value))]

X = np.random.uniform(0, 1, 100)
target_value = 0.3
print(find_nearest_value(X, target_value))