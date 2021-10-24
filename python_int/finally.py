menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

# TODO: 3, item not found
try:
	for i in range(menu):
		if input() == i:
			print(f"{i}\nThanks for your order")
except (IndexError, TypeError):
	print('Item not found')