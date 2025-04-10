"""
This app draws the rectangle as we click and drag our mouse.
"""

import pygame
import sys

GRAY = (30, 30, 30)

class Game:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode()
        self.start_pos = None
        self.rect = None
        self.running = True

        pygame.display.set_caption("Draw Rectangle")

    def update(self):
        self.root.fill(GRAY)

        if self.rect:
            pygame.draw.rect(self.root, "cyan", self.rect, 1, 5)

        pygame.display.update()

    def handle_escape(self):
        self.rect = None

    def handle_mouse_down(self):
        self.start_pos = pygame.mouse.get_pos()
        self.handle_escape()

    def handle_mouse_move(self):
        if self.start_pos != None:
            self._render_rect()
    
    def handle_mouse_up(self):
        self._render_rect()
        self.start_pos = None

    def _render_rect(self):
        end = pygame.mouse.get_pos()
        left = min(self.start_pos[0], end[0])
        top = min(self.start_pos[1], end[1])
        width = end[0] - self.start_pos[0]
        height = end[1] - self.start_pos[1]
        self.rect = pygame.Rect(
            left, top,
            abs(width), abs(height)
        )
        
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_mouse_down()
                if event.type == pygame.MOUSEBUTTONUP:
                    self.handle_mouse_up()
                if event.type == pygame.MOUSEMOTION:
                    self.handle_mouse_move()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.handle_escape()

            self.update()
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
    