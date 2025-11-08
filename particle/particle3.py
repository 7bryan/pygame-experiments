import pygame, random, math
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
size = (1000, 700)
fps = 60

'''
for i in range(50):
    angle = random between 0 and 2π
    speed = random between 1 and 5
    vx = cos(angle) * speed
    vy = sin(angle) * speed
'''

class Particle:
    def __init__(self, screen, pos):
        self.screen = screen 
        self.color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
        self.pos = pos.copy()
        self.rad = random.randint(10, 50)
        #determine the speed and the angle for each explosion particle
        self.angle = random.uniform(0, 2 * math.pi)
        self.speed = random.randint(1, 5)
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.rad)

    def move(self):
        self.pos[0] += self.vx
        self.pos[1] += self.vy
            

def init():
    pygame.init()
    screen = pygame.display.set_mode(size)
    
    return screen 

def game_loop(screen):
    clock = pygame.time.Clock()
    running = True
    explosions = [] #container for each explosion

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                particles = [] #container for each particle
                pos = list(pygame.mouse.get_pos())
                #for each click, create 50 particle and store it in particles
                for i in range(50):
                    particles.append(Particle(screen, pos))
                #then store the 50 particle that stored in particles into explosions     
                explosions.append(particles)

        screen.fill(black)
        #for each click (each explosion in explosions), draw the 50 particle and move it
        for explosion in explosions:
            for particle in explosion:
                particle.draw()
                particle.move()

        pygame.display.update()
        clock.tick(fps)

def main():
    screen = init()
    game_loop(screen)
    pygame.quit()

if __name__ == "__main__":
    main()


