# INITIAL THOUGHT PROCESS
"""
1.) Load text file into 2D array
    a.) Pad array to avoid index errors
2.) Create function to access value of neighbor
3.) Start with first letter in array
4.) Search neighbors
5.) If neighbor is valid then search it's neighbor in the same direction
6.) If word is found then add to total count
7.) Report total
"""

def search_neighbors(grid, start_row, start_col, word_goal, directions):
    total = 0
    for direction in directions:
        words = 'X'
        found = True
        # Iterate through the characters of `word_goal`
        for i in range(len(word_goal)):
            next_row = start_row + (direction[0] * (i + 1))
            next_col = start_col + (direction[1] * (i + 1))
                    
            # Check if the character matches the corresponding `word_goal` character
            if grid[next_row][next_col] != word_goal[i]:
                found = False
                break

            # Accumulate the matched character
            words += grid[next_row][next_col]
        if found and words == 'X' + word_goal:
                total += 1
                print(f"{words} found at ({start_row},{start_col}) in direction {direction}")
    return total

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
grid = [list(line) for line in lines]

# Pad grid to prevent indexing errors
rows = len(grid)
cols = len(grid[0])
padded_grid = [['H'] * (cols+2)]
for row in grid:
    padded_grid.append(['H'] + row + ['H'])
padded_grid.append(['H'] * (cols+2))

# Variables
directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1),   # Right
    (-1, -1), # Up-Left
    (-1, 1),  # Up-Right
    (1, -1),  # Down-Left
    (1, 1),   # Down-Right
]
word_goal = 'MAS'
total = 0

# Find X's in grid and then search neighbors for pattern
for y, row in enumerate(padded_grid):
    for x, letter in enumerate(row):
        if letter == 'X':
            print(f"X Found at: ({y},{x})")
            total += search_neighbors(padded_grid,y,x, word_goal, directions)

print(f"Total XMAS's Found: {total}")