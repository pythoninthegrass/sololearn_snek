import os

fn = fn = os.path.join("../python_core/books.txt")  # "/usercode/files/books.txt"

N = int(input())

with open(fn, "r") as file:
    # for line in file:
    #     print(line[:1] + str(len(line.strip())))
    print(file.read()[:N])
