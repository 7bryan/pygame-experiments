import pygame, random, math
from pygame.locals import *

black = (0, 0, 0)
size = (800, 600)

def init():
    pygame.init()
    screen = pygame.display.set_mode(size)
    
    return screen 

def game_loop(screen):
    fps = 60
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(black)

        pygame.display.update()
        clock.tick(fps)

def main():
    screen = init()
    game_loop(screen)
    pygame.init()

if __name__ == "__main__":
    main()


