car = {
    'brand':'BMW',
    'year': 2018,
    'color': 'red',
    'mileage': 15000
}

# print(car['brand'])

choice = input()

for k, v in car.items():
    if k == choice:
        print(v)
