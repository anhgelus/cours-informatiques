import numpy as np

a = np.array([[7, 0], [-1, 5], [-1, 2]])
b = np.array([[-1, 4], [-4, 0]])
c = np.array([[-7], [3]])
d = np.array([[8, 2]])

print(np.dot(a, b))
print(np.dot(a, c))
print(np.dot(c, a))
print(np.dot(d, c))
print(np.dot(d, b, c))
print(np.dot(a.transpose(), a))
print(np.dot(a, a.transpose()))
