with open("python_core/books.txt", "r") as file:
    raw = file.readlines()
    raw_lst = [line.strip() for line in raw]
    print(raw_lst)

    # TODO: get len of each word, strip after 0 index, concatenate strings (e.g., GoT)
    for i in raw_lst:
        print(i)
        # print(i[0][:1])
