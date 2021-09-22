class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        # self.balance = 0
        # self.status = False
    def __add__(self, other):
        return self.balance + other.balance

a = BankAccount(1024)
b = BankAccount(42)

result = a + b
print(result)
