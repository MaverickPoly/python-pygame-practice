"""
Play a sound when Spacebar is pressed or a Button is Clicked
"""

import pygame
import os

pygame.init()

WIDTH, HEIGHT = 1100, 600
RECT_W, RECT_H = 130, 130


screen = pygame.display.set_mode((WIDTH, HEIGHT))
sound = pygame.mixer.Sound(os.path.join("9.PlaySound", "sound.mp3"))
rect = pygame.Rect(WIDTH / 2 - RECT_W / 2, HEIGHT / 2 - RECT_H / 2, RECT_W, RECT_H)

pygame.display.set_caption("Play a sound")

def play_sound():
    sound.play()

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                    play_sound()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    play_sound()

        screen.fill("violet")
        pygame.draw.rect(screen, "wheat", rect, border_radius=18)
        
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
