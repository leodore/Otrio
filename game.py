import logic
import pygame
from pygame.locals import *


class Board:
    def __init__(self):
        self.grid_lines = [[(25,200), (575,200)],
                           [(25,400), (575,400)],
                           [(200,25), (200,575)],
                           [(400,25), (400,575)]
                          ]
        self.circ_center = [(100,100), (100,300), (100,500),
                            (300,100), (300,300), (300,500),
                            (500,100), (500,300), (500,500)
                           ]
        self.circ_rad = [90,70,50]
    def draw(self, surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (0,0,0), line[0], line[1], 5)
        for c in self.circ_center:
            for r in self.circ_rad:
                pygame.draw.circle(surface, (105,105,105), c,r, 3)

class Game:
    def __init__(self):
        grid = Grid()
        self.screen = pygame.display.set_mode((1000,600))
        pygame.display.set_caption("Otrio")
        self.screen.fill((255,255,255))
        grid.draw(self.screen)


    def run(self):
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == KEYDOWN and event.key == K_q):
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(pygame.mouse.get_pos())

            pygame.display.flip()

def main():
    pygame.init()
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
