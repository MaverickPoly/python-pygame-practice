"""
Generate random shape, with random color, position and sizes every x time
"""

import pygame
import time
import random


WIDTH, HEIGHT = 1300, 700
DARK_GRAY = (20, 20, 20)
FPS = 60

class App:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.start_time = time.time()
        self.running = True
        pygame.display.set_caption("Random Shape Generator")
        self.shape_options = ["circle", "rect", "polygon", "ellipse", "arc"]

        self.circles = []
        self.rects = []
        self.polygons = []
        self.ellipses = []

        self.run()
        pygame.quit()

    @staticmethod
    def get_rgba():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    def generate_shape(self):
        shape = random.choice(self.shape_options)
        match shape:
            case "circle":
                self.circles.append({
                    "color": self.get_rgba(), 
                    "center": (random.randint(0, WIDTH - 20), random.randint(0, HEIGHT - 20)), 
                    "radius": random.randint(5, 20)
                })
            case "rect":
                self.rects.append({
                    "color": self.get_rgba(),
                    "rect": pygame.Rect(
                        random.randint(0, WIDTH - 300), random.randint(0, HEIGHT - 300), 
                        random.randint(50, 300), random.randint(50, 300),
                    ),
                    "border_radius": random.randint(0, 20),
                })
            case "polygon":
                self.polygons.append({
                    "color": self.get_rgba(),
                    "points": [(random.randint(0, 1300), random.randint(0, 700)) for _ in range(random.randint(3, 6))]
                })
            case "ellipse":
                self.ellipses.append({
                    "color": self.get_rgba(),
                    "rect": pygame.Rect(random.randint(0, 500), random.randint(0, 400), random.randint(100, 700), random.randint(100, 400))
                })

    def update(self):
        self.window.fill(DARK_GRAY)

        if time.time() - self.start_time > 1:
            self.start_time = time.time()
            self.generate_shape()

        for circle in self.circles:
            pygame.draw.circle(self.window, **circle)
        for rect in self.rects:
            pygame.draw.rect(self.window, **rect)
        for polygon in self.polygons:
            pygame.draw.polygon(self.window, **polygon)
        for ellipse in self.ellipses:
            pygame.draw.ellipse(self.window, **ellipse)

        self.clock.tick(FPS)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()


if __name__ == "__main__":
    App()
