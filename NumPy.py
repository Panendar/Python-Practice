import numpy as np

# a = np.array([1, 2, 3, 4, 5])
# b = np.array([10, 20, 30, 40, 50])
# print(a[0:5:2])
# print(b[::-1])
# print(b[[0,3,-1]]) #multi indexing
# print(type(a))
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# a = a.astype(np.float64)
# print(a.dtype)

# A = np.array([
#     [1,2,3],
#     [4,5,6]
# ])
# print(A.shape)
# print(A.size)

# B = np.array([[
#     [1,2,3],
#     [4,5,6],
# ],
# [
#     [7,8,9],
#     [10,11,12],
# ]])
# print(B.shape)

x = np.array([1,5,8])
# print(x+1)
# print(x*2)
# print(x-4)
# print(x/2)
# print(x**2)

y = np.array([4,7,3])
# print(x+y)
# print(x*y)
# print(x/y)

z = np.zeros([4,5])
# print(z)
w = np.ones([2,5])
# print(w)
c = np.full([3,4], 9)
# print(c)

r =np.random.randint(low=0, high=10, size=(2,3))
# print(r)

ages = np.random.randint(low = 18, high = 80, size = 10)
heights = np.random.randint(low = 150, high = 300, size = 10)
# print("Ages:", ages)
# print("Heights:", heights)
# print("Ages greater than 50:", ages>50)
# print("Heights of ages less than 50:", heights[ages<50])
# print("Ages: ", ages[ages<50])
# shuffled_idx = np.random.permutation(10)
# print("Shuffled indices:", shuffled_idx)
# print("Ages after shuffling:", ages[shuffled_idx])
# print("Heights after shuffling:", heights[shuffled_idx])
# sorted_idx = np.argsort(ages)
# print("Sorted indices based on ages:", sorted_idx)
# print("Ages after sorting:", ages[sorted_idx])
# print("Heights after sorting based on ages:", heights[sorted_idx])


# matrix properties and operations
m1 = np.array([1,4])
m2 = np.array([[2,3,4],[5,6,1]])
# print(m1.shape)
# print(m2.shape)

a = m2.transpose()
# print(a)
m3 = np.matmul(m1,m2)
# print(f"{m3}, shape {m3.shape}, Sum of all elements: {np.sum(m3)}")
# print(f" exponential of m1 :{np.exp(m1)}\n sin of m1 :{np.sin(m1)}\n cos of m1 :{np.cos(m1)}\n hyperbolic tangent of m1 :{np.tanh(m1)}\n")


# BROADCAST  
s = np.array([1,3,5,6])
q = np.array([2])
ab = s * q
# print(ab)
n1 = np.array([[1], [3], [5], [6]])
n2 = np.array([2,4,6])
n = n1 * n2
# print(n)


# Max, Min, Norms
arr = np.array([3,5,9,12,29,13.33,5,-5,-11])
# print(f"Max: {np.max(arr)}\nMin: {np.min(arr)}")
# print(f"{arr.max()},{arr.min()}")
# print(f"Norm : {np.linalg.norm(arr)}")  # The square root of the sum of squares of all elements in an array

#  NUMPY IN NEURAL NETWORKS
# For neural networks, the output of the neural network,z1 , is dependent on the inputs x1 and x2. The importance of each of the inputs is given by values called weights w11,w22.
# The inputs are given by x1 and x2, and the outputs are given by z1. Here, w11 is the weight of input 1 on output 1 (our only output in this case), and w22 is the weight of input 2 on output 1.
# In general, w_ij represents the weight of input j on output i.
# The output, z1, is given by : z1 = f(w11*x1 + w22*x2)
# where f is a specified nonlinear function, and it is usually the hyperbolic tangent function, tanh().

# Here, we will write a function neural_network, which will apply a neural network operation with 2 inputs and 1 output and a given weight matrix.
def neural_network(inputs, weights):
    inputs = np.array(inputs)
    weights = np.array(weights)
    z = np.dot(inputs.T, weights)
    z1 = np.tanh(z)
    return z1
# print(neural_network([0.5, 5], [4, 20]))
# print(neural_network([0.2, 0.3], [0.4, 0.1]))  # since the output is always 1, the weights are not significant in this case
# Normalize your inputs
# Ensure inputs are in a reasonable range like 0–1 or -1–1.
# Use sigmoid instead of tanh if you want values between 0 and 1:
# z1 = 1/(1+np.exp(-z))

# SCALAR FUNCTIONS
def scalar_function(x,y):
    if x>y:
        return x*y
    else:
        return x/y
# VECTOR FUNCTIONS
def vector_function(x,y):
    x = np.array(x)
    y = np.array(y)
    mag_x = np.linalg.norm(x)
    mag_y = np.linalg.norm(y)
    if mag_x>mag_y:
        return x*y
    else:
        return x/y
print(scalar_function(5,10))
print(vector_function([1,2,3],[4,5,6]))