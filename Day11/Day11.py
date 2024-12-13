# INITIAL THOUGHT PROCESS
"""
1.) Get input as list of stones
2.) Create function that processes the list of stones
3.) Set stones variable as returned list
4.) Run process for amount of blinks
5.) Return lenth of list of stones
"""
def foo(stones):
    new_stones = []
    index = 0
    for stone in stones:
        if stone == 0:
            new_stones.insert(index, 1)
        elif len(str(stone)) % 2 == 0:
            stone = str(stone)
            firstpart, secondpart = stone[:len(stone)//2], stone[len(stone)//2:]
            new_stones.insert(index, int(firstpart))
            index += 1
            new_stones.insert(index, int(secondpart))
        else:
            stone *= 2024
            new_stones.insert(index,stone)      
        index += 1
    return new_stones

# Imports
from pathlib import Path

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "example.txt"
input = TEXT_FILE.read_text()

# Get Input & Convert to ints
stones = input.split(' ')
stones = [int(stone) for stone in stones]

# Blink
blinks = 25
for i in range(blinks):
    stones = foo(stones)

print(f"Number of stones: {len(stones)}")