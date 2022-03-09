import pygame
import color
import player

pygame.init()

class Game():
    def __init__(self):
        self.window_width = 1000
        self.window_height = 800

        self.window_title = "Winter Survival Game"

        self.screen = pygame.display.set_mode([self.window_width, self.window_height])
        pygame.display.set_caption(self.window_title)

        self.running = True

        self.clock = pygame.time.Clock()
        self.events = pygame.event.get()

        self.player = player.Player()

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

    def update(self):
        self.player.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()