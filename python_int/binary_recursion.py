def convert(num):
   return (num % 2 + 10 * convert(num // 2)) if num > 1 else num

num = int(input())

print(convert(num))
