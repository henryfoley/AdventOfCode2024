# INITIAL THOUGHT PROCESS
"""
1.) Find '0' trailhead
2.) Extend frontier of trailheads nine times
3.) For each valid path add to a total
4.) Add total to list for each trailhead
5.) Sum the total of the list
"""

# Functions
def neighbors(grid, current):
    neighbors = []
    directions = ((0,-1),(0,1),(-1,0),(1,0))
    for direction in directions:
        neighbor_x = current[0] + direction[0]
        neighbor_y = current[1] + direction[1]
        neighbor = grid[neighbor_x][neighbor_y]
        if neighbor != -1:
            neighbors.append([neighbor_x,neighbor_y])
    return neighbors

# Imports
from pathlib import Path
import queue
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "example.txt"
input = TEXT_FILE.read_text()

# Create grid
regex_key = '.+'
rows = re.findall(regex_key, input, re.MULTILINE)
grid = [list(map(int, row)) for row in rows]

# Pad grid to prevent indexing errors
rows = len(grid)
cols = len(grid[0])
padded_grid = [[-1] * (cols+2)]
for row in grid:
    padded_grid.append([-1] + row + [-1])
padded_grid.append([-1] * (cols+2))


# Get trailhead coordinates in grid
trailhead_cords = []
for x, row in enumerate(padded_grid):
    for y, num in enumerate(row):
        if num == 0:
            trailhead_cords.append([x,y])

# BFS on grid using trailheads
for trailhead in trailhead_cords:
    print(f"Trailhead: {trailhead}")
    frontier = queue.Queue()
    frontier.put(trailhead)
    reached = set()
    reached.add(tuple(trailhead))

    while not frontier.empty():
        current = frontier.get()
        for next in neighbors(grid,current):
            frontier.put(next)
            reached.add(tuple(next))
   
print(f"First trailhead neighbors: {neighbors(padded_grid,trailhead_cords[0])}")
print(padded_grid)
print(trailhead_cords)