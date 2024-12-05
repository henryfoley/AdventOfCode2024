# INITIAL THOUGHT PROCESS
"""
1.) Load text file into 2D array
2.) Create function to access value of neighbor
3.) Start with first letter in array
4.) Search neighbors
5.) If neighbor is valid then search it's neighbor in the same direction
6.) If max length is reached then add to total count
7.) Report total
"""

# Imports
from pathlib import Path
import re

# Get contents of text file
ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "example.txt"
contents = TEXT_FILE.read_text()

# Regex
regex_key = 'mul\(*(\d+)\,(\d+)\)'
matches = re.findall(regex_key, contents, re.MULTILINE)

total = 0
print(contents)

