import random

class Dice:
    def __init__(self, diceSides: int = 6):
        self.diceSides = diceSides

    def roll(self):
        return random.randint(1, self.diceSides)
