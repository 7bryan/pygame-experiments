import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Insertion Sort Visualization")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)

# Generate random array
def generate_array(size, min_val, max_val):
    return [random.randint(min_val, max_val) for _ in range(size)]

# Draw bars
def draw_bars(array, current_index=None, comparing_index=None):
    screen.fill(BLACK)  # Clear screen
    bar_width = WIDTH // len(array)
    for i, val in enumerate(array):
        color = GREEN
        if i == current_index:
            color = BLUE
        elif i == comparing_index:
            color = ORANGE

        bar_height = (val / max(array)) * HEIGHT * 0.8 # Scale height
        pygame.draw.rect(screen, color, (i * bar_width, HEIGHT - bar_height, bar_width - 1, bar_height))
    pygame.display.update()

# Insertion Sort algorithm with visualization
def insertion_sort_visualized(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            draw_bars(array, i, j) # Visualize swap
            pygame.time.delay(10) # Control speed
            j -= 1
        array[j + 1] = key
        draw_bars(array, i) # Visualize insertion
        pygame.time.delay(10) # Control speed
    draw_bars(array) # Final sorted state

# Main loop
def main():
    array = generate_array(50, 10, 500)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN: # Start sorting on Enter
                    insertion_sort_visualized(array)
                if event.key == pygame.K_r: # Reset array on 'R'
                    array = generate_array(50, 10, 500)
                    draw_bars(array)

        #screen.fill(BLACK)
        draw_bars(array) # Initial draw

    pygame.quit()

if __name__ == "__main__":
    main()
