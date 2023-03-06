#class to calculate area of a circle and radius
from cmath import pi


class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi*self.radius**2
    
    def perimeter(self):
        return pi*2*self.radius
    
c = Circle(6)
print(c.area())
print(c.perimeter())