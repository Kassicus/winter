import pygame
import color

class Player():
    def __init__(self):
        self.x = 500
        self.y = 400

        self.width = 38
        self.height = 64

        self.rect = (self.x, self.y, self.width, self.height)

        self.image = pygame.image.load("assets/test/player_test.png")

        self.walking_speed = 5

        self.x_velocity = 0
        self.y_velocity = 0

        self.friction = 1

    def draw(self, surface):
        #pygame.draw.rect(surface, color.white, self.rect)
        surface.blit(self.image, (self.x, self.y))

    def update(self, events):
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.movement_handler(events)

    def movement_handler(self, events):
        if self.x_velocity > 0:
            self.x_velocity -= self.friction
        elif self.x_velocity < 0:
            self.x_velocity += self.friction
        else:
            self.x_velocity = 0

        if self.y_velocity > 0:
            self.y_velocity -= self.friction
        elif self.y_velocity < 0:
            self.y_velocity += self.friction
        else:
            self.y_velocity = 0

        if pygame.key.get_pressed()[pygame.K_a]:
            self.x_velocity = -self.walking_speed
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.x_velocity = self.walking_speed

        if pygame.key.get_pressed()[pygame.K_w]:
            self.y_velocity = -self.walking_speed
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.y_velocity = self.walking_speed