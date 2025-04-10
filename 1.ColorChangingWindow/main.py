"""
This app changes the background color of the screen every time we press `Spacebar` or use our mouse wheel
"""

import pygame
from random import randint


WIDTH, HEIGHT = 1200, 800
FPS = 60


class Game:
    def __init__(self):
        pygame.init()

        # Variables
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.color = (255, 255, 255, 1)

        # Setup
        pygame.display.set_caption("Color Changing Window")

    def handle_click(self):
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255), randint(0, 1))

    def update(self):
        self.window.fill(self.color)

        self.clock.tick(FPS)
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.handle_click()
                if event.type == pygame.MOUSEWHEEL:
                    self.handle_click()

            self.update()


if __name__ == "__main__":
    game = Game()
    game.run()
