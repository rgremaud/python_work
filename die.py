"""Building a class to imitate a dice"""
from random import randint

class Die:
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        dice_value = randint(1,self.sides)
        print(f"You have rolled a {dice_value}")

    def multi_roll(self, total_rolls):
        i = 0
        while i <= total_rolls:
            self.roll_die()
            i += 1


my_dice = Die(sides=20)
my_dice.multi_roll(total_rolls = 10)