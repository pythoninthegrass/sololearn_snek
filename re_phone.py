import re

# valid phone number has exactly 8 digits and starts with 1, 8 or 9.
# e.g., 81234567, 57345672, 98765432

num = input()

num_regex = re.compile(r'^[1|8|9]\d{1,8}$')

if num_regex.match(num):
	print('Valid')
else:
	print('Invalid')
