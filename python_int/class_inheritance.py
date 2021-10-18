class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width * self.height)

class Rectangle(Shape):
    def perimeter(self):
        print(2 * (w + h))

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()
