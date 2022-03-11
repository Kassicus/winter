import pygame
import color

class Player():
    def __init__(self, surface):
        self.x = 500
        self.y = 400

        self.width = 38
        self.height = 64

        self.rect = (self.x, self.y, self.width, self.height)

        self.images = [
            pygame.image.load("assets/test/player_test_left.png"),
            pygame.image.load("assets/test/player_test_right.png")
        ]

        self.master_surface = surface

        self.walking_speed = 5

        self.x_velocity = 0
        self.y_velocity = 0

        self.friction = 1

        self.facing = 'left'

        self.notice_font = pygame.font.Font("assets/fonts/hurmit.otf", 18)

    def notify_pickup(self, entity_id):
        notice = ("Press [SPACE] to pickup: " + str(entity_id))
        notice_text = self.notice_font.render(notice, 1, color.white)
        self.master_surface.blit(notice_text, (self.x - 25, self.y - 25))

    def movement_handler(self):
        if self.x_velocity < 0:
            self.facing = 'left'
        elif self.x_velocity > 0:
            self.facing = 'right'

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

    def draw(self, surface):
        if self.facing == 'left':
            surface.blit(self.images[0], (self.x, self.y))
        elif self.facing == 'right':
            surface.blit(self.images[1], (self.x, self.y))

    def update(self):
        self.x += self.x_velocity
        self.y += self.y_velocity

        self.movement_handler()