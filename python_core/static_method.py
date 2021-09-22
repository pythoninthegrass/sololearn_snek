class Pizza:
	def __init__(self, toppings):
		self.toppings = toppings

	@staticmethod
	def validate_topping(topping):
		if topping == "pineapple":
			raise ValueError("No pineapples!")
		else:
			return True


def not_pineapple():
	if all(Pizza.validate_topping(i) for i in ingredients):
		pizza = Pizza(ingredients)
	return pizza

# TODO: while loop; validate (len: is/are, strip, list commas, re contractions)
# ingredients = ["cheese", "pepperoni", "pineapple"]
ingredients = input().title()
try:
	not_pineapple()
	print(f"V gud. {ingredients} are acceptable ")
except ValueError as e:
	print("Pineapples belong on trees")
