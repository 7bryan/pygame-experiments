import pygame, random
from pygame.locals import *

size = (800, 600)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
fps = 60


class Circle:
    def __init__(self, screen, color, pos, rad):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.rad = rad

        #init the move speed of x and y
        self.move_x = random.randint(-4, 4)
        self.move_y = random.randint(-4, 4)

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.pos, self.rad)

    def move(self):
        #move the circle with the speed of x and y
        self.pos[0] += self.move_x
        self.pos[1] += self.move_y

        #check if the circle collide and change its direction to opposite way 
        if self.pos[0] >= size[0] - self.rad or self.pos[0] <= self.rad:
            self.move_x *= -1

        if self.pos[1] >= size[1] - self.rad or self.pos[1] <= self.rad:
            self.move_y *= -1


def init():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("particle")

    return screen

def main_loop(screen):
    running = True
    circles = [] #list for string all the cirle class in the screen

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #get the position of where we click and turned it into list so its modifiadable
                pos = list(pygame.mouse.get_pos()) 
                #get random color and random radius
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                rad = random.randint(1, 50)
                #append the circle class to the circles list
                circles.append(Circle(screen, color, pos, rad))


        screen.fill(black)

        #for each circle in circles, call the draw and move function of the circle class
        for circle in circles:
            circle.draw()
            circle.move()
            

        pygame.display.update()


def main():
    screen = init()
    main_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
