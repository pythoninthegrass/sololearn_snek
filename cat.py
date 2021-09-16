def concatenate(*args):
    res = ""
    for arg in args:
        res += " " + arg
    return res

print(concatenate("I", "love", "Python", "!"))
