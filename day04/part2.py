import numpy as np
import re

with open("./day4.data") as data:
    rows = [list(r.strip()) for r in data.readlines()]
    grid = np.array(rows)

def safe(grid, x, y):
    return 0 < x < grid.shape[1]-1 and 0 < y < grid.shape[0]-1


def search(grid, x, y):

    poss = [
        [1,1, "S"],
        [1,-1, "S"],
        [-1,1, "M"],
        [-1,-1, "M"],
    ]

    if safe(grid, x, y):
        if grid[x][y] != "A":
            return 0
        
        if all([grid[x-dx][y-dy] == v for dx, dy, v in poss]):
            return 1

    return 0
    
total = 0

for i in range(4):
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            total += search(grid, x, y)
    grid = np.rot90(grid)

print(total)


