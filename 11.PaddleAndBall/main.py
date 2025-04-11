"""
Simple Paddle that can move horizontally and Ball that bounces and moves
"""
import pygame
import random


WIDTH, HEIGHT = 1200, 600
FPS = 60
PADDLE_SPEED = 12
PADDLE_W, PADDLE_H = 160, 12
BALL_RADIUS = 20

class Paddle:
    def __init__(self, position, screen, color):
        self.rect = pygame.Rect(*position)
        self.screen = screen
        self.color = color

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and not self.rect.x < 0:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and not self.rect.x + PADDLE_W > WIDTH:
            self.rect.x += PADDLE_SPEED
        
    def update(self):
        self.move()
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ball:
    def __init__(self, vector: tuple[int, int], color: str | tuple[int, int, int], screen: pygame.Surface):
        self.vector = pygame.Vector2(*vector)
        self.position = pygame.Vector2(WIDTH / 2, HEIGHT / 2)
        self.color = color
        self.screen = screen

    def move(self):
        self.position += self.vector
        
        if self.position.x < 0 or self.position.x > WIDTH:
            self.vector.x *= -1
        if self.position.y < 0 or self.position.y > HEIGHT:
            self.vector.y *= -1

    def update(self):
        self.move()
        pygame.draw.circle(self.screen, self.color, self.position, BALL_RADIUS)



class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Paddle and ball")
        self.clock = pygame.time.Clock()
        self.running = True

        self.paddle = Paddle((WIDTH / 2 - PADDLE_W / 2, HEIGHT - 80, PADDLE_W, PADDLE_H), self.screen, "white")
        self.ball = Ball(
            (random.choice([-7, 7]), random.choice([-7, 7])), 
            (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
            self.screen
        )

        self.run()

    def collision(self):
        if self.ball.position.y + BALL_RADIUS > self.paddle.rect.y and \
           self.paddle.rect.x < self.ball.position.x < self.paddle.rect.x + PADDLE_W:
            self.ball.vector.y *= -1

    def update(self):
        self.screen.fill((30, 30, 30))
        self.collision()

        self.paddle.update()
        self.ball.update()
        
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
    Game()
