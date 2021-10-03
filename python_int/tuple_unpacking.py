def calc(x):
    perim = x * 4
    area = x ** 2
    return perim, area

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))
