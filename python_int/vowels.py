word = input()

vowels = ['a', 'e', 'i', 'o', 'u']

non_vowels = [i for i in word if i not in vowels]
# for i in word:
#     if i in vowels:
#         print(i)

print(non_vowels)
