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

def draw_bars(screen, arr, i_idx = None, j_idx = None, min_idx = None):
    screen.fill(black)
    bar_width = size[0] // len(arr) #sizing the bar width so all bar can fit
    max_val = max(arr)

    for i in range(len(arr)):
        
        color = green
        
        if i == i_idx:
            color = blue
        elif i == j_idx:
            color = orange
        elif i == min_idx:
            color = red

        bar_height = (arr[i] / max(arr)) * size[1] * 0.8 #scaling the height
        pygame.draw.rect(screen, color, (i * bar_width, size[1] - bar_height, bar_width - 1, bar_height))
    pygame.display.update()

def sort(screen, arr):
    n = len(arr)
    for i in range(n):
        min_idx = i

        #highligth starting point
        draw_bars(screen, arr, i_idx = i, min_idx = min_idx)
        #pygame.time.delay(5)

        for j in range(i + 1, n):
            #highlight j and current min
            draw_bars(screen, arr, i_idx = i, j_idx = j, min_idx = min_idx)
            #pygame.time.delay(5)

            if arr[j] < arr[min_idx]:
                min_idx = j

                #highligth new min
                draw_bars(screen, arr, i_idx = i, j_idx = j, min_idx = min_idx)
                #pygame.time.delay(5)

        #swap after finishing timer loop
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

        #highligth swap result
        draw_bars(screen, arr, i_idx = i, min_idx = min_idx)
        #pygame.time.delay(5)

    #final draw
    draw_bars(screen, arr)


def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen):
    running = True
    arr = make_data(200, 10, 500)
    sorting = False

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not sorting:
                    sorting = True
                    sort(screen, arr)
                    sorting = False

                if event.key == pygame.K_r:
                    arr = make_data(200, 10, 500)
                    draw_bars(screen, arr)

        if not sorting:
            draw_bars(screen, arr)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()



