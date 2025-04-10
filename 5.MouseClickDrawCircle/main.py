"""
Draws circle where we click in the window
"""
import pygame
from random import randint


WIDTH, HEIGHT = 1200, 600
RADIUS = 30

class App:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Mouse Click")
        self.clock = pygame.time.Clock()
        self.running = True
        self.circles = []

        self.run()

    def handle_click(self):
        position = pygame.mouse.get_pos()
        # Color, Center, Radius
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.circles.append([color, position])
    
    def update(self):
        self.root.fill((40, 40, 40))

        for circle in self.circles:
            pygame.draw.circle(self.root, circle[0], circle[1], RADIUS)

        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click()
            self.update()
        pygame.quit()


if __name__ == "__main__":
    App()
