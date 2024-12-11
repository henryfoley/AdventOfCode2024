# INITIAL THOUGHT PROCESS
"""
1.) Create list of keys (indexes and numbers)
2.) If the index of key is even then add number to a block
3.) If the index of the key is odd then add '.' to a block
4.) Iterate over the block and replace '.' with valid numbers
5.) Append the processed letter to the new block
6.) Find checksum of new block
"""

# # Imports
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
total = sum(i*int(num) for i,num in enumerate(new_block))


print(f"Final Total: {total}")

from collections import deque


lengths = [int(num) for num in input]

filled_grid = deque()
moved_grid = deque()
gaps = deque()

cur_pos = 0
for i,num in enumerate(lengths):
    if i%2 == 0:
        filled_grid.append([i//2,cur_pos,num])
    else:
        if num > 0:
            gaps.append([cur_pos,num])
    cur_pos += num

while True:
    gap_pos,gap_len = gaps.popleft()
    file_id,file_pos,file_len = filled_grid.pop()
    if gap_pos > file_pos:
        filled_grid.append([file_id,file_pos,file_len])
        break
    if gap_len > file_len:
        moved_grid.append([file_id,gap_pos,file_len])
        gaps.appendleft([gap_pos+file_len,gap_len-file_len])
    elif gap_len == file_len:
        moved_grid.append([file_id,gap_pos,file_len])
    else:
        moved_grid.append([file_id,gap_pos,gap_len])
        filled_grid.append([file_id,file_pos,file_len-gap_len])
    
final_grid = filled_grid + moved_grid
answer = sum(num*(start*length+(length*(length-1))//2) for num,start,length in final_grid) # (start) + (start+1) + ... + (start+length-1)
print(answer)