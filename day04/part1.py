import numpy as np
import re

with open("./day4.data") as data:
    rows = [list(r.strip()) for r in data.readlines()]
    grid = np.array(rows)

def safe(grid, x, y):
    return 0 <= x < grid.shape[1] and 0 <= y < grid.shape[0]


offsets = [
    [0, 1],
    [1, 0],
    [1, 1],
    [0, -1],
    [-1, 0],
    [-1, -1],
    [-1, 1],
    [1, -1],
]
def search(grid, x, y):
    if grid[x][y] in ["A", "M"]:
        return 0

    seqs = ["" for _ in range(8)]
    for i in range(4):
        for j, offset in enumerate(offsets):
            dx = offset[0]*i
            dy = offset[1]*i
            if safe(grid, x+dx, y+dy):
                seqs[j] += grid[x+dx][y+dy]
    
    return sum([1 if s == "XMAS" else 0 for s in seqs])

    
total = 0

for x in range(grid.shape[0]):
    for y in range(grid.shape[1]):
        total += search(grid, x, y)

print(total)


