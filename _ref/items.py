import pygame

class Stone():
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.width = 16
        self.height = 16

        self.pickup_offset = 48

        self.rect = (self.x, self.y, self.width, self.height)

        self.id = "stone_item"
        
        self.image = pygame.image.load("assets/test/stone.png")

        self.in_world = True

    def player_can_pickup(self, player):
        if self.x - self.pickup_offset < player.x + (player.width / 2) < self.x + self.width + self.pickup_offset:
            if self.y - self.pickup_offset < player.y + (player.width / 2) < self.y + self.height + self.pickup_offset:
                return True
            else:
                return False
        else:
            return False

    def draw(self, surface):
        if self.in_world:
            surface.blit(self.image, (self.x, self.y))

    def update(self, player):
        if self.player_can_pickup(player):
            player.notify_pickup(self.id)