import pygame
import color
import player
import inventory
import world

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

        self.fps_font = pygame.font.Font("assets/fonts/hurmit.otf", 18)

        self.world = world.World()

        self.player = player.Player(self.screen)

        self.inventory = inventory.Inventory()

    def start(self):
        while self.running:
            self.events = pygame.event.get()

            for event in self.events:
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        self.inventory.toggle_active()

            self.draw()

            self.update()

    def get_fps(self):
        fps = ("fps: " + str(int(self.clock.get_fps())))
        fps_text = self.fps_font.render(fps, 1, color.white)
        return(fps_text)

    def draw(self):
        self.screen.fill(color.black)

        self.screen.blit(self.get_fps(), (10, 10))

        self.world.draw(self.screen)

        self.player.draw(self.screen)

        self.inventory.draw(self.screen)

    def update(self):
        self.world.update(self.events, self.inventory, self.player)

        self.player.update()

        self.inventory.update()

        pygame.display.update()
        self.clock.tick(30)

game = Game()
game.start()

pygame.quit()