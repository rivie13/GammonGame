'''
GammonGame
Created by: Riviera Sperduto
creation date: 12/26/2024
last edit: 12/27/2024
'''


#importing stuff
import pygame, sys
from pygame.locals import *
from Boards.board import Board
from Checkers.checker import Checker
from Dice.dice import Dice
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CHECKER_COLOR_WHITE, CHECKER_COLOR_BLACK, POINT_WIDTH, POINTS_POSITIONS_DICT, CHECKERS_STARTING_POSITIONS

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("GAMMON")
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen)
        #dictionary of Checker objects created by dictionary of checker piece starting position info...
        self.checkerPieces = self.initializeStart()
        self.dice1 = Dice(self.screen)
        self.dice2 = Dice(self.screen)

    def initializeStart(self):
        checkerPieces = []
        for pieceNumber, positionInfo in CHECKERS_STARTING_POSITIONS.items():
            if pieceNumber <= 15:
                checkerPieces.append(Checker(CHECKER_COLOR_WHITE, positionInfo))
            else:
                checkerPieces.append(Checker(CHECKER_COLOR_BLACK, positionInfo))
        return checkerPieces


    def run(self):
        players = ["Player 1", "Player 2"]  # Define players
        current_player_index = 0  # Start with Player 1

        dice_rolled = False  # Flag to check if dice have been rolled

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Handle key presses for the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and not dice_rolled:
                        # Roll dice if space is pressed and dice haven't been rolled yet
                        self.dice1.roll()
                        self.dice2.roll()

                        # Print results (or implement game logic here)
                        print(
                            f"{players[current_player_index]} rolled {self.dice1.current_value} and {self.dice2.current_value}"
                        )

                        # Draw the dice results
                        self.dice1.draw(self.screen, self.dice1, (200, 200))
                        self.dice2.draw(self.screen, self.dice2, (300, 200))
                        pygame.display.flip()

                        dice_rolled = True  # Set flag to True once dice are rolled

                    elif event.key == pygame.K_RETURN and dice_rolled:
                        # Switch player when Enter is pressed after dice have been rolled
                        current_player_index = (current_player_index + 1) % len(players)
                        dice_rolled = False  # Reset dice roll flag for the next player

            # Clear the screen (but after drawing the dice)
            self.screen.fill((0, 0, 0))  # Assuming a black background

            # Draw the board and checkers
            self.board.draw()
            for checker in self.checkerPieces:
                checker.draw(self.screen)

            # Display current player's turn
            font = pygame.font.Font(None, 36)
            turn_text = font.render(f"{players[current_player_index]}'s Turn", True, (255, 255, 255))
            self.screen.blit(turn_text, (100, 300))

            # If dice have been rolled, show the results and wait for Enter to switch turns
            if dice_rolled:
                font = pygame.font.Font(None, 36)
                pause_text = font.render(
                    f"{players[current_player_index]}'s turn complete. Press Enter for next turn.", True,
                    (255, 255, 255)
                )
                self.screen.blit(pause_text, (100, 400))

                # Draw the dice results on top of the board and other elements
                self.dice1.draw(self.screen, self.dice1, (200, 200))
                self.dice2.draw(self.screen, self.dice2, (300, 200))

            # Update the display
            pygame.display.flip()

            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()

