import numpy as np


def LU(a):
    n = len(a)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1 : n] = a[i, k + 1 : n] - lam * a[k, k + 1 : n]
                a[i, k] = lam
    return a


def LUsolve(a, b):
    n = len(a)
    for k in range(1, n):
        b[k] = b[k] - np.dot(a[k, 0:k], b[0:k])
    b[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1 : n], b[k + 1 : n])) / a[k, k]
    return b


a = np.array(
    [
        [2.0, 0.0, -1.0, 0.0],
        [0.0, 1.0, 2.0, 0.0],
        [-1.0, 2.0, 0.0, 1.0],
        [0.0, 0.0, 1.0, -2.0],
    ]
)
b = np.array([[1.0, 0.0, 0.0, 0.0], [0.0, 0.0, 1.0, 0.0]])


a = LU(a)
# print(a)


det = np.prod(np.diagonal(a))
# print("\nDeterminant =", det)

for i in range(len(b)):
    x = LUsolve(a, b[i])
    print("x", i + 1, "=", x)
