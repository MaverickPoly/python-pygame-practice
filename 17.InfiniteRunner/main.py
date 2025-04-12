"""
A runner that kinda runs infinately and can jump.
"""

import pygame
import os


WIDTH, HEIGHT = 800, 400
FPS = 60
DARK_GRAY = (20, 20, 20)
PLAYER_W, PLAYER_H = 80, 140


class Player:
    def __init__(self, screen: pygame.Surface, x: int, y: int):
        self.screen = screen

        self.animation_frames = [
            pygame.image.load(os.path.join("17.InfiniteRunner", "images", f"player_walk_{i}.png")).convert_alpha()
            for i in range(1, 3)
        ]
        self.frame_index = 0
        self.image = self.animation_frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(x, y), )
        self.animation_speed = 10
        self.frame_counter = 0

        # Jump
        self.player_jump = pygame.image.load(os.path.join("17.InfiniteRunner", "images", "jump.png")).convert_alpha()
        self.gravity = 0

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animate(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.frame_counter += 1
            if self.frame_counter >= self.animation_speed:
                self.frame_counter = 0
                self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
                self.image = self.animation_frames[self.frame_index]

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.get_input()
        self.apply_gravity()
        self.animate()
        self.draw()


class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Infinite Runner")
        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(self.screen, 300, 300)
        self.sky = pygame.image.load(os.path.join("17.InfiniteRunner", "images", "Sky.png")).convert_alpha()
        self.ground = pygame.image.load(os.path.join("17.InfiniteRunner", "images", "ground.png")).convert_alpha()

        self.run()
        pygame.quit()

    def update(self):
        self.screen.fill("white")

        self.screen.blit(self.sky, (0, 0))
        self.screen.blit(self.ground, (0, 300))

        self.player.update()

        self.clock.tick(FPS)
        pygame.display.update()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()



if __name__ == "__main__":
    game = Game()
