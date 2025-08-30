import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
print(a[0:5:2])
print(b[::-1])
print(b[[0,3,-1]]) #multi indexing
print(type(a))
print(a.dtype)
print(a.ndim)
print(a.size)
a = a.astype(np.float64)
print(a.dtype)

A = np.array([
    [1,2,3],
    [4,5,6]
])
print(A.shape)
print(A.size)

B = np.array([[
    [1,2,3],
    [4,5,6],
],
[
    [7,8,9],
    [10,11,12],
]])
print(B.shape)