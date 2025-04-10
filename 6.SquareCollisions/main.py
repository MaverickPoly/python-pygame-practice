"""
We can move two squares, first arrows keys, second `wsad`.
They cannot go out of screen or collide with each other.
"""

import pygame


WIDTH, HEIGHT = 1300, 800
RECT_WIDTH, RECT_HEIGHT = 200, 200
SPEED = 10


class MyRect:
    def __init__(
            self,
            position: tuple[int, int], 
            color: tuple[int, int, int] | str, 
            display: pygame.Surface, 
        ):
        self.rect = pygame.Rect(position[0], position[1], RECT_WIDTH, RECT_HEIGHT)
        self.color = color
        self.display = display
            
    def update(self):
        pygame.draw.rect(self.display, self.color, self.rect, border_radius=12)


class App:
    def __init__(self):
        pygame.init()

        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Squares Collision")
        self.running = True
        self.clock = pygame.time.Clock()

        self.rect1 = MyRect((WIDTH / 3 - RECT_WIDTH, HEIGHT / 2 - RECT_HEIGHT), "wheat", self.display)
        self.rect2 = MyRect((WIDTH / 3 * 2, HEIGHT / 2 - RECT_HEIGHT), "gray", self.display)
        
        self.run()

    def move(self):
        rect1_x_old = self.rect1.rect.x
        rect1_y_old = self.rect1.rect.y
        rect2_x_old = self.rect2.rect.x
        rect2_y_old = self.rect2.rect.y

        keys = pygame.key.get_pressed()
        # RIGHT Rectangle
        if keys[pygame.K_UP] and self.rect2.rect.y > 0:
            self.rect2.rect.y -= SPEED
        if keys[pygame.K_DOWN] and self.rect2.rect.y + RECT_HEIGHT < HEIGHT:
            self.rect2.rect.y += SPEED
        if keys[pygame.K_LEFT] and self.rect2.rect.x > 0:
            self.rect2.rect.x -= SPEED
        if keys[pygame.K_RIGHT] and self.rect2.rect.x + RECT_WIDTH < WIDTH:
            self.rect2.rect.x += SPEED

        # LEFT Rectangle
        if keys[pygame.K_w] and self.rect1.rect.y > 0: # UP
            self.rect1.rect.y -= SPEED
        if keys[pygame.K_s] and self.rect1.rect.y + RECT_HEIGHT < HEIGHT: # DOWN
            self.rect1.rect.y += SPEED
        if keys[pygame.K_a] and self.rect1.rect.x > 0:  # LEFT
            self.rect1.rect.x -= SPEED
        if keys[pygame.K_d] and self.rect1.rect.x + RECT_WIDTH < WIDTH:  # RIGHT
            self.rect1.rect.x += SPEED
        
        if self.rect1.rect.colliderect(self.rect2.rect):
            self.rect1.rect.x = rect1_x_old
            self.rect1.rect.y = rect1_y_old
            self.rect2.rect.x = rect2_x_old
            self.rect2.rect.y = rect2_y_old

    def update(self):
        self.display.fill((50, 50, 50))
        self.move()

        self.rect1.update()
        self.rect2.update()

        self.clock.tick(60)
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
        pygame.quit()
    

if __name__ == "__main__":
    app = App()
