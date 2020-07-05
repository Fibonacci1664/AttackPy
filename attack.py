import random

'''
This is a multi line comment
I can write line
after line
after
line.
'''

# This is a single line comment


class Enemy:
    hp = 200            # This is an instance variable/attribute/member/field

    def __init__(self, atkl, atkh):     # This is basically a constructor.
        self.atkl = atkl
        self.atkh = atkh

    def getatk(self):
        print(self.atkl)

    def gethp(self):
        print("HP is ", self.hp)


enemy1 = Enemy(40, 49)
enemy1.getatk()
enemy1.gethp()

enemy2 = Enemy(75, 9)
enemy2.getatk()
enemy2.gethp()


# playerhp = 260
# enemyatkl = 60
# enemyatkh = 80
#
# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp -= dmg
#
#     if playerhp <= 30:
#         playerhp = 30
#
#     print("Enemy strikes for ", dmg, "point of damage. Current HP is now ", playerhp)
#
#     if playerhp > 30:
#         continue
#
#     print("You use magic to teleport away from the danger!")
#     break;

