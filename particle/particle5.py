import pygame, random, math
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
fps = 60
size = (1000, 700)

class Bullet:
    def __init__(self, screen, pos, mass):
        self.screen = screen
        self.pos = pos
        self.mass = mass
        self.rect = pygame.Rect(self.pos[0] - (mass / 2), self.pos[1], self.mass, self.mass) #center the bullet spawn
        #the bullet life span
        self.life = 50 #100 | -1 | 60fps 
    
    def draw(self):
        pygame.draw.rect(self.screen, red, self.rect)

    def move(self):
        #self.pos[1] -= 50
        self.rect.y -= 30 # updating the rect pos

    def lifespan(self):
        self.life -= 1

    def hit(self):
        ...

class Target:
    def __init__(self, screen, pos, mass):
        self.screen = screen
        self.pos = pos
        self.mass = mass
        self.target = pygame.Rect(self.pos[0], self.pos[1], self.mass, self.mass)
        self.live = True

    def draw(self):
        pygame.draw.rect(self.screen, green, self.target)
            
    def hit(self, bullet):
        if self.target.colliderect(bullet):
            self.live = False
    
def init():
    pygame.init()
    screen = pygame.display.set_mode(size)
    
    return screen

def game_loop(screen):
    running = True
    clock = pygame.time.Clock()
    bullets = []
    targets = []
    shooting = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == MOUSEBUTTONDOWN:
                #pos = list(pygame.mouse.get_pos())
                shooting = True
                #bullets.append(Bullet(screen, pos, 30))
            if event.type == MOUSEBUTTONUP:
                shooting = False

        screen.fill(black)

        while len(targets) < 6:
            pos = [random.randint(0, size[0] - 100), 50]
            targets.append(Target(screen, pos, 100))

        if shooting:
            pos = list(pygame.mouse.get_pos())

            bullets.append(Bullet(screen, pos, 30))

        '''
        for target in targets:
            if target.live:
                target.draw()
                target.hit()
        '''

        for bullet in bullets:
            bullet.draw()
            bullet.move()
            bullet.lifespan()

            if bullet.life < 0:
                bullets.remove(bullet) #removing the bullet after a period of time

        for target in targets:
            target.draw()
            for bullet in bullets:
                target.hit(bullet)
            if target.live == False:
                targets.remove(target)

        print(f"{len(targets)} {len(bullets)}")
        pygame.display.update()
        clock.tick(fps)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()


