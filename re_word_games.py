import re

word = input()
pattern = r'(gl\w+)'

if re.match(pattern, word):
    print("Match")
else:
    print("No match")
