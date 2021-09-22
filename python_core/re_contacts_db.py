import re

phone = input()
# phone = '0014860098'
pattern = r'^0+'
replacement = r'+'

new_string = re.sub(pattern, replacement, phone)
print(new_string)
