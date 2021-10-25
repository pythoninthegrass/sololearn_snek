menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

item = input()

try:
    if item.isnumeric():
        item = int(item)
        for i in range(len(menu)):
            if item == i:
                print(f"{menu[i]}\nThanks for your order")
                break
            elif item > len(menu):
                raise IndexError
    elif item.isalpha():
        raise TypeError
except (IndexError, TypeError):
    print('Item not found')
