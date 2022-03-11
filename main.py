import pygame
import color
import player
import animation

pygame.init()

class Game():
    def __init__(self):
        self.window_width = 1000
        self.window_height = 800

        self.window_title = "Untitled Winter Survival Game"

        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        pygame.display.set_caption(self.window_title)

        self.running = True

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.player = player.Player()

        animation.test_animation.playing = True

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

            self.draw()

            self.update()

    def draw(self):
        self.screen.fill(color.black)

        self.player.draw(self.screen)

        animation.test_animation.draw(self.screen)

    def update(self):
        self.player.update()

        animation.test_animation.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()