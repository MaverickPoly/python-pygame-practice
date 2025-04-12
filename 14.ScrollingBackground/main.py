"""
Background that moves/scrolls left constantly
"""

import pygame
import os


WIDTH, HEIGHT = 533, 800

class Main:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Scrolling Background")
        self.clock = pygame.time.Clock()
        self.running = True

        self.bg_image = pygame.image.load(os.path.join("14.ScrollingBackground", "bgImage.jpg")).convert_alpha()
        self.bg_image = pygame.transform.scale(self.bg_image, (self.bg_image.get_width(), HEIGHT))

        self.scroll_x = 0
        self.bg_width = self.bg_image.get_width()

        self.run()
        pygame.quit()

    def update(self):
        self.root.fill((30, 30, 30))

        self.scroll_x -= 5

        if self.scroll_x <= -self.bg_width:
            self.scroll_x = 0
        
        self.root.blit(self.bg_image, (self.scroll_x, 0))
        self.root.blit(self.bg_image, (self.scroll_x + self.bg_width, 0))

        self.clock.tick(60)
        pygame.display.flip()

    def run(self):
        while self.running:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.running = False

            self.update()


if __name__ == "__main__":
    main = Main()
