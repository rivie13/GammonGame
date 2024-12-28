# dice.py

import random
import pygame

class Dice:
    def __init__(self, screen):
        """
        Initialize a generic dice with a specified number of sides.
        :par`am sides: Number of sides on the dice. Default is 6.
        """
        self.screen = screen
        self.sides = 6
        self.current_value = 1

    def roll(self):
        """
        Roll the dice and return a random number between 1 and the number of sides.
        """
        sides = int(self.sides)

        self.current_value = random.randint(1, sides)
        #return self.current_value

    def draw(self, screen, dice1, position1):
        """
        Draw two dice on the screen.
        :param screen: The pygame surface to draw on.
        :param dice1: The first dice object (normal or special).
        :param dice2: The second dice object (normal or special).
        :param position1: Tuple (x, y) for the position of the first dice.
        :param position2: Tuple (x, y) for the position of the second dice.
        """
        # Dimensions for the dice
        dice_size = 60
        border_width = 5
        font = pygame.font.Font(None, 36)  # Default font for numbers

        # Helper function to draw an individual dice
        def draw_single_dice(dice, position):
            x, y = position
            pygame.draw.rect(screen, (255, 255, 255), (x, y, dice_size, dice_size))  # Dice face
            pygame.draw.rect(screen, (0, 0, 0), (x, y, dice_size, dice_size), border_width)  # Border

            # Draw the number on the dice
            text = font.render(str(dice.current_value), True, (0, 0, 0))
            text_rect = text.get_rect(center=(x + dice_size // 2, y + dice_size // 2))
            screen.blit(text, text_rect)

        # Draw both dice
        draw_single_dice(dice1, position1)



    def __str__(self):
        return f"Dice({self.sides}-sided)"