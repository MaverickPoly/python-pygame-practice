"""
Simple Sprite animaion. 
An image that changes of the class
"""

import pygame
import os


WIDTH, HEIGHT = 1100, 600
FPS = 60
DARK_GRAY = (25, 25, 20)
PLAYER_W, PLAYER_H = 50, 100


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.animation_frames = [
            pygame.transform.scale(pygame.image.load(os.path.join("13.SpriteAnimation", "images", f"image_{i}.png")).convert(), (PLAYER_W, PLAYER_H))
            for i in range(10)
        ]
        self.frame_index = 0
        self.image = self.animation_frames[self.frame_index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_speed = 5
        self.frame_counter = 0

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.animation_speed:
            self.frame_counter = 0
            self.frame_index = (self.frame_index + 1) % len(self.animation_frames)
            self.image = self.animation_frames[self.frame_index]
        

class Game:
    def __init__(self):
        pygame.init()

        self.root = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sprite animation")
        self.running = True
        self.clock = pygame.time.Clock()

        self.sprite_group = pygame.sprite.Group()
        self.player = Player(WIDTH / 2 - PLAYER_W / 2, HEIGHT / 2 - PLAYER_H / 2, self.sprite_group)

        self.run()
        pygame.quit()

    def update(self):
        self.root.fill(DARK_GRAY)

        self.sprite_group.update()
        self.sprite_group.draw(self.root)

        self.clock.tick(FPS)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update()


if __name__ == "__main__":
    Game()
        