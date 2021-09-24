data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}
# print(data['United Kingdom'])

name = input()

# for k, v in data.items():
#     if k == name:
#         print(v)
#     else:
#         print('Not found')

print(data.get(name, 'Not found'))
