class Number:
    def __init__(self, num):
        self.value = num

    def isEven(self):
        return self.value % 2 == 0

x = Number(int(input()))
print(x.isEven())
