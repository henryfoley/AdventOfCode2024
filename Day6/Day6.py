# INITIAL THOUGHT PROCESS
"""
1.) Load input into 2D array
2.) Get the start position within the array
3.) Iterate through 2D array in start direction
4.) Add visited spots to list
5.) If next spot is a wall then change direction
6.) Continue this pattern until exited array
7.) Report final count of visited spots

"""

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
input = TEXT_FILE.read_text()

# Regex
regex_key = '.+'
lines = re.findall(regex_key, input, re.MULTILINE)

grid = [tuple(line) for line in lines]

start_x = 0
start_y = 0

# Get start position
for index, line in enumerate(grid):
    # print(line)
    if '^' in line:
        start_x = line.index('^')
        start_y = index
        # print(f"Value ^ found in tuple {line} at row index {start_y} and column index {start_x}")

seeking = True
currentLocation_x = start_x
currentLocation_y = start_y
left = [0,-1]
right = [0,1]
up = [-1,0]
down = [1,0]
direction = up

visited_spots = set()  # Track visited spots
visited_spots.add((currentLocation_x, currentLocation_y))  # Add starting point

print(f"Grid Bounds are x: {len(grid[0])}, y:{len(grid)}")
while seeking == True:

    # Print Current Value
    # print(f"Value at ({currentLocation_y},{currentLocation_x}) is: {grid[currentLocation_y][currentLocation_x]}")

    # Check if current location is out of bounds
    if currentLocation_x < 0 or currentLocation_x >= len(grid[0]) or currentLocation_y < 0 or currentLocation_y >= len(grid):
        seeking = False
        break

    # Calculate the next location
    next_x = currentLocation_x + direction[1]
    next_y = currentLocation_y + direction[0]

    # Check if next location is out of bounds
    if next_x < 0 or next_x >= len(grid[0]) or next_y < 0 or next_y >= len(grid):
        # print("Next location out of bounds. Stopping.")
        seeking = False
        break

    # Check for wall
    if grid[next_y][next_x] == '#':
        # print(f"Hit Wall at ({next_y},{next_x}) is: {grid[next_y][next_x]} ")
        if direction == up:
            direction = right
        elif direction == right:
            direction = down
        elif direction == down:
            direction = left
        elif direction == left:
            direction = up
        continue

    # Update location
    currentLocation_x = next_x
    currentLocation_y = next_y

    # Increment visited count
    if (currentLocation_x, currentLocation_y) not in visited_spots:
        visited_spots.add((currentLocation_x, currentLocation_y))

print(f"Total Spots Visited: {len(visited_spots)}")