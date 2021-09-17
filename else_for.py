ages = []
i = 0
while i < 3:
    age = int(input())
    if age >= 16:
        ages.append(age)
        i += 1
    else:
        print("Too young!")
        break

else:
   print("Get ready!")
