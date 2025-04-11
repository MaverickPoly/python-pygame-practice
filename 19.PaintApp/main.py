"""
Simple paint app that allows us to draw with different colors
"""

import pygame

WIDTH, HEIGHT = 1400, 800
FPS = 1000

# Colors
DARK_GRAY = (25, 25, 25)
GRAY = (230, 230, 230)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
MAGENTA = (255, 0, 255)
BROWN = (165, 45, 45)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

COLORS = [GRAY, RED, BLUE, GREEN, PURPLE, MAGENTA, BROWN, BLACK, YELLOW, ORANGE, WHITE]
COLOR_NAMES = ["White", "Red", "Blue", "Green", "Purple", "Magenta", "Brown", "Black", "Yellow", "Orange", "White"]

class App:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Simple Paint App")
        self.clock = pygame.time.Clock()
        self.running = True

        self.drawing = False
        self.brush_size = 5
        self.current_color = GRAY

        self.run()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drawing = True
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.drawing = False
            if event.type == pygame.MOUSEWHEEL:
                self.brush_size = max(1, self.brush_size + event.y)
                print(event.y)
            if event.type == pygame.KEYDOWN:
                if pygame.K_0 <= event.key <= pygame.K_9:
                    color_index = event.key - pygame.K_0
                    if color_index < len(COLORS):
                        self.current_color = COLORS[color_index]
                        print(f"Color switched to: {COLOR_NAMES[color_index]}")

    def draw(self):
        if self.drawing:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(self.root, self.current_color, pos, self.brush_size)

    def update(self):
        # self.root.fill(GRAY)
        self.draw()
        # self.clock.tick(FPS)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.handle_events()
            self.update()


if __name__ == "__main__":
    App()
