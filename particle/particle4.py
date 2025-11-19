import pygame, random, math, sys
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
fps = 60
size = (1000, 700)
running = True

class Rectangle:
    def __init__(self, screen, pos, mass, running):
        self.screen = screen
        self.pos = pos
        self.mass = mass
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.mass, self.mass)
        self.running = running

    def draw(self):
        pygame.draw.rect(self.screen, red, self.rect) 

    def move(self):
        self.pos[0] += 10
        if self.pos[0] + self.mass > size[0]:
            pygame.quit()
            sys.exit()


class particle:
    def __init__(self, screen, position):
        self.screen = screen
        self.mass = random.randint(10 , 50)
        self.pos = [size[0] - self.mass, random.randint(self.positon, )]
        self.rect = pygame.draw.rect(self.pos, self.mass, self.mass)

        self.angle = random.uniform(0, math.pi)
        self.speed = random.randint(1, 5)
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed

    def draw(self):
        pygame.draw.rect(self.pos, self.mass, self.mass)

    def move(self):
        self.pos[0] += self.vx
        self.pos[1] += self.vy




def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen, mass, running):
    clock = pygame.time.Clock()
    pos = [0, size[1] / 2 - mass / 2] #setting so the rect is always on the middle of the window
    particles = []
    temp_pos = 0

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(black)

        rect1 = Rectangle(screen, pos, mass, running)
        
        if rect1.pos[0] + mass < size[0]:
            rect1.draw()
            rect1.move()
            temp_pos = rect1.pos[0]
        else:
            for i in range(50):
                particles.append(particle(screen, temp_pos))

        pygame.display.update()
        clock.tick(fps)

def main():
    mass = int(input("enter : "))
    screen = init()
    game_loop(screen, mass, running)

    pygame.quit()

if __name__ == "__main__":
    main() 
