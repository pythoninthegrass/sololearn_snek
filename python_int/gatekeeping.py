n = [2, 4, 6, 8]

res = 1

# 1: 4, 2: 6
for x in n[1:3]:
  res *= x

# 4*1; 6*4
print(res)
