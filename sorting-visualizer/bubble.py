import pygame, random
from pygame.locals import * 
#data = [5, 1, 4, 2, 8, 10, 11, 1, 4, 2, 2, 2, 41, 101, 45]

black = (0, 0, 0)
green = (0, 255, 0)
size = (1000, 700)

def make_data(size, min, max):
    data = []
    for i in range(size):
        data.append(random.randint(min, max))
    return data

data = make_data(50, 10, 500)

def draw_bars(screen, array):
    screen.fill(black)
    bar_width = size[0] // len(array)
    for i in range(len(array)):
        bar_height = (array[i] / max(array)) * size[1] * 0.8
        pygame.draw.rect(screen, green, (i * bar_width, size[1] - bar_height, bar_width - 1, bar_height))
    pygame.display.update()

def sort(screen, data):
    for i in range(len(data) - 1):
        for j in range(len(data) - 1 - i):
            draw_bars(screen, data)
            pygame.time.delay(10)
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        draw_bars(screen, data)
        pygame.time.delay(10)
    draw_bars(screen, data)


def init():
    pygame.init()
    screen = pygame.display.set_mode(size)

    return screen

def game_loop(screen):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False


        sort(screen, data)

def main():
    screen = init()
    game_loop(screen)

    pygame.quit()

if __name__ == "__main__":
    main()

