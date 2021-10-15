def my_min(*args):
    for i in args:
        if i == min(args):
            return i

print(my_min(8, 13, 4, 42, 120, 7))
