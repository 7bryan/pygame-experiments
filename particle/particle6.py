import pygame, random, math
from pygame.locals import *

black = (0, 0, 0)
fps = 60
size = (1000, 700)

class Particle:
    def __init__(self, screen, pos, mass):
        self.screen = screen
        self.pos = pos
        self.mass = mass
        self.rand = random.randint(0, 255)
        self.color = (self.rand, self.rand, self.rand)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.mass, self.mass)

        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.randint(4, 7)
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed

        self.life = 20
        
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        self.life -= 1

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy


def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen):
    clock = pygame.time.Clock()
    running = True
    particles = []
    explode = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                pos = list(pygame.mouse.get_pos())

                explode = True
                '''
                for i in range(50):
                    particles.append(Particle(screen, pos, random.randint(10, 30)))
                '''
            if event.type == MOUSEBUTTONUP:
                explode = False

            if event.type == MOUSEMOTION and explode:
                pos = event.pos
 

        screen.fill(black)
        
        if explode:
            for i in range(50):
                particles.append(Particle(screen, pos, random.randint(10, 30)))
        



        for particle in particles:
            particle.draw()
            particle.move()

            if particle.life < 0:
                particles.remove(particle)

        pygame.display.update()
        clock.tick(fps)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
