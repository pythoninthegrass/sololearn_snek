def decor(func):
    def wrapper(*args, **kwargs):
        print("***")
        func(*args, **kwargs)
        print("***\nEND OF PAGE")
    return wrapper

@decor
def invoice(num):
    print("INVOICE #" +num)

invoice(input())
