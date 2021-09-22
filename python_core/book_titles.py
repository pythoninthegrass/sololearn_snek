with open("./books.txt", "r") as file:
    for line in file:
        print(line[:1] + str(len(line.strip())))
