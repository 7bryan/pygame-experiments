import pygame, random
from pygame.locals import * 
#data = [5, 1, 4, 2, 8, 10, 11, 1, 4, 2, 2, 2, 41, 101, 45]

black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
orange = (255, 165, 0)
size = (1000, 700)

def make_data(size, min, max):
    data = []
    for i in range(size):
        data.append(random.randint(min, max))
    return data

def draw_bars(screen, array, curret_idx=None, comparing_idx=None, sorted_border=None):
    screen.fill(black)
    bar_width = size[0] // len(array)
    max_val = max(array)
    for i, val in enumerate(array):
        color = green
        if i == curret_idx:
            color = blue
        elif i  == comparing_idx:
            color = orange
        elif i == sorted_border is not None and i >= sorted_border:
            color = (100, 100, 100) #grey

        bar_height = (val / max(array)) * size[1] * 0.8
        pygame.draw.rect(screen, color, (i * bar_width, size[1] - bar_height, bar_width - 1, bar_height))
    pygame.display.update()

def sort(screen, data):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            draw_bars(screen, data, j, j + 1, sorted_border = n - i)
            
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_bars(screen, data, j, j + 1, sorted_border = n - i)
                
        draw_bars(screen, data, sorted_border = n - i)
        
    draw_bars(screen, data)


def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen):
    running = True
    data = make_data(200, 10, 500)

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    sort(screen, data)
                if event.key == pygame.K_r:
                    data = make_data(200, 10, 500)
                    draw_bars(screen, data)

        draw_bars(screen, data)
        #sort(screen, data)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()

