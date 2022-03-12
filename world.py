import pygame
import random

class Tree():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = pygame.image.load("assets/test/tree.png")

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        pass

class World():
    def __init__(self):
        self.trees = [
            Tree(random.randint(100, 900), random.randint(100, 700))
        ]

    def draw(self, surface):
        for tree in self.trees:
            tree.draw(surface)

    def update(self):
        for tree in self.trees:
            tree.update()