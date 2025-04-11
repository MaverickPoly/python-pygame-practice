"""
Load and display an image on the screen
"""

import pygame
import os

pygame.init()

info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Display")
clock = pygame.time.Clock()

image = pygame.image.load(os.path.join("8.ImageDisplay", "image1.jpg")).convert()
image = pygame.transform.scale(image, (WIDTH, HEIGHT))
rect = image.get_rect()
rect.topleft = (0, 0)

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")
        screen.blit(image, (0, 0), rect)

        clock.tick(FPS)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
