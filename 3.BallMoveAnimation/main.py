"""
Infinite bouncing ball animation
"""

import pygame
import random

WIDTH, HEIGHT = 1100, 600
RADIUS = 20
SPEED = 5
FPS = 60

class Game:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.clock = pygame.time.Clock()
        self.position = pygame.Vector2(WIDTH // 2 - RADIUS // 2, HEIGHT // 2 - RADIUS // 2)
        self.vector = pygame.Vector2(SPEED, SPEED)

    def handle_collide(self):
        if self.position.x + RADIUS * 2 > WIDTH or self.position.x <= 0:
            self.vector.x *= -1
        if self.position.y + RADIUS * 2 > HEIGHT or self.position.y <= 0:
            self.vector.y *= -1

    def update(self):
        self.root.fill("black")
        pygame.draw.circle(self.root, "brown", self.position, RADIUS)

        self.handle_collide()

        self.position += self.vector

        self.clock.tick(FPS)
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()
        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
