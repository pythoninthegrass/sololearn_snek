class Shape:
    """
    We are improving our drawing application. Our application needs to support adding and comparing two Shape objects.
    Add the corresponding methods to enable addition + and comparison using the greater than > operator for the Shape class.

    The addition should return a new object with the sum of the widths and heights of the operands, while the comparison should return the result of comparing the areas of the objects.

    The given code creates two Shape objects from user input, outputs the area() of their addition and compares them.
    """
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        return self.__class__(self.width + other.width, self.height + other.height) # i.e., `return Shape(self.width ...)`

    def __gt__(self, other):
        return self.area() > other.area()


w1 = int(input())       # 2
h1 = int(input())       # 3
w2 = int(input())       # 4
h2 = int(input())       # 2

s1 = Shape(w1, h1)
s2 = Shape(w2, h2)
result = s1 + s2

print(result.area())    # 30
print(s1 > s2)          # False
