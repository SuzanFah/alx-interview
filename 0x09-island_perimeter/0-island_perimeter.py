#!/usr/bin/python3
"""Module that calculates the perimeter of an island in a grid."""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in grid.
    
    Args:
        grid (list of list): 2D list of integers representing an island
        
    Returns:
        The perimeter of the island
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all 4 sides
                # Top
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Bottom
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
