import math

#BASE Class
class Shape:
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
    def area(self):
        return self.length * self.breadth

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
c = Circle(5)
print("Area of circle: ", c.area())

r = Rectangle(10, 20)
print("Area of rectangle: ", r.area())

t = Triangle(10, 20)
print("Area of triangle: ", t.area())


shape = [Circle(10), Rectangle(25,40), Triangle(50,40)]

for s in shape:
    print(f"The area of the {type(s).__name__} is : {s.area()}")
    