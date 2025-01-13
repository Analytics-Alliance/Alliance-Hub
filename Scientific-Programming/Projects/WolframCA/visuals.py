import pygame

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