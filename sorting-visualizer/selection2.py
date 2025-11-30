import pygame, random
from pygame.locals import *

width = 1000
height = 700
size = [width, height]
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)

def make_data(size, min, max):
    arr = []
    for i in range(size):
        arr.append(random.randint(min, max))

    return arr

def draw_bars(screen, arr): 
    screen.fill(black) 
    bar_width = size[0] // len(arr) #sizing the bar width so all bar can fit 
    for i in range(len(arr)): 
        bar_height = (arr[i] / max(arr)) * size[1] * 0.8 #scaling the height 
        pygame.draw.rect(screen, green, (i * bar_width, size[1] - bar_height, bar_width - 1, bar_height)) 

    pygame.display.update() 

def sort(screen, arr): 
    for i in range(len(arr)): 
        min = i 
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr[min]: 
                min = j 

        arr[i], arr[min] = arr[min], arr[i] 
        draw_bars(screen, arr) 
        pygame.time.delay(50) 
    draw_bars(screen, arr) 
    pygame.time.delay(50)

def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen):
    running = True
    arr = make_data(200, 10, 500)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sort(screen, arr)
                if event.key == pygame.K_r:
                    arr = make_data(200, 10, 500)
                    draw_bars(screen, arr)

        draw_bars(screen, arr)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()


