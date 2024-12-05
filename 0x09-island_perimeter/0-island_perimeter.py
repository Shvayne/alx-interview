#!/usr/bin/python3
"""THis module contains a function to calculate the perimeter of a grid"""

def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the given grid.
    
    Args:
        grid (List[List[int]]): A 2D grid where 0 is water and 1 is land
    
    Returns:
        int: The perimeter of the island
    """
    # Initialize perimeter
    perimeter = 0
    
    # Get grid dimensions
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Iterate through each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If current cell is land
            if grid[r][c] == 1:
                # Check all 4 adjacent sides
                # Top side
                if r == 0 or grid[r-1][c] == 0:
                    perimeter += 1
                
                # Bottom side
                if r == rows-1 or grid[r+1][c] == 0:
                    perimeter += 1
                
                # Left side
                if c == 0 or grid[r][c-1] == 0:
                    perimeter += 1
                
                # Right side
                if c == cols-1 or grid[r][c+1] == 0:
                    perimeter += 1
    
    return perimeter