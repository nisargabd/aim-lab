import numpy as np

def nonlin(x, deriv=False):
    if (deriv==True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))

xrange = 10000

X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])

y = np.array([[0, 0, 1, 1]]).T

np.random.seed(1)

syn0 = 2 * np.random.random((3, 1)) - 1

for iter in range(xrange):
    l0 = X
    l1 = nonlin(np.dot(l0, syn0))
    l1_error = y - l1
    l1_delta = l1_error * nonlin(l1, True)
    syn0 += np.dot(l0.T, l1_delta)

print("Actual Output:\n" + str(y))
print("Output After Training:")
print(l1)


# OUTPUT:
# Actual Output:
# [[0]
# [0]
# [1]
# [1]]
# Output After Training:
# [[0.00966449]
# [0.00786506]
# [0.99358898]
# [0.99211957]]