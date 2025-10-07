from dice import Dice

class DiceHand:
    def __init__(self, numb_dice: int = 1):
        self.dice = [Dice() for _ in range(numb_dice)]
        self.lastRoll = []
   def roll(self):
        self.lastRoll = [die.roll() for die in self.dice]
        return self.lastRoll

    def __str__(self):
        return " ".join(str(die) for die in self.lastRoll)
    
