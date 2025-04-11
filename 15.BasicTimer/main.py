"""
Basic Timer that counts up
"""

import pygame, time

pygame.init()

WIDTH, HEIGHT = 700, 300

root = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Timer")

running = True
clock = pygame.time.Clock()
font = pygame.font.Font(None, 80)
start_time = time.time()


def main():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        root.fill("white")
        text_surface = font.render(f"{round(time.time() - start_time)}", True, "black")
        root.blit(text_surface, (root.get_width() / 2 - text_surface.get_width() / 2, root.get_height() / 2 - text_surface.get_width() / 2))

        clock.tick(60)
        pygame.display.flip()
    pygame.quit()


main()
