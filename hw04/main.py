import math as m

class Shapes(object):
    def area(self):
        pass    
class Ellipse(Shapes):
    def __init__(self, a, b):
        self.a = a
        self.b = b         
    def area(self):
        return self.a * self.b * m.pi
class Rectangle(Shapes):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Ellipse):
    def __init__(self, a):
        super().__init__(a, a)
class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)
        
def compute_area(shapes):
    return sum([x.area() for x in shapes])

shapes = [Ellipse(10, 20), Square(15), Circle(5),
          Rectangle(20, 15), Circle(5), Square(15),
          Ellipse(10, 20)]
total_area = compute_area(shapes)
print(total_area)
