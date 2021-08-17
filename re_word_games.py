import re
word = input()
# word = r'gl'

# TODO: match 'glass' (anchors?)
if re.match(word, 'glue'):
    print("Match")
else:
    print("No match")
