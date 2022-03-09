import pygame
import color

class Player():
    def __init__(self):
        self.x = 500
        self.y = 400

        self.width = 38
        self.height = 64

        self.rect = (self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, color.white, self.rect)

    def update(self):
        pass