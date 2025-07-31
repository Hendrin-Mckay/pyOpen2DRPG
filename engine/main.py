import pygame

class Game:
    def __init__(self, title, width, height):
        pygame.init()
        self.title = title
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 0, 0))  # Black
            pygame.display.flip()

        pygame.quit()

if __name__ == '__main__':
    game = Game("My Game", 800, 600)
    game.run()
