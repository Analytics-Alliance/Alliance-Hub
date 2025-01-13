import pygame
import numpy as np
from utils import update_grid  # Import the update_grid function from utils

# Constants
CELL_SIZE = 10
GRID_WIDTH = 80
GRID_HEIGHT = 60
WINDOW_WIDTH = CELL_SIZE * GRID_WIDTH
WINDOW_HEIGHT = CELL_SIZE * GRID_HEIGHT
FPS = 10  # Adjusted for a slower update rate

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()

# Initialize the grid with random states
grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT), p=[0.8, 0.2])  # 80% dead, 20% alive

def draw_grid(screen, grid, cell_size):
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            color = (255, 255, 255) if grid[x, y] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x * cell_size, y * cell_size, cell_size, cell_size))
    
    # Draw grid lines
    for x in range(grid.shape[0] + 1):
        pygame.draw.line(screen, (200, 200, 200), (x * cell_size, 0), (x * cell_size, grid.shape[1] * cell_size))
    for y in range(grid.shape[1] + 1):
        pygame.draw.line(screen, (200, 200, 200), (0, y * cell_size), (grid.shape[0] * cell_size, y * cell_size))

def main():
    global grid  # Declare grid as global to modify it within the function
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

        # Update the grid based on Conway's Game of Life rules
        grid = update_grid(grid)

        # Draw the grid
        screen.fill((0, 0, 0))  # Clear the screen
        draw_grid(screen, grid, CELL_SIZE)  # Call the draw_grid function

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate

    pygame.quit()

if __name__ == "__main__":
    main()