import os

n = int(input())

fn = os.path.join("numbers.txt")
with open(fn, "w+") as file:
    for i in range(1, n + 1):
        if i == n:
            file.write(str(i))
        else:
            file.write(str(i) + "\n")

with open(fn, "r") as file:
    print(file.read())
