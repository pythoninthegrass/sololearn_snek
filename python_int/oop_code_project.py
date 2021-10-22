class Enemy:
  name = ""
  lives = 0
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)

class OwnWorst(Enemy):
  def __init__(self):
    super().__init__('Human', 2)


m = Monster()
a = Alien()
o = OwnWorst()


while (m.lives > 0 or a.lives > 0) and o.lives > 0:
    x = input('gun or laser?\nRaise your weapon: ')
    if x == 'exit':
        print('The only way to win is to not start.')
        break
    elif x == 'laser':
        a.hit()
    elif x == 'gun':
        m.hit()
    else:
        print(r"That's not a knife. THIS is a knife.")
        o.hit()
