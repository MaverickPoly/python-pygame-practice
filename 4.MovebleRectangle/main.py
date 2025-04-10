"""
Rectangle that we can move using arrow keys, with collision detecting
"""

import pygame


WIDTH, HEIGHT = (1200, 600)
RECT_WIDTH, RECT_HEIGHT = 300, 200
SPEED = 10
FPS = 60

class Main:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Rectangle Movement")
        self.running = True
        self.rect = pygame.Rect(WIDTH / 2 - RECT_WIDTH / 2, HEIGHT / 2 - RECT_HEIGHT / 2, RECT_WIDTH, RECT_HEIGHT)
        self.clock = pygame.time.Clock()

    def handle_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not self.rect.y <= 0:
            self.rect.y -= SPEED
        if keys[pygame.K_DOWN] and not self.rect.y + RECT_HEIGHT >= HEIGHT:
            self.rect.y += SPEED
        if keys[pygame.K_LEFT] and not self.rect.x <= 0:
            self.rect.x -= SPEED
        if keys[pygame.K_RIGHT] and not self.rect.x + RECT_WIDTH >= WIDTH:
            self.rect.x += SPEED

    def handle_collision(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x + RECT_WIDTH >= WIDTH:
            self.rect.x = WIDTH - RECT_WIDTH
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.y + RECT_HEIGHT >= HEIGHT:
            self.rect.y = HEIGHT - RECT_HEIGHT

    def update(self):
        self.root.fill((20, 20, 20))

        pygame.draw.rect(self.root, "orange", self.rect, border_radius=7)
        # self.handle_collision()

        self.clock.tick(FPS)
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.handle_inputs()
            self.update()
        pygame.quit()

if __name__ == "__main__":
    app = Main()
    app.run()
