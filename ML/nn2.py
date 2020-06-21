import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return (x > 0).astype(np.int)

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([1.0, 0.5])
W1 = np.array([[0.1, 0.3, 0.5],
               [0.2, 0.4, 0.6]])

B1 = np.array([0.1, 0.2, 0.3])
A1 = np.dot(X, W1) + B1

print(X)
print(A1)

Z1 = sigmoid(A1)
print(Z1)


# 2層
W2 = np.array([[0.1, 0.5],
               [0.2, 0.7],
               [0.3, 0.9]])
B2 = np.array([0.1, 0.2])
A2 = np.dot(Z1, W2) + B2
Z2 = sigmoid(A2)

print(A2)
print(Z2)


# 3層
def identity(x):
    return x

W3 = np.array([[0.1, 0.3],
               [0.2, 0.4]])

B3 = np.array([0.1, 0.2])
A3 = np.dot(Z2, W3) + B3

Y = identity(A3)

print(A3)
print(Y)

