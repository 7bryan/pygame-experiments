import pygame, random, math
from pygame.locals import *

size = (800, 600)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
fps = 30


class Circle:
    def __init__(self, screen, color, pos, rad):
        self.screen = screen
        self.color = color
        self.pos = pos
        self.rad = rad

        #init the move speed of x and y
        self.move_x = random.randint(-3, 3)
        self.move_y = random.randint(-3, 3)

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

    def collide(self, other):
        #getting the distance on x and y axis
        dx = self.pos[0] - other.pos[0]
        dy = self.pos[1] - other.pos[1]
        #getting the distance between two point based on the dx and dy
        distance = math.hypot(dx, dy)
        
        return distance < (self.rad + other.rad) #check if two circle collide



def init():
    pygame.init()
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("particle")

    return screen

def main_loop(screen):
    running = True
    circles = [] #list for string all the cirle class in the screen
    clock = pygame.time.Clock()

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
            
        
        for i in range(len(circles)):
            for j in range(i + 1, len(circles)):
                c1 = circles[i]
                c2 = circles[j]
                if c1.collide(c2):
                    c1.move_x *= -1
                    c1.move_y *= -1
                    c2.move_x *= -1
                    c2.move_y *= -1

        pygame.display.update()
        clock.tick(fps)


def main():
    screen = init()
    main_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()
