# Boards/board.py
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, BOARD_COLOR, POINT_COLOR_1, POINT_COLOR_2, POINT_WIDTH, POINT_HEIGHT, \
    BAR_WIDTH


class Board:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        # Fill background
        self.screen.fill(BOARD_COLOR)

        # Calculate bar position
        mid_x = SCREEN_WIDTH // 2
        pygame.draw.rect(self.screen, (0, 0, 0), (mid_x - BAR_WIDTH // 2, 0, BAR_WIDTH, SCREEN_HEIGHT))

        # Draw points (triangles)
        for i in range(6):  # 6 triangles on each side of the bar
            # Left side triangles
            left_x = i * POINT_WIDTH
            color = POINT_COLOR_2 if i % 2 == 0 else POINT_COLOR_1
            top_triangle = [(left_x, 0), (left_x + POINT_WIDTH, 0), (left_x + POINT_WIDTH // 2, POINT_HEIGHT)]
            pygame.draw.polygon(self.screen, color, top_triangle)
            bottom_triangle = [(left_x, SCREEN_HEIGHT), (left_x + POINT_WIDTH, SCREEN_HEIGHT),
                               (left_x + POINT_WIDTH // 2, SCREEN_HEIGHT - POINT_HEIGHT)]
            color = POINT_COLOR_1 if i % 2 == 0 else POINT_COLOR_2
            pygame.draw.polygon(self.screen, color, bottom_triangle)

            # Right side triangles
            right_x = mid_x + BAR_WIDTH // 2 + i * POINT_WIDTH
            color = POINT_COLOR_2 if i % 2 == 0 else POINT_COLOR_1
            top_triangle = [(right_x, 0), (right_x + POINT_WIDTH, 0), (right_x + POINT_WIDTH // 2, POINT_HEIGHT)]
            pygame.draw.polygon(self.screen, color, top_triangle)

            bottom_triangle = [(right_x, SCREEN_HEIGHT), (right_x + POINT_WIDTH, SCREEN_HEIGHT),
                               (right_x + POINT_WIDTH // 2, SCREEN_HEIGHT - POINT_HEIGHT)]
            color = POINT_COLOR_1 if i % 2 == 0 else POINT_COLOR_2
            pygame.draw.polygon(self.screen, color, bottom_triangle)