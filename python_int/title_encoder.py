with open("/mnt/c/Users/wahrh/Documents/code/sololearn_snek/python_core/books.txt", "r") as file:
    raw = file.readlines()
    raw_lst = [line.strip() for line in raw]
    new_lst = []
    final = []

    for i in raw_lst:
        if len(i) > 1 and '' not in i:
            new_lst.append(i[0])
        else:
            new_lst.append(i)

    get_spaces = []

    for i in new_lst:
        if ' ' in i:
            get_spaces.append(i.split(' '))
    
    eat_the_book = ""

    for i in get_spaces[0:1]:
        for a in i:
            eat_the_book += a[0]
    
    final.append(eat_the_book)

    eat_another_book = ""

    for i in get_spaces[1:]:
        for a in i:
            eat_another_book += a[0]
    little_titles = []

    for item in raw_lst:
        if " " not in item:
            little_titles.append(item[0])


    print(str(little_titles[0])) 
    print(str(little_titles[1]))
    print(eat_the_book)
    print(eat_another_book)


    # TODO: get len of each word, strip after 0 index, concatenate strings (e.g., GoT)
    # for i in raw_lst:
    #     print(i)

    #     # print(i[0][:1])
