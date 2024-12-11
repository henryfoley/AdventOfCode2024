# INITIAL THOUGHT PROCESS
"""
1.) Create list of keys (indexes and numbers)
2.) If the index of key is even then add number to a block
3.) If the index of the key is odd then add '.' to a block
4.) Iterate over the block and replace '.' with valid numbers
5.) Append the processed letter to the new block
6.) Find checksum of new block
"""

# Imports
from pathlib import Path

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
input = TEXT_FILE.read_text()

keys = []
index = -1

# Iterate over each character in the input string and add it to a list of keys
for num in input:
    current_num = int(num)
    index += 1
    keys.append([index,current_num])

block = []
i = 0

# Process each key in the `keys` list to build the `block` list
for key in keys:
    if key[0] % 2 == 0:
        for x in range(key[1]):
            block.append(str(i))
        i += 1
    else:
       for x in range(key[1]):
            block.append('.')

# Initialize the offset to point to the end of the block
offset = len(block) - 1
new_block = []

# Iterate over the `block` list and replace '.' with valid numbers. Append the processed letter to the new block
for j, letter in enumerate(block):
    if letter == '.':
        while block[offset] == '.':
            offset -= 1
        block[j] = block[offset]
        block[offset] = 'x'
        offset -=1
    if letter == 'x':
        break
    new_block.append(block[j])

# Calculate the total by iterating over the new block
total = 0
for y, num in enumerate(new_block):
    total += y * int(num)

print(f"Final Total: {total}")