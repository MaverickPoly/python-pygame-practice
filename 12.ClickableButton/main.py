"""
Button that sends windows notification when clicked and changes color on hover
"""
import pygame
from plyer import notification


WIDTH, HEIGHT = 1100, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (40, 40, 40)
RED = (200, 0, 0)

BTN_WIDTH = 200
BTN_HEIGHT = 50


class Button:
    def __init__(self, width, height, x, y, color, text, font: pygame.font.Font, border_radius: int, screen: pygame.Surface):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.font = font
        self.border_radius = border_radius
        self.screen = screen
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect, border_radius=self.border_radius)
        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.screen.blit(text_surface, text_rect)

    def update(self):
        self.draw()


class App:
    def __init__(self):
        pygame.init()

        self.running = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Pygame Button")
        self.font = pygame.font.SysFont(None, 36)

        self.button = Button(
            BTN_WIDTH, BTN_HEIGHT, 
            WIDTH / 2 - BTN_WIDTH / 2, 
            HEIGHT / 2 - BTN_HEIGHT / 2, 
            WHITE, "Click me!", 
            self.font, 12, self.screen
        )

        self.run()
        pygame.quit()

    def send_notification(self):
        notification.notify(
            title = "Button Clicked",
            message = "You clicked the button in the app!",
            timeout = 5
        )

    def update(self):
        self.screen.fill(DARK_GRAY)

        self.button.update()

        pygame.display.update()
    
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button.rect.collidepoint(event.pos):
                        self.button.color = RED
                        self.send_notification()
                    else:
                        self.button.color = WHITE
                if event.type == pygame.MOUSEMOTION:
                    if self.button.rect.collidepoint(event.pos):
                        self.button.color = GRAY
                    else:
                        self.button.color = WHITE
            
            self.update()


if __name__ == "__main__":
    App()
