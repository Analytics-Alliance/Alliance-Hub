import numpy as np

def update_grid(grid):
    new_grid = np.zeros_like(grid)
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            # Count live neighbors
            live_neighbors = np.sum(grid[max(0, x-1):min(x+2, grid.shape[0]), max(0, y-1):min(y+2, grid.shape[1])]) - grid[x, y]
            
            # Apply Conway's Game of Life rules
            if grid[x, y] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[x, y] = 0  # Dies
                else:
                    new_grid[x, y] = 1  # Lives
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[x, y] = 1  # Becomes alive

    return new_grid
