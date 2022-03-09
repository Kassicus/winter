import pygame
import items
import random

class World():
    def __init__(self):
        self.ground_items = [
            items.Stone(random.randint(100, 900), random.randint(100, 700)),
            items.Stone(random.randint(100, 900), random.randint(100, 700)),
            items.Stone(random.randint(100, 900), random.randint(100, 700))
        ]

    def draw(self, surface):
        for item in self.ground_items:
            item.draw(surface)

    def update(self, events, inventory, player):
        for item in self.ground_items:
            item.update(player)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for item in self.ground_items:
                        if item.player_can_pickup(player):
                            inventory.add_item(item)
                            index = self.ground_items.index(item)
                            self.ground_items.pop(index)