class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")


name = input()
level = input()

player1 = Player(name, level)
player1.intro()
