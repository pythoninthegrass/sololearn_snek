import re

word = input()
pattern = r'(\w+l\w+)'

if re.match(pattern, word):
    print("Match")
else:
    print("No match")
