names = [ "John", "Paul", "George", "Ringo" ]

with open("names.txt", "w") as f:
    for name in names:
        f.write(name + "\n")

with open("names.txt", "r") as f:
    for line in f:
        print(line.strip())
