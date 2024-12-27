# Checkers/checker.py
import pygame

class Checker:
    def __init__(self, color, position, radius=25):
        self.color = color
        self.position = position
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)