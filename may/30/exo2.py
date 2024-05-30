import numpy as np

q1 = np.array([i for i in range(51) if i % 2 == 0])
q2 = np.cos(q1*q1)
q3 = np.min(q2)
q4 = np.random.random([3, 3, 3])
q5 = q4[[0], [0], [0]]

print(q1)
print(q2)
print(q3)
print(q4)
print(q5)
