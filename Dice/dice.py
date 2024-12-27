# dice.py

import random

class Dice:
    def __init__(self, sides=6):
        """
        Initialize a generic dice with a specified number of sides.
        :par`am sides: Number of sides on the dice. Default is 6.
        """
        self.sides = sides

    def roll(self):
        """
        Roll the dice and return a random number between 1 and the number of sides.
        """
        return random.randint(1, self.sides)

    def __str__(self):
        return f"Dice({self.sides}-sided)"