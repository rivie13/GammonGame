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
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, CHECKER_COLOR_WHITE, CHECKER_COLOR_BLACK, POINT_WIDTH

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("GAMMON")
        self.clock = pygame.time.Clock()
        self.board = Board(self.screen)
        #create a position placement dictionary which will go through all the board positions
        #center of each position is 32.08 mod since spots are 64.16... should I round up?
        self.checkers = [
            Checker(CHECKER_COLOR_WHITE, (SCREEN_WIDTH // 4, 20)),
            Checker(CHECKER_COLOR_WHITE, (SCREEN_WIDTH // 4 + POINT_WIDTH, 20)),
            Checker(CHECKER_COLOR_BLACK, (SCREEN_WIDTH - SCREEN_WIDTH // 4, SCREEN_HEIGHT - 20)),
        ]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.board.draw()
            for checker in self.checkers:
                checker.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()

