# INITIAL THOUGHT PROCESS
"""
1.) Load text file into 2D array
2.) Create function to access value of neighbor
3.) If neighbor is valid 
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
