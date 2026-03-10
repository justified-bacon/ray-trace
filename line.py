import numpy as np
import vectormath

x = np.array([1,1,1])

print(vectormath.magnitude(x))

l = vectormath.line()

l.point = np.array([1,0,0])
l.vector = np.array([0,0,1])

p = np.array()

# g = np.array([[1,1,1,1], [0,0,0,0]])
# print(g.shape)

print(vectormath.crossProduct(np.array([0,1,0]), np.array([1,0,0])))



