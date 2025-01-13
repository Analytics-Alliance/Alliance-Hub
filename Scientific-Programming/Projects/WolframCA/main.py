import pygame
import numpy as np
from visuals import draw_grid  # Import the new visuals module

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

def update_grid():
    global grid
    new_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT), dtype=int)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            # Apply Wolfram's rule (e.g., Rule 30)
            left = grid[x - 1, y] if x > 0 else 0
            center = grid[x, y]
            right = grid[x + 1, y] if x < GRID_WIDTH - 1 else 0
            
            # Rule 30: 111 -> 0, 110 -> 0, 101 -> 0, 100 -> 1, 011 -> 1, 010 -> 1, 001 -> 1, 000 -> 0
            new_grid[x, y] = 1 if (left, center, right) in [(0, 0, 1), (0, 1, 0), (1, 0, 0), (1, 1, 0)] else 0

    grid = new_grid

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

        # Update the grid based on the cellular automata rules
        update_grid()

        # Draw the grid
        screen.fill((0, 0, 0))  # Clear the screen
        draw_grid(screen, grid, CELL_SIZE)  # Call the draw_grid function from visuals

        pygame.display.flip()  # Update the display
        clock.tick(FPS)  # Control the frame rate

    pygame.quit()

def foo():
    # Placeholder function for future implementation
    print("This is the foo function.")

if __name__ == "__main__":
    main()