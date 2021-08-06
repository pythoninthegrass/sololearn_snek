class Vehicle: 
    def horn(self):
        print("Beep!")

class Car(Vehicle):
    def __init__(self, name, color):
        self.name = name
        self.color = color

car = Car("BMW", "red")
# print(f"Name: {car.name}\n Color: {car.color}")
car.horn()
