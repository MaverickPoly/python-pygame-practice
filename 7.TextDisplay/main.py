"""
Displaying a simple text in the middle of the screen
"""

import pygame

pygame.init()

WIDTH, HEIGHT = 800, 400

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Display Text")

font = pygame.font.SysFont("Arial", 50)
text_surface = font.render("Hello Pygame", True, (30, 30, 30))
running = True


def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")
        screen.blit(text_surface, (WIDTH / 2 - text_surface.get_width() / 2, HEIGHT / 2 - text_surface.get_height() / 2))
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
