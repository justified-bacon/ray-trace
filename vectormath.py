import numpy as np

class line():
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector

        if not ((type(self.point) == np.ndarray) and (type(self.vector) == np.ndarray)):
            raise TypeError('point and vector must be numpy arrays')
        
        if self.point.shape != (3,) or self.vector.shape != (3,):
            raise ValueError("point and vector arrays have to be of shape (3,)")
                    
        if np.array_equal( self.vector,  np.array([0,0,0])):
            raise ValueError("error: direction vector can't be null")

def magnitude(self):
    magnitude = (self[0]**2 + self[1]**2 + self[2]**2)**(1/2)
    return magnitude

def crossProduct(a, b):
    return np.array([a[1]*b[2] - a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])

def distLinePoint(line, point):
    dist = magnitude(crossProduct((point - line.point), line.vector)) / magnitude(line.vector)
    return dist
