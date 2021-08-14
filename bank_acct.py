class BankAccount:
    def __init__(self, balance):
        self._balance = balance
        # print(f"Current balance: {self._balance}")

    def deposit(self, value):
        self._value = value
        return value + self._balance

    def __repr__(self):
         return f"Account Balance: {self._value}"

acc = BankAccount(0)
# print("How much to deposit?")
acc.deposit(int(input()))
print(acc)
