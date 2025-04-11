"""
A simple program that counts the number of frames and time, then displays it
"""

import pygame
import time


WIDTH, HEIGHT = 1200, 600


class App:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

        pygame.display.set_caption("Frames Counter")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 40)
        
        self.frames = 0
        self.start_time = time.time()

        self.run()

    def update(self):
        self.screen.fill("black")

        self.frames += 1
        current_time = time.time()

        frame_text = self.font.render(f"Frames: {self.frames}", True, "white")
        time_text = self.font.render(f"Time: {round(current_time - self.start_time)}", True, "white")

        self.screen.blit(frame_text, (300, HEIGHT / 2 - frame_text.get_height() / 2))
        self.screen.blit(time_text, (700, HEIGHT / 2 - frame_text.get_height() / 2))

        self.clock.tick(30)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.update()
        pygame.quit()


if __name__ == "__main__":
    App()
