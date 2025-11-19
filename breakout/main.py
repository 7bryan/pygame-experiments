import pygame, math, random
from pygame.locals import *

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
size = (1000, 700)
fps = 60

class Wall:
    def __init__(self, screen, pos, width, height):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)

    def draw(self):
        pygame.draw.rect(self.screen, green, self.rect)

class Player:
    def __init__(self, screen, pos, width, height):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        self.move_right = False
        self.move_left = False

    def draw(self):
        pygame.draw.rect(self.screen, red, self.rect)

    def move(self):
        if self.move_right:
            self.rect.x += 10 
        if self.move_left:
            self.rect.x -= 10

class Ball:
    def __init__(self, screen, pos, width, height):
        self.screen = screen
        self.pos = pos
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.width, self.height)
        
        #self.angle = random.uniform(-math.pi / 4, math.pi + math.pi/4)
        self.angle = random.choice([random.uniform(-1, -0.2), random.uniform(math.pi + 0.2, math.pi + 1)])
        self.speed = 8
        self.vx = math.cos(self.angle) * self.speed
        self.vy = math.sin(self.angle) * self.speed
        
    def draw(self):
        pygame.draw.rect(self.screen, blue, self.rect)

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy


def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen):
    running = True
    clock = pygame.time.Clock()
    walls = []
    player = Player(screen, [450, 600], 100, 20)
    ball = Ball(screen, [490, 580], 20, 20)

    for i in range(5):
        for j in range(10):
            walls.append(Wall(screen, [100 * j, (30 * i)], 90, 20))

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.move_right = True 
                if event.key == pygame.K_a:
                    player.move_left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.move_right = False
                if event.key == pygame.K_a:
                    player.move_left = False

        screen.fill(black)

        for wall in walls:
            wall.draw()

        player.draw()
        player.move()

        ball.draw()
        ball.move()

        #bounce on paddle
        if ball.rect.colliderect(player.rect):
            ball.vy = -abs(ball.vy)

            #change angle depending where it hits paddle
            hit_pos = (ball.rect.centerx - player.rect.centerx) / (player.width / 2)
            ball.vx = hit_pos * 8 # adjust for angle efect

        if ball.rect.left < 0 or ball.rect.right > size[0] :
            ball.vx = -ball.vx
        if ball.rect.top <= 0:
            ball.vy = -ball.vy
        if ball.rect.bottom >= size[1]:
            running = False

        for wall in walls:
            if ball.rect.colliderect(wall.rect):
                walls.remove(wall)
                ball.vy = -ball.vy
                break

        pygame.display.update()
        clock.tick(fps)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
