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

    def initializeStart(self):
        checkerPieces = []
        for pieceNumber, positionInfo in CHECKERS_STARTING_POSITIONS.items():
            if pieceNumber <= 15:
                checkerPieces.append(Checker(CHECKER_COLOR_WHITE, positionInfo))
            else:
                checkerPieces.append(Checker(CHECKER_COLOR_BLACK, positionInfo))
        return checkerPieces


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.board.draw()
            for checker in self.checkerPieces:
                checker.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    Game().run()

