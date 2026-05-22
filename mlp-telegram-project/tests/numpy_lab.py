import numpy as np


# vector
x = np.array([1, 2, 3])

print("Vector:")
print(x)

# matrix
W = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

print("\nMatrix:")
print(W)

# dot product
result = np.dot(x, W)

print("\nDot product:")
print(result)

# transpose
print("\nTranspose:")
print(W.T)

# random weights
weights = np.random.randn(
    4,
    3
)

print("\nRandom weights:")
print(weights)