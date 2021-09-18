n = int(input())
#n = 15	# 1, Solo, Learn, 7, Solo, 11, 13

#is_odd_if_zero = x & 1
#is_odd = (x & 1) == 1

for x in range(1, n):
    if (x & 1) == 0:
        continue
    elif x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)
