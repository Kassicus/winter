import pygame
import color
import animation

class Player():
    def __init__(self):
        self.x = 500
        self.y = 400

        self.width = 38
        self.height = 64

        self.rect = (self.x, self.y, self.width, self.height)

        self.walking_speed = 5

        self.x_velocity = 0
        self.y_velocity = 0

        self.friction = 1

        self.facing_left = pygame.image.load("assets/test/player_test_left.png")
        self.facing_right = pygame.image.load("assets/test/player_test_right.png")

        self.image = self.facing_left

        #self.anim_walk_left = animation.StaticAnimation()
        #self.anim_walk_right = animation.StaticAnimation()
        #self.anim_walk_up = animation.StaticAnimation()
        #self.anim_walk_down = animation.StaticAnimation()

        #self.anim_standing = animation.StaticAnimation()

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

        self.x += self.x_velocity
        self.y += self.y_velocity

        self.move()

    def move(self):
        if self.x_velocity < 0:
            self.x_velocity += self.friction
            self.image = self.facing_left
        elif self.x_velocity > 0:
            self.x_velocity -= self.friction
            self.image = self.facing_right

        if self.y_velocity < 0:
            self.y_velocity += self.friction
        elif self.y_velocity > 0:
            self.y_velocity -= self.friction

        if pygame.key.get_pressed()[pygame.K_a]:
            self.x_velocity = -self.walking_speed
        elif pygame.key.get_pressed()[pygame.K_d]:
            self.x_velocity = self.walking_speed

        if pygame.key.get_pressed()[pygame.K_w]:
            self.y_velocity = -self.walking_speed
        elif pygame.key.get_pressed()[pygame.K_s]:
            self.y_velocity = self.walking_speed