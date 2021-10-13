ages = [3, 1, 9, 0.4, 7, 12, 2, 1.7, 5.7, 42, 6.7, 14.5, 21]

num = int(float(input()))

elems = list(filter(lambda x: x > num, ages))

print(len(elems))
