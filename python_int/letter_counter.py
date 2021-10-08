# text = input()
text = 'hello'
dict = {}

for letter in text:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1

print(dict)
