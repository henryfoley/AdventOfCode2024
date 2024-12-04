# INITIAL THOUGHT PROCESS
"""
1.) Extract all number pairs within 'mul(,)
2.) Multiply all the number sets
3.) Add each of their sums
"""

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "input.txt"
contents = TEXT_FILE.read_text()

# Regex
regex_key = 'mul\(*(\d+)\,(\d+)\)'
matches = re.findall(regex_key, contents, re.MULTILINE)

column_1 = []
column_2 = []

for match in matches:
    column_1.append(int(match[0]))
    column_2.append(int(match[1]))

if len(column_1) != len(column_2):
    print("Number sets are not the same length")
    exit()

total = 0

for i in range(len(column_1)):
    total += column_1[i] * column_2[i]

print(total)