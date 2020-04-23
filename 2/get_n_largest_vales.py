import numpy as np


def get_n_largest_values(X, n):
    a = np.array(X).flatten().tolist()
    a = sorted(a)
    b = []
    for i in range(n):
        b.append(a.pop())
        i+=1
    return np.array(b)

X = np.random.uniform(0, 1, 100)
print(get_n_largest_values(X, 3))
print(get_n_largest_values(X, 5))