import math

class Shape:
    def area(self):
        raise NotImpletedError("Derived classes must override this method")
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length =length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        
    def print_area(shape):
        print(f" The area of the {shape.__class__.__name__.lower()} is: {shape.area()}")

