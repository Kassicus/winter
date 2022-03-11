import pygame
import color

class Slot():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.width = 50
        self.height = 50

        self.rect = (self.x, self.y, self.width, self.height)

        self.item = None

    def hovered(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.x < mouse_pos[0] < self.x + self.width:
            if self.y < mouse_pos[1] < self.y + self.height:
                return True
            else:
                return False
        else:
            return False

    def draw(self, surface):
        pygame.draw.rect(surface, color.white, self.rect, 5)

        if self.item != None:
            surface.blit(self.item.image, (self.x + (self.width / 2) - (self.item.width / 2), self.y + (self.height / 2) - (self.item.height / 2)))

        if self.hovered():
            pygame.draw.rect(surface, color.green, self.rect)

    def update(self):
        pass

class Inventory():
    def __init__(self):
        self.x = 100
        self.y = 100
        
        self.width = 800
        self.height = 600

        self.rect = (self.x, self.y, self.width, self.height)

        self.active = False

        self.slots = [
            Slot(self.x + 10, self.y + 10),
            Slot(self.x + 70, self.y + 10),
            Slot(self.x + 130, self.y + 10)
        ]

    def add_item(self, entity):
        for slot in self.slots:
            if slot.item == None:
                slot.item = entity
                break

    def toggle_active(self):
        self.active = not self.active

    def draw(self, surface):
        if self.active:
            pygame.draw.rect(surface, color.white, self.rect, 5)

            for slot in self.slots:
                slot.draw(surface)

    def update(self):
        if self.active:
            for slot in self.slots:
                slot.update()