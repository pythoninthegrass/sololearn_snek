try:
    name = input()  # 'demo'
    if len(name) <= 3:
        raise ValueError
    else:
        print("Account Created")
except:
    print("Invalid Name")
