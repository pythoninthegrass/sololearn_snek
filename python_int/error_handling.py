def withdraw(amount):
   print(str(amount) + " withdrawn!")


def some_function():
    try:
        withdraw(int(input()))
        return True
    except ValueError:
        print("Please enter a number")
        withdraw(int(input()))
        return False


res = False
while (res == False):
    try:
        some_function()
        res = True
    except:
        # continue    # solution wants a break
        break
