#!/usr/bin/python3
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y )
        else:
            return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)
            
    def __bool__(self):
        return bool(self.x or self.y)


v1 = Vector(2, 1)
v2 = Vector(0,1)
v3 = Vector(3, 4)
print(v1 * 2)
print(v1 * v3)
print(2 * v1)