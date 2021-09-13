import re

# valid phone number has exactly 8 digits and starts with 1, 8 or 9. 
# e.g., 81234567, 57345672

#num_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?(.)?|(.)+){3}')
#print(num_regex.search("My numbers are 415-555-1234, 555-4242, and 212-555-0000"))

# num = input()
num = '57345672'

# TODO: QA edge case test that fails
num_regex = re.compile(r'^(1|8|9)(\d){0,8}')
# num_regex.search("57345672")
print(num_regex.match(num))
if num_regex.match(num):
	print('Valid')
else:
	print('Invalid')
