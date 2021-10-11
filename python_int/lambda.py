price = int(input())
perc = int(input())

res = (lambda x,y: x * float(y / 100)) (price, perc)

print(res)
