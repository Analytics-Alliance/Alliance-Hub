import pygame
import numpy as np

# Constants
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 30

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Elementary Cellular Automata Grid")
clock = pygame.time.Clock()

# Initialize the grid
grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)

def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = (255, 255, 255) if grid[x, y] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw grid lines
    for x in range(GRID_WIDTH + 1):
        pygame.draw.line(screen, (200, 200, 200), (x * CELL_SIZE, 0), (x * CELL_SIZE, WINDOW_HEIGHT))
    for y in range(GRID_HEIGHT + 1):
        pygame.draw.line(screen, (200, 200, 200), (0, y * CELL_SIZE), (WINDOW_WIDTH, y * CELL_SIZE))

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Toggle the cell state on mouse click
                mouse_x, mouse_y = event.pos
                grid_x = mouse_x // CELL_SIZE
                grid_y = mouse_y // CELL_SIZE
                if 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
                    grid[grid_x, grid_y] = 1 - grid[grid_x, grid_y]  # Toggle state

        # Draw the grid
        screen.fill((0, 0, 0))  # Clear the screen
        draw_grid()
        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()